# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| interior_glazing_grid | direct | -0.169% | 0.721% | 0.169% | PASS |
| interior_glazing_grid | indirect | -0.730% | 3.707% | 0.730% | PASS |
| interior_glazing_grid | full | -0.380% | 3.698% | 0.380% | PASS |
| adjacent_grid | direct | -0.023% | 1.053% | 0.023% | PASS |
| adjacent_grid | indirect | -3.304% | 11.601% | 3.304% | FAIL |
| adjacent_grid | full | -2.396% | 11.596% | 2.396% | FAIL |
