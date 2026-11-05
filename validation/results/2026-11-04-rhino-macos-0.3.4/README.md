# Live Rhino 8 acceptance, macOS, Foton 0.3.4, 4 November 2026

Commit `cc972d8` (release-0.3.4), Foton 0.3.4, Rhino 8.35.26251.13002 on macOS 26.6.2 (Apple M4 Pro, Metal), the same Ladybug Tools install as the [0.3.3 checklist](../2026-11-04-rhino-macos-0.3.3/README.md), Radiance 5.4a. `cc972d8` holds the Grasshopper components rebuilt in Rhino 8.35 with `scripts/build_grasshopper.py` from the 0.3.4 version bump (`45fdf68`). 0.3.4 changes only the components (#43), so the 0.3.3 Metal and Vulkan suites still stand. Rhino was driven through McNeel's Rhino MCP router 0.4.0.

Every Foton call in the checks used `/Users/ssanjay/GitHub/foton-0.3.4/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.4 built from this tree: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py` and as `executable_` for the Honeybee and Ladybug steps. The install tests used scratch `FOTON_HOME` folders, so `~/.foton` was not touched.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.4-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` and Rhino restarted (`yak list` shows foton 0.3.4). The HB-Foton category has one "Foton" group with all four components, each with an icon, loaded from the 0.3.4 package. Canvas search for "Foton" finds all four, and each shows 0.3.4. Foton Settings' `install_`, using the toggle now wired in the example, was run inside Rhino into a scratch folder, with pip pointed at the local 0.3.4 wheel. It installs in the background while Rhino stays usable, stops cleanly when switched off mid-install, carries on at the next toggle, ends at "0.3.4 / metal", and says "already installed" when toggled again |
| install (new in 0.3.4) | With `PIP_INDEX_URL` at an unreachable URL and no find-links, `install_` turns Settings red ("Install failed"). `report` shows pip's error, the exit code (1), the command to rerun in a terminal and the log path, and `install.log` and `pip.log` are written in `FOTON_HOME`. `python_ = "uv"` takes the uv route even with Python 3.12 installed: it downloaded uv and Python 3.12.16 and installed 0.3.4 in 86 s, run outside Rhino from the same code |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.4.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.4 on Metal |
| honeybee_metrics | `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the bundle's shoebox example. It returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh (`HB Load Objects` into `HB Get Grids and Views`), with no errors or warnings. `HB Load Objects` warned that the example's model schema (2.4.0) is newer than the installed Honeybee's (2.2.0), and loaded it |

Not covered: a fresh Rhino profile, Windows, the Package Manager window and hover tooltips by eye (checked through Grasshopper's component server instead), and `install_` against the published PyPI release (0.3.4 was not on PyPI yet).
