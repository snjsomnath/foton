# MSL Ray-Tracing Compatibility

## Runtime Compilation Baseline

When `newLibraryWithSource` is called without an explicit Metal language version,
the compiler may expose less than the newest SDK headers document. Compiler
diagnostics are the authority for that active source profile.

| Concern | Baseline approach | Version-gated alternative |
| --- | --- | --- |
| Ray traversal | `intersector<triangle_data, instancing>` | `intersection_query` |
| Hit result | Returned `intersection_result` | Candidate/committed query methods |
| Instance metadata index | `intersection.instance_id` | User-defined instance ID result |
| Weighted atomics | `atomic_uint` fixed point or reduction | `atomic_float` |
| Filtering | Descriptor mask and ray mask | Intersection functions |

Do not adopt a version-gated alternative until the host explicitly selects a
compatible `MTLLanguageVersion`, the device supports the feature, and a minimal
runtime compilation test succeeds.

## Instance Identity

`instance_id` is the zero-based index of the instance descriptor in the TLAS.
It can index an engine metadata buffer only if both arrays are generated from
the same deterministic instance ordering and updated together.

`MTLAccelerationStructureUserIDInstanceDescriptor.userID` is a distinct custom
value. Populate it when useful, but some runtime source profiles do not expose a
corresponding `user_instance_id` field on `intersection_result`. Do not substitute
the descriptor mask: masks are bitwise category filters.

For stable application identity, store room ID, mesh ID, material offset, and
dirty revision in the metadata record indexed by the descriptor-order
`instance_id`.

## Baseline Visibility Kernel

```metal
intersector<triangle_data, instancing> ray_intersector;
ray_intersector.set_triangle_cull_mode(triangle_cull_mode::none);
ray_intersector.force_opacity(forced_opacity::opaque);
ray_intersector.assume_geometry_type(geometry_type::triangle);
ray_intersector.accept_any_intersection(true);

const auto hit = ray_intersector.intersect(
    visibility_ray,
    acceleration_structure,
    category_mask);

if (hit.type != intersection_type::none) {
    const uint metadata_index = hit.instance_id;
}
```

## Compiler Failures

- `unknown type name 'atomic_float'`: use integer fixed-point accumulation or
  explicitly select and test a supporting language version.
- `unknown type name 'intersection_params'`: use the baseline `intersector` API.
- `no template named 'intersection_query'`: use the baseline `intersector` API.
- Missing committed/candidate methods: the query API is unavailable in the
  selected source profile.
- Missing `user_instance_id`: use descriptor-order `instance_id`, or explicitly
  enable and test a language level that exposes custom user IDs.
- A suggested underscored type such as `_intersection_params` is private and
  must not be used.

## Validation Order

1. Compile the MSL source with production compile options.
2. Create the compute pipeline.
3. Trace analytical hit and miss rays.
4. Verify transformed-instance and metadata indexing.
5. Verify masks independently from identity.
6. Compare a direct-visibility fixture against CPU and Radiance references.
7. Record hardware transport provenance and reject silent CPU fallback.

## Radiance Daylight Transport

Use any-hit traversal only for visibility rays. A path that needs a hit point,
surface normal, material, or transparent-interface distance must use the closest
intersection.

Radiance `rcontrib -I+` counts the sensor irradiance hemisphere as its first
ambient level. To compare against a GPU path tracer allowing `N` diffuse material
bounces, run Radiance with `-ab N+1`.

When escaped paths are accumulated into Tregenza or Reinhart bins, implement the
`reinhart.cal` `rbin` boundaries exactly:

- Ground is bin zero.
- Altitude row is `floor(altitude / alpha)`.
- Azimuth sectors are centered on north and advance toward east.
- The final cap is the zenith bin.

Nearest-center assignment changes boundary ownership and inflates per-patch
CV(RMSE), even when total transport energy is correct.
