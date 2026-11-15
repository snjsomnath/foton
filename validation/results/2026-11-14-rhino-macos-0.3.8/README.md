# Live Rhino 8 acceptance, macOS, Foton 0.3.8, 14 November 2026

Commit `16e9459`, Foton 0.3.8, Rhino 8.35.26251.13002 on macOS 26.6.2 (Apple M4 Pro, Metal), the same Ladybug Tools install (1.9.0) as the [0.3.7 checklist](../2026-11-10-rhino-macos-0.3.7/README.md), Radiance 5.4a. `16e9459` holds the Grasshopper components and both example definitions, rebuilt in Rhino 8.35 with `scripts/build_grasshopper.py` for 0.3.8. It is also the commit the 0.3.8 [Metal suite](../2026-11-14-architectural-v4-metal-0.3.8-release/README.md) ran on. Rhino was driven through McNeel's Rhino MCP router, with IronPython scripts run by `_-RunPythonScript`. Everything was run on 14 November, in three freshly started Rhinos: one for the install tests, one for the automated checks and the demo, one for the Honeybee and Ladybug steps.

Every Foton call outside the install tests used `/Users/ssanjay/GitHub/foton-0.3.8/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.8 installed from the wheel built from a clean clone of this branch: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py`, the demo and the Honeybee and Ladybug steps. The install tests used scratch `FOTON_HOME` folders, set in Rhino's IronPython `os.environ` so the components saw them. `~/.foton` was not changed.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.8-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` while Rhino was closed (`yak list` shows foton 0.3.8; the installed package is byte-identical to the `.yak`, and its definitions and user objects to the build). The HB-Foton category has one "Foton" group with all four components, each with an icon, not obsolete, loaded from the 0.3.8 package, and each description names Foton 0.3.8. Foton Settings' `install_`, using the toggle wired in the First Analysis example, was run inside Rhino into a scratch folder, with pip pointed at the local 0.3.8 wheel. It installs in the background, stops cleanly when switched off after 12 s (no pip process left for that folder), carries on at the next toggle, ends at "0.3.8 / metal" 15 s later, and says "Foton 0.3.8 is already installed" when toggled again |
| install (failure and uv) | With `PIP_INDEX_URL` at an unreachable URL and no find-links, `install_` turns Settings red ("Install failed"). `report` shows pip's error, the exit code (1), the command to rerun in a terminal and the log path, and `install.log` and `pip.log` are written in `FOTON_HOME`. `python_ = "uv"` takes the uv route even with Python 3.12 installed: it downloaded uv 0.13.8 and Python 3.12.16 and installed 0.3.8 in 26 s (capabilities: 0.3.8, metal, ready), run outside Rhino from the bundle's `foton_gh` |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.8.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.8 on Metal. open_example also covered **Foton Interactive Demo.gh**, opened from the installed package (see below) |
| honeybee_metrics | In a freshly started Rhino, `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the package's shoebox example. It returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings. The run manifest reports engine 0.3.8 with Metal selected. In the demo, Save run and HB Annual Daylight Metrics agreed on all 240 sensors (largest DA difference 0.00 %) |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh (`HB Load Objects` into `HB Get Grids and Views`), with no errors or warnings on any of the three |

For the last two steps, First Analysis was read into a Grasshopper document with `GH_Archive`, as `check_grasshopper.py` does. The Honeybee and Ladybug components were created from Grasshopper's component server and wired by script. That was a workaround: opening a definition in the Grasshopper window through the router stopped responding twice at that point. It had worked earlier in the session for the install tests and the demo.

## Foton Interactive Demo

**Foton Interactive Demo.gh** was opened from `packages/8.0/foton/0.3.8/`. The runs saved during the 0.3.7 check were still on disk (`~/foton_simulation/interactive_demo`, `interactive_demo-001`). It opened and solved on the first try: Foton Settings showed "0.3.8 / metal", sDA with the default room was 53.75 % (as in 0.3.7), and no component had errors or warnings.

- Moving the room width, south window-to-wall ratio, overhang and DA threshold sliders updated DA each time.
- Neighbour block on: sDA dropped to 25 %.
- Daylight factor on: Foton Daylight Factor unlocked, giving a mean DF of 1.50 %. Turning it off locked it again, with no warnings either way.
- 3 floors of 4 rooms solved in 1.5 s with no errors.
- Save run wrote a new 0.3.8 run (`interactive_demo-002`). Foton Annual Results and HB Annual Daylight Metrics read it, and the comparison panel reported "240 sensors, largest DA difference 0.00 %". After that the canvas had no errors or warnings.

Slider timings in this session, solved through the Grasshopper SDK rather than by dragging on the canvas: 0.39 s for the first geometry move (warm-up), then 0.07–0.09 s for geometry and threshold moves, and 0.19 s for the neighbour block.

Not covered: a fresh Rhino profile, Windows, the Package Manager window and hover tooltips by eye (checked through Grasshopper's component server instead), `install_` against the published PyPI release (0.3.8 is not on PyPI yet), ESC during a run, and flipping `_run` during a run.
