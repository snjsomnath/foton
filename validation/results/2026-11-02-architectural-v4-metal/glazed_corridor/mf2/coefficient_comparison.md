# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| glazed_corridor_corridor_grid | direct | -0.461% | 1.163% | 0.461% | PASS |
| glazed_corridor_corridor_grid | indirect | -0.182% | 2.060% | 0.182% | PASS |
| glazed_corridor_corridor_grid | full | -0.367% | 2.029% | 0.367% | PASS |
| glazed_corridor_office_grid | direct | -0.084% | 0.894% | 0.084% | PASS |
| glazed_corridor_office_grid | indirect | -0.691% | 5.632% | 0.691% | PASS |
| glazed_corridor_office_grid | full | -0.446% | 5.624% | 0.446% | PASS |
| glazed_corridor_meeting_grid | direct | -0.036% | 1.844% | 0.036% | PASS |
| glazed_corridor_meeting_grid | indirect | 1.711% | 21.903% | 1.711% | FAIL |
| glazed_corridor_meeting_grid | full | 1.504% | 21.921% | 1.504% | FAIL |
