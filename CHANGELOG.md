# Changelog

All notable Foton changes are recorded here.

## 0.3.6 - 2026-11-08

Faster on NVIDIA, AMD and Intel graphics cards (Vulkan). Results are
byte-identical to 0.3.5.

- The scene, its BVH and the result buffers now live in the graphics card's
  own memory. Before, they sat in system memory, so on a separate card every
  ray read the scene over the PCIe bus. On a Colab L4 this makes tracing about
  2.4 times faster on the 256-room office block. If a model doesn't fit in the
  card's memory, Foton falls back to system memory instead of failing. Setting
  `FOTON_VULKAN_HOST_MEMORY=1` forces the old behaviour, for comparisons.
- Grasshopper runs on Vulkan are much faster. The component asks for hourly
  illuminance, which Vulkan worked out on a single CPU thread: about 37 s of a
  40 s run on the office block on a Colab L4. It now uses every CPU core and
  SIMD, adding in the same order as before, so the values are unchanged.
- `install_` in Grasshopper now upgrades an engine older than the
  components, so installing 0.3.6 from the Package Manager also brings the
  faster engine.
- Sample tiles are sent to the GPU eight at a time, all room BVHs are built in
  one go, and the sampling loop stops early, as it already did on Metal.

## 0.3.5 - 2026-11-05

Fixes a Grasshopper error found by the second Windows test.

- Foton Annual Daylight and Foton Daylight Factor lock the Grasshopper canvas
  while a run is in progress. On Windows, flipping a toggle during a run
  expired the running component: Grasshopper kept reporting "object expired
  during a solution" until the run ended as cancelled. The lock is meant to
  stop that; it still needs confirming on Windows. On a Mac the error never
  happened, and a click made during a run takes effect once the run ends.
  Press ESC to stop a run.
- The Windows testing guide explains how to time a second run that isn't
  reused.

## 0.3.4 - 2026-11-04

Fixes the Grasshopper install on Windows, found by the first Windows test.

- `install_` on Windows no longer opens a terminal window for each step. Live
  mode's background process and Check also start without one.
- When an install step fails, Foton Settings now shows the whole log in
  `report` and turns red, instead of stopping with an empty `report`. The
  message gives the exit code, the end of pip's own log and the exact command
  to run by hand. Every step is also saved to `~/.foton/install.log`, and pip's
  detailed log to `~/.foton/pip.log`.
- The version Foton installs is written as `~=0.3.3` instead of
  `>=0.3.3,<0.4`, which means the same but has no `<` or `>` for a Windows
  shell to misread.
- Connecting `uv` to `python_` makes `install_` download its own Python even
  when one is installed, so the no-Python route can be tested on any computer.
- The example definition has a toggle on `install_`.

## 0.3.3 - 2026-11-04

Makes installing Foton in Rhino straightforward.

- The Foton components now appear on an **HB-Foton** tab in the Grasshopper
  toolbar and in canvas search. Since 0.3.0 they had been hidden from both,
  so the only way to reach them was through the example file.
- The components are built on Rhino 8's current IronPython 2 script
  component, so they no longer carry an "OLD" badge. They need Rhino 8.
- `install_` on Foton Settings no longer needs Python installed first. When it
  finds no Python 3.10 to 3.13, it downloads uv into `~/.foton`, which fetches
  a private Python 3.12 for Foton's environment. Nothing outside `~/.foton`
  changes.
- `install_` runs in the background, so Rhino stays usable while Foton
  installs; Foton Settings shows how long it has been running and checks the
  install when it finishes. Before, Rhino froze until the install was done,
  which could be minutes when Foton downloads its own Python.
- The components are easier to use: each has its own icon, a description,
  and help text on every input and output (hover over one to read it). The
  version shows under each component.
- Foton is packaged for Rhino's Package Manager (Yak). The release workflow
  builds the package, attaches it to the GitHub release and publishes it.
- New step-by-step install guide with screenshots in
  `docs/grasshopper-quickstart.md`, and a maintainer guide in
  `docs/publishing-yak.md`.
- The browser viewer's demo now works from a pip install. Its Gothenburg
  weather file ships inside the package; before, the demo stopped with "Demo
  weather is missing" unless it ran from a checkout.
- The citation (CITATION.cff) now lists Alexander Hollberg as second author.
- CI runs less: a push to main after a tested pull request gets a quick Linux
  check, a newer push cancels a pull request's older run, pull requests test
  four Python jobs instead of six, and the viewer is checked only when it
  changes.
- The release check reuses an earlier version's Metal and Vulkan suites when
  nothing in the engine changed since: only the version number, the
  Grasshopper components, the viewer or documentation.
- Faster live mode in Grasshopper with identical results. The background
  worker keeps prepared weather in memory across geometry changes instead of
  re-reading the EPW and the cached sky matrix on every run; the Grasshopper
  bridge waits on a .NET event instead of IronPython's polling queue, passes
  at most one progress update per quarter second to Rhino during a live run,
  and reads the weather and schedule files in place instead of copying them.

