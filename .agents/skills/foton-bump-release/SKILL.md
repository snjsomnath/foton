---
name: foton-bump-release
description: Bump Foton's coordinated Python, Rust, and viewer versions, validate the maturin artifacts, publish a tagged release to PyPI through GitHub Actions, and verify the resulting PyPI and GitHub Release. Use when preparing a new Foton release, changing pyproject or Cargo versions, creating release tags, or recovering a failed release workflow.
---

# Foton Bump & Release

Use this skill for an end-to-end Foton release. The distribution is
`foton-daylight`; the public import is `foton`, the compatibility import is
`daylight_engine`, and the native module is `daylight_engine._native`.

## Preflight

1. Read the repository's release-pipeline guidance and inspect the current branch,
   worktree, latest tag, GitHub Actions, PyPI JSON, and GitHub Releases.
2. Require a clean worktree and a `main` branch synchronized with `origin/main`.
3. Choose a new immutable semantic version. Confirm that the version is absent from
   PyPI and that its tag and GitHub Release do not already exist. Never reuse or move
   a published version/tag.

## Bump metadata

Update the same version in:

- `pyproject.toml` `[project].version`;
- workspace `Cargo.toml` `[workspace.package].version`;
- `Cargo.lock` workspace package entries (run `cargo check --workspace` to refresh);
- `CHANGELOG.md`, with the release date and user-visible changes;
- `python/daylight_engine/viewer/app.py` FastAPI version;
- `viewer/package.json` and the root package entry in `viewer/package-lock.json`;
- release documentation examples if they name a concrete version.

Do not mass-replace historical benchmark fixtures or test fixtures. Preserve
`tool.maturin.python-packages = ["foton", "daylight_engine", "honeybee_foton"]`.

## Validate before tagging

Run local checks appropriate to the change:

```text
cargo fmt --all -- --check
cargo test --workspace
cd viewer && npm ci && npm test -- --run && npm run build
```

In an isolated Python environment install the test and optional Honeybee/viewer
dependencies, then run `python -m pytest tests/python -q`.

Build and smoke-test a release wheel and source distribution. Use an explicit Linux
interpreter (`python3.13`) and `manylinux: "2014"` in CI. Set
`MACOSX_DEPLOYMENT_TARGET=11.0` for macOS wheels. Install the wheel and verify:

```python
from foton import Engine
import foton, daylight_engine
assert foton.Engine is daylight_engine.Engine
assert foton.__version__ == "X.Y.Z"
print(Engine().capabilities())
```

Build a wheel from the generated sdist and install it too. Cargo package metadata
warnings are non-blocking; build, install, import, and test failures are blockers.

## Commit, tag, and publish

1. Review `git diff --check`, commit the bump, and push `main`.
2. Wait for CI on the exact commit to pass all required jobs.
3. Create an annotated tag and push it:

   ```text
   git tag -a vX.Y.Z -m "Foton X.Y.Z" <commit>
   git push origin vX.Y.Z
   ```

4. Monitor `release.yml`. It must finish 16 wheels (Linux, Windows, Apple Silicon
   macOS, Intel macOS across Python 3.10–3.13) plus one sdist before publication.
5. Publish only through PyPI trusted publishing. The publish job needs
   `environment: pypi` and `permissions: id-token: write`; the account-side claims
   are project `foton-daylight`, owner `snjsomnath`, repository `foton`, workflow
   `release.yml`, environment `pypi`.
6. Create the GitHub Release only after the PyPI job succeeds. The GitHub Release job
   must check out the repository before `gh release create --verify-tag`.

Never substitute a stored PyPI password/token for OIDC as the first fix. An
`invalid-publisher` error means the trusted-publisher claims need correction.

## Verify the public release

Check the PyPI JSON endpoint for the new version and exactly 17 files. In a fresh
virtual environment install from the public index with cache disabled:

```text
python -m pip install --no-cache-dir --index-url https://pypi.org/simple foton-daylight==X.Y.Z
python -c "from foton import Engine; print(Engine().capabilities())"
```

Verify `foton.Engine is daylight_engine.Engine`, the imported version, a non-draft
GitHub Release, and 17 attached artifacts. If pip briefly lists only the old version,
wait for index-cache propagation and retry; do not republish.

## Recovery rules

- If artifacts fail before PyPI publication, fix the workflow on `main`; a rerun of a
  tag uses the workflow at the tagged commit.
- Before considering a tag move, verify both PyPI and GitHub Release are absent. Ask
  for explicit approval before deleting or force-moving any tag.
- If PyPI succeeds but GitHub Release creation fails, do not rebuild or republish.
  Fix the workflow and create the GitHub Release from the retained run artifacts.
- After publication, report the version, commit, tag, workflow URL, PyPI URL, GitHub
  Release URL, artifact count, and final verification result.
