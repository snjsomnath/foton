# Vulkan suite on an NVIDIA Tesla T4, Foton 0.3.8

Commit `7eca2fe` (branch `claude/project-thread-1f1b9e`, clean clone, Foton
0.3.8), 2026-11-15 06:23 UTC, 20 minutes. Google Colab T4 runtime: NVIDIA
Tesla T4 (driver 580.82.07), Python 3.13, Radiance 5.4a (b268408a). As before,
a hand-written ICD manifest points the Vulkan loader at NVIDIA's headless EGL
library. The wheel was built on the runtime with `maturin build --release`
from that commit. This is the Vulkan entry of
[`validation/release-evidence.json`](../../release-evidence.json).

`7eca2fe` is the version bump. The release code commit `16e9459`, which the
[Metal suite](../2026-11-14-architectural-v4-metal-0.3.8-release/README.md) and
the [Rhino checklist](../2026-11-14-rhino-macos-0.3.8/README.md) ran on, only
adds the rebuilt Grasshopper files in `grasshopper_foton/distribution/`. The
suite never loads those, and the release verifier accepts the run for that
reason.

It ran `validate_release_suite.py --backend vulkan --workers 2
--reuse-references` against the published bundle
[`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03)
(SHA-256 checked).

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors: the same eight documented open cases as the
[0.3.7 T4 run](../2026-11-10-architectural-v4-vulkan-t4-0.3.7/README.md) and
the 0.3.8 Metal run. Every case ran on the Vulkan device.

`coefficient_comparison.{json,md}` and `converged_annual.json` are
byte-identical to the 0.3.7 T4 run in all 212 cases (636 files). That is
expected: the change in 0.3.8 is an optional `engine=` argument to
`HoneybeeStudy` (#67), which the suite does not pass. `report.md` differs only
in version strings, paths and timings.

## Python environment

The Ladybug Tools packages have the same pinned versions as the 0.3.7 run
(honeybee-core 1.64.61, honeybee-radiance 1.66.281,
honeybee-radiance-postprocess 0.5.7, ladybug-geometry 1.35.1, lbt-recipes
0.28.8, numpy 2.1.0; the full list is in `suite.json`). Colab's own packages
had moved since 0.3.7, so three changes were needed to rebuild that
environment. None of them touches Foton:

- pip no longer resolves the pinned openstudio, openstudio-backporter and
  honeybee-openstudio versions together, so the pinned list was installed
  with `--no-deps`. luigi 3.3.0, click 8.1.7, click-plugins 1.1.1.2,
  pydantic-openapi-helper 1.0.5, python-daemon 3.1.2, lockfile 0.12.2 and
  tenacity 8.5.0 (the 0.3.7 versions) were then added for Honeybee's stock
  recipe.
- Colab now ships cupy 14 for CUDA 13. honeybee-radiance-postprocess uses cupy
  whenever it can import it, and cupy 14 fails there on a list input, so every
  case stopped with an error. cupy was uninstalled, and postprocessing ran on
  numpy, as it does on the Mac.

## Files

`suite.json`, `suite.md`, and per case `report.md`, `coefficient_comparison.{json,md}`,
`converged_annual.json` and, for the acceptance model, `stock_comparison/`.
The arrays, stage folders and scene files stayed on the Colab runtime.
