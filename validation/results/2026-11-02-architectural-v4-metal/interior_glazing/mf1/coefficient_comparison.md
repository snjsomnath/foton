# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| interior_glazing_grid | direct | -0.151% | 0.645% | 0.151% | PASS |
| interior_glazing_grid | indirect | -0.830% | 2.998% | 0.830% | PASS |
| interior_glazing_grid | full | -0.406% | 2.997% | 0.406% | PASS |
| adjacent_grid | direct | -0.210% | 0.999% | 0.210% | PASS |
| adjacent_grid | indirect | -3.105% | 9.745% | 3.105% | FAIL |
| adjacent_grid | full | -2.303% | 9.769% | 2.303% | PASS |
