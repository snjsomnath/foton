# Live Rhino 8 acceptance, macOS, Foton 0.3.5, 5 November 2026

Commit `967462c`, Foton 0.3.5, Rhino 8.35.26251.13002 on macOS 26.6.2 (Apple M4 Pro, Metal), the same Ladybug Tools install as the [0.3.4 checklist](../2026-11-04-rhino-macos-0.3.4/README.md), Radiance 5.4a. `967462c` holds the Grasshopper components rebuilt in Rhino 8.35 with `scripts/build_grasshopper.py` from the 0.3.5 version bump (`4f2a1c5`). 0.3.5 changes only the components, so the 0.3.3 Metal and Vulkan suites still stand. Rhino was driven through McNeel's Rhino MCP router 0.4.0.

Every Foton call in the checks used `/Users/ssanjay/GitHub/foton-0.3.5/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.5 built from this tree: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py` and as `executable_` for the Honeybee and Ladybug steps. The install tests used scratch `FOTON_HOME` folders. `~/.foton` was upgraded separately from 0.3.1 to the same 0.3.5 wheel.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.5-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` and Rhino restarted (`yak list` shows foton 0.3.5). The HB-Foton category has one "Foton" group with all four components, each with an icon, loaded from the 0.3.5 package. Canvas search for "Foton" finds all four, and each shows 0.3.5. Foton Settings' `install_`, using the toggle wired in the example, was run inside Rhino into a scratch folder, with pip pointed at the local 0.3.5 wheel. It installs in the background while Rhino stays usable, stops cleanly when switched off mid-install, carries on at the next toggle, ends at "0.3.5 / metal", and says "already installed" when toggled again |
| install (failure and uv) | With `PIP_INDEX_URL` at an unreachable URL and no find-links, `install_` turns Settings red ("Install failed"). `report` shows pip's error, the exit code (1), the command to rerun in a terminal and the log path, and `install.log` and `pip.log` are written in `FOTON_HOME`. `python_ = "uv"` takes the uv route even with Python 3.12 installed: it downloaded uv and Python 3.12.16 and installed 0.3.5 in 32 s, run outside Rhino from the same code |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.5.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.5 on Metal |
| honeybee_metrics | `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the bundle's shoebox example. It returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh (`HB Load Objects` into `HB Get Grids and Views`), with no errors or warnings. `HB Load Objects` warned that the example's model schema (2.4.0) is newer than the installed Honeybee's (2.2.0), and loaded it |

## Flipping `_run` during a run (new in 0.3.5)

The example was open on the canvas with `reuse_` set to False. Foton Annual Daylight was started by double-clicking its `_run` toggle, and about a second into the run (Grasshopper in its Process phase, Foton tracing) `_run` was double-clicked again. The same was then done on Foton Daylight Factor. The clicks were real AppKit mouse events posted to Rhino's event queue at the toggle's position on screen. A posted double-click flips an idle toggle, so this method is known to work. The runs on this machine take about 1.5 to 2 s, so each click landed during the run.

| Check | Annual Daylight | Daylight Factor |
| --- | --- | --- |
| The run finishes without "object expired during a solution" | yes, "Complete" | yes, "Complete" |
| The canvas is locked (`Enabled` False) during the run | yes | yes |
| The click is ignored | **no** | **no** |
| The canvas is usable after the run | yes | yes |
| ESC still cancels | not tested | not tested |

On macOS the click is not ignored, only held back. Grasshopper's canvas still receives the mouse events while it is disabled and applies the double-click as soon as the solution ends and the canvas is unlocked. `_run` then flips back to False and the component solves again with `_run` off, which clears its outputs on the canvas (the results stay on disk). The 0.3.4 components, which do not lock the canvas, behave the same way here. Neither showed "object expired during a solution", so the Windows volunteer's error did not reproduce on macOS and this check cannot show whether 0.3.5 fixes it. That needs Windows.

ESC was not tested. The screen was locked during the session, so no window could take keyboard focus and posted ESC key events never reached Rhino, even when it was idle. The automated `cancel` check above stops a run through Foton's own cancel path, not through the ESC key.

Not covered: a fresh Rhino profile, Windows, the Package Manager window and hover tooltips by eye (checked through Grasshopper's component server instead), `install_` against the published PyPI release (0.3.5 was not on PyPI yet), and ESC during a run.
