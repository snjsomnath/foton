# Teaching category under Seattle weather (overcast)

Commit `fc3aafd`, 2026-11-02 21:51 UTC, 32 minutes with 12 Radiance workers on an M4 Pro. Radiance 5.4a, `epw/seattle.epw` (Seattle-Tacoma TMY3, see [`epw/README.md`](../../../epw/README.md)), `final` preset: 256 direct samples per patch, 65,536 indirect samples at MF:1 and 262,144 at MF:2, 8 bounces. Same gates as the full campaigns. The report marks the checkout `dirty`: while this run followed the Phoenix run unattended, documentation files and `scripts/run_honeybee_annual_reference.py` (not used by this suite) were being edited; no engine, scene or suite code differed from `fc3aafd`. Suite status is `incomplete` because the run selects one category of the 106 scenes.

**Result: 32 of 32 cases passed** (16 teaching scenes × MF:1, MF:2), 0 accuracy failures, 0 unstable references, 0 errors.

| | Gothenburg ([run 2](../2026-11-02-architectural-v4-metal-run2/README.md)) | Phoenix ([run](../2026-11-02-teaching-climate-phoenix/README.md)) | **Seattle** |
| --- | ---: | ---: | ---: |
| Cases passed | 32 / 32 | 32 / 32 | **32 / 32** |
| Annual energy bias, median / worst | 0.06 % / 0.51 % | 0.07 % / 0.64 % | **0.05 % / 0.60 %** |
| Hourly CV(RMSE), median / worst | 1.42 % / 3.95 % | 1.59 % / 3.12 % | **1.43 % / 3.58 %** |
| Worst metric mean error (DA, cDA, UDI) | 0.56 pp | 0.91 pp | **0.48 pp** |

Seattle behaves like Gothenburg: the overcast sky matrix spreads energy over many patches, per-patch noise averages out, and the worst grids are again `teaching_obstruction60` and `teaching_reflectance70`. The sDA table and the climate discussion are in the Phoenix README; Seattle's column there shows the lower daylight availability (depth 6 m room 94 % instead of 100 %, WWR 20 % room 50 % instead of 64 % in Gothenburg) that Foton and Radiance agree on.

## Files

`suite.json` holds every case's full report; `suite.md` the status table; per case `report.md`, `coefficient_comparison.{json,md}` and `converged_annual.json`. Raw stage folders, coefficient matrices and the weather cache (5 GB) stay on the machine that ran it.
