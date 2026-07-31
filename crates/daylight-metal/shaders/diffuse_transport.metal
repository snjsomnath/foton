#include "contracts.metal"

struct TransportUniforms {
    uint sensor_count;
    uint sample_offset;
    uint sample_count;
    uint maximum_bounces;
    uint patch_count;
    uint active_category_mask;
    uint maximum_transparent_intersections;
    uint padding;
    uint scene_seed_low;
    uint scene_seed_high;
    float accumulator_scale;
    uint padding_two;
};

struct FinalizeUniforms {
    uint coefficient_count;
    float accumulator_scale;
    uint2 padding;
};

static uint mix32(uint value)
{
    value ^= value >> 16;
    value *= 0x7feb352du;
    value ^= value >> 15;
    value *= 0x846ca68bu;
    return value ^ (value >> 16);
}

static uint rotate_left(uint value, uint amount)
{
    return (value << amount) | (value >> (32u - amount));
}

static uint sobol_uint(uint index, uint dimension)
{
    const uint gray = index ^ (index >> 1);
    uint value = 0;
    uint direction = 0x80000000u;
    for (uint bit = 0; bit < 32; ++bit) {
        if ((gray & (1u << bit)) != 0) {
            value ^= direction;
        }
        if (dimension == 0) {
            direction >>= 1;
        } else {
            direction ^= direction >> 1;
        }
    }
    return value;
}

static uint owen_scramble(uint value, uint seed)
{
    value = reverse_bits(value);
    value ^= value * 0x3d20adeau;
    value += seed;
    value *= (seed >> 16) | 1u;
    value ^= value * 0x05526c56u;
    value ^= value * 0x53a22864u;
    return reverse_bits(value);
}

static float sequence_value(
    uint sensor_id,
    uint sample_index,
    uint bounce_depth,
    uint dimension,
    uint scene_seed_low,
    uint scene_seed_high)
{
    const uint scramble_seed = mix32(
        scene_seed_low
        ^ scene_seed_high
        ^ rotate_left(sensor_id, 7u)
        ^ rotate_left(bounce_depth, 13u)
        ^ dimension * 0x9e3779b9u);
    const uint sobol = sobol_uint(sample_index, dimension & 1u);
    return (float(owen_scramble(sobol, scramble_seed)) + 0.5f)
        * (1.0f / 4294967296.0f);
}

static float3 cosine_direction(
    float3 normal,
    uint sensor_id,
    uint sample_index,
    uint bounce_depth,
    uint scene_seed_low,
    uint scene_seed_high)
{
    const float first = sequence_value(
        sensor_id,
        sample_index,
        bounce_depth,
        0,
        scene_seed_low,
        scene_seed_high);
    const float second = sequence_value(
        sensor_id,
        sample_index,
        bounce_depth,
        1,
        scene_seed_low,
        scene_seed_high);
    const float radius = sqrt(first);
    const float azimuth = 2.0f * M_PI_F * second;
    const float3 local_direction = float3(
        radius * cos(azimuth),
        radius * sin(azimuth),
        sqrt(1.0f - first));
    const float3 helper = abs(normal.z) < 0.999f
        ? float3(0.0f, 0.0f, 1.0f)
        : float3(1.0f, 0.0f, 0.0f);
    const float3 tangent = normalize(cross(helper, normal));
    const float3 bitangent = cross(normal, tangent);
    return normalize(
        tangent * local_direction.x
        + bitangent * local_direction.y
        + normal * local_direction.z);
}

static uint tregenza_ring_count(uint ring)
{
    switch (ring) {
        case 0: return 30;
        case 1: return 30;
        case 2: return 24;
        case 3: return 24;
        case 4: return 18;
        case 5: return 12;
        default: return 6;
    }
}

static uint radiance_patch(float3 direction, uint patch_count)
{
    if (direction.z < 0.0f) {
        return 0;
    }
    const uint multiplier = patch_count == 146u ? 1u : 2u;
    const uint regular_row_count = 7u * multiplier;
    const float altitude_increment = (0.5f * M_PI_F) /
        (float(regular_row_count) + 0.5f);
    const uint row = uint(floor(
        asin(clamp(direction.z, -1.0f, 1.0f)) / altitude_increment));
    if (row >= regular_row_count) {
        return patch_count - 1u;
    }

    const uint parent_ring = uint(floor(
        (float(row) + 0.5f) / float(multiplier)));
    const uint row_patch_count =
        tregenza_ring_count(parent_ring) * multiplier;
    uint offset = 1u;
    for (uint prior_row = 0; prior_row < row; ++prior_row) {
        const uint prior_parent = uint(floor(
            (float(prior_row) + 0.5f) / float(multiplier)));
        offset += tregenza_ring_count(prior_parent) * multiplier;
    }

    float azimuth = atan2(direction.x, direction.y);
    if (azimuth < 0.0f) {
        azimuth += 2.0f * M_PI_F;
    }
    const float azimuth_increment =
        2.0f * M_PI_F / float(row_patch_count);
    uint azimuth_index = uint(floor(
        (azimuth + 0.5f * azimuth_increment) / azimuth_increment));
    if (azimuth_index >= row_patch_count) {
        azimuth_index = 0u;
    }
    return offset + azimuth_index;
}

