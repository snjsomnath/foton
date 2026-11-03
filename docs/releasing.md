# Release Process

The published distribution is `foton-daylight`; users import it as `foton`.

## Repository setup

1. Create or connect the GitHub repository.
2. Push this source tree, including `.github/workflows/`.
3. Create a protected GitHub environment named `pypi`.
4. On PyPI, create a pending trusted publisher for distribution
   `foton-daylight`.
5. Configure the publisher with the GitHub owner, repository, workflow filename
   `release.yml`, and environment `pypi`.

The release workflow requests `id-token: write` only in the publish job. No long-lived
PyPI token is required.

## Release checklist

1. Update the workspace and Python versions.
2. Add release notes to `CHANGELOG.md`.
3. Run the local validation:

   ```bash
   cargo fmt --all -- --check
   cargo test --workspace
   python -m pytest tests/python
   cd viewer && npm ci && npm test -- --run && npm run build
   ```

4. Build and inspect a local artifact:

   ```bash
   maturin build --release --out dist
   python -m pip install --force-reinstall dist/*.whl
   python -c "from foton import Engine; print(Engine().capabilities())"
   ```

5. Push an annotated tag matching the package version:

   ```bash
   git tag -a v0.3.0 -m "Foton 0.3.0"
   git push origin v0.3.0
   ```

The tag starts the wheel matrix, the Grasshopper packaging and the evidence
check. Publication requires all distributions, the Grasshopper package and
`scripts/verify_release_evidence.py` to pass for the tagged commit; run it
locally first:

   ```bash
   python scripts/verify_release_evidence.py --commit "$(git rev-parse HEAD)" --version 0.3.0
   ```

## Name ownership

The exact PyPI project name `foton` belongs to another publisher. Do not upload this
project under that name unless ownership has been formally transferred on PyPI.

## Public-beta acceptance gate

Read [release readiness](release-readiness.md) before tagging. Publishing
requires committed, release-commit numerical suites for Metal and Vulkan, a
live Rhino 8 checklist, a named list of any cases outside the gates, and a
source-matched Grasshopper download. Produce the suites with
`scripts/validate_release_suite.py` on the release commit after the version
bump, commit their reports under `validation/results/`, name them in
`validation/release-evidence.json`, then tag the commit that adds them.
