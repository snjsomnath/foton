# Changelog

All notable Foton changes are recorded here.

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
