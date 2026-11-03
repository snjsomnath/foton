# Hardware Benchmark

- Recorded: `2026-11-03 19:56:42Z`
- Machine: MacBook Pro, Apple M4 Pro, 24 GB
- GPU / backend: Apple M4 Pro / `metal`
- Foton: `0.3.0`
- Settings: `{"direct_samples": 256, "maximum_bounces": 8, "maximum_samples": 65536, "sky_density": 1}`
- Weather: `gothenburg.epw`
- Repeats per scene: 5 (median shown)

| Scene | Rooms | Sensors | Cold annual run | GPU tracing |
| --- | ---: | ---: | ---: | ---: |
| teaching_office | 1 | 96 | 0.14 s | 0.04 s |
| courtyard_rooms | 4 | 112 | 0.17 s | 0.05 s |
| acceptance | 3 | 2020 | 1.07 s | 0.90 s |
| office_floors | 256 | 9216 | 5.77 s | 4.68 s |
