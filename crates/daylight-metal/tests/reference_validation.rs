use std::sync::atomic::AtomicBool;

#[cfg(target_os = "macos")]
use daylight_core::InstanceUpdate;
use daylight_core::{
    AnalysisQuality, AnalysisRequest, Backend, ShoeboxOptions, SkyBasis, SkyMatrix,
    patch_directions, patch_solid_angles, shoebox_scene,
};
#[cfg(target_os = "macos")]
use daylight_metal::MetalBackend;
use daylight_metal::ReferenceBackend;

#[cfg(target_os = "macos")]
fn enabled_metal() -> Option<MetalBackend> {
    match MetalBackend::new() {
        Ok(backend) => Some(backend),
        Err(error) => {
            assert!(
                std::env::var_os("DAYLIGHT_ENGINE_METAL_TEST").is_none(),
                "Metal validation was requested but the GPU is unavailable: {error}"
            );
            None
        }
    }
}

fn request() -> AnalysisRequest {
    let timestep_count = 4;
    let mut values = vec![[0.0; 3]; SkyBasis::Tregenza.row_count() * timestep_count];
    for patch in 0..SkyBasis::Tregenza.row_count() {
        for timestep in 0..timestep_count {
            values[patch * timestep_count + timestep] = [1.0 + timestep as f32, 0.5, 0.25];
        }
    }
    AnalysisRequest {
        sky: SkyMatrix::new(SkyBasis::Tregenza, timestep_count, values).unwrap(),
        occupancy_weights: vec![1.0, 0.0, 0.5, 1.0],
        quality: AnalysisQuality::Preview,
        threshold_lux: 300.0,
        udi_lower_lux: 100.0,
        udi_upper_lux: 3000.0,
        time_fraction: 0.5,
        direct_samples: 1,
        maximum_samples: 16,
        maximum_bounces: 1,
        scene_seed: 42,
        export_coefficients: true,
        export_illuminance: false,
        coefficient_override: None,
    }
}

fn direct_request() -> AnalysisRequest {
    AnalysisRequest {
        sky: SkyMatrix::new(
            SkyBasis::Tregenza,
            1,
            vec![[1.0; 3]; SkyBasis::Tregenza.row_count()],
        )
        .unwrap(),
        occupancy_weights: vec![1.0],
        quality: AnalysisQuality::Preview,
        threshold_lux: 300.0,
        udi_lower_lux: 100.0,
        udi_upper_lux: 3000.0,
        time_fraction: 0.5,
        direct_samples: 1,
        maximum_samples: 0,
        maximum_bounces: 0,
        scene_seed: 42,
        export_coefficients: true,
        export_illuminance: false,
        coefficient_override: None,
    }
}

fn coefficient_energy(result: &daylight_core::AnalysisResult) -> f32 {
    result
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum()
}

