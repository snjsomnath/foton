# Vulkan Daylight Engine Architecture

## Correctness gates

1. Validate patch directions and unoccluded cosine response analytically.
2. Validate binary direct visibility against a matching zero-bounce reference.
3. Validate diffuse and material transport against Radiance daylight coefficients.
4. Validate tiled annual illuminance, then DF and sDA reductions.
5. Optimize only after each gate is reproducible.

Do not compare one-ray patch visibility with a multi-bounce `rcontrib` matrix.

## Sky and metric contracts

- Tregenza matrix: 146 rows, with ground at index 0 and 145 sky patches.
- Reinhart MF:2 matrix: 578 rows, with ground at index 0 and 577 sky patches.
- Preserve Radiance patch ordering and RGB until photopic conversion.
- Compute DF with a CIE standard overcast sky, not an annual EPW.
- Compute sDA from occupied annual timesteps with area-weighted sensors.

## Vulkan baseline

- Require `VK_KHR_acceleration_structure`, `VK_KHR_ray_query`,
  `VK_KHR_deferred_host_operations`, and buffer device address support.
- Build BLASes for reusable geometry and TLAS instances for placed geometry.
- Use compute shaders with `GL_EXT_ray_query`; terminate direct-visibility rays on the
  first committed hit.
- Keep geometry, material, room, sensor, and patch indices in explicit storage buffers.
- Use synchronization2 barriers for AS build/update and shader reads.

The TLAS instance mask is 8 bits. Use it for broad categories or batches, not as a
unique room identifier for 1000 rooms. Build room-to-instance ranges and dispatch only
dirty/visible room batches; consider multiple TLASes when scene partitioning measures
better than one global TLAS.

## Transport representation

One ray from each sensor to each patch estimates direct visibility or a direct cosine
term only. It is not a full daylight coefficient.

For reusable indirect coefficients, trace paths from sensors and accumulate each path's
throughput into the sky patch where it escapes. Include material reflectance, cosine,
PDF, Russian roulette, and RGB throughput. For interactive previews, use fewer samples
and temporal accumulation; invalidate only affected rooms after geometry changes.

## Annual integration

Use a tiled Vulkan compute kernel for `DC × sky`. CuPy is CUDA-specific and `faer` is a
CPU library, so neither is a portable Vulkan baseline. Treat cooperative-matrix
extensions as an optional optimized path after feature detection.

Do not allocate the complete `[sensor, 8760]` array at large scale. For 216,000 sensors
it occupies about 7.6 GB as float32. Process time in tiles, increment per-sensor occupied
and threshold counters on the GPU, and retain full hourly values only when explicitly
requested.

## Scale budgets

A 6 m × 9 m room on a 0.5 m grid has roughly 216 sensors; 1000 rooms therefore approach
216,000 sensors, not 25,000. A scalar Tregenza DC buffer is about 126 MB at that scale;
RGB is about 378 MB. Reinhart MF:2 is about four times larger.

Tracing 1024 rays for every sensor means more than 220 million rays per global pass
before patch multiplication. Restrict high-sample convergence to dirty rooms, adapt
samples by variance, and publish measured percentile latency rather than a fixed 100 ms
claim.
