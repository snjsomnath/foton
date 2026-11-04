# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.245% | 0.773% | 0.245% | PASS |
| three_room_chain_0_grid | indirect | -0.677% | 1.768% | 0.677% | PASS |
| three_room_chain_0_grid | full | -0.395% | 1.745% | 0.395% | PASS |
| three_room_chain_1_grid | direct | -1.092% | 1.714% | 1.092% | PASS |
| three_room_chain_1_grid | indirect | 0.944% | 3.355% | 0.944% | PASS |
| three_room_chain_1_grid | full | 0.171% | 3.287% | 0.171% | PASS |
| three_room_chain_2_grid | direct | -0.204% | 1.535% | 0.204% | PASS |
| three_room_chain_2_grid | indirect | 4.716% | 8.446% | 4.716% | FAIL |
| three_room_chain_2_grid | full | 3.193% | 8.404% | 3.193% | PASS |
