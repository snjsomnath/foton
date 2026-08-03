//! Vulkan device discovery and backend entry point.
//!
//! Only hardware NVIDIA, AMD, and Intel adapters exposing the Vulkan ray-query
//! extension set are candidates for the daylight transport backend.

use std::{
    collections::HashMap,
    mem::size_of,
    sync::{
        Arc, Mutex,
        atomic::{AtomicBool, Ordering},
    },
    time::Instant,
};

use ash::{Entry, vk};
use bytemuck::{Pod, Zeroable};
use daylight_core::{
    AnalysisMetadata, AnalysisRequest, AnalysisResult, AnnualIlluminance, Backend,
    BackendCapabilities, CoefficientMatrix, DaylightError, GpuTimings, InstanceUpdate, Result,
    SOLVER_VERSION, SceneData, SceneHandle, Vec3, annual_metrics_from_accumulators,
    evaluate_daylight_factor, patch_directions, patch_solid_angles, scene_fingerprint,
};

mod runtime;
use runtime::{Acceleration, Buffer, Context, Pipeline, backend, build_acceleration};

const ANNUAL_SCALE: f32 = 100_000.0;
const TRANSPORT_SCALE: f32 = 100_000_000.0;
const MAX_TRANSPARENT: u32 = 64;

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct DirectUniforms {
    sensor_count: u32,
    patch_count: u32,
    active_mask: u32,
    max_transparent: u32,
}

