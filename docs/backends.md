# Compute Backends

## Automatic selection

```python
from foton import Engine

engine = Engine()
print(engine.capabilities())
```

Selection is deterministic:

1. A compatible Apple GPU selects Metal.
2. A compatible discrete Vulkan GPU selects Vulkan.
3. A compatible integrated Vulkan GPU selects Vulkan.
4. Otherwise Foton selects the deterministic CPU reference backend.

Vulkan auto-selection accepts NVIDIA (`0x10DE`), AMD (`0x1002`), and Intel
(`0x8086`) hardware devices. CPU and software Vulkan implementations are rejected.

## Explicit selection

```python
metal = Engine({"backend": "metal"})
vulkan = Engine({"backend": "vulkan"})
reference = Engine({"backend": "reference"})
```

Explicit Metal or Vulkan requests fail with a diagnostic when the backend is
unavailable. They never silently fall back to the reference backend.

## Vulkan requirements

The physical device and driver must expose Vulkan 1.3 plus:

- Buffer device address
- Acceleration structures
- Deferred host operations
- Ray query
- Scalar block layout
- SPIR-V 1.4-compatible shader support

Foton embeds its SPIR-V compute shaders in the wheel. The Vulkan loader and hardware
driver remain system prerequisites.

## Result provenance

Every result reports:

- `transport_backend`
- `used_reference_fallback`
- Upload, acceleration-structure, tracing, annual-reduction, and snapshot timings
- Solver metadata through `metadata_json()`

Use these fields when collecting benchmark data or comparing different machines.
