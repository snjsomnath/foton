# Changelog

All notable Foton changes are recorded here.

## Unreleased

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
