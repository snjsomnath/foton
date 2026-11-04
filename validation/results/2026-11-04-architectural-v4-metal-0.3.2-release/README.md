# Metal suite on the 0.3.2 release commit, judged against the published references

Commit `3101ba1` (branch `release-0.3.2`, clean checkout, Foton 0.3.2), 2026-11-04,
6.0 minutes on an Apple M4 Pro, Radiance 5.4a. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked), the same references the 0.3.0 and 0.3.1 suites were judged
against.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.1, in the same classes
([`known-open-cases.json`](../../known-open-cases.json)).
The coefficient, annual, darkness and sky-bin sections of every case are
identical to the [0.3.1 release run](../2026-11-03-architectural-v4-metal-0.3.1-release/README.md)
on all 212 cases, as are each case's settings, outcomes and result class.

What changed between the two runs:

- Every case now records a `sky_sources` section: the candidate ran with
  Foton's own Perez sky (`foton-sky-r1 (foton-daylight 0.3.2)`), the default
  in 0.3.2. The solver version in each `candidate` section reads 0.3.2.
- The stock-recipe comparison of the `acceptance` model (`stock_comparison/`,
  both sky densities) moved slightly, because Foton's Honeybee path now builds
  its annual sky with the built-in sky instead of `gendaymtx`. It is a
  diagnostic comparison with the stock Honeybee recipe, not a gate; it reads
  `passed: false` in 0.3.1 and 0.3.2 alike. The largest metric changes are
  under 2 percentage points (for example `office_01` UDI at MF:1, 53.37 to
  51.81 pp maximum error, and `classroom_01` cDA, 0.0 to 0.07 pp).

The run used a fresh venv in the release worktree with exactly the
dependency versions of the 0.3.1 run (honeybee-core 1.64.61,
honeybee-radiance 1.66.281, ladybug-geometry 1.35.1, lbt-recipes 0.28.8,
numpy 2.1.0, the full list in `suite.json`), with `foton-daylight` 0.3.2
installed editable from this commit and the 0.3.2 sources first on
`PYTHONPATH`. `suite.json` records the native module path and
`engine_version` 0.3.2; unlike the 0.3.1 run, the package metadata also reads
`foton-daylight` 0.3.2.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`. The arrays stayed on the machine.
