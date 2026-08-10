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

constant uint sobol_directions[512] = {
    0x80000000u, 0x40000000u, 0x20000000u, 0x10000000u, 0x08000000u, 0x04000000u, 0x02000000u, 0x01000000u,
    0x00800000u, 0x00400000u, 0x00200000u, 0x00100000u, 0x00080000u, 0x00040000u, 0x00020000u, 0x00010000u,
    0x00008000u, 0x00004000u, 0x00002000u, 0x00001000u, 0x00000800u, 0x00000400u, 0x00000200u, 0x00000100u,
    0x00000080u, 0x00000040u, 0x00000020u, 0x00000010u, 0x00000008u, 0x00000004u, 0x00000002u, 0x00000001u,
    0x80000000u, 0xc0000000u, 0xa0000000u, 0xf0000000u, 0x88000000u, 0xcc000000u, 0xaa000000u, 0xff000000u,
    0x80800000u, 0xc0c00000u, 0xa0a00000u, 0xf0f00000u, 0x88880000u, 0xcccc0000u, 0xaaaa0000u, 0xffff0000u,
    0x80008000u, 0xc000c000u, 0xa000a000u, 0xf000f000u, 0x88008800u, 0xcc00cc00u, 0xaa00aa00u, 0xff00ff00u,
    0x80808080u, 0xc0c0c0c0u, 0xa0a0a0a0u, 0xf0f0f0f0u, 0x88888888u, 0xccccccccu, 0xaaaaaaaau, 0xffffffffu,
    0x80000000u, 0xc0000000u, 0x60000000u, 0x90000000u, 0xe8000000u, 0x5c000000u, 0x8e000000u, 0xc5000000u,
    0x68800000u, 0x9cc00000u, 0xee600000u, 0x55900000u, 0x80680000u, 0xc09c0000u, 0x60ee0000u, 0x90550000u,
    0xe8808000u, 0x5cc0c000u, 0x8e606000u, 0xc5909000u, 0x6868e800u, 0x9c9c5c00u, 0xeeee8e00u, 0x5555c500u,
    0x8000e880u, 0xc0005cc0u, 0x60008e60u, 0x9000c590u, 0xe8006868u, 0x5c009c9cu, 0x8e00eeeeu, 0xc5005555u,
    0x80000000u, 0xc0000000u, 0x20000000u, 0x50000000u, 0xf8000000u, 0x74000000u, 0xa2000000u, 0x93000000u,
    0xd8800000u, 0x25400000u, 0x59e00000u, 0xe6d00000u, 0x78080000u, 0xb40c0000u, 0x82020000u, 0xc3050000u,
    0x208f8000u, 0x51474000u, 0xfbea2000u, 0x75d93000u, 0xa0858800u, 0x914e5400u, 0xdbe79e00u, 0x25db6d00u,
    0x58800080u, 0xe54000c0u, 0x79e00020u, 0xb6d00050u, 0x800800f8u, 0xc00c0074u, 0x200200a2u, 0x50050093u,
    0x80000000u, 0x40000000u, 0x20000000u, 0xb0000000u, 0xf8000000u, 0xdc000000u, 0x7a000000u, 0x9d000000u,
    0x5a800000u, 0x2fc00000u, 0xa1600000u, 0xf0b00000u, 0xda880000u, 0x6fc40000u, 0x81620000u, 0x40bb0000u,
    0x22878000u, 0xb3c9c000u, 0xfb65a000u, 0xddb2d000u, 0x78022800u, 0x9c0b3c00u, 0x5a0fb600u, 0x2d0ddb00u,
    0xa2878080u, 0xf3c9c040u, 0xdb65a020u, 0x6db2d0b0u, 0x800228f8u, 0x400b3cdcu, 0x200fb67au, 0xb00ddb9du,
    0x80000000u, 0xc0000000u, 0xa0000000u, 0xd0000000u, 0x48000000u, 0x6c000000u, 0x7a000000u, 0x95000000u,
    0x20800000u, 0x10c00000u, 0xe8a00000u, 0xbcd00000u, 0x32480000u, 0xf96c0000u, 0x5afa0000u, 0x85550000u,
    0xc8008000u, 0xac00c000u, 0xda00a000u, 0x4500d000u, 0x68804800u, 0x7cc06c00u, 0x92a07a00u, 0x29d09500u,
    0x12c82080u, 0xe9ac10c0u, 0xb25ae8a0u, 0x3985bcd0u, 0xfa48b248u, 0x556c396cu, 0x80fafafau, 0xc0555555u,
    0x80000000u, 0x40000000u, 0xa0000000u, 0x50000000u, 0xd8000000u, 0x9c000000u, 0x36000000u, 0x63000000u,
    0xb6800000u, 0x23400000u, 0x16200000u, 0x73100000u, 0xcef80000u, 0xef8c0000u, 0xf8ce0000u, 0x8cef0000u,
    0x4ef88000u, 0xaf8c4000u, 0x58cea000u, 0xdcef5000u, 0x96f85800u, 0x338cdc00u, 0x6ece9600u, 0xbfef3300u,
    0x2078ee80u, 0x10ccff40u, 0x78ee8020u, 0xccff4010u, 0xee802078u, 0xff4010ccu, 0x802078eeu, 0x4010ccffu,
    0x80000000u, 0xc0000000u, 0x60000000u, 0x90000000u, 0x38000000u, 0xe4000000u, 0x56000000u, 0x5b000000u,
    0x70800000u, 0x6fc00000u, 0xb8200000u, 0x24300000u, 0x36180000u, 0xcb240000u, 0x488e0000u, 0x8bf90000u,
    0xee358000u, 0x7f26c000u, 0x46842000u, 0xa4fff000u, 0xf0800800u, 0xafc00c00u, 0xd8200600u, 0xb4300900u,
    0x0e180380u, 0x2f240e40u, 0x1e8e0560u, 0xd0f905b0u, 0x9eb58708u, 0x10e6c6fcu, 0xfea42b82u, 0x80cff243u,
    0x80000000u, 0x40000000u, 0x60000000u, 0xb0000000u, 0x68000000u, 0x34000000u, 0x2a000000u, 0x57000000u,
    0x9f800000u, 0x3c400000u, 0xaa200000u, 0x17100000u, 0xff980000u, 0x8c6c0000u, 0xc23a0000u, 0x231d0000u,
    0xd5928000u, 0xdb79c000u, 0x5d9de000u, 0x1f521000u, 0x7f980800u, 0xcc6c0400u, 0xa23a0600u, 0x931d0b00u,
    0xbd928680u, 0xef79c340u, 0x779de2a0u, 0x48521570u, 0xe01801f8u, 0xf02c07c4u, 0x081a0ca2u, 0x840d0a71u,
    0x80000000u, 0x40000000u, 0xa0000000u, 0x10000000u, 0x78000000u, 0x74000000u, 0x8a000000u, 0xb9000000u,
    0x96800000u, 0x3cc00000u, 0xd2200000u, 0x9d100000u, 0xc4a80000u, 0xe1c40000u, 0xb6be0000u, 0x6ccd0000u,
    0x0a2a8000u, 0xf93a4000u, 0x3693a000u, 0x2cd63000u, 0xaa280800u, 0xe9040400u, 0x4e9e0a00u, 0x58dd0100u,
    0x20028780u, 0x503e4740u, 0xd80da8a0u, 0x640b3b90u, 0xf22a8168u, 0xcd3a47ccu, 0x1c93a722u, 0x85d638d1u,
    0x80000000u, 0x40000000u, 0xe0000000u, 0x30000000u, 0x58000000u, 0x7c000000u, 0xee000000u, 0x61000000u,
    0x74800000u, 0xbc400000u, 0x4ca00000u, 0xb0500000u, 0x1a980000u, 0x9d5c0000u, 0xd80e0000u, 0x3c030000u,
    0x0e158000u, 0x510b4000u, 0x2cb0a000u, 0xc0685000u, 0xa2958800u, 0xd14b4400u, 0x6e10ae00u, 0x21385300u,
    0x948d8d80u, 0x8c5743c0u, 0x14bea0e0u, 0xcc6b5510u, 0xf4800ac8u, 0xfc400804u, 0xaca0042au, 0x80500e15u,
    0x80000000u, 0xc0000000u, 0xa0000000u, 0x50000000u, 0x08000000u, 0x1c000000u, 0x72000000u, 0x9b000000u,
    0xb3800000u, 0x3cc00000u, 0xe1a00000u, 0x37f00000u, 0xfa080000u, 0x47240000u, 0x61aa0000u, 0xf7d30000u,
    0x5a3e8000u, 0x1711c000u, 0x69986000u, 0xebfdf000u, 0x28368800u, 0x8c35cc00u, 0xda326a00u, 0xd72ef500u,
    0xc9880880u, 0xbbe40dc0u, 0x200a0d20u, 0x90230cb0u, 0xa8368bb8u, 0x4c35c20cu, 0x7a32693au, 0x872efacfu,
    0x80000000u, 0xc0000000u, 0xe0000000u, 0x70000000u, 0x48000000u, 0x5c000000u, 0xa2000000u, 0x51000000u,
    0xdc800000u, 0x65c00000u, 0xb6a00000u, 0xa8f00000u, 0x28180000u, 0xec2c0000u, 0x0a2a0000u, 0x7d0b0000u,
    0x36ba8000u, 0x68c34000u, 0xc83fa000u, 0x9c3d3000u, 0x42228800u, 0x212f4c00u, 0x94b5ae00u, 0x39c63700u,
    0x14800c80u, 0xf9c009c0u, 0xf4a00420u, 0x89f00210u, 0xbc980948u, 0xd5ec039cu, 0x1e8a014au, 0x84fb0f9fu,
    0x80000000u, 0xc0000000u, 0x60000000u, 0x90000000u, 0x48000000u, 0x6c000000u, 0x42000000u, 0xa3000000u,
    0xf1800000u, 0xda400000u, 0x25200000u, 0x2fb00000u, 0xe0080000u, 0x500c0000u, 0x28060000u, 0xfc090000u,
    0x0a048000u, 0xcf06c000u, 0xb3842000u, 0x794a3000u, 0xd4af1800u, 0xf5fda400u, 0xc52a5200u, 0x7fbefb00u,
    0xc8000080u, 0xac0000c0u, 0x22000060u, 0x33000090u, 0xb9800048u, 0xb640006cu, 0x67200042u, 0x8cb000a3u,
    0x80000000u, 0x40000000u, 0x60000000u, 0x30000000u, 0x68000000u, 0x1c000000u, 0x9a000000u, 0x55000000u,
    0xd7800000u, 0x97c00000u, 0xf7200000u, 0xc6300000u, 0xad880000u, 0xb2c40000u, 0x28a60000u, 0x7df30000u,
    0xa8ae8000u, 0x3df5c000u, 0xc8a7a000u, 0x0df25000u, 0xa0a5f800u, 0x11ffbc00u, 0x3aae5200u, 0x44fff300u,
    0xed268080u, 0xd331c040u, 0x1a01a060u, 0x15015030u, 0xb78b7868u, 0xa7ca7c1cu, 0x9f29f29au, 0xda3da355u,
    0x80000000u, 0xc0000000u, 0xa0000000u, 0xb0000000u, 0x38000000u, 0x2c000000u, 0xae000000u, 0x6d000000u,
    0xcf800000u, 0x7d400000u, 0x45a00000u, 0x69100000u, 0xc5a80000u, 0xa91c0000u, 0x65a20000u, 0x19170000u,
    0x5da18000u, 0x3515c000u, 0xf3ab6000u, 0x58131000u, 0x3c279800u, 0x2554c400u, 0x7983c200u, 0x4c425500u,
    0xbc279880u, 0xe554c4c0u, 0xd983c2a0u, 0xfc4255b0u, 0x842798b8u, 0xc954c4ecu, 0x7783c20eu, 0x914255ddu
};

