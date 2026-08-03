use std::{
    collections::HashSet,
    sync::{
        Arc, Mutex, Weak,
        atomic::{AtomicBool, Ordering},
    },
};

use daylight_core::{
    AnalysisJob, AnalysisQuality, AnalysisRequest, Backend, CoefficientMatrix, DaylightError,
    Instance, InstanceUpdate, Material, MeshRange, SceneData, SceneHandle, Sensor, SkyBasis,
    SkyMatrix, Vec3,
};
#[cfg(target_os = "macos")]
use daylight_metal::MetalBackend;
use daylight_metal::ReferenceBackend;
use daylight_vulkan::VulkanBackend;
#[cfg(target_os = "macos")]
use daylight_vulkan::is_apple_gpu;
use numpy::{
    PyArray, PyArray1, PyArray2, PyArray3, PyReadonlyArray1, PyReadonlyArray2, PyReadonlyArray3,
    PyUntypedArrayMethods,
    ndarray::{Array2, Array3},
};
use pyo3::{
    exceptions::{PyRuntimeError, PyValueError},
    prelude::*,
    types::PyDict,
};

#[pyclass(name = "Engine")]
struct PyEngine {
    backend: Arc<dyn Backend>,
}

#[pyclass(name = "Scene")]
struct PyScene {
    backend: Arc<dyn Backend>,
    handle: SceneHandle,
    active_jobs: Arc<Mutex<Vec<Weak<AtomicBool>>>>,
}

#[pyclass(name = "AnalysisJob")]
struct PyAnalysisJob {
    inner: Mutex<Option<AnalysisJob>>,
}

#[pyclass(name = "Snapshot", frozen)]
#[derive(Clone)]
struct PySnapshot {
    #[pyo3(get)]
    status: String,
    #[pyo3(get)]
    progress: f32,
    #[pyo3(get)]
    solver_revision: u64,
    #[pyo3(get)]
    message: Option<String>,
}

#[pyclass(name = "AnalysisResult", frozen)]
struct PyAnalysisResult {
    result: daylight_core::AnalysisResult,
}

#[pymethods]
impl PyEngine {
    #[new]
    #[pyo3(signature = (config=None))]
    fn new(config: Option<&Bound<'_, PyDict>>) -> PyResult<Self> {
        let requested_backend = config
            .and_then(|value| value.get_item("backend").ok().flatten())
            .map(|value| value.extract::<String>())
            .transpose()?
            .unwrap_or_else(|| "auto".into());
        let backend: Arc<dyn Backend> = match requested_backend.as_str() {
            "reference" | "cpu" => Arc::new(ReferenceBackend),
            "metal" => create_metal_backend()?,
            "vulkan" => create_vulkan_backend()?,
            "auto" => create_auto_backend(),
            other => {
                return Err(PyValueError::new_err(format!(
                    "unknown backend {other:?}; expected 'auto', 'metal', 'vulkan', or 'reference'"
                )));
            }
        };
        Ok(Self { backend })
    }

    fn capabilities(&self, py: Python<'_>) -> PyResult<Py<PyDict>> {
        let capabilities = self.backend.capabilities();
        let output = PyDict::new(py);
        output.set_item("name", capabilities.name)?;
        output.set_item("hardware_acceleration", capabilities.hardware_acceleration)?;
        output.set_item("supports_ray_tracing", capabilities.supports_ray_tracing)?;
        output.set_item("supports_async_jobs", capabilities.supports_async_jobs)?;
        Ok(output.unbind())
    }

