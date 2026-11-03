# Architectural corpus v3: Metal diagnostic campaign

The corpus implementation and local test checks are complete. **The full Metal
campaign is still running; this is not a completed campaign or release approval.**
The live report accounts for completed comparisons without treating unstable
Radiance references as numerical passes or confirmed solver failures.

## Completed implementation checks

- 90 deterministic HBJSON models: the existing 50 plus the five-by-eight
  I/J/L/T/cross footprint and window-profile matrix.
- Full isolated-environment Python suite: 687 tests passed, with 119 subtests
  passed, against the installed campaign wheel.
- All 180 independent Radiance exports compiled successfully.
- Cross-shaped distributed-window Metal smoke comparison completed with actual
  GPU execution; smoke results are diagnostic, not release qualification.
- No transport solver or numerical acceptance gates were changed in this
  iteration. The independent direct oracle uses verified binary-double I/O and
  a four-worker pool; its prescribed integration budgets are unchanged.

See the [corpus catalogue](../../architectural-scenes.md) and
[sample models](../../../test_models/architectural/README.md).

## Frozen inputs and provenance

Campaign root: `/private/tmp/foton-campaign.YlxanX`.

- Source revision: `d931af507757f977fe4d8356cc7dec62437fe081`, with an
  uncommitted working tree. Source files, their hashes, the working-tree patch,
  and installed dependencies are recorded in `final-inputs/snapshot.json`.
- Wheel SHA-256:
  `fa1516e688ead05382a886d9f189bbbccef1383e14daad7953ca69452bf46dcf`.
- Installed native library SHA-256:
  `e55b8c414c7334aa3b72e0d8ccd5e0ac28cc8e743a91457cc63cb199d1157dca`.
- Model manifest SHA-256:
  `a6b6f4b080d47b2fcfe0c8eb9b7ffa010ea88791f2f0e08649cd42e352f6362c`.
- Weather SHA-256:
  `98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee`.
- Hardware: Apple M4 Pro, 20-core GPU, Metal 4, macOS 26.6.2, arm64.
- Environment: isolated CPython 3.13, current wheel plus Honeybee/test extras,
  `lbt-recipes==0.28.8`, setuptools, and Radiance 6.0.2.

The primary full-quality run was `metal-final`, using both sky bases, the final
preset, four Radiance workers, direct integration at 256/1,024 samples per patch,
four replicates at each established bounce/sample level, seven controlled skies,
and annual comparisons.

## Artifacts lost

The campaign wrote everything under `/private/tmp/foton-campaign.YlxanX`. That
directory was removed by the operating system before it was archived, and no
copy exists. No numerical result from this run survives; only this description
does. Future campaigns must write under `validation/results/` or another
persistent location, never a temporary directory.

The run also compared Foton at `maximum_bounces=1` against an eight-bounce
Radiance reference, so even a complete record would not have passed the gates.
See [purpose and plan](../../../docs/purpose-and-plan.md).

## Pending qualification

Completion requires all 180 comparisons to be accounted for, including any
execution errors or inconclusive references. Numerical passing is not required
to finish this diagnostic run-and-report task.

Clean-commit validation, Windows Vulkan validation on an accessible Windows GPU
runner, and live Windows/Rhino acceptance remain necessary for release
qualification. The equivalent Windows command and artifact requirements are in
the [validation procedure](../../architectural-scenes.md).
