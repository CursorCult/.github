# NEXT priorities for CursorCult: A Roadmap of Sorts

## Roll Out tN/vN Test Strategy + Mint Workflow [P1]

**Why**: Remove tag/branch ambiguity, keep `main` minimal, and standardize release minting with CI gates.

- [ ] Migrate remaining rule repos to `tN` branches (tests + `requirements-test.txt`)
- [ ] Ensure `main` only has `vN` tags and no tests/test requirements
- [ ] Adopt reusable `test-rule.yml` and `mint-rule.yml` workflows everywhere
- [ ] Update KISS, DRY, and YAGNI to follow the new strategy

## Publish CursorCult 0.14.6+ and Validate Pipx Flow [P1]

**Why**: `cursorcult test` is part of the core workflow and must work with the default install.

- [ ] Verify PyPI has the latest `cursorcult` version
- [ ] Validate `pipx install --python python3.12 cursorcult` supports `cursorcult test`

## UNO: Confirm New Evaluate Output + t0 CI [P2]

**Why**: UNO is the trailblazer for the new workflows and output format.

- [ ] Confirm domain-by-domain output format in `evaluate.py`
- [ ] Confirm `t0` CI runs via the reusable workflow
