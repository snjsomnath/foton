# Teaching category under Phoenix weather (sunny)

Commit `fc3aafd` (clean checkout), 2026-11-02 21:19 UTC, 32 minutes with 12 Radiance workers on an M4 Pro. Radiance 5.4a, `epw/phoenix.epw` (Phoenix Sky Harbor TMY3, see [`epw/README.md`](../../../epw/README.md)), `final` preset: 256 direct samples per patch, 65,536 indirect samples at MF:1 and 262,144 at MF:2, 8 bounces. Same gates as the full campaigns. Suite status is `incomplete` because the run selects one category of the 106 scenes; the suite only calls a complete run `passed`.

**Result: 32 of 32 cases passed** (16 teaching scenes × MF:1, MF:2), 0 accuracy failures, 0 unstable references, 0 errors.

| | Gothenburg ([run 2](../2026-11-02-architectural-v4-metal-run2/README.md)) | **Phoenix** | Seattle ([run](../2026-11-02-teaching-climate-seattle/README.md)) |
| --- | ---: | ---: | ---: |
| Cases passed | 32 / 32 | **32 / 32** | 32 / 32 |
| Annual energy bias, median / worst | 0.06 % / 0.51 % | **0.07 % / 0.64 %** | 0.05 % / 0.60 % |
| Hourly CV(RMSE), median / worst | 1.42 % / 3.95 % | **1.59 % / 3.12 %** | 1.43 % / 3.58 % |
| Worst metric mean error (DA, cDA, UDI) | 0.56 pp | **0.91 pp** | 0.48 pp |

The worst grids are the same in every climate: `teaching_obstruction60` (a 60° obstruction leaves the room lit by a sliver of sky, so few patches carry the light) and `teaching_reflectance70` (the most inter-reflection). Phoenix's sharper sky matrix, with most of the energy in the solar patches, raises the worst metric error from 0.5 to 0.9 pp and otherwise changes nothing: Foton and converged `rfluxmtx` smear the sun the same way, so this run tests parity under a peaky sky, not the direct-sun decision. That decision is quantified separately against a traced sun in [`2026-11-02-teaching-sun-vs-stock/`](../2026-11-02-teaching-sun-vs-stock/README.md).

What the climate does to the answers a course would read off, sDA (Foton / Radiance) at MF:1:

| Scene | Gothenburg | Phoenix | Seattle |
| --- | ---: | ---: | ---: |
| depth 4 m | 100 / 100 | 100 / 100 | 100 / 100 |
| depth 6 m | 100 / 100 | 100 / 100 | 94 / 94 |
| depth 8 m | 62 / 62 | 73 / 75 | 58 / 58 |
| depth 10 m | 50 / 50 | 55 / 55 | 43 / 45 |
| WWR 20 % | 64 / 64 | 83 / 83 | 50 / 50 |
| WWR 60 % | 100 / 100 | 100 / 100 | 100 / 100 |
| overhang 1.0 m | 69 / 67 | 100 / 94 | 61 / 61 |
| obstruction 60° | 11 / 11 | 28 / 31 | 11 / 11 |

Where the two engines differ by 2–6 pp the grid has 36 sensors (2.8 pp each) and the differing sensors sit within the 5 pp ambiguity band around the 50 % DA threshold, which the sDA gate excludes.

## Files

`suite.json` holds every case's full report; `suite.md` the status table; per case `report.md`, `coefficient_comparison.{json,md}` and `converged_annual.json`. Raw stage folders, coefficient matrices and the weather cache (5 GB) stay on the machine that ran it.
