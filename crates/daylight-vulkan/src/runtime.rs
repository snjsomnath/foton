use std::{
    ffi::CStr,
    io::Cursor,
    mem::size_of,
    sync::{Arc, Mutex},
};

use ash::{Entry, vk};
use bytemuck::Pod;
use daylight_core::{DaylightError, Result, SceneData};

use crate::VulkanDevice;

pub(crate) struct Context {
    pub instance: ash::Instance,
    pub device: Arc<ash::Device>,
    pub acceleration: Arc<ash::khr::acceleration_structure::Device>,
    pub queue: vk::Queue,
    pub command_pool: vk::CommandPool,
    pub memory: vk::PhysicalDeviceMemoryProperties,
    /// Keep buffers in the GPU's own memory and copy through staging buffers.
    /// Off only when `FOTON_VULKAN_HOST_MEMORY=1` asks for the old behaviour,
    /// where every buffer lives in host-visible memory.
    pub device_local: bool,
    pub queue_lock: Mutex<()>,
    // Owns the loaded Vulkan loader; dropping it unloads the library under
    // the instance on Linux, so it must outlive every Vulkan call.
    _entry: Entry,
}

impl Context {
    /// Create a Vulkan instance and logical device for `selected`.
    pub fn new(selected: &VulkanDevice) -> Result<Arc<Self>> {
        let entry = unsafe { Entry::load() }.map_err(|error| backend(error.to_string()))?;
        let application = vk::ApplicationInfo::default()
            .application_name(c"foton")
            .api_version(vk::API_VERSION_1_3);
        let instance = unsafe {
            entry.create_instance(
                &vk::InstanceCreateInfo::default().application_info(&application),
                None,
            )
        }
        .map_err(vk_error("create Vulkan instance"))?;
        let physical_device = unsafe { instance.enumerate_physical_devices() }
            .map_err(vk_error("enumerate Vulkan devices"))?
            .into_iter()
            .find(|device| {
                let properties = unsafe { instance.get_physical_device_properties(*device) };
                properties.vendor_id == selected.vendor_id
                    && unsafe { CStr::from_ptr(properties.device_name.as_ptr()) }.to_bytes()
                        == selected.name.as_bytes()
            })
            .ok_or_else(|| backend("selected Vulkan device disappeared"))?;
        let queue_family =
            unsafe { instance.get_physical_device_queue_family_properties(physical_device) }
                .iter()
                .position(|family| family.queue_flags.contains(vk::QueueFlags::COMPUTE))
                .ok_or_else(|| backend("Vulkan device has no compute queue"))? as u32;
        let priorities = [1.0];
        let queues = [vk::DeviceQueueCreateInfo::default()
            .queue_family_index(queue_family)
            .queue_priorities(&priorities)];
        let extension_names = [
            ash::khr::acceleration_structure::NAME.as_ptr(),
            ash::khr::ray_query::NAME.as_ptr(),
            ash::khr::buffer_device_address::NAME.as_ptr(),
            ash::khr::deferred_host_operations::NAME.as_ptr(),
        ];
        let mut buffer_address =
            vk::PhysicalDeviceBufferDeviceAddressFeatures::default().buffer_device_address(true);
        let mut acceleration_features =
            vk::PhysicalDeviceAccelerationStructureFeaturesKHR::default()
                .acceleration_structure(true);
        let mut ray_query = vk::PhysicalDeviceRayQueryFeaturesKHR::default().ray_query(true);
        let mut scalar =
            vk::PhysicalDeviceScalarBlockLayoutFeatures::default().scalar_block_layout(true);
        let device_info = vk::DeviceCreateInfo::default()
            .queue_create_infos(&queues)
            .enabled_extension_names(&extension_names)
            .push_next(&mut buffer_address)
            .push_next(&mut acceleration_features)
            .push_next(&mut ray_query)
            .push_next(&mut scalar);
        let device = Arc::new(
            unsafe { instance.create_device(physical_device, &device_info, None) }
                .map_err(vk_error("create Vulkan ray-query device"))?,
        );
        let queue = unsafe { device.get_device_queue(queue_family, 0) };
        let command_pool = unsafe {
            device.create_command_pool(
                &vk::CommandPoolCreateInfo::default()
                    .queue_family_index(queue_family)
                    .flags(vk::CommandPoolCreateFlags::RESET_COMMAND_BUFFER),
                None,
            )
        }
        .map_err(vk_error("create Vulkan command pool"))?;
        let acceleration = Arc::new(ash::khr::acceleration_structure::Device::new(
            &instance, &device,
        ));
        let memory = unsafe { instance.get_physical_device_memory_properties(physical_device) };
        Ok(Arc::new(Self {
            instance,
            device,
            acceleration,
            queue,
            command_pool,
            memory,
            device_local: std::env::var("FOTON_VULKAN_HOST_MEMORY").as_deref() != Ok("1"),
            queue_lock: Mutex::new(()),
            _entry: entry,
        }))
    }

