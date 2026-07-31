---
name: foton-release-pipeline
description: Build, publish, verify, and recover Foton's maturin-based Python releases across Linux, Windows, Apple Silicon, and Intel macOS. Use when changing pyproject metadata, wheel matrices, PyPI trusted publishing, version tags, GitHub Releases, package naming, public imports, or release CI.
---

# Foton Release Pipeline

Treat the PyPI distribution, Python import, Rust extension, and compatibility import as
separate contracts:

- Distribution: `foton-daylight`
- Public import: `foton`
- Compatibility import: `daylight_engine`
- Native extension: `daylight_engine._native`

Preserve both packages in `tool.maturin.python-packages`. Verify that
`foton.Engine is daylight_engine.Engine` after every packaging change.

## Release Gates

1. Keep `pyproject.toml`, `CHANGELOG.md`, and tag `vX.Y.Z` aligned.
2. Run CI on Rust 1.85 and Python 3.10–3.13 before tagging.
3. Build wheels for Linux, Windows, Apple Silicon macOS, and Intel macOS.
4. Install and import every wheel before uploading it.
5. Build an sdist and confirm it can rebuild a wheel.
6. Publish through PyPI trusted publishing only after all artifacts pass.
7. Create the GitHub Release only after PyPI succeeds.

Use `manylinux: "2014"` and an explicit Linux interpreter such as `python3.13`.
Set `MACOSX_DEPLOYMENT_TARGET=11.0` before compiling macOS wheels:
`shaderc-sys` builds glslang with `std::filesystem`, which is unavailable under the
10.12 target selected by some Intel Python installations.

The GitHub Release job must check out the repository before running
`gh release create --verify-tag`; downloaded artifacts alone do not provide Git
repository context.

## Trusted Publisher

Configure the pending PyPI publisher for a first release with these exact claims:

- Project: `foton-daylight`
- Owner: `snjsomnath`
- Repository: `foton`
- Workflow: `release.yml`
- Environment: `pypi`

Keep `environment: pypi` and `permissions: id-token: write` on the publish job. An
`invalid-publisher` OIDC error means the account-side publisher does not match these
claims; do not replace OIDC with a stored password as the first fix.

## Recovery

- If artifacts fail before PyPI publication, fix the workflow on `main`. A tag-triggered
  rerun still uses the workflow at the tagged commit.
- Before moving a failed tag, verify that the PyPI version and GitHub Release are both
  absent. Rewriting a published tag is prohibited.
- If PyPI succeeds but GitHub Release creation fails, do not rebuild or republish.
  Fix the workflow for future tags and create the release from the retained run
  artifacts.
- Request explicit approval before deleting or force-moving a tag.

## Final Verification

Create a clean virtual environment and run:

```text
python -m pip install foton-daylight==X.Y.Z
python -c "from foton import Engine; print(Engine().capabilities())"
```

Verify the PyPI JSON endpoint, a non-draft GitHub Release, and 17 attached artifacts
for the current 16-wheel plus sdist matrix.
