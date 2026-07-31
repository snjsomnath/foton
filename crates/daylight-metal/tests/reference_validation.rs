use std::sync::atomic::AtomicBool;

#[cfg(target_os = "macos")]
use daylight_core::InstanceUpdate;
use daylight_core::{
    AnalysisQuality, AnalysisRequest, Backend, ShoeboxOptions, SkyBasis, SkyMatrix, shoebox_scene,
};
#[cfg(target_os = "macos")]
use daylight_metal::MetalBackend;
use daylight_metal::ReferenceBackend;

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
        time_fraction: 0.5,
        maximum_samples: 16,
        maximum_bounces: 1,
        scene_seed: 42,
        export_coefficients: true,
    }
}

#[cfg(target_os = "macos")]
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
        time_fraction: 0.5,
        maximum_samples: 0,
        maximum_bounces: 0,
        scene_seed: 42,
        export_coefficients: true,
    }
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
    let Ok(metal) = MetalBackend::new() else {
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
    assert_eq!(cpu.annual.sensors, gpu.annual.sensors);
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
    let Ok(metal) = MetalBackend::new() else {
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
fn committed_metal_scene_reuses_resident_acceleration_structures() {
    let Ok(metal) = MetalBackend::new() else {
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
