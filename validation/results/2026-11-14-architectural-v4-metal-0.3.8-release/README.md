# Metal suite on the 0.3.8 release commit, judged against the published references

Commit `16e9459` (branch `claude/project-thread-1f1b9e`, clean clone, Foton 0.3.8), 2026-11-14,
6.0 minutes on an Apple M4 Pro, Radiance 5.4a. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked), the same references every suite since 0.3.0 was judged against.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.3 and 0.3.7, in the same classes
([`known-open-cases.json`](../../known-open-cases.json)).
Each case's settings, outcomes and result class match the
[0.3.7 release run](../2026-11-09-architectural-v4-metal-0.3.7-release/README.md).

`coefficient_comparison.{json,md}` and `converged_annual.json` are
byte-identical to the 0.3.7 run in all 212 cases. That is expected: the change
in 0.3.8 is an optional `engine=` argument to `HoneybeeStudy` (#67), which the
suite does not pass. Every case's sensor grid still matches the reference
(`sensor_grid_sha256_matches` in all 212).

Outside the timings, each `report.md` differs from 0.3.7 only in the version
strings (now 0.3.8), the bundle and scene paths, and `model_sha256`, which
changes from run to run in every campaign because the exported HBJSON is
regenerated each time. The diagnostic stock-recipe comparison of the
`acceptance` model reruns Honeybee's stock Radiance recipe each time and so
varies from run to run (`passed: false` in every release, not a gate).

The run used a fresh venv outside the checkout with exactly the dependency
versions of the 0.3.7 run (honeybee-core 1.64.61, honeybee-radiance 1.66.281,
ladybug-geometry 1.35.1, lbt-recipes 0.28.8, numpy 2.1.0; the full list is in
`suite.json`), with `foton-daylight` 0.3.8 built from this clone
(`maturin develop --release`, the abi3 native module) and the 0.3.8 sources
first on `PYTHONPATH`. `suite.json` records the native module path and
`engine_version` 0.3.8.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`. The arrays stayed on the machine.
