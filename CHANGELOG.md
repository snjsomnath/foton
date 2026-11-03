# Changelog

All notable Foton changes are recorded here.

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
