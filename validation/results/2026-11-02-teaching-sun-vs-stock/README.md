# Patch sun versus traced sun: Foton against the stock Honeybee recipe in three climates

2026-11-02, commit `fc3aafd`, Metal on an M4 Pro, Radiance 5.4a, lbt-recipes 0.28.8.
This quantifies the direct-sun decision in [purpose and plan](../../../docs/purpose-and-plan.md#4-decide-direct-sun):
Foton is a two-phase method whose sun is carried inside its sky patch, while
Honeybee's `annual-daylight` recipe (enhanced two-phase) replaces the direct
part of that patch with a sun traced at its true position. The release suite
cannot see this difference because its reference is `rfluxmtx`, which smears
the sun the same way Foton does.

Two teaching rooms (`teaching_depth6`, 6 × 6 × 3 m with a 5.4 × 1.33 m south
window; `teaching_depth10`, the same window on a 10 m deep room; 36 sensors
each) were run with Foton's `final` preset at MF:1 and with the stock recipe
under Gothenburg (mixed), Phoenix (sunny) and Seattle (overcast) weather. The
recipe was run twice: at its own default ambient parameters
(`-ab 2 -ad 5000 -lw 2e-05 -dr 0`) and at converged ones
(`-ab 6 -ad 25000 -lw 4e-07 -dr 0`). Occupancy 08:00–18:00, 3,650 hours.
Errors are Foton minus recipe.

| Room | Climate | Recipe ambient | NMBE | CV(RMSE) | DA MAE | DA max | UDI MAE | sDA Foton | sDA recipe |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| depth 6 m | Gothenburg | default | +15.1 % | 22.7 % | 18.0 pp | 40.0 pp | 4.3 pp | 100.0 | 52.8 |
| depth 6 m | Gothenburg | converged | +0.7 % | 2.9 % | 0.6 pp | 2.0 pp | 0.2 pp | 100.0 | 100.0 |
| depth 6 m | Phoenix | default | +15.2 % | 22.4 % | 28.4 pp | 64.8 pp | 3.1 pp | 100.0 | 55.6 |
| depth 6 m | Phoenix | converged | +0.7 % | 2.8 % | 0.7 pp | 5.5 pp | 0.1 pp | 100.0 | 100.0 |
| depth 6 m | Seattle | default | +14.6 % | 22.5 % | 19.3 pp | 39.2 pp | 5.8 pp | 94.4 | 50.0 |
| depth 6 m | Seattle | converged | +0.6 % | 3.0 % | 0.6 pp | 2.9 pp | 0.2 pp | 94.4 | 88.9 |
| depth 10 m | Gothenburg | default | +17.3 % | 28.7 % | 15.4 pp | 34.8 pp | 19.8 pp | 50.0 | 28.3 |
| depth 10 m | Gothenburg | converged | +0.7 % | 3.6 % | 0.8 pp | 2.6 pp | 0.5 pp | 50.0 | 46.7 |
| depth 10 m | Phoenix | default | +16.6 % | 27.5 % | 21.6 pp | 56.1 pp | 27.5 pp | 55.0 | 33.3 |
| depth 10 m | Phoenix | converged | +0.6 % | 3.7 % | 1.3 pp | 5.4 pp | 0.8 pp | 55.0 | 51.7 |
| depth 10 m | Seattle | default | +16.6 % | 27.8 % | 14.8 pp | 34.7 pp | 20.9 pp | 43.3 | 30.0 |
| depth 10 m | Seattle | converged | +0.7 % | 3.6 % | 0.7 pp | 3.3 pp | 0.7 pp | 43.3 | 43.3 |

## What it shows

- **The patch sun costs little in these rooms.** Against a converged recipe
  with a traced sun, Foton is 0.6–0.7 % high in energy with 2.8–3.7 % hourly
  CV(RMSE) in every climate, Phoenix included; DA mean error stays at or under
  1.3 pp and UDI under 1 pp. The sunny climate shows up only in the worst
  single sensor (DA 5.4–5.5 pp off in Phoenix against 2–3 pp elsewhere) and in
  the sDA of the deep room (3.3 pp, which is one sensor of 36 on this grid).
  The two-phase-only decision for 0.3 is therefore quantified at about 1 pp
  of DA and 1 % of energy for a south-facing teaching room, not the large
  effect the plan had allowed for.
- **The recipe's default ambient settings are the real discrepancy.** At
  `-ab 2 -ad 5000` the recipe reads 15–17 % below Foton in every climate, and
  that bias moves DA by 15–28 pp and sDA by 20–47 pp because so many sensors
  in these rooms sit near the 300 lux threshold. The same recipe converged in
  ambient agrees with Foton, and the release campaigns show Foton agreeing
  with converged `rfluxmtx`, so the gap is the two-bounce default, not Foton.
  Anyone checking Foton against a stock Honeybee annual run should expect
  Foton to come out about 15 % higher unless they raise `-ab` and `-ad`.
- The recipe at converged settings took 0.7 minutes per room with two
  workers; Foton's `final` pass took about a second on the GPU.

## Files

`table.json` holds the numbers above; each `<room>_<climate>_<ambient>/`
folder has the `comparison.{json,md}` written by `compare_annual_daylight`
and the recipe's `reference_manifest.json` (command, parameters, versions).
`sun_vs_stock.py` is the driver as run, with its scratch paths; the stock
runs came from `scripts/run_honeybee_annual_reference.py`, whose new
`--radiance-parameters` option set the converged ambient values. Foton's
illuminance folders and the recipe's project folders are not kept.
