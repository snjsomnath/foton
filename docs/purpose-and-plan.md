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

Accuracy is not yet established, for one main reason: the default and validated
setting is **one diffuse bounce**, while the Radiance reference uses eight. With
0.5 reflectance one bounce captures roughly half of the reflected light. The
only recorded comparison (15 September 2026, two scenes) showed Foton 17.6% low
on full transport, consistent with that. The one full campaign (18 September)
was lost with its temporary directory before it was archived.

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

- Measure: run six scenes (sealed, open aperture, coloured glass, dark interior,
  bright deep room, one borrowed-light case) at 1, 2, 4, 6 and 8 bounces against
  the existing eight-bounce Radiance reference. Record error and trace time.
- Choose the lowest bounce count that passes the 5%/10% transport gates with
  margin, probably 4 to 6, and make it the `final` preset default.
- Remove every hard-coded `maximum_bounces=1`: the preset default in
  `python/daylight_engine/honeybee/annual.py`, the suite record in
  `scripts/validate_release_suite.py`, and the candidate trace in
  `scripts/validate_honeybee_coefficients.py`. The suite must validate whatever
  the preset is.
- Requires Radiance 6 on the machine running the sweep.

### 2. Two cheap robustness fixes

- Recentre geometry in the Honeybee adapter before the float32 cast. Models
  placed at real-world coordinates currently lose precision silently; at a
  SWEREF99 northing of 6.4 million the float32 spacing is 0.5 m.
- Split the GPU trace into tiles so cancellation works mid-run and Windows
  GPU timeouts cannot kill a long dispatch.

### 3. One archived Metal campaign

Run the full suite once on Metal from a clean commit, with output under
`validation/results/<date>-<label>/`. Keep the JSON and Markdown reports in the
repository and the bulk oracle matrices in a compressed archive next to them.
This is the first parity evidence tied to a commit.

### 4. Decide direct sun

Foton is a two-phase sky-patch method with no separate sun. That is correct for
DF and for coefficient parity against `rfluxmtx`, but DA, UDI and sDA depend on
direct sun, which Honeybee's annual recipe treats separately. For version 0.3
the documentation should state the two-phase scope plainly. A direct-sun pass is
a later feature, not a blocker for parity now.

### 5. Teaching fixtures

The 90 current scenes test physical interactions well but are weighted toward a
footprint-by-window-shape matrix (47 of 90) whose window shapes teach little.
Add a `teaching` category of roughly 15 to 20 scenes built as parameter sweeps:
window-to-wall ratio 20/40/60%, room depth 4/6/8/10 m, surface reflectance
0.3/0.5/0.7, overhang depth 0/0.5/1.0 m, obstruction angle 0/30/60°; three
named room types (classroom, open-plan office, living room); and three climates
beyond Gothenburg (one sunny, one overcast). Reduce the window-shape matrix to a
sample.

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
- The resident-scene cache can store old geometry under a new revision if an
  update races an analysis, and entries are never evicted.
- Transport logic is written three times (MSL, GLSL, Rust). Every fix above has
  to be made in all three.