    /// Record commands with `record`, submit them and wait until the GPU has finished.
    pub fn submit<F>(&self, record: F) -> Result<()>
    where
        F: FnOnce(vk::CommandBuffer),
    {
        let _guard = self
            .queue_lock
            .lock()
            .map_err(|_| backend("Vulkan queue lock is poisoned"))?;
        let commands = unsafe {
            self.device.allocate_command_buffers(
                &vk::CommandBufferAllocateInfo::default()
                    .command_pool(self.command_pool)
                    .level(vk::CommandBufferLevel::PRIMARY)
                    .command_buffer_count(1),
            )
        }
        .map_err(vk_error("allocate Vulkan command buffer"))?;
        let command = commands[0];
        unsafe {
            self.device
                .begin_command_buffer(
                    command,
                    &vk::CommandBufferBeginInfo::default()
                        .flags(vk::CommandBufferUsageFlags::ONE_TIME_SUBMIT),
                )
                .map_err(vk_error("begin Vulkan command buffer"))?;
            // Make earlier submissions' writes visible to these commands, and
            // these commands' writes visible to the next submission and the host.
            let barrier = [vk::MemoryBarrier::default()
                .src_access_mask(vk::AccessFlags::MEMORY_WRITE)
                .dst_access_mask(vk::AccessFlags::MEMORY_READ | vk::AccessFlags::MEMORY_WRITE)];
            self.device.cmd_pipeline_barrier(
                command,
                vk::PipelineStageFlags::ALL_COMMANDS,
                vk::PipelineStageFlags::ALL_COMMANDS,
                vk::DependencyFlags::empty(),
                &barrier,
                &[],
                &[],
            );
            record(command);
            let host_barrier = [vk::MemoryBarrier::default()
                .src_access_mask(vk::AccessFlags::MEMORY_WRITE)
                .dst_access_mask(vk::AccessFlags::HOST_READ | vk::AccessFlags::MEMORY_READ)];
            self.device.cmd_pipeline_barrier(
                command,
                vk::PipelineStageFlags::ALL_COMMANDS,
                vk::PipelineStageFlags::HOST | vk::PipelineStageFlags::ALL_COMMANDS,
                vk::DependencyFlags::empty(),
                &host_barrier,
                &[],
                &[],
            );
            self.device
                .end_command_buffer(command)
                .map_err(vk_error("end Vulkan command buffer"))?;
            self.device
                .queue_submit(
                    self.queue,
                    &[vk::SubmitInfo::default().command_buffers(&commands)],
                    vk::Fence::null(),
                )
                .map_err(vk_error("submit Vulkan command buffer"))?;
            self.device
                .queue_wait_idle(self.queue)
                .map_err(vk_error("wait for Vulkan queue"))?;
            self.device
                .free_command_buffers(self.command_pool, &commands);
        }
        Ok(())
    }
}

impl Drop for Context {
    fn drop(&mut self) {
        unsafe {
            let _ = self.device.device_wait_idle();
            self.device.destroy_command_pool(self.command_pool, None);
            self.device.destroy_device(None);
            self.instance.destroy_instance(None);
        }
    }
}

pub(crate) struct Buffer {
    device: Arc<ash::Device>,
    pub handle: vk::Buffer,
    memory: vk::DeviceMemory,
    pub size: vk::DeviceSize,
    /// True when the CPU can map this buffer directly.
    host_visible: bool,
}

