use std::{
    sync::atomic::{AtomicBool, Ordering},
    time::Instant,
};

use daylight_core::{
    AnalysisMetadata, AnalysisRequest, AnalysisResult, AnnualIlluminance, Backend,
    BackendCapabilities, CoefficientMatrix, DaylightError, GpuTimings, MaterialKind, Result,
    SOLVER_VERSION, SceneData, Vec3, cosine_hemisphere, evaluate_daylight_factor,
    low_discrepancy_sample, patch_directions, patch_sample_directions, patch_solid_angles,
    radiance_patch_index, reduce_annual_metrics, scene_fingerprint,
    thin_glass_reflectance_from_transmissivity, thin_glass_transmittance_from_transmissivity,
};

const RAY_EPSILON: f32 = 1.0e-4;
const RAY_MIN_DISTANCE: f32 = 1.0e-6;

#[derive(Clone, Debug, Default)]
pub struct ReferenceBackend;

#[derive(Clone, Copy)]
struct Hit {
    distance: f32,
    normal: Vec3,
    material_index: usize,
}

impl Backend for ReferenceBackend {
    fn capabilities(&self) -> BackendCapabilities {
        BackendCapabilities {
            name: "deterministic-cpu-reference".into(),
            hardware_acceleration: false,
            supports_ray_tracing: false,
            supports_async_jobs: true,
        }
    }

