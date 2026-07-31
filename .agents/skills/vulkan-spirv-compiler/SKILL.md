---
name: vulkan-spirv-compiler
description: Compile and validate GLSL Vulkan shaders to SPIR-V with glslangValidator, including target-environment and ray-query extension checks. Use when editing .comp or .glsl shaders in a Vulkan daylight-analysis project.
---
# Vulkan SPIR-V Compiler

Compile a shader with `scripts/compile_shader.py` before changing runtime Vulkan code.

The script requires `glslangValidator` on `PATH` or via `--validator`. It uses Vulkan
semantics (`-V`) and defaults to `vulkan1.3`. The default output is `bin/<name>.spv`
next to the input shader; pass `--output` to select another path.

Use `--require-ray-query` for shaders that must declare
`#extension GL_EXT_ray_query : require`. Pass `--spirv-val` to run SPIR-V Tools
validation after compilation. Treat compiler or validator diagnostics as blocking.

```text
python scripts/compile_shader.py --input shaders/daylight.comp \
  --require-ray-query --spirv-val
```

The generated SPIR-V is a build artifact and should normally be excluded from source
control. No pip dependency is required; install the Vulkan SDK or standalone glslang.