    #[allow(clippy::too_many_arguments)]
    fn create_scene(
        &self,
        vertices: PyReadonlyArray2<'_, f32>,
        triangles: PyReadonlyArray2<'_, u32>,
        triangle_materials: PyReadonlyArray1<'_, u32>,
        mesh_ranges: PyReadonlyArray2<'_, u32>,
        instance_transforms: PyReadonlyArray3<'_, f32>,
        instance_mesh_indices: PyReadonlyArray1<'_, u32>,
        instance_room_ids: PyReadonlyArray1<'_, u32>,
        instance_masks: PyReadonlyArray1<'_, u32>,
        material_kinds: PyReadonlyArray1<'_, u32>,
        material_diffuse_rgb: PyReadonlyArray2<'_, f32>,
        material_transmittance_rgb: PyReadonlyArray2<'_, f32>,
        sensor_positions: PyReadonlyArray2<'_, f32>,
        sensor_normals: PyReadonlyArray2<'_, f32>,
        sensor_ids: PyReadonlyArray1<'_, u32>,
        sensor_room_ids: PyReadonlyArray1<'_, u32>,
        sensor_area_weights: PyReadonlyArray1<'_, f32>,
    ) -> PyResult<PyScene> {
        require_shape_2d(&vertices, "vertices", 3)?;
        require_shape_2d(&triangles, "triangles", 3)?;
        require_shape_2d(&mesh_ranges, "mesh_ranges", 2)?;
        require_shape_3d(&instance_transforms, "instance_transforms", 4, 4)?;
        require_shape_2d(&material_diffuse_rgb, "material_diffuse_rgb", 3)?;
        require_shape_2d(&material_transmittance_rgb, "material_transmittance_rgb", 3)?;
        require_shape_2d(&sensor_positions, "sensor_positions", 3)?;
        require_shape_2d(&sensor_normals, "sensor_normals", 3)?;

        let vertex_rows = rows_f32(&vertices, "vertices")?;
        let triangle_rows = rows_u32(&triangles, "triangles")?;
        let mesh_rows = rows_u32(&mesh_ranges, "mesh_ranges")?;
        let transforms = contiguous_3d(&instance_transforms, "instance_transforms")?;
        let diffuse_rows = rows_f32(&material_diffuse_rgb, "material_diffuse_rgb")?;
        let transmittance_rows =
            rows_f32(&material_transmittance_rgb, "material_transmittance_rgb")?;
        let sensor_position_rows = rows_f32(&sensor_positions, "sensor_positions")?;
        let sensor_normal_rows = rows_f32(&sensor_normals, "sensor_normals")?;

        let triangle_materials = contiguous_1d(&triangle_materials, "triangle_materials")?;
        let instance_mesh_indices = contiguous_1d(&instance_mesh_indices, "instance_mesh_indices")?;
        let instance_room_ids = contiguous_1d(&instance_room_ids, "instance_room_ids")?;
        let instance_masks = contiguous_1d(&instance_masks, "instance_masks")?;
        let material_kinds = contiguous_1d(&material_kinds, "material_kinds")?;
        let sensor_ids = contiguous_1d(&sensor_ids, "sensor_ids")?;
        let sensor_room_ids = contiguous_1d(&sensor_room_ids, "sensor_room_ids")?;
        let sensor_area_weights = contiguous_1d(&sensor_area_weights, "sensor_area_weights")?;

        let instance_count = instance_transforms.shape()[0];
        require_equal_lengths(
            "instances",
            &[
                instance_count,
                instance_mesh_indices.len(),
                instance_room_ids.len(),
                instance_masks.len(),
            ],
        )?;
        let material_count = material_kinds.len();
        require_equal_lengths(
            "materials",
            &[
                material_count,
                material_diffuse_rgb.shape()[0],
                material_transmittance_rgb.shape()[0],
            ],
        )?;
        let sensor_count = sensor_positions.shape()[0];
        require_equal_lengths(
            "sensors",
            &[
                sensor_count,
                sensor_normals.shape()[0],
                sensor_ids.len(),
                sensor_room_ids.len(),
                sensor_area_weights.len(),
            ],
        )?;

        let scene = SceneData {
            vertices: vertex_rows
                .iter()
                .map(|row| Vec3::new(row[0], row[1], row[2]))
                .collect(),
            triangles: triangle_rows
                .iter()
                .map(|row| [row[0], row[1], row[2]])
                .collect(),
            triangle_materials: triangle_materials.to_vec(),
            meshes: mesh_rows
                .iter()
                .map(|row| MeshRange {
                    first_triangle: row[0],
                    triangle_count: row[1],
                })
                .collect(),
            instances: (0..instance_count)
                .map(|index| {
                    let mut transform = [0.0; 16];
                    transform.copy_from_slice(&transforms[index * 16..(index + 1) * 16]);
                    Instance {
                        transform,
                        mesh_index: instance_mesh_indices[index],
                        room_id: instance_room_ids[index],
                        category_mask: instance_masks[index],
                        _padding: 0,
                    }
                })
                .collect(),
            materials: (0..material_count)
                .map(|index| Material {
                    kind: material_kinds[index],
                    diffuse_rgb: diffuse_rows[index],
                    transmittance_rgb: transmittance_rows[index],
                    internal_transmissivity_rgb: [0.0; 3],
                    _padding: 0,
                })
                .collect(),
            sensors: (0..sensor_count)
                .map(|index| Sensor {
                    position: Vec3::new(
                        sensor_position_rows[index][0],
                        sensor_position_rows[index][1],
                        sensor_position_rows[index][2],
                    ),
                    normal: Vec3::new(
                        sensor_normal_rows[index][0],
                        sensor_normal_rows[index][1],
                        sensor_normal_rows[index][2],
                    ),
                    sensor_id: sensor_ids[index],
                    room_id: sensor_room_ids[index],
                    area_weight: sensor_area_weights[index],
                    _padding: [0; 3],
                })
                .collect(),
        };
        let handle = self.backend.commit_scene(scene).map_err(core_error)?;
        Ok(PyScene {
            backend: Arc::clone(&self.backend),
            handle,
            active_jobs: Arc::new(Mutex::new(Vec::new())),
        })
    }
}

