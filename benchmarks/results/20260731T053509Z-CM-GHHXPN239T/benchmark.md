# Hardware Benchmark

- Recorded: `2026-07-31 05:35:23Z`
- Host: `CM-GHHXPN239T`
- CPU: `Apple M4 Pro`
- GPU: `Apple M4 Pro`
- Selected backend: `metal`
- Large scene: `1000 rooms / 25000 sensors`
- Direct mismatched rays: `13`
- Direct weighted visible-energy error: `2.4774%`
- Full transport NMBE: `5.0366%`
- Full transport CV(RMSE): `343.9671%`
- Engine tracing: `5.8159 ms`
- Radiance rcontrib: `3614.0193 ms`

## README hardware row

| 20260731T053509Z-CM-GHHXPN239T | 2026-07-31 05:35:23Z | CM-GHHXPN239T | macOS 26.5.2 | MacBook Pro | Apple M4 Pro | 14 | 24 GB | Apple M4 Pro | metal | 0.1.0 |

## README benchmark rows

| 20260731T053509Z-CM-GHHXPN239T | Honeybee direct visibility | 216 sensors × 146 patches | 0 / 0 | 13 mismatches; 2.477% energy | 0.00 ms | 0.17 ms | 0.06 ms | n/a | 65.19 ms |
| 20260731T053509Z-CM-GHHXPN239T | Diffuse + thin glass coefficients | 216 sensors × 146 patches | 4096 / 2 | NMBE 5.037%; CV(RMSE) 343.967% | 0.00 ms | 5.82 ms | 7.85 ms | 30.68 ms | 3614.02 ms |
| 20260731T053509Z-CM-GHHXPN239T | Annual illuminance + DA/sDA | 216 sensors × 8760 hours | 4096 / 2 | NMBE 5.016%; CV(RMSE) 26.344%; sDA Δ 0.00 pp | 0.00 ms | 5.82 ms | 7.85 ms | 30.68 ms | 3623.86 ms |
| 20260731T053509Z-CM-GHHXPN239T | 1,000-room resident scene | 1000 rooms / 25000 sensors | 64 / 1 | performance fixture | 6.62 ms | 12.37 ms | 2.11 ms | 55.78 ms | 4641.37 ms |
| 20260731T053509Z-CM-GHHXPN239T | 1,000-room resident scene (cached) | 1000 rooms / 25000 sensors | 64 / 1 | resident BLAS/TLAS reuse | 0.00 ms | 4.18 ms | 2.00 ms | 38.96 ms | 4468.86 ms |
