---
name: foton-viewer-development
description: Start, debug, and validate Foton's Vite frontend and Python/FastAPI viewer backend together. Use when npm run dev starts only Vite, Python fails with ENOENT, virtual-environment selection is wrong, the native extension is missing, frontend/backend shutdown is inconsistent, or viewer CI fails.
---

# Foton Viewer Development

Run development from `viewer/`:

```text
npm run dev
```

`viewer/scripts/dev.mjs` must start both `npm run dev:frontend` and
`python -m foton.viewer --reload`. A ready Vite URL does not prove the backend started.
Watch both child processes and terminate the peer when either exits or emits an error.

Resolve Python in this order:

1. Explicit `PYTHON`
2. Existing active `VIRTUAL_ENV`
3. Existing repository `.venv`
4. `python3` on Unix or `python` on Windows

Validate the executable itself, not only the virtual-environment directory. A stale
`.venv` directory can produce `spawn .../.venv/bin/python ENOENT`.

Prepare development dependencies and the native extension with the repository
interpreter:

```text
python -m pip install -e '.[viewer]'
```

Set `PYTHONPATH` to include the repository `python/` directory, but do not treat that as
a replacement for building/installing `daylight_engine._native`.

## Diagnostics

- Backend ENOENT: print the selected interpreter, check it exists, then use `PYTHON` or
  recreate `.venv`.
- `ModuleNotFoundError` for `foton`: install the package with viewer extras.
- Missing `_native`: rebuild/install through maturin rather than changing imports.
- Frontend works but API fails: inspect the backend child output and configured API URL.
- Port conflict: identify which child owns the port before changing defaults.

Validate viewer changes with `npm test -- --run` and `npm run build`. Exercise
`npm run dev` when changing process orchestration.
