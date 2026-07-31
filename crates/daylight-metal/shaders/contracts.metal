#include <metal_stdlib>
#include <metal_raytracing>

using namespace metal;
using namespace raytracing;

struct Sensor {
    packed_float3 position;
    packed_float3 normal;
    uint sensor_id;
    uint room_id;
    float area_weight;
    packed_uint3 padding;
};

struct InstanceMetadata {
    uint room_id;
    uint mesh_id;
    uint material_offset;
    uint dirty_revision;
};

struct NormalTransform {
    float4 row0;
    float4 row1;
    float4 row2;
};

struct Material {
    uint kind;
    packed_float3 diffuse_rgb;
    packed_float3 visible_transmittance_rgb;
    packed_float3 internal_transmissivity_rgb;
    uint padding;
};

struct DirectVisibilityUniforms {
    uint sensor_count;
    uint patch_count;
    uint active_category_mask;
    uint maximum_transparent_intersections;
};

struct AnnualReductionUniforms {
    uint sensor_count;
    uint patch_count;
    uint timestep_count;
    uint sensor_offset;
    float threshold_lux;
};

static float3 transform_normal(
    float3 object_normal,
    constant NormalTransform& transform)
{
    return normalize(float3(
        dot(transform.row0.xyz, object_normal),
        dot(transform.row1.xyz, object_normal),
        dot(transform.row2.xyz, object_normal)));
}

static float fresnel_reflectance(float cosine)
{
    constexpr float index_of_refraction = 1.52f;
    const float sin_incident_squared = max(1.0f - cosine * cosine, 0.0f);
    const float sin_transmitted_squared =
        sin_incident_squared / (index_of_refraction * index_of_refraction);
    if (sin_transmitted_squared >= 1.0f) {
        return 1.0f;
    }
    const float cos_transmitted = sqrt(1.0f - sin_transmitted_squared);
    const float perpendicular =
        (cosine - index_of_refraction * cos_transmitted)
        / (cosine + index_of_refraction * cos_transmitted);
    const float parallel =
        (index_of_refraction * cosine - cos_transmitted)
        / (index_of_refraction * cosine + cos_transmitted);
    return 0.5f * (
        perpendicular * perpendicular
        + parallel * parallel);
}

static float thin_glass_transmission(float transmissivity, float cosine)
{
    if (transmissivity <= 0.0f) {
        return 0.0f;
    }
    const float reflectance = fresnel_reflectance(abs(cosine));
    const float interface_transmission = 1.0f - reflectance;
    const float numerator =
        interface_transmission * interface_transmission * transmissivity;
    const float denominator =
        1.0f - reflectance * reflectance * transmissivity * transmissivity;
    return max(numerator / denominator, 0.0f);
}

static float3 thin_glass_transmission(
    packed_float3 transmissivity,
    float cosine)
{
    return float3(
        thin_glass_transmission(transmissivity.x, cosine),
        thin_glass_transmission(transmissivity.y, cosine),
        thin_glass_transmission(transmissivity.z, cosine));
}

static float3 hit_normal(
    uint instance_index,
    uint triangle_index,
    float3 ray_direction,
    device const packed_float3* triangle_normals,
    constant NormalTransform* normal_transforms)
{
    float3 normal = transform_normal(
        float3(triangle_normals[triangle_index]),
        normal_transforms[instance_index]);
    if (dot(normal, ray_direction) > 0.0f) {
        normal = -normal;
    }
    return normal;
}
