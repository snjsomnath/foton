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
    const float index_of_refraction = 1.52;
    float incident = abs(cosine);
    float transmitted = sqrt(
        (1.0 - 1.0 / (index_of_refraction * index_of_refraction))
        + incident * incident / (index_of_refraction * index_of_refraction));
    vec3 attenuation = pow(transmissivity, vec3(1.0 / transmitted));
    float perpendicular_amplitude =
        (incident - index_of_refraction * transmitted)
        / (incident + index_of_refraction * transmitted);
    float perpendicular = perpendicular_amplitude * perpendicular_amplitude;
    float parallel_amplitude =
        (transmitted - index_of_refraction * incident)
        / (transmitted + index_of_refraction * incident);
    float parallel = parallel_amplitude * parallel_amplitude;
    vec3 attenuation_squared = attenuation * attenuation;
    vec3 perpendicular_transmission =
        (1.0 - perpendicular) * (1.0 - perpendicular) * attenuation
        / (1.0 - perpendicular * perpendicular * attenuation_squared);
    vec3 parallel_transmission =
        (1.0 - parallel) * (1.0 - parallel) * attenuation
        / (1.0 - parallel * parallel * attenuation_squared);
    return max(
        0.5 * (perpendicular_transmission + parallel_transmission),
        0.0);
}

vec3 thin_glass_reflection(vec3 transmissivity, float cosine) {
    const float index_of_refraction = 1.52;
    float incident = abs(cosine);
    float transmitted = sqrt(
        (1.0 - 1.0 / (index_of_refraction * index_of_refraction))
        + incident * incident / (index_of_refraction * index_of_refraction));
    vec3 attenuation = pow(transmissivity, vec3(1.0 / transmitted));
    float perpendicular_amplitude =
        (incident - index_of_refraction * transmitted)
        / (incident + index_of_refraction * transmitted);
    float perpendicular = perpendicular_amplitude * perpendicular_amplitude;
    float parallel_amplitude =
        (transmitted - index_of_refraction * incident)
        / (transmitted + index_of_refraction * incident);
    float parallel = parallel_amplitude * parallel_amplitude;
    vec3 attenuation_squared = attenuation * attenuation;
    vec3 perpendicular_reflection =
        perpendicular
        * (1.0 + (1.0 - 2.0 * perpendicular) * attenuation_squared)
        / (1.0 - perpendicular * perpendicular * attenuation_squared);
    vec3 parallel_reflection =
        parallel
        * (1.0 + (1.0 - 2.0 * parallel) * attenuation_squared)
        / (1.0 - parallel * parallel * attenuation_squared);
    return max(
        0.5 * (perpendicular_reflection + parallel_reflection),
        0.0);
}

float color_intensity(vec3 color) {
    return dot(color, vec3(0.265, 0.670, 0.065));
}