## 0.3.2 - 2026-11-04

The first release with Foton's own sky: `pip install foton-daylight[honeybee]`
now runs annual daylight with no Radiance install. It also brings live mode,
daylight factor and a one-click install to Grasshopper, and a rewritten README
for first-time visitors.

- The README is rewritten for a first-time visitor, with charts of speed and
  accuracy and a diagram of how a run works.
- Grasshopper now defaults to 8 diffuse bounces, the validated setting. The
  Foton Annual Daylight component used to pass `bounces_ = 1` when nothing was
  connected, which reads about 18 % low; scripted and command-line runs were
  not affected.
- Foton Settings finds `foton-honeybee` on its own: in Foton's environment in
  `~/.foton`, on PATH, and in the usual pip, venv and pipx folders on Windows
  and macOS. Its new `install_` toggle creates that environment from a Python
  3.10 to 3.13 already on the computer and installs Foton into it.
- Live mode: `live_` on the annual and daylight factor components sends runs to
  a background worker (`foton-honeybee serve`) that keeps the scene, the GPU and
  the traced coefficients between runs and writes no files. Changing
  thresholds, schedule or weather then only recomputes the metrics.
- Daylight factor: a new Foton Daylight Factor component, a
  `foton-honeybee daylight-factor` command and `HoneybeeStudy.daylight_factor()`.
  Results are written in Honeybee's daylight-factor layout (one `.res` file per
  grid). Annual daylight and daylight factor share traced coefficients.
- Annual-daylight result files and manifests are unchanged; the command now
  shares its code with the worker.

- The browser demo (`npm run dev:demo`) is a shorter 54.5-second cut that follows
  one room. It holds the daylight metric explanations longer, drops the
  1,024-zone ending and the header affiliation, labels each result as live
  preview or final quality, and closes on the Grasshopper and Python install routes.
- Faster annual runs with identical results. On an M4 Pro the diffuse trace is
  about 36 % faster (2,020 sensors: 1.18 s to 0.76 s; 9,216 sensors: 6.58 s to
  4.26 s), mostly because the GPU's random-number loop now stops at the
  highest set bit of the sample index. Large models also build their scene
  structures in one GPU submission (0.093 s to 0.007 s for 256 rooms), the
  hourly illuminance export skips dark hours and one 323 MB copy, and result
  folders are written with `np.save` instead of memory maps (2.86 s to 0.58 s
  for 9,216 sensors on macOS). Coefficients, hourly illuminance, every metric
  and every result file are bit-identical to before on all 106 architectural
  scenes and `test.hbjson`, and on the 9,216-sensor office block once the
  room fix below is applied.
- Includes the 0.3.1 fix for Metal models with many rooms (see below).
- The first trace that uses a newly built scene now reports the
  acceleration-structure build time in `acceleration_structure_ms`; it was
  always 0 for committed scenes.
- `scripts/benchmark_hardware.py` now times cold end-to-end annual daylight
  runs at the shipped defaults on four Honeybee models of increasing size,
  replacing the July 2026 fixtures that used 4,096 samples and 2 bounces.
  `scripts/benchmark_grasshopper.py` times the Grasshopper component's round
  trip stage by stage. `scripts/benchmark_suite.py` runs both and files the
  result under a hardware-derived machine ID in `benchmarks/machines/`, and
  `scripts/compare_benchmarks.py` tabulates every machine. The README speed figures come from new runs on
  3 November 2026; the old July results were removed.
- Foton computes its own annual sky matrix. `daylight_core::sky::perez`
  implements the Perez all-weather model (Perez, Seals and Michalsky 1993,
  with the Perez et al. 1990 luminous-efficacy fits) over the Tregenza 1987
  and Reinhart MF:2 patches from the published papers; it is exposed as
  `daylight_engine.perez_sky_matrix` and is the default
  `prepare_annual_weather` source (`sky_source="foton"`). Radiance's
  `gendaymtx` is now optional at run time (`sky_source="gendaymtx"`,
  `--sky-source`) and serves as the validation oracle: the matrix agrees with
  `gendaymtx -O0` bit for bit on Gothenburg, Phoenix and Seattle at both
  densities, with identical sun-up hour sets (`tests/python/test_builtin_sky.py`,
  golden file under `tests/fixtures/sky`). The weather cache is keyed on the
  source; weather metadata, the run manifest and the Grasshopper Settings
  preflight report it, and a missing Radiance no longer fails the preflight.
  `pip install foton-daylight[honeybee]` is the whole run-time requirement
  for an annual study; Radiance 5.4a is needed only to reproduce validation
  evidence (the "Radiance 6" wording in the docs was never required).
- README: a table of headline accuracy figures against Radiance from the
  0.3.0 release runs, install notes for the viewer, the command-line tool and
  Grasshopper, and full GitHub links so images and links work on PyPI.
- The source distribution no longer bundles `validation/results/` (20.9 MB
  down to about 2 MB).
