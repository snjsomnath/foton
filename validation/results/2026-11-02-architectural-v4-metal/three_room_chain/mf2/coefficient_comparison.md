# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.245% | 0.773% | 0.245% | PASS |
| three_room_chain_0_grid | indirect | -0.727% | 3.235% | 0.727% | PASS |
| three_room_chain_0_grid | full | -0.412% | 3.222% | 0.412% | PASS |
| three_room_chain_1_grid | direct | -1.092% | 1.714% | 1.092% | PASS |
| three_room_chain_1_grid | indirect | 0.071% | 8.607% | 0.071% | PASS |
| three_room_chain_1_grid | full | -0.370% | 8.582% | 0.370% | PASS |
| three_room_chain_2_grid | direct | -0.201% | 1.535% | 0.201% | PASS |
| three_room_chain_2_grid | indirect | 5.917% | 26.981% | 5.917% | FAIL |
| three_room_chain_2_grid | full | 4.009% | 27.002% | 4.009% | FAIL |
