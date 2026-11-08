#!/bin/bash
# Foton Vulkan speed check on a Colab GPU: a released Foton from PyPI against
# a branch. Run in a Colab cell:
#   !curl -sL https://raw.githubusercontent.com/snjsomnath/foton/main/scripts/benchmark_vulkan_colab.sh | BRANCH=main bash
set -e
BRANCH=${BRANCH:-main}
BASELINE=${BASELINE:-0.3.5}
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader
nproc
apt-get -qq update >/dev/null && apt-get -qq install -y libvulkan1 vulkan-tools >/dev/null
mkdir -p /etc/vulkan/icd.d
printf '{"file_format_version":"1.0.0","ICD":{"library_path":"libEGL_nvidia.so.0","api_version":"1.3"}}\n' > /etc/vulkan/icd.d/nvidia_icd.json
vulkaninfo --summary 2>/dev/null | grep -E "deviceName|driverVersion" || true
cd /content && rm -rf foton-run && git clone -q --branch "$BRANCH" https://github.com/snjsomnath/foton.git foton-run
cd /content/foton-run && git log --oneline -1
if [ ! -x "$HOME/.cargo/bin/cargo" ]; then curl -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal >/dev/null 2>&1; fi
export PATH="$HOME/.cargo/bin:$PATH"
apt-get -qq install -y cmake ninja-build >/dev/null
pip -q install "maturin>=1.9.4,<2"
echo "== building the branch wheel"
rm -rf /content/wheels && maturin build --release --out /content/wheels 2>&1 | tail -2
echo "== baseline: foton-daylight $BASELINE from PyPI"
pip -q install --force-reinstall --no-deps "foton-daylight==$BASELINE"
pip -q install "foton-daylight[honeybee]==$BASELINE"
python scripts/benchmark_vulkan_identity.py run --output /content/profile-old
echo "== branch build"
pip -q install --force-reinstall --no-deps /content/wheels/foton_daylight-*.whl
python -c "import foton; print(foton.__version__, foton.__file__)"
python scripts/benchmark_vulkan_identity.py run --output /content/profile-new
echo "== branch build with buffers back in host memory"
FOTON_VULKAN_HOST_MEMORY=1 python scripts/benchmark_vulkan_identity.py run --output /content/profile-host
echo "== compare $BASELINE -> branch"
python scripts/benchmark_vulkan_identity.py compare /content/profile-old /content/profile-new
echo "== compare branch with host memory -> branch"
python scripts/benchmark_vulkan_identity.py compare /content/profile-host /content/profile-new
