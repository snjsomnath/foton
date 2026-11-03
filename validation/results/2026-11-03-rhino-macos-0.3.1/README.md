# Live Rhino 8 acceptance, macOS, Foton 0.3.1, 3 November 2026

Commit `80694dd` (release-0.3.1), Foton 0.3.1, Rhino 8.35.26251.13002 on macOS 26.6 (Apple M4 Pro, Metal), Ladybug Tools 1.9.0, Radiance 5.4a. The Grasshopper bundle was `dist/foton-grasshopper-0.3.1.zip` built by `scripts/package_grasshopper.py`.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | The bundle's three `.ghuser` files are byte-identical to the ones already installed for 0.3.0, so they were not copied again; the component server lists all three under `HB-Foton` |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` run inside Rhino against the extracted bundle: seven automated checks, all true, in `rhino-smoke.json`; the Settings component reported engine 0.3.1 on Metal |
| honeybee_metrics | `HB Annual Daylight Metrics` read Foton's results folder for the bundle's shoebox example and returned DA identical to Foton's own output on all 36 sensors |
| ladybug_heatmap | `LB Spatial Heatmap` built its mesh and 36 colours from those values with no errors or warnings |

Not covered: a fresh Rhino profile, a fresh UserObjects install and Windows.
