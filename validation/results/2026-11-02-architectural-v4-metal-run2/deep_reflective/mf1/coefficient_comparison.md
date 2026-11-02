# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| deep_reflective_grid | direct | -0.045% | 0.713% | 0.045% | PASS |
| deep_reflective_grid | indirect | -5.428% | 5.207% | 5.428% | FAIL |
| deep_reflective_grid | full | -4.013% | 5.205% | 4.013% | PASS |