#[pymethods]
impl PyScene {
    #[getter]
    fn revision(&self) -> u64 {
        self.handle.revision()
    }

    fn sensor_count(&self) -> PyResult<usize> {
        Ok(self.handle.snapshot().map_err(core_error)?.sensors.len())
    }

    #[pyo3(signature = (instance_indices, transforms, room_ids=None))]
    fn update_rooms(
        &self,
        instance_indices: PyReadonlyArray1<'_, u32>,
        transforms: PyReadonlyArray3<'_, f32>,
        room_ids: Option<PyReadonlyArray1<'_, u32>>,
    ) -> PyResult<u64> {
        require_shape_3d(&transforms, "transforms", 4, 4)?;
        let indices = contiguous_1d(&instance_indices, "instance_indices")?;
        let transforms = contiguous_3d(&transforms, "transforms")?;
        if indices.len() * 16 != transforms.len() {
            return Err(PyValueError::new_err(
                "transforms must contain one [4,4] matrix per instance index",
            ));
        }
        let room_ids = room_ids
            .as_ref()
            .map(|values| contiguous_1d(values, "room_ids"))
            .transpose()?;
        if room_ids
            .as_ref()
            .is_some_and(|values| values.len() != indices.len())
        {
            return Err(PyValueError::new_err(
                "room_ids must match instance_indices length",
            ));
        }

        cancel_active_jobs(&self.active_jobs);
        let updates = indices
            .iter()
            .copied()
            .enumerate()
            .map(|(update_index, instance_index)| {
                let mut transform = [0.0; 16];
                transform.copy_from_slice(&transforms[update_index * 16..(update_index + 1) * 16]);
                InstanceUpdate {
                    instance_index: instance_index as usize,
                    transform,
                    room_id: room_ids.as_ref().map(|values| values[update_index]),
                }
            })
            .collect::<Vec<_>>();
        self.backend
            .update_instances(&self.handle, &updates)
            .map_err(core_error)
    }

