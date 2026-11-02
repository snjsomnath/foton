# Public beta release readiness

Current status: **implementation available for testing; validated launch blocked**.
See the [15 September diagnostics](../validation/results/2026-09-15-readiness/README.md)
for live Rhino results and unresolved numerical evidence.

## Supported scope

| Capability | Beta scope |
| --- | --- |
| Grasshopper | Rhino 8 Windows and macOS; external CPython bridge |
| Materials | Diffuse Plastic and thin Glass, index 1.52 |
| Metrics | DA, cDA, UDI bands, static area-weighted sDA |
| Weather | Hourly 8,760-step EPW/WEA; Radiance 6 sky generation |
| Sky bases | Tregenza 146 and Reinhart MF:2 578, including ground |
| Excluded | Dynamic apertures/shades, BSDF, ASE, glare, compliance certification |
| Hardware evidence | Publish actual tested device/driver combinations; other devices remain unverified |

## Reproducible numerical evidence

Install the current wheel plus `honeybee`, `test`, `lbt-recipes==0.28.8`, and
`setuptools`. From a clean checkout run:

```bash
python scripts/validate_release_suite.py --backend metal --output artifacts
# On a Windows machine with a compatible GPU:
python scripts/validate_release_suite.py --backend vulkan --output artifacts
```

The output directory must be new. The command writes `suite.json`, `suite.md`,
per-scene reports, model inputs, coefficient matrices, Radiance commands and versions,
convergence diagnostics, annual metrics, and hardware/driver details. An error in
one case is recorded and the remaining cases are attempted. All commands return
nonzero unless the complete, clean-checkout GPU suite passes.

Use `--scene sealed --sky-density 1 --smoke` for a fast diagnostic, or
`--backend reference` without a GPU. Partial, smoke, CPU, dirty-checkout, and unstable
oracle runs are explicitly **incomplete** and cannot qualify a release.

The [90 architectural scenes](../validation/architectural-scenes.md) cover controls,
room form, orientation, openings, shading, context, materials, room connections,
and the original acceptance HBJSON. The original ten identifiers remain, with
40 additional procedural fixtures including courtyard rooms, a rooflit atrium
feeding two storeys, serial glazing, louvres, light shelves and deep reveals.
Generated [HBJSON samples](../test_models/architectural/README.md) include a hash
manifest and a per-scene architectural question. The open-aperture fixture removes
glazing in both independent exports. It is a transport test, not a newly supported
Honeybee material.

Each scene runs in both sky bases (180 required cases), under uniform, overcast,
horizon-weighted and four cardinal-direction controlled skies, then Gothenburg
annual weather. Four Radiance replicates are
evaluated at each of `(ad=20000,bounces=1)`, `(40000,8)`, `(40000,12)`, `(80000,12)`;
the 12-bounce mean is the reference. Depth stability compares 8 with 12 bounces
and sampling stability 40,000 with 80,000 ambient divisions;
each reference level also checks replicate-half stability (the one-bounce level
is a diagnostic only). Stability RMS gates are 5% at MF:1 and 10% at MF:2, where
the same ray budget covers four times as many bins; energy gates do not change.
References that are physically dark (sealed rooms), skies a room cannot see, and
indirect stages below 0.5% of direct energy count as agreement rather than as
relative error over noise. sDA ignores sensors whose reference DA lies within
5 pp of the 50% threshold and allows one sensor's share on small grids.
Direct integration uses independent
stratified sky samples at 256 and 1,024 samples per patch, not the native sampler.
Failure to establish stability is inconclusive, never evidence that Foton passed.
Use `--category shading` or repeated `--scene` arguments to diagnose an interaction.
The full converged suite is computationally expensive; the acceptance workflow
allows up to 24 hours per platform, and actual duration depends on hardware.

Release gates use per-grid coefficient bias/RMS-normalized error limits of
2%/5% direct, 3%/10% indirect, and 5%/10% full transport. Annual illuminance uses
5% absolute bias and 10% CV(RMSE); metric mean absolute errors and sDA differences
must be below 2 percentage points. The sealed-room absolute limit is 0.000001 lux.
Official Honeybee reload must agree within 0.05 percentage points. Error
percentiles and worst locations remain visible alongside aggregate scores.

The stock Honeybee acceptance comparison and performance data are separate from
numerical correctness. A 10x speed target is a performance diagnostic, not an
accuracy gate. Compare cold with cold and cached with cached at comparable accuracy.
The existing final quality preset remains unchanged and must pass these gates
before it can be advertised as validated.

## Grasshopper artifact build

In Rhino 8, run `scripts/build_grasshopper.py` using `_RunPythonScript`. This creates
three actual `.ghuser` files and `.gh`/`.ghx` examples, reloads them through
Grasshopper's archive API, and records source and artifact hashes under
`grasshopper_foton/distribution`. It does not install user objects or replace the
active definition. Then run:

```bash
python scripts/package_grasshopper.py
```

The packager refuses missing or stale components. Rebuild them after changing
component, bridge, or builder sources. Commit the generated artifacts with their
manifest before a release; upload the resulting versioned ZIP as the release asset.

## Required live acceptance

Use a fresh CPython environment and Rhino 8 profile on each target OS. Record the
exact commit, wheel, Rhino version, OS, device/driver, date, and reproduction notes.
Copy `validation/rhino-evidence.example.json` outside the checkout and mark only
scenarios actually verified: install, open example, run, cancel, rerun, change
inputs, upgrade/reuse invalidation, move/reload results, HB metrics, and LB heatmap.

The acceptance workflow requires trusted self-hosted runners labelled
`foton-metal` (macOS ARM64) and `foton-vulkan` (Windows X64), with Radiance 6 on PATH.
Set `FOTON_RHINO_EVIDENCE` in each runner environment to its current-commit live
acceptance JSON. GPU tests fail when explicitly requested hardware is unavailable.
Publishing waits for both targets and the source-matched Grasshopper package.
Missing runners or missing evidence block the release; they do not justify bypassing it.

## Launch checklist

- Current-commit complete passing reports for both GPU platforms.
- Downloadable components open and run without script editing on both Rhino targets.
- All live acceptance scenarios completed with retained evidence.
- Historical 0.1.0 benchmarks clearly labelled; no unverified accuracy or speed claims.
- Known limitations, tested hardware, installation guidance, and reporting instructions published.
