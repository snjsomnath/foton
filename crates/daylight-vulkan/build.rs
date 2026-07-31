use std::{env, fs, path::PathBuf};

fn main() {
    let shader_dir = PathBuf::from("shaders");
    let output_dir = PathBuf::from(env::var_os("OUT_DIR").expect("OUT_DIR is set"));
    let common =
        fs::read_to_string(shader_dir.join("common.glsl")).expect("read Vulkan shader contracts");
    let compiler = shaderc::Compiler::new().expect("create shader compiler");
    let mut options = shaderc::CompileOptions::new().expect("create shader options");
    options.set_target_env(
        shaderc::TargetEnv::Vulkan,
        shaderc::EnvVersion::Vulkan1_3 as u32,
    );
    options.set_target_spirv(shaderc::SpirvVersion::V1_4);
    options.set_optimization_level(shaderc::OptimizationLevel::Performance);
    for name in [
        "direct_visibility",
        "diffuse_transport",
        "finalize_indirect",
        "annual_reduce",
    ] {
        let path = shader_dir.join(format!("{name}.comp"));
        let source = fs::read_to_string(&path).expect("read Vulkan shader");
        let source = source.replace("#include \"common.glsl\"", &common);
        let artifact = compiler
            .compile_into_spirv(
                &source,
                shaderc::ShaderKind::Compute,
                path.to_str().expect("UTF-8 shader path"),
                "main",
                Some(&options),
            )
            .unwrap_or_else(|error| panic!("compile {}: {error}", path.display()));
        fs::write(
            output_dir.join(format!("{name}.spv")),
            artifact.as_binary_u8(),
        )
        .expect("write SPIR-V");
        println!("cargo:rerun-if-changed={}", path.display());
    }
    println!(
        "cargo:rerun-if-changed={}",
        shader_dir.join("common.glsl").display()
    );
}