pub(crate) struct Pipeline {
    device: Arc<ash::Device>,
    pub pipeline: vk::Pipeline,
    pub layout: vk::PipelineLayout,
    pub descriptor_layout: vk::DescriptorSetLayout,
    descriptor_types: Vec<vk::DescriptorType>,
}

impl Pipeline {
    /// Build a compute pipeline from SPIR-V with the given descriptor bindings and push-constant size.
    pub fn new(
        context: &Context,
        spirv: &[u8],
        descriptor_types: &[vk::DescriptorType],
        push_constant_size: u32,
    ) -> Result<Self> {
        let bindings = descriptor_types
            .iter()
            .enumerate()
            .map(|(binding, descriptor_type)| {
                vk::DescriptorSetLayoutBinding::default()
                    .binding(binding as u32)
                    .descriptor_type(*descriptor_type)
                    .descriptor_count(1)
                    .stage_flags(vk::ShaderStageFlags::COMPUTE)
            })
            .collect::<Vec<_>>();
        let descriptor_layout = unsafe {
            context.device.create_descriptor_set_layout(
                &vk::DescriptorSetLayoutCreateInfo::default().bindings(&bindings),
                None,
            )
        }
        .map_err(vk_error("create Vulkan descriptor layout"))?;
        let layouts = [descriptor_layout];
        let push_ranges = [vk::PushConstantRange::default()
            .stage_flags(vk::ShaderStageFlags::COMPUTE)
            .size(push_constant_size)];
        let layout = unsafe {
            context.device.create_pipeline_layout(
                &vk::PipelineLayoutCreateInfo::default()
                    .set_layouts(&layouts)
                    .push_constant_ranges(&push_ranges),
                None,
            )
        }
        .map_err(vk_error("create Vulkan pipeline layout"))?;
        let words = ash::util::read_spv(&mut Cursor::new(spirv))
            .map_err(|error| backend(format!("read embedded SPIR-V: {error}")))?;
        let module = unsafe {
            context
                .device
                .create_shader_module(&vk::ShaderModuleCreateInfo::default().code(&words), None)
        }
        .map_err(vk_error("create Vulkan shader module"))?;
        let stage = vk::PipelineShaderStageCreateInfo::default()
            .stage(vk::ShaderStageFlags::COMPUTE)
            .module(module)
            .name(c"main");
        let pipeline = unsafe {
            context.device.create_compute_pipelines(
                vk::PipelineCache::null(),
                &[vk::ComputePipelineCreateInfo::default()
                    .stage(stage)
                    .layout(layout)],
                None,
            )
        }
        .map_err(|(_, error)| backend(format!("create Vulkan compute pipeline: {error}")))?[0];
        unsafe { context.device.destroy_shader_module(module, None) };
        Ok(Self {
            device: Arc::clone(&context.device),
            pipeline,
            layout,
            descriptor_layout,
            descriptor_types: descriptor_types.to_vec(),
        })
    }

    /// Bind buffers, the acceleration structure and push constants, and run the pipeline over `groups` work groups.
    pub fn dispatch(
        &self,
        context: &Context,
        buffers: &[&Buffer],
        acceleration: Option<vk::AccelerationStructureKHR>,
        push_constants: &[u8],
        groups: [u32; 3],
    ) -> Result<()> {
        self.dispatch_batch(context, buffers, acceleration, &[(push_constants, groups)])
    }

