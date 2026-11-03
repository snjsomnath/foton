#!/usr/bin/env python3
"""Run the full benchmark suite and file the result under this machine's ID.

Runs the hardware timing suite (``benchmark_hardware.py``) and the Grasshopper
round trip (``benchmark_grasshopper.py``) at their defaults and writes one JSON
file to ``benchmarks/machines/<machine-id>/<timestamp>.json``. The machine ID
is derived from hardware fields only, so reruns on the same computer land in
the same folder whatever the Foton version, OS update or driver. Commit the
file in a pull request; ``compare_benchmarks.py`` tabulates every machine.

    python scripts/benchmark_suite.py
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import benchmark_grasshopper  # noqa: E402
import benchmark_hardware  # noqa: E402

MACHINES = ROOT / "benchmarks" / "machines"
SCHEMA_VERSION = 1


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("auto", "metal", "vulkan"), default="auto")
    parser.add_argument("--output", default=str(MACHINES), help="Root folder for machine results.")
    parser.add_argument("--label", help="Optional note, such as 'on battery' or 'eGPU'.")
    parser.add_argument("--skip-grasshopper", action="store_true")
    parser.add_argument("--quick", action="store_true", help="Smoke run; not for comparison.")
    return parser.parse_args(argv)


def _command_text(command):
    if shutil.which(command[0]) is None:
        return ""
    completed = subprocess.run(
        command, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False
    )
    return completed.stdout.strip() if completed.returncode == 0 else ""


def _gpu_details():
    """Return GPU vendor, core count and driver where the platform reports them."""
    system = platform.system()
    if system == "Darwin":
        text = _command_text(["system_profiler", "SPDisplaysDataType"])
        cores = re.search(r"Total Number of Cores:\s*(\d+)", text)
        vendor = re.search(r"Vendor:\s*(.+)", text)
        return {
            "vendor": vendor.group(1).strip() if vendor else "Apple",
            "cores": int(cores.group(1)) if cores else None,
            "driver": f"macOS {platform.mac_ver()[0]}",
        }
    text = _command_text(
        ["nvidia-smi", "--query-gpu=name,driver_version,memory.total", "--format=csv,noheader"]
    )
    if text:
        name, driver, memory = (part.strip() for part in text.splitlines()[0].split(","))
        return {"vendor": "NVIDIA", "name": name, "driver": driver, "memory": memory}
    if system == "Windows":
        text = _command_text(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | "
                "Select-Object -First 1 Name,AdapterCompatibility,DriverVersion | ConvertTo-Json",
            ]
        )
        if text:
            data = json.loads(text)
            return {
                "vendor": data.get("AdapterCompatibility"),
                "name": data.get("Name"),
                "driver": data.get("DriverVersion"),
            }
    return {"vendor": None, "driver": None}


def _git_commit():
    commit = _command_text(["git", "-C", str(ROOT), "rev-parse", "HEAD"])
    dirty = bool(_command_text(["git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=no"]))
    return {"commit": commit or None, "dirty": dirty}


def machine_fingerprint(host, engine):
    """Describe the machine and give it an ID that depends on hardware only."""
    gpu = {"name": host["gpu"], **_gpu_details()}
    hardware = {
        "system": host["system"],
        "machine": host["machine"],
        "model": host.get("model_identifier") or host["model"],
        "cpu": host["cpu"],
        "cpu_count": host["cpu_count"],
        "memory": host["memory"],
        "gpu": gpu["name"],
        "gpu_cores": gpu.get("cores"),
    }
    digest = hashlib.sha256(json.dumps(hardware, sort_keys=True).encode()).hexdigest()[:8]
    names = host["cpu"] if gpu["name"] == host["cpu"] else f"{host['cpu']} {gpu['name']}"
    slug = re.sub(r"[^a-z0-9]+", "-", names.lower()).strip("-")
    return {
        "machine_id": f"{slug}-{digest}",
        "model_name": host["model"],
        "hardware": hardware,
        "gpu": gpu,
        "os": f"{'macOS' if host['system'] == 'Darwin' else host['system']} {host['release']}",
        "python": host["python"],
        "backend": engine["selected_backend"],
        "foton": {"version": engine["version"], **_git_commit()},
    }


def main():
    args = parse_args()
    flags = ["--backend", args.backend]
    hardware_args = benchmark_hardware.parse_args(flags + (["--quick"] if args.quick else []))
    hardware = benchmark_hardware.run_suite(hardware_args)
    grasshopper = None
    if not args.skip_grasshopper:
        grasshopper_args = benchmark_grasshopper.parse_args(
            flags + (["--repeats", "1"] if args.quick else [])
        )
        grasshopper = benchmark_grasshopper.run_suite(grasshopper_args)
    fingerprint = machine_fingerprint(hardware["host"], hardware["engine"])
    recorded = datetime.now(timezone.utc)
    result = {
        "schema_version": SCHEMA_VERSION,
        "recorded_at_utc": recorded.strftime("%Y-%m-%d %H:%M:%SZ"),
        "label": args.label,
        "quick": args.quick,
        "fingerprint": fingerprint,
        "annual": hardware,
        "grasshopper": grasshopper,
    }
    folder = Path(args.output) / fingerprint["machine_id"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{recorded:%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(benchmark_hardware.report_markdown(hardware))
    if grasshopper:
        print(benchmark_grasshopper.report_markdown(grasshopper))
    print(f"Saved {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
