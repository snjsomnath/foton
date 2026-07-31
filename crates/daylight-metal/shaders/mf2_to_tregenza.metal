#include <metal_stdlib>

using namespace metal;

struct BasisReductionUniforms {
    uint sensor_count;
    uint source_patch_count;
    uint destination_patch_count;
    uint padding;
};

kernel void mf2_to_tregenza(
    constant BasisReductionUniforms& uniforms [[buffer(0)]],
    device const packed_float3* mf2_coefficients [[buffer(1)]],
    device const uint* parent_patch [[buffer(2)]],
    device atomic_float* tregenza_coefficients [[buffer(3)]],
    uint2 thread_position [[thread_position_in_grid]])
{
    const uint source_patch = thread_position.x;
    const uint sensor_index = thread_position.y;
    if (source_patch >= uniforms.source_patch_count || sensor_index >= uniforms.sensor_count) {
        return;
    }
    const uint destination_patch = parent_patch[source_patch];
    const float3 value =
        mf2_coefficients[sensor_index * uniforms.source_patch_count + source_patch];
    const uint destination =
        (sensor_index * uniforms.destination_patch_count + destination_patch) * 3;
    atomic_fetch_add_explicit(&tregenza_coefficients[destination], value.x, memory_order_relaxed);
    atomic_fetch_add_explicit(&tregenza_coefficients[destination + 1], value.y, memory_order_relaxed);
    atomic_fetch_add_explicit(&tregenza_coefficients[destination + 2], value.z, memory_order_relaxed);
}