    /// Like `dispatch`, but record several dispatches, each with its own push
    /// constants, in one submission. The dispatches may overlap on the GPU, so
    /// they must not depend on each other's results.
    pub fn dispatch_batch(
        &self,
        context: &Context,
        buffers: &[&Buffer],
        acceleration: Option<vk::AccelerationStructureKHR>,
        dispatches: &[(&[u8], [u32; 3])],
    ) -> Result<()> {
        let storage_count = self
            .descriptor_types
            .iter()
            .filter(|kind| **kind == vk::DescriptorType::STORAGE_BUFFER)
            .count() as u32;
        let as_count = u32::from(acceleration.is_some());
        let mut pool_sizes = vec![vk::DescriptorPoolSize {
            ty: vk::DescriptorType::STORAGE_BUFFER,
            descriptor_count: storage_count,
        }];
        if as_count > 0 {
            pool_sizes.push(vk::DescriptorPoolSize {
                ty: vk::DescriptorType::ACCELERATION_STRUCTURE_KHR,
                descriptor_count: as_count,
            });
        }
        let pool = unsafe {
            context.device.create_descriptor_pool(
                &vk::DescriptorPoolCreateInfo::default()
                    .max_sets(1)
                    .pool_sizes(&pool_sizes),
                None,
            )
        }
        .map_err(vk_error("create Vulkan descriptor pool"))?;
        let layouts = [self.descriptor_layout];
        let set = unsafe {
            context.device.allocate_descriptor_sets(
                &vk::DescriptorSetAllocateInfo::default()
                    .descriptor_pool(pool)
                    .set_layouts(&layouts),
            )
        }
        .map_err(vk_error("allocate Vulkan descriptor set"))?[0];
        let buffer_infos = buffers
            .iter()
            .map(|buffer| {
                [vk::DescriptorBufferInfo::default()
                    .buffer(buffer.handle)
                    .range(buffer.size)]
            })
            .collect::<Vec<_>>();
        let mut writes = buffer_infos
            .iter()
            .enumerate()
            .map(|(binding, info)| {
                vk::WriteDescriptorSet::default()
                    .dst_set(set)
                    .dst_binding(binding as u32)
                    .descriptor_type(vk::DescriptorType::STORAGE_BUFFER)
                    .buffer_info(info)
            })
            .collect::<Vec<_>>();
        let acceleration_handles = acceleration.map(|handle| [handle]);
        let mut acceleration_info = acceleration_handles.as_ref().map(|handles| {
            vk::WriteDescriptorSetAccelerationStructureKHR::default()
                .acceleration_structures(handles)
        });
        if let Some(info) = acceleration_info.as_mut() {
            writes.push(
                vk::WriteDescriptorSet::default()
                    .dst_set(set)
                    .dst_binding(buffers.len() as u32)
                    .descriptor_type(vk::DescriptorType::ACCELERATION_STRUCTURE_KHR)
                    .descriptor_count(1)
                    .push_next(info),
            );
        }
        unsafe { context.device.update_descriptor_sets(&writes, &[]) };
        let result = context.submit(|command| unsafe {
            context.device.cmd_bind_pipeline(
                command,
                vk::PipelineBindPoint::COMPUTE,
                self.pipeline,
            );
            context.device.cmd_bind_descriptor_sets(
                command,
                vk::PipelineBindPoint::COMPUTE,
                self.layout,
                0,
                &[set],
                &[],
            );
            for (push_constants, groups) in dispatches {
                context.device.cmd_push_constants(
                    command,
                    self.layout,
                    vk::ShaderStageFlags::COMPUTE,
                    0,
                    push_constants,
                );
                context
                    .device
                    .cmd_dispatch(command, groups[0], groups[1], groups[2]);
            }
        });
        unsafe { context.device.destroy_descriptor_pool(pool, None) };
        result
    }
}

impl Drop for Pipeline {
    fn drop(&mut self) {
        unsafe {
            self.device.destroy_pipeline(self.pipeline, None);
            self.device.destroy_pipeline_layout(self.layout, None);
            self.device
                .destroy_descriptor_set_layout(self.descriptor_layout, None);
        }
    }
}

impl Buffer {
    /// Create a buffer holding a copy of `values`.
    pub fn from_data<T: Pod>(
        context: &Context,
        values: &[T],
        usage: vk::BufferUsageFlags,
    ) -> Result<Self> {
        let buffer = Self::new(
            context,
            std::mem::size_of_val(values).max(4) as u64,
            usage,
            !context.device_local,
        )?;
        buffer.write(context, values)?;
        Ok(buffer)
    }

