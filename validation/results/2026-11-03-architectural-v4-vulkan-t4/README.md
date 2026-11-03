# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.0

Commit `87f96a0` (clean clone, wheel built from the same tree, `foton-daylight`
0.3.0), 2026-11-03 10:48 UTC, 23.8 minutes. Google Colab Pro runtime: NVIDIA
Tesla T4 (driver 580.82.07, Vulkan API 1.4.312, conformance 1.4.1.3, VBIOS
90.04.A7.00.01; the reports name it `Vulkan device: Tesla T4`), 2 vCPU, 12 GB
RAM, Linux 6.6 with glibc 2.39, Python 3.13, Radiance 5.4a 2022-04-07 LBNL
(5.4.b268408ad5, the same build as the Mac), honeybee-core 1.64.61,
honeybee-radiance 1.66.281, ladybug-geometry 1.35.1, lbt-recipes 0.28.8,
numpy 2.1.0. Colab ships no Vulkan ICD manifest; one was written by hand
pointing at NVIDIA's headless EGL library (`libEGL_nvidia.so.0`). This is the Vulkan entry of
[`validation/release-evidence.json`](../../release-evidence.json) and the
first run of Foton's Vulkan backend on real hardware.

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03),
exported from the [Metal campaign of the same morning](../2026-11-03-architectural-v4-metal-0.3.0/README.md).
Two vCPUs could not have redone that campaign's six hours of twelve-worker
Radiance; they did not need to, because the references describe the scenes,
not the engine. The run still exported every scene, audited the sky bins,
prepared the Gothenburg weather and ran Honeybee's stock recipe on the
acceptance model through Radiance on the T4's own CPU.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as Metal, in the same classes.
Every case executed on the Vulkan device (`transport_backend: vulkan`, no
reference fallback) and every sensor grid matched its reference exactly.

## Vulkan against Metal

Judged against identical references, the two backends agree far inside the
gates. Over all 212 cases and every grid:

| Quantity | Vulkan minus Metal |
| --- | --- |
| Direct-stage energy bias (NMBE) | identical to the printed digit on every grid |
| Full-stage energy bias (NMBE) | median 0.000, largest 0.008 percentage points (`interior_glazing` MF:2, adjacent room) |
| DA mean absolute error | largest difference 0.003 percentage points |
| Result class | identical on all 212 cases |

The remaining differences are floating-point order and the two GPUs' random
sequences in the indirect stage; they are two orders of magnitude below the
smallest gate.

Cold end-to-end annual run, median over the corpus: 1.54 s on the T4 against
0.25 s on the Apple M4 Pro. Both are the `final` preset as shipped.

## What this run established

- The two Vulkan bugs found by the first hardware smoke test the same morning
  (a dropped `ash::Entry` that unloaded the loader and crashed on Linux, and
  an acceleration-structure descriptor written without a count, which left
  every ray missing) are fixed in `87f96a0`; before the fix the full
  coefficients summed to about 12π per sensor instead of the reference's 0.4
  to 0.6.
- `--reuse-references` works across machines, operating systems and GPU
  vendors: the sensor-grid check passed on every case, with a largest
  coordinate difference of 0.0 even for the rotated scenes.

Not covered: Windows (the Vulkan backend has only run on Linux), any GPU other
than the T4, a stock Vulkan loader configuration (see the ICD note above).
`hardware.driver_diagnostics` is empty in `suite.json` because the suite's
diagnostics only know macOS; the device and driver details above were read on
the runtime with `nvidia-smi` and `vulkaninfo --summary`.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays and stage folders stayed on the Colab runtime.
