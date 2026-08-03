use std::{
    collections::HashMap,
    ffi::c_void,
    ptr::NonNull,
    sync::{
        Arc, Mutex,
        atomic::{AtomicBool, Ordering},
    },
    time::Instant,
};

use bytemuck::{Pod, Zeroable};
use daylight_core::{
    AnalysisMetadata, AnalysisRequest, AnalysisResult, AnnualIlluminance, Backend,
    BackendCapabilities, CoefficientMatrix, DaylightError, GpuTimings, InstanceUpdate, Result,
    SOLVER_VERSION, SceneData, SceneHandle, Vec3, annual_metrics_from_accumulators,
    patch_sample_directions, patch_solid_angles, scene_fingerprint,
};
use objc2::{
    rc::{Retained, autoreleasepool},
    runtime::ProtocolObject,
};
use objc2_foundation::{NSArray, NSString};
use objc2_metal::{
    MTLAccelerationStructure, MTLAccelerationStructureCommandEncoder,
    MTLAccelerationStructureDescriptor, MTLAccelerationStructureGeometryDescriptor,
    MTLAccelerationStructureInstanceDescriptorType, MTLAccelerationStructureInstanceOptions,
    MTLAccelerationStructureTriangleGeometryDescriptor,
    MTLAccelerationStructureUserIDInstanceDescriptor, MTLBuffer, MTLCommandBuffer,
    MTLCommandEncoder, MTLCommandQueue, MTLComputeCommandEncoder, MTLComputePipelineState,
    MTLCreateSystemDefaultDevice, MTLDevice, MTLIndexType,
    MTLInstanceAccelerationStructureDescriptor, MTLLibrary, MTLPackedFloat3, MTLPackedFloat4x3,
    MTLPrimitiveAccelerationStructureDescriptor, MTLResourceOptions, MTLSize,
};

use crate::reference::compute_daylight_factor;

const ANNUAL_ACCUMULATOR_SCALE: f32 = 100_000.0;
const TRANSPORT_ACCUMULATOR_SCALE: f32 = 100_000_000.0;
const MAXIMUM_TRANSPARENT_INTERSECTIONS: u32 = 64;

#[link(name = "CoreGraphics", kind = "framework")]
unsafe extern "C" {}

