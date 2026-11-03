# Changelog

All notable Foton changes are recorded here.

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
