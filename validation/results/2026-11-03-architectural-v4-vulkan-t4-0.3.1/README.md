# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.1

Commit `6afe2aa` (branch `release-0.3.1`, clean clone, `foton-daylight` 0.3.1
wheel built from the same tree), 2026-11-03 19:55 UTC, 23.5 minutes. Google
Colab runtime: NVIDIA Tesla T4 (driver 580.82.07, Vulkan API 1.4.312,
conformance 1.4.1.3; the reports name it `Vulkan device: Tesla T4`), 2 vCPU,
12 GB RAM, Python 3.13, Radiance 5.4a 2022-04-07 LBNL (5.4.b268408ad5). It is
the same Colab runtime as the [0.3.0 run](../2026-11-03-architectural-v4-vulkan-t4/README.md),
with the same hand-written ICD manifest pointing at NVIDIA's headless EGL
library and the same Python environment; only the Foton wheel was replaced
(installed with `--no-deps`). This is the Vulkan entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight open cases as 0.3.0, in the same classes,
and the same as the [0.3.1 Metal suite](../2026-11-03-architectural-v4-metal-0.3.1-release/README.md).
Every case executed on the Vulkan device. The coefficient, annual and darkness
sections of every report are identical to the 0.3.0 T4 run on all 212 cases,
as expected: 0.3.1 changes only the Metal backend.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays and stage folders stayed on the Colab runtime.
