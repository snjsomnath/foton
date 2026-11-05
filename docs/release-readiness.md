# Release readiness

Foton 0.3.0 was released on 3 November 2026. This page covers what a release
supports, how the accuracy evidence is produced and checked, and what to tick
off before the next release. The platforms tested for 0.3.0 are listed under
[Tested platforms for 0.3.0](#tested-platforms-for-030).

The [15 September diagnostics](../validation/results/2026-09-15-readiness/README.md)
are kept for history. They were taken before the fixes that went into 0.3.0.

## Supported scope

| Capability | Beta scope |
| --- | --- |
| Grasshopper | Rhino 8 Windows and macOS; external CPython bridge |
| Materials | Diffuse Plastic and thin Glass, index 1.52 |
| Metrics | DA, cDA, UDI bands, static area-weighted sDA |
| Weather | Hourly 8,760-step EPW/WEA; Foton's built-in Perez all-weather sky (Radiance's `gendaymtx` optional, used as the validation oracle) |
| Sky bases | Tregenza 146 and Reinhart MF:2 578, including ground |
| Excluded | Dynamic apertures/shades, BSDF, ASE, glare, compliance certification |
| Hardware evidence | Publish actual tested device/driver combinations; other devices remain unverified |

## Reproducible numerical evidence

Install the current wheel plus `honeybee`, `test`, `lbt-recipes==0.28.8`, and
`setuptools`, with Radiance 5.4a available (the suite needs it for its
references, its sky-bin audit and as the oracle for the built-in sky; users
do not). From a clean checkout run:

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

The bundles live as GitHub release assets, one per scene corpus version, since
the repository cannot hold the arrays. For corpus version 4:

```bash
gh release download references-corpus4-2026-11-03 --repo snjsomnath/foton --pattern '*.zip'
```

```bash
shasum -a 256 foton-references-corpus4-2026-11-03.zip  # de4be5a59e4b694d0c9f8f5ef697649527e45dd231d9794b23ff7a9f8038417b
```

```bash
unzip foton-references-corpus4-2026-11-03.zip -d ../references
```

```bash
python scripts/validate_release_suite.py --backend vulkan --workers 2 --reuse-references ../references/foton-references-corpus4-2026-11-03 --output validation/results/<date>-architectural-v4-vulkan-<machine>
```

The bundle was exported from the Metal campaign of 3 November 2026 at commit
f65030f (its [README](../validation/results/2026-11-03-architectural-v4-metal-0.3.0/README.md)
names the eight open cases a reusing run should expect). Keep it outside the
checkout so the run stays clean. When the corpus changes, the first campaign
pays for Radiance once and a new bundle is published next to it.

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
both). Foton's annual run uses its own Perez sky; the Radiance side of the
annual comparison keeps `gendaymtx`'s. Each case report records both sources
under `sky_sources` with the largest per-hour relative difference between
the two matrices, and `tests/python/test_builtin_sky.py` holds the
floating-point comparison itself (a committed `gendaymtx` golden file for
CI, the whole year live when Radiance is installed). Four Radiance replicates are
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
  evidence manifests, `docs/`, `README.md`, `CHANGELOG.md`, `epw/README.md`,
  the verifier itself, `tests/` and `.github/`. A backend's suite also
  tolerates changes to the other backend's crate, and the Rhino checklist
  tolerates changes to `validation/` and the suite scripts, which it never
  runs. Anything that changes the engine, the scenes or the suite a piece of
  evidence depends on invalidates it and that suite must run again (against
  the published reference bundle, minutes rather than hours).

The verifier prints which backend ran on which system and device and which
Rhino version was exercised; the release notes state exactly those
combinations as tested and everything else as unverified. The
`Public beta acceptance` workflow (`workflow_dispatch`) can produce a suite on
a registered self-hosted GPU runner, but a run on any machine with Radiance
and the GPU, committed under `validation/results/`, is equally valid evidence.

### Tested platforms for 0.3.5

0.3.5 changes only the Grasshopper components, so it reuses the 0.3.3 GPU
suites.

