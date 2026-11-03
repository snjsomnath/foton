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

A GPU host without the cores for the Radiance oracle (a cloud GPU with two
vCPUs) can be judged against the converged references of a finished campaign.
`python scripts/export_reference_bundle.py <campaign> --output <bundle>`
collects each case's converged full, integrated-direct and one-bounce
references with their stability verdicts, and `--reuse-references <bundle>`
makes the suite compare the candidate against them instead of rerunning
Radiance. The references describe the scene, not the engine, so nothing about
what is judged changes: the run still exports the scene, audits the sky bins,
prepares the weather and runs the stock recipe through Radiance. It refuses a
bundle from a smoke, dirty or different-corpus run and refuses any case whose
sensor grid or model summary differs from the reference's. `suite.json` and
every report name the source campaign and commit under `reference_source`, and
the release verifier prints it.

The [106 architectural scenes](../validation/architectural-scenes.md) cover controls,
room form, orientation, openings, shading, context, materials, room connections,
and the original acceptance HBJSON. The original ten identifiers remain, with
96 additional procedural fixtures including courtyard rooms, a rooflit atrium
feeding two storeys, serial glazing, louvres, light shelves and deep reveals.
Generated [HBJSON samples](../test_models/architectural/README.md) include a hash
manifest and a per-scene architectural question. The open-aperture fixture removes
glazing in both independent exports. It is a transport test, not a newly supported
Honeybee material.

Each scene runs in both sky bases (212 required cases), under uniform, overcast,
horizon-weighted and four cardinal-direction controlled skies, then Gothenburg
annual weather (`--weather epw/phoenix.epw` or `epw/seattle.epw` substitutes
a sunny or an overcast climate; the teaching category has been run under
both). Four Radiance replicates are
evaluated at each of `(ad=20000,bounces=1)`, `(40000,8)`, `(40000,12)`, `(80000,12)`,
with four more replicates added (up to twelve) while a level's replicate halves
disagree; the 12-bounce mean is the reference. Direct integration doubles its
samples per patch from 256 up to 16,384 until two successive levels agree. Depth stability compares 8 with 12 bounces
and sampling stability 40,000 with 80,000 ambient divisions;
each reference level also checks replicate-half stability (the one-bounce level
is a diagnostic only). Stability RMS gates are 5% at MF:1 and 10% at MF:2, where
the same ray budget covers four times as many bins; energy gates do not change.
References that are physically dark (a grid whose hourly illuminance averages
under 1 lux and never exceeds 10 lux in either engine: sealed rooms, windowless
rooms in multi-room models), skies a room cannot see, controlled skies worth
under 0.5% of the uniform-sky light, and indirect stages below 0.5% of direct
energy count as agreement rather than as relative error over noise; their
errors are still recorded. The indirect stage's RMS error is normalised by the
full coefficients it contributes to, so a rooflit room's small, noisy reflected
component is judged by its effect on the result; its energy bias gate (3%) is
unchanged. Radiance-versus-Radiance stability also waives differences below
1e-4 summed coefficient energy per sensor. Controlled-sky scatter is normalised
to the uniform-sky level for the same reason; each sky's bias gate stays at 5%. sDA ignores sensors whose reference DA lies within
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
The suite runs the `final` quality preset as users get it: 256 direct samples
per patch, 65,536 indirect samples at MF:1 and 262,144 at MF:2 (the budget
scales with the patch count so per-patch noise, and with it hourly
illuminance error, is the same at both densities), eight bounces. The preset
must pass these gates before it can be advertised as validated. The two
archived Metal campaigns (176 and then 204 of 212 cases) are summarised in
[purpose and plan](purpose-and-plan.md); the eight open cases are named there.

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

## Release evidence lives in the repository

Publication is gated on evidence committed under `validation/results/` and
named in `validation/release-evidence.json`, which
`scripts/verify_release_evidence.py` checks on every release tag (the
`acceptance` job of `release.yml`, on a hosted runner, needs no GPU). It
requires:

- one complete, clean, non-smoke run of the corpus for the **Metal** backend
  on macOS and one for the **Vulkan** backend on Windows or Linux, each
  recording the wheel version being released and GPU execution on every case;
- every case outside the gates to be named in
  `validation/known-open-cases.json` with its result class, a reason and a
  pointer to where it is documented; an execution error is never an open case;
- at least one live Rhino 8 checklist (`validation/rhino-evidence.example.json`
  filled in): install the user objects, open the example, run, cancel, rerun,
  change inputs, upgrade invalidates reuse, reload moved results, Honeybee
  metrics, Ladybug heatmap, with a date and reproduction notes;
- each evidence file to carry the release commit, or an ancestor of it whose
  difference to the release commit touches only `validation/results/`, the two
  evidence manifests, `docs/`, `README.md`, `CHANGELOG.md` and `epw/README.md`.
  Anything that changes the engine, the scenes or the suite invalidates the
  evidence and the suite must run again.

The verifier prints which backend ran on which system and device and which
Rhino version was exercised; the release notes state exactly those
combinations as tested and everything else as unverified. The
`Public beta acceptance` workflow (`workflow_dispatch`) can produce a suite on
a registered self-hosted GPU runner, but a run on any machine with Radiance
and the GPU, committed under `validation/results/`, is equally valid evidence.

## Launch checklist

- `scripts/verify_release_evidence.py` passes for the release commit and version.
- Downloadable components open and run without script editing in the Rhino 8
  that the evidence names.
- Historical 0.1.0 benchmarks clearly labelled; no unverified accuracy or speed claims.
- Known limitations, tested hardware, installation guidance, and reporting instructions published.
