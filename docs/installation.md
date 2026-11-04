# Installation

Foton is the product and Python import name. The PyPI distribution is named
`foton-daylight` because the shorter `foton` project name is already registered by
another publisher.

## In Rhino and Grasshopper

Rhino 8 users don't need the steps on this page. Install **foton** from
Rhino's Package Manager and let the Foton Settings component install the rest,
as the [Grasshopper quickstart](grasshopper-quickstart.md) shows. This page is
for running Foton from Python or the command line.

## Install from PyPI

```bash
python -m pip install foton-daylight
```

Optional integrations:

```bash
python -m pip install "foton-daylight[honeybee]"
python -m pip install "foton-daylight[viewer]"
```

The `honeybee` extra is what annual studies need. The `viewer` extra installs
the viewer's local service, but the browser app itself is built from a clone
of the repository (see [Build from source](#build-from-source) and the
[demo guide](../viewer/src/demo/README.md)).

Verify the installation:

```bash
python -c "from foton import Engine; print(Engine().capabilities())"
```

## Supported platforms

| Platform | Preferred backend | Runtime prerequisite |
| --- | --- | --- |
| macOS on Apple silicon | Metal | A Metal ray-tracing-capable Apple GPU |
| Linux x86-64 | Vulkan | A Vulkan 1.3 loader and a GPU with ray tracing (NVIDIA RTX, AMD Radeon RX 6000 or newer, Intel Arc) and current driver |
| Windows x86-64 | Vulkan | A GPU with ray tracing (NVIDIA RTX, AMD Radeon RX 6000 or newer, Intel Arc) and current driver |
| Any supported Python platform | Reference CPU | No GPU runtime |

Foton rejects software Vulkan devices during automatic selection. If no supported GPU
is available, `Engine()` chooses the deterministic reference backend.

## Radiance (optional, validation only)

Annual daylight does not need Radiance. Foton computes its own Perez
all-weather sky matrix (Perez, Seals and Michalsky 1993 over the Tregenza 1987
and Reinhart MF:2 patch subdivisions), implemented in Rust from the published
papers and validated to floating-point agreement against Radiance's
`gendaymtx` on three climates at both densities. `pip install
"foton-daylight[honeybee]"` is the whole run-time requirement for an annual
study; `foton-honeybee capabilities` reports the sky source in use.

Radiance is needed only to reproduce the validation evidence: the release
suite converges `rfluxmtx` references, audits the sky patch numbering with
`rcontrib`, and uses `gendaymtx` as the oracle for the built-in sky.
Everything here runs on Radiance 5.4a. Point Foton at an installation with:

```bash
export RADIANCE_BIN=/path/to/radiance/bin
```

OpenStudio Radiance installations under `/Applications/OpenStudio-*/Radiance/bin`
are discovered automatically on macOS. A study can still ask for Radiance's
sky with `HoneybeeStudy(..., sky_source="gendaymtx")` or
`foton-honeybee annual-daylight --sky-source gendaymtx`; the manifest records
which source produced the matrix either way.

## Build from source

Source builds require Python 3.10 or newer, Rust 1.85 or newer, and a C/C++ build
toolchain usable by `shaderc`.

```bash
git clone https://github.com/snjsomnath/foton.git
cd foton
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[honeybee,viewer,test]"
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.
