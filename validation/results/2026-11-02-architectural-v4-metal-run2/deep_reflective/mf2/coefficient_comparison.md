# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| deep_reflective_grid | direct | -0.030% | 0.429% | 0.030% | PASS |
| deep_reflective_grid | indirect | -5.568% | 5.228% | 5.568% | FAIL |
| deep_reflective_grid | full | -4.113% | 5.228% | 4.113% | PASS |
