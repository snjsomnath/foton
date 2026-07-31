# Hardware Benchmark

- Recorded: `2026-07-31 05:31:56Z`
- Host: `CM-GHHXPN239T`
- CPU: `Apple M4 Pro`
- GPU: ` Apple M4 Pro`
- Selected backend: `metal`
- Large scene: `1000 rooms / 25000 sensors`
- Direct mismatched rays: `13`
- Direct weighted visible-energy error: `2.4774%`
- Full transport NMBE: `5.2660%`
- Full transport CV(RMSE): `345.7627%`
- Engine tracing: `5.7727 ms`
- Radiance rcontrib: `3688.3753 ms`

## README hardware row

| 20260731T053150Z-CM-GHHXPN239T | 2026-07-31 05:31:56Z | CM-GHHXPN239T | Darwin 26.5.2 | MacBook Pro | Apple M4 Pro | 14 | 24 GB |  Apple M4 Pro | metal | 0.1.0 |

## README benchmark rows

| 20260731T053150Z-CM-GHHXPN239T | Honeybee direct visibility | 216 sensors × 146 patches | 0 / 0 | 13 mismatches; 2.477% energy | 0.00 ms | 0.17 ms | 0.06 ms | n/a | 72.54 ms |
| 20260731T053150Z-CM-GHHXPN239T | Diffuse + thin glass coefficients | 216 sensors × 146 patches | 4096 / 2 | NMBE 5.266%; CV(RMSE) 345.763% | 0.00 ms | 5.77 ms | 8.32 ms | 35.35 ms | 3688.38 ms |
| 20260731T053150Z-CM-GHHXPN239T | Annual illuminance + DA/sDA | 216 sensors × 8760 hours | 4096 / 2 | NMBE 5.315%; CV(RMSE) 27.416%; sDA Δ 0.00 pp | 0.00 ms | 5.77 ms | 8.32 ms | 35.35 ms | n/a |
| 20260731T053150Z-CM-GHHXPN239T | 1,000-room resident scene | 1000 rooms / 25000 sensors | 64 / 1 | performance fixture | 0.00 ms | 12.25 ms | 2.19 ms | 59.43 ms | n/a |
