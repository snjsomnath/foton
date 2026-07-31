---
name: ladybug-epw-sky-matrix
description: Validate EPW weather data with Ladybug Core and generate Radiance-compatible Perez sky matrices with gendaymtx. Use when preparing annual Tregenza or Reinhart weather inputs for Metal, Vulkan, Radiance, DF, DA, or sDA workflows.
---
# Ladybug EPW Sky Matrix

Validate the EPW with `ladybug-core`, then invoke Radiance `gendaymtx` to preserve the
official Perez model and patch ordering. Do not substitute an equal-area or Fibonacci
hemisphere because its rows will not align with `rcontrib`.

Use `tregenza` for 146 rows (ground plus 145 sky patches) or `reinhart-mf2` for 578
rows (ground plus 577 sky patches). The NumPy output shape is
`[patch, timestep, rgb]`; patch 0 is ground. Keep RGB through the matrix product and
apply the Radiance photopic conversion only when producing illuminance.

```text
python scripts/gen_sky_matrix.py --epw weather.epw --basis tregenza \
  --out build/sky.npy --metadata-out build/sky.json
```

Install `ladybug-core` and NumPy from `requirements.txt`, and provide `gendaymtx` on
`PATH` or with `--gendaymtx`. Use visible output for daylight metrics and solar output
only for solar-energy workflows.

Radiance binaries may also need their function-library path. Preserve `RAYPATH`, honor
`RADIANCE_LIB`, and add a sibling `../lib` directory when it contains `rayinit.cal`.
