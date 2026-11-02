# Purpose and plan

Last revised 2 November 2026. This page states what Foton is for and what has to
happen next. Where it disagrees with [release readiness](release-readiness.md),
this page wins; that document describes a public-release qualification process
that is heavier than the current goal.

## Purpose

Foton exists to compute daylight metrics for teaching, fast enough to use
interactively. Concretely:

- **Metrics:** daylight factor (DF), daylight autonomy (DA), useful daylight
  illuminance (UDI) and static spatial daylight autonomy (sDA).
- **Scope:** single zones, usually several at once, with diffuse surfaces, thin
  glass and static shading. The room types and conditions are the ones used in
  daylighting courses, not arbitrary project models.
- **Speed:** near real time, so that a slider in Grasshopper or the viewer gives
  an answer while the student is still looking. Speed is the reason the engine is
  written in Rust and runs on the GPU.
- **Platforms:** macOS (Metal), Windows and Linux (Vulkan), with a CPU reference
  backend that gives the same answer slowly.
- **Reference:** Radiance. Foton is correct when it agrees with Radiance on the
  scenes above; it does not try to reproduce Radiance's full material model.

Out of scope for now: BSDF and dynamic shading, glare and ASE, compliance
certification, and real project models with arbitrary materials.

## Where it stands

The engine's core physics is sound: sky patch layout, solid angles, cosine
sampling, estimator weights and the thin-glass model match Radiance on inspection,
and the Metal, Vulkan and CPU implementations agree with each other.

Speed is already sufficient. On an M4 Pro a 216-sensor room traces in about 6 ms
at 4,096 samples and 2 bounces, against about 3.5 s for Radiance. Raising the
bounce count to what accuracy needs stays well under 100 ms.

Accuracy on the full corpus is not yet established. Until 2 November 2026 the
default and validated setting was **one diffuse bounce**, while the Radiance
reference uses eight; the only recorded comparison (15 September 2026, two
scenes) showed Foton 17.6% low on full transport for that reason, and the one
full campaign (18 September) was lost with its temporary directory. Step 1 below
fixed the default; the corpus-wide campaign (step 3) has not been rerun since.

## Plan

Steps are in order; each should be finished before the next starts.

### 1. Make the bounce count match the physics

The cost side is already measured. Metal, M4 Pro, 4,096 samples, MF:2, wall
time per analysis and total coefficient energy relative to one bounce:

| Scene | Sensors | 1 bounce | 2 | 4 | 6 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| black_open | 36 | 1.8 ms / 1.000 | 1.9 / 1.000 | 1.8 / 1.000 | 1.8 / 1.000 | 1.8 / 1.000 |
| coloured_glass | 36 | 2.3 ms / 1.000 | 3.3 / 1.113 | 2.8 / 1.193 | 3.3 / 1.211 | 3.7 / 1.216 |
| dark_interior | 36 | 2.1 ms / 1.000 | 2.6 / 1.006 | 2.9 / 1.006 | 2.8 / 1.006 | 3.0 / 1.006 |
| deep_reflective | 72 | 2.4 ms / 1.000 | 2.7 / 1.296 | 3.1 / 1.744 | 3.5 / 2.062 | 3.9 / 2.283 |
| interior_glazing | 72 | 3.4 ms / 1.000 | 3.7 / 1.111 | 4.3 / 1.188 | 4.8 / 1.206 | 5.4 / 1.210 |

Eight bounces cost about 1.5 times one bounce and nothing exceeds 6 ms, so speed
does not constrain the choice. The coloured-glass room gains 21.6% energy from
one to eight bounces, which is the September deficit (1/1.216 = 0.82). The
bright deep room is still gaining 10% between six and eight bounces, so the
eight-bounce Radiance reference itself may not be converged there; the sweep
below must check that before trusting it.

**Done 2 November 2026** with `scripts/bounce_sweep.py`; results in
[`validation/results/2026-11-02-bounce-sweep/`](../validation/results/2026-11-02-bounce-sweep/README.md)
(Radiance 5.4a, `-ad 40000`, MF:1, six scenes, bounces 1/2/4/6/8/12).

- Foton at *n* bounces matches Radiance at *n* material bounces to within 0.5%
  on every lit scene, so the bounce semantics agree and the one-bounce deficit
  is purely truncation: −18% on the coloured-glass and interior-glazing rooms,
  −57% on the bright deep room, −0.7% on the dark room.
- Against a 12-bounce Radiance reference, 8 bounces is within −0.3% to −0.5%
  on the glazed rooms and −0.05% on the dark room, at ≈1.5× the one-bounce
  trace time (all under 6 ms). **`DEFAULT_MAXIMUM_BOUNCES = 8`** is now the
  default in `annual.py`, `protocol.py`, the CLI, `honeybee_foton.client`,
  the PyO3 `analyze` signature and both validation scripts.
