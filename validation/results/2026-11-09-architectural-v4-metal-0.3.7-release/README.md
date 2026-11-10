# Metal suite on the 0.3.7 release commit, judged against the published references

Commit `536fa73` (branch `claude/project-thread-d6uhm6`, clean clone, Foton 0.3.7), 2026-11-09,
6.5 minutes on an Apple M4 Pro, Radiance 5.4a. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked), the same references every suite since 0.3.0 was judged against.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.3, in the same classes
([`known-open-cases.json`](../../known-open-cases.json)).
Each case's settings, outcomes and result class match the
[0.3.3 release run](../2026-11-04-architectural-v4-metal-0.3.3-release/README.md).

`coefficient_comparison.{json,md}` and `converged_annual.json` are
byte-identical to the 0.3.3 run in 211 of 212 cases. The exception is the
`acceptance` model at MF:2. The engine change in 0.3.7 is the Honeybee
adapter's triangulation of planar faces (#62), which presumably moves some of
that model's triangles by rounding-level amounts. There, 7 values in `converged_annual.json` and 20 in
`coefficient_comparison.json` differ in their last digits, by at most 1.4e-5
relative (largest absolute change 4.5e-6 lux, in a median error). The `.md`
tables, rounded for display, do not change. A second run on the same build
was byte-identical to the first.

Each case's version strings now read 0.3.7. The diagnostic stock-recipe
comparison of the `acceptance` model reruns Honeybee's stock Radiance recipe
each time and so varies from run to run (`passed: false` in every release, not
a gate).

The run used a fresh venv outside the checkout with exactly the dependency
versions of the 0.3.3 run (honeybee-core 1.64.61, honeybee-radiance 1.66.281,
ladybug-geometry 1.35.1, lbt-recipes 0.28.8, numpy 2.1.0; the full list is in
`suite.json`), with `foton-daylight` 0.3.7 built from this commit
(`maturin develop --release`, the abi3 native module) and the 0.3.7 sources
first on `PYTHONPATH`. `suite.json` records the native module path and
`engine_version` 0.3.7.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`. The arrays stayed on the machine.