    /// Create a buffer of `size` bytes filled with zeros.
    pub fn zeroed(context: &Context, size: usize, usage: vk::BufferUsageFlags) -> Result<Self> {
        let buffer = Self::new(context, size.max(4) as u64, usage, !context.device_local)?;
        if buffer.host_visible {
            unsafe {
                let pointer = context
                    .device
                    .map_memory(buffer.memory, 0, buffer.size, vk::MemoryMapFlags::empty())
                    .map_err(vk_error("map Vulkan buffer"))?;
                pointer.cast::<u8>().write_bytes(0, buffer.size as usize);
                context.device.unmap_memory(buffer.memory);
            }
        } else {
            context.submit(|command| unsafe {
                context
                    .device
                    .cmd_fill_buffer(command, buffer.handle, 0, vk::WHOLE_SIZE, 0);
            })?;
        }
        Ok(buffer)
    }

    /// Create a buffer of `size` bytes whose contents the GPU will overwrite
    /// before reading, such as acceleration-structure storage and scratch.
    pub fn uninitialized(
        context: &Context,
        size: usize,
        usage: vk::BufferUsageFlags,
    ) -> Result<Self> {
        Self::new(context, size.max(4) as u64, usage, !context.device_local)
    }

    fn new(
        context: &Context,
        size: vk::DeviceSize,
        usage: vk::BufferUsageFlags,
        host_visible: bool,
    ) -> Result<Self> {
        let handle = unsafe {
            context.device.create_buffer(
                &vk::BufferCreateInfo::default().size(size).usage(
                    usage
                        | vk::BufferUsageFlags::SHADER_DEVICE_ADDRESS
                        | vk::BufferUsageFlags::TRANSFER_SRC
                        | vk::BufferUsageFlags::TRANSFER_DST,
                ),
                None,
            )
        }
        .map_err(vk_error("create Vulkan buffer"))?;
        let requirements = unsafe { context.device.get_buffer_memory_requirements(handle) };
        let host_flags =
            vk::MemoryPropertyFlags::HOST_VISIBLE | vk::MemoryPropertyFlags::HOST_COHERENT;
        let allocate = |required: vk::MemoryPropertyFlags| {
            let index = memory_type(&context.memory, requirements.memory_type_bits, required)?;
            let mut flags = vk::MemoryAllocateFlagsInfo::default()
                .flags(vk::MemoryAllocateFlags::DEVICE_ADDRESS);
            Some(unsafe {
                context.device.allocate_memory(
                    &vk::MemoryAllocateInfo::default()
                        .allocation_size(requirements.size)
                        .memory_type_index(index)
                        .push_next(&mut flags),
                    None,
                )
            })
        };
        // GPU memory first. If the card is out of it, or has none this buffer
        // can use, fall back to host-visible memory: slower, but it still works.
        let device_attempt = if host_visible {
            None
        } else {
            allocate(vk::MemoryPropertyFlags::DEVICE_LOCAL)
        };
        let (memory, host_visible) = match device_attempt {
            Some(Ok(memory)) => Ok((memory, false)),
            Some(Err(error)) if error != vk::Result::ERROR_OUT_OF_DEVICE_MEMORY => {
                Err(backend(format!("allocate Vulkan buffer memory: {error}")))
            }
            _ => match allocate(host_flags) {
                Some(Ok(memory)) => Ok((memory, true)),
                Some(Err(error)) => Err(backend(format!("allocate Vulkan buffer memory: {error}"))),
                None => Err(backend(
                    "no host-visible Vulkan memory type supports the buffer",
                )),
            },
        }
        .inspect_err(|_| unsafe { context.device.destroy_buffer(handle, None) })?;
        if let Err(error) = unsafe { context.device.bind_buffer_memory(handle, memory, 0) } {
            unsafe {
                context.device.destroy_buffer(handle, None);
                context.device.free_memory(memory, None);
            }
            return Err(backend(format!("bind Vulkan buffer memory: {error}")));
        }
        Ok(Self {
            device: Arc::clone(&context.device),
            handle,
            memory,
            size,
            host_visible,
        })
    }

    /// GPU address of the buffer, for shaders that read it by pointer.
    pub fn address(&self) -> vk::DeviceAddress {
        unsafe {
            self.device.get_buffer_device_address(
                &vk::BufferDeviceAddressInfo::default().buffer(self.handle),
            )
        }
    }

