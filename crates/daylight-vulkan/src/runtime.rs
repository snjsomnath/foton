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
    pub queue_lock: Mutex<()>,
}

impl Context {
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
            queue_lock: Mutex::new(()),
        }))
    }

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
            record(command);
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
}

pub(crate) struct Pipeline {
    device: Arc<ash::Device>,
    pub pipeline: vk::Pipeline,
    pub layout: vk::PipelineLayout,
    pub descriptor_layout: vk::DescriptorSetLayout,
    descriptor_types: Vec<vk::DescriptorType>,
}

impl Pipeline {
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

    pub fn dispatch(
        &self,
        context: &Context,
        buffers: &[&Buffer],
        acceleration: Option<vk::AccelerationStructureKHR>,
        push_constants: &[u8],
        groups: [u32; 3],
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
    pub fn from_data<T: Pod>(
        context: &Context,
        values: &[T],
        usage: vk::BufferUsageFlags,
    ) -> Result<Self> {
        let buffer = Self::new(context, std::mem::size_of_val(values).max(4) as u64, usage)?;
        buffer.write(values)?;
        Ok(buffer)
    }

    pub fn zeroed(context: &Context, size: usize, usage: vk::BufferUsageFlags) -> Result<Self> {
        let buffer = Self::new(context, size.max(4) as u64, usage)?;
        unsafe {
            let pointer = context
                .device
                .map_memory(buffer.memory, 0, buffer.size, vk::MemoryMapFlags::empty())
                .map_err(vk_error("map Vulkan buffer"))?;
            pointer.cast::<u8>().write_bytes(0, buffer.size as usize);
            context.device.unmap_memory(buffer.memory);
        }
        Ok(buffer)
    }

    fn new(context: &Context, size: vk::DeviceSize, usage: vk::BufferUsageFlags) -> Result<Self> {
        let handle = unsafe {
            context.device.create_buffer(
                &vk::BufferCreateInfo::default()
                    .size(size)
                    .usage(usage | vk::BufferUsageFlags::SHADER_DEVICE_ADDRESS),
                None,
            )
        }
        .map_err(vk_error("create Vulkan buffer"))?;
        let requirements = unsafe { context.device.get_buffer_memory_requirements(handle) };
        let memory_type = memory_type(
            &context.memory,
            requirements.memory_type_bits,
            vk::MemoryPropertyFlags::HOST_VISIBLE | vk::MemoryPropertyFlags::HOST_COHERENT,
        )
        .ok_or_else(|| backend("no host-visible Vulkan memory type supports the buffer"))?;
        let mut flags =
            vk::MemoryAllocateFlagsInfo::default().flags(vk::MemoryAllocateFlags::DEVICE_ADDRESS);
        let memory = unsafe {
            context.device.allocate_memory(
                &vk::MemoryAllocateInfo::default()
                    .allocation_size(requirements.size)
                    .memory_type_index(memory_type)
                    .push_next(&mut flags),
                None,
            )
        }
        .map_err(vk_error("allocate Vulkan buffer memory"))?;
        unsafe {
            context
                .device
                .bind_buffer_memory(handle, memory, 0)
                .map_err(vk_error("bind Vulkan buffer memory"))?;
        }
        Ok(Self {
            device: Arc::clone(&context.device),
            handle,
            memory,
            size,
        })
    }

    pub fn address(&self) -> vk::DeviceAddress {
        unsafe {
            self.device.get_buffer_device_address(
                &vk::BufferDeviceAddressInfo::default().buffer(self.handle),
            )
        }
    }

    pub fn write<T: Pod>(&self, values: &[T]) -> Result<()> {
        let bytes: &[u8] = bytemuck::cast_slice(values);
        if bytes.len() > self.size as usize {
            return Err(backend("Vulkan buffer write exceeds allocation"));
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

    pub fn read<T: Pod>(&self, count: usize) -> Result<Vec<T>> {
        if count * size_of::<T>() > self.size as usize {
            return Err(backend("Vulkan buffer read exceeds allocation"));
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
    let mut bottoms = Vec::with_capacity(scene.meshes.len());
    for mesh in &scene.meshes {
        let first = mesh.first_triangle as usize;
        let end = first + mesh.triangle_count as usize;
        let indices = Buffer::from_data(
            context,
            &scene.triangles[first..end],
            vk::BufferUsageFlags::ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_KHR,
        )?;
        let triangles = vk::AccelerationStructureGeometryTrianglesDataKHR::default()
            .vertex_format(vk::Format::R32G32B32_SFLOAT)
            .vertex_data(vk::DeviceOrHostAddressConstKHR {
                device_address: vertex.address(),
            })
            .vertex_stride(size_of::<daylight_core::Vec3>() as u64)
            .max_vertex(scene.vertices.len().saturating_sub(1) as u32)
            .index_type(vk::IndexType::UINT32)
            .index_data(vk::DeviceOrHostAddressConstKHR {
                device_address: indices.address(),
            });
        let geometry = vk::AccelerationStructureGeometryKHR::default()
            .geometry_type(vk::GeometryTypeKHR::TRIANGLES)
            .flags(vk::GeometryFlagsKHR::OPAQUE)
            .geometry(vk::AccelerationStructureGeometryDataKHR { triangles });
        let (handle, storage) = build_one(
            context,
            vk::AccelerationStructureTypeKHR::BOTTOM_LEVEL,
            &[geometry],
            &[mesh.triangle_count],
        )?;
        bottoms.push((handle, storage, indices));
    }
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
    let mut resources = vec![vertex, instance_buffer];
    let bottom_levels = bottoms
        .into_iter()
        .map(|(handle, storage, indices)| {
            resources.push(indices);
            (handle, storage)
        })
        .collect();
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
    let storage = Buffer::zeroed(
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
    let scratch = Buffer::zeroed(
        context,
        sizes.build_scratch_size as usize,
        vk::BufferUsageFlags::STORAGE_BUFFER,
    )?;
    build_info.dst_acceleration_structure = handle;
    build_info.scratch_data = vk::DeviceOrHostAddressKHR {
        device_address: scratch.address(),
    };
    let ranges = primitive_counts
        .iter()
        .map(|count| vk::AccelerationStructureBuildRangeInfoKHR::default().primitive_count(*count))
        .collect::<Vec<_>>();
    context.submit(|command| unsafe {
        context.acceleration.cmd_build_acceleration_structures(
            command,
            &[build_info],
            &[ranges.as_slice()],
        );
    })?;
    Ok((handle, storage))
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
