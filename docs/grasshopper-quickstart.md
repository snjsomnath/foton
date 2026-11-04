# First Foton analysis in Rhino 8

Foton is a public beta in preparation. Only hardware and scenes with published
passing release evidence should be described as validated.

## Install once

1. Download the versioned `foton-grasshopper-<version>.zip` release asset and extract
   the entire archive into a permanent folder. Keep `examples` beside the `.gh` file.
2. Open **Foton First Analysis.gh** in Rhino 8 Grasshopper. The components already
   contain their scripts and bridge; no script editing or module search paths are needed.
   To reuse them in other definitions, copy the four `.ghuser` files into the
   Grasshopper User Objects folder (available from Grasshopper's File / Special Folders menu).
3. Set `install_` to True on **Foton Settings**. It finds a Python 3.10 to 3.13 on your
   computer, creates Foton's own environment in `~/.foton`, and installs
   `foton-daylight[honeybee]` into it. The download happens once, and the component
   shows each step as it goes. Once Foton is installed, leaving the
   toggle on costs only a quick check.

If you have no Python 3.10 to 3.13, install one from python.org first. If you would
rather install Foton yourself, run `python -m pip install "foton-daylight[honeybee]"`;
Foton Settings looks in the usual pip, virtual-environment and pipx folders, so you
normally don't need to connect a path.

Radiance is not needed. The annual sky matrix is computed by Foton's own Perez
all-weather model. Radiance 5.4a is used only to reproduce the validation evidence;
if it is installed, Foton Settings reports it and a run can opt into its sky.

The downloadable asset is produced only from a Rhino-generated, round-trip-tested
build matching the current component sources. If no asset is published yet, the
manual scripts in `grasshopper_foton/components` remain developer sources, not a
completed easy-install release.

## Five-minute example

1. Toggle **Check** on Foton Settings. Confirm the version, protocol, and selected
   backend. If Foton is not found, set `install_` to True, or connect the full
   `foton-honeybee` path to `executable_`.
2. Read any setup warnings. Metal or Vulkan should be selected for GPU execution.
   CPU reference fallback is usable for diagnosis but does not demonstrate GPU performance.
3. Toggle **Run** on Foton Annual Daylight. The example contains a shaded shoebox
   and Gothenburg weather. First-run weather preparation can take longer than later runs.
4. Connect `results` to **HB Annual Daylight Metrics**. Pair the original Honeybee
   SensorGrid meshes with `DA` in **LB Spatial Heatmap**; branches preserve model order.
5. Save the result folder. **Foton Annual Results** reloads its `run_manifest.json`
   without running a simulation. New result folders can be moved as a unit.

![The example definition with Foton's three components feeding HB Annual Daylight Metrics and LB Spatial Heatmap](images/grasshopper-canvas.png)

![Daylight autonomy of the shaded shoebox drawn by LB Spatial Heatmap in the Rhino viewport](images/grasshopper-heatmap-viewport.png)

The canvas above is the shipped example plus the two Ladybug Tools components
from step 4 and three Custom Preview components for the room; Honeybee's own
metrics component returns the same DA as Foton's `DA` output because Foton
writes a standard annual-daylight results folder.

Use `quality_ = final` when evaluating accuracy; it is the preset the
[0.3.0 release evidence](release-readiness.md#tested-platforms-for-030)
validated against converged Radiance. Preview is visibly labelled. Changing
inputs, quality defaults, solver versions, backend, or sky model version invalidates
automatic reuse. Missing/corrupt metric files also cause a new run in a numbered folder.

## Live mode for sliders

Set `live_` to True on **Foton Annual Daylight** or **Foton Daylight Factor** when you
want to drag a slider and see results straight away. Foton then keeps running in the
background between runs, with the model, the GPU and the traced daylight
coefficients ready.

- Changing thresholds, the schedule or the weather reuses the traced coefficients, so
  only the metrics are recomputed.
- Changing geometry, the grid filter or the trace settings traces again, but skips
  starting Foton and loading its libraries.
- Live runs write no files, so `results` is empty and Honeybee's result components
  have nothing to read. Turn `live_` off and run again to save a results folder.
- Press ESC to stop a long live run. This also stops the background process; the next
  live run starts a new one.

The background process stops when Rhino closes.

## Daylight factor

**Foton Daylight Factor** needs only a Honeybee model. It returns the daylight factor
for each sensor under a CIE overcast sky, in one branch per SensorGrid, ready for
**LB Spatial Heatmap**. A saved run writes Honeybee's daylight-factor layout: one
`.res` file per grid with `grids_info.json`.

Daylight factor and annual daylight use the same traced coefficients. In live mode,
running one after the other on the same model and settings traces only once.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Executable not found | Set `install_` to True on Settings, or connect the full path to `executable_`. |
| Install says no Python was found | Install Python 3.10 to 3.13 from python.org, or connect a `python` executable to `python_`. |
| Live run is no faster | The first live run starts Foton and traces as usual; only later runs on the same model are fast. |
| Settings reports `gendaymtx` unavailable | Nothing to do: annual runs use Foton's built-in sky. Install Radiance 5.4a and set `RADIANCE_BIN` only to reproduce validation evidence or to opt into `gendaymtx`. |
| Reference CPU selected | Update the GPU driver and inspect backend requirements; explicit Metal/Vulkan requests report errors instead of falling back. |
| Output/cache not writable | Use a local writable output folder and inspect Settings' directory diagnostics. |
| Unsupported modifier | Use diffuse Plastic or thin Glass with refractive index 1.52; Foton reports the rejected object/modifier. |
| Cancelled or failed | Read `report`; partial output is never eligible for reuse. Retry into the automatically allocated new folder. |

Report problems with Foton Settings output, OS/Rhino/GPU versions, the error text,
and a minimal shareable model. Remove private project paths from diagnostics before posting.
