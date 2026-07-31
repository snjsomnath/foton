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
    metrics=["df", "da", "static_sda300_50"],
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
