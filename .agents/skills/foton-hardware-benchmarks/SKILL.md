---
name: foton-hardware-benchmarks
description: Run, diagnose, and publish Foton hardware benchmarks with realistic Honeybee/Radiance comparisons, annual metrics, resident-scene reuse, and README hardware/result tables. Use when benchmarking a new CPU/GPU, adding fixtures, investigating Radiance n/a values, clearing or appending benchmark rows, or comparing Metal/Vulkan performance over time.
---

# Foton Hardware Benchmarks

Use `scripts/benchmark_hardware.py` as the canonical entry point. Published runs must
use a hardware backend; `auto` may select Metal or Vulkan but must not silently record
the reference backend as a hardware result.

Install project and comparison dependencies with:

```text
python -m pip install -e '.[honeybee]'
```

Run a publishable benchmark:

```text
python scripts/benchmark_hardware.py --backend auto --append-readme
```

Use `--quick` only for smoke testing. Keep the standard sample and bounce settings for
rows intended to compare computers over time.

## Required Fixture Set

Retain all five README rows for each run:

1. Honeybee shaded-shoebox direct visibility against Radiance.
2. Multi-bounce diffuse plus thin-glass daylight coefficients.
3. Annual illuminance plus DA/sDA comparison.
4. Cold 1,000-room, 25,000-sensor resident scene.
5. Cached rerun proving resident BLAS/TLAS reuse.

Record engine timings, total wall time, Radiance time, accuracy, backend, GPU, CPU,
core count, RAM, OS, Python, and engine version. The 1,000-room fixture is a performance
comparison; do not invent an accuracy metric for it.

## Radiance Discovery

Resolve `oconv` and `rcontrib` in this order:

1. `--radiance-bin`
2. `RADIANCE_BIN`
3. Honeybee Radiance configuration
4. `/Applications/OpenStudio-*/Radiance/bin`
5. `PATH`

For OpenStudio, a typical explicit value is
`/Applications/OpenStudio-3.9.0/Radiance/bin`. Preserve `RAYPATH`, honor
`RADIANCE_LIB`, and include the sibling `../lib` directory when it contains
`rayinit.cal`. Treat version-probe errors as metadata, not benchmark failure, when the
actual simulation commands succeed.

Do not leave Radiance as `n/a` for the large-scene cold or cached rows when a comparable
Radiance path exists. Distinguish an intentional non-comparison from a failed command,
and preserve the failure log.

## Outputs and README

Each run writes JSON, Markdown, command logs, and comparison artifacts under
`benchmarks/results/<run-id>/`. On subprocess failure, report the log path and output
tail.

Append hardware metadata only between `BENCHMARK_HARDWARE` markers and result rows only
between `BENCHMARK_RESULTS` markers. Preserve historical rows and deduplicate exact
rows. Clear benchmark tables only when explicitly requested, leaving headers and
markers intact.

Before accepting appended rows, confirm the hardware table contains the run ID and all
five result rows use the same run ID.
