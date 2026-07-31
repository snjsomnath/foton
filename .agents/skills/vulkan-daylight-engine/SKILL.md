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