    /// Copy `values` into the start of the buffer.
    pub fn write<T: Pod>(&self, context: &Context, values: &[T]) -> Result<()> {
        let bytes: &[u8] = bytemuck::cast_slice(values);
        if bytes.len() > self.size as usize {
            return Err(backend("Vulkan buffer write exceeds allocation"));
        }
        if bytes.is_empty() {
            return Ok(());
        }
        if !self.host_visible {
            let staging = Self::new(
                context,
                bytes.len() as u64,
                vk::BufferUsageFlags::empty(),
                true,
            )?;
            staging.write(context, values)?;
            let region = [vk::BufferCopy::default().size(bytes.len() as u64)];
            return context.submit(|command| unsafe {
                context
                    .device
                    .cmd_copy_buffer(command, staging.handle, self.handle, &region);
            });
        }
        unsafe {
            let pointer = self
                .device
                .map_memory(self.memory, 0, self.size, vk::MemoryMapFlags::empty())
                .map_err(vk_error("map Vulkan buffer"))?;
            std::ptr::copy_nonoverlapping(bytes.as_ptr(), pointer.cast(), bytes.len());
            self.device.unmap_memory(self.memory);
        }
        Ok(())
    }

    /// Read `count` values from the start of the buffer.
    pub fn read<T: Pod>(&self, context: &Context, count: usize) -> Result<Vec<T>> {
        let length = count * size_of::<T>();
        if length > self.size as usize {
            return Err(backend("Vulkan buffer read exceeds allocation"));
        }
        if length == 0 {
            return Ok(Vec::new());
        }
        if !self.host_visible {
            let staging = Self::new(context, length as u64, vk::BufferUsageFlags::empty(), true)?;
            let region = [vk::BufferCopy::default().size(length as u64)];
            context.submit(|command| unsafe {
                context
                    .device
                    .cmd_copy_buffer(command, self.handle, staging.handle, &region);
            })?;
            return staging.read(context, count);
        }
        unsafe {
            let pointer = self
                .device
                .map_memory(self.memory, 0, self.size, vk::MemoryMapFlags::empty())
                .map_err(vk_error("map Vulkan readback buffer"))?;
            let values = std::slice::from_raw_parts(pointer.cast::<T>(), count).to_vec();
            self.device.unmap_memory(self.memory);
            Ok(values)
        }
    }
}

impl Drop for Buffer {
    fn drop(&mut self) {
        unsafe {
            self.device.destroy_buffer(self.handle, None);
            self.device.free_memory(self.memory, None);
        }
    }
}

pub(crate) struct Acceleration {
    loader: Arc<ash::khr::acceleration_structure::Device>,
    pub handle: vk::AccelerationStructureKHR,
    _storage: Buffer,
    _resources: Vec<Buffer>,
    _bottom_levels: Vec<(vk::AccelerationStructureKHR, Buffer)>,
}

impl Drop for Acceleration {
    fn drop(&mut self) {
        unsafe {
            self.loader
                .destroy_acceleration_structure(self.handle, None);
            for (handle, _) in &self._bottom_levels {
                self.loader.destroy_acceleration_structure(*handle, None);
            }
        }
    }
}

