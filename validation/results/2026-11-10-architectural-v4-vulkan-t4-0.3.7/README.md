# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.7

Commit `536fa73` (branch `claude/project-thread-d6uhm6`, clean clone, Foton
0.3.7), 2026-11-10 04:15 UTC, 20.6 minutes. Google Colab T4 runtime: NVIDIA
Tesla T4 (driver 580.82.07; the reports name it `Vulkan device: Tesla T4`),
Python 3.13, Radiance 5.4a (b268408a). As before, a hand-written ICD manifest
points the Vulkan loader at NVIDIA's headless EGL library. The wheel was built
on the runtime with `maturin build --release` from that commit, and the Python
environment uses the same pinned versions as the
[e200cfc T4 run](../2026-11-08-architectural-v4-vulkan-t4-e200cfc/README.md)
(honeybee-core 1.64.61, honeybee-radiance 1.66.281, ladybug-geometry 1.35.1,
lbt-recipes 0.28.8, numpy 2.1.0); the full list and the `vulkaninfo` summary
are in `suite.json`. This is the Vulkan entry of
[`validation/release-evidence.json`](../../release-evidence.json), and the
same commit as the 0.3.7
[Metal suite](../2026-11-09-architectural-v4-metal-0.3.7-release/README.md).

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight documented open cases as e200cfc and as
the 0.3.7 Metal run. Every case executed on the Vulkan device. Each case's
settings, outcomes and result class match the e200cfc run.

`coefficient_comparison.{json,md}` and `converged_annual.json` are
byte-identical to the e200cfc run in 210 of 212 cases. The exceptions are the
`acceptance` model at MF:1 and MF:2, where the engine change in 0.3.7 (the
Honeybee adapter's triangulation of planar faces, #62) presumably moves some
triangles by rounding-level amounts: 3 and 2 values in `converged_annual.json`
and 10 each in `coefficient_comparison.json` differ in their last digits, by at
most 1.2e-6 relative. The `.md` tables, rounded for display, do not change. On
Metal the same model changed at MF:2 only. Only `report.md` otherwise differs,
in its version strings and timings.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays, stage folders and scene files stayed on the Colab runtime.
