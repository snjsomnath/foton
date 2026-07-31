use std::{
    sync::{
        Arc,
        atomic::{AtomicBool, Ordering},
    },
    time::Duration,
};

use daylight_core::{
    AnalysisJob, AnalysisQuality, AnalysisRequest, AnalysisResult, Backend, BackendCapabilities,
    CoefficientMatrix, DaylightError, InstanceUpdate, Material, SampleKey, Sensor, ShoeboxOptions,
    SkyBasis, SkyMatrix, Vec3, evaluate_daylight_factor, low_discrepancy_sample,
    mf2_to_tregenza_map, patch_directions, radiance_glass_transmissivity, radiance_patch_index,
    reduce_annual_metrics, scene_fingerprint, shoebox_scene, sobol_uint, thin_glass_transmittance,
};

fn assert_close(actual: f32, expected: f32, tolerance: f32) {
    assert!(
        (actual - expected).abs() <= tolerance,
        "expected {expected}, got {actual}"
    );
}

#[test]
fn mf2_mapping_has_four_children_except_zenith() {
    let mapping = mf2_to_tregenza_map();
    assert_eq!(mapping.len(), 578);
    assert_eq!(mapping[0], 0);
    assert_eq!(mapping[577], 145);
    for parent in 1..145 {
        assert_eq!(
            mapping
                .iter()
                .filter(|candidate| **candidate == parent)
                .count(),
            4
        );
    }
    assert_eq!(
        mapping
            .iter()
            .filter(|candidate| **candidate == 145)
            .count(),
        1
    );
}

#[test]
fn coefficient_aggregation_preserves_energy() {
    let values = (0..578).map(|index| [index as f32, 2.0, 3.0]).collect();
    let matrix = CoefficientMatrix::new(1, SkyBasis::ReinhartMf2, values).unwrap();
    let aggregate = matrix.aggregate_tregenza().unwrap();
    for component in 0..3 {
        let source_sum: f32 = matrix.values.iter().map(|value| value[component]).sum();
        let aggregate_sum: f32 = aggregate.values.iter().map(|value| value[component]).sum();
        assert_close(source_sum, aggregate_sum, 0.01);
    }
}

#[test]
fn patch_directions_match_basis_and_are_normalized() {
    for basis in [SkyBasis::Tregenza, SkyBasis::ReinhartMf2] {
        let directions = patch_directions(basis);
        assert_eq!(directions.len(), basis.row_count());
        for direction in directions {
            assert_close(direction.length(), 1.0, 1e-5);
        }
    }
}

#[test]
fn tregenza_patch_order_advances_from_north_to_east() {
    let directions = patch_directions(SkyBasis::Tregenza);
    assert!(directions[1].x.abs() < 1.0e-6);
    assert!(directions[1].y > 0.0);
    assert!(directions[2].x > 0.0);
    assert!(directions[2].y > 0.0);
}

#[test]
fn radiance_bins_contain_their_canonical_patch_centers() {
    for basis in [SkyBasis::Tregenza, SkyBasis::ReinhartMf2] {
        for (patch_index, direction) in patch_directions(basis).into_iter().enumerate() {
            assert_eq!(
                radiance_patch_index(basis, direction),
                patch_index,
                "basis={basis:?}, patch={patch_index}"
            );
        }
        assert_eq!(radiance_patch_index(basis, Vec3::new(0.0, 0.0, -1.0)), 0);
        assert_eq!(
            radiance_patch_index(basis, Vec3::new(0.0, 0.0, 1.0)),
            basis.row_count() - 1
        );
    }
}

#[test]
fn radiance_glass_conversion_matches_known_sixty_percent_case() {
    let transmissivity = radiance_glass_transmissivity(0.6).unwrap();
    assert_close(transmissivity, 0.654, 0.002);
    let normal_transmittance = thin_glass_transmittance(0.6, 1.0).unwrap();
    assert_close(normal_transmittance, 0.6, 0.001);
    assert!(thin_glass_transmittance(0.6, 0.2).unwrap() < normal_transmittance);
}

#[test]
fn samples_depend_on_stable_key_not_dispatch_order() {
    let key = SampleKey {
        scene_seed: 42,
        sensor_id: 91,
        sample_index: 7,
        bounce_depth: 2,
        dimension: 4,
    };
    assert_eq!(low_discrepancy_sample(key), low_discrepancy_sample(key));
    assert_ne!(
        low_discrepancy_sample(key),
        low_discrepancy_sample(SampleKey {
            sensor_id: 92,
            ..key
        })
    );
}

#[test]
fn first_sobol_dimension_follows_gray_code_order() {
    assert_eq!(sobol_uint(0, 0), 0x0000_0000);
    assert_eq!(sobol_uint(1, 0), 0x8000_0000);
    assert_eq!(sobol_uint(2, 0), 0xc000_0000);
    assert_eq!(sobol_uint(3, 0), 0x4000_0000);
}

