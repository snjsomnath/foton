---
name: metal-raytracing
description: Implement, debug, and validate Apple Metal hardware ray tracing with acceleration structures and MSL intersectors. Use when editing .metal shaders, objc2-metal host code, BLAS/TLAS descriptors, instance metadata, ray masks, or runtime Metal compilation paths.
---

# Metal Ray Tracing

Build ray-tracing code against the language level actually selected by the host,
not against the newest SDK header alone. Keep identity, filtering, and transport
provenance explicit so compiler fallbacks cannot silently change results.

## Workflow

1. Inspect the device, macOS version, SDK, compiler diagnostics, and
   `MTLCompileOptions` used by the host.
2. Identify whether the shader is runtime-compiled or built by an offline Metal
   toolchain. Treat runtime compilation with no explicit language version as the
   compatibility baseline.
3. Audit runtime sources:

   ```bash
   python .agents/skills/metal-raytracing/scripts/check_msl_compat.py \
     crates/daylight-metal/shaders/direct_visibility.metal
   ```

4. Build BLAS resources before TLAS resources. Keep all referenced buffers and
   acceleration structures alive until GPU completion.
5. Compile the smallest pipeline first, then validate analytical rays, a CPU
   reference, and finally Radiance fixtures.
6. Record the actual transport backend and fail validation when hardware
   traversal silently falls back.

## Compatibility Baseline

- Prefer `intersector<triangle_data, instancing>` and its returned
  `intersection_result` for runtime-compiled visibility kernels.
- Enable `accept_any_intersection(true)` only for binary shadow rays. Diffuse,
  reflective, and transparent transport requires the closest committed hit.
- Use `intersection.instance_id` to index metadata only when the metadata array
  is built in the exact TLAS descriptor order. Populate descriptor `userID` too,
  but do not read `user_instance_id` unless the selected MSL version compiles it.
- Reserve instance masks for bitwise geometry-category filtering. Never encode
  arbitrary room identity in masks.
- Avoid `atomic_float` in baseline runtime sources. Use integer fixed-point
  atomics, threadgroup reduction, or explicitly select and verify a language
  level that supports float atomics.
- Treat `intersection_query`, `intersection_params`, candidate/committed query
  methods, and user-instance result fields as version-gated APIs.
- Never use underscored Metal types suggested by diagnostics; they are private
  implementation details.

Read `references/msl-raytracing-compatibility.md` before introducing a
version-gated API or changing instance identity behavior.

## Validation

- Compile every runtime MSL source with the same host options used in production.
- Test misses, front/back faces, category masks, instance-to-metadata mapping,
  transformed instances, empty scenes, and cancellation lifetimes.
- Compare direct visibility against deterministic CPU rays before testing
  stochastic transport.
- For Radiance `rcontrib -I+`, match `N` material bounces with `-ab N+1`; the
  sensor hemisphere consumes the first ambient level.
- Classify escaped paths with the exact `reinhart.cal` altitude and azimuth
  boundaries. Nearest-patch-center classification is not `rbin` compatible.
- Include compiler messages and the selected Metal language version in backend
  errors and benchmark metadata.
