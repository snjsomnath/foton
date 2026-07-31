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
   git tag -a v0.1.0 -m "Foton 0.1.0"
   git push origin v0.1.0
   ```

The tag starts the wheel matrix. Publication happens only after every wheel and source
distribution has been built and uploaded as workflow artifacts.

## Name ownership

The exact PyPI project name `foton` belongs to another publisher. Do not upload this
project under that name unless ownership has been formally transferred on PyPI.
