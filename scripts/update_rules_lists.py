#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Iterable


ORG_DEFAULT = "CursorCult"
MARKER_START = "<!-- RULES:START -->"
MARKER_END = "<!-- RULES:END -->"
SHOWCASE_START = "<!-- SHOWCASE:START -->"
SHOWCASE_END = "<!-- SHOWCASE:END -->"


@dataclass(frozen=True)
class Repo:
    name: str
    description: str | None
    default_branch: str


@dataclass(frozen=True)
class GitHubApiError(RuntimeError):
    status: int
    url: str
    body: str


def _github_token_optional() -> str | None:
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    return token.strip() if token else None


def _request_json(url: str, token: str | None) -> tuple[Any, dict[str, str]]:
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "CursorCult-Readme-Updater")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return json.loads(raw), headers
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8")
        except Exception:
            pass
        raise GitHubApiError(status=e.code, url=url, body=body) from e


def _paginate(url: str, token: str | None) -> Iterable[Any]:
    while url:
        data, headers = _request_json(url, token)
        if not isinstance(data, list):
            raise RuntimeError(f"Expected list response for {url}, got {type(data)}")
        for item in data:
            yield item
        link = headers.get("link", "")
        next_url = None
        for part in link.split(","):
            part = part.strip()
            if not part:
                continue
            if 'rel="next"' in part:
                m = re.search(r"<([^>]+)>", part)
                if m:
                    next_url = m.group(1)
                break
        url = next_url


def list_rule_repos(org: str, token: str | None) -> list[Repo]:
    url = f"https://api.github.com/orgs/{urllib.parse.quote(org)}/repos?per_page=100&type=public"
    repos: list[Repo] = []
    for item in _paginate(url, token):
        name = item.get("name") or ""
        if not name or name.startswith(".") or name.startswith("_"):
            continue
        if item.get("fork") is True:
            continue
        if item.get("archived") is True:
            continue
        default_branch = item.get("default_branch") or "main"
        description = item.get("description")
        if isinstance(description, str):
            description = description.strip() or None
        else:
            description = None
        repos.append(Repo(name=name, description=description, default_branch=default_branch))

    repos.sort(key=lambda r: r.name.casefold())
    return repos


_TAG_RE = re.compile(r"^v(\d+)$")


def latest_rule_tag(org: str, repo: str, token: str | None) -> str | None:
    url = f"https://api.github.com/repos/{urllib.parse.quote(org)}/{urllib.parse.quote(repo)}/tags?per_page=100"
    best: tuple[int, str] | None = None
    for item in _paginate(url, token):
        name = item.get("name")
        if not isinstance(name, str):
            continue
        m = _TAG_RE.match(name.strip())
        if not m:
            continue
        n = int(m.group(1))
        if best is None or n > best[0]:
            best = (n, name.strip())
    return best[1] if best else None


def rule_md_exists(org: str, repo: str, ref: str, token: str | None) -> bool:
    url = (
        f"https://api.github.com/repos/{urllib.parse.quote(org)}/{urllib.parse.quote(repo)}"
        f"/contents/RULE.md?ref={urllib.parse.quote(ref)}"
    )
    try:
        _request_json(url, token)
        return True
    except GitHubApiError as e:
        if e.status == 404:
            return False
        raise


def build_rules_markdown(org: str, repos: list[Repo], token: str | None) -> str:
    lines: list[str] = []
    for repo in repos:
        tag = latest_rule_tag(org, repo.name, token)
        ref = tag or repo.default_branch
        link = f"https://github.com/{org}/{repo.name}/blob/{ref}/RULE.md"
        if not rule_md_exists(org, repo.name, ref, token):
            link = f"https://github.com/{org}/{repo.name}"

        label = f"`{tag}`" if tag else "`unreleased`"
        desc = f" — {repo.description}" if repo.description else ""
        lines.append(f"- [{repo.name}]({link}) {label}{desc}")
    return "\n".join(lines) + ("\n" if lines else "")


def fetch_registry() -> dict[str, Any]:
    url = "https://raw.githubusercontent.com/CursorCult/_intake/main/registry.json"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Warning: Failed to fetch registry: {e}", file=sys.stderr)
        return {{}}

def fetch_github_stars(url: str, token: str | None) -> int | None:
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)", url)
    if not m: return None
    owner, repo = m.groups()
    repo = repo.replace(".git", "")
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        data, _ = _request_json(api_url, token)
        return data.get("stargazers_count")
    except Exception:
        return None

def check_benchmark(rule_name: str, token: str | None) -> str | None:
    # Return link to results if exists
    path = f"rules/{rule_name}/python/RESULTS.md"
    url = f"https://api.github.com/repos/CursorCult/_results/contents/{path}"
    try:
        _request_json(url, token)
        return f"https://github.com/CursorCult/_results/blob/main/{path}"
    except Exception:
        return None

def build_showcase_markdown(registry: dict[str, Any], token: str | None) -> str:
    lines = []
    candidates = []
    for key, entry in registry.items():
        if entry.get("license") == "Unlicense" and not entry.get("archived", False):
            candidates.append(entry)
    
    candidates.sort(key=lambda x: x["name"].lower())
    
    for entry in candidates:
        name = entry["name"]
        desc = entry.get("description") or ""
        url = entry.get("source_url") or ""
        maint = entry.get("maintainer") or "?"
        
        stars = fetch_github_stars(url, token)
        star_badge = f" ⭐ {stars}" if stars is not None else ""
        
        bench_link = check_benchmark(name, token)
        bench_badge = f" [🏆 Benchmark]({bench_link})" if bench_link else ""
        
        line = f"- [{name}]({url}){star_badge}{bench_badge} — {desc} (by @{maint})"
        lines.append(line)
        
    return "\n".join(lines) + ("\n" if lines else "")


def replace_between_markers(contents: str, replacement: str, start_marker: str, end_marker: str) -> str:
    start = contents.find(start_marker)
    end = contents.find(end_marker)
    if start == -1 or end == -1 or end < start:
        return contents

    end += len(end_marker)
    before = contents[:start]
    after = contents[end:]

    block = (
        f"{start_marker}\n"
        f"<!-- Auto-generated. Edits will be overwritten. -->\n\n"
        f"{replacement}"
        f"{end_marker}"
    )
    if not block.endswith("\n"):
        block += "\n"

    return before + block + after.lstrip("\n")


def update_file(path: str, rules_md: str, showcase_md: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            original = f.read()
    except FileNotFoundError:
        return False

    current = original
    current = replace_between_markers(current, rules_md, MARKER_START, MARKER_END)
    current = replace_between_markers(current, showcase_md, SHOWCASE_START, SHOWCASE_END)
    
    if current == original:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(current)
    return True

def main(argv: list[str]) -> int:
    org = os.getenv("CURSORCULT_ORG", ORG_DEFAULT)
    token = _github_token_optional()

    target_files = argv[1:] if len(argv) > 1 else ["README.md", "profile/README.md"]
    
    # 1. Build Org Rules List
    repos = list_rule_repos(org, token)
    rules_md = build_rules_markdown(org, repos, token)
    
    # 2. Build Community Showcase
    registry = fetch_registry()
    showcase_md = build_showcase_markdown(registry, token)

    changed_any = False
    for path in target_files:
        if update_file(path, rules_md, showcase_md):
            print(f"updated: {path}")
            changed_any = True
        else:
            print(f"unchanged: {path}")

    if not changed_any:
        print("no changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))