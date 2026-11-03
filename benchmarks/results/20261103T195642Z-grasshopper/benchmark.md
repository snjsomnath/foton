# Grasshopper Round-Trip Benchmark

- Recorded: `2026-11-03 19:56:42Z`
- Machine: MacBook Pro, Apple M4 Pro, 24 GB
- GPU / backend: Apple M4 Pro / `metal`
- Foton: `0.3.0`, `final` preset, 8 bounces, MF:1
- Weather: `gothenburg.epw`
- Repeats per scene: 3 (median shown, seconds)
- Path: `foton_gh.run_annual_daylight` in CPython; Rhino not running

| Stage | teaching_office (96 sensors) | acceptance (2020 sensors) | office_floors (9216 sensors) |
| --- | ---: | ---: | ---: |
| HBJSON export | 0.002 | 0.017 | 0.126 |
| Input staging and hashing | 0.007 | 0.008 | 0.009 |
| Process start-up and imports | 0.114 | 0.115 | 0.136 |
| Scene build and GPU upload | 0.156 | 0.180 | 0.556 |
| Annual sky matrix | 0.081 | 0.082 | 0.083 |
| GPU tracing | 0.055 | 0.827 | 4.518 |
| Metric reduction | 0.000 | 0.000 | 0.002 |
| Result writing | 0.034 | 0.065 | 0.566 |
| Process exit | 0.017 | 0.020 | 0.048 |
| Metric loading in the component | 0.002 | 0.005 | 0.173 |
| **Component total** | 0.472 | 1.325 | 6.211 |
| Honeybee AnnualDaylight load + DA | 0.021 | 0.044 | 0.175 |
| **Round trip total** | 0.494 | 1.367 | 6.388 |
| Output folder size (MB) | 3.4 | 37.7 | 167.2 |
