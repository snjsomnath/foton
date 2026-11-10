# Live Rhino 8 acceptance, macOS, Foton 0.3.7, 9–10 November 2026

Commit `536fa73`, Foton 0.3.7, Rhino 8.35.26251.13002 on macOS 26.6.2 (Apple M4 Pro, Metal), the same Ladybug Tools install (1.9.0) as the [0.3.6 checklist](../2026-11-08-rhino-macos-0.3.6/README.md), Radiance 5.4a. `536fa73` holds the Grasshopper components and both example definitions, rebuilt in Rhino 8.35 with `scripts/build_grasshopper.py` for 0.3.7. It is also the commit the 0.3.7 [Metal suite](../2026-11-09-architectural-v4-metal-0.3.7-release/README.md) ran on. Rhino was driven through McNeel's Rhino MCP router. The install, the automated checks and the demo were run on 9 November, the Honeybee and Ladybug steps on 10 November, each in a freshly started Rhino.

Every Foton call outside the install tests used `/Users/ssanjay/GitHub/foton-0.3.7/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.7 installed from the wheel built from a clean clone of this commit: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py`, the demo and the Honeybee and Ladybug steps. The install tests used scratch `FOTON_HOME` folders, set in Rhino's IronPython `os.environ` so the components saw them. `~/.foton` was not changed.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.7-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` and Rhino restarted (`yak list` shows foton 0.3.7; the installed package is byte-identical to the `.yak`, and its definitions and user objects to the build). The HB-Foton category has one "Foton" group with all four components, each with an icon, not obsolete, loaded from the 0.3.7 package, and each description names Foton 0.3.7. Foton Settings' `install_`, using the toggle wired in the First Analysis example, was run inside Rhino into a scratch folder, with pip pointed at the local 0.3.7 wheel. It installs in the background, stops cleanly when switched off mid-install (no pip process left), carries on at the next toggle, ends at "0.3.7 / metal" in under 27 s, and says "Foton 0.3.7 is already installed" when toggled again |
| install (failure and uv) | With `PIP_INDEX_URL` at an unreachable URL and no find-links, `install_` turns Settings red ("Install failed"). `report` shows pip's error, the exit code (1), the command to rerun in a terminal and the log path, and `install.log` and `pip.log` are written in `FOTON_HOME`. `python_ = "uv"` takes the uv route even with Python 3.12 installed: it downloaded uv and Python 3.12.16 and installed 0.3.7 in 30 s (capabilities: 0.3.7, metal, ready), run outside Rhino from the bundle's `foton_gh` |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.7.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.7 on Metal. open_example also covered **Foton Interactive Demo.gh**, opened from the installed package (see below) |
| honeybee_metrics | In a freshly started Rhino, `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the package's shoebox example. It returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings. The run manifest reports engine 0.3.7 with Metal selected. In the demo, Save run and HB Annual Daylight Metrics agreed on all 240 sensors (largest DA difference 0.00 %) |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh (`HB Load Objects` into `HB Get Grids and Views`), with no errors or warnings on any of the three. The 0.3.6 checklist saw a schema-version warning from `HB Load Objects` here; this time there was none |

## Foton Interactive Demo

**Foton Interactive Demo.gh** was opened from `packages/8.0/foton/0.3.7/`. Unlike the 0.3.6 check, the run saved during that check was still on disk (`~/foton_simulation/interactive_demo`), so the saved-run half of the demo started from it. It opened and solved on the first try: Foton Settings showed "0.3.7 / metal", sDA with the default room was 53.75 % (as in 0.3.6), and no component had errors or warnings.

- Moving the room width, south window-to-wall ratio, overhang and DA threshold sliders updated DA each time.
- Neighbour block on: sDA dropped to 25 %.
- Daylight factor on: Foton Daylight Factor unlocked, giving a mean DF of 1.50 %. Turning it off locked it again, with no warnings either way.
- 3 floors of 4 rooms solved in 1.6 s with no errors.
- Save run wrote a new 0.3.7 run (`interactive_demo-001`). Foton Annual Results and HB Annual Daylight Metrics read it, and the comparison panel reported "240 sensors, largest DA difference 0.00 %". After that the canvas had no errors or warnings.

Slider timings in this session, solved through the Grasshopper SDK rather than by dragging on the canvas: 0.44 s for the first geometry move (warm-up), then 0.07–0.09 s for geometry and threshold moves, and 0.18 s for the neighbour block.

Not covered: a fresh Rhino profile, Windows, the Package Manager window and hover tooltips by eye (checked through Grasshopper's component server instead), `install_` against the published PyPI release (0.3.7 is not on PyPI yet), ESC during a run, and flipping `_run` during a run.
