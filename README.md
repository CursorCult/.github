# CursorCult `.github`

This repository powers **organization-wide defaults** for the CursorCult GitHub org, and serves as the landing zone for shared docs.

## What this repo is for

- **Org profile README**: see `profile/README.md` (renders on https://github.com/CursorCult)
- **Shared GitHub “community health” files** (as we add them): PR templates, issue templates, contributing docs, etc.
- **Pointers to rule packs** hosted in the org
- **Cursor links**: https://cursor.com and rule format docs

## CursorCult rule packs

Small, opinionated rule packs you can mix-and-match per project:

- [`_CursorCult`](https://github.com/CursorCult/_CursorCult) — CLI + canonical docs (start here)
- [`TDD`](https://github.com/CursorCult/TDD) — test-first workflow
- [`SpecsFirst`](https://github.com/CursorCult/SpecsFirst) — write the contract before the code
- [`DesignToTest`](https://github.com/CursorCult/DesignToTest) — design for testability
- [`NoMocksNoSkips`](https://github.com/CursorCult/NoMocksNoSkips) — prefer real tests over mocks/skip
- [`LimitMocks`](https://github.com/CursorCult/LimitMocks) — when you *must* mock, keep it tight
- [`NoDeadCode`](https://github.com/CursorCult/NoDeadCode) — keep the repo alive and prunable
- [`DRY`](https://github.com/CursorCult/DRY) — duplication is a design smell
- [`RAII`](https://github.com/CursorCult/RAII) — resource lifetime discipline (esp. systems code)
- [`TruthOrSilence`](https://github.com/CursorCult/TruthOrSilence) — say what you know; don’t guess
- [`NoHedging`](https://github.com/CursorCult/NoHedging) — remove weasel words, commit to claims
- [`EzGrep`](https://github.com/CursorCult/EzGrep) — write code that’s easy to search and refactor
- [`UMP`](https://github.com/CursorCult/UMP), [`UNO`](https://github.com/CursorCult/UNO), [`PUTTPUTT`](https://github.com/CursorCult/PUTTPUTT), [`Pinocchio`](https://github.com/CursorCult/Pinocchio) — specialty packs

Browse the org repos: https://github.com/CursorCult

Quick start (CLI):

```sh
pipx install cursorcult
cursorcult
```

Cursor docs for rule files: https://cursor.com/docs/context/rules#rulemd-file-format

## License

Released into the public domain under the Unlicense. See `LICENSE`.
