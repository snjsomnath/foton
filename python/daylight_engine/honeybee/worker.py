"""``foton-honeybee serve``: a background worker that keeps studies warm.

Grasshopper starts one worker and sends it one JSON request per line on
stdin. The worker keeps the prepared scene, the GPU and the traced sky
coefficients between requests, so a change of thresholds, schedule or weather
reuses the coefficients and only a change of geometry or trace settings traces
again. Replies use the same JSON-lines protocol as ``--jsonl`` runs, with the
request's ``id`` echoed in ``request_id``.

Request: ``{"id": "1", "command": "annual-daylight", "options": {...}}``.
Commands: ``annual-daylight``, ``daylight-factor``, ``ping``, ``shutdown``.
Options use the Python names of the command-line flags (``model``, ``wea``,
``output``, ``grid_filter``, ``maximum_bounces``...). Leave ``output`` out for
a live run: nothing is written and the values come back in the reply.

The worker exits when stdin closes, so it never outlives the program that
started it.
"""

from __future__ import annotations

from collections import OrderedDict
import json
import sys
from typing import Any, TextIO

from .commands import annual_daylight, daylight_factor, new_study, study_key
from .protocol import ProtocolWriter

# A resident study holds a GPU scene; two covers switching between two models.
MAXIMUM_STUDIES = 2
# Traced coefficients kept per study (each is sensors x patches x 3 floats).
MAXIMUM_COEFFICIENT_SETS = 4

COMMANDS = {
    "annual-daylight": annual_daylight,
    "daylight-factor": daylight_factor,
}


class Worker:
    """Keeps recently used studies in memory between requests, oldest dropped first."""

    def __init__(self) -> None:
        self.studies: OrderedDict[tuple, Any] = OrderedDict()
        # Weather outlives studies: a geometry change makes a new study, but
        # the sky matrix for the same weather file is reused from memory.
        self.weather_memo: dict = {}

    def study(self, options: dict[str, Any]):
        """Return ``(study, reused)`` for these options, creating the study when it is not already held."""
        key = study_key(options)
        study = self.studies.pop(key, None)
        reused = study is not None
        if study is None:
            study = new_study(options, weather_memo=self.weather_memo)
        self.studies[key] = study
        while len(self.studies) > MAXIMUM_STUDIES:
            self.studies.popitem(last=False)
        return study, reused

    def handle(self, request: dict[str, Any], writer: ProtocolWriter) -> bool:
        """Answer one request. Returns False when the worker should stop."""
        request_id = request.get("id")
        command = request.get("command")
        if command == "shutdown":
            writer.emit("complete", request_id=request_id, message="Worker stopped")
            return False
        if command == "ping":
            from foton import __version__

            writer.emit(
                "complete",
                request_id=request_id,
                message="Worker ready",
                engine_version=__version__,
                resident_studies=len(self.studies),
            )
            return True
        run = COMMANDS.get(command)
        if run is None:
            raise ValueError("unknown worker command {0!r}".format(command))
        options = dict(request.get("options") or {})

        def progress(update):
            writer.emit("progress", request_id=request_id, **update)

        writer.emit(
            "started",
            request_id=request_id,
            recipe=command.replace("-", "_"),
            progress=0.0,
            message="Preparing study",
        )
        study, reused = self.study(options)
        manifest = run(options, progress=progress, study=study)
        cache = study._coefficient_cache
        while len(cache) > MAXIMUM_COEFFICIENT_SETS:
            cache.pop(next(iter(cache)))
        manifest["worker"] = {"study_reused": reused}
        writer.emit(
            "complete",
            request_id=request_id,
            progress=1.0,
            message="Analysis complete",
            manifest=manifest,
        )
        return True


def serve(stdin: TextIO | None = None, stdout: TextIO | None = None) -> int:
    """Run the worker loop on ``stdin`` and ``stdout`` until stdin closes or ``shutdown`` arrives. Returns the exit code."""
    stdin = stdin or sys.stdin
    protocol_stream = stdout or sys.stdout
    writer = ProtocolWriter(protocol_stream)
    # Anything a library prints must not corrupt the protocol stream.
    original_stdout = sys.stdout
    sys.stdout = sys.stderr
    worker = Worker()
    try:
        writer.emit("ready", message="Foton worker ready")
        for line in stdin:
            line = line.strip()
            if not line:
                continue
            request_id = None
            try:
                request = json.loads(line)
                if not isinstance(request, dict):
                    raise ValueError("a worker request must be a JSON object")
                request_id = request.get("id")
                if not worker.handle(request, writer):
                    break
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as error:
                writer.emit(
                    "failed",
                    request_id=request_id,
                    error_type=error.__class__.__name__,
                    message=str(error),
                )
    finally:
        sys.stdout = original_stdout
    return 0
