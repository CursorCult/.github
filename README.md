# CursorCult `.github`

This repository powers **organization-wide defaults** for the CursorCult GitHub org, and serves as the landing zone for shared docs.

## What this repo is for

- **Org profile README**: see `profile/README.md` (renders on https://github.com/CursorCult)
- **Shared GitHub “community health” files** (as we add them): PR templates, issue templates, contributing docs, etc.
- **Pointers to rule packs** hosted in the org
- **Cursor links**: https://cursor.com and rule format docs

## CursorCult rule packs

Small, opinionated rule packs you can mix-and-match per project. The canonical list lives in the org profile at https://github.com/CursorCult.

<!-- RULES:START -->
<!-- Auto-generated. Edits will be overwritten. -->

- [DesignToTest](https://github.com/CursorCult/DesignToTest/blob/v0/RULE.md) `v0` — Design interfaces for rapid, isolated testing
- [DRY](https://github.com/CursorCult/DRY/blob/v0/RULE.md) `v0` — Do not repeat yourself (DRY), a classic rule for reducing code duplication
- [EzGrep](https://github.com/CursorCult/EzGrep/blob/v0/RULE.md) `v0` — Optimize naming for grep/ack-based code search
- [LimitMocks](https://github.com/CursorCult/LimitMocks/blob/v0/RULE.md) `v0` — Prefer real dependencies; use mocks sparingly
- [NoDeadCode](https://github.com/CursorCult/NoDeadCode/blob/v0/RULE.md) `v0` — Forbid dead, unused, or unreachable code
- [NoHedging](https://github.com/CursorCult/NoHedging/blob/v0/RULE.md) `v0` — Avoid hedged defaults; require explicit, validated data
- [NoMocksNoSkips](https://github.com/CursorCult/NoMocksNoSkips/blob/v0/RULE.md) `v0` — Forbid mocks and skipped tests; require real systems
- [Pinocchio](https://github.com/CursorCult/Pinocchio/blob/v0/RULE.md) `v0` — Reduce the risk of doc rot, i.e. current truths become future lies
- [PUTTPUTT](https://github.com/CursorCult/PUTTPUTT/blob/v0/RULE.md) `v0` — Enforce total test coverage through public-only tests
- [RAII](https://github.com/CursorCult/RAII/blob/v0/RULE.md) `v0` — Require constructors to fully acquire resources and establish invariants
- [SpecsFirst](https://github.com/CursorCult/SpecsFirst/blob/v0/RULE.md) `v0` — Write specs first; keep spec/design/code in sync
- [TDD](https://github.com/CursorCult/TDD/blob/v0/RULE.md) `v0` — Practice test-driven development (write tests first)
- [TruthOrSilence](https://github.com/CursorCult/TruthOrSilence/blob/v0/RULE.md) `v0` — Delete false internal prose; truth or silence
- [UMP](https://github.com/CursorCult/UMP/blob/v0/RULE.md) `v0` — Simple naming scheme where private entities are prefixed with an underscore
- [UNO](https://github.com/CursorCult/UNO/blob/v0/RULE.md) `v0` — Enforce one definition per file in source code
<!-- RULES:END -->

## How to contribute

### Propose a new repo (rule, benchmark, tooling)

Use the intake repo:

- https://github.com/CursorCult/_intake

Submit a PR with one YAML file under `submissions/` describing:

- `CursorCult/<rule>` rule pack repos (repos that don’t start with `.` or `_`)
- `_benchmark_<RULE>` benchmark repos (show results improving across `v0`, `v1`, `v2`, …)
- `_benchmark_<RULESET>` benchmark repos (benchmarks a named ruleset)

### Rulesets

Rulesets are registered in:

- https://github.com/CursorCult/_rulesets

Each ruleset is `rulesets/<NAME>.txt` with newline-separated rule names (no versions).

Eligibility requirement: rules referenced by rulesets must have a `v1` tag.

### Using rulesets (CLI)

```sh
pipx install cursorcult
cursorcult link --ruleset <NAME>
```

Browse the org repos: https://github.com/CursorCult

Quick start (CLI):

```sh
pipx install cursorcult
cursorcult
```

Cursor docs for rule files: https://cursor.com/docs/context/rules#rulemd-file-format

## License

Released into the public domain under the Unlicense. See `LICENSE`.
