# Validation

Radiance remains the numerical oracle for transport, glazing, daylight factor, and
annual illuminance. Store generated references outside source control or under a
fixture-specific directory with metadata describing Radiance arguments, sky basis,
units, RGB-to-photopic conversion, schedule, and scene hash.

Compare dense `.npy` or headerless CSV arrays:

```bash
python validation/compare.py \
  --reference reference.npy \
  --candidate candidate.npy \
  --out validation-report.json
```

The command fails unless absolute NMBE is below 5% and CV(RMSE) is below 10%.
The repository skills under `.agents/skills/` provide the Radiance scene, weather,
sensor, and `rcontrib` preparation workflows.

