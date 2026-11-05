# Foton

**Annual daylight results for Honeybee models in about a second, on your
computer's GPU.**

[![PyPI](https://img.shields.io/pypi/v/foton-daylight?style=flat-square)](https://pypi.org/project/foton-daylight/)
[![Python](https://img.shields.io/pypi/pyversions/foton-daylight?style=flat-square)](https://pypi.org/project/foton-daylight/)
[![CI](https://img.shields.io/github/actions/workflow/status/snjsomnath/foton/ci.yml?branch=main&style=flat-square&label=tests)](https://github.com/snjsomnath/foton/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](https://github.com/snjsomnath/foton/blob/main/LICENSE)

Foton computes daylight autonomy (DA), useful daylight illuminance (UDI),
spatial daylight autonomy (sDA) and daylight factor for Honeybee models. It
does the expensive ray tracing on the GPU, so a full year of hourly results
for a typical model takes about a second. You keep your Honeybee model and your
Ladybug result components. Only the slow step changes.

<p align="center"><img src="https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/grasshopper-live-mode.gif" width="55%" alt="Animation: as the window of a room is widened and narrowed in Grasshopper, daylight autonomy on the floor and the sDA, cDA, UDI and daylight factor plans update with it"></p>

*Live mode in Grasshopper (new in 0.3.2). Each time the window changes, Foton reruns the
annual study and every metric updates in about a third of a second.*

## Who it is for

- **Teachers and students** who want daylight results to update while they
  move a wall, a window or a shading fin.
- **Designers** comparing many early options, where waiting minutes per run
  means testing fewer ideas.
- **Researchers** who need thousands of annual runs for a parameter study.

## At a glance

<p align="center"><img src="https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/annual-run-times.png" width="85%" alt="Bar chart: a full annual daylight run takes 0.14 s for a 96-sensor room, 1.07 s for 2,020 sensors and 5.77 s for a 9,216-sensor office block"></p>

<p align="center"><img src="https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/benchmark-models.png" width="85%" alt="The four benchmark models drawn in 3D with the roof off: a single teaching office, four rooms around a courtyard, the three-room acceptance model and a four-storey office block with 256 rooms. Every sensor is a small square coloured by its daylight autonomy"></p>

<p align="center"><img src="https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/accuracy-sda.png" width="60%" alt="Scatter plot: sDA from Foton against sDA from Radiance for 119 sensor grids, all close to the diagonal"></p>

On a typical room Foton's daylight autonomy is within 0.2 percentage points of
converged Radiance. Details are under [Accuracy](#accuracy) and
[Speed](#speed) below.

## Quick start

```bash
pip install "foton-daylight[honeybee]"
```

That is all an annual study needs: from version 0.3.2, Radiance does not have
to be installed.

```python
from foton.honeybee import run_annual_daylight

run = run_annual_daylight(
    model="my_building.hbjson",   # any Honeybee model with sensor grids
    wea="my_city.epw",            # any EnergyPlus weather file
    output_folder="foton-results",
)

for grid in run.grids:
    print(f"{grid.identifier}: sDA {grid.sda:.0f} %, mean DA {grid.da.mean():.0f} %")
```

The `foton-results` folder has the same layout as a Honeybee annual daylight
run, so Honeybee's own metric and visualisation components can read it. To
check which GPU Foton will use, run `foton-honeybee capabilities`.

**In Rhino 8 and Grasshopper:** type `PackageManager` in Rhino, search for
**foton** and install it. You can also download `foton-grasshopper-<version>.zip`
from the [releases page](https://github.com/snjsomnath/foton/releases). The
components appear on the **HB-Foton** tab. Set `install_` on Foton Settings to
True and it installs the rest, including its own Python if you don't have one.
The [Grasshopper quickstart](https://github.com/snjsomnath/foton/blob/main/docs/grasshopper-quickstart.md)
walks through it with screenshots. It takes about five minutes. Foton's results go straight into Ladybug's own
components, such as the spatial heatmap below.

<p align="center"><img src="https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/grasshopper-heatmap-viewport.png" width="70%" alt="Daylight autonomy of a shaded room computed by Foton in Grasshopper and drawn by Ladybug's spatial heatmap"></p>

## How it works

![Diagram: your Honeybee model and weather file go into Foton, which builds a GPU scene, traces light from every sky patch to every sensor, applies the year's hourly skies, and writes results in Honeybee's format](https://raw.githubusercontent.com/snjsomnath/foton/main/docs/images/how-it-works.png)

Foton uses the same daylight-coefficient method as Radiance's matrix workflow.
It traces, once, how much light from each patch of the sky reaches each
sensor. It then combines those coefficients with the 8,760 hourly skies of a
weather file. Foton does both steps on the GPU: Metal on Apple silicon, Vulkan
on Windows and Linux. A slower CPU version gives the same answer on any
machine. More in [architecture](https://github.com/snjsomnath/foton/blob/main/docs/architecture.md).

## Accuracy

Foton is checked against Radiance 5.4a on 106 test models, each at two sky
resolutions: 212 cases with 234 sensor grids. The Radiance results are
repeated with more rays until they stop changing, so they serve as the correct
answer. Metal and Vulkan give the same figures to two decimal places.

| Compared with Radiance | Typical grid (median) | 95 % of grids within |
| --- | ---: | ---: |
| Daylight reaching the sensors from the sky, total difference | 0.5 % | 1.2 % |
| Annual hourly illuminance, total difference | 0.1 % | 0.6 % |
| Annual hourly illuminance, hour-by-hour scatter (CV(RMSE)) | 2.4 % | 7.1 % |
| Daylight autonomy (DA), average error per grid | 0.2 pp | 0.5 pp |
| Useful daylight illuminance (UDI), average error per grid | 0.2 pp | 0.6 pp |
| Spatial daylight autonomy (sDA) | 0 pp | 2.8 pp (one sensor in 36) |

pp means percentage points. 204 of the 212 cases pass every check. The eight
that don't are rooms lit only through glass from another room, plus one very
bright deep room where Radiance itself changes by 3.6 % between 8 and 12
bounces. They are explained in the
[accuracy notes](https://github.com/snjsomnath/foton/blob/main/docs/purpose-and-plan.md).
Raw results:
[Metal](https://github.com/snjsomnath/foton/blob/main/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/README.md),
[Vulkan](https://github.com/snjsomnath/foton/blob/main/validation/results/2026-11-03-architectural-v4-vulkan-t4/README.md).

## Speed

<!-- speed-table:start (generated by scripts/refresh_readme_speed.py) -->
Measured on 4 November 2026 on a MacBook Pro (Apple M4 Pro, 24 GB), using Metal and Foton 0.3.2 (commit `a5ca9d7`) at its default `final` quality (8 bounces, 256 direct and 65,536 indirect samples, 146-patch sky, Gothenburg weather). An annual run starts from a model Foton has not seen before: loading it, building the GPU scene, tracing, and writing DA and UDI for all 8,760 hours. The Grasshopper round trip adds writing the HBJSON, starting Foton and reading the results back. Annual times are the median of 5 runs and round trips the median of 3.

| Model | Rooms | Sensors | Annual run | Grasshopper round trip |
| --- | ---: | ---: | ---: | ---: |
| Teaching office | 1 | 96 | 0.16 s | 0.59 s |
| Courtyard with four rooms | 4 | 112 | 0.18 s | – |
| Acceptance model | 3 | 2,020 | 1.05 s | 1.56 s |
| Four-storey office block | 256 | 9,216 | 6.10 s | 6.93 s |

Raw data: [apple-m4-pro-672fe35d](https://github.com/snjsomnath/foton/blob/main/benchmarks/machines/apple-m4-pro-672fe35d/20261104T081559Z.json). Other machines: [results by machine](https://github.com/snjsomnath/foton/blob/main/benchmarks/machines/README.md).
<!-- speed-table:end -->

## What it does

- Annual DA, continuous DA, UDI (low, useful, high) and sDA, plus daylight factor
- Hourly illuminance for every sensor, in Honeybee's result format
- Its own annual sky model (Perez all-weather), so Radiance is not needed
- Diffuse surfaces with several light bounces, thin glass, and shading devices
- 146-patch (Tregenza) and 578-patch (Reinhart) skies
- `preview` and `final` quality settings
- Metal (macOS), Vulkan (Windows, Linux) and a CPU fallback that gives the
  same answer
- A Python API, a command-line tool and four Grasshopper components

## What it does not do

Foton covers ordinary architectural daylighting: matte surfaces, ordinary
glazing, shading devices and building-scale sensor grids. Use Radiance for:

- glossy or mirror-like materials, and other Radiance material types
- complex fenestration (BSDF), prismatic films and other light-redirecting systems
- glare, annual sunlight exposure (ASE) and dynamic shading
- certification or compliance reports

One known difference: Foton treats the sun as part of its sky patch, as
Radiance's `rfluxmtx` method does, rather than tracing it as a separate disc.
On south-facing rooms in Phoenix, Seattle and Gothenburg this changed DA by
about 1 percentage point
([measured](https://github.com/snjsomnath/foton/blob/main/validation/results/2026-11-02-teaching-sun-vs-stock/README.md)).

## Documentation

- [Installation](https://github.com/snjsomnath/foton/blob/main/docs/installation.md): supported GPUs and platforms
- [Grasshopper quickstart](https://github.com/snjsomnath/foton/blob/main/docs/grasshopper-quickstart.md)
- [Python API](https://github.com/snjsomnath/foton/blob/main/docs/python-api.md)
- [How it works](https://github.com/snjsomnath/foton/blob/main/docs/architecture.md)
- [Accuracy notes and plan](https://github.com/snjsomnath/foton/blob/main/docs/purpose-and-plan.md)
- [Reproducing the benchmarks](https://github.com/snjsomnath/foton/blob/main/docs/benchmarking.md)
- [Validation models](https://github.com/snjsomnath/foton/blob/main/validation/architectural-scenes.md)
- [FAQ](https://github.com/snjsomnath/foton/blob/main/docs/faq.md)
- [Changelog](https://github.com/snjsomnath/foton/blob/main/CHANGELOG.md)

### Live teaching demo

A clone of this repository also includes a one-minute animated teaching demo
that runs live on your GPU. It needs Node.js 20 or newer:

```bash
pip install -e ".[viewer]"
cd viewer && npm ci && npm run dev:demo
```

Then open `http://127.0.0.1:5173/demo.html`. See the
[demo guide](https://github.com/snjsomnath/foton/blob/main/viewer/src/demo/README.md).

## Status

Foton is young (version 0.3) and still changing. The accuracy figures above
hold for the kinds of rooms in the test set. They are not a claim that Foton
matches Radiance on any model. Please
[open an issue](https://github.com/snjsomnath/foton/issues) if you find a model
where the two disagree.

## How this was built

This project is basically an exercise in using LLMs to create
reimplementations within a tight scope against a deterministic target. In
this case, we wanted to have fast GPU based daylighting calculations for
teaching purposes, so we built it! (or asked an LLM to). The code and
documentation were generated by an LLM. Radiance served as the deterministic
target: every result above comes from comparing Foton with it.

## Citing Foton

If you use Foton in research, please cite it. GitHub's **Cite this repository**
button gives the reference, from
[CITATION.cff](https://github.com/snjsomnath/foton/blob/main/CITATION.cff).

## License and credits

Foton is released under the
[MIT License](https://github.com/snjsomnath/foton/blob/main/LICENSE).
[NOTICE](https://github.com/snjsomnath/foton/blob/main/NOTICE) credits the
published methods and data it builds on, and
[THIRD_PARTY_LICENSES.md](https://github.com/snjsomnath/foton/blob/main/THIRD_PARTY_LICENSES.md)
lists the open-source libraries inside the Python package.
[ACKNOWLEDGEMENTS.md](https://github.com/snjsomnath/foton/blob/main/ACKNOWLEDGEMENTS.md)
thanks the people and projects that made Foton possible.

Foton works alongside [Ladybug Tools](https://www.ladybug.tools/) and is tested
against [Radiance](https://www.radiance-online.org/). It is not affiliated with
either project. The optional Honeybee packages are licensed separately under
AGPL-3.0 and GPL-3.0, and Foton does not include their code.

## Authors

Foton was started and is led by
[Sanjay Somanath](https://github.com/snjsomnath) at Chalmers University of
Technology. Its copyright belongs to the Foton contributors; see
[AUTHORS.md](https://github.com/snjsomnath/foton/blob/main/AUTHORS.md).
