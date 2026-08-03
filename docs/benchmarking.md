# Benchmarking and Validation

The benchmark suite keeps unlike transport stages separate. Direct visibility is
binary; diffuse coefficients and annual illuminance use NMBE and CV(RMSE).

## Full hardware benchmark

```bash
python scripts/benchmark_hardware.py \
  --backend auto \
  --radiance-bin /path/to/radiance/bin \
  --append-readme
```

The suite runs:

1. Honeybee shaded-shoebox direct visibility against Radiance.
2. Multi-bounce diffuse and thin-glass coefficients against `rcontrib`.
3. An 8,760-hour deterministic annual propagation with DA and area-weighted sDA.
4. A cold 1,000-room/25,000-sensor resident-scene benchmark.
5. A cached resident-scene rerun and cached Radiance-octree reference.

Each run writes `benchmark.json`, `benchmark.md`, command logs, coefficient artifacts,
and Radiance scene files under `benchmarks/results/<run-id>/`.

## Quick smoke run

```bash
python scripts/benchmark_hardware.py --quick
```

The quick mode keeps the fixture structure but lowers transport samples. Do not mix
quick and default rows when comparing hardware.

## Interpreting accuracy

- Direct visibility: mismatch count and cosine/solid-angle-weighted visible energy.
- Coefficients: NMBE and CV(RMSE) over the complete RGB coefficient matrix.
- Annual: occupied-hour illuminance NMBE/CV(RMSE), DA difference, and sDA percentage
  point difference.
- Large scene: performance only unless an explicit coefficient comparison is added.

The deterministic annual sky is intended for repeatable hardware comparisons, not as
a climate-specific LM-83 claim.

## Honeybee annual-daylight acceptance

`test_models/test.hbjson` is the practitioner-facing acceptance model. Compare a
Foton export and the standard Honeybee Radiance `annual-daylight` result with:

```python
from foton.honeybee import compare_annual_daylight

report = compare_annual_daylight(
    "simulation/foton-annual",
    "simulation/radiance-annual",
    model="test_models/test.hbjson",
    foton_seconds=1.2,
    radiance_seconds=23.0,
    output_folder="simulation/comparison",
)
assert report["passed"], report
```

The report enforces grid IDs, counts, sun-up-hour ordering, per-grid NMBE and
CV(RMSE), all five annual metric errors, area-weighted sDA, and the 10×
end-to-end speed gate. It also records percentile and maximum sensor-hour
errors in JSON and Markdown so aggregate passes cannot conceal outliers.