- Removed old output folders (`simulation/` and four July benchmark runs) and
  the viewer's compiled config files. `tsc -b` no longer writes them into the
  source tree.
- Docs updated for the 0.3.0 release.

## 0.3.1 - 2026-11-03

A fix-only release.

- Metal: on models with many rooms (about 256 or more), the GPU could skip
  whole rooms while tracing, so rays passed through their walls. Results were
  wrong and changed from run to run; on a 256-room, 9,216-sensor office block
  mean DA moved between 0.47 and 0.89 where the correct value is 0.68.
  Every room's geometry is now kept resident for the whole trace. Models up to
  128 rooms, all validation scenes and the acceptance model were unaffected
  and give bit-identical results to 0.3.0.

## 0.3.0 - 2026-11-03

Radiance parity established and archived. Foton's purpose is now stated:
near-real-time DF, DA, UDI and sDA for single zones, for teaching, with
Radiance as the correctness reference ([purpose and plan](docs/purpose-and-plan.md)).

- Default to eight diffuse bounces (was one), matching the Radiance reference
  the suite converges; the September comparison had read 17.6 % low for this
  reason alone.
- `final` quality preset: 256 direct samples per patch and 65,536 indirect
  samples at Tregenza density, scaled with the square of the sky density
  (262,144 at Reinhart MF:2) so per-patch noise is the same at both; about
  1.3 s / 5 s on 2,020 sensors on an M4 Pro. `quality_preset()` exposes it.
- Honeybee geometry is recentred before the float32 cast; bounce origins are
  kept inside concave corners; the diffuse trace is tiled so cancellation and
  GPU watchdogs are honoured.
- 106-scene architectural validation corpus (controls, form, orientation,
  openings, shading, context, materials, room connections, the acceptance
  model and a 16-scene teaching category) with a release suite that converges
  `rfluxmtx` references adaptively and gates coefficients, annual illuminance,
  DA/cDA/UDI/sDA and reference stability.
- Archived Metal campaign on the shipped preset: 204 of 212 cases pass; the
  eight outside the gates (rooms lit only through internal glazing, one
  12 m room neither engine converges at 8 bounces) are documented as open.
  The teaching category passes 32 of 32 under Gothenburg, Phoenix and
  Seattle weather; the two extra EPWs ship under `epw/`.
- The two-phase patch sun is measured against Honeybee's traced sun at about
  1 pp of DA and 1 % of energy; a separate direct-sun pass stays on the plan.
- Grasshopper packaging with source-matched components, release evidence
  tooling, public-beta acceptance workflow, hardened Honeybee bridge with
  binary Radiance I/O, `--radiance-parameters` on the stock-recipe script.
- Cinematic viewer demo with procedural geometry and a solar path.
- Vulkan: the first run on hardware (an NVIDIA T4) found and fixed two
  backend bugs, a dropped `ash::Entry` that unloaded the loader and crashed
  on Linux, and an acceleration-structure descriptor written without a
  count, which left every ray missing.
- Release evidence lives in the repository and is checked by
  `scripts/verify_release_evidence.py` on every tag; no self-hosted runners.
  A campaign's converged Radiance references can be exported as a bundle and
  reused by another backend or machine with
  `validate_release_suite.py --reuse-references`; the corpus-4 bundle is
  published as the `references-corpus4-2026-11-03` pre-release.

Tested: Metal on an Apple M4 Pro (macOS 26.6) and Vulkan on an NVIDIA Tesla
T4 (Linux), both 204 of 212 cases against the same converged Radiance 5.4a
references with the same eight documented open cases, agreeing with each
other within 0.008 percentage points of energy bias; Rhino 8.35 on macOS with
Ladybug Tools 1.9.0 for the Grasshopper checklist. Unverified: Windows on any
backend, Rhino on Windows, other GPUs. Details and the evidence files are in
[release readiness](docs/release-readiness.md#tested-platforms-for-030).

## 0.2.0 - 2026-08-12

Expanded the Python and Honeybee integration for annual daylight analysis.

- Added the Honeybee annual-daylight protocol, client, recipe, and result helpers.
- Added sensor-grid adaptation, weather preparation, validation, and Radiance comparison tools.
- Added the `foton-honeybee` command and packaged `honeybee_foton` compatibility bridge.
- Added annual timing display improvements and expanded Python, Rust, and viewer test coverage.

## 0.1.0 - 2026-07-31

Initial public release.

- Automatic Metal, Vulkan, or deterministic CPU backend selection.
- Native Metal and Vulkan ray-query transport with resident acceleration structures.
- Direct visibility, diffuse multi-bounce transport, thin glass, and coefficient export.
- Tregenza and Reinhart MF:2 sky bases.
- GPU annual reduction for daylight autonomy and static area-weighted sDA.
- Honeybee geometry conversion and native Radiance comparison tools.
- Reproducible hardware benchmarks, including a 1,000-room/25,000-sensor fixture.
- Local Three.js daylight viewer.
