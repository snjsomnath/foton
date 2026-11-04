# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.2

Commit `3101ba1` (branch `release-0.3.2`, clean clone, `foton-daylight` 0.3.2
wheel built from the same tree), 2026-11-04 07:35 UTC, 25.0 minutes. Google
Colab T4 runtime: NVIDIA Tesla T4 (driver 580.82.07 from `nvidia-smi`; the
reports name it `Vulkan device: Tesla T4`), 2 vCPU, 12 GB RAM, Python 3.13,
Radiance 5.4a 2022-04-07 LBNL (5.4.b268408ad5). As for 0.3.1, a hand-written
ICD manifest points the Vulkan loader at NVIDIA's headless EGL library
(`/usr/lib64-nvidia/libEGL_nvidia.so.0`). The Python environment has the
pinned versions of the Metal suites (honeybee-core 1.64.61, honeybee-radiance
1.66.281, ladybug-geometry 1.35.1, lbt-recipes 0.28.8, numpy 2.1.0; the full
list is in `suite.json`), and the wheel was installed with `--no-deps`. This
is the Vulkan entry of [`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.1, in the same classes,
and the same as the [0.3.2 Metal suite](../2026-11-04-architectural-v4-metal-0.3.2-release/README.md).
Every case executed on the Vulkan device. The coefficient, annual, darkness
and sky-bin sections of every report are identical to the
[0.3.1 T4 run](../2026-11-03-architectural-v4-vulkan-t4-0.3.1/README.md) on
all 212 cases, as are each case's settings, outcomes and result class.

As on Metal, each case now records a `sky_sources` section (the candidate ran
with Foton's own Perez sky, `foton-sky-r1 (foton-daylight 0.3.2)`, the 0.3.2
default), each `candidate` section reads solver version 0.3.2, and the
diagnostic stock-recipe comparison of the `acceptance` model moved slightly
because Foton's Honeybee path now builds its sky itself. That comparison
reads `passed: false` in 0.3.1 and 0.3.2 alike and is not a gate; its largest
metric change is under 4 percentage points (`office_02` DA at MF:2, 34.64 to
30.80 pp maximum error).

`vulkan-tools` was not installed on this runtime, so the suite's
`driver_diagnostics` field records that `vulkaninfo` was missing instead of
the driver summary the 0.3.1 run kept; the device name and driver above come
from Foton's capabilities and `nvidia-smi`.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays and stage folders stayed on the Colab runtime.
