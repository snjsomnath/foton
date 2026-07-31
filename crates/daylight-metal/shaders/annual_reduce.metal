#include "contracts.metal"

kernel void annual_reduce(
    constant AnnualReductionUniforms& uniforms [[buffer(0)]],
    device const packed_float3* coefficients [[buffer(1)]],
    device const packed_float3* sky_patch_timestep_rgb [[buffer(2)]],
    device const float* occupancy_weights [[buffer(3)]],
    device atomic_uint* occupied_accumulators [[buffer(4)]],
    device atomic_uint* threshold_accumulators [[buffer(5)]],
    uint2 thread_position [[thread_position_in_grid]])
{
    const uint timestep = thread_position.x;
    const uint sensor = uniforms.sensor_offset + thread_position.y;
    if (sensor >= uniforms.sensor_count || timestep >= uniforms.timestep_count) {
        return;
    }

    const float occupied = occupancy_weights[timestep];
    if (occupied <= 0.0f) {
        return;
    }

    float3 response = 0.0f;
    for (uint patch = 0; patch < uniforms.patch_count; ++patch) {
        const float3 coefficient =
            float3(coefficients[sensor * uniforms.patch_count + patch]);
        const float3 sky =
            float3(sky_patch_timestep_rgb[(patch * uniforms.timestep_count) + timestep]);
        response += coefficient * sky;
    }

    const float illuminance = dot(response, float3(47.435f, 119.93f, 11.635f));
    constexpr float accumulator_scale = 100000.0f;
    const uint occupied_ticks = uint(round(occupied * accumulator_scale));
    atomic_fetch_add_explicit(
        &occupied_accumulators[sensor], occupied_ticks, memory_order_relaxed);
    if (illuminance >= uniforms.threshold_lux) {
        atomic_fetch_add_explicit(
            &threshold_accumulators[sensor], occupied_ticks, memory_order_relaxed);
    }
}
