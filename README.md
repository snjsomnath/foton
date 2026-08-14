# Foton

**GPU-accelerated daylight transport for architectural analysis.**

[![PyPI](https://img.shields.io/pypi/v/foton-daylight?style=flat-square)](https://pypi.org/project/foton-daylight/)
[![Radiance benchmark](https://img.shields.io/badge/Radiance-benchmarked-blue?style=flat-square)](https://www.radiance-online.org/)
[![Honeybee](https://img.shields.io/badge/Honeybee-1.x-orange?style=flat-square)](https://www.ladybug.tools/honeybee/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

Foton is an experimental GPU-based daylight transport engine for architectural
analysis.

It is not a replacement for Radiance or Honeybee. Instead, it explores whether
the expensive ray-traced transport step in a Radiance-style daylight workflow
can be moved to the GPU and made fast enough for interactive use.

## Where Foton fits

A simplified Radiance matrix workflow looks like:

    Sky
     |
     v
    rfluxmtx / rcontrib
     |
     v
    Sky -> sensor transport
     |
     v
    Illuminance / annual metrics

Foton focuses on the transport step:

    Sky
     |
     v
    +-----------+
    |   Foton   |  GPU ray tracing
    +-----------+
     |
     v
    Sky -> sensor transport
     |
     v
    Illuminance / annual metrics

Foton uses Honeybee-generated models and Radiance as a reference for
benchmarking.

## What it does

- GPU ray-traced direct visibility
- Diffuse multi-bounce transport
- Thin-glass transport
- Tregenza (146) and Reinhart MF:2 (578) sky subdivisions
- Daylight transport coefficients
- Illuminance and annual daylight calculations
- DA and sDA
- Metal and Vulkan GPU backends
- Deterministic CPU reference backend
- Python API and Honeybee integration

The current implementation is aimed primarily at conventional architectural
daylighting: diffuse surfaces, ordinary glazing, shading devices, and
building-scale sensor grids.

## What it does not do

Foton does not currently reproduce the full Radiance material and transport
model.

In particular, it should not yet be assumed equivalent to Radiance for:

- complex BSDF materials
- advanced daylight-redirecting systems
- highly specular environments
- arbitrary Radiance material types
- certification or compliance calculations

Radiance remains the reference for those applications.

## How does it compare with Radiance?

The repository contains automated comparisons against Radiance using
Honeybee-generated test scenes.

In the current benchmark:

- Direct visibility: 13 mismatches out of 31,536 sensor/sky-patch tests
- Full diffuse + thin-glass transport: 5.3% NMBE
- Annual illuminance: 5.2% NMBE
- sDA difference: 0.0 percentage points (!but the geometry that this has been tested on is fairly simple)

These results are from a specific test scene and configuration. They are not a
claim that Foton will match Radiance to a fixed accuracy for arbitrary models.

The benchmark results and methodology are included in the repository so that
the comparison can be reproduced and improved over time.

## Performance

On the current benchmark machine (Apple M4 Pro), the 216-sensor / 146-patch
full transport calculation took:

    Foton:      5.79 ms
    rcontrib:   3574 ms

This is a single benchmark configuration, not a general speedup claim.

The purpose of the comparison is to show the potential of GPU transport for
interactive daylight analysis. (I also don't have access to other GPUs at the moment to test out foton using vullkan)

## Installation

    pip install foton-daylight

For Honeybee support:

    pip install "foton-daylight[honeybee]"

## Status

Foton is experimental and under active development.

The goal is not to replace Radiance. The goal is to make a focused part of
Radiance-style daylight transport fast enough to use interactively in
architectural design and research.
