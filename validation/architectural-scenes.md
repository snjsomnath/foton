# Architectural daylight corpus

`validation/scenes.py` defines 90 deterministic architectural questions. Suite
version 3 preserves the original 50 cases and adds a five-by-eight footprint/window
matrix. There are 89 generated models plus the three-room acceptance HBJSON. Every
model has explicit diffuse/Glass materials, room-linked sensor grids and metadata.
The default procedural workplane uses one-metre cells, 0.75 m above each floor;
the acceptance case retains its original three grids and 2,020 sensors.

## Coverage

| Category | Cases | Architectural interactions |
| --- | ---: | --- |
| Controls | 3 | Darkness, direct integration through an open aperture, clear-glazed reference |
| Form | 47 | I/J/L/T/cross window matrix, L/U-shaped and trapezoidal plans, shallow/deep spaces, narrow corridor, double height, pitched roof |
| Orientation | 4 | North/east/west windows and a 37-degree room rotation including shades and grids |
| Openings | 7 | Rooflights, multiple roof openings, corner/opposite glazing, ribbon windows, clerestory, near-full-height glazing |
| Shading | 10 | Overhang/fins, deep overhang, asymmetric fins, horizontal/vertical/eggcrate louvres, shelf, balcony, reveals, rooflight shaft |
| Context | 5 | Neighbouring facade, canyon, enclosed courtyard, offset tower and reflective neighbouring facade |
| Materials | 7 | Tinted glass, bright deep room, dark finishes, bright ceiling, coloured walls, low/mixed glazing transmittance |
| Connections | 6 | Interior glazing, serial glazing, corridor-to-office light, stacked opaque zones, four courtyard rooms, rooflit atrium |
| Integration | 1 | Original Honeybee model, grid ordering, stock recipe and metric reload |

The generated sample [catalogue](../test_models/architectural/README.md) lists the question for
each individual model. `python -m validation.scenes --list` reads the source catalogue
without requiring Honeybee to be installed.

The new `plan_{i,j,l,t,cross}_{profile}` matrix extrudes orthogonal rectangle-union
outlines to 3 m. Floor areas are respectively 90, 63, 54, 63 and 63 m². Profiles
are `small_center`, `large_center`, `offset_low`, `offset_high`, `triangle`,
`circle`, `arch` and `distributed`. Single openings use the lowest south-facing
boundary edge, selected by segment rather than ambiguous wall orientation.
Small rectangles, triangles, circles and arches each have 1.44 m² polygon area;
large rectangles have 4.8 m². Circular windows are regular 32-sided polygons;
arches use a 16-segment semicircle with an area-adjusted rectangular base.
Distributed 1 × 1.2 m windows appear on every vertical facade, including recesses.
All use clear glass at 0.6 transmittance and diffuse surfaces at 0.5 reflectance.
Metadata includes `footprint_family` and `window_profile`.

## Generate and inspect

Use an environment with the current Foton build and the `honeybee` and `test`
extras. The geometry tests require Honeybee Radiance as well as Honeybee Core.
Converged comparisons additionally require Radiance 6 and the oracle dependencies
listed in [release readiness](../docs/release-readiness.md).

```bash
python -m validation.scenes --output /tmp/foton-architectural-samples
python -m validation.scenes --list --category connections
python -m validation.scenes --output /tmp/foton-shading-samples --category shading
```

The output directory must be new. Export validates each Honeybee model and writes
HBJSON files, a readable catalogue, and `manifest.json` with version, architectural
questions, coverage tags, room/aperture/shade/sensor counts and SHA-256 hashes.
Files contain `user_data.validation_scene` so the purpose travels with the model.
Exports include Radiance properties only, keeping optional Honeybee Energy plugins
from changing the daylight samples. Material libraries are sorted to stabilize
hashes between Python processes; face, vertex and sensor order are preserved.
Source and exported models use Honeybee's normalized HBJSON geometry representation
to preserve geometry and grids on reload.
Open them through Honeybee's HBJSON loader in Grasshopper. Static shades use actual
opaque faces; the canyon, tower and balcony use closed six-face volumes. A rooflight
well uses four opaque interior faces beneath the opening. It represents the shaft's
optical restriction. The atrium explicitly splits its shared wall at the office
floor level so both sets of interior windows have valid reciprocal adjacencies.

## Test geometry and physical interactions

```bash
python -m pytest tests/python/test_architectural_scenes.py tests/python/test_release_readiness.py
```

The tests validate every model, deterministic regeneration, HBJSON round trips,
Radiance geometry/material export, workplane containment, positive sensor areas,
unit conversion and native scene preparation. Every scene also runs a small
reference-backend transport diagnostic in both sky bases with finite, nonnegative
coefficient checks. Saved sample hashes and contents must match the generator.