    #[allow(clippy::too_many_arguments)]
    #[pyo3(signature = (
        sky,
        occupancy,
        quality="preview",
        metrics=None,
        threshold_lux=300.0,
        udi_lower_lux=100.0,
        udi_upper_lux=3000.0,
        time_fraction=0.5,
        maximum_samples=64,
        maximum_bounces=1,
        scene_seed=0,
        export_coefficients=false,
        export_illuminance=false,
        coefficient_override=None,
        supersede=true
    ))]
    fn analyze(
        &self,
        sky: PyReadonlyArray3<'_, f32>,
        occupancy: PyReadonlyArray1<'_, f32>,
        quality: &str,
        metrics: Option<Vec<String>>,
        threshold_lux: f32,
        udi_lower_lux: f32,
        udi_upper_lux: f32,
        time_fraction: f32,
        maximum_samples: u32,
        maximum_bounces: u32,
        scene_seed: u64,
        export_coefficients: bool,
        export_illuminance: bool,
        coefficient_override: Option<PyReadonlyArray3<'_, f32>>,
        supersede: bool,
    ) -> PyResult<PyAnalysisJob> {
        require_shape_3d(&sky, "sky", sky.shape()[1], 3)?;
        let basis = match sky.shape()[0] {
            daylight_core::TREGENZA_ROWS => SkyBasis::Tregenza,
            daylight_core::REINHART_MF2_ROWS => SkyBasis::ReinhartMf2,
            rows => {
                return Err(PyValueError::new_err(format!(
                    "sky has {rows} patches; expected 146 or 578 including ground"
                )));
            }
        };
        let quality = match quality {
            "preview" => AnalysisQuality::Preview,
            "final" => AnalysisQuality::Final,
            other => {
                return Err(PyValueError::new_err(format!(
                    "unknown quality {other:?}; expected 'preview' or 'final'"
                )));
            }
        };
        if quality == AnalysisQuality::Preview && basis != SkyBasis::Tregenza {
            return Err(PyValueError::new_err(
                "preview quality requires a 146-row Tregenza sky",
            ));
        }
        if quality == AnalysisQuality::Final && basis != SkyBasis::ReinhartMf2 {
            return Err(PyValueError::new_err(
                "final quality requires a 578-row Reinhart MF:2 sky",
            ));
        }
        validate_metrics(metrics.as_deref())?;
        let sky_values = contiguous_3d(&sky, "sky")?
            .chunks_exact(3)
            .map(|rgb| [rgb[0], rgb[1], rgb[2]])
            .collect();
        let sky = SkyMatrix::new(basis, sky.shape()[1], sky_values).map_err(core_error)?;
        let occupancy = contiguous_1d(&occupancy, "occupancy")?.to_vec();
        if occupancy.len() != sky.timestep_count {
            return Err(PyValueError::new_err(
                "occupancy length must match the sky timestep dimension",
            ));
        }
        let coefficient_override = coefficient_override
            .as_ref()
            .map(|values| {
                require_shape_3d(values, "coefficient_override", basis.row_count(), 3)?;
                let sensor_count = values.shape()[0];
                if sensor_count != self.handle.snapshot().map_err(core_error)?.sensors.len() {
                    return Err(PyValueError::new_err(
                        "coefficient_override sensor count must match the scene",
                    ));
                }
                let values = contiguous_3d(values, "coefficient_override")?
                    .chunks_exact(3)
                    .map(|rgb| [rgb[0], rgb[1], rgb[2]])
                    .collect();
                CoefficientMatrix::new(sensor_count, basis, values).map_err(core_error)
            })
            .transpose()?;
        if supersede {
            cancel_active_jobs(&self.active_jobs);
        }
        let request = AnalysisRequest {
            sky,
            occupancy_weights: occupancy,
            quality,
            threshold_lux,
            udi_lower_lux,
            udi_upper_lux,
            time_fraction,
            maximum_samples,
            maximum_bounces,
            scene_seed,
            export_coefficients,
            export_illuminance,
            coefficient_override,
        };
        let job = AnalysisJob::spawn(Arc::clone(&self.backend), self.handle.clone(), request);
        self.active_jobs
            .lock()
            .expect("active job lock poisoned")
            .push(Arc::downgrade(&job.cancellation_handle()));
        Ok(PyAnalysisJob {
            inner: Mutex::new(Some(job)),
        })
    }
}

