# Live Rhino 8 acceptance, macOS, 3 November 2026

Commit `f65030f`, Foton 0.3.0, Rhino 8.35.26251.13002 on macOS 26.6 (Apple M4 Pro, Metal), Ladybug Tools 1.9.0, Radiance 5.4a. The Grasshopper bundle was `dist/foton-grasshopper-0.3.0.zip` built by `scripts/package_grasshopper.py` from the committed, round-trip-tested `.ghuser` files.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | The three `.ghuser` files were copied into Grasshopper's UserObjects folder; the component server found all three under `HB-Foton / Recipes` |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` run inside Rhino against the extracted bundle: seven automated checks, all true, in `rhino-smoke.json` |
| honeybee_metrics | `HB Annual Daylight Metrics` read Foton's results folder and returned DA identical to Foton's own output on all 36 sensors |
| ladybug_heatmap | `LB Spatial Heatmap` coloured the model's sensor-grid mesh from those values; screenshots in `docs/images/` |

Not covered: a fresh Rhino profile (an existing profile with Ladybug Tools was used) and Windows. The release notes say so.