Behavioural comparisons check that opaque shades cannot increase direct light,
combined eggcrate shades retain both individual masks, lowered glass transmittance
reduces direct light, surface reflectance changes preserve direct light while
changing reflected light, red walls preserve RGB differences, and a bright neighbour
changes reflected light without changing its direct obstruction. Borrowed-light
cases must export each shared window once and produce light in each zone. Closing
the lower-storey exterior windows must leave that room dark despite a lit storey
above. Orientation and rotation checks inspect actual normals, shade vertices and
sensor positions.

These are physical diagnostics with modest fixed sample budgets. They do not
establish Radiance convergence or qualify GPU accuracy.

## Compare against Radiance

```bash
python scripts/validate_release_suite.py --backend metal --models-dir test_models/architectural --workers 4 --output /tmp/foton-full-corpus
python scripts/validate_release_suite.py --backend vulkan --models-dir test_models/architectural --workers 4 --output /tmp/foton-windows-corpus
python scripts/validate_release_suite.py --backend reference --category connections --sky-density 1 --smoke --output /tmp/foton-connections-smoke
```

Every case compares direct, indirect and full coefficients, seven controlled skies
(uniform, overcast, horizon, north, east, south, west), annual illuminance and annual
metrics against independent Radiance export and sampling. Reports retain the case
question, interactions and model counts alongside errors, convergence evidence,
hardware and timings. Separate cold/cached timings and official Honeybee metric
reload remain available. The stock recipe comparison remains on the acceptance case.

Complete evidence requires 90 scenes in both sky bases (180 cases), a stable oracle, actual GPU
execution and a clean release commit. Category/scene subsets, smoke runs and CPU
diagnostics remain incomplete. The verifier rejects obsolete suite versions,
missing scenes, repeated cases and missing platforms. Read the
[release gates](../docs/release-readiness.md) for the numerical thresholds and live
Rhino acceptance requirements.

`--models-dir` checks manifest version, coverage, hashes, metadata and Honeybee
validity before running. Archive the models, weather and installed wheel together;
pass `--weather` and `--wheel` to record their hashes. Reports include dependencies,
revision/dirty state, GPU capabilities, per-case elapsed time and result classes:
stable accuracy failure, unstable reference, execution error or pass. A dirty
snapshot remains diagnostic even when all numerical comparisons pass.

The runner defaults to `--direct-io binary`: native-endian double-precision
Radiance ray input/output avoids large text conversions without changing sample
counts, weights, origins, direction generation or convergence gates. Real Radiance
parity tests cover open and polygon-glazed scenes in both sky bases. The established
ASCII path remains available via `--direct-io ascii` for regression diagnostics.
Binary direct integration dispatches independent sensor chunks to four single-
process Radiance workers, avoiding `rcontrib -n 4` per-ray IPC overhead while
preserving the total worker budget. Each stage records elapsed time and invocation
count. Only the final regenerable ray chunk is retained, as with the ASCII path.

For Windows, install the same wheel version built for Windows and the Honeybee/test
extras, `lbt-recipes==0.28.8` and `setuptools`; use Radiance 6 and an actual Vulkan
GPU without fallback. Run the Vulkan command above with the frozen EPW via
`--weather`, the archived Windows wheel via `--wheel`, and `--radiance-bin` pointing
to its Radiance binaries. Retain the full output tree (suite/report JSON and
Markdown, oracle intermediates, logs, candidate cold/cached results), fixture
manifest/HBJSON, EPW, wheel, dependency lock, source snapshot and driver diagnostics.
Windows execution remains pending an accessible GPU runner; a clean commit and
separate live Rhino evidence are still required for release qualification.

Equivalent PowerShell command (replace the explicit paths with the archived inputs):

```powershell
python scripts/validate_release_suite.py --backend vulkan --models-dir C:\foton-campaign\inputs\models --weather C:\foton-campaign\inputs\gothenburg.epw --wheel C:\foton-campaign\inputs\foton_daylight-0.2.0-cp313-cp313-win_amd64.whl --radiance-bin C:\Radiance\bin --workers 4 --output C:\foton-campaign\vulkan-full
python scripts/summarize_release_campaign.py C:\foton-campaign\vulkan-full
```

The corpus covers diffuse Plastic, thin Glass and static architectural shading.
Dynamic shades, BSDF, AirBoundary and compliance metrics outside the supported
scope are not used. Actual climate/north/schedule parameter sweeps and real project
models can expand this battery in future versions; the current annual cases use
Gothenburg weather and the existing default occupancy schedule.
