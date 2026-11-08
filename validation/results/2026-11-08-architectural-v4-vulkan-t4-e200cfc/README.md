# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.6 engine

Commit `e200cfc` (the head of #56, clean clone; the wheel built from that tree
reports 0.3.5 because the version bump came after it), 2026-11-08 15:15 UTC,
20.1 minutes. Google Colab T4 runtime: NVIDIA Tesla T4 (driver 580.82.07; the
reports name it `Vulkan device: Tesla T4`), Python 3.13, Radiance 5.4a. As
before, a hand-written ICD manifest points the Vulkan loader at NVIDIA's
headless EGL library. The Python environment uses the same pinned versions as
the [0.3.3 T4 run](../2026-11-04-architectural-v4-vulkan-t4-0.3.3/README.md);
the full list and the `vulkaninfo` summary are in `suite.json`.

`e200cfc` has the 0.3.6 engine: it differs from the 0.3.6 release commit only
in version numbers and in files the suite never reads. It includes the Vulkan
speed-ups of 0.3.6 (buffers in GPU memory, batched dispatches and BLAS builds,
the early-exit Sobol loop and the threaded hourly export). This is the Vulkan
entry of [`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight documented open cases as 0.3.3. Every
case executed on the Vulkan device.

The speed-ups leave the numbers unchanged: `coefficient_comparison.json`,
`coefficient_comparison.md` and `converged_annual.json` are byte-identical to
the 0.3.3 T4 run for all 212 cases. Only `report.md` differs, in its version
strings and timings.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays and stage folders stayed on the Colab runtime.
