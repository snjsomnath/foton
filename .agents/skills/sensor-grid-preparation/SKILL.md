---
name: sensor-grid-preparation
description: Validate, normalize, index, and serialize per-room Radiance sensor grids for large Vulkan daylight scenes. Use when generating or auditing sensor coordinates, normals, room ownership, spacing, or GPU upload buffers.
---
# Sensor Grid Preparation

Run `scripts/prepare_sensors.py` before GPU or Radiance simulations. Input rows must
contain at least six whitespace-separated values: `x y z nx ny nz`; blank lines and
lines beginning with `#` are ignored. Extra columns are ignored.

The output CSV uses stable zero-based `room_index` and `sensor_index` values. The NumPy
output has shape `[sensor_count, 6]` and columns `[x, y, z, nx, ny, nz]`. Reject
zero-length normals and normalize normals by default. Use `--preserve-normal-length`
only when reproducing a legacy dataset.

```text
python scripts/prepare_sensors.py --input sensors.pts \
  --csv-out build/sensors.csv --npy-out build/sensors.npy \
  --metadata-out build/sensors.json --room-index 42
```

Use one room index per batch and concatenate batches explicitly in engine preprocessing.
Do not encode room identity in Vulkan's 8-bit TLAS cull mask.
