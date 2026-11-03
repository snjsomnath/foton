# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| glazed_corridor_corridor_grid | direct | -0.432% | 1.019% | 0.432% | PASS |
| glazed_corridor_corridor_grid | indirect | -0.249% | 1.849% | 0.249% | PASS |
| glazed_corridor_corridor_grid | full | -0.370% | 1.784% | 0.370% | PASS |
| glazed_corridor_office_grid | direct | 0.036% | 0.831% | 0.036% | PASS |
| glazed_corridor_office_grid | indirect | -0.475% | 5.368% | 0.475% | PASS |
| glazed_corridor_office_grid | full | -0.268% | 5.363% | 0.268% | PASS |
| glazed_corridor_meeting_grid | direct | 0.106% | 1.261% | 0.106% | PASS |
| glazed_corridor_meeting_grid | indirect | 0.758% | 20.651% | 0.758% | FAIL |
| glazed_corridor_meeting_grid | full | 0.682% | 20.604% | 0.682% | FAIL |
