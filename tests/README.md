# Tests — regression guard

The review is model-driven, so these tests guard the **structural invariants** of
a produced `review-state` — the drift we have actually hit (a separate
`recommendations[]` creeping back, an opinion line in the matter block, issues
missing their position/fallback, blown caps).

## Naming convention
- `*.review-state.json` — **golden**, well-formed fixtures. These gate a release
  (`tools/release.sh` runs the guard over them; all must PASS).
- `*.bad-state.json` — **negative** fixtures, deliberately broken. Run manually to
  confirm the guard still bites; they are NOT part of the release gate.

## Run
```bash
# golden (must all pass)
python tools/check_review_state.py tests/fixtures/*.review-state.json

# negative (must fail — proves the guard works)
python tools/check_review_state.py tests/fixtures/*.bad-state.json
```

- `acme.review-state.json` → PASS.
- `regressed.bad-state.json` → FAIL (separate `recommendations[]`, an
  `overall_read` opinion, an issue missing `fallback`).

Exit code is `0` only if every checked file passes. WARNINGs (caps, brevity) are
printed but never fail the run.

## How this fits the workflow
- The `review` skill's **Self-check before delivering** lists the same invariants
  for the model to eyeball at generation time.
- `check_review_state.py` is the deterministic backstop; `tools/release.sh` runs it
  over the golden fixtures on every release.

## Adding a fixture
Drop a `*.review-state.json` (golden) or `*.bad-state.json` (negative) in
`fixtures/`. For a negative case, note here which ERROR it exercises.