- Open: the bright deep room (`deep_reflective`, 12 m, high reflectance) is not
  converged at 12 bounces in either engine, and at 12 bounces Foton sits +7%
  above Radiance while agreeing with it at 8. Something in how the two engines
  terminate deep paths differs; it only shows in a scene well outside teaching
  reflectances, and is tracked under "Smaller known issues".
- Sealed and open-aperture rooms have no reflected light; their indirect-error
  columns in the sweep are noise over a zero reference.

### 2. Two cheap robustness fixes

**Done 2 November 2026.**

- The adapter keeps geometry and sensors in world coordinates as float64 and
  recentres them on `scene_origin` (whole-metre bounding-box midpoint) when the
  native scene is created, so a model at a SWEREF99 northing of 6.4 million
  traces identically to the same room at the origin. Radiance comparisons keep
  using the world arrays. `scene_origin_m` is recorded in `geometry_info`.
- Both GPU backends split the diffuse trace into sample tiles of at most 2^22
  sensor×sample paths, checking cancellation between tiles; the per-path weight
  uses the total sample count so results are unchanged. Scenes under about
  1,000 sensors at 4,096 samples still run as one dispatch.

### 3. One archived Metal campaign

Run the full suite once on Metal from a clean commit, with output under
`validation/results/<date>-<label>/`. Keep the JSON and Markdown reports in the
repository and the bulk oracle matrices in a compressed archive next to them.
This is the first parity evidence tied to a commit.

**In progress, 2 November 2026.** A first run from commit `2621348` marked every
scene `unstable_reference` within a minute: the suite's depth-stability check
compared Radiance at 4 and 8 bounces, which differ by about 2% from physics
alone. The levels are now `(20000,1)`, `(40000,8)`, `(40000,12)`, `(80000,12)`
with the 12-bounce mean as reference. The campaign was restarted on suite
version 4 (106 scenes, teaching category included) with 12 Radiance workers into
`validation/results/2026-11-02-architectural-v4-metal/`. Raw stage folders are
ignored by git; only the report, suite and comparison JSON/Markdown are tracked.

### 4. Decide direct sun

**Decided 2 November 2026: version 0.3 is two-phase only.** Foton is a sky-patch
method with no separate sun. That is correct for DF and for coefficient parity
against `rfluxmtx`; DA, UDI and sDA depend on direct sun, which Honeybee's
annual recipe traces separately, so those metrics will differ from Honeybee in
sunny climates (patch-smeared sun under-states peak illuminance and spreads it
across neighbouring sensors). The README states this under "What it does not
do". A direct-sun pass (sun-position coefficients, as in the 2-phase DDS or
Honeybee's enhanced 2-phase) is the first feature after parity, not a blocker
for it; the teaching use is mostly overcast-sky and relative comparisons.

### 5. Teaching fixtures

**Done 2 November 2026 (suite version 4).** The 90 earlier scenes test physical
interactions well but are weighted toward a footprint-by-window-shape matrix
(47 of 90) whose window shapes teach little. `validation/scenes.py` now adds a
`teaching` category of 16 single-parameter sweeps on a 6 × 6 × 3 m base:
WWR 20/40/60 %, depth 4/6/8/10 m, reflectance 0.3/0.5/0.7, overhang 0.5/1.0 m,
obstruction 30/60°, and a classroom, an open-plan office and a living room.
They run under the same gates with `--category teaching`. The window-shape
matrix is kept for continuity with the 2026-11-02 campaign.

Still to do: climates. The suite runs one EPW (Gothenburg). Add one sunny and
one overcast EPW and run the teaching category under each; this is the only
place the direct-sun decision (step 4) is quantified.

### 6. Vulkan and Linux

Repeat step 3 on a Windows or Linux machine with a Vulkan 1.3 GPU. Until then
Vulkan is "built and unit-tested", not "validated".

## Smaller known issues

Not blocking; fix opportunistically.

- Sky light reaching a sensor by specular reflection off glass is never counted;
  Radiance counts it. Small, mainly in scenes with glazed neighbours.
- `convergence` in result metadata is hard-coded to 1.0 and nothing measures it.
- The README calls MF:2-to-Tregenza aggregation "exact"; about 32% of the solid
  angle lands outside the mapped parent. Only tests use the aggregation.
- The daylight-factor outdoor reference is 0.44% high on Tregenza.
- Only 16 Sobol dimensions exist, so paths beyond bounce 7 reuse dimensions.
  With the default now at 8 bounces this is live; the sweep shows no visible
  bias from it at 8, but 12 bounces diverge from Radiance by +7% in the bright
  deep room, and dimension reuse is the first suspect.
- The resident-scene cache can store old geometry under a new revision if an
  update races an analysis, and entries are never evicted.
- Transport logic is written three times (MSL, GLSL, Rust). Every fix above has
  to be made in all three.
