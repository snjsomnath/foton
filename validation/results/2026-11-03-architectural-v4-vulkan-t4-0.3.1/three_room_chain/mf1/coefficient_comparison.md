# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.263% | 0.759% | 0.263% | PASS |
| three_room_chain_0_grid | indirect | -0.594% | 1.414% | 0.594% | PASS |
| three_room_chain_0_grid | full | -0.378% | 1.386% | 0.378% | PASS |
| three_room_chain_1_grid | direct | -0.976% | 1.716% | 0.976% | PASS |
| three_room_chain_1_grid | indirect | 0.221% | 4.525% | 0.221% | PASS |
| three_room_chain_1_grid | full | -0.233% | 4.468% | 0.233% | PASS |
| three_room_chain_2_grid | direct | 0.052% | 1.701% | 0.052% | PASS |
| three_room_chain_2_grid | indirect | 6.311% | 12.040% | 6.311% | FAIL |
| three_room_chain_2_grid | full | 4.361% | 11.936% | 4.361% | FAIL |
