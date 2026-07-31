# Full GPU Transport Comparison

- Basis: `tregenza`
- Matrix shape: `[216, 146, 3]`
- Samples: `65536`
- Diffuse bounces: `2`
- Radiance ambient bounces: `3`
- Glass visible transmittance: `None`
- Transport backend: `metal`
- Reference fallback: `False`
- NMBE: `-0.2283%`
- CV(RMSE): `326.3559%`
- Mean absolute error: `0.00035175266`
- Maximum absolute error: `0.11164817`
- Uniform-sky sensor NMBE: `-0.2283%`
- Uniform-sky sensor CV(RMSE): `25.9278%`
- Metal tracing: `24.8925 ms`
- Radiance rcontrib: `53459.2829 ms`
