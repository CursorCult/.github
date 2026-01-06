# NEXT priorities for WKS: A Roadmap of Sorts

## Consolidate Utils into Config Domain [P1]

**Why**: Move all `wks/utils` and `wks/api/utils` code to `wks/api/config` to achieve strict `wks/api/<domain>` behavior and better structure. This ensures all API code follows the domain-based organization pattern and eliminates the top-level utils directory.

**Status**: In progress (PR #55). See PR description for detailed task list and migration plan.

- [ ] Audit all files in `wks/utils/` and `wks/api/utils/`
- [ ] Move utility functions to `wks/api/config/` (or appropriate domain if domain-specific)
- [ ] Update all imports across the codebase
- [ ] Remove `wks/utils/` and `wks/api/utils/` directories
- [ ] Update documentation to reflect new structure
- [ ] Verify all tests still pass after migration

## Roll Out tN/vN Test Strategy + Mint Workflow [P1]

**Why**: Remove tag/branch ambiguity, enforce clean `main`, and standardize release minting with CI gates.

- [ ] Migrate remaining rule repos to `tN` test branches (tests + `requirements-test.txt`)
- [ ] Ensure `main` only has `vN` tags and no tests/test requirements
- [ ] Adopt reusable `test-rule.yml` and `mint-rule.yml` workflows
- [ ] Update KISS, DRY, and YAGNI to follow the new strategy

## Implement Diff (bsdiff and Meyers) [P2]

- [ ] Scope design and baseline requirements
