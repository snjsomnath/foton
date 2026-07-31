# Hardware Benchmark

- Recorded: `2026-07-31 05:42:00Z`
- Host: `CM-GHHXPN239T`
- CPU: `Apple M4 Pro`
- GPU: `Apple M4 Pro`
- Selected backend: `metal`
- Large scene: `1000 rooms / 25000 sensors`
- Direct mismatched rays: `13`
- Direct weighted visible-energy error: `2.4774%`
- Full transport NMBE: `5.2952%`
- Full transport CV(RMSE): `344.3788%`
- Engine tracing: `5.7920 ms`
- Radiance rcontrib: `3574.3131 ms`

## README hardware row

| 20260731T054146Z-CM-GHHXPN239T | 2026-07-31 05:42:00Z | CM-GHHXPN239T | macOS 26.5.2 | MacBook Pro | Apple M4 Pro | 14 | 24 GB | Apple M4 Pro | metal | 0.1.0 |

## README benchmark rows

| 20260731T054146Z-CM-GHHXPN239T | Honeybee direct visibility | 216 sensors × 146 patches | 0 / 0 | 13 mismatches; 2.477% energy | 0.00 ms | 0.17 ms | 0.06 ms | n/a | 66.27 ms |
| 20260731T054146Z-CM-GHHXPN239T | Diffuse + thin glass coefficients | 216 sensors × 146 patches | 4096 / 2 | NMBE 5.295%; CV(RMSE) 344.379% | 0.00 ms | 5.79 ms | 7.81 ms | 30.95 ms | 3574.31 ms |
| 20260731T054146Z-CM-GHHXPN239T | Annual illuminance + DA/sDA | 216 sensors × 8760 hours | 4096 / 2 | NMBE 5.193%; CV(RMSE) 26.955%; sDA Δ 0.00 pp | 0.00 ms | 5.79 ms | 7.81 ms | 30.95 ms | 3583.38 ms |
| 20260731T054146Z-CM-GHHXPN239T | 1,000-room resident scene | 1000 rooms / 25000 sensors | 64 / 1 | performance fixture | 5.00 ms | 18.28 ms | 2.10 ms | 63.86 ms | 4621.42 ms |
| 20260731T054146Z-CM-GHHXPN239T | 1,000-room resident scene (cached) | 1000 rooms / 25000 sensors | 64 / 1 | resident BLAS/TLAS reuse | 0.00 ms | 4.24 ms | 2.10 ms | 39.17 ms | 4431.31 ms |
