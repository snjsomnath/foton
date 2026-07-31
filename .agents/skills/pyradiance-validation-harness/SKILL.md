---
name: pyradiance-validation-harness
description: Validate Metal, Vulkan, or other GPU visibility, daylight-coefficient, and annual-illuminance outputs against Radiance references. Use after changing traversal, Honeybee geometry conversion, acceleration structures, materials, sampling, sky ordering, matrix multiplication, or daylight metrics.
---
# Pyradiance Validation Harness

Run `scripts/validate_dc.py` with a Radiance `.oct`, sensor `.pts`, and GPU CSV. The
GPU CSV must contain `sensor_index`, `sky_patch_index`, and either `coefficient` or
`value`; indices are zero-based. Select the same basis used by the sky matrix:
`tregenza` means 146 rows including ground, and `reinhart-mf2` means 578 rows including
ground. Never compare matrices with inferred or mismatched patch ordering.

Validate in stages: direct visibility first, full daylight coefficients second, and
annual illuminance last. Visibility uses maximum absolute error; coefficient and annual
comparisons use NMBE and CV(RMSE). Use `--fail-on-threshold` in CI.

Direct visibility is a binary `[sensor, sky_patch]` transport diagnostic. It does not
produce illuminance, DF, DA, cDA/csDA, or sDA, and it is not an image. Store both
matrices plus JSON/Markdown comparison metadata. Add visual heatmaps only as derived
debug artifacts; never substitute them for numerical comparisons.

Supply the complete modifier and calculation arguments through
`RADIANCE_RCONTRIB_ARGS` or `--rcontrib-args`. Live RGB output is converted to photopic
illuminance with Radiance's 179 lm/W weighting. For a precomputed scalar reference, pass
`--reference`.

Radiance executables are external and require their function library. Preserve
`RAYPATH`, honor `RADIANCE_LIB`, and detect a sibling `../lib` directory containing
`rayinit.cal` when an executable is under `.../bin`. Pass the same environment to every
Radiance subprocess.

```text
python scripts/validate_dc.py --oct scene.oct --pts sensors.pts \
  --gpu gpu_coefficients.csv --basis tregenza --mode daylight-coefficient \
  --out validation_report.md --fail-on-threshold
```

Do not expect one-ray binary sky visibility to agree with a multi-bounce Radiance
daylight-coefficient matrix. Compare like-for-like transport stages.

For binary edge rays, report total mismatches, identified edge-ray mismatches,
non-edge mismatches, and solid-angle/cosine-weighted visible-energy error separately.
Do not hide edge disagreements, but do not treat isolated exact-edge classification
differences as diffuse transport bias.