| Evidence | Platform | Result |
| --- | --- | --- |
| [Metal suite](../validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/README.md) | Apple M4 Pro, macOS 26.6, Radiance 5.4a | reused from 0.3.3 |
| [Vulkan suite](../validation/results/2026-11-04-architectural-v4-vulkan-t4-0.3.3/README.md) | NVIDIA Tesla T4, Linux (Google Colab), Radiance 5.4a | reused from 0.3.3 |
| [Rhino 8 checklist](../validation/results/2026-11-05-rhino-macos-0.3.5/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios, plus flipping `_run` during a run |

### Tested platforms for 0.3.4

0.3.4 changes only the Grasshopper components, so it reuses the 0.3.3 GPU
suites.

| Evidence | Platform | Result |
| --- | --- | --- |
| [Rhino 8 checklist](../validation/results/2026-11-04-rhino-macos-0.3.4/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios |
| Windows volunteer, 2026-11-05 | Rhino 8, Windows, Vulkan (GPU and system details to follow) | checked by a volunteer, not a full validation: Package Manager install, `install_` (about 1.5 minutes), Check selects Vulkan, the example and the volunteer's own room run. Flipping `_run` during a run showed "object expired during a solution", fixed in 0.3.5. The Python install and the benchmark are not done yet. |

### Tested platforms for 0.3.3

| Evidence | Platform | Result |
| --- | --- | --- |
| [Metal suite](../validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/README.md) | Apple M4 Pro, macOS 26.6, Radiance 5.4a | 204 of 212, the eight documented open cases; coefficients and annual results identical to 0.3.2 |
| [Vulkan suite](../validation/results/2026-11-04-architectural-v4-vulkan-t4-0.3.3/README.md) | NVIDIA Tesla T4, Linux (Google Colab), Radiance 5.4a | 204 of 212, the same eight; coefficients and annual results identical to 0.3.2 |
| [Rhino 8 checklist](../validation/results/2026-11-04-rhino-macos-0.3.3/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios; installed through the Package Manager package, with the background install_ |

### Tested platforms for 0.3.2

| Evidence | Platform | Result |
| --- | --- | --- |
| [Metal suite](../validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/README.md) | Apple M4 Pro, macOS 26.6, Radiance 5.4a | 204 of 212, the eight documented open cases; coefficients and annual results identical to 0.3.1 |
| [Vulkan suite](../validation/results/2026-11-04-architectural-v4-vulkan-t4-0.3.2/README.md) | NVIDIA Tesla T4, Linux (Google Colab), Radiance 5.4a | 204 of 212, the same eight; coefficients and annual results identical to 0.3.1 |
| [Rhino 8 checklist](../validation/results/2026-11-04-rhino-macos-0.3.2/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios, four components including live mode and daylight factor |

### Tested platforms for 0.3.1

| Evidence | Platform | Result |
| --- | --- | --- |
| [Metal suite](../validation/results/2026-11-03-architectural-v4-metal-0.3.1-release/README.md) | Apple M4 Pro, macOS 26.6, Radiance 5.4a | 204 of 212, the eight documented open cases; identical to 0.3.0 |
| [Vulkan suite](../validation/results/2026-11-03-architectural-v4-vulkan-t4-0.3.1/README.md) | NVIDIA Tesla T4, Linux (Google Colab), Radiance 5.4a | 204 of 212, the same eight; identical to 0.3.0 |
| [Rhino 8 checklist](../validation/results/2026-11-03-rhino-macos-0.3.1/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios |

### Tested platforms for 0.3.0

| Evidence | Platform | Result |
| --- | --- | --- |
| [Metal suite](../validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/README.md) | Apple M4 Pro, macOS 26.6, Radiance 5.4a | 204 of 212, the eight documented open cases |
| [Vulkan suite](../validation/results/2026-11-03-architectural-v4-vulkan-t4/README.md) | NVIDIA Tesla T4, Linux (Google Colab), Radiance 5.4a | 204 of 212, the same eight; agrees with Metal within 0.008 pp of energy bias |
| [Rhino 8 checklist](../validation/results/2026-11-03-rhino-macos/README.md) | Rhino 8.35, macOS, Metal, Ladybug Tools 1.9.0 | all ten scenarios |
| [Reference campaign](../validation/results/2026-11-03-architectural-v4-metal-0.3.0/README.md) | Apple M4 Pro, 6.2 h with twelve Radiance workers | source of the published reference bundle |

Unverified: the Windows numerical suite and benchmark, Rhino on Windows beyond
the one volunteer check above, a fresh Rhino profile, any GPU other than the
two above.

## Launch checklist

- `scripts/verify_release_evidence.py` passes for the release commit and version.
- Downloadable components open and run without script editing in the Rhino 8
  that the evidence names.
- Older benchmark figures are labelled with their date and settings; no unverified accuracy or speed claims.
- Known limitations, tested hardware, installation guidance, and reporting instructions published.
