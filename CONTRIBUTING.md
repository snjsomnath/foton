# Contributing

Use Python 3.10 or newer, Rust 1.85 or newer, and Node.js 20 or newer.

```bash
python -m pip install -e ".[honeybee,viewer,test]"
cargo test --workspace
python -m pytest tests/python
cd viewer && npm ci && npm test -- --run
```

Keep changes focused and preserve backend parity. Transport changes should be validated
in this order: direct visibility, full coefficients, then annual illuminance and
metrics. GPU-specific integration tests should skip cleanly when compatible hardware
is unavailable.

## Adding your computer to the benchmarks

Speed results from more GPUs make the README's speed table more useful. A run
takes a few minutes and changes nothing outside `benchmarks/machines/`.

You need a Metal GPU (any Apple silicon Mac) or a Vulkan GPU (NVIDIA, AMD or
Intel with current drivers). Laptops should be plugged in.

1. Fork the repository on GitHub, clone your fork, and make a branch:

   ```bash
   git clone https://github.com/<your-name>/foton.git
   cd foton
   git checkout -b benchmark-<your-gpu>
   ```

2. Install Foton from the checkout with the Honeybee extra:

   ```bash
   python -m pip install -e ".[honeybee,test]"
   ```

   Check that Foton sees your GPU and not just the CPU fallback:

   ```bash
   python -c "from foton import Engine; print(Engine().capabilities())"
   ```

3. Close other heavy programs, then run the suite and rebuild the table:

   ```bash
   python scripts/benchmark_suite.py
   python scripts/compare_benchmarks.py --write
   ```

   Add `--label "on battery"` (or any short note) if the setup is unusual.
   Don't use `--quick` for a submission: quick runs are left out of the table.

4. Check what changed. You should see one new JSON file under
   `benchmarks/machines/<machine-id>/` and an updated
   `benchmarks/machines/README.md`. The JSON file records your OS, CPU, GPU,
   driver, RAM, Python and Foton versions, and your computer's network name
   (`hostname`). If you'd rather not share that name, replace it in the file
   with something like `"my-laptop"` before you commit.

5. Commit those two files, push, and open a pull request against `main`
   titled "Benchmark: <your CPU and GPU>".

Please don't edit the README speed table yourself. The maintainer refreshes
it from `benchmarks/machines/` with `scripts/refresh_readme_speed.py`.
[docs/benchmarking.md](docs/benchmarking.md) explains what each benchmark
measures.

## Opening a pull request

1. Branch from `main` and keep each pull request to one change.
2. Run the checks at the top of this page for the parts you touched. CI runs
   on several operating systems and is slow, so please test locally first.
3. If the change affects users, add a short line under `## Unreleased` in
   `CHANGELOG.md`.
4. In the description, say what changed, why, and how you tested it. For
   changes to light transport or results, include before and after numbers
   from the validation suite ([docs/release-readiness.md](docs/release-readiness.md)).
5. Changes to the Grasshopper component sources need the `.ghuser` files
   rebuilt in Rhino 8 with `scripts/build_grasshopper.py`. If you can't run
   Rhino, say so in the pull request and the maintainer will rebuild them.
