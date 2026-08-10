# Python API

Build the extension with Maturin:

```bash
python -m pip install -e .
```

```python
from foton import Engine
```

`Engine()` automatically selects Metal for a compatible Apple GPU, probes Vulkan
for compatible NVIDIA, AMD, or Intel ray-query GPUs, and otherwise uses the
deterministic CPU reference backend. Use `Engine({"backend": "metal"})`,
`Engine({"backend": "vulkan"})`, or `Engine({"backend": "reference"})` to
request a backend explicitly. Vulkan requires a system Vulkan 1.3 driver exposing
ray query, scalar block layout, buffer device address, and acceleration-structure
features. Vulkan results report `transport_backend="vulkan"` and never silently fall
back after an explicit Vulkan request. `Engine.create_scene(...)` accepts only C-contiguous
`float32` and `uint32` NumPy arrays matching the contracts in
`docs/architecture.md`.

```python
job = scene.analyze(
    sky,                 # float32[146, timestep, 3] preview
    occupancy,           # float32[timestep]
    quality="preview",
    metrics=[
        "df", "da", "cda", "udi_lower", "udi", "udi_upper",
        "static_sda300_50",
    ],
    maximum_samples=64,
    maximum_bounces=1,
    export_coefficients=False,
)
snapshot = job.poll()
result = job.result()    # releases the GIL while waiting
```

Starting a superseding analysis or calling `Scene.update_rooms(...)` cancels stale
jobs. Scene inputs are copied before jobs start, so callers may mutate or free their
NumPy arrays after `create_scene` returns.

Coefficient export is intentionally opt-in because a
`float32[sensor,patch,3]` matrix can be large:

```python
job = scene.analyze(
    sky,
    occupancy,
    quality="preview",
    maximum_samples=0,
    maximum_bounces=0,
    export_coefficients=True,
)
result = job.result()
coefficients = result.coefficients()  # NumPy float32[sensor, patch, 3]
```

`result.has_coefficients()` reports whether export was requested. `metadata_json()`
serializes only solver metadata and never embeds the coefficient matrix.

## Honeybee annual daylight

Install the Honeybee extra and ensure Radiance `gendaymtx` is available:

```bash
python -m pip install -e '.[honeybee]'
export RADIANCE_BIN=/path/to/radiance/bin
```

Use a study when running more than one weather, schedule, or threshold analysis.
The prepared model, native scene, acceleration structures, and compatible
coefficient tensor stay resident:

```python
from foton.honeybee import HoneybeeStudy

study = HoneybeeStudy(
    "test_models/test.hbjson",
    backend="auto",
    grid_filter="*",
)
run = study.annual_daylight(
    "epw/gothenburg.epw",
    schedule=None,
    north=0,
    quality="final",
    sky_density=1,
)

office = run.grid("office_01")
print(office.da, office.cda, office.udi, office.sda)
print(run.timings, run.results_folder)
```

For a one-shot run:

```python
from foton.honeybee import run_annual_daylight

run = run_annual_daylight(
    model="test_models/test.hbjson",
    wea="epw/gothenburg.epw",
    output_folder="simulation/foton-annual",
    export_illuminance=True,
)
```

The default schedule follows Honeybee Radiance: 08:00–18:00 exclusive, with
3,650 occupied hours. Supplied schedule values are occupied at `>=0.1`.
DA, cDA, UDI-low, UDI, UDI-high, and area-weighted sDA are returned in the
original HBJSON SensorGrid and sensor order.

`sky_density=1` is the Honeybee-compatible Tregenza MF:1 default (146 rows).
Use `sky_density=2` for Reinhart MF:2 (578 rows). Final quality uses 64
deterministic solid-angle samples per sky patch, 4,096 indirect samples, one
diffuse bounce, and seed 0. `direct_samples` is available as an advanced
override. Re-running only weather, schedule, thresholds, or raw export on the
same study reuses compatible coefficients and reports zero tracing time.

With `export_illuminance=True`, the `results` folder is directly loadable by
`honeybee_radiance_postprocess.results.AnnualDaylight`. Raw export is opt-in for
the convenience API and on by default for `Recipe("annual_daylight")` and the
CLI:

```bash
python -m foton.honeybee annual-daylight \
  --jsonl \
  --model test_models/test.hbjson \
  --wea epw/gothenburg.epw \
  --output simulation/foton-annual
```

With `--jsonl`, the CLI streams versioned `started`, `progress`, and `complete`
events. The final event embeds the same manifest written to
`run_manifest.json`, including grid-grouped metric paths, timings, warnings,
cache status, versions, and an input-content fingerprint. Without `--jsonl`,
the CLI prints only the final manifest for backwards compatibility.

Use `foton-honeybee capabilities` for the protocol/engine handshake. The
`honeybee_foton` package supplies a cancelable subprocess client plus controllers
for the initial Foton Settings, Annual Daylight, and Annual Results components.
It discovers `foton-honeybee` from `PATH` or an explicit user setting and never
generates runner source or embeds a Python executable path. Metric results are
returned as one already ordered branch per SensorGrid.

Copy-ready IronPython component sources are available in
[`grasshopper_foton`](../grasshopper_foton). They provide Foton Settings, Foton
Annual Daylight, and Foton Annual Results scripts with documented GhPython node
names. Their `results` output is a one-item Honeybee-compatible result-folder
list, and each metric output is already grouped into one DataTree branch per
SensorGrid for Ladybug spatial visualization components.

## Honeybee direct-visibility recipe

Install the optional Honeybee adapter dependencies and provide native Radiance
executables separately:

```bash
python -m pip install -e '.[honeybee]'
export RADIANCE_BIN=/path/to/radiance/bin
```

The adapter mirrors the Ladybug Tools recipe call pattern:

```python
from foton.honeybee import Recipe, RecipeSettings

recipe = Recipe("direct_visibility")
recipe.input_value_by_name("model", model_or_hbjson)
recipe.input_value_by_name("backend", "compare")
recipe.input_value_by_name("sky_basis", "tregenza")

project = recipe.run(RecipeSettings(folder="simulation", workers=8))
report = recipe.output_value_by_name("comparison_report", project)
```

This recipe compares identical patch-center rays on Metal and native
`rcontrib -ab 0`. Honeybee Apertures are geometric openings; static shades are
opaque. It does not validate glazing transmission, indirect daylight
coefficients, or annual metrics.

Run the deterministic shaded-shoebox fixture with:

```bash
python scripts/compare_honeybee_shoebox.py --auto-grid
```