pub(crate) fn build_acceleration(
    context: &Arc<Context>,
    scene: &SceneData,
) -> Result<Arc<Acceleration>> {
    let vertex = Buffer::from_data(
        context,
        &scene.vertices,
        vk::BufferUsageFlags::ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_KHR,
    )?;
    // One index buffer for every mesh, and every bottom-level build in one
    // submission instead of one submission and wait per mesh.
    let indices = Buffer::from_data(
        context,
        &scene.triangles,
        vk::BufferUsageFlags::ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_KHR,
    )?;
    let geometries = scene
        .meshes
        .iter()
        .map(|mesh| {
            let triangles = vk::AccelerationStructureGeometryTrianglesDataKHR::default()
                .vertex_format(vk::Format::R32G32B32_SFLOAT)
                .vertex_data(vk::DeviceOrHostAddressConstKHR {
                    device_address: vertex.address(),
                })
                .vertex_stride(size_of::<daylight_core::Vec3>() as u64)
                .max_vertex(scene.vertices.len().saturating_sub(1) as u32)
                .index_type(vk::IndexType::UINT32)
                .index_data(vk::DeviceOrHostAddressConstKHR {
                    device_address: indices.address()
                        + u64::from(mesh.first_triangle) * size_of::<[u32; 3]>() as u64,
                });
            [vk::AccelerationStructureGeometryKHR::default()
                .geometry_type(vk::GeometryTypeKHR::TRIANGLES)
                .flags(vk::GeometryFlagsKHR::OPAQUE)
                .geometry(vk::AccelerationStructureGeometryDataKHR { triangles })]
        })
        .collect::<Vec<_>>();
    let mut bottoms = Vec::with_capacity(scene.meshes.len());
    let mut scratches = Vec::with_capacity(scene.meshes.len());
    let mut infos = Vec::with_capacity(scene.meshes.len());
    for (mesh, geometry) in scene.meshes.iter().zip(&geometries) {
        let (info, handle, storage, scratch) = prepare_build(
            context,
            vk::AccelerationStructureTypeKHR::BOTTOM_LEVEL,
            geometry,
            &[mesh.triangle_count],
        )?;
        infos.push(info);
        bottoms.push((handle, storage));
        scratches.push(scratch);
    }
    let ranges = scene
        .meshes
        .iter()
        .map(|mesh| {
            [vk::AccelerationStructureBuildRangeInfoKHR::default()
                .primitive_count(mesh.triangle_count)]
        })
        .collect::<Vec<_>>();
    let range_slices = ranges
        .iter()
        .map(|range| range.as_slice())
        .collect::<Vec<_>>();
    if !infos.is_empty() {
        context.submit(|command| unsafe {
            context
                .acceleration
                .cmd_build_acceleration_structures(command, &infos, &range_slices);
        })?;
    }
    drop(scratches);
    let instances = scene
        .instances
        .iter()
        .enumerate()
        .map(|(index, instance)| {
            let bottom = bottoms[instance.mesh_index as usize].0;
            let address = unsafe {
                context
                    .acceleration
                    .get_acceleration_structure_device_address(
                        &vk::AccelerationStructureDeviceAddressInfoKHR::default()
                            .acceleration_structure(bottom),
                    )
            };
            vk::AccelerationStructureInstanceKHR {
                transform: vk::TransformMatrixKHR {
                    matrix: [
                        instance.transform[0],
                        instance.transform[1],
                        instance.transform[2],
                        instance.transform[3],
                        instance.transform[4],
                        instance.transform[5],
                        instance.transform[6],
                        instance.transform[7],
                        instance.transform[8],
                        instance.transform[9],
                        instance.transform[10],
                        instance.transform[11],
                    ],
                },
                instance_custom_index_and_mask: vk::Packed24_8::new(
                    index as u32,
                    instance.category_mask as u8,
                ),
                instance_shader_binding_table_record_offset_and_flags: vk::Packed24_8::new(
                    0,
                    vk::GeometryInstanceFlagsKHR::TRIANGLE_FACING_CULL_DISABLE.as_raw() as u8,
                ),
                acceleration_structure_reference: vk::AccelerationStructureReferenceKHR {
                    device_handle: address,
                },
            }
        })
        .collect::<Vec<_>>();
    let instance_bytes = unsafe {
        std::slice::from_raw_parts(
            instances.as_ptr().cast::<u8>(),
            std::mem::size_of_val(instances.as_slice()),
        )
    };
    let instance_buffer = Buffer::from_data(
        context,
        instance_bytes,
        vk::BufferUsageFlags::ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_KHR,
    )?;
    let instance_data = vk::AccelerationStructureGeometryInstancesDataKHR::default()
        .array_of_pointers(false)
        .data(vk::DeviceOrHostAddressConstKHR {
            device_address: instance_buffer.address(),
        });
    let geometry = vk::AccelerationStructureGeometryKHR::default()
        .geometry_type(vk::GeometryTypeKHR::INSTANCES)
        .geometry(vk::AccelerationStructureGeometryDataKHR {
            instances: instance_data,
        });
    let (handle, storage) = build_one(
        context,
        vk::AccelerationStructureTypeKHR::TOP_LEVEL,
        &[geometry],
        &[instances.len() as u32],
    )?;
    let resources = vec![vertex, indices, instance_buffer];
    let bottom_levels = bottoms;
    Ok(Arc::new(Acceleration {
        loader: Arc::clone(&context.acceleration),
        handle,
        _storage: storage,
        _resources: resources,
        _bottom_levels: bottom_levels,
    }))
}