pub struct MetalBackend {
    device: Retained<ProtocolObject<dyn MTLDevice>>,
    command_queue: Retained<ProtocolObject<dyn MTLCommandQueue>>,
    annual_pipeline: Retained<ProtocolObject<dyn MTLComputePipelineState>>,
    annual_illuminance_pipeline: Retained<ProtocolObject<dyn MTLComputePipelineState>>,
    direct_pipeline: Retained<ProtocolObject<dyn MTLComputePipelineState>>,
    diffuse_pipeline: Retained<ProtocolObject<dyn MTLComputePipelineState>>,
    finalize_pipeline: Retained<ProtocolObject<dyn MTLComputePipelineState>>,
    resident_scenes: Mutex<HashMap<u64, ResidentScene>>,
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct AnnualUniforms {
    sensor_count: u32,
    patch_count: u32,
    timestep_count: u32,
    sensor_offset: u32,
    threshold_lux: f32,
    udi_lower_lux: f32,
    udi_upper_lux: f32,
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct DirectUniforms {
    sensor_count: u32,
    patch_count: u32,
    direct_sample_count: u32,
    active_category_mask: u32,
    maximum_transparent_intersections: u32,
    padding: [u32; 3],
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct TransportUniforms {
    sensor_count: u32,
    sample_offset: u32,
    sample_count: u32,
    maximum_bounces: u32,
    patch_count: u32,
    active_category_mask: u32,
    maximum_transparent_intersections: u32,
    padding: u32,
    scene_seed_low: u32,
    scene_seed_high: u32,
    accumulator_scale: f32,
    padding_two: u32,
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct FinalizeUniforms {
    coefficient_count: u32,
    accumulator_scale: f32,
    padding: [u32; 2],
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct InstanceMetadata {
    room_id: u32,
    mesh_id: u32,
    material_offset: u32,
    dirty_revision: u32,
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct NormalTransform {
    row_zero: [f32; 4],
    row_one: [f32; 4],
    row_two: [f32; 4],
}

struct AccelerationResources {
    top_level: Retained<ProtocolObject<dyn MTLAccelerationStructure>>,
    _bottom_levels: Vec<Retained<ProtocolObject<dyn MTLAccelerationStructure>>>,
}

struct GpuCoefficientOutput {
    buffer: Retained<ProtocolObject<dyn MTLBuffer>>,
    upload_ms: f64,
    acceleration_structure_ms: f64,
    tracing_ms: f64,
}

unsafe impl Send for AccelerationResources {}
unsafe impl Sync for AccelerationResources {}

#[derive(Clone)]
struct ResidentScene {
    revision: u64,
    acceleration: Arc<AccelerationResources>,
}

impl MetalBackend {
    pub fn new() -> Result<Self> {
        let device = MTLCreateSystemDefaultDevice().ok_or_else(|| DaylightError::Backend {
            detail: "Metal is unavailable on this system".into(),
        })?;
        let command_queue = device
            .newCommandQueue()
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to create the Metal command queue".into(),
            })?;
        let annual_source = format!(
            "{}\n{}",
            include_str!("../shaders/contracts.metal"),
            include_str!("../shaders/annual_reduce.metal")
                .replace("#include \"contracts.metal\"", "")
        );
        let annual_pipeline = compile_pipeline(&device, &annual_source, "annual_reduce")?;
        let annual_illuminance_pipeline =
            compile_pipeline(&device, &annual_source, "annual_illuminance")?;
        let direct_source = format!(
            "{}\n{}",
            include_str!("../shaders/contracts.metal"),
            include_str!("../shaders/direct_visibility.metal")
                .replace("#include \"contracts.metal\"", "")
        );
        let direct_pipeline = compile_pipeline(&device, &direct_source, "direct_visibility")?;
        let diffuse_source = format!(
            "{}\n{}",
            include_str!("../shaders/contracts.metal"),
            include_str!("../shaders/diffuse_transport.metal")
                .replace("#include \"contracts.metal\"", "")
        );
        let diffuse_pipeline = compile_pipeline(&device, &diffuse_source, "diffuse_transport")?;
        let finalize_pipeline = compile_pipeline(&device, &diffuse_source, "finalize_indirect")?;
        Ok(Self {
            device,
            command_queue,
            annual_pipeline,
            annual_illuminance_pipeline,
            direct_pipeline,
            diffuse_pipeline,
            finalize_pipeline,
            resident_scenes: Mutex::new(HashMap::new()),
        })
    }

    pub fn device_name(&self) -> String {
        self.device.name().to_string()
    }

    pub fn supports_ray_tracing(&self) -> bool {
        self.device.supportsRaytracing()
    }

    pub fn command_queue_label(&self) -> Option<String> {
        self.command_queue.label().map(|label| label.to_string())
    }

    fn reduce_annual_on_gpu(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        coefficient_buffer: &ProtocolObject<dyn MTLBuffer>,
        cancelled: &AtomicBool,
    ) -> Result<(daylight_core::AnnualMetrics, f64)> {
        let sky_buffer = self.buffer_with_data(&request.sky.values)?;
        let occupancy_buffer = self.buffer_with_data(&request.occupancy_weights)?;
        let occupied_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate occupied-weight buffer".into(),
            })?;
        let threshold_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate threshold-weight buffer".into(),
            })?;
        let continuous_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate continuous-autonomy buffer".into(),
            })?;
        let udi_lower_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate lower-UDI buffer".into(),
            })?;
        let udi_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate UDI buffer".into(),
            })?;
        let udi_upper_buffer = self
            .device
            .newBufferWithLength_options(
                scene.sensors.len() * size_of::<u32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate upper-UDI buffer".into(),
            })?;
        unsafe {
            for buffer in [
                &occupied_buffer,
                &threshold_buffer,
                &continuous_buffer,
                &udi_lower_buffer,
                &udi_buffer,
                &udi_upper_buffer,
            ] {
                std::ptr::write_bytes(
                    buffer.contents().as_ptr(),
                    0,
                    scene.sensors.len() * size_of::<u32>(),
                );
            }
        }

        let mut gpu_ms = 0.0;
        const SENSOR_TILE: usize = 256;
        for sensor_offset in (0..scene.sensors.len()).step_by(SENSOR_TILE) {
            check_cancelled(cancelled)?;
            let tile_sensor_count = (scene.sensors.len() - sensor_offset).min(SENSOR_TILE);
            let uniforms = AnnualUniforms {
                sensor_count: scene.sensors.len() as u32,
                patch_count: request.sky.basis.row_count() as u32,
                timestep_count: request.sky.timestep_count as u32,
                sensor_offset: sensor_offset as u32,
                threshold_lux: request.threshold_lux,
                udi_lower_lux: request.udi_lower_lux,
                udi_upper_lux: request.udi_upper_lux,
            };
            let command_buffer = self.command_buffer("annual reduction")?;
            let encoder =
                command_buffer
                    .computeCommandEncoder()
                    .ok_or_else(|| DaylightError::Backend {
                        detail: "failed to create annual reduction encoder".into(),
                    })?;
            encoder.setComputePipelineState(&self.annual_pipeline);
            unsafe {
                encoder.setBytes_length_atIndex(
                    NonNull::from(&uniforms).cast::<c_void>(),
                    size_of::<AnnualUniforms>(),
                    0,
                );
                encoder.setBuffer_offset_atIndex(Some(coefficient_buffer), 0, 1);
                encoder.setBuffer_offset_atIndex(Some(&sky_buffer), 0, 2);
                encoder.setBuffer_offset_atIndex(Some(&occupancy_buffer), 0, 3);
                encoder.setBuffer_offset_atIndex(Some(&occupied_buffer), 0, 4);
                encoder.setBuffer_offset_atIndex(Some(&threshold_buffer), 0, 5);
                encoder.setBuffer_offset_atIndex(Some(&continuous_buffer), 0, 6);
                encoder.setBuffer_offset_atIndex(Some(&udi_lower_buffer), 0, 7);
                encoder.setBuffer_offset_atIndex(Some(&udi_buffer), 0, 8);
                encoder.setBuffer_offset_atIndex(Some(&udi_upper_buffer), 0, 9);
            }
            encoder.dispatchThreads_threadsPerThreadgroup(
                MTLSize {
                    width: request.sky.timestep_count,
                    height: tile_sensor_count,
                    depth: 1,
                },
                MTLSize {
                    width: self.annual_pipeline.threadExecutionWidth().max(1),
                    height: 1,
                    depth: 1,
                },
            );
            encoder.endEncoding();
            gpu_ms += complete(command_buffer, "annual reduction")?;
        }

        let occupied_accumulators = unsafe {
            std::slice::from_raw_parts(
                occupied_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let threshold_accumulators = unsafe {
            std::slice::from_raw_parts(
                threshold_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let continuous_accumulators = unsafe {
            std::slice::from_raw_parts(
                continuous_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let udi_lower_accumulators = unsafe {
            std::slice::from_raw_parts(
                udi_lower_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let udi_accumulators = unsafe {
            std::slice::from_raw_parts(
                udi_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let udi_upper_accumulators = unsafe {
            std::slice::from_raw_parts(
                udi_upper_buffer.contents().as_ptr().cast::<u32>(),
                scene.sensors.len(),
            )
        };
        let occupied_weight =
            occupied_accumulators.first().copied().unwrap_or(0) as f32 / ANNUAL_ACCUMULATOR_SCALE;
        let threshold_weights = threshold_accumulators
            .iter()
            .map(|value| *value as f32 / ANNUAL_ACCUMULATOR_SCALE)
            .collect::<Vec<_>>();
        let to_weights = |values: &[u32]| {
            values
                .iter()
                .map(|value| *value as f32 / ANNUAL_ACCUMULATOR_SCALE)
                .collect::<Vec<_>>()
        };
        let continuous_weights = to_weights(continuous_accumulators);
        let udi_lower_weights = to_weights(udi_lower_accumulators);
        let udi_weights = to_weights(udi_accumulators);
        let udi_upper_weights = to_weights(udi_upper_accumulators);
        let metrics = annual_metrics_from_accumulators(
            &scene.sensors,
            occupied_weight,
            &threshold_weights,
            &continuous_weights,
            &udi_lower_weights,
            &udi_weights,
            &udi_upper_weights,
            request.threshold_lux,
            request.udi_lower_lux,
            request.udi_upper_lux,
            request.time_fraction,
        )?;
        Ok((metrics, gpu_ms))
    }

    fn annual_illuminance_on_gpu(
        &self,
        request: &AnalysisRequest,
        sensor_count: usize,
        coefficient_buffer: &ProtocolObject<dyn MTLBuffer>,
    ) -> Result<AnnualIlluminance> {
        let sky_buffer = self.buffer_with_data(&request.sky.values)?;
        let value_count = sensor_count * request.sky.timestep_count;
        let output = self
            .device
            .newBufferWithLength_options(
                value_count * size_of::<f32>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate annual illuminance buffer".into(),
            })?;
        let uniforms = AnnualUniforms {
            sensor_count: sensor_count as u32,
            patch_count: request.sky.basis.row_count() as u32,
            timestep_count: request.sky.timestep_count as u32,
            sensor_offset: 0,
            threshold_lux: request.threshold_lux,
            udi_lower_lux: request.udi_lower_lux,
            udi_upper_lux: request.udi_upper_lux,
        };
        let command_buffer = self.command_buffer("annual illuminance")?;
        let encoder =
            command_buffer
                .computeCommandEncoder()
                .ok_or_else(|| DaylightError::Backend {
                    detail: "failed to create annual illuminance encoder".into(),
                })?;
        encoder.setComputePipelineState(&self.annual_illuminance_pipeline);
        unsafe {
            encoder.setBytes_length_atIndex(
                NonNull::from(&uniforms).cast::<c_void>(),
                size_of::<AnnualUniforms>(),
                0,
            );
            encoder.setBuffer_offset_atIndex(Some(coefficient_buffer), 0, 1);
            encoder.setBuffer_offset_atIndex(Some(&sky_buffer), 0, 2);
            encoder.setBuffer_offset_atIndex(Some(&output), 0, 3);
        }
        encoder.dispatchThreads_threadsPerThreadgroup(
            MTLSize {
                width: request.sky.timestep_count,
                height: sensor_count,
                depth: 1,
            },
            MTLSize {
                width: self
                    .annual_illuminance_pipeline
                    .threadExecutionWidth()
                    .max(1)
                    .min(request.sky.timestep_count),
                height: 1,
                depth: 1,
            },
        );
        encoder.endEncoding();
        complete(command_buffer, "annual illuminance")?;
        let values = unsafe {
            std::slice::from_raw_parts(output.contents().as_ptr().cast::<f32>(), value_count)
        }
        .to_vec();
        Ok(AnnualIlluminance {
            sensor_count,
            timestep_count: request.sky.timestep_count,
            values,
        })
    }

    fn trace_coefficients_on_gpu(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        resident: Option<&AccelerationResources>,
    ) -> Result<GpuCoefficientOutput> {
        let acceleration_started = Instant::now();
        let built_acceleration = if resident.is_none() {
            Some(self.build_acceleration_structures(scene)?)
        } else {
            None
        };
        let acceleration =
            resident
                .or(built_acceleration.as_ref())
                .ok_or_else(|| DaylightError::Backend {
                    detail: "resident acceleration structure is unavailable".into(),
                })?;
        let acceleration_structure_ms = if built_acceleration.is_some() {
            acceleration_started.elapsed().as_secs_f64() * 1_000.0
        } else {
            0.0
        };

        let upload_started = Instant::now();
        let basis = request.sky.basis;
        let directions = patch_sample_directions(basis, request.direct_samples);
        let solid_angles = patch_solid_angles(basis);
        let metadata = scene
            .instances
            .iter()
            .map(|instance| InstanceMetadata {
                room_id: instance.room_id,
                mesh_id: instance.mesh_index,
                material_offset: scene.meshes[instance.mesh_index as usize].first_triangle,
                dirty_revision: 0,
            })
            .collect::<Vec<_>>();
        let triangle_normals = triangle_normals(scene)?;
        let normal_transforms = scene
            .instances
            .iter()
            .map(|instance| normal_transform(instance.transform))
            .collect::<Result<Vec<_>>>()?;
        let sensor_buffer = self.buffer_with_data(&scene.sensors)?;
        let direction_buffer = self.buffer_with_data(&directions)?;
        let solid_angle_buffer = self.buffer_with_data(&solid_angles)?;
        let metadata_buffer = self.buffer_with_data(&metadata)?;
        let triangle_material_buffer = self.buffer_with_data(&scene.triangle_materials)?;
        let material_buffer = self.buffer_with_data(&scene.materials)?;
        let triangle_normal_buffer = self.buffer_with_data(&triangle_normals)?;
        let normal_transform_buffer = self.buffer_with_data(&normal_transforms)?;
        let output_len = scene.sensors.len() * basis.row_count();
        let output_buffer = self
            .device
            .newBufferWithLength_options(
                output_len * size_of::<[f32; 3]>(),
                MTLResourceOptions::StorageModeShared,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate direct coefficient buffer".into(),
            })?;
        unsafe {
            std::ptr::write_bytes(
                output_buffer.contents().as_ptr(),
                0,
                output_len * size_of::<[f32; 3]>(),
            );
        }
        let upload_ms = upload_started.elapsed().as_secs_f64() * 1_000.0;

        let uniforms = DirectUniforms {
            sensor_count: scene.sensors.len() as u32,
            patch_count: basis.row_count() as u32,
            direct_sample_count: request.direct_samples,
            active_category_mask: u32::MAX,
            maximum_transparent_intersections: MAXIMUM_TRANSPARENT_INTERSECTIONS,
            padding: [0; 3],
        };
        let command_buffer = self.command_buffer("direct visibility")?;
        let encoder =
            command_buffer
                .computeCommandEncoder()
                .ok_or_else(|| DaylightError::Backend {
                    detail: "failed to create direct visibility encoder".into(),
                })?;
        encoder.setComputePipelineState(&self.direct_pipeline);
        unsafe {
            encoder.setBytes_length_atIndex(
                NonNull::from(&uniforms).cast::<c_void>(),
                size_of::<DirectUniforms>(),
                0,
            );
            encoder.setBuffer_offset_atIndex(Some(&sensor_buffer), 0, 1);
            encoder.setBuffer_offset_atIndex(Some(&direction_buffer), 0, 2);
            encoder.setBuffer_offset_atIndex(Some(&solid_angle_buffer), 0, 3);
            encoder.setBuffer_offset_atIndex(Some(&metadata_buffer), 0, 4);
            encoder.setBuffer_offset_atIndex(Some(&triangle_material_buffer), 0, 5);
            encoder.setBuffer_offset_atIndex(Some(&material_buffer), 0, 6);
            encoder.setBuffer_offset_atIndex(Some(&triangle_normal_buffer), 0, 7);
            encoder.setBuffer_offset_atIndex(Some(&normal_transform_buffer), 0, 8);
            encoder.setBuffer_offset_atIndex(Some(&output_buffer), 0, 9);
            encoder.setAccelerationStructure_atBufferIndex(Some(&acceleration.top_level), 10);
        }
        encoder.dispatchThreads_threadsPerThreadgroup(
            MTLSize {
                width: basis.row_count(),
                height: scene.sensors.len(),
                depth: 1,
            },
            MTLSize {
                width: self
                    .direct_pipeline
                    .threadExecutionWidth()
                    .max(1)
                    .min(basis.row_count()),
                height: 1,
                depth: 1,
            },
        );
        encoder.endEncoding();
        let mut tracing_ms = complete(command_buffer, "direct visibility")?;

        if request.maximum_samples > 0 && request.maximum_bounces > 0 {
            let accumulator_len = output_len * 3;
            let indirect_buffer = self
                .device
                .newBufferWithLength_options(
                    accumulator_len * size_of::<u32>(),
                    MTLResourceOptions::StorageModeShared,
                )
                .ok_or_else(|| DaylightError::Backend {
                    detail: "failed to allocate indirect coefficient buffer".into(),
                })?;
            unsafe {
                std::ptr::write_bytes(
                    indirect_buffer.contents().as_ptr(),
                    0,
                    accumulator_len * size_of::<u32>(),
                );
            }
            let transport_uniforms = TransportUniforms {
                sensor_count: scene.sensors.len() as u32,
                sample_offset: 0,
                sample_count: request.maximum_samples,
                maximum_bounces: request.maximum_bounces,
                patch_count: basis.row_count() as u32,
                active_category_mask: u32::MAX,
                maximum_transparent_intersections: MAXIMUM_TRANSPARENT_INTERSECTIONS,
                padding: 0,
                scene_seed_low: request.scene_seed as u32,
                scene_seed_high: (request.scene_seed >> 32) as u32,
                accumulator_scale: TRANSPORT_ACCUMULATOR_SCALE,
                padding_two: 0,
            };
            let command_buffer = self.command_buffer("diffuse transport")?;
            let encoder =
                command_buffer
                    .computeCommandEncoder()
                    .ok_or_else(|| DaylightError::Backend {
                        detail: "failed to create diffuse transport encoder".into(),
                    })?;
            encoder.setComputePipelineState(&self.diffuse_pipeline);
            unsafe {
                encoder.setBytes_length_atIndex(
                    NonNull::from(&transport_uniforms).cast::<c_void>(),
                    size_of::<TransportUniforms>(),
                    0,
                );
                encoder.setBuffer_offset_atIndex(Some(&sensor_buffer), 0, 1);
                encoder.setBuffer_offset_atIndex(Some(&direction_buffer), 0, 2);
                encoder.setBuffer_offset_atIndex(Some(&metadata_buffer), 0, 3);
                encoder.setBuffer_offset_atIndex(Some(&triangle_material_buffer), 0, 4);
                encoder.setBuffer_offset_atIndex(Some(&material_buffer), 0, 5);
                encoder.setBuffer_offset_atIndex(Some(&triangle_normal_buffer), 0, 6);
                encoder.setBuffer_offset_atIndex(Some(&normal_transform_buffer), 0, 7);
                encoder.setBuffer_offset_atIndex(Some(&indirect_buffer), 0, 8);
                encoder.setAccelerationStructure_atBufferIndex(Some(&acceleration.top_level), 9);
            }
            encoder.dispatchThreads_threadsPerThreadgroup(
                MTLSize {
                    width: request.maximum_samples as usize,
                    height: scene.sensors.len(),
                    depth: 1,
                },
                MTLSize {
                    width: self
                        .diffuse_pipeline
                        .threadExecutionWidth()
                        .max(1)
                        .min(request.maximum_samples as usize),
                    height: 1,
                    depth: 1,
                },
            );
            encoder.endEncoding();
            tracing_ms += complete(command_buffer, "diffuse transport")?;

            let finalize_uniforms = FinalizeUniforms {
                coefficient_count: output_len as u32,
                accumulator_scale: TRANSPORT_ACCUMULATOR_SCALE,
                padding: [0; 2],
            };
            let command_buffer = self.command_buffer("finalize indirect coefficients")?;
            let encoder =
                command_buffer
                    .computeCommandEncoder()
                    .ok_or_else(|| DaylightError::Backend {
                        detail: "failed to create indirect finalization encoder".into(),
                    })?;
            encoder.setComputePipelineState(&self.finalize_pipeline);
            unsafe {
                encoder.setBytes_length_atIndex(
                    NonNull::from(&finalize_uniforms).cast::<c_void>(),
                    size_of::<FinalizeUniforms>(),
                    0,
                );
                encoder.setBuffer_offset_atIndex(Some(&indirect_buffer), 0, 1);
                encoder.setBuffer_offset_atIndex(Some(&output_buffer), 0, 2);
            }
            encoder.dispatchThreads_threadsPerThreadgroup(
                MTLSize {
                    width: output_len,
                    height: 1,
                    depth: 1,
                },
                MTLSize {
                    width: self
                        .finalize_pipeline
                        .threadExecutionWidth()
                        .max(1)
                        .min(output_len),
                    height: 1,
                    depth: 1,
                },
            );
            encoder.endEncoding();
            tracing_ms += complete(command_buffer, "finalize indirect coefficients")?;
        }

        Ok(GpuCoefficientOutput {
            buffer: output_buffer,
            upload_ms,
            acceleration_structure_ms,
            tracing_ms,
        })
    }

    fn build_acceleration_structures(&self, scene: &SceneData) -> Result<AccelerationResources> {
        let vertex_buffer = self.buffer_with_data(&scene.vertices)?;
        let mut bottom_levels = Vec::with_capacity(scene.meshes.len());
        for mesh in &scene.meshes {
            let triangle_start = mesh.first_triangle as usize;
            let triangle_end = triangle_start + mesh.triangle_count as usize;
            let index_buffer =
                self.buffer_with_data(&scene.triangles[triangle_start..triangle_end])?;
            let geometry = MTLAccelerationStructureTriangleGeometryDescriptor::descriptor();
            geometry.setOpaque(true);
            geometry.setVertexBuffer(Some(&vertex_buffer));
            geometry.setVertexStride(size_of::<daylight_core::Vec3>());
            geometry.setIndexBuffer(Some(&index_buffer));
            geometry.setIndexType(MTLIndexType::UInt32);
            geometry.setTriangleCount(mesh.triangle_count as usize);
            let geometry: Retained<MTLAccelerationStructureGeometryDescriptor> =
                unsafe { Retained::cast_unchecked(geometry) };
            let geometries = NSArray::from_retained_slice(&[geometry]);
            let descriptor = MTLPrimitiveAccelerationStructureDescriptor::descriptor();
            descriptor.setGeometryDescriptors(Some(&geometries));
            bottom_levels.push(self.build_acceleration_structure(&descriptor)?);
        }

        let instance_descriptors = scene
            .instances
            .iter()
            .enumerate()
            .map(
                |(instance_index, instance)| MTLAccelerationStructureUserIDInstanceDescriptor {
                    transformationMatrix: packed_transform(instance.transform),
                    options: MTLAccelerationStructureInstanceOptions::DisableTriangleCulling,
                    mask: instance.category_mask,
                    intersectionFunctionTableOffset: 0,
                    accelerationStructureIndex: instance.mesh_index,
                    userID: instance_index as u32,
                },
            )
            .collect::<Vec<_>>();
        let instance_bytes = unsafe {
            std::slice::from_raw_parts(
                instance_descriptors.as_ptr().cast::<u8>(),
                std::mem::size_of_val(instance_descriptors.as_slice()),
            )
        };
        let instance_buffer = self.buffer_with_data(instance_bytes)?;
        let acceleration_array = NSArray::from_retained_slice(&bottom_levels);
        let descriptor = MTLInstanceAccelerationStructureDescriptor::descriptor();
        descriptor.setInstanceDescriptorBuffer(Some(&instance_buffer));
        descriptor.setInstanceCount(instance_descriptors.len());
        descriptor
            .setInstanceDescriptorType(MTLAccelerationStructureInstanceDescriptorType::UserID);
        unsafe {
            descriptor.setInstanceDescriptorStride(size_of::<
                MTLAccelerationStructureUserIDInstanceDescriptor,
            >());
        }
        descriptor.setInstancedAccelerationStructures(Some(&acceleration_array));
        let top_level = self.build_acceleration_structure(&descriptor)?;
        Ok(AccelerationResources {
            top_level,
            _bottom_levels: bottom_levels,
        })
    }

    fn build_acceleration_structure(
        &self,
        descriptor: &MTLAccelerationStructureDescriptor,
    ) -> Result<Retained<ProtocolObject<dyn MTLAccelerationStructure>>> {
        let sizes = self
            .device
            .accelerationStructureSizesWithDescriptor(descriptor);
        let acceleration = self
            .device
            .newAccelerationStructureWithSize(sizes.accelerationStructureSize)
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate an acceleration structure".into(),
            })?;
        let scratch = self
            .device
            .newBufferWithLength_options(
                sizes.buildScratchBufferSize,
                MTLResourceOptions::StorageModePrivate,
            )
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to allocate acceleration-structure scratch memory".into(),
            })?;
        let command_buffer = self.command_buffer("acceleration-structure build")?;
        let encoder = command_buffer
            .accelerationStructureCommandEncoder()
            .ok_or_else(|| DaylightError::Backend {
                detail: "failed to create acceleration-structure encoder".into(),
            })?;
        encoder.buildAccelerationStructure_descriptor_scratchBuffer_scratchBufferOffset(
            &acceleration,
            descriptor,
            &scratch,
            0,
        );
        encoder.endEncoding();
        complete(command_buffer, "acceleration-structure build")?;
        Ok(acceleration)
    }

    fn buffer_with_data<T: Pod>(
        &self,
        values: &[T],
    ) -> Result<Retained<ProtocolObject<dyn MTLBuffer>>> {
        let pointer =
            NonNull::new(values.as_ptr() as *mut c_void).ok_or_else(|| DaylightError::Backend {
                detail: "cannot upload an empty Metal buffer".into(),
            })?;
        unsafe {
            self.device
                .newBufferWithBytes_length_options(
                    pointer,
                    std::mem::size_of_val(values),
                    MTLResourceOptions::StorageModeShared,
                )
                .ok_or_else(|| DaylightError::Backend {
                    detail: "failed to upload a shared Metal buffer".into(),
                })
        }
    }

    fn command_buffer(
        &self,
        operation: &str,
    ) -> Result<Retained<ProtocolObject<dyn MTLCommandBuffer>>> {
        self.command_queue
            .commandBuffer()
            .ok_or_else(|| DaylightError::Backend {
                detail: format!("failed to create {operation} command buffer"),
            })
    }

    fn resident_acceleration(
        &self,
        handle: &SceneHandle,
        scene: &SceneData,
    ) -> Result<Arc<AccelerationResources>> {
        if let Some(resident) = self
            .resident_scenes
            .lock()
            .map_err(|_| DaylightError::Backend {
                detail: "resident scene cache is poisoned".into(),
            })?
            .get(&handle.id())
            .filter(|resident| resident.revision == handle.revision())
            .cloned()
        {
            return Ok(resident.acceleration);
        }
        let acceleration = Arc::new(self.build_acceleration_structures(scene)?);
        self.resident_scenes
            .lock()
            .map_err(|_| DaylightError::Backend {
                detail: "resident scene cache is poisoned".into(),
            })?
            .insert(
                handle.id(),
                ResidentScene {
                    revision: handle.revision(),
                    acceleration: Arc::clone(&acceleration),
                },
            );
        Ok(acceleration)
    }

    fn analyze_internal(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        solver_revision: u64,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
        resident: Option<&AccelerationResources>,
    ) -> Result<AnalysisResult> {
        check_cancelled(cancelled)?;
        let mut scene = scene.clone();
        scene.validate()?;
        request.sky.validate()?;
        validate_request(request)?;
        let gpu_coefficients = if let Some(coefficients) = &request.coefficient_override {
            coefficients.validate()?;
            if coefficients.sensor_count != scene.sensors.len()
                || coefficients.basis != request.sky.basis
            {
                return Err(DaylightError::InvalidShape {
                    field: "coefficient_override",
                    detail: "coefficient sensor count and basis must match the request".into(),
                });
            }
            let upload_started = Instant::now();
            let buffer = self.buffer_with_data(&coefficients.values)?;
            GpuCoefficientOutput {
                buffer,
                upload_ms: upload_started.elapsed().as_secs_f64() * 1_000.0,
                acceleration_structure_ms: 0.0,
                tracing_ms: 0.0,
            }
        } else {
            self.trace_coefficients_on_gpu(&scene, request, resident)?
        };
        progress(0.75);
        check_cancelled(cancelled)?;
        let (annual, annual_reduction_ms) =
            self.reduce_annual_on_gpu(&scene, request, &gpu_coefficients.buffer, cancelled)?;
        let annual_illuminance = if request.export_illuminance {
            Some(self.annual_illuminance_on_gpu(
                request,
                scene.sensors.len(),
                &gpu_coefficients.buffer,
            )?)
        } else {
            None
        };
        check_cancelled(cancelled)?;
        let coefficients = coefficient_matrix_from_buffer(
            &gpu_coefficients.buffer,
            scene.sensors.len(),
            request.sky.basis,
        )?;
        let daylight_factor = Some(compute_daylight_factor(&coefficients, &scene)?);
        progress(1.0);
        Ok(AnalysisResult {
            solver_revision,
            coefficients: request.export_coefficients.then_some(coefficients),
            annual_illuminance,
            annual,
            daylight_factor,
            sample_count: request.maximum_samples,
            bounce_count: request.maximum_bounces,
            timings: GpuTimings {
                upload_ms: gpu_coefficients.upload_ms,
                acceleration_structure_ms: gpu_coefficients.acceleration_structure_ms,
                tracing_ms: gpu_coefficients.tracing_ms,
                annual_reduction_ms,
                ..GpuTimings::default()
            },
            metadata: AnalysisMetadata {
                metric_label: "static_sDA300_50".into(),
                solver_version: SOLVER_VERSION.into(),
                scene_fingerprint: scene_fingerprint(&scene),
                basis: request.sky.basis,
                quality: request.quality,
                glazing_model: "radiance_thin_glass_non_refracting".into(),
                schedule_timestep_count: request.sky.timestep_count,
                direct_sample_count: request.direct_samples,
                convergence: 1.0,
                transport_backend: "metal".into(),
                used_reference_fallback: false,
            },
        })
    }
}

fn validate_request(request: &AnalysisRequest) -> Result<()> {
    if request.occupancy_weights.len() != request.sky.timestep_count {
        return Err(DaylightError::InvalidShape {
            field: "occupancy_weights",
            detail: "schedule length must match sky timesteps".into(),
        });
    }
    if !request.threshold_lux.is_finite()
        || request.threshold_lux <= 0.0
        || !request.udi_lower_lux.is_finite()
        || request.udi_lower_lux < 0.0
        || !request.udi_upper_lux.is_finite()
        || request.udi_upper_lux <= request.udi_lower_lux
        || !request.time_fraction.is_finite()
        || !(0.0..=1.0).contains(&request.time_fraction)
        || request
            .occupancy_weights
            .iter()
            .any(|weight| !weight.is_finite() || *weight < 0.0)
        || request.occupancy_weights.iter().sum::<f32>() <= 0.0
    {
        return Err(DaylightError::InvalidValue {
            field: "analysis request",
            detail: "metric thresholds, time fraction, and occupancy weights are invalid".into(),
        });
    }
    if request.occupancy_weights.iter().sum::<f32>() > (u32::MAX as f32 / ANNUAL_ACCUMULATOR_SCALE)
    {
        return Err(DaylightError::InvalidValue {
            field: "occupancy_weights",
            detail: "total occupancy weight exceeds Metal annual accumulator capacity".into(),
        });
    }
    if (request.maximum_samples == 0) != (request.maximum_bounces == 0) {
        return Err(DaylightError::InvalidValue {
            field: "analysis request",
            detail: "maximum_samples and maximum_bounces must both be zero or both be positive"
                .into(),
        });
    }
    if request.direct_samples == 0 {
        return Err(DaylightError::InvalidValue {
            field: "direct_samples",
            detail: "direct_samples must be positive".into(),
        });
    }
    Ok(())
}

impl Backend for MetalBackend {
    fn capabilities(&self) -> BackendCapabilities {
        BackendCapabilities {
            name: format!(
                "Metal device: {} (GPU direct, diffuse, glass, and annual reduction)",
                self.device_name()
            ),
            hardware_acceleration: true,
            supports_ray_tracing: self.supports_ray_tracing(),
            supports_async_jobs: true,
        }
    }

    fn commit_scene(&self, scene: SceneData) -> Result<SceneHandle> {
        let handle = SceneHandle::new(scene)?;
        let snapshot = handle.snapshot()?;
        self.resident_acceleration(&handle, &snapshot)?;
        Ok(handle)
    }

    fn update_instances(&self, handle: &SceneHandle, updates: &[InstanceUpdate]) -> Result<u64> {
        let revision = handle.update_instances(updates)?;
        let snapshot = handle.snapshot()?;
        self.resident_acceleration(handle, &snapshot)?;
        Ok(revision)
    }

    fn analyze_committed(
        &self,
        handle: &SceneHandle,
        request: &AnalysisRequest,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult> {
        let scene = handle.snapshot()?;
        let acceleration = self.resident_acceleration(handle, &scene)?;
        self.analyze_internal(
            &scene,
            request,
            handle.revision(),
            cancelled,
            progress,
            Some(&acceleration),
        )
    }

    fn analyze(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        solver_revision: u64,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult> {
        self.analyze_internal(scene, request, solver_revision, cancelled, progress, None)
    }
}

fn complete(
    command_buffer: Retained<ProtocolObject<dyn MTLCommandBuffer>>,
    operation: &str,
) -> Result<f64> {
    autoreleasepool(|_| {
        command_buffer.commit();
        command_buffer.waitUntilCompleted();
        if let Some(error) = command_buffer.error() {
            return Err(DaylightError::Backend {
                detail: format!("Metal {operation} failed: {error}"),
            });
        }
        Ok((command_buffer.GPUEndTime() - command_buffer.GPUStartTime()).max(0.0) * 1_000.0)
    })
}

fn check_cancelled(cancelled: &AtomicBool) -> Result<()> {
    if cancelled.load(Ordering::Acquire) {
        Err(DaylightError::Cancelled)
    } else {
        Ok(())
    }
}

fn coefficient_matrix_from_buffer(
    buffer: &ProtocolObject<dyn MTLBuffer>,
    sensor_count: usize,
    basis: daylight_core::SkyBasis,
) -> Result<CoefficientMatrix> {
    let coefficient_count = sensor_count * basis.row_count();
    let values = unsafe {
        std::slice::from_raw_parts(
            buffer.contents().as_ptr().cast::<[f32; 3]>(),
            coefficient_count,
        )
    }
    .to_vec();
    CoefficientMatrix::new(sensor_count, basis, values)
}

fn triangle_normals(scene: &SceneData) -> Result<Vec<Vec3>> {
    scene
        .triangles
        .iter()
        .enumerate()
        .map(|(triangle_index, triangle)| {
            let first = scene.vertices[triangle[0] as usize];
            let second = scene.vertices[triangle[1] as usize];
            let third = scene.vertices[triangle[2] as usize];
            second
                .subtract(first)
                .cross(third.subtract(first))
                .normalized()
                .map_err(|_| DaylightError::InvalidValue {
                    field: "triangles",
                    detail: format!("triangle {triangle_index} is degenerate"),
                })
        })
        .collect()
}

fn normal_transform(matrix: [f32; 16]) -> Result<NormalTransform> {
    let (a, b, c) = (matrix[0], matrix[1], matrix[2]);
    let (d, e, f) = (matrix[4], matrix[5], matrix[6]);
    let (g, h, i) = (matrix[8], matrix[9], matrix[10]);
    let cofactor_zero = [e * i - f * h, f * g - d * i, d * h - e * g];
    let cofactor_one = [c * h - b * i, a * i - c * g, b * g - a * h];
    let cofactor_two = [b * f - c * e, c * d - a * f, a * e - b * d];
    let determinant = a * cofactor_zero[0] + b * cofactor_zero[1] + c * cofactor_zero[2];
    if !determinant.is_finite() || determinant.abs() <= 1.0e-10 {
        return Err(DaylightError::InvalidValue {
            field: "instances.transform",
            detail: "linear transform must be finite and invertible".into(),
        });
    }
    let inverse = determinant.recip();
    Ok(NormalTransform {
        row_zero: [
            cofactor_zero[0] * inverse,
            cofactor_zero[1] * inverse,
            cofactor_zero[2] * inverse,
            0.0,
        ],
        row_one: [
            cofactor_one[0] * inverse,
            cofactor_one[1] * inverse,
            cofactor_one[2] * inverse,
            0.0,
        ],
        row_two: [
            cofactor_two[0] * inverse,
            cofactor_two[1] * inverse,
            cofactor_two[2] * inverse,
            0.0,
        ],
    })
}

fn packed_transform(matrix: [f32; 16]) -> MTLPackedFloat4x3 {
    MTLPackedFloat4x3 {
        columns: [
            MTLPackedFloat3 {
                x: matrix[0],
                y: matrix[4],
                z: matrix[8],
            },
            MTLPackedFloat3 {
                x: matrix[1],
                y: matrix[5],
                z: matrix[9],
            },
            MTLPackedFloat3 {
                x: matrix[2],
                y: matrix[6],
                z: matrix[10],
            },
            MTLPackedFloat3 {
                x: matrix[3],
                y: matrix[7],
                z: matrix[11],
            },
        ],
    }
}

#[cfg(test)]
mod tests {
    use super::normal_transform;

    #[test]
    fn normal_transform_is_inverse_transpose() {
        let transform = normal_transform([
            2.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        ])
        .unwrap();
        assert_eq!(transform.row_zero, [0.5, 0.0, 0.0, 0.0]);
        assert_eq!(transform.row_one, [0.0, 0.25, 0.0, 0.0]);
        assert_eq!(transform.row_two, [0.0, 0.0, 0.125, 0.0]);
    }

    #[test]
    fn singular_normal_transform_is_rejected() {
        assert!(
            normal_transform([
                1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0,
            ])
            .is_err()
        );
    }
}

fn compile_pipeline(
    device: &ProtocolObject<dyn MTLDevice>,
    source: &str,
    function_name: &str,
) -> Result<Retained<ProtocolObject<dyn MTLComputePipelineState>>> {
    let source = NSString::from_str(source);
    let library = device
        .newLibraryWithSource_options_error(&source, None)
        .map_err(|error| DaylightError::Backend {
            detail: format!("failed to compile Metal source: {error}"),
        })?;
    let function_name = NSString::from_str(function_name);
    let function =
        library
            .newFunctionWithName(&function_name)
            .ok_or_else(|| DaylightError::Backend {
                detail: format!("Metal function {function_name} was not found"),
            })?;
    device
        .newComputePipelineStateWithFunction_error(&function)
        .map_err(|error| DaylightError::Backend {
            detail: format!("failed to create Metal compute pipeline: {error}"),
        })
}
