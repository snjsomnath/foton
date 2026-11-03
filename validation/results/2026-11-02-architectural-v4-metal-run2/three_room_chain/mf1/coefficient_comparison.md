# Foton / Radiance coefficient-stage comparison

Overall: **FAIL**

| Grid | Stage | NMBE | RMS-normalized RMSE | Energy error | Gate |
|---|---|---:|---:|---:|:---:|
| three_room_chain_0_grid | direct | -0.263% | 0.759% | 0.263% | PASS |
| three_room_chain_0_grid | indirect | -0.556% | 1.428% | 0.556% | PASS |
| three_room_chain_0_grid | full | -0.365% | 1.400% | 0.365% | PASS |
| three_room_chain_1_grid | direct | -0.976% | 1.716% | 0.976% | PASS |
| three_room_chain_1_grid | indirect | 0.437% | 4.529% | 0.437% | PASS |
| three_room_chain_1_grid | full | -0.099% | 4.491% | 0.099% | PASS |
| three_room_chain_2_grid | direct | 0.052% | 1.702% | 0.052% | PASS |
| three_room_chain_2_grid | indirect | 7.293% | 12.854% | 7.293% | FAIL |
| three_room_chain_2_grid | full | 5.022% | 12.703% | 5.022% | FAIL |
