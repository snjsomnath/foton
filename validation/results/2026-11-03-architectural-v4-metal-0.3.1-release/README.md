# Metal suite on the 0.3.1 release commit, judged against the published references

Commit `80694dd` (branch `release-0.3.1`, clean checkout, Foton 0.3.1), 2026-11-03,
5.9 minutes on an Apple M4 Pro, Radiance 5.4a. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked), the same references the 0.3.0 suites were judged against.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.0, in the same classes.
The coefficient, annual, darkness and sky-bin sections of every case's report
are identical to the [0.3.0 release run](../2026-11-03-architectural-v4-metal-0.3.0-release/README.md)
on all 212 cases. That is expected: 0.3.1 only changes how Metal keeps each
room's geometry resident, which matters for models with a few hundred rooms,
and the largest corpus scene has far fewer.

The run used the same Python environment as the 0.3.0 release run (the same
Honeybee, Ladybug and lbt-recipes versions), with the 0.3.1 sources and native
module from this commit put first on `PYTHONPATH`; `suite.json` records the
native module path and `engine_version` 0.3.1. The package metadata of that
environment still reads `foton-daylight` 0.3.0, which is the only dependency
difference from the 0.3.0 run.

A first attempt in a freshly created venv picked up newer Honeybee and Ladybug
releases (honeybee-core 1.64.81, honeybee-radiance 1.66.301, ladybug-geometry
1.35.7) and no lbt-recipes. There, `sealed` MF:2 read 0.001 lux instead of
dark and the stock recipe on the acceptance model could not run. That run is
not evidence for this release; it is a note that the suite depends on the
pinned Ladybug Tools versions.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`.