#[repr(C)]
#[derive(Clone, Copy, Pod, Zeroable)]
struct TransportUniforms {
    sensor_count: u32,
    sample_offset: u32,
    sample_count: u32,
    maximum_bounces: u32,
    patch_count: u32,
    active_mask: u32,
    max_transparent: u32,
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
    scale: f32,
    padding: [u32; 2],
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

const NVIDIA_VENDOR_ID: u32 = 0x10DE;
const AMD_VENDOR_ID: u32 = 0x1002;
const INTEL_VENDOR_ID: u32 = 0x8086;

pub fn is_apple_gpu(device_name: &str) -> bool {
    device_name
        .trim_start()
        .to_ascii_lowercase()
        .starts_with("apple")
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct VulkanDevice {
    pub vendor_id: u32,
    pub name: String,
    pub device_type: vk::PhysicalDeviceType,
}

impl VulkanDevice {
    pub fn vendor_name(&self) -> &'static str {
        match self.vendor_id {
            NVIDIA_VENDOR_ID => "nvidia",
            AMD_VENDOR_ID => "amd",
            INTEL_VENDOR_ID => "intel",
            _ => "unknown",
        }
    }
}

pub fn compatible_devices() -> Result<Vec<VulkanDevice>> {
    let entry = unsafe { Entry::load() }.map_err(|error| DaylightError::Backend {
        detail: format!("unable to load Vulkan loader: {error}"),
    })?;
    let application = vk::ApplicationInfo::default().api_version(vk::API_VERSION_1_3);
    let create_info = vk::InstanceCreateInfo::default().application_info(&application);
    let instance = unsafe { entry.create_instance(&create_info, None) }.map_err(|error| {
        DaylightError::Backend {
            detail: format!("unable to create Vulkan instance: {error}"),
        }
    })?;
    let result = (|| {
        let devices = unsafe { instance.enumerate_physical_devices() }.map_err(|error| {
            DaylightError::Backend {
                detail: format!("unable to enumerate Vulkan devices: {error}"),
            }
        })?;
        let mut compatible = Vec::new();
        for device in devices {
            let properties = unsafe { instance.get_physical_device_properties(device) };
            if !is_supported_vendor(properties.vendor_id)
                || !matches!(
                    properties.device_type,
                    vk::PhysicalDeviceType::DISCRETE_GPU | vk::PhysicalDeviceType::INTEGRATED_GPU
                )
                || !has_required_extensions(&instance, device)?
                || !has_required_features(&instance, device)
                || !has_compute_queue(&instance, device)
            {
                continue;
            }
            compatible.push(VulkanDevice {
                vendor_id: properties.vendor_id,
                name: unsafe { std::ffi::CStr::from_ptr(properties.device_name.as_ptr()) }
                    .to_string_lossy()
                    .into_owned(),
                device_type: properties.device_type,
            });
        }
        compatible.sort_by_key(|device| match device.device_type {
            vk::PhysicalDeviceType::DISCRETE_GPU => 0,
            vk::PhysicalDeviceType::INTEGRATED_GPU => 1,
            _ => 2,
        });
        Ok(compatible)
    })();
    unsafe { instance.destroy_instance(None) };
    result
}

fn has_compute_queue(instance: &ash::Instance, device: vk::PhysicalDevice) -> bool {
    unsafe { instance.get_physical_device_queue_family_properties(device) }
        .iter()
        .any(|family| family.queue_flags.contains(vk::QueueFlags::COMPUTE))
}

fn has_required_features(instance: &ash::Instance, device: vk::PhysicalDevice) -> bool {
    let mut buffer_address = vk::PhysicalDeviceBufferDeviceAddressFeatures::default();
    let mut acceleration = vk::PhysicalDeviceAccelerationStructureFeaturesKHR::default();
    let mut ray_query = vk::PhysicalDeviceRayQueryFeaturesKHR::default();
    let mut scalar = vk::PhysicalDeviceScalarBlockLayoutFeatures::default();
    let mut features = vk::PhysicalDeviceFeatures2::default()
        .push_next(&mut buffer_address)
        .push_next(&mut acceleration)
        .push_next(&mut ray_query)
        .push_next(&mut scalar);
    unsafe { instance.get_physical_device_features2(device, &mut features) };
    buffer_address.buffer_device_address == vk::TRUE
        && acceleration.acceleration_structure == vk::TRUE
        && ray_query.ray_query == vk::TRUE
        && scalar.scalar_block_layout == vk::TRUE
}

fn is_supported_vendor(vendor_id: u32) -> bool {
    matches!(
        vendor_id,
        NVIDIA_VENDOR_ID | AMD_VENDOR_ID | INTEL_VENDOR_ID
    )
}

fn has_required_extensions(instance: &ash::Instance, device: vk::PhysicalDevice) -> Result<bool> {
    let extensions =
        unsafe { instance.enumerate_device_extension_properties(device) }.map_err(|error| {
            DaylightError::Backend {
                detail: format!("unable to enumerate Vulkan device extensions: {error}"),
            }
        })?;
    let names = extensions
        .iter()
        .map(|extension| unsafe { std::ffi::CStr::from_ptr(extension.extension_name.as_ptr()) })
        .collect::<Vec<_>>();
    Ok([
        ash::khr::acceleration_structure::NAME,
        ash::khr::ray_query::NAME,
        ash::khr::buffer_device_address::NAME,
        ash::khr::deferred_host_operations::NAME,
    ]
    .iter()
    .all(|required| {
        names
            .iter()
            .any(|name| name.to_bytes() == required.to_bytes())
    }))
}

pub struct VulkanBackend {
    device: VulkanDevice,
    resident_scenes: Mutex<HashMap<u64, ResidentScene>>,
    direct: Pipeline,
    diffuse: Pipeline,
    finalize: Pipeline,
    annual: Pipeline,
    context: Arc<Context>,
}

#[derive(Clone)]
struct ResidentScene {
    revision: u64,
    acceleration: Arc<Acceleration>,
}

impl VulkanBackend {
    pub fn new() -> Result<Self> {
        let device =
            compatible_devices()?
                .into_iter()
                .next()
                .ok_or_else(|| DaylightError::Backend {
                    detail:
                        "no compatible NVIDIA, AMD, or Intel Vulkan ray-query device is available"
                            .into(),
                })?;
        let context = Context::new(&device)?;
        let storage = vk::DescriptorType::STORAGE_BUFFER;
        let acceleration = vk::DescriptorType::ACCELERATION_STRUCTURE_KHR;
        let direct = Pipeline::new(
            &context,
            include_bytes!(concat!(env!("OUT_DIR"), "/direct_visibility.spv")),
            &[
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                acceleration,
            ],
            size_of::<DirectUniforms>() as u32,
        )?;
        let diffuse = Pipeline::new(
            &context,
            include_bytes!(concat!(env!("OUT_DIR"), "/diffuse_transport.spv")),
            &[
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                storage,
                acceleration,
            ],
            size_of::<TransportUniforms>() as u32,
        )?;
        let finalize = Pipeline::new(
            &context,
            include_bytes!(concat!(env!("OUT_DIR"), "/finalize_indirect.spv")),
            &[storage, storage],
            size_of::<FinalizeUniforms>() as u32,
        )?;
        let annual = Pipeline::new(
            &context,
            include_bytes!(concat!(env!("OUT_DIR"), "/annual_reduce.spv")),
            &[
                storage, storage, storage, storage, storage, storage, storage, storage, storage,
            ],
            size_of::<AnnualUniforms>() as u32,
        )?;
        Ok(Self {
            device,
            resident_scenes: Mutex::new(HashMap::new()),
            context,
            direct,
            diffuse,
            finalize,
            annual,
        })
    }

