# CursorCult

> Opinionated Cursor rules and writing practices for building software that stays readable under pressure.

<p align="center">
  <img alt="CursorCult" src="https://img.shields.io/badge/Focus-Clarity-blue" />
  <img alt="CursorCult" src="https://img.shields.io/badge/Style-Testable-green" />
  <img alt="CursorCult" src="https://img.shields.io/badge/Defaults-Strong-purple" />
</p>

## ⚡ Quick start

- `_CursorCult` (CLI + canonical docs): https://github.com/CursorCult/_CursorCult
- Install: `pipx install cursorcult` (then run `cursorcult`)
- Cursor (the editor): https://cursor.com

## 🧭 What you’ll find

- **Rule packs**: focused, composable sets of Cursor rules you can drop into a repo
- **Style constraints**: bias toward clarity, testability, and fast refactors
- **Strong defaults**: fewer “maybe”s, more executable intent

## 🛠️ How to use

1. Pick a pack from https://github.com/CursorCult
2. Add its rules to your project (commonly under `.cursor/rules/`)
3. Tune per-repo: keep the rules short, enforceable, and aligned with your team

## 📦 Rule packs

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

## 🌟 Why CursorCult

- **Readable under pressure:** rules are written to keep teams aligned even when timelines are tight.
- **Composable defaults:** mix and match packs to fit your stack without carrying dead weight.
- **Practice > prose:** every rule favors habits that are testable and enforceable, not aspirational.

## 🤝 Contributing

PRs that make rules **clearer, smaller, and more enforceable** are welcome. If you’re proposing a new pack, keep it narrow and name it after the constraint it enforces.

## 📝 License

Unlicense / public domain. See the org `.github` repo for details.
