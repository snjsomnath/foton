---
name: vulkan-daylight-engine
description: Design and review scalable Vulkan ray-query daylight engines for hundreds to thousands of rooms, including BLAS/TLAS organization, transport stages, GPU matrix tiling, interactive refinement, validation gates, and performance budgets. Use when implementing or optimizing the core real-time engine.
---
# Vulkan Daylight Engine

Read [architecture.md](references/architecture.md) before designing buffers, dispatches,
acceleration structures, indirect sampling, annual integration, or interactive updates.

Implement one transport stage at a time and retain a Radiance-comparable output at each
gate. Use GLSL with `GL_EXT_ray_query` for the baseline Vulkan path. Introduce another
shader language only with an explicit, tested SPIR-V toolchain.

Measure real hardware throughput before promising frame time or convergence latency.
Report room count, sensor count, patch basis, ray count, GPU, VRAM, AS build/update
time, dispatch time, and metric-reduction time together.

## Backend Selection

Keep Python and CLI selection behavior identical:

1. On macOS, select Metal only when the native Metal device is an Apple GPU.
2. Otherwise select the highest-ranked compatible Vulkan device.
3. Fall back deterministically to the CPU reference backend only for `auto`.
4. Fail explicit `metal` or `vulkan` requests with the backend diagnostic.

Accept only discrete or integrated NVIDIA (`0x10DE`), AMD (`0x1002`), or Intel
(`0x8086`) devices. Reject CPU/software Vulkan devices. Require a compute queue,
buffer device address, acceleration structures, deferred host operations, ray query,
and scalar block layout. Rank discrete before integrated devices.

Compare extension names through `CStr::to_bytes()` for the Rust 1.85 baseline.
Capability strings and result metadata must name the selected backend/device and must
not report reference fallback for a GPU result.

Guard Vulkan integration tests with the project GPU environment flag. Keep direct
coefficient energy within 1% of reference and multi-bounce energy within 2%, while
retaining scene-reuse and committed-scene invalidation tests.