#[pymethods]
impl PyAnalysisJob {
    fn poll(&self) -> PyResult<PySnapshot> {
        let guard = self.inner.lock().expect("job lock poisoned");
        let job = guard
            .as_ref()
            .ok_or_else(|| PyRuntimeError::new_err("job result was already consumed"))?;
        let snapshot = job.poll();
        Ok(PySnapshot {
            status: format!("{:?}", snapshot.status).to_lowercase(),
            progress: snapshot.progress,
            solver_revision: snapshot.solver_revision,
            message: snapshot.message,
        })
    }

    fn cancel(&self) {
        if let Some(job) = self.inner.lock().expect("job lock poisoned").as_ref() {
            job.cancel();
        }
    }

    fn result(&self, py: Python<'_>) -> PyResult<PyAnalysisResult> {
        let job = self
            .inner
            .lock()
            .expect("job lock poisoned")
            .take()
            .ok_or_else(|| PyRuntimeError::new_err("job result was already consumed"))?;
        let result = py.detach(|| job.result()).map_err(core_error)?;
        Ok(PyAnalysisResult { result })
    }
}

#[pymethods]
impl PyAnalysisResult {
    #[getter]
    fn solver_revision(&self) -> u64 {
        self.result.solver_revision
    }

    #[getter]
    fn sample_count(&self) -> u32 {
        self.result.sample_count
    }

    #[getter]
    fn bounce_count(&self) -> u32 {
        self.result.bounce_count
    }

    fn sensor_ids(&self) -> Vec<u32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.sensor_id)
            .collect()
    }

    fn daylight_autonomy(&self) -> Vec<f32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.daylight_autonomy)
            .collect()
    }

    fn continuous_daylight_autonomy(&self) -> Vec<f32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.continuous_daylight_autonomy)
            .collect()
    }

    fn useful_daylight_illuminance_lower(&self) -> Vec<f32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.useful_daylight_illuminance_lower)
            .collect()
    }

    fn useful_daylight_illuminance(&self) -> Vec<f32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.useful_daylight_illuminance)
            .collect()
    }

    fn useful_daylight_illuminance_upper(&self) -> Vec<f32> {
        self.result
            .annual
            .sensors
            .iter()
            .map(|metric| metric.useful_daylight_illuminance_upper)
            .collect()
    }

    fn room_ids(&self) -> Vec<u32> {
        self.result
            .annual
            .rooms
            .iter()
            .map(|metric| metric.room_id)
            .collect()
    }

    fn static_sda_300_50(&self) -> Vec<f32> {
        self.result
            .annual
            .rooms
            .iter()
            .map(|metric| metric.static_sda_300_50)
            .collect()
    }

    fn daylight_factor(&self) -> Option<Vec<f32>> {
        self.result
            .daylight_factor
            .as_ref()
            .map(|metric| metric.per_sensor_percent.clone())
    }

    fn has_coefficients(&self) -> bool {
        self.result.coefficients.is_some()
    }

    fn coefficients(&self, py: Python<'_>) -> PyResult<Option<Py<PyArray3<f32>>>> {
        let Some(coefficients) = self.result.coefficients.as_ref() else {
            return Ok(None);
        };
        let values = coefficients
            .values
            .iter()
            .flat_map(|rgb| rgb.iter().copied())
            .collect::<Vec<_>>();
        let array = Array3::from_shape_vec(
            (coefficients.sensor_count, coefficients.basis.row_count(), 3),
            values,
        )
        .map_err(|error| PyRuntimeError::new_err(error.to_string()))?;
        Ok(Some(PyArray::from_owned_array(py, array).unbind()))
    }

    fn annual_illuminance(&self, py: Python<'_>) -> PyResult<Option<Py<PyArray2<f32>>>> {
        let Some(illuminance) = self.result.annual_illuminance.as_ref() else {
            return Ok(None);
        };
        let array = Array2::from_shape_vec(
            (illuminance.sensor_count, illuminance.timestep_count),
            illuminance.values.clone(),
        )
        .map_err(|error| PyRuntimeError::new_err(error.to_string()))?;
        Ok(Some(PyArray::from_owned_array(py, array).unbind()))
    }

    fn timings(&self, py: Python<'_>) -> PyResult<Py<PyDict>> {
        let timings = &self.result.timings;
        let output = PyDict::new(py);
        output.set_item("upload_ms", timings.upload_ms)?;
        output.set_item(
            "acceleration_structure_ms",
            timings.acceleration_structure_ms,
        )?;
        output.set_item("tracing_ms", timings.tracing_ms)?;
        output.set_item("annual_reduction_ms", timings.annual_reduction_ms)?;
        output.set_item("snapshot_ms", timings.snapshot_ms)?;
        Ok(output.unbind())
    }

    fn metadata_json(&self) -> PyResult<String> {
        serde_json::to_string(&self.result.metadata)
            .map_err(|error| PyRuntimeError::new_err(error.to_string()))
    }

    #[getter]
    fn transport_backend(&self) -> &str {
        &self.result.metadata.transport_backend
    }

    #[getter]
    fn used_reference_fallback(&self) -> bool {
        self.result.metadata.used_reference_fallback
    }
}

