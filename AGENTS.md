# CursorCult Project Context

This directory represents the **CursorCult** GitHub organization, a collection of opinionated Cursor rule packs and the tooling to manage them.

## 📂 Organization Structure

The repositories are categorized into **Infrastructure** (prefixed with `_` or `.`) and **Rule Packs**.

### 🏗️ Infrastructure Repositories

These repositories power the ecosystem, tooling, and governance.

*   **`_CursorCult`**: The flagship repository. Contains:
    *   The `cursorcult` CLI tool (Python).
    *   Canonical documentation.
    *   The source for the documentation website.
*   **`.github`**: Organization-wide health files and the public profile README (`profile/README.md`), which serves as the landing page.
*   **`_intake`**: The submission queue. New rules/benchmarks are proposed here via "Metadata PRs" (YAML files).
*   **`_rulesets`**: A registry of named collections of rules (e.g., `JDev.txt`).
*   **`_results`**: Stores benchmark results (`RESULTS.md`) and pins versions of benchmarks and metrics.
*   **`_metrics`**: Reusable metric scripts (e.g., code coverage) for benchmarks.
*   **`_benchmark_<RULE>`**: Benchmarking harnesses for specific rules (e.g., `_benchmark_TDD`).
*   **`CursorCult.github.io`**: The organization's GitHub Pages site (currently redirects to the GitHub profile).

### 📦 Rule Packs

Each of these directories is a standalone repository defining a specific engineering rule. They follow a strict format.

*   **Examples**: `TDD`, `DRY`, `PAPER`, `UNO`, `PUTTPUTT`, etc.
*   **Standard File Structure**:
    *   `RULE.md`: The rule definition (Cursor rule format).
    *   `README.md`: Human-readable documentation, installation instructions, and "Why".
    *   `LICENSE`: The Unlicense (Public Domain).
    *   `.github/workflows/ccverify.yml`: CI workflow to verify repo compliance.

## 🛠️ The `cursorcult` CLI

The `_CursorCult` repo contains the Python-based CLI tool used to manage these rules.

**Key Commands:**
*   `cursorcult list`: List all available rule packs in the org.
*   `cursorcult link <NAME>`: Install a rule pack into the current project's `.cursor/rules/` directory (as a submodule).
*   `cursorcult update`: Update installed rules to their latest compliant versions.
*   `cursorcult register <URL>`: Generate a submission YAML for a new rule.
*   `cursorcult verify`: specific check to ensure a rule repo follows the standard format.
*   Publishing: `_CursorCult` has `.github/workflows/publish.yml` that auto-publishes to PyPI on push to `main` when `pyproject.toml` version lacks a matching `vX.Y.Z` tag. It builds, publishes via trusted publishing, and then tags.

## 🏷️ Versioning Policy

*   **`v0` (Volatile)**: Development channel. Tags move; implies "latest bleeding edge".
*   **`v1+` (Stable)**: Immutable release tags. Updates are explicit.

## 🧪 Rule Repo Version/Testing Policy

Rule repos use separate test branches to avoid `vN` tag/branch ambiguity.

*   **Tags (`vN`)** live on `main` only. `main` contains exactly one commit per version tag.
*   **Test branches (`tN`)** contain full tests and `requirements-test.txt`.
*   `tests/` and `requirements-test.txt` must never appear on `main`.
*   `requirements-test.txt` may only include `cursorcult` and `pytest`.
*   Each `tN` branch must still be a valid rule repo after removing `tests/` and `requirements-test.txt`.
*   For `v1+`, the `vN` tag must match the tip of the `tN` branch, excluding `tests/` and `requirements-test.txt`.
*   Once `v1` exists, `t0` must be fully merged into `main`.

## 🧰 Reusable Workflows

*   **`test-rule.yml`**: reusable workflow to run `pytest` on `t*` branches.
*   **`mint-rule.yml`**: reusable workflow to mint `vN` from `tN`:
    *   runs tests and `cursorcult verify`,
    *   builds a clean `main` snapshot,
    *   force-updates `main` and tags `vN`.

## 🔄 Workflows

1.  **Creating a Rule**: Use `cursorcult new <NAME>` (maintainers) or `cursorcult register` (community).
2.  **Updating the Registry**: PRs to `_intake` trigger automation to update the central `registry.json`.
3.  **Showcase Generation**: The `.github/scripts/update_rules_lists.py` script generates the list of rules in the profile README, including stars and benchmark badges.
