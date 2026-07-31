# Foton

Hardware-adaptive, backend-neutral daylight analysis engine for progressive daylight
coefficients, daylight factor, daylight autonomy, and static sDA.

## Install

The product and import name is Foton. The PyPI distribution is `foton-daylight`
because the shorter `foton` project name is owned by another publisher.

```bash
python -m pip install foton-daylight
```

```python
from foton import Engine

engine = Engine()
print(engine.capabilities())
```

See [installation](docs/installation.md), [backend requirements](docs/backends.md),
[Python API](docs/python-api.md), and [benchmarking](docs/benchmarking.md).

## Implemented

- Typed Rust scene contracts for instanced triangle meshes, materials, and sensors.
- Canonical Tregenza 146 and Reinhart MF:2 578 sky mapping including ground.
- Exact MF:2-to-Tregenza parent aggregation and deterministic sample keys.
- Lambertian transport and Radiance-compatible visible-transmittance conversion with
  angular thin-glass interface effects.
- Streamed annual metrics with explicit weighted occupancy schedules.
- Native Metal BLAS/TLAS construction, direct ray-query visibility, and tiled GPU
  annual reduction through runtime-compiled MSL.
- Vulkan 1.3 BLAS/TLAS construction and SPIR-V ray-query compute pipelines for
  NVIDIA, AMD, and Intel GPUs on Linux and Windows.
- Resident scene handles that reuse acceleration structures across analyses and
  revisioned instance updates.
- Async PyO3 jobs with cancellation, supersession, copied NumPy ownership, snapshots,
  GIL release while waiting, and opt-in coefficient export.
- Canonical shoebox and generated 1,000-room/25,000-sensor fixtures.

Direct visibility, multi-bounce diffuse and thin-glass transport, and annual metric
reduction execute on Metal or Vulkan. The deterministic CPU backend and Radiance
remain validation oracles.

## Development

```bash
cargo test -p daylight-core -p daylight-metal -p daylight-vulkan -p daylight-cli
cargo check -p daylight-python --features extension-module
cargo run -p daylight-cli -- hardware
cargo run -p daylight-cli -- fixture --output tests/fixtures/shoebox.json
python -m unittest discover -s validation
```

Build the Python extension from source:

```bash
python -m pip install -e .
```

Compare a Honeybee shaded shoebox against native Radiance direct visibility:

```bash
python scripts/compare_honeybee_shoebox.py --auto-grid
```

## Hardware Benchmarks

Run the reproducible Honeybee/Radiance benchmark after installing the Honeybee
extra and making Radiance `oconv` and `rcontrib` available on `PATH` (or set
`RADIANCE_BIN`). Bundled OpenStudio installations under `/Applications` are
detected automatically:

```bash
python -m pip install -e '.[honeybee]'
python scripts/benchmark_hardware.py --backend auto --append-readme
```

Each run writes a self-contained folder under `benchmarks/results/` with command
logs, `benchmark.json`, and `benchmark.md`. It executes four versioned stages:

| Stage | Fixture | Validation |
| --- | --- | --- |
| Direct visibility | Honeybee shaded shoebox, aperture, overhang, fins, 216 sensors | Binary patch-center ray mismatches and weighted visible energy against Radiance |
| Full transport | Same room with 0.6 visible-transmittance glass and diffuse bounces | Coefficient NMBE and CV(RMSE) against `rcontrib` |
| Annual metrics | Both coefficient matrices multiplied by the same deterministic 8,760-hour Tregenza sky and 08:00–18:00 schedule | Occupied illuminance NMBE/CV(RMSE), DA, area-weighted sDA, and GPU/CPU reduction agreement |
| Large scene | One resident shoebox mesh instanced into 1,000 rooms with 25,000 sensors | Cold and cached scene, tracing, annual-reduction, and wall-clock timings |

Use `--quick` for a 256-sample, one-bounce smoke benchmark. Use an explicit
`--backend metal` or `--backend vulkan` to require that device; the run fails
rather than silently benchmarking the CPU reference. `--append-readme` adds one
hardware row and five fixture rows below, while the JSON report remains the
detailed artifact.

### Hardware

<!-- BENCHMARK_HARDWARE:START -->
| Run | Date (UTC) | Host | OS | Model | CPU | Cores | RAM | GPU | Backend | Engine |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| 20260731T054146Z-CM-GHHXPN239T | 2026-07-31 05:42:00Z | CM-GHHXPN239T | macOS 26.5.2 | MacBook Pro | Apple M4 Pro | 14 | 24 GB | Apple M4 Pro | metal | 0.1.0 |
<!-- BENCHMARK_HARDWARE:END -->

### Results

<!-- BENCHMARK_RESULTS:START -->
| Run | Fixture | Scale | Samples / bounces | Accuracy vs Radiance | Scene / AS | Trace | Annual | Wall | Radiance |
| --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 20260731T054146Z-CM-GHHXPN239T | Honeybee direct visibility | 216 sensors × 146 patches | 0 / 0 | 13 mismatches; 2.477% energy | 0.00 ms | 0.17 ms | 0.06 ms | n/a | 66.27 ms |
| 20260731T054146Z-CM-GHHXPN239T | Diffuse + thin glass coefficients | 216 sensors × 146 patches | 4096 / 2 | NMBE 5.295%; CV(RMSE) 344.379% | 0.00 ms | 5.79 ms | 7.81 ms | 30.95 ms | 3574.31 ms |
| 20260731T054146Z-CM-GHHXPN239T | Annual illuminance + DA/sDA | 216 sensors × 8760 hours | 4096 / 2 | NMBE 5.193%; CV(RMSE) 26.955%; sDA Δ 0.00 pp | 0.00 ms | 5.79 ms | 7.81 ms | 30.95 ms | 3583.38 ms |
| 20260731T054146Z-CM-GHHXPN239T | 1,000-room resident scene | 1000 rooms / 25000 sensors | 64 / 1 | performance fixture | 5.00 ms | 18.28 ms | 2.10 ms | 63.86 ms | 4621.42 ms |
| 20260731T054146Z-CM-GHHXPN239T | 1,000-room resident scene (cached) | 1000 rooms / 25000 sensors | 64 / 1 | resident BLAS/TLAS reuse | 0.00 ms | 4.24 ms | 2.10 ms | 39.17 ms | 4431.31 ms |
<!-- BENCHMARK_RESULTS:END -->

## Local Three.js viewer

Install the native extension and local viewer dependencies:

```bash
python -m pip install -e '.[viewer]'
cd viewer && npm install
```

Run the Python service and Vite frontend together:

```bash
cd viewer && npm run dev
```

Open `http://127.0.0.1:5173`, upload an hourly EPW, and edit the parametric
shoebox. The viewer runs a 64-sample Tregenza preview during interaction and a
4,096-sample Reinhart MF:2 refinement after the controls are idle. Radiance
`gendaymtx` must be on `PATH` or under `RADIANCE_BIN`; daylight transport remains
native Metal or Vulkan, selected from the GPU vendor.

For a single-process local build:

```bash
cd viewer && npm run build
foton-viewer
```

Release maintainers should also read [the release process](docs/releasing.md).
