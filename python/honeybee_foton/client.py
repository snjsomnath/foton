"""Cancelable external-process client for the ``foton-honeybee`` CLI."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import json
from pathlib import Path
import queue
import shutil
import subprocess
import threading
from typing import Callable

from foton.honeybee.protocol import annual_request, parse_message

from .results import load_manifest


class FotonProcessError(RuntimeError):
    pass


class FotonProcessCancelled(FotonProcessError):
    pass


@dataclass(frozen=True)
class FotonRunHandle:
    future: object
    cancel_event: threading.Event

    def cancel(self):
        self.cancel_event.set()

    def result(self, timeout=None):
        return self.future.result(timeout=timeout)


def discover_executable(configured=None) -> str:
    if configured:
        path = Path(configured).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        return str(path)
    executable = shutil.which("foton-honeybee")
    if executable is None:
        raise FileNotFoundError(
            "foton-honeybee is not on PATH; install foton-daylight or configure "
            "the executable in Foton Settings"
        )
    return executable


@dataclass(frozen=True)
class AnnualDaylightRequest:
    model: str
    wea: str
    output_folder: str
    schedule: str | None = None
    backend: str = "auto"
    grid_filter: str = "*"
    north: float = 0.0
    quality: str = "final"
    sky_density: int = 1
    threshold: float = 300.0
    udi_lower: float = 100.0
    udi_upper: float = 3000.0
    target_time: float = 50.0
    direct_samples: int | None = None
    maximum_samples: int | None = None
    maximum_bounces: int = 1
    scene_seed: int = 0
    export_illuminance: bool = True

    def protocol_request(self):
        return annual_request(
            model=self.model,
            wea=self.wea,
            schedule=self.schedule,
            backend=self.backend,
            grid_filter=self.grid_filter,
            north=self.north,
            quality=self.quality,
            sky_density=self.sky_density,
            threshold=self.threshold,
            udi_lower=self.udi_lower,
            udi_upper=self.udi_upper,
            target_time=self.target_time,
            direct_samples=self.direct_samples,
            maximum_samples=self.maximum_samples,
            maximum_bounces=self.maximum_bounces,
            scene_seed=self.scene_seed,
            export_illuminance=self.export_illuminance,
        )

    def command(self, executable, output_folder):
        command = [
            executable,
            "annual-daylight",
            "--jsonl",
            "--model",
            str(Path(self.model).expanduser().resolve()),
            "--wea",
            str(Path(self.wea).expanduser().resolve()),
            "--output",
            str(output_folder),
            "--backend",
            self.backend,
            "--grid-filter",
            self.grid_filter,
            "--north",
            str(self.north),
            "--quality",
            self.quality,
            "--sky-density",
            str(self.sky_density),
            "--threshold",
            str(self.threshold),
            "--udi-lower",
            str(self.udi_lower),
            "--udi-upper",
            str(self.udi_upper),
            "--target-time",
            str(self.target_time),
            "--maximum-bounces",
            str(self.maximum_bounces),
            "--scene-seed",
            str(self.scene_seed),
            (
                "--export-illuminance"
                if self.export_illuminance
                else "--no-export-illuminance"
            ),
        ]
        if self.schedule:
            command.extend(
                ["--schedule", str(Path(self.schedule).expanduser().resolve())]
            )
        if self.direct_samples is not None:
            command.extend(["--direct-samples", str(self.direct_samples)])
        if self.maximum_samples is not None:
            command.extend(["--maximum-samples", str(self.maximum_samples)])
        return command


class FotonClient:
    def __init__(self, executable=None):
        self.executable = discover_executable(executable)
        self._executor = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="honeybee-foton"
        )

    def capabilities(self, backend="auto"):
        completed = subprocess.run(
            [self.executable, "capabilities", "--backend", backend],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if completed.returncode:
            raise FotonProcessError(completed.stderr.strip())
        return json.loads(completed.stdout)

    def run_annual_daylight(
        self,
        request: AnnualDaylightRequest,
        *,
        progress: Callable[[dict], None] | None = None,
        cancel_event=None,
        output_policy="unique",
    ):
        requested_output = Path(request.output_folder).expanduser().resolve()
        if output_policy == "reuse" and requested_output.exists():
            manifest = load_manifest(requested_output / "run_manifest.json")
            fingerprint = request.protocol_request()["fingerprint"]
            if manifest.get("request", {}).get("fingerprint") != fingerprint:
                raise FotonProcessError(
                    "existing output is incompatible with this request"
                )
            if progress:
                progress({"event": "reused", "manifest": manifest})
            return manifest
        allocation_policy = "error" if output_policy == "reuse" else output_policy
        output = _resolve_output(request, allocation_policy, reserve=True)
        command = request.command(self.executable, output)
        process = subprocess.Popen(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
        )
        messages: queue.Queue = queue.Queue()
        stderr_lines = []

        def read_stdout():
            assert process.stdout is not None
            for line in process.stdout:
                messages.put(("stdout", line))
            messages.put(("stdout_done", None))

        def read_stderr():
            assert process.stderr is not None
            for line in process.stderr:
                stderr_lines.append(line)

        stdout_thread = threading.Thread(target=read_stdout, daemon=True)
        stderr_thread = threading.Thread(target=read_stderr, daemon=True)
        stdout_thread.start()
        stderr_thread.start()
        manifest = None
        stdout_done = False
        while process.poll() is None or not stdout_done:
            if cancel_event is not None and cancel_event.is_set():
                process.terminate()
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    process.kill()
                raise FotonProcessCancelled(
                    "Foton annual daylight run was cancelled"
                )
            try:
                kind, value = messages.get(timeout=0.1)
            except queue.Empty:
                continue
            if kind == "stdout_done":
                stdout_done = True
                continue
            message = parse_message(value)
            if progress:
                progress(message)
            if message["event"] == "complete":
                manifest = message["manifest"]
        return_code = process.wait()
        stdout_thread.join(timeout=1)
        stderr_thread.join(timeout=1)
        if return_code != 0:
            raise FotonProcessError(
                "Foton process failed with exit code "
                f"{return_code}: {''.join(stderr_lines).strip()}"
            )
        if manifest is None:
            raise FotonProcessError("Foton process completed without a manifest")
        return manifest

    def run_annual_daylight_async(self, request, **options):
        cancel_event = options.pop("cancel_event", None) or threading.Event()
        future = self._executor.submit(
            self.run_annual_daylight,
            request,
            cancel_event=cancel_event,
            **options,
        )
        return FotonRunHandle(future=future, cancel_event=cancel_event)


def _resolve_output(request, policy, *, reserve=False):
    output = Path(request.output_folder).expanduser().resolve()
    if policy not in {"unique", "error", "reuse"}:
        raise ValueError("output_policy must be 'unique', 'error', or 'reuse'")
    if policy == "reuse":
        return output
    if policy == "error":
        if output.exists():
            raise FileExistsError(output)
    for index in range(1_000_000):
        candidate = (
            output
            if index == 0
            else output.with_name(f"{output.name}-{index:03d}")
        )
        if not reserve:
            if not candidate.exists():
                return candidate
            if policy == "error":
                raise FileExistsError(candidate)
            continue
        candidate.parent.mkdir(parents=True, exist_ok=True)
        try:
            candidate.mkdir(exist_ok=False)
        except FileExistsError:
            if policy == "error":
                raise
            continue
        return candidate
    raise RuntimeError(f"could not allocate an output folder beside {output}")