    pub fn device(&self) -> &VulkanDevice {
        &self.device
    }

    fn resident_acceleration(
        &self,
        handle: &SceneHandle,
        scene: &SceneData,
    ) -> Result<Arc<Acceleration>> {
        if let Some(resident) = self
            .resident_scenes
            .lock()
            .map_err(|_| backend("Vulkan resident-scene cache is poisoned"))?
            .get(&handle.id())
            .filter(|resident| resident.revision == handle.revision())
            .cloned()
        {
            return Ok(resident.acceleration);
        }
        let acceleration = build_acceleration(&self.context, scene)?;
        self.resident_scenes
            .lock()
            .map_err(|_| backend("Vulkan resident-scene cache is poisoned"))?
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
        resident: Option<&Acceleration>,
    ) -> Result<AnalysisResult> {
        check_cancelled(cancelled)?;
        let mut scene = scene.clone();
        scene.validate()?;
        request.sky.validate()?;
        validate_request(request)?;
        let acceleration_started = Instant::now();
        let built;
        let acceleration = if let Some(resident) = resident {
            resident
        } else {
            built = build_acceleration(&self.context, &scene)?;
            &built
        };
        let acceleration_ms = if resident.is_some() {
            0.0
        } else {
            acceleration_started.elapsed().as_secs_f64() * 1_000.0
        };
        let upload_started = Instant::now();
        let common = upload_scene(&self.context, &scene, request)?;
        let coefficient_count = scene.sensors.len() * request.sky.basis.row_count();
        let coefficients = if let Some(coefficients) = &request.coefficient_override {
            coefficients.validate()?;
            if coefficients.sensor_count != scene.sensors.len()
                || coefficients.basis != request.sky.basis
            {
                return Err(DaylightError::InvalidShape {
                    field: "coefficient_override",
                    detail: "coefficient sensor count and basis must match the request".into(),
                });
            }
            Buffer::from_data(
                &self.context,
                &coefficients.values,
                vk::BufferUsageFlags::STORAGE_BUFFER,
            )?
        } else {
            Buffer::zeroed(
                &self.context,
                coefficient_count * size_of::<Vec3>(),
                vk::BufferUsageFlags::STORAGE_BUFFER,
            )?
        };
        let upload_ms = upload_started.elapsed().as_secs_f64() * 1_000.0;
        let tracing_started = Instant::now();
        if request.coefficient_override.is_none() {
            self.direct.dispatch(
                &self.context,
                &[
                    &common.sensors,
                    &common.directions,
                    &common.angles,
                    &common.metadata,
                    &common.triangle_materials,
                    &common.materials,
                    &common.triangle_normals,
                    &common.normal_transforms,
                    &coefficients,
                ],
                Some(acceleration.handle),
                bytemuck::bytes_of(&DirectUniforms {
                    sensor_count: scene.sensors.len() as u32,
                    patch_count: request.sky.basis.row_count() as u32,
                    active_mask: u32::MAX,
                    max_transparent: MAX_TRANSPARENT,
                }),
                [
                    (request.sky.basis.row_count() as u32).div_ceil(8),
                    (scene.sensors.len() as u32).div_ceil(8),
                    1,
                ],
            )?;
        }
        if request.coefficient_override.is_none() && request.maximum_samples > 0 {
            let indirect = Buffer::zeroed(
                &self.context,
                coefficient_count * 3 * size_of::<u32>(),
                vk::BufferUsageFlags::STORAGE_BUFFER,
            )?;
            self.diffuse.dispatch(
                &self.context,
                &[
                    &common.sensors,
                    &common.directions,
                    &common.metadata,
                    &common.triangle_materials,
                    &common.materials,
                    &common.triangle_normals,
                    &common.normal_transforms,
                    &indirect,
                ],
                Some(acceleration.handle),
                bytemuck::bytes_of(&TransportUniforms {
                    sensor_count: scene.sensors.len() as u32,
                    sample_offset: 0,
                    sample_count: request.maximum_samples,
                    maximum_bounces: request.maximum_bounces,
                    patch_count: request.sky.basis.row_count() as u32,
                    active_mask: u32::MAX,
                    max_transparent: MAX_TRANSPARENT,
                    padding: 0,
                    scene_seed_low: request.scene_seed as u32,
                    scene_seed_high: (request.scene_seed >> 32) as u32,
                    accumulator_scale: TRANSPORT_SCALE,
                    padding_two: 0,
                }),
                [
                    request.maximum_samples.div_ceil(8),
                    (scene.sensors.len() as u32).div_ceil(8),
                    1,
                ],
            )?;
            self.finalize.dispatch(
                &self.context,
                &[&indirect, &coefficients],
                None,
                bytemuck::bytes_of(&FinalizeUniforms {
                    coefficient_count: coefficient_count as u32,
                    scale: TRANSPORT_SCALE,
                    padding: [0; 2],
                }),
                [(coefficient_count as u32).div_ceil(64), 1, 1],
            )?;
        }
        let tracing_ms = tracing_started.elapsed().as_secs_f64() * 1_000.0;
        progress(0.75);
        check_cancelled(cancelled)?;
        let reduction_started = Instant::now();
        let occupied = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        let threshold = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        let continuous = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        let udi_lower = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        let udi = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        let udi_upper = Buffer::zeroed(
            &self.context,
            scene.sensors.len() * size_of::<u32>(),
            vk::BufferUsageFlags::STORAGE_BUFFER,
        )?;
        self.annual.dispatch(
            &self.context,
            &[
                &coefficients,
                &common.sky,
                &common.occupancy,
                &occupied,
                &threshold,
                &continuous,
                &udi_lower,
                &udi,
                &udi_upper,
            ],
            None,
            bytemuck::bytes_of(&AnnualUniforms {
                sensor_count: scene.sensors.len() as u32,
                patch_count: request.sky.basis.row_count() as u32,
                timestep_count: request.sky.timestep_count as u32,
                sensor_offset: 0,
                threshold_lux: request.threshold_lux,
                udi_lower_lux: request.udi_lower_lux,
                udi_upper_lux: request.udi_upper_lux,
            }),
            [
                (request.sky.timestep_count as u32).div_ceil(8),
                (scene.sensors.len() as u32).div_ceil(8),
                1,
            ],
        )?;
        let occupied_ticks = occupied.read::<u32>(scene.sensors.len())?;
        let threshold_ticks = threshold.read::<u32>(scene.sensors.len())?;
        let continuous_ticks = continuous.read::<u32>(scene.sensors.len())?;
        let udi_lower_ticks = udi_lower.read::<u32>(scene.sensors.len())?;
        let udi_ticks = udi.read::<u32>(scene.sensors.len())?;
        let udi_upper_ticks = udi_upper.read::<u32>(scene.sensors.len())?;
        let occupied_weight = occupied_ticks.first().copied().unwrap_or(0) as f32 / ANNUAL_SCALE;
        let to_weights = |values: Vec<u32>| {
            values
                .into_iter()
                .map(|value| value as f32 / ANNUAL_SCALE)
                .collect::<Vec<_>>()
        };
        let threshold_weights = to_weights(threshold_ticks);
        let continuous_weights = to_weights(continuous_ticks);
        let udi_lower_weights = to_weights(udi_lower_ticks);
        let udi_weights = to_weights(udi_ticks);
        let udi_upper_weights = to_weights(udi_upper_ticks);
        let annual = annual_metrics_from_accumulators(
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
        let annual_reduction_ms = reduction_started.elapsed().as_secs_f64() * 1_000.0;
        let values = coefficients
            .read::<Vec3>(coefficient_count)?
            .into_iter()
            .map(|value| [value.x, value.y, value.z])
            .collect();
        let coefficient_matrix =
            CoefficientMatrix::new(scene.sensors.len(), request.sky.basis, values)?;
        let daylight_factor = Some(compute_daylight_factor(&coefficient_matrix, &scene)?);
        let annual_illuminance = request
            .export_illuminance
            .then(|| annual_illuminance(&coefficient_matrix, request));
        progress(1.0);
        Ok(AnalysisResult {
            solver_revision,
            coefficients: request.export_coefficients.then_some(coefficient_matrix),
            annual_illuminance,
            annual,
            daylight_factor,
            sample_count: request.maximum_samples,
            bounce_count: request.maximum_bounces,
            timings: GpuTimings {
                upload_ms,
                acceleration_structure_ms: acceleration_ms,
                tracing_ms,
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
                convergence: 1.0,
                transport_backend: "vulkan".into(),
                used_reference_fallback: false,
            },
        })
    }
}

impl Backend for VulkanBackend {
    fn capabilities(&self) -> BackendCapabilities {
        BackendCapabilities {
            name: format!("Vulkan device: {}", self.device.name),
            hardware_acceleration: true,
            supports_ray_tracing: true,
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

struct SceneBuffers {
    sensors: Buffer,
    directions: Buffer,
    angles: Buffer,
    metadata: Buffer,
    triangle_materials: Buffer,
    materials: Buffer,
    triangle_normals: Buffer,
    normal_transforms: Buffer,
    sky: Buffer,
    occupancy: Buffer,
}

fn upload_scene(
    context: &Context,
    scene: &SceneData,
    request: &AnalysisRequest,
) -> Result<SceneBuffers> {
    let usage = vk::BufferUsageFlags::STORAGE_BUFFER;
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
    let normal_transforms = scene
        .instances
        .iter()
        .map(|instance| normal_transform(instance.transform))
        .collect::<Result<Vec<_>>>()?;
    Ok(SceneBuffers {
        sensors: Buffer::from_data(context, &scene.sensors, usage)?,
        directions: Buffer::from_data(context, &patch_directions(request.sky.basis), usage)?,
        angles: Buffer::from_data(context, &patch_solid_angles(request.sky.basis), usage)?,
        metadata: Buffer::from_data(context, &metadata, usage)?,
        triangle_materials: Buffer::from_data(context, &scene.triangle_materials, usage)?,
        materials: Buffer::from_data(context, &scene.materials, usage)?,
        triangle_normals: Buffer::from_data(context, &triangle_normals(scene)?, usage)?,
        normal_transforms: Buffer::from_data(context, &normal_transforms, usage)?,
        sky: Buffer::from_data(context, &request.sky.values, usage)?,
        occupancy: Buffer::from_data(context, &request.occupancy_weights, usage)?,
    })
}

fn validate_request(request: &AnalysisRequest) -> Result<()> {
    if request.occupancy_weights.len() != request.sky.timestep_count {
        return Err(DaylightError::InvalidShape {
            field: "occupancy_weights",
            detail: "schedule length must match sky timesteps".into(),
        });
    }
    let occupied: f32 = request.occupancy_weights.iter().sum();
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
        || occupied <= 0.0
        || occupied > u32::MAX as f32 / ANNUAL_SCALE
    {
        return Err(DaylightError::InvalidValue {
            field: "analysis request",
            detail: "metric thresholds, time fraction, or occupancy weights are invalid".into(),
        });
    }
    if (request.maximum_samples == 0) != (request.maximum_bounces == 0) {
        return Err(DaylightError::InvalidValue {
            field: "analysis request",
            detail: "maximum_samples and maximum_bounces must both be zero or both be positive"
                .into(),
        });
    }
    Ok(())
}

fn check_cancelled(cancelled: &AtomicBool) -> Result<()> {
    if cancelled.load(Ordering::Acquire) {
        Err(DaylightError::Cancelled)
    } else {
        Ok(())
    }
}

fn triangle_normals(scene: &SceneData) -> Result<Vec<Vec3>> {
    scene
        .triangles
        .iter()
        .enumerate()
        .map(|(index, triangle)| {
            let first = scene.vertices[triangle[0] as usize];
            let second = scene.vertices[triangle[1] as usize];
            let third = scene.vertices[triangle[2] as usize];
            second
                .subtract(first)
                .cross(third.subtract(first))
                .normalized()
                .map_err(|_| DaylightError::InvalidValue {
                    field: "triangles",
                    detail: format!("triangle {index} is degenerate"),
                })
        })
        .collect()
}

fn normal_transform(matrix: [f32; 16]) -> Result<NormalTransform> {
    let (a, b, c) = (matrix[0], matrix[1], matrix[2]);
    let (d, e, f) = (matrix[4], matrix[5], matrix[6]);
    let (g, h, i) = (matrix[8], matrix[9], matrix[10]);
    let first = [e * i - f * h, f * g - d * i, d * h - e * g];
    let second = [c * h - b * i, a * i - c * g, b * g - a * h];
    let third = [b * f - c * e, c * d - a * f, a * e - b * d];
    let determinant = a * first[0] + b * first[1] + c * first[2];
    if !determinant.is_finite() || determinant.abs() <= 1.0e-10 {
        return Err(DaylightError::InvalidValue {
            field: "instances.transform",
            detail: "linear transform must be finite and invertible".into(),
        });
    }
    let inverse = determinant.recip();
    Ok(NormalTransform {
        row_zero: [
            first[0] * inverse,
            first[1] * inverse,
            first[2] * inverse,
            0.0,
        ],
        row_one: [
            second[0] * inverse,
            second[1] * inverse,
            second[2] * inverse,
            0.0,
        ],
        row_two: [
            third[0] * inverse,
            third[1] * inverse,
            third[2] * inverse,
            0.0,
        ],
    })
}

fn annual_illuminance(
    coefficients: &CoefficientMatrix,
    request: &AnalysisRequest,
) -> AnnualIlluminance {
    let timestep_count = request.sky.timestep_count;
    let mut values = vec![0.0; coefficients.sensor_count * timestep_count];
    for sensor in 0..coefficients.sensor_count {
        for timestep in 0..timestep_count {
            let mut response = [0.0; 3];
            for patch in 0..coefficients.basis.row_count() {
                let coefficient = coefficients.get(sensor, patch);
                let sky = request.sky.get(patch, timestep);
                for component in 0..3 {
                    response[component] += coefficient[component] * sky[component];
                }
            }
            values[sensor * timestep_count + timestep] =
                response[0] * 47.435 + response[1] * 119.93 + response[2] * 11.635;
        }
    }
    AnnualIlluminance {
        sensor_count: coefficients.sensor_count,
        timestep_count,
        values,
    }
}

fn compute_daylight_factor(
    coefficients: &CoefficientMatrix,
    scene: &SceneData,
) -> Result<daylight_core::DaylightFactorMetrics> {
    let directions = patch_directions(coefficients.basis);
    let solid_angles = patch_solid_angles(coefficients.basis);
    let mut sky_luminance = vec![0.0; coefficients.basis.row_count()];
    for patch_index in 1..coefficients.basis.row_count() {
        sky_luminance[patch_index] = (1.0 + 2.0 * directions[patch_index].z.max(0.0)) / 3.0;
    }
    let exterior = (1..coefficients.basis.row_count())
        .map(|index| sky_luminance[index] * directions[index].z.max(0.0) * solid_angles[index])
        .sum();
    let interior = (0..scene.sensors.len())
        .map(|sensor| {
            (0..coefficients.basis.row_count())
                .map(|patch| {
                    let value = coefficients.get(sensor, patch);
                    (value[0] * 0.265 + value[1] * 0.67 + value[2] * 0.065) * sky_luminance[patch]
                })
                .sum()
        })
        .collect::<Vec<_>>();
    evaluate_daylight_factor(&interior, exterior)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn supports_only_hardware_vendor_allowlist() {
        assert!(is_supported_vendor(NVIDIA_VENDOR_ID));
        assert!(is_supported_vendor(AMD_VENDOR_ID));
        assert!(is_supported_vendor(INTEL_VENDOR_ID));
        assert!(!is_supported_vendor(0x106B));
    }

    #[test]
    fn recognizes_only_apple_named_metal_devices() {
        assert!(is_apple_gpu("Apple M4 Max"));
        assert!(!is_apple_gpu("AMD Radeon Pro 5600M"));
        assert!(!is_apple_gpu("Intel Iris Plus Graphics"));
    }
}