    fn analyze(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        solver_revision: u64,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult> {
        let mut result =
            self.analyze_with_coefficients(scene, request, solver_revision, cancelled, progress)?;
        if !request.export_coefficients {
            result.coefficients = None;
        }
        Ok(result)
    }
}

impl ReferenceBackend {
    pub fn analyze_with_coefficients(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        solver_revision: u64,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult> {
        let mut scene = scene.clone();
        scene.validate()?;
        request.sky.validate()?;
        if request.occupancy_weights.len() != request.sky.timestep_count {
            return Err(DaylightError::InvalidShape {
                field: "occupancy_weights",
                detail: "schedule length must match sky timesteps".into(),
            });
        }

        let tracing_started = Instant::now();
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
            progress(0.75);
            coefficients.clone()
        } else {
            trace_coefficients(&scene, request, cancelled, progress)?
        };
        let tracing_ms = tracing_started.elapsed().as_secs_f64() * 1_000.0;

        let reduction_started = Instant::now();
        let annual = reduce_annual_metrics(
            &coefficients,
            &request.sky,
            &request.occupancy_weights,
            &scene.sensors,
            request.threshold_lux,
            request.udi_lower_lux,
            request.udi_upper_lux,
            request.time_fraction,
        )?;
        let daylight_factor = Some(compute_daylight_factor(&coefficients, &scene)?);
        let annual_illuminance = request
            .export_illuminance
            .then(|| annual_illuminance(&coefficients, request));
        let annual_reduction_ms = reduction_started.elapsed().as_secs_f64() * 1_000.0;
        progress(1.0);

        Ok(AnalysisResult {
            solver_revision,
            coefficients: Some(coefficients),
            annual_illuminance,
            annual,
            daylight_factor,
            sample_count: request.maximum_samples,
            bounce_count: request.maximum_bounces,
            timings: GpuTimings {
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
                direct_sample_count: request.direct_samples,
                convergence: 1.0,
                transport_backend: "reference".into(),
                used_reference_fallback: false,
            },
        })
    }
}

fn annual_illuminance(
    coefficients: &CoefficientMatrix,
    request: &AnalysisRequest,
) -> AnnualIlluminance {
    let timestep_count = request.sky.timestep_count;
    let mut values = vec![0.0; coefficients.sensor_count * timestep_count];
    for sensor in 0..coefficients.sensor_count {
        for timestep in 0..timestep_count {
            let mut illuminance = 0.0;
            for patch in 0..coefficients.basis.row_count() {
                let coefficient = coefficients.get(sensor, patch);
                let sky = request.sky.get(patch, timestep);
                illuminance += (coefficient[0] * sky[0]) * 47.435
                    + (coefficient[1] * sky[1]) * 119.93
                    + (coefficient[2] * sky[2]) * 11.635;
            }
            values[sensor * timestep_count + timestep] = illuminance;
        }
    }
    AnnualIlluminance {
        sensor_count: coefficients.sensor_count,
        timestep_count,
        values,
    }
}

fn trace_coefficients(
    scene: &SceneData,
    request: &AnalysisRequest,
    cancelled: &AtomicBool,
    progress: &(dyn Fn(f32) + Send + Sync),
) -> Result<CoefficientMatrix> {
    let basis = request.sky.basis;
    let patch_count = basis.row_count();
    let direct_samples = request.direct_samples.max(1);
    let directions = patch_sample_directions(basis, direct_samples);
    let solid_angles = patch_solid_angles(basis);
    let mut values = vec![[0.0; 3]; scene.sensors.len() * patch_count];
    let mut reported_bucket = 0_u32;

    for (sensor_index, sensor) in scene.sensors.iter().enumerate() {
        check_cancelled(cancelled)?;
        for patch_index in 0..patch_count {
            let mut integrated = [0.0_f32; 3];
            for sample_index in 0..direct_samples as usize {
                let direction = directions[patch_index * direct_samples as usize + sample_index];
                let cosine = sensor.normal.dot(direction).max(0.0);
                if cosine == 0.0 {
                    continue;
                }
                let transmission = visibility_transmission(
                    scene,
                    sensor.position.add(sensor.normal.scale(RAY_EPSILON)),
                    direction,
                )?;
                for component in 0..3 {
                    integrated[component] += transmission[component] * cosine;
                }
            }
            let geometric_weight = solid_angles[patch_index] / direct_samples as f32;
            for component in 0..3 {
                values[sensor_index * patch_count + patch_index][component] =
                    integrated[component] * geometric_weight;
            }
        }

        if request.maximum_bounces > 0 && request.maximum_samples > 0 {
            accumulate_indirect(scene, sensor_index, request, &mut values, cancelled)?;
        }
        let sensor_progress = (sensor_index + 1) as f32 / scene.sensors.len() as f32 * 0.9;
        let bucket = (sensor_progress * 100.0) as u32;
        if bucket > reported_bucket {
            reported_bucket = bucket;
            progress(sensor_progress);
        }
    }
    CoefficientMatrix::new(scene.sensors.len(), basis, values)
}

fn accumulate_indirect(
    scene: &SceneData,
    sensor_index: usize,
    request: &AnalysisRequest,
    coefficients: &mut [[f32; 3]],
    cancelled: &AtomicBool,
) -> Result<()> {
    let sensor = scene.sensors[sensor_index];
    let basis = request.sky.basis;
    let patch_count = basis.row_count();
    let sample_weight = std::f32::consts::PI / request.maximum_samples as f32;

    for sample_index in 0..request.maximum_samples {
        if sample_index % 64 == 0 {
            check_cancelled(cancelled)?;
        }
        let mut origin = sensor.position.add(sensor.normal.scale(RAY_EPSILON));
        let mut direction = sample_direction(
            sensor.normal,
            sensor.sensor_id,
            sample_index,
            0,
            request.scene_seed,
        );
        let mut throughput = [1.0_f32; 3];
        let mut diffuse_bounces = 0;
        let mut transparent_intersections = 0;

        for _ in 0..=(request.maximum_bounces + 64) {
            let Some(hit) = nearest_hit(scene, origin, direction) else {
                if diffuse_bounces > 0 {
                    let patch_index = radiance_patch_index(basis, direction);
                    let destination = &mut coefficients[sensor_index * patch_count + patch_index];
                    for component in 0..3 {
                        destination[component] += throughput[component] * sample_weight;
                    }
                }
                break;
            };
            let material = scene.materials[hit.material_index];
            if material.kind == MaterialKind::ThinGlass as u32 {
                if transparent_intersections >= 64 {
                    break;
                }
                let incidence = direction.dot(hit.normal).abs();
                let mut transmission = [0.0_f32; 3];
                let mut reflection = [0.0_f32; 3];
                for component in 0..3 {
                    transmission[component] = thin_glass_transmittance_from_transmissivity(
                        material.internal_transmissivity_rgb[component],
                        incidence,
                    )?;
                    reflection[component] = thin_glass_reflectance_from_transmissivity(
                        material.internal_transmissivity_rgb[component],
                        incidence,
                    )?;
                }
                let transmission_energy = color_intensity(transmission);
                let reflection_energy = color_intensity(reflection);
                let total_energy = transmission_energy + reflection_energy;
                if total_energy <= 1.0e-8 {
                    break;
                }
                let reflection_probability = reflection_energy / total_energy;
                let branch_sample = low_discrepancy_sample(daylight_core::SampleKey {
                    sensor_id: sensor.sensor_id,
                    sample_index,
                    bounce_depth: diffuse_bounces,
                    dimension: 2 + transparent_intersections,
                    scene_seed: request.scene_seed,
                });
                if branch_sample < reflection_probability {
                    for component in 0..3 {
                        throughput[component] *= reflection[component] / reflection_probability;
                    }
                    origin = origin
                        .add(direction.scale(hit.distance))
                        .add(hit.normal.scale(RAY_EPSILON));
                    direction =
                        direction.subtract(hit.normal.scale(2.0 * direction.dot(hit.normal)));
                } else {
                    let transmission_probability = 1.0 - reflection_probability;
                    if transmission_probability <= 1.0e-8 {
                        break;
                    }
                    for component in 0..3 {
                        throughput[component] *= transmission[component] / transmission_probability;
                    }
                    origin = origin.add(direction.scale(hit.distance + RAY_EPSILON));
                }
                transparent_intersections += 1;
                continue;
            }
            if diffuse_bounces >= request.maximum_bounces {
                break;
            }
            for (component, value) in throughput.iter_mut().enumerate() {
                *value *= material.diffuse_rgb[component];
            }
            if throughput.iter().all(|value| *value <= 1.0e-6) {
                break;
            }
            origin = origin
                .add(direction.scale(hit.distance))
                .add(hit.normal.scale(RAY_EPSILON));
            diffuse_bounces += 1;
            direction = sample_direction(
                hit.normal,
                sensor.sensor_id,
                sample_index,
                diffuse_bounces,
                request.scene_seed,
            );
        }
    }
    Ok(())
}

fn color_intensity(color: [f32; 3]) -> f32 {
    0.265 * color[0] + 0.670 * color[1] + 0.065 * color[2]
}

fn sample_direction(
    normal: Vec3,
    sensor_id: u32,
    sample_index: u32,
    bounce_depth: u32,
    scene_seed: u64,
) -> Vec3 {
    let key = daylight_core::SampleKey {
        sensor_id,
        sample_index,
        bounce_depth,
        dimension: 0,
        scene_seed,
    };
    let first = low_discrepancy_sample(key);
    let second = low_discrepancy_sample(daylight_core::SampleKey {
        dimension: 1,
        ..key
    });
    let local = cosine_hemisphere(first, second);
    orient_to_normal(local, normal)
}

fn orient_to_normal(local: Vec3, normal: Vec3) -> Vec3 {
    let helper = if normal.z.abs() < 0.999 {
        Vec3::new(0.0, 0.0, 1.0)
    } else {
        Vec3::new(1.0, 0.0, 0.0)
    };
    let tangent = helper.cross(normal).normalized_or(Vec3::new(1.0, 0.0, 0.0));
    let bitangent = normal.cross(tangent);
    tangent
        .scale(local.x)
        .add(bitangent.scale(local.y))
        .add(normal.scale(local.z))
        .normalized_or(normal)
}

fn visibility_transmission(scene: &SceneData, origin: Vec3, direction: Vec3) -> Result<[f32; 3]> {
    let mut origin = origin;
    let mut transmission = [1.0_f32; 3];
    for _ in 0..64 {
        let Some(hit) = nearest_hit(scene, origin, direction) else {
            return Ok(transmission);
        };
        let material = scene.materials[hit.material_index];
        if material.kind != MaterialKind::ThinGlass as u32 {
            return Ok([0.0; 3]);
        }
        let incidence = direction.dot(hit.normal).abs();
        for component in 0..3 {
            transmission[component] *= thin_glass_transmittance_from_transmissivity(
                material.internal_transmissivity_rgb[component],
                incidence,
            )?;
        }
        origin = origin.add(direction.scale(hit.distance + RAY_EPSILON));
    }
    Err(DaylightError::Backend {
        detail: "ray exceeded 64 transparent intersections".into(),
    })
}

fn nearest_hit(scene: &SceneData, origin: Vec3, direction: Vec3) -> Option<Hit> {
    let mut nearest = None;
    for instance in &scene.instances {
        let mesh = scene.meshes[instance.mesh_index as usize];
        for triangle_index in
            mesh.first_triangle as usize..(mesh.first_triangle + mesh.triangle_count) as usize
        {
            let triangle = scene.triangles[triangle_index];
            let vertices = triangle
                .map(|index| transform_point(instance.transform, scene.vertices[index as usize]));
            if let Some((distance, normal)) =
                intersect_triangle(origin, direction, vertices[0], vertices[1], vertices[2])
            {
                if nearest
                    .as_ref()
                    .is_none_or(|hit: &Hit| distance < hit.distance)
                {
                    nearest = Some(Hit {
                        distance,
                        normal,
                        material_index: scene.triangle_materials[triangle_index] as usize,
                    });
                }
            }
        }
    }
    nearest
}

fn transform_point(matrix: [f32; 16], point: Vec3) -> Vec3 {
    let x = matrix[0] * point.x + matrix[1] * point.y + matrix[2] * point.z + matrix[3];
    let y = matrix[4] * point.x + matrix[5] * point.y + matrix[6] * point.z + matrix[7];
    let z = matrix[8] * point.x + matrix[9] * point.y + matrix[10] * point.z + matrix[11];
    let w = matrix[12] * point.x + matrix[13] * point.y + matrix[14] * point.z + matrix[15];
    if w != 0.0 && w != 1.0 {
        Vec3::new(x / w, y / w, z / w)
    } else {
        Vec3::new(x, y, z)
    }
}

fn intersect_triangle(
    origin: Vec3,
    direction: Vec3,
    first: Vec3,
    second: Vec3,
    third: Vec3,
) -> Option<(f32, Vec3)> {
    let edge_one = second.subtract(first);
    let edge_two = third.subtract(first);
    let perpendicular = direction.cross(edge_two);
    let determinant = edge_one.dot(perpendicular);
    if determinant.abs() < 1.0e-8 {
        return None;
    }
    let inverse = determinant.recip();
    let distance_from_first = origin.subtract(first);
    let u = distance_from_first.dot(perpendicular) * inverse;
    if !(0.0..=1.0).contains(&u) {
        return None;
    }
    let cross = distance_from_first.cross(edge_one);
    let v = direction.dot(cross) * inverse;
    if v < 0.0 || u + v > 1.0 {
        return None;
    }
    let distance = edge_two.dot(cross) * inverse;
    if distance <= RAY_MIN_DISTANCE {
        return None;
    }
    let geometric_normal = edge_one
        .cross(edge_two)
        .normalized_or(Vec3::new(0.0, 0.0, 1.0));
    let normal = if geometric_normal.dot(direction) > 0.0 {
        geometric_normal.scale(-1.0)
    } else {
        geometric_normal
    };
    Some((distance, normal))
}

pub(crate) fn compute_daylight_factor(
    coefficients: &CoefficientMatrix,
    scene: &SceneData,
) -> Result<daylight_core::DaylightFactorMetrics> {
    let directions = patch_directions(coefficients.basis);
    let solid_angles = patch_solid_angles(coefficients.basis);
    let mut sky_luminance = vec![0.0_f32; coefficients.basis.row_count()];
    for patch_index in 1..coefficients.basis.row_count() {
        sky_luminance[patch_index] = (1.0 + 2.0 * directions[patch_index].z.max(0.0)) / 3.0;
    }
    let exterior_horizontal = (1..coefficients.basis.row_count())
        .map(|patch| sky_luminance[patch] * directions[patch].z.max(0.0) * solid_angles[patch])
        .sum::<f32>();
    let interior = (0..scene.sensors.len())
        .map(|sensor| {
            (0..coefficients.basis.row_count())
                .map(|patch| {
                    let coefficient = coefficients.get(sensor, patch);
                    let photopic =
                        coefficient[0] * 0.265 + coefficient[1] * 0.67 + coefficient[2] * 0.065;
                    photopic * sky_luminance[patch]
                })
                .sum::<f32>()
        })
        .collect::<Vec<_>>();
    evaluate_daylight_factor(&interior, exterior_horizontal)
}

fn check_cancelled(cancelled: &AtomicBool) -> Result<()> {
    if cancelled.load(Ordering::Acquire) {
        Err(DaylightError::Cancelled)
    } else {
        Ok(())
    }
}
