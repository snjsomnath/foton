# Live Rhino 8 acceptance, macOS, Foton 0.3.3, 4 November 2026

Commit `eda816c` (release-0.3.3), Foton 0.3.3, Rhino 8.35.26251.13002 on macOS 26.6 (Apple M4 Pro, Metal), the same Ladybug Tools install as the [0.3.2 checklist](../2026-11-04-rhino-macos-0.3.2/README.md), Radiance 5.4a. The components are the Grasshopper build committed at `5a2ad44`, built in Rhino 8.35; the release commit changes only a CI workflow after it. They now use Rhino 8's IronPython 2 Script component (no "OLD" badge), and the build checks that every port tooltip, component description and icon survives a save and reload.

Every Foton call in the checks used `/Users/ssanjay/GitHub/foton-0.3.3/.venv/bin/foton-honeybee`, `foton-daylight` 0.3.3 built from this tree: as `FOTON_HONEYBEE_EXE` for `check_grasshopper.py` and connected to `executable_` for the Honeybee and Ladybug steps. The install tests used scratch `FOTON_HOME` folders, so `~/.foton` was not touched.

`rhino-evidence.json` is the checklist the release verifier reads. All ten scenarios passed:

| Scenario | How it was exercised |
| --- | --- |
| install | `dist/foton-0.3.3-any-any.yak` from `scripts/package_yak.py`, installed with `yak install` and Rhino restarted. Package Manager lists foton 0.3.3. The HB-Foton tab shows one "Foton" group with all four components and their icons, canvas search for "Foton" finds all four, and each shows 0.3.3 and its help on hover. Foton Settings' `install_` was run inside Rhino into scratch folders, with pip pointed at the local 0.3.3 wheel: it installs in the background while Rhino stays usable, ends at "0.3.3 / metal", says "already installed" when toggled again, and restarts cleanly after being switched off mid-install. The route that downloads its own Python (uv) installed 0.3.3 on Python 3.12.16 in 85 s, run outside Rhino from the same code |
| open_example, run, rerun, change_inputs, upgrade_invalidates_reuse, reload_moved_results, cancel | `scripts/check_grasshopper.py` in a freshly started Rhino against the extracted `dist/foton-grasshopper-0.3.3.zip`: ten automated checks, all true, in `rhino-smoke.json`, engine 0.3.3 on Metal |
| honeybee_metrics | `HB Annual Daylight Metrics` read the results folder of a fresh Foton Annual Daylight run of the bundle's shoebox example and returned DA identical to Foton's own output on all 36 sensors (maximum difference 0.0 pp), with no errors or warnings |
| ladybug_heatmap | `LB Spatial Heatmap` built a 36-face mesh with vertex colours from those values and the example model's SensorGrid mesh, with no errors or warnings |

Not covered: a fresh Rhino profile, Windows, and `install_` against the published PyPI release (0.3.3 was not on PyPI yet).
