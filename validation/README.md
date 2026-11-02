# Validation

For release qualification use the [90-scene architectural suite](../docs/release-readiness.md),
not a single array comparison or historical benchmark. The suite command is:

```bash
python scripts/validate_release_suite.py --backend metal --output artifacts
```

The [architectural corpus](architectural-scenes.md) documents each design question
and the behavioural checks. Browse the generated [sample models](../test_models/architectural/README.md)
or export a fresh set of 90 validated HBJSON files and their coverage/hash manifest:

```bash
python -m validation.scenes --list
python -m validation.scenes --output /tmp/foton-architectural-samples
python -m pytest tests/python/test_architectural_scenes.py tests/python/test_release_readiness.py
```

The release suite now requires 180 cases: all 90 scenes in both sky bases. Each
case retains its architectural question, coverage tags and model counts. Filter
with `--category` or `--scene` for diagnostics; a subset cannot qualify a release.

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
The scripts and `validation/oracle.py` provide scene, weather, sensor and Radiance
preparation. GPU fallback and incomplete oracle convergence cannot qualify a release.
