# Live Rhino 8 acceptance, macOS, Foton 0.3.2, 4 November 2026

Commit `3101ba1` (release-0.3.2), Foton 0.3.2, Rhino 8.35.26251.13002 on macOS 26.6 (Apple M4 Pro, Metal), the same Ladybug Tools install as the [0.3.1 checklist](../2026-11-03-rhino-macos-0.3.1/README.md), Radiance 5.4a. The Grasshopper bundle was `dist/foton-grasshopper-0.3.2.zip` built by `scripts/package_grasshopper.py` (its build check passed, so no rebuild in Rhino was needed). It has four components: Foton Settings, Foton Annual Daylight, Foton Annual Results and the new Foton Daylight Factor.

Every step used `/Users/ssanjay/GitHub/foton-release-0.3.2/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.2 installed editable into a fresh venv in the release worktree. It was passed as `FOTON_HONEYBEE_EXE` to `check_grasshopper.py` and connected to `executable_` for the Honeybee and Ladybug steps. The usual `~/.foton/venv` was moved aside during the checks so no other build could be picked up.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | The bundle's four `.ghuser` files were copied into the Grasshopper UserObjects folder, replacing the ones there. Those were already byte-identical (checked with `cmp`), so Grasshopper did not need a restart |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` run inside Rhino against the extracted bundle: ten automated checks, all true, in `rhino-smoke.json`. New since 0.3.1: `daylight_factor` (the Daylight Factor component runs and returns DF), `live_matches_saved` (live mode returns the saved run's DA and DF and writes nothing) and `live_reuses_coefficients` (a threshold change in live mode reuses the traced coefficients, `coefficient_trace_seconds: 0.0`; timings in `live_timings`). The Settings component reported engine 0.3.2 on Metal, and every run manifest reports engine 0.3.2 (the moved folder's manifest carries the check's deliberate `older-test-version` stamp) |
| honeybee_metrics | `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the bundle's shoebox example and returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh, with no errors or warnings |

Not covered: a fresh Rhino profile, a fresh UserObjects install and Windows.
