# Installation

Foton is the product and Python import name. The PyPI distribution is named
`foton-daylight` because the shorter `foton` project name is already registered by
another publisher.

## Install from PyPI

```bash
python -m pip install foton-daylight
```

Optional integrations:

```bash
python -m pip install "foton-daylight[honeybee]"
python -m pip install "foton-daylight[viewer]"
```

Verify the installation:

```bash
python -c "from foton import Engine; print(Engine().capabilities())"
```

## Supported platforms

| Platform | Preferred backend | Runtime prerequisite |
| --- | --- | --- |
| macOS on Apple silicon | Metal | A Metal ray-tracing-capable Apple GPU |
| Linux x86-64 | Vulkan | A Vulkan 1.3 loader and compatible NVIDIA, AMD, or Intel driver |
| Windows x86-64 | Vulkan | A Vulkan 1.3-compatible NVIDIA, AMD, or Intel driver |
| Any supported Python platform | Reference CPU | No GPU runtime |

Foton rejects software Vulkan devices during automatic selection. If no supported GPU
is available, `Engine()` chooses the deterministic reference backend.

## Radiance

Radiance is not bundled in the wheel. Honeybee comparisons and benchmark references
require `oconv`, `rcontrib`, and the Radiance function library:

```bash
export RADIANCE_BIN=/path/to/radiance/bin
```

OpenStudio Radiance installations under `/Applications/OpenStudio-*/Radiance/bin`
are discovered automatically on macOS.

## Build from source

Source builds require Python 3.10 or newer, Rust 1.85 or newer, and a C/C++ build
toolchain usable by `shaderc`.

```bash
git clone <repository-url>
cd foton
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[honeybee,viewer,test]"
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.