fn build_one(
    context: &Arc<Context>,
    as_type: vk::AccelerationStructureTypeKHR,
    geometries: &[vk::AccelerationStructureGeometryKHR<'_>],
    primitive_counts: &[u32],
) -> Result<(vk::AccelerationStructureKHR, Buffer)> {
    let (info, handle, storage, _scratch) =
        prepare_build(context, as_type, geometries, primitive_counts)?;
    let ranges = primitive_counts
        .iter()
        .map(|count| vk::AccelerationStructureBuildRangeInfoKHR::default().primitive_count(*count))
        .collect::<Vec<_>>();
    context.submit(|command| unsafe {
        context.acceleration.cmd_build_acceleration_structures(
            command,
            &[info],
            &[ranges.as_slice()],
        );
    })?;
    Ok((handle, storage))
}

/// Create an acceleration structure and its scratch buffer, and return the
/// build description that fills it.
fn prepare_build<'a>(
    context: &Arc<Context>,
    as_type: vk::AccelerationStructureTypeKHR,
    geometries: &'a [vk::AccelerationStructureGeometryKHR<'a>],
    primitive_counts: &[u32],
) -> Result<(
    vk::AccelerationStructureBuildGeometryInfoKHR<'a>,
    vk::AccelerationStructureKHR,
    Buffer,
    Buffer,
)> {
    let mut build_info = vk::AccelerationStructureBuildGeometryInfoKHR::default()
        .ty(as_type)
        .flags(vk::BuildAccelerationStructureFlagsKHR::PREFER_FAST_TRACE)
        .mode(vk::BuildAccelerationStructureModeKHR::BUILD)
        .geometries(geometries);
    let mut sizes = vk::AccelerationStructureBuildSizesInfoKHR::default();
    unsafe {
        context.acceleration.get_acceleration_structure_build_sizes(
            vk::AccelerationStructureBuildTypeKHR::DEVICE,
            &build_info,
            primitive_counts,
            &mut sizes,
        );
    }
    let storage = Buffer::uninitialized(
        context,
        sizes.acceleration_structure_size as usize,
        vk::BufferUsageFlags::ACCELERATION_STRUCTURE_STORAGE_KHR,
    )?;
    let handle = unsafe {
        context.acceleration.create_acceleration_structure(
            &vk::AccelerationStructureCreateInfoKHR::default()
                .buffer(storage.handle)
                .size(sizes.acceleration_structure_size)
                .ty(as_type),
            None,
        )
    }
    .map_err(vk_error("create Vulkan acceleration structure"))?;
    let scratch = Buffer::uninitialized(
        context,
        sizes.build_scratch_size as usize,
        vk::BufferUsageFlags::STORAGE_BUFFER,
    )?;
    build_info.dst_acceleration_structure = handle;
    build_info.scratch_data = vk::DeviceOrHostAddressKHR {
        device_address: scratch.address(),
    };
    Ok((build_info, handle, storage, scratch))
}

fn memory_type(
    properties: &vk::PhysicalDeviceMemoryProperties,
    bits: u32,
    required: vk::MemoryPropertyFlags,
) -> Option<u32> {
    (0..properties.memory_type_count).find(|index| {
        bits & (1 << index) != 0
            && properties.memory_types[*index as usize]
                .property_flags
                .contains(required)
    })
}

pub(crate) fn backend(detail: impl Into<String>) -> DaylightError {
    DaylightError::Backend {
        detail: detail.into(),
    }
}

pub(crate) fn vk_error(operation: &'static str) -> impl FnOnce(vk::Result) -> DaylightError {
    move |error| backend(format!("{operation}: {error}"))
}
