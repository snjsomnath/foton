use std::{fs, path::PathBuf, sync::atomic::AtomicBool, time::Instant};

use clap::{Parser, Subcommand};
use daylight_core::{
    AnalysisQuality, AnalysisRequest, Backend, ShoeboxOptions, SkyBasis, SkyMatrix, shoebox_scene,
};
#[cfg(target_os = "macos")]
use daylight_metal::MetalBackend;
use daylight_metal::ReferenceBackend;
use daylight_vulkan::VulkanBackend;
#[cfg(target_os = "macos")]
use daylight_vulkan::is_apple_gpu;

#[derive(Parser)]
#[command(version, about = "GPU daylight engine diagnostics and fixtures")]
struct Arguments {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    Hardware,
    Fixture {
        #[arg(long)]
        output: PathBuf,
        #[arg(long, default_value_t = 1)]
        rooms: usize,
        #[arg(long, default_value_t = 25)]
        sensors_per_room: usize,
        #[arg(long)]
        glazing_transmittance: Option<f32>,
    },
    Benchmark {
        #[arg(long, default_value_t = 1)]
        rooms: usize,
        #[arg(long, default_value_t = 25)]
        sensors_per_room: usize,
        #[arg(long, default_value_t = 0)]
        samples: u32,
        #[arg(long, default_value_t = 0)]
        bounces: u32,
    },
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    match Arguments::parse().command {
        Command::Hardware => hardware()?,
        Command::Fixture {
            output,
            rooms,
            sensors_per_room,
            glazing_transmittance,
        } => {
            let scene = shoebox_scene(ShoeboxOptions {
                room_count: rooms,
                sensors_per_room,
                glazing_transmittance: glazing_transmittance.map(|value| [value; 3]),
            })?;
            if let Some(parent) = output.parent() {
                fs::create_dir_all(parent)?;
            }
            fs::write(output, serde_json::to_vec_pretty(&scene)?)?;
        }
        Command::Benchmark {
            rooms,
            sensors_per_room,
            samples,
            bounces,
        } => benchmark(rooms, sensors_per_room, samples, bounces)?,
    }
    Ok(())
}

fn hardware() -> Result<(), Box<dyn std::error::Error>> {
    let capabilities = auto_backend().capabilities();
    println!("{}", serde_json::to_string_pretty(&capabilities)?);
    Ok(())
}

fn benchmark(
    rooms: usize,
    sensors_per_room: usize,
    samples: u32,
    bounces: u32,
) -> Result<(), Box<dyn std::error::Error>> {
    let scene = shoebox_scene(ShoeboxOptions {
        room_count: rooms,
        sensors_per_room,
        glazing_transmittance: Some([0.6; 3]),
    })?;
    let sky = SkyMatrix::new(
        SkyBasis::Tregenza,
        1,
        vec![[1.0; 3]; SkyBasis::Tregenza.row_count()],
    )?;
    let request = AnalysisRequest {
        sky,
        occupancy_weights: vec![1.0],
        quality: AnalysisQuality::Preview,
        threshold_lux: 300.0,
        time_fraction: 0.5,
        maximum_samples: samples,
        maximum_bounces: bounces,
        scene_seed: 0,
        export_coefficients: false,
    };
    let backend = auto_backend();
    let started = Instant::now();
    let result = backend.analyze(&scene, &request, 1, &AtomicBool::new(false), &|_| {})?;
    let output = serde_json::json!({
        "rooms": rooms,
        "sensors": scene.sensors.len(),
        "triangles_per_room": scene.triangles.len(),
        "samples": samples,
        "bounces": bounces,
        "wall_clock_ms": started.elapsed().as_secs_f64() * 1000.0,
        "timings": result.timings,
        "estimated_scene_bytes": estimate_scene_bytes(&scene),
    });
    println!("{}", serde_json::to_string_pretty(&output)?);
    Ok(())
}

fn auto_backend() -> Box<dyn Backend> {
    #[cfg(target_os = "macos")]
    if let Ok(backend) = MetalBackend::new() {
        if is_apple_gpu(&backend.device_name()) {
            return Box::new(backend);
        }
    }
    if let Ok(backend) = VulkanBackend::new() {
        return Box::new(backend);
    }
    Box::new(ReferenceBackend)
}

fn estimate_scene_bytes(scene: &daylight_core::SceneData) -> usize {
    scene.vertices.len() * size_of::<daylight_core::Vec3>()
        + scene.triangles.len() * size_of::<[u32; 3]>()
        + scene.triangle_materials.len() * size_of::<u32>()
        + scene.meshes.len() * size_of::<daylight_core::MeshRange>()
        + scene.instances.len() * size_of::<daylight_core::Instance>()
        + scene.materials.len() * size_of::<daylight_core::Material>()
        + scene.sensors.len() * size_of::<daylight_core::Sensor>()
}
