#!/usr/bin/env bash
# Regenerate THIRD_PARTY_LICENSES.md from the Rust dependencies that are
# compiled into the Foton wheel. Needs cargo-about:
#   cargo install cargo-about --locked --features cli
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root"
cargo about generate \
    --config scripts/licenses/about.toml \
    --manifest-path crates/daylight-python/Cargo.toml \
    --output-file THIRD_PARTY_LICENSES.md \
    scripts/licenses/about.hbs
echo "Wrote THIRD_PARTY_LICENSES.md"
