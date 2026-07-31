---
name: daylight-benchmark-scene
description: Generate deterministic Radiance and Honeybee shoebox scenes, material reflectances, apertures, static shades, and sensor grids for GPU daylight-engine regression tests. Use when creating canonical fixtures or comparing Metal, Vulkan, and Radiance transport stages.
---
# Daylight Benchmark Scene

Generate a fixed shoebox before tuning GPU code. Keep geometry, materials, sensor
positions, sky basis, and Radiance options versioned together so benchmark changes are
intentional.

Run `scripts/generate_shoebox.py` to create:

- `materials.rad` with 70% walls, 20% floor, and 80% ceiling.
- `room.rad` for a 6 m × 9 m × 3 m room with one open south aperture.
- `sensors.pts` at 0.75 m with a 0.5 m grid.
- `scene.json` containing dimensions, counts, and coordinate conventions.

```text
python scripts/generate_shoebox.py --output-dir benchmarks/shoebox-v1
```

Treat this as a geometry/transport fixture, not an LM-83 model. Add glazing, exterior
obstructions, blinds, and occupancy only in separately named benchmark variants.

For Honeybee direct-visibility fixtures, clone and convert the model to metres without
mutating the caller. Triangulate punched opaque parent faces, omit aperture polygons so
openings remain open, and include overhangs, fins, orphaned shades, and shade meshes as
opaque geometry. Feed identical patch-center directions, flattened sensor ordering, and
geometry semantics to the GPU and Radiance paths.