#[test]
fn annual_reduction_uses_schedule_and_area_weights() {
    let coefficients =
        CoefficientMatrix::new(2, SkyBasis::Tregenza, vec![[1.0, 1.0, 1.0]; 2 * 146]).unwrap();
    let sky = SkyMatrix::new(SkyBasis::Tregenza, 2, vec![[1.0, 1.0, 1.0]; 146 * 2]).unwrap();
    let sensors = vec![
        Sensor {
            normal: Vec3::new(0.0, 0.0, 1.0),
            sensor_id: 1,
            room_id: 9,
            area_weight: 1.0,
            ..Sensor::default()
        },
        Sensor {
            normal: Vec3::new(0.0, 0.0, 1.0),
            sensor_id: 2,
            room_id: 9,
            area_weight: 3.0,
            ..Sensor::default()
        },
    ];
    let result =
        reduce_annual_metrics(&coefficients, &sky, &[1.0, 0.0], &sensors, 300.0, 0.5).unwrap();
    assert_eq!(result.occupied_weight, 1.0);
    assert_eq!(result.rooms[0].static_sda_300_50, 100.0);
}

#[test]
fn daylight_factor_is_ratio_of_simultaneous_illuminance() {
    let result = evaluate_daylight_factor(&[100.0, 200.0], 10_000.0).unwrap();
    assert_eq!(result.per_sensor_percent, vec![1.0, 2.0]);
    assert_eq!(result.mean_percent, 1.5);
}

#[test]
fn material_validation_distinguishes_glass_and_diffuse_inputs() {
    Material::lambertian([0.7, 0.7, 0.7]).validate().unwrap();
    Material::thin_glass([0.6, 0.6, 0.6]).validate().unwrap();
}

#[test]
fn generated_portfolio_reuses_one_mesh_and_has_stable_ids() {
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1_000,
        sensors_per_room: 25,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    assert_eq!(scene.meshes.len(), 1);
    assert_eq!(scene.instances.len(), 1_000);
    assert_eq!(scene.sensors.len(), 25_000);
    assert_eq!(scene.instances[999].room_id, 999);
    assert_eq!(scene.sensors[24_999].sensor_id, 24_999);
}

#[test]
fn scene_fingerprint_changes_with_geometry_revision() {
    let scene = shoebox_scene(ShoeboxOptions::default()).unwrap();
    let original = scene_fingerprint(&scene);
    let mut changed = scene.clone();
    changed.instances[0].transform[3] = 1.0;
    assert_ne!(original, scene_fingerprint(&changed));
    assert_eq!(original, scene_fingerprint(&scene));
}

#[test]
fn scene_handle_updates_are_revisioned_and_transactional() {
    let handle =
        daylight_core::SceneHandle::new(shoebox_scene(ShoeboxOptions::default()).unwrap()).unwrap();
    let original = handle.snapshot().unwrap();
    let mut moved = original.instances[0].transform;
    moved[3] = 2.0;
    let revision = handle
        .update_instances(&[InstanceUpdate {
            instance_index: 0,
            transform: moved,
            room_id: Some(17),
        }])
        .unwrap();
    assert_eq!(revision, 2);
    assert_eq!(handle.revision(), 2);
    assert_eq!(handle.snapshot().unwrap().instances[0].transform, moved);
    assert_eq!(handle.snapshot().unwrap().instances[0].room_id, 17);

    let error = handle
        .update_instances(&[
            InstanceUpdate {
                instance_index: 0,
                transform: original.instances[0].transform,
                room_id: Some(23),
            },
            InstanceUpdate {
                instance_index: usize::MAX,
                transform: original.instances[0].transform,
                room_id: None,
            },
        ])
        .unwrap_err();
    assert!(matches!(error, DaylightError::InvalidValue { .. }));
    assert_eq!(handle.revision(), 2);
    assert_eq!(handle.snapshot().unwrap().instances[0].room_id, 17);
}

struct CancellableBackend {
    active: Arc<AtomicBool>,
}

impl Backend for CancellableBackend {
    fn capabilities(&self) -> BackendCapabilities {
        BackendCapabilities {
            name: "cancellation-test".into(),
            hardware_acceleration: false,
            supports_ray_tracing: false,
            supports_async_jobs: true,
        }
    }

    fn analyze(
        &self,
        _scene: &daylight_core::SceneData,
        _request: &AnalysisRequest,
        _solver_revision: u64,
        cancelled: &AtomicBool,
        _progress: &(dyn Fn(f32) + Send + Sync),
    ) -> daylight_core::Result<AnalysisResult> {
        self.active.store(true, Ordering::Release);
        while !cancelled.load(Ordering::Acquire) {
            std::thread::sleep(Duration::from_millis(1));
        }
        self.active.store(false, Ordering::Release);
        Err(DaylightError::Cancelled)
    }
}

#[test]
fn dropping_job_joins_cancelled_worker() {
    let active = Arc::new(AtomicBool::new(false));
    let backend: Arc<dyn Backend> = Arc::new(CancellableBackend {
        active: Arc::clone(&active),
    });
    let scene = backend
        .commit_scene(shoebox_scene(ShoeboxOptions::default()).unwrap())
        .unwrap();
    let request = AnalysisRequest {
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
        scene_seed: 0,
        export_coefficients: false,
    };
    let job = AnalysisJob::spawn(backend, scene, request);
    for _ in 0..100 {
        if active.load(Ordering::Acquire) {
            break;
        }
        std::thread::sleep(Duration::from_millis(1));
    }
    drop(job);
    assert!(!active.load(Ordering::Acquire));
}
