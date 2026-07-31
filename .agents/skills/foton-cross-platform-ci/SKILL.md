---
name: foton-cross-platform-ci
description: Diagnose and fix Foton CI across Rust, Python, Linux, Windows, macOS, maturin, and the web viewer. Use when GitHub Actions fails, a platform-specific backend leaks into another target, a wheel cannot build or import, the minimum Rust/Python version breaks, or CI differs from local development.
---

# Foton Cross-Platform CI

Inspect the failing job and full log before editing. Fix the smallest root cause and
rerun the narrowest affected check first.

## Supported Baselines

- Rust: 1.85
- Python: 3.10 and 3.13 in regular CI; 3.10–3.13 in releases
- Linux wheels: manylinux2014
- macOS release target: 11.0
- Viewer: Node 20

Do not accept syntax merely because local stable Rust compiles it. Avoid let-chain
syntax unsupported by Rust 1.85. Compare Vulkan extension `CStr` values through
`to_bytes()` rather than relying on newer trait implementations.

Use `#[cfg(target_os = "macos")]` on Metal imports, helpers, and tests, not only on
their call sites. Keep Linux and Windows builds free of unused Metal symbols. Apply the
same rule to platform probes in both Python bindings and CLI code.

Use `datetime.now(timezone.utc)` for Python 3.10 compatibility; `datetime.UTC` is not
available there.

## Maturin Rules

For the native Python OS matrix, set `container: "off"` so the interpreter installed
by `actions/setup-python` remains visible. For the dedicated Linux package smoke test,
use the manylinux container with an explicit interpreter such as `python3.13`.

Always install the built wheel before Python tests. Do not let tests accidentally import
the source tree in place of packaged contents. Verify:

```text
import foton
import daylight_engine
assert foton.Engine is daylight_engine.Engine
```

## Failure Signatures

- `no virtualenv found` from `maturin develop`: build a wheel and install it in CI.
- Interpreter missing inside manylinux: use the container interpreter name, not the
  host setup-python path.
- glslang `std::filesystem` unavailable on Intel macOS: set deployment target 11.0.
- Linux/Windows unused Metal import: cfg-gate the import or helper.
- GitHub Release says `not a git repository`: add checkout to that job.
- OIDC `invalid-publisher`: correct PyPI trusted-publisher claims.

Ignore unrelated runner deprecation warnings while fixing a concrete failure. After
the targeted job passes, run the full Rust, Python, viewer, and package matrix.
