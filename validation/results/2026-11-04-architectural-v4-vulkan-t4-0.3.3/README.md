# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.3

Commit `eda816c` (branch `release-0.3.3`, clean clone, `foton-daylight` 0.3.3
wheel built from the same tree), 2026-11-04 10:27 UTC, 21.6 minutes. Google
Colab T4 runtime with the High RAM option: NVIDIA Tesla T4 (driver 580.82.07,
15 GB; the reports name it `Vulkan device: Tesla T4`), 8 vCPU, 50 GB RAM,
Python 3.13, Radiance 5.4a 2022-04-07 LBNL (5.4.b268408ad5). The 0.3.2 run
used the standard T4 runtime (2 vCPU, 12 GB RAM), which is why this one is
quicker; the GPU and driver are the same. As before, a hand-written ICD
manifest points the Vulkan loader at NVIDIA's headless EGL library
(`/usr/lib64-nvidia/libEGL_nvidia.so.0`). The Python environment has the
pinned versions of the Metal suites (honeybee-core 1.64.61, honeybee-radiance
1.66.281, ladybug-geometry 1.35.1, lbt-recipes 0.28.8, numpy 2.1.0; the full
list is in `suite.json`), and the wheel was installed with `--no-deps`. This
time `vulkan-tools` was installed, so `suite.json` records the full
`vulkaninfo` summary under `driver_diagnostics`. This is the Vulkan entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.2, in the same classes,
and the same as the [0.3.3 Metal suite](../2026-11-04-architectural-v4-metal-0.3.3-release/README.md).
Every case executed on the Vulkan device. The coefficient, annual, darkness
and sky-bin sections of every report are identical to the
[0.3.2 T4 run](../2026-11-04-architectural-v4-vulkan-t4-0.3.2/README.md) on
all 212 cases, as are each case's settings, outcomes and result class; the
Rust engine is unchanged since 0.3.2.

The only other differences from 0.3.2 are the version strings (sky version
`foton-sky-r1 (foton-daylight 0.3.3)`, solver version 0.3.3) and the
diagnostic stock-recipe comparison of the `acceptance` model, which reruns
Honeybee's stock Radiance recipe each time and varies from run to run; it
reads `passed: false` in every release and is not a gate.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays and stage folders stayed on the Colab runtime.