static void accumulate_indirect(
    device atomic_uint* coefficients,
    uint destination,
    float3 value,
    float scale)
{
    const uint3 ticks = uint3(round(max(value, 0.0f) * scale));
    atomic_fetch_add_explicit(
        &coefficients[destination],
        ticks.x,
        memory_order_relaxed);
    atomic_fetch_add_explicit(
        &coefficients[destination + 1],
        ticks.y,
        memory_order_relaxed);
    atomic_fetch_add_explicit(
        &coefficients[destination + 2],
        ticks.z,
        memory_order_relaxed);
}

kernel void diffuse_transport(
    constant TransportUniforms& uniforms [[buffer(0)]],
    device const Sensor* sensors [[buffer(1)]],
    device const packed_float3* patch_directions [[buffer(2)]],
    device const InstanceMetadata* instance_metadata [[buffer(3)]],
    device const uint* triangle_materials [[buffer(4)]],
    device const Material* materials [[buffer(5)]],
    device const packed_float3* triangle_normals [[buffer(6)]],
    constant NormalTransform* normal_transforms [[buffer(7)]],
    device atomic_uint* indirect_coefficients [[buffer(8)]],
    instance_acceleration_structure acceleration_structure [[buffer(9)]],
    uint2 thread_position [[thread_position_in_grid]])
{
    const uint local_sample = thread_position.x;
    const uint sensor_index = thread_position.y;
    if (local_sample >= uniforms.sample_count || sensor_index >= uniforms.sensor_count) {
        return;
    }

    const Sensor sensor = sensors[sensor_index];
    const uint sample_index = uniforms.sample_offset + local_sample;
    float3 origin = float3(sensor.position) + float3(sensor.normal) * 1.0e-4f;
    float3 direction = cosine_direction(
        normalize(float3(sensor.normal)),
        sensor.sensor_id,
        sample_index,
        0,
        uniforms.scene_seed_low,
        uniforms.scene_seed_high);
    float3 throughput = 1.0f;
    uint diffuse_bounces = 0;
    uint transparent_intersections = 0;

    intersector<triangle_data, instancing> path_intersector;
    path_intersector.set_triangle_cull_mode(triangle_cull_mode::none);
    path_intersector.force_opacity(forced_opacity::opaque);
    path_intersector.assume_geometry_type(geometry_type::triangle);

    const uint maximum_path_intersections =
        uniforms.maximum_bounces + uniforms.maximum_transparent_intersections + 1u;
    for (uint path_intersection = 0; path_intersection < maximum_path_intersections; ++path_intersection) {
        ray path_ray;
        path_ray.origin = origin;
        path_ray.direction = direction;
        path_ray.min_distance = 1.0e-4f;
        path_ray.max_distance = INFINITY;
        const auto intersection = path_intersector.intersect(
            path_ray,
            acceleration_structure,
            uniforms.active_category_mask);

        if (intersection.type == intersection_type::none) {
            if (diffuse_bounces > 0) {
                const uint patch = radiance_patch(direction, uniforms.patch_count);
                const uint destination =
                    (sensor_index * uniforms.patch_count + patch) * 3;
                accumulate_indirect(
                    indirect_coefficients,
                    destination,
                    throughput * (M_PI_F / float(uniforms.sample_count)),
                    uniforms.accumulator_scale);
            }
            break;
        }

        const uint instance_index = intersection.instance_id;
        const InstanceMetadata metadata = instance_metadata[instance_index];
        const uint triangle_index = metadata.material_offset + intersection.primitive_id;
        const Material material = materials[triangle_materials[triangle_index]];
        const float3 normal = hit_normal(
            instance_index,
            triangle_index,
            direction,
            triangle_normals,
            normal_transforms);

        if (material.kind == 1u) {
            if (transparent_intersections >= uniforms.maximum_transparent_intersections) {
                break;
            }
            throughput *= thin_glass_transmission(
                material.internal_transmissivity_rgb,
                abs(dot(direction, normal)));
            if (all(throughput <= 1.0e-6f)) {
                break;
            }
            origin += direction * (intersection.distance + 1.0e-4f);
            ++transparent_intersections;
            continue;
        }

        if (diffuse_bounces >= uniforms.maximum_bounces) {
            break;
        }
        throughput *= float3(material.diffuse_rgb);
        if (all(throughput <= 1.0e-6f)) {
            break;
        }
        origin += direction * intersection.distance + normal * 1.0e-4f;
        ++diffuse_bounces;
        direction = cosine_direction(
            normal,
            sensor.sensor_id,
            sample_index,
            diffuse_bounces,
            uniforms.scene_seed_low,
            uniforms.scene_seed_high);
    }
}

kernel void finalize_indirect(
    constant FinalizeUniforms& uniforms [[buffer(0)]],
    device const uint* indirect_coefficients [[buffer(1)]],
    device packed_float3* coefficients [[buffer(2)]],
    uint coefficient_index [[thread_position_in_grid]])
{
    if (coefficient_index >= uniforms.coefficient_count) {
        return;
    }
    const uint source = coefficient_index * 3;
    const float3 indirect = float3(
        indirect_coefficients[source],
        indirect_coefficients[source + 1],
        indirect_coefficients[source + 2])
        / uniforms.accumulator_scale;
    coefficients[coefficient_index] =
        packed_float3(float3(coefficients[coefficient_index]) + indirect);
}
