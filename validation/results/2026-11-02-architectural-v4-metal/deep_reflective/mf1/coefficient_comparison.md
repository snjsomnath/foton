# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| deep_reflective_grid | direct | -0.045% | 0.713% | 0.045% | PASS |
| deep_reflective_grid | indirect | -5.659% | 6.349% | 5.659% | FAIL |
| deep_reflective_grid | full | -4.183% | 6.345% | 4.183% | PASS |