#[pyfunction]
fn sky_patch_directions(py: Python<'_>, basis: &str) -> PyResult<Py<PyArray2<f32>>> {
    let directions = daylight_core::patch_directions(parse_sky_basis(basis)?);
    let values = directions
        .iter()
        .flat_map(|direction| [direction.x, direction.y, direction.z])
        .collect::<Vec<_>>();
    let array = Array2::from_shape_vec((directions.len(), 3), values)
        .map_err(|error| PyRuntimeError::new_err(error.to_string()))?;
    Ok(PyArray::from_owned_array(py, array).unbind())
}

#[pyfunction]
fn sky_patch_solid_angles(py: Python<'_>, basis: &str) -> PyResult<Py<PyArray1<f32>>> {
    Ok(PyArray::from_vec(
        py,
        daylight_core::patch_solid_angles(parse_sky_basis(basis)?),
    )
    .unbind())
}

fn parse_sky_basis(value: &str) -> PyResult<SkyBasis> {
    match value {
        "tregenza" => Ok(SkyBasis::Tregenza),
        "reinhart-mf2" | "reinhart_mf2" => Ok(SkyBasis::ReinhartMf2),
        other => Err(PyValueError::new_err(format!(
            "unknown sky basis {other:?}; expected 'tregenza' or 'reinhart-mf2'"
        ))),
    }
}

fn cancel_active_jobs(active_jobs: &Mutex<Vec<Weak<AtomicBool>>>) {
    let mut handles = active_jobs.lock().expect("active job lock poisoned");
    for handle in handles.iter().filter_map(Weak::upgrade) {
        handle.store(true, Ordering::Release);
    }
    handles.clear();
}

fn validate_metrics(metrics: Option<&[String]>) -> PyResult<()> {
    let supported = HashSet::from([
        "df",
        "da",
        "cda",
        "udi",
        "udi_lower",
        "udi_upper",
        "static_sda300_50",
    ]);
    if let Some(metrics) = metrics {
        for metric in metrics {
            if !supported.contains(metric.as_str()) {
                return Err(PyValueError::new_err(format!(
                    "unsupported metric {metric:?}; expected df, da, cda, udi, \
                     udi_lower, udi_upper, or static_sda300_50"
                )));
            }
        }
    }
    Ok(())
}

fn require_equal_lengths(field: &str, lengths: &[usize]) -> PyResult<()> {
    if lengths.windows(2).any(|pair| pair[0] != pair[1]) {
        return Err(PyValueError::new_err(format!(
            "{field} arrays have inconsistent leading dimensions: {lengths:?}"
        )));
    }
    Ok(())
}

fn require_shape_2d<T: numpy::Element>(
    array: &PyReadonlyArray2<'_, T>,
    field: &str,
    columns: usize,
) -> PyResult<()> {
    if array.shape()[1] != columns {
        return Err(PyValueError::new_err(format!(
            "{field} must have shape [N,{columns}]"
        )));
    }
    Ok(())
}

