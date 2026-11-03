#include "contracts.metal"

kernel void direct_visibility(
    constant DirectVisibilityUniforms& uniforms [[buffer(0)]],
    device const Sensor* sensors [[buffer(1)]],
    device const packed_float3* patch_directions [[buffer(2)]],
    device const float* patch_solid_angles [[buffer(3)]],
    device const InstanceMetadata* instance_metadata [[buffer(4)]],
    device const uint* triangle_materials [[buffer(5)]],
    device const Material* materials [[buffer(6)]],
    device const packed_float3* triangle_normals [[buffer(7)]],
    constant NormalTransform* normal_transforms [[buffer(8)]],
    device packed_float3* coefficients [[buffer(9)]],
    instance_acceleration_structure acceleration_structure [[buffer(10)]],
    uint2 thread_position [[thread_position_in_grid]])
{
    const uint patch_index = thread_position.x;
    const uint sensor_index = thread_position.y;
    if (patch_index >= uniforms.patch_count || sensor_index >= uniforms.sensor_count) {
        return;
    }

    const Sensor sensor = sensors[sensor_index];
    intersector<triangle_data, instancing> visibility_intersector;
    visibility_intersector.set_triangle_cull_mode(triangle_cull_mode::none);
    visibility_intersector.force_opacity(forced_opacity::opaque);
    visibility_intersector.assume_geometry_type(geometry_type::triangle);
    // Transparent transport must commit the closest hit. Accepting any hit can
    // select farther glass before nearer opaque geometry and leak through it.
    visibility_intersector.accept_any_intersection(false);

    float3 integrated = 0.0f;
    for (uint sample_index = 0; sample_index < uniforms.direct_sample_count; ++sample_index) {
        const float3 direction = normalize(
            patch_directions[
                patch_index * uniforms.direct_sample_count + sample_index]);
        const float cosine = max(dot(float3(sensor.normal), direction), 0.0f);
        if (cosine == 0.0f) {
            continue;
        }

        ray visibility_ray;
        visibility_ray.origin =
            float3(sensor.position) + float3(sensor.normal) * 1.0e-4f;
        visibility_ray.direction = direction;
        visibility_ray.min_distance = 1.0e-4f;
        visibility_ray.max_distance = INFINITY;

        float3 transmission = 1.0f;
        for (
            uint transparent_intersection = 0;
            transparent_intersection <= uniforms.maximum_transparent_intersections;
            ++transparent_intersection)
        {
            const auto intersection = visibility_intersector.intersect(
                visibility_ray,
                acceleration_structure,
                uniforms.active_category_mask);
            if (intersection.type == intersection_type::none) {
                break;
            }

            const uint instance_index = intersection.instance_id;
            const InstanceMetadata metadata = instance_metadata[instance_index];
            const uint triangle_index =
                metadata.material_offset + intersection.primitive_id;
            const Material material = materials[triangle_materials[triangle_index]];
            if (material.kind != 1u
                || transparent_intersection
                    == uniforms.maximum_transparent_intersections)
            {
                transmission = 0.0f;
                break;
            }

            const float3 normal = hit_normal(
                instance_index,
                triangle_index,
                direction,
                triangle_normals,
                normal_transforms);
            transmission *= thin_glass_transmission(
                material.internal_transmissivity_rgb,
                abs(dot(direction, normal)));
            if (all(transmission <= 1.0e-6f)) {
                transmission = 0.0f;
                break;
            }
            visibility_ray.origin +=
                direction * (intersection.distance + 1.0e-4f);
        }
        integrated += transmission * cosine;
    }

    coefficients[sensor_index * uniforms.patch_count + patch_index] =
        integrated * (
            patch_solid_angles[patch_index]
            / float(uniforms.direct_sample_count));
}
