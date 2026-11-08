# Live Rhino 8 acceptance, macOS, Foton 0.3.6, 8 November 2026

Commit `22bd6e6`, Foton 0.3.6, Rhino 8.35.26251.13002 on macOS 26.6.2 (Apple M4 Pro, Metal), the same Ladybug Tools install as the [0.3.5 checklist](../2026-11-05-rhino-macos-0.3.5/README.md), Radiance 5.4a. `22bd6e6` holds the Grasshopper components and both example definitions, rebuilt in Rhino 8.35 with `scripts/build_grasshopper.py`. It adds the new Foton Interactive Demo, and its components build the embedded bridge once per Rhino session and skip the progress redraw for live runs that end within 0.25 s. The engine (`python/`, `crates/`) is the same as at `e200cfc`, where the 0.3.6 Vulkan suite ran. Rhino was driven through McNeel's Rhino MCP router 0.4.0.

Every Foton call in the checks used `/Users/ssanjay/GitHub/foton-0.3.6/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.6 built from this tree: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py` and as `executable_` for the Honeybee, Ladybug and demo steps. The install tests used scratch `FOTON_HOME` folders, set in Rhino's IronPython `os.environ` so the components saw them. `~/.foton` was not changed.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.6-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` and Rhino restarted (`yak list` shows foton 0.3.6; the installed definitions and user objects are byte-identical to the build). The HB-Foton category has one "Foton" group with all four components, each with an icon, not obsolete, loaded from the 0.3.6 package, and each description names Foton 0.3.6. Foton Settings' `install_`, using the toggle wired in the First Analysis example, was run inside Rhino into a scratch folder, with pip pointed at the local 0.3.6 wheel. It installs in the background, stops cleanly when switched off mid-install (no pip process left), carries on at the next toggle, ends at "0.3.6 / metal" after 9 s, and says "Foton 0.3.6 is already installed" when toggled again |
| install (failure and uv) | With `PIP_INDEX_URL` at an unreachable URL and no find-links, `install_` turns Settings red ("Install failed"). `report` shows pip's error, the exit code (1), the command to rerun in a terminal and the log path, and `install.log` and `pip.log` are written in `FOTON_HOME`. `python_ = "uv"` takes the uv route even with Python 3.12 installed: it downloaded uv and Python 3.12.16 and installed 0.3.6 in 45 s (capabilities: 0.3.6, metal, ready), run outside Rhino from the bundle's `foton_gh` |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.6.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.6 on Metal. open_example also covered the new **Foton Interactive Demo.gh**, opened from the installed package (see below) |
| honeybee_metrics | `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the bundle's shoebox example. It returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings. The run manifest reports engine 0.3.6 on Metal. In the demo, Save run and HB Annual Daylight Metrics agreed on all 240 sensors (largest DA difference 0.00 %) |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh (`HB Load Objects` into `HB Get Grids and Views`), with no errors or warnings. `HB Load Objects` warned that the example's model schema (2.4.0) is newer than the installed Honeybee's (2.2.0), and loaded it. The demo's DA and DF heatmaps also drew without warnings |

## Foton Interactive Demo (new in 0.3.6)

**Foton Interactive Demo.gh** was opened from `packages/8.0/foton/0.3.6/` with no earlier saved runs on disk. It opened and solved on the first try: Foton Settings showed "0.3.6 / metal", and sDA with the default room was 53.75 %. The only message was HB Annual Daylight Metrics' warning that `_results` had no data, which is expected until the first Save run.

- Dragging the room width, south window-to-wall ratio, overhang and DA threshold sliders updated DA each time.
- Neighbour block on: sDA dropped to 25 %.
- Daylight factor on: Foton Daylight Factor, its heatmap and its panel unlocked, giving a mean DF of 1.50 %. Turning it off locked them again, with no warnings either way.
- 3 floors of 4 rooms solved in about 10 s with no errors.
- Save run: Foton Annual Results and HB Annual Daylight Metrics read the saved run, and the comparison panel reported "240 sensors, largest DA difference 0.00 %". After that the canvas had no errors or warnings.

Slider timings in this session, measured after the automated checks and the Honeybee steps had run: 0.46–0.63 s for a geometry move and 0.32–0.44 s for a threshold move. In a freshly started Rhino with only the demo open, the same moves measured 0.17–0.21 s and about 0.07 s.

Not covered: a fresh Rhino profile, Windows, the Package Manager window and hover tooltips by eye (checked through Grasshopper's component server instead), `install_` against the published PyPI release (0.3.6 was not on PyPI yet), ESC during a run, and the 0.3.5 check of flipping `_run` during a run, which was not repeated.