fn require_shape_3d<T: numpy::Element>(
    array: &PyReadonlyArray3<'_, T>,
    field: &str,
    second: usize,
    third: usize,
) -> PyResult<()> {
    if array.shape()[1] != second || array.shape()[2] != third {
        return Err(PyValueError::new_err(format!(
            "{field} must have shape [N,{second},{third}]"
        )));
    }
    Ok(())
}

fn rows_f32(array: &PyReadonlyArray2<'_, f32>, field: &str) -> PyResult<Vec<[f32; 3]>> {
    let values = array.as_slice().map_err(|_| {
        PyValueError::new_err(format!("{field} must be a C-contiguous float32 array"))
    })?;
    Ok(values
        .chunks_exact(3)
        .map(|row| [row[0], row[1], row[2]])
        .collect())
}

fn rows_u32(array: &PyReadonlyArray2<'_, u32>, field: &str) -> PyResult<Vec<[u32; 3]>> {
    let values = array.as_slice().map_err(|_| {
        PyValueError::new_err(format!("{field} must be a C-contiguous uint32 array"))
    })?;
    if array.shape()[1] == 2 {
        return Ok(values
            .chunks_exact(2)
            .map(|row| [row[0], row[1], 0])
            .collect());
    }
    Ok(values
        .chunks_exact(3)
        .map(|row| [row[0], row[1], row[2]])
        .collect())
}

fn contiguous_1d<'py, T: numpy::Element>(
    array: &'py PyReadonlyArray1<'py, T>,
    field: &str,
) -> PyResult<&'py [T]> {
    array.as_slice().map_err(|_| {
        PyValueError::new_err(format!(
            "{field} must be C-contiguous; call numpy.ascontiguousarray first"
        ))
    })
}

fn contiguous_3d<'py, T: numpy::Element>(
    array: &'py PyReadonlyArray3<'py, T>,
    field: &str,
) -> PyResult<&'py [T]> {
    array.as_slice().map_err(|_| {
        PyValueError::new_err(format!(
            "{field} must be C-contiguous; call numpy.ascontiguousarray first"
        ))
    })
}

#[cfg(target_os = "macos")]
fn create_metal_backend() -> PyResult<Arc<dyn Backend>> {
    Ok(Arc::new(MetalBackend::new().map_err(core_error)?))
}

fn create_vulkan_backend() -> PyResult<Arc<dyn Backend>> {
    Ok(Arc::new(VulkanBackend::new().map_err(core_error)?))
}

fn create_auto_backend() -> Arc<dyn Backend> {
    #[cfg(target_os = "macos")]
    if let Ok(backend) = MetalBackend::new() {
        if is_apple_gpu(&backend.device_name()) {
            return Arc::new(backend);
        }
    }

    if let Ok(backend) = VulkanBackend::new() {
        return Arc::new(backend);
    }
    Arc::new(ReferenceBackend)
}

#[cfg(not(target_os = "macos"))]
fn create_metal_backend() -> PyResult<Arc<dyn Backend>> {
    Err(PyRuntimeError::new_err(
        "the Metal backend is available only on macOS",
    ))
}

fn core_error(error: DaylightError) -> PyErr {
    match error {
        DaylightError::InvalidShape { .. } | DaylightError::InvalidValue { .. } => {
            PyValueError::new_err(error.to_string())
        }
        DaylightError::Cancelled => PyRuntimeError::new_err("analysis was cancelled"),
        _ => PyRuntimeError::new_err(error.to_string()),
    }
}

#[pymodule]
fn _native(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add("__version__", env!("CARGO_PKG_VERSION"))?;
    module.add_function(wrap_pyfunction!(sky_patch_directions, module)?)?;
    module.add_function(wrap_pyfunction!(sky_patch_solid_angles, module)?)?;
    module.add_class::<PyEngine>()?;
    module.add_class::<PyScene>()?;
    module.add_class::<PyAnalysisJob>()?;
    module.add_class::<PySnapshot>()?;
    module.add_class::<PyAnalysisResult>()?;
    Ok(())
}
