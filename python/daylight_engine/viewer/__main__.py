"""Run the local Foton viewer."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()
    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        parser.error("the MVP viewer binds only to localhost")
    try:
        import uvicorn
    except ImportError as exc:
        raise RuntimeError(
            "viewer dependencies are missing; install foton-daylight[viewer]"
        ) from exc
    uvicorn.run(
        "foton.viewer.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