static uint sobol_uint(uint index, uint dimension)
{
    const uint gray = index ^ (index >> 1);
    uint value = 0;
    const uint offset = (dimension % 16u) * 32u;
    for (uint bit = 0; bit < 32; ++bit) {
        if ((gray & (1u << bit)) != 0) {
            value ^= sobol_directions[offset + bit];
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
    const uint sobol = sobol_uint(sample_index, dimension);
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
        bounce_depth * 2u,
        scene_seed_low,
        scene_seed_high);
    const float second = sequence_value(
        sensor_id,
        sample_index,
        bounce_depth,
        bounce_depth * 2u + 1u,
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
        path_ray.min_distance = 1.0e-6f;
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
            const float incidence = abs(dot(direction, normal));
            const float3 transmission = thin_glass_transmission(
                material.internal_transmissivity_rgb,
                incidence);
            const float3 reflection = thin_glass_reflection(
                material.internal_transmissivity_rgb,
                incidence);
            const float transmission_energy = color_intensity(transmission);
            const float reflection_energy = color_intensity(reflection);
            const float total_energy = transmission_energy + reflection_energy;
            if (total_energy <= 1.0e-8f) {
                break;
            }
            const float reflection_probability =
                reflection_energy / total_energy;
            const float branch_sample = sequence_value(
                sensor.sensor_id,
                sample_index,
                diffuse_bounces,
                12u + transparent_intersections,
                uniforms.scene_seed_low,
                uniforms.scene_seed_high);
            if (branch_sample < reflection_probability) {
                throughput *= reflection / reflection_probability;
                origin += direction * intersection.distance + normal * 1.0e-4f;
                direction = reflect(direction, normal);
            } else {
                const float transmission_probability =
                    1.0f - reflection_probability;
                if (transmission_probability <= 1.0e-8f) {
                    break;
                }
                throughput *= transmission / transmission_probability;
                origin += direction * (intersection.distance + 1.0e-4f);
            }
            if (all(throughput <= 1.0e-6f)) {
                break;
            }
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
