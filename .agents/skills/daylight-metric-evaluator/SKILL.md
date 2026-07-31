---
name: daylight-metric-evaluator
description: Compute daylight factor, per-sensor daylight autonomy, and area-weighted sDA from validated illuminance arrays. Use when evaluating Vulkan or Radiance results, enforcing LM-83-style schedules, or implementing GPU metric reductions.
---
# Daylight Metric Evaluator

Run `scripts/evaluate_metrics.py` on illuminance arrays shaped `[sensor, timestep]`.
Provide an explicit occupied-hour mask when available. For an 8760-hour array, the
fallback mask selects 08:00–18:00 local clock time every day.

Do not run this skill on binary visibility or daylight-coefficient matrices. First
combine coefficients with a compatible weather sky matrix to obtain illuminance, or
consume the engine's equivalent GPU reduction counters. Direct visibility alone cannot
produce DF, DA, cDA/csDA, or sDA.

Compute sDA as an area-weighted spatial percentage. Uniform sensor counting is valid
only for a uniform grid representing equal floor areas. Keep the defaults at 300 lux
for at least 50% of occupied hours unless the analysis specification says otherwise.
Define any continuous daylight-autonomy metric explicitly before implementation;
`cDA`/`csDA` naming and aggregation are not interchangeable with LM-83 sDA.

Compute daylight factor separately under a CIE standard overcast sky:
`DF = 100 × E_interior / E_exterior_horizontal`. Do not derive DF from an annual EPW.

```text
python scripts/evaluate_metrics.py --annual-lux annual.npy \
  --out metrics.json --sensor-out sensor_metrics.csv
```
