# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.245% | 0.773% | 0.245% | PASS |
| three_room_chain_0_grid | indirect | -0.654% | 1.758% | 0.654% | PASS |
| three_room_chain_0_grid | full | -0.387% | 1.730% | 0.387% | PASS |
| three_room_chain_1_grid | direct | -1.092% | 1.714% | 1.092% | PASS |
| three_room_chain_1_grid | indirect | 1.165% | 3.440% | 1.165% | PASS |
| three_room_chain_1_grid | full | 0.307% | 3.393% | 0.307% | PASS |
| three_room_chain_2_grid | direct | -0.202% | 1.536% | 0.202% | PASS |
| three_room_chain_2_grid | indirect | 5.374% | 9.345% | 5.374% | FAIL |
| three_room_chain_2_grid | full | 3.641% | 9.352% | 3.641% | PASS |
