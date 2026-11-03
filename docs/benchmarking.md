# Benchmarking and Validation

The public-beta release gate is the [90-scene architectural validation suite](release-readiness.md).
The README speed figures come from the hardware timing benchmark below; accuracy
claims come from the validation suite. Re-run current code before making accuracy
or performance claims.

The comparison scripts keep unlike transport stages separate. Direct visibility is
binary; diffuse coefficients and annual illuminance use NMBE and CV(RMSE).

## Hardware timing benchmark

```bash
python scripts/benchmark_hardware.py --backend auto
```

The suite times cold annual daylight runs at Foton's shipped defaults (the
`final` preset, MF:1 sky, default bounce depth) on four Honeybee models of
increasing size:

1. `teaching_office`: a 1-room, 96-sensor corpus scene.
2. `courtyard_rooms`: a 4-room, 112-sensor corpus scene with shading.
3. `acceptance`: the 3-room, 2,020-sensor acceptance model.
4. `office_floors`: a generated double-loaded office block, 4 storeys and 256
   rooms, each with one 40 % glazed facade and a 1 m sensor grid (9,216 sensors).

Each repeat builds a new `HoneybeeStudy` and runs `annual_daylight` to written
DA/UDI results, so it includes model preparation, acceleration-structure build,
GPU upload, tracing and metric reduction. One unrecorded warm-up run compiles
GPU pipelines and fills the weather cache. The report gives the median, minimum
and maximum of five repeats. Pass `--scenes` to choose other corpus scenes.

Each run writes `benchmark.json` and `benchmark.md` under
`benchmarks/results/<run-id>/`. That folder is ignored by git. The one committed run,
[`20261103T195604Z-CM-GHHXPN239T`](../benchmarks/results/20261103T195604Z-CM-GHHXPN239T/benchmark.md),
is the source of the speed figures in the README.

The benchmark does not run Radiance. Speed against Radiance is recorded by the
validation suite, which times Honeybee's stock annual-daylight recipe on the
acceptance model (`compatibility.stock.performance` in each campaign's
`suite.json`). `scripts/benchmark_large_scene.py` remains available for the
instanced 1,000-room resident-scene stress test.

## Grasshopper round trip

```bash
python scripts/benchmark_grasshopper.py --repeats 3
```

This times the path the Foton Annual Daylight component takes, through
`grasshopper_foton.foton_gh.run_annual_daylight`: HBJSON export, input staging,
the `foton-honeybee annual-daylight --jsonl` subprocess and loading the metric
files back. The subprocess's JSONL progress events are timestamped as they
arrive, which splits its time into start-up, scene build, sky, tracing, metric
reduction and result writing. A last step reads the results folder with
Honeybee's `AnnualDaylight` loader, as the Honeybee/Ladybug result components
do. It runs in CPython without Rhino, so IronPython serialisation and DataTree
conversion inside Grasshopper are not measured.

## Quick smoke run

```bash
python scripts/benchmark_hardware.py --quick
```

The quick mode uses the `preview` preset and a single repeat. Do not mix quick
and default rows when comparing hardware.

## Interpreting accuracy

- Direct visibility: mismatch count and cosine/solid-angle-weighted visible energy.
- Coefficients: NMBE and CV(RMSE) over the complete RGB coefficient matrix.
- Annual: occupied-hour illuminance NMBE/CV(RMSE), DA difference, and sDA percentage
  point difference.

## Honeybee annual-daylight acceptance

`test_models/test.hbjson` is the practitioner-facing acceptance model. Compare a
Foton export and the standard Honeybee Radiance `annual-daylight` result with:

- 3 cleanly separated Rooms and 4 Apertures;
- 3 SensorGrids and 2,020 sensors in immutable HBJSON order;
- `classroom_01` at indices 0–174, `office_02` at 175–1134, and
  `office_01` at 1135–2019;
- one paired 0.88-transmittance interior aperture between the offices; and
- a sealed classroom that must remain physically dark.

```python
from foton.honeybee import compare_annual_daylight

report = compare_annual_daylight(
    "simulation/foton-annual",
    "simulation/radiance-annual",
    model="test_models/test.hbjson",
    foton_seconds=1.2,
    radiance_seconds=23.0,
    output_folder="simulation/comparison",
    oracle="stock",
)
assert report["passed"], report
```

The stock-oracle report gates grid IDs, counts, sun-up-hour ordering, and per-grid
absolute NMBE below 5%. The 10× end-to-end speed target is reported separately
and does not affect numerical correctness. Sensor CV(RMSE),
all five annual metric errors, and area-weighted sDA remain published
diagnostics because a single stock Radiance run is stochastic. Pass
`oracle="converged"` for the strict CV(RMSE), metric, and sDA gates after the
coefficient oracle has converged. Both modes record percentile and maximum
sensor-hour errors so aggregate passes cannot conceal outliers.
It additionally loads Foton output through the official
`AnnualDaylight` result API and requires recomputed DA/cDA/UDI values to agree
within 0.05 percentage points.

Run the coefficient-stage oracle against the exact scene, sky dome, octree, and
sensor files generated by a completed Honeybee recipe:

```bash
python scripts/validate_honeybee_coefficients.py \
  --model test_models/test.hbjson \
  --honeybee-project simulation/radiance-annual \
  --output simulation/coefficient-parity \
  --radiance-replicates 4 \
  --maximum-radiance-replicates 8 \
  --radiance-ambient-divisions 20000 \
  --direct-oracle-samples 256
```

The harness compares center-ray visibility, an independently ray-integrated
direct coefficient oracle, and the isolated one-bounce delta. It starts with
four `-ad 20000` Radiance runs and automatically expands to eight when the two
replicate-half means exceed 5% RMS-normalized RMSE or 1% energy bias. An
unstable oracle is reported as such instead of being treated as a Foton failure.
The stock `-ad 5000` recipe remains a separate compatibility comparison.