#[test]
fn transport_microfixtures_cover_patch_edges_glass_bounce_sealing_and_overlap() {
    let backend = ReferenceBackend;
    let mut direct = direct_request();
    direct.direct_samples = 64;

    let open = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 1,
        glazing_transmittance: None,
    })
    .unwrap();
    let glass = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 1,
        glazing_transmittance: Some([0.64; 3]),
    })
    .unwrap();
    let sealed = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 1,
        glazing_transmittance: Some([0.0; 3]),
    })
    .unwrap();
    let open_result = backend
        .analyze(&open, &direct, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let glass_result = backend
        .analyze(&glass, &direct, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let sealed_result = backend
        .analyze(&sealed, &direct, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let open_energy = coefficient_energy(&open_result);
    let glass_energy = coefficient_energy(&glass_result);
    assert!(open_energy > glass_energy && glass_energy > 0.0);
    assert_eq!(coefficient_energy(&sealed_result), 0.0);

    let directions = patch_directions(SkyBasis::Tregenza);
    let solid_angles = patch_solid_angles(SkyBasis::Tregenza);
    let coefficients = open_result.coefficients.as_ref().unwrap();
    let has_partially_exposed_patch = (1..SkyBasis::Tregenza.row_count()).any(|patch| {
        let cosine = directions[patch].z.max(0.0);
        let maximum = cosine * solid_angles[patch];
        if maximum <= 1.0e-8 {
            return false;
        }
        let fraction = coefficients.get(0, patch)[0] / maximum;
        fraction > 0.01 && fraction < 0.99
    });
    assert!(
        has_partially_exposed_patch,
        "64-sample integration must resolve a partially exposed sky patch"
    );

    let mut one_bounce = direct.clone();
    one_bounce.maximum_samples = 512;
    one_bounce.maximum_bounces = 1;
    let bounced = backend
        .analyze(&glass, &one_bounce, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert!(coefficient_energy(&bounced) > glass_energy);

    let mut overlapping = shoebox_scene(ShoeboxOptions {
        room_count: 2,
        sensors_per_room: 1,
        glazing_transmittance: Some([0.64; 3]),
    })
    .unwrap();
    overlapping.instances[1].transform = overlapping.instances[0].transform;
    overlapping.sensors[1].position = overlapping.sensors[0].position;
    overlapping.validate().unwrap();
    let overlap_result = backend
        .analyze(&overlapping, &direct, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let overlap_coefficients = overlap_result.coefficients.as_ref().unwrap();
    assert_eq!(
        overlap_coefficients.values[0], overlap_coefficients.values[1],
        "overlapping-room geometry must be traced consistently, not suppressed"
    );
}

#[test]
fn repeated_runs_preserve_deterministic_coefficients() {
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 2,
        sensors_per_room: 2,
        glazing_transmittance: Some([0.6, 0.55, 0.5]),
    })
    .unwrap();
    let backend = ReferenceBackend;
    let request = request();
    let first = backend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let second = backend
        .analyze(&scene, &request, 2, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert_eq!(
        first.coefficients.as_ref().unwrap().values,
        second.coefficients.as_ref().unwrap().values
    );
}

#[cfg(target_os = "macos")]
#[test]
fn metal_diffuse_glass_transport_matches_cpu_reference_when_available() {
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let request = request();
    let cpu = ReferenceBackend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let gpu = metal
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    for (reference, candidate) in cpu.annual.sensors.iter().zip(&gpu.annual.sensors) {
        assert_eq!(reference.sensor_id, candidate.sensor_id);
        assert_eq!(reference.room_id, candidate.room_id);
        assert_eq!(reference.passes_sda, candidate.passes_sda);
        for (left, right) in [
            (reference.daylight_autonomy, candidate.daylight_autonomy),
            (
                reference.continuous_daylight_autonomy,
                candidate.continuous_daylight_autonomy,
            ),
            (
                reference.useful_daylight_illuminance_lower,
                candidate.useful_daylight_illuminance_lower,
            ),
            (
                reference.useful_daylight_illuminance,
                candidate.useful_daylight_illuminance,
            ),
            (
                reference.useful_daylight_illuminance_upper,
                candidate.useful_daylight_illuminance_upper,
            ),
        ] {
            assert!((left - right).abs() < 1.0e-5);
        }
    }
    assert_eq!(cpu.annual.rooms, gpu.annual.rooms);
    assert_eq!(gpu.metadata.transport_backend, "metal");
    assert!(!gpu.metadata.used_reference_fallback);
    assert_eq!(gpu.sample_count, request.maximum_samples);
    assert_eq!(gpu.bounce_count, request.maximum_bounces);
    let cpu_coefficients = cpu.coefficients.as_ref().unwrap();
    let gpu_coefficients = gpu.coefficients.as_ref().unwrap();
    let reference_energy: f32 = cpu_coefficients.values.iter().flatten().sum();
    let candidate_energy: f32 = gpu_coefficients.values.iter().flatten().sum();
    let relative_energy_error =
        (candidate_energy - reference_energy).abs() / reference_energy.max(1.0e-6);
    assert!(
        relative_energy_error < 0.02,
        "relative coefficient-energy error {relative_energy_error}; reference={reference_energy}; candidate={candidate_energy}"
    );
}

#[cfg(target_os = "macos")]
#[test]
fn metal_direct_visibility_matches_cpu_reference_when_available() {
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: None,
    })
    .unwrap();
    let request = direct_request();
    let cpu = ReferenceBackend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let gpu = metal
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let cpu_coefficients = cpu.coefficients.as_ref().unwrap();
    let gpu_coefficients = gpu.coefficients.as_ref().unwrap();
    assert_eq!(gpu.metadata.transport_backend, "metal");
    assert!(!gpu.metadata.used_reference_fallback);
    let mismatches = cpu_coefficients
        .values
        .iter()
        .flatten()
        .zip(gpu_coefficients.values.iter().flatten())
        .enumerate()
        .filter(|(_, (reference, candidate))| (*reference - *candidate).abs() >= 1.0e-5)
        .map(|(index, (reference, candidate))| (index, *reference, *candidate))
        .collect::<Vec<_>>();
    let reference_energy: f32 = cpu_coefficients.values.iter().flatten().sum();
    let candidate_energy: f32 = gpu_coefficients.values.iter().flatten().sum();
    let relative_energy_error =
        (candidate_energy - reference_energy).abs() / reference_energy.max(1.0e-6);
    let mismatch_preview = mismatches.iter().take(18).collect::<Vec<_>>();
    assert!(
        mismatches.len() * 100 < cpu_coefficients.values.len() * 3 * 2,
        "too many edge mismatches: {}; reference energy={reference_energy}; candidate energy={candidate_energy}; first={mismatch_preview:?}",
        mismatches.len(),
    );
    assert!(
        relative_energy_error < 0.01,
        "relative coefficient-energy error {relative_energy_error}"
    );
    assert_eq!(
        cpu_coefficients.get(0, 145),
        gpu_coefficients.get(0, 145),
        "non-boundary zenith blocker must match exactly"
    );
    assert!(gpu.timings.acceleration_structure_ms > 0.0);
    assert!(gpu.timings.tracing_ms > 0.0);
}

#[cfg(target_os = "macos")]
#[test]
fn metal_integrated_direct_coefficients_match_cpu_reference_when_available() {
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let mut request = direct_request();
    request.direct_samples = 64;
    let cpu = ReferenceBackend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let gpu = metal
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert_eq!(gpu.metadata.direct_sample_count, 64);
    let reference_energy: f32 = cpu
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    let candidate_energy: f32 = gpu
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    assert!((candidate_energy - reference_energy).abs() / reference_energy < 0.01);
}

#[cfg(target_os = "macos")]
#[test]
fn committed_metal_scene_reuses_resident_acceleration_structures() {
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: None,
    })
    .unwrap();
    let original_transform = scene.instances[0].transform;
    let handle = metal.commit_scene(scene).unwrap();
    let request = direct_request();

    let first = metal
        .analyze_committed(&handle, &request, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let second = metal
        .analyze_committed(&handle, &request, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert_eq!(first.solver_revision, 1);
    assert_eq!(second.solver_revision, 1);
    assert_eq!(first.timings.acceleration_structure_ms, 0.0);
    assert_eq!(second.timings.acceleration_structure_ms, 0.0);
    assert_eq!(first.coefficients, second.coefficients);

    let revision = metal
        .update_instances(
            &handle,
            &[InstanceUpdate {
                instance_index: 0,
                transform: original_transform,
                room_id: Some(7),
            }],
        )
        .unwrap();
    let updated = metal
        .analyze_committed(&handle, &request, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert_eq!(revision, 2);
    assert_eq!(updated.solver_revision, 2);
    assert_eq!(updated.timings.acceleration_structure_ms, 0.0);
    assert_eq!(first.coefficients, updated.coefficients);
}

#[cfg(target_os = "macos")]
#[test]
fn metal_traces_every_mesh_of_a_many_room_scene() {
    // Each Honeybee room becomes its own mesh and bottom-level acceleration
    // structure. With a few hundred of them, structures the encoder never
    // declared resident were skipped, so rays crossed walls and the result
    // changed between runs. A scene with one mesh per room must trace exactly
    // like the same rooms instancing one shared mesh.
    let Some(metal) = enabled_metal() else {
        return;
    };
    let shared = shoebox_scene(ShoeboxOptions {
        room_count: 256,
        sensors_per_room: 36,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let mut separate = shared.clone();
    let mesh = shared.meshes[0];
    let first = mesh.first_triangle as usize;
    let last = first + mesh.triangle_count as usize;
    separate.meshes.clear();
    separate.triangles.clear();
    separate.triangle_materials.clear();
    for (index, instance) in separate.instances.iter_mut().enumerate() {
        separate.meshes.push(daylight_core::MeshRange {
            first_triangle: separate.triangles.len() as u32,
            triangle_count: mesh.triangle_count,
        });
        separate
            .triangles
            .extend_from_slice(&shared.triangles[first..last]);
        separate
            .triangle_materials
            .extend_from_slice(&shared.triangle_materials[first..last]);
        instance.mesh_index = index as u32;
    }
    let mut request = request();
    request.maximum_samples = 16384;
    request.maximum_bounces = 4;
    let expected = metal
        .analyze(&shared, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let handle = metal.commit_scene(separate).unwrap();
    for _ in 0..3 {
        let traced = metal
            .analyze_committed(&handle, &request, &AtomicBool::new(false), &|_| {})
            .unwrap();
        assert_eq!(traced.coefficients, expected.coefficients);
    }
}

#[cfg(target_os = "macos")]
#[test]
fn committed_metal_scene_reduces_cached_coefficients_without_retracing() {
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let handle = metal.commit_scene(scene).unwrap();
    let first_request = request();
    let first = metal
        .analyze_committed(&handle, &first_request, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let mut cached_request = first_request.clone();
    cached_request.coefficient_override = first.coefficients.clone();
    cached_request.export_coefficients = false;
    cached_request.threshold_lux = 100.0;
    let cached = metal
        .analyze_committed(&handle, &cached_request, &AtomicBool::new(false), &|_| {})
        .unwrap();
    assert_eq!(cached.timings.tracing_ms, 0.0);
    assert!(cached.coefficients.is_none());
    assert_ne!(first.annual.sensors, cached.annual.sensors);
}

#[cfg(target_os = "macos")]
#[test]
fn metal_sample_tiling_is_exact_when_available() {
    // 2,048 sensors at 4,096 samples exceed the 2^22 paths-per-dispatch bound and
    // trace as two sample tiles. Each 1,024-sensor half fits one dispatch. The
    // fixed-point accumulators are order-independent, so the tiled result must
    // equal the untiled halves exactly.
    let Some(metal) = enabled_metal() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 2048,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let mut request = request();
    request.maximum_samples = 4096;
    request.maximum_bounces = 2;
    let tiled = metal
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let tiled = tiled.coefficients.as_ref().unwrap();
    for (half, range) in [(0usize, 0..1024usize), (1, 1024..2048)] {
        let mut subset = scene.clone();
        subset.sensors = scene.sensors[range.clone()].to_vec();
        let untiled = metal
            .analyze(&subset, &request, 1, &AtomicBool::new(false), &|_| {})
            .unwrap();
        let untiled = untiled.coefficients.as_ref().unwrap();
        for (local, global) in range.enumerate() {
            for patch in 0..SkyBasis::Tregenza.row_count() {
                assert_eq!(
                    tiled.get(global, patch),
                    untiled.get(local, patch),
                    "half {half}, sensor {global}, patch {patch}"
                );
            }
        }
    }
}

#[test]
fn sealed_room_stays_dark_under_deep_diffuse_sampling() {
    // One escaping path in ~5 million is enough to fail the sealed-room gate.
    // Before bounce origins stepped back along the incoming ray, hits within
    // float error of a concave corner landed outside the adjacent wall.
    let sealed = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 36,
        glazing_transmittance: Some([0.0; 3]),
    })
    .unwrap();
    let mut request = request();
    request.direct_samples = 256;
    request.maximum_samples = 16384;
    request.maximum_bounces = 8;
    for seed in 0..4u64 {
        request.scene_seed = seed;
        let cpu = ReferenceBackend
            .analyze(&sealed, &request, 1, &AtomicBool::new(false), &|_| {})
            .unwrap();
        assert_eq!(
            coefficient_energy(&cpu),
            0.0,
            "reference leaked at seed {seed}"
        );
        #[cfg(target_os = "macos")]
        if let Some(metal) = enabled_metal() {
            let gpu = metal
                .analyze(&sealed, &request, 1, &AtomicBool::new(false), &|_| {})
                .unwrap();
            assert_eq!(coefficient_energy(&gpu), 0.0, "metal leaked at seed {seed}");
        }
    }
}
