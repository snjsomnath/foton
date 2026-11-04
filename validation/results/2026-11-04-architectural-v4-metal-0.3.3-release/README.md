# Metal suite on the 0.3.3 release commit, judged against the published references

Commit `eda816c` (branch `release-0.3.3`, clean checkout, Foton 0.3.3), 2026-11-04,
5.7 minutes on an Apple M4 Pro, Radiance 5.4a. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked), the same references the 0.3.0, 0.3.1 and 0.3.2 suites were
judged against.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.2, in the same classes
([`known-open-cases.json`](../../known-open-cases.json)).
The coefficient, annual, darkness and sky-bin sections of every case are
identical to the [0.3.2 release run](../2026-11-04-architectural-v4-metal-0.3.2-release/README.md)
on all 212 cases, as are each case's settings, outcomes and result class. The
Rust engine is unchanged since 0.3.2; 0.3.3 changes the Grasshopper
components, packaging and installer.

The only other differences from 0.3.2 are the version strings (each case's
sky version reads `foton-sky-r1 (foton-daylight 0.3.3)` and its solver version
0.3.3) and the diagnostic stock-recipe comparison of the `acceptance` model,
which reruns Honeybee's stock Radiance recipe each time and so varies from run
to run (largest metric change under 2.3 percentage points; `passed: false` in
every release, not a gate).

The run used a fresh venv outside the checkout with exactly the dependency
versions of the 0.3.1 and 0.3.2 runs (honeybee-core 1.64.61, honeybee-radiance
1.66.281, ladybug-geometry 1.35.1, lbt-recipes 0.28.8, numpy 2.1.0; the full
list is in `suite.json`), with `foton-daylight` 0.3.3 built from this commit
(`maturin develop --release`, the abi3 native module) and the 0.3.3 sources
first on `PYTHONPATH`. `suite.json` records the native module path and
`engine_version` 0.3.3.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`. The arrays stayed on the machine.
