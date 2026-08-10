# Foton GhPython components

These scripts are copy-ready sources for manual IronPython GhPython components.
They run Foton through the external `foton-honeybee` executable, so Rhino never
loads Foton's CPython native extension.

## Installation

1. Install `foton-daylight[honeybee]` in a normal CPython environment and make
   `foton-honeybee` available on `PATH`. On Windows, the command will usually be
   `foton-honeybee.exe` in the environment's `Scripts` folder.
2. Clone or copy this `grasshopper_foton` folder to a stable location.
3. Add the folder's **parent directory** to Rhino's IronPython module search
   paths. This allows `from grasshopper_foton.foton_gh import ...` to work.
4. Create GhPython components and paste the corresponding source from
   [`components`](components). Create input/output nodes exactly as documented
   at the top of each script. Preserve capitalization such as `DA` and `_run`.
5. If Rhino cannot find the executable from `PATH`, connect its full path to
   `executable_`. No Python executable path or generated runner script is used.

## Components

### Foton Settings

Checks executable discovery, protocol compatibility, Foton version, selected
backend, backend capabilities, and the weather-cache location.

### Foton Annual Daylight

Accepts a Honeybee Model or HBJSON path and a Ladybug Wea or EPW/WEA path. It
also accepts Honeybee-style `-t/-lt/-ut` thresholds, an annual schedule, numeric
or vector north, quality, sky density, backend, grid filter, and advanced sample
overrides.

The script serializes object inputs, invokes `foton-honeybee annual-daylight
--jsonl`, reports stage progress on the component, and terminates the subprocess
when ESC is detected through Rhino's `scriptcontext.escape_test`. Existing results are reused only
when the protocol's content fingerprint is compatible. Otherwise, an atomically
reserved `-001`, `-002`, etc. output folder prevents collisions.

### Foton Annual Results

Loads `run_manifest.json` without rerunning Foton. This is useful when opening a
Grasshopper definition after an analysis has completed.

## Honeybee/Ladybug interoperability

`results` is a one-item list containing Foton's official-compatible annual
results folder. It can be connected directly to components such as **HB Annual
Daylight Metrics** and **HB Annual Results to Data**. Foton exports
`grids_info.json`, `sun-up-hours.txt`, and the static-aperture NumPy arrays those
components expect.

`DA`, `cDA`, `UDI`, `UDI_low`, and `UDI_up` are DataTrees with one branch per
SensorGrid. Branch order and sensor order are identical to the HBJSON model, so
the trees can be paired with the corresponding SensorGrid meshes in **LB Spatial
Heatmap**. `sDA`, `grid_ids`, and `room_ids` use the same grid order.

Dynamic aperture schedules, ASE, enhanced direct-sun results, BSDF materials,
and glare are intentionally not exposed by these initial components.

## Result tree contract

For the canonical `test_models/test.hbjson`, metric trees contain:

- branch `{0}`: `classroom_01`, 175 values;
- branch `{1}`: `office_02`, 960 values;
- branch `{2}`: `office_01`, 885 values.

The scripts do not regroup flattened values. They read the ordered grid entries
and per-grid metric files from Foton's versioned manifest.
