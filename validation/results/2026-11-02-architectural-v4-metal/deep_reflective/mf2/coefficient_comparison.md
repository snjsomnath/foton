# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| deep_reflective_grid | direct | -0.030% | 0.429% | 0.030% | PASS |
| deep_reflective_grid | indirect | -5.655% | 6.615% | 5.655% | FAIL |
| deep_reflective_grid | full | -4.177% | 6.615% | 4.177% | PASS |
