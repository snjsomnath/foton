#extension GL_EXT_scalar_block_layout : require

struct Sensor {
    vec3 position;
    vec3 normal;
    uint sensor_id;
    uint room_id;
    float area_weight;
    uvec3 padding;
};

struct InstanceMetadata {
    uint room_id;
    uint mesh_id;
    uint material_offset;
    uint dirty_revision;
};

struct NormalTransform {
    vec4 row0;
    vec4 row1;
    vec4 row2;
};

struct Material {
    uint kind;
    vec3 diffuse_rgb;
    vec3 visible_transmittance_rgb;
    vec3 internal_transmissivity_rgb;
    uint padding;
};

vec3 transform_normal(vec3 value, NormalTransform transform) {
    return normalize(vec3(
        dot(transform.row0.xyz, value),
        dot(transform.row1.xyz, value),
        dot(transform.row2.xyz, value)));
}

float fresnel_reflectance(float cosine) {
    const float index_of_refraction = 1.52;
    float incident = max(1.0 - cosine * cosine, 0.0);
    float transmitted = incident / (index_of_refraction * index_of_refraction);
    if (transmitted >= 1.0) return 1.0;
    float cos_transmitted = sqrt(1.0 - transmitted);
    float perpendicular = (cosine - index_of_refraction * cos_transmitted)
        / (cosine + index_of_refraction * cos_transmitted);
    float parallel = (index_of_refraction * cosine - cos_transmitted)
        / (index_of_refraction * cosine + cos_transmitted);
    return 0.5 * (perpendicular * perpendicular + parallel * parallel);
}

vec3 thin_glass_transmission(vec3 transmissivity, float cosine) {
    float reflectance = fresnel_reflectance(abs(cosine));
    float interface_transmission = 1.0 - reflectance;
    vec3 numerator = interface_transmission * interface_transmission * transmissivity;
    vec3 denominator = 1.0 - reflectance * reflectance * transmissivity * transmissivity;
    return max(numerator / denominator, 0.0);
}
