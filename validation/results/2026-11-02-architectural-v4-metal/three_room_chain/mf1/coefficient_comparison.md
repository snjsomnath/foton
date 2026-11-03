# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.263% | 0.759% | 0.263% | PASS |
| three_room_chain_0_grid | indirect | -0.619% | 2.402% | 0.619% | PASS |
| three_room_chain_0_grid | full | -0.387% | 2.388% | 0.387% | PASS |
| three_room_chain_1_grid | direct | -0.975% | 1.716% | 0.975% | PASS |
| three_room_chain_1_grid | indirect | -0.089% | 7.785% | 0.089% | PASS |
| three_room_chain_1_grid | full | -0.425% | 7.759% | 0.425% | PASS |
| three_room_chain_2_grid | direct | 0.052% | 1.700% | 0.052% | PASS |
| three_room_chain_2_grid | indirect | 5.566% | 21.150% | 5.566% | FAIL |
| three_room_chain_2_grid | full | 3.850% | 21.055% | 3.850% | FAIL |
