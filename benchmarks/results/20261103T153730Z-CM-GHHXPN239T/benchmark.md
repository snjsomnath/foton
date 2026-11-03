# Hardware Benchmark

- Recorded: `2026-11-03 15:37:56Z`
- Machine: MacBook Pro, Apple M4 Pro, 24 GB
- GPU / backend: Apple M4 Pro / `metal`
- Foton: `0.3.0`
- Settings: `{"direct_samples": 256, "maximum_bounces": 8, "maximum_samples": 65536, "sky_density": 1}`
- Weather: `gothenburg.epw`
- Repeats per scene: 5 (median shown)

| Scene | Rooms | Sensors | Cold annual run | GPU tracing |
| --- | ---: | ---: | ---: | ---: |
| teaching_office | 1 | 96 | 0.16 s | 0.05 s |
| courtyard_rooms | 4 | 112 | 0.20 s | 0.07 s |
| acceptance | 3 | 2020 | 1.42 s | 1.25 s |
| office_floors | 256 | 9216 | 2.93 s | 1.51 s |
