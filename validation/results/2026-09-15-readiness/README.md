# Public-beta readiness diagnostics — 15 September 2026

**Not release acceptance evidence.** These runs used a modified checkout of
Foton 0.2.0 on Apple M4 Pro (20 GPU cores), macOS 26.6.2, Metal, and Radiance
6.0.2. The retained reports include their base commit and settings. They cannot
qualify an immutable release commit.

## Rhino

[Live Rhino evidence](rhino-smoke.json) records seven passing checks in Rhino
8.35.26251.13002: packaged example execution, result reload, compatible reuse,
upgrade invalidation, changed-input recomputation, moved-result reload, and
external-process cancellation. The actual `.gh` and `.ghuser` files were built
and round-tripped through Grasshopper's archive API.

The live run exposed and fixed two IronPython differences: `communicate()` does
not populate `returncode`, and the .NET subprocess wrapper has no `terminate()`
or `kill()` method. The bridge now waits explicitly and uses the underlying
.NET process when required.

This used the existing Rhino profile. Fresh-install acceptance, a physical Escape
key cancellation check, and downstream Honeybee/Ladybug component wiring remain
to be verified on both target operating systems. Windows Vulkan is unverified.

## Numerical results

[Two-scene final-quality diagnostic](two-scene-final-diagnostic.json) retains the
full settings, commands and convergence evidence for the sealed and coloured-glass
rooms in MF:1. Both runs are **incomplete** because the Radiance reference did not
establish convergence.

The coloured-glass room nevertheless identifies a clear issue to investigate:
the current one-bounce preset gives full-transport bias of -17.604% and
RMS-normalized error of 22.330% against the eight-bounce reference. Annual bias
is -13.403% and CV(RMSE) is 19.410%. These exceed the intended 5%/10% gates.
The reference also changes by 1.978% bias between four and eight bounces,
exceeding its 1% convergence gate. A deeper reference is required before an
accuracy claim can be made.

The sealed Foton room is dark. Radiance produced small, inconsistent light leaks,
so relative-error percentages are unsuitable evidence of solver accuracy here.
The absolute darkness gate is retained. The diagnostic predates the tighter
1e-8 coefficient near-zero tolerance; its old coefficient pass flags must not be
used for acceptance.

The ten-scene smoke run exercised both sky bases. All nine procedural scenes
completed on Metal; the original acceptance-case stock comparison exposed an
unsupported recipe input, which was removed. The stock recipe uses MF:1
internally; this is recorded separately from the candidate sky basis. The
converged coefficient oracle still tests both MF:1 and MF:2.

After correcting the recipe invocation, the [pipeline rerun](pipeline-smoke.json)
completed the sealed and 2,020-sensor acceptance scenes in both sky bases on
Metal, including cold/cached annual runs, independent sky-bin audits, stock
Honeybee comparison, and official metric reload. Together with the preceding
procedural run, all ten scenes have been exercised in both bases. These were
multiple diagnostic invocations, not one passing release suite.

## Required before validated launch

- Establish a stable full-transport Radiance reference, including sealed-room behavior.
- Select and verify a final bounce/sample budget against all ten scenes and both bases.
- Complete numerical parameter sweeps for rotation, units, ordering, sensor areas,
  and schedules; current contract tests do not replace these end-to-end comparisons.
- Run the full suite on Metal and a named Windows Vulkan GPU.
- Complete fresh-install Rhino acceptance and downstream component connections on both OSes.
- Configure trusted GPU runners and retain passing evidence for the release commit.

See [release readiness](../../../docs/release-readiness.md) for commands and gates.
