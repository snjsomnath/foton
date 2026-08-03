use std::sync::atomic::AtomicBool;

use daylight_core::{
    AnalysisQuality, AnalysisRequest, Backend, ShoeboxOptions, SkyBasis, SkyMatrix, shoebox_scene,
};
use daylight_metal::ReferenceBackend;
use daylight_vulkan::VulkanBackend;

fn request(samples: u32, bounces: u32) -> AnalysisRequest {
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
        maximum_samples: samples,
        maximum_bounces: bounces,
        scene_seed: 7,
        export_coefficients: true,
        export_illuminance: false,
        coefficient_override: None,
    }
}

fn enabled_backend() -> Option<VulkanBackend> {
    std::env::var_os("DAYLIGHT_ENGINE_VULKAN_TEST")?;
    VulkanBackend::new().ok()
}

#[test]
fn direct_visibility_matches_reference_when_enabled() {
    let Some(vulkan) = enabled_backend() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: None,
    })
    .unwrap();
    let request = request(0, 0);
    let reference = ReferenceBackend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let candidate = vulkan
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let reference_energy: f32 = reference
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    let candidate_energy: f32 = candidate
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    assert_eq!(candidate.metadata.transport_backend, "vulkan");
    assert!(!candidate.metadata.used_reference_fallback);
    assert!((candidate_energy - reference_energy).abs() / reference_energy < 0.01);
}

#[test]
fn diffuse_transport_matches_reference_when_enabled() {
    let Some(vulkan) = enabled_backend() else {
        return;
    };
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: 1,
        sensors_per_room: 4,
        glazing_transmittance: Some([0.6; 3]),
    })
    .unwrap();
    let request = request(64, 1);
    let reference = ReferenceBackend
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let candidate = vulkan
        .analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})
        .unwrap();
    let reference_energy: f32 = reference
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    let candidate_energy: f32 = candidate
        .coefficients
        .as_ref()
        .unwrap()
        .values
        .iter()
        .flatten()
        .sum();
    assert!((candidate_energy - reference_energy).abs() / reference_energy < 0.02);
}
