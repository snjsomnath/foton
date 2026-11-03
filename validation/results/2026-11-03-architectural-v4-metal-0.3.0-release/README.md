# Metal suite on the 0.3.0 release commit, judged against the published references

Commit `5c419d1` (clean checkout, `foton-daylight` 0.3.0), 2026-11-03 10:50 UTC,
5.5 minutes on an Apple M4 Pro. This is the Metal entry of
[`validation/release-evidence.json`](../../release-evidence.json).

It ran `validate_release_suite.py --backend metal --reuse-references` against
the bundle [`foton-references-corpus4-2026-11-03`](https://github.com/snjsomnath/foton/releases/tag/references-corpus4-2026-11-03),
exported from the [six-hour campaign of the same morning](../2026-11-03-architectural-v4-metal-0.3.0/README.md)
on commit `f65030f`. Between that commit and this one the suite script gained
the reuse mode itself, so the release gate asked for a run on the later
commit; the Radiance oracle did not need to be repeated.

**Result: 204 of 212 cases passed**, 2 accuracy failures, 6 unstable
references, 0 errors; the same eight open cases as the campaign, in the same
classes. Every case executed on the GPU, every sensor grid matched its
reference exactly (largest coordinate difference 0.0), and every coefficient
error agrees with the campaign to the printed digit: Foton's Metal transport is
deterministic, and the references are the same arrays.

The run still exported every scene, audited the sky bins, prepared the
Gothenburg weather and ran Honeybee's stock recipe on the acceptance model
through Radiance 5.4a; only the replicated `rfluxmtx` oracle was taken from
the bundle. Each `report.json` records that under `reference_source`.

Files as in every campaign: `suite.json`, `suite.md`, and per case `report.md`,
`coefficient_comparison.{json,md}`, `converged_annual.json` and, for the
acceptance model, `stock_comparison/`.
