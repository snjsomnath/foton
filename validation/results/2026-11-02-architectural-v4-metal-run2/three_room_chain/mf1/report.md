# Foton report

Status: **failed**

```json
{
  "scene": "three_room_chain",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "three_room_chain",
    "category": "connections",
    "question": "Can daylight cross two successive internal glass partitions?",
    "interactions": [
      "borrowed_light",
      "serial_glazing",
      "paired_apertures"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 14.999999999999996
  },
  "sky_density": 1,
  "status": "failed",
  "passed": false,
  "model_sha256": "848fdc8e1fab3da490d9d4ccb829ec9a7c2bae463834873c24156dc39a42518b",
  "weather_sha256": "98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee",
  "gpu_executed": true,
  "candidate": {
    "capabilities": {
      "name": "Metal device: Apple M4 Pro (GPU direct, diffuse, glass, and annual reduction)",
      "hardware_acceleration": true,
      "supports_ray_tracing": true,
      "supports_async_jobs": true
    },
    "direct": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.2.0",
      "scene_fingerprint": 1666965602579954223,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "metal",
      "used_reference_fallback": false
    },
    "full": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.2.0",
      "scene_fingerprint": 1666965602579954223,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "metal",
      "used_reference_fallback": false
    }
  },
  "sky_bin_audit": {
    "passed": true,
    "ray_count": 2336,
    "command": [
      "/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
      "-f",
      "/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.019309155610223977,
        "rms_normalized_error_percent": 0.5180703015933942,
        "absolute_error": {
          "p95": 4.789326339960098e-06,
          "p99": 4.62816096842289e-05,
          "maximum": 0.00023132911883294582
        },
        "worst_index": [
          6,
          96,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.24179191404592212,
        "rms_normalized_error_percent": 1.653169518434747,
        "absolute_error": {
          "p95": 0.0,
          "p99": 5.232635885477066e-06,
          "maximum": 4.955328768119216e-05
        },
        "worst_index": [
          13,
          17,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": -0.9185420452086702,
        "rms_normalized_error_percent": 2.17879723643301,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 1.2653428711928427e-05
        },
        "worst_index": [
          4,
          15,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      1024,
      4096
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.09092834773300788,
        "rms_normalized_error_percent": 0.9347800061850994,
        "absolute_error": {
          "p95": 5.7076511438935995e-05,
          "p99": 0.0001586712896823883,
          "maximum": 0.00044035911560058594
        },
        "worst_index": [
          13,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": -0.30804957638514996,
        "rms_normalized_error_percent": 3.5996326454769725,
        "absolute_error": {
          "p95": 6.987545930314809e-06,
          "p99": 3.256404306739569e-05,
          "maximum": 0.0001756567507982254
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": -0.1779215564057455,
        "rms_normalized_error_percent": 4.858978789815855,
        "absolute_error": {
          "p95": 1.068967321771197e-06,
          "p99": 5.134814273333177e-06,
          "maximum": 3.6353798350319266e-05
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.04145791980273444,
        "rms_normalized_error_percent": 0.7708390406273151,
        "absolute_error": {
          "p95": 5.116598913446069e-05,
          "p99": 0.00012406939640641212,
          "maximum": 0.00030709803104400635
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.16274277791528918,
        "rms_normalized_error_percent": 2.978127638805039,
        "absolute_error": {
          "p95": 5.794474418507889e-06,
          "p99": 2.6421912480145693e-05,
          "maximum": 0.0001361712347716093
        },
        "worst_index": [
          14,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.0009937856083386814,
        "rms_normalized_error_percent": 4.286161661931463,
        "absolute_error": {
          "p95": 9.616354645913816e-07,
          "p99": 4.782239557243884e-06,
          "maximum": 3.06995352730155e-05
        },
        "worst_index": [
          15,
          17,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.08914945794308811,
                "cvrmse_percent": 15.077534801213243,
                "rms_normalized_rmse_percent": 3.600010545654315,
                "reference_energy": 5.701452635869828,
                "candidate_energy": 5.7065354499895875,
                "relative_energy_error_percent": 0.0891494579430881,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.619980119168758e-07,
                  "p95": 0.00014125939924269915,
                  "p99": 0.00043217395432293415,
                  "maximum": 0.0008905548602342606
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 117,
                  "rgb_channel": 0,
                  "reference": 0.017351539805531502,
                  "candidate": 0.018242094665765762
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2318589076924042,
                "cvrmse_percent": 72.81387151135712,
                "rms_normalized_rmse_percent": 4.104752148927263,
                "reference_energy": 1.7004264359005958,
                "candidate_energy": 1.7043690260609878,
                "relative_energy_error_percent": 0.2318589076924042,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.6257046051323414e-05,
                  "p95": 0.00023595447419211268,
                  "p99": 0.0006131292320787907,
                  "maximum": 0.001215220894664526
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.0006616853643208742,
                  "candidate": -0.0005535355303436518
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.7697811649946047,
                "cvrmse_percent": 94.09215760678084,
                "rms_normalized_rmse_percent": 8.896781027986712,
                "reference_energy": 0.12220737254597225,
                "candidate_energy": 0.12314810188206593,
                "relative_energy_error_percent": 0.7697811649946047,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.965049447491765e-05,
                  "maximum": 0.000225176103413105
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.002494175569154322,
                  "candidate": 0.002268999465741217
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.417525609581737,
                "cvrmse_percent": 251.9539156673105,
                "rms_normalized_rmse_percent": 12.17259167308043,
                "reference_energy": 0.08825530440992324,
                "candidate_energy": 0.08612170982399903,
                "relative_energy_error_percent": 2.417525609581737,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.935653568187263e-07,
                  "p99": 8.39104159240378e-05,
                  "maximum": 0.000502754541230388
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.00022294215159490705,
                  "candidate": -0.00027981238963548094
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.018850364325482483,
                "cvrmse_percent": 257.769009820443,
                "rms_normalized_rmse_percent": 16.21273710607163,
                "reference_energy": 0.012473896098526893,
                "candidate_energy": 0.012471544723666739,
                "relative_energy_error_percent": 0.018850364325482483,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 8.447295113001019e-05
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0003068950609304011,
                  "candidate": 0.0003913680120604113
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 4.822247123381037,
                "cvrmse_percent": 377.7615139595171,
                "rms_normalized_rmse_percent": 16.86099109394955,
                "reference_energy": 0.012067205829907834,
                "candidate_energy": 0.012649116315913034,
                "relative_energy_error_percent": 4.822247123381037,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.0653543995431392e-05,
                  "maximum": 0.00010145064879907295
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": -6.741539255017415e-05,
                  "candidate": 3.4035256248898804e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.9914999511093,
            "full": 433.71608399320394
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.4441249417141,
            "full": 425.08812504820526
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.43512495141476,
            "full": 419.960833969526
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.76300006452948,
            "full": 421.00783402565867
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06599508056603537,
                "cvrmse_percent": 7.011723345380845,
                "rms_normalized_rmse_percent": 1.6768278609743141,
                "reference_energy": 5.712780529492079,
                "candidate_energy": 5.716550683605078,
                "relative_energy_error_percent": 0.06599508056603538,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.1257437765598297e-07,
                  "p95": 7.58664682507515e-05,
                  "p99": 0.00019767507910728455,
                  "maximum": 0.00042467471212148666
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.0074450846295803785,
                  "candidate": 0.007020409917458892
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.16052134266693005,
                "cvrmse_percent": 20.704559544078048,
                "rms_normalized_rmse_percent": 1.767524064504857,
                "reference_energy": 3.031544079482348,
                "candidate_energy": 3.026677804222423,
                "relative_energy_error_percent": 0.16052134266693005,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7819723946720387e-07,
                  "p90": 4.165712743997574e-05,
                  "p95": 0.0001073349267244339,
                  "p99": 0.0003055159468203783,
                  "maximum": 0.0007899478077888489
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.031922630965709686,
                  "candidate": 0.032712578773498535
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -1.0443557940011705,
                "cvrmse_percent": 56.399985653863865,
                "rms_normalized_rmse_percent": 5.336629359860863,
                "reference_energy": 0.12408010193666996,
                "candidate_energy": 0.12278426420289179,
                "relative_energy_error_percent": 1.0443557940011705,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3928023690823466e-05,
                  "maximum": 0.00015450251521542668
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 10,
                  "sky_patch_index": 15,
                  "rgb_channel": 0,
                  "reference": 0.0013085484970360994,
                  "candidate": 0.0011540459818206728
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.4823839039380877,
                "cvrmse_percent": 68.14687756111358,
                "rms_normalized_rmse_percent": 5.876972950491963,
                "reference_energy": 0.20254694489249303,
                "candidate_energy": 0.20352399875257277,
                "relative_energy_error_percent": 0.4823839039380878,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.9556485259263354e-08,
                  "p90": 5.564520051848376e-06,
                  "p95": 9.868399502011016e-06,
                  "p99": 5.017479998059571e-05,
                  "maximum": 0.00030181347392499447
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.005383138544857502,
                  "candidate": 0.0050813250709325075
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -5.049320371765731,
                "cvrmse_percent": 172.89048951978202,
                "rms_normalized_rmse_percent": 10.87543627997151,
                "reference_energy": 0.013029789799475111,
                "candidate_energy": 0.012371873968731961,
                "relative_energy_error_percent": 5.04932037176573,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.755706272087991e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.00043826550245285034,
                  "candidate": 0.00037070843973197043
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.3172935795906473,
                "cvrmse_percent": 152.68973808641022,
                "rms_normalized_rmse_percent": 11.825943641362077,
                "reference_energy": 0.0266587302974024,
                "candidate_energy": 0.02630755655479433,
                "relative_energy_error_percent": 1.3172935795906475,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.820754592240519e-07,
                  "p95": 1.6174740267160814e-06,
                  "p99": 8.673698175698519e-06,
                  "maximum": 0.0001287601626245305
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.000120751210488379,
                  "candidate": -8.008952136151493e-06
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.59729105886072,
            "full": 5133.199750096537
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.56345902010798,
            "full": 5173.495167051442
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.44829199835658,
            "full": 5238.84645907674
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.80529208201915,
            "full": 5370.8803749177605
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.037406087512210424,
                "cvrmse_percent": 6.325746061202852,
                "rms_normalized_rmse_percent": 1.5137770268593447,
                "reference_energy": 5.712018533945866,
                "candidate_energy": 5.709881891294344,
                "relative_energy_error_percent": 0.03740608751221043,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.905734047293663e-07,
                  "p95": 6.570815457962453e-05,
                  "p99": 0.00017471471801400185,
                  "maximum": 0.00034070038236677647
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.007349965628236532,
                  "candidate": 0.007690666010603309
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.1861382767094546,
                "cvrmse_percent": 19.319021307888914,
                "rms_normalized_rmse_percent": 1.6525117852688955,
                "reference_energy": 3.0379494848559894,
                "candidate_energy": 3.043604271674404,
                "relative_energy_error_percent": 0.1861382767094546,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.374172076713421e-07,
                  "p90": 3.703530819620937e-05,
                  "p95": 0.00010992959141731262,
                  "p99": 0.0002745778765529394,
                  "maximum": 0.0005898494273424149
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02472801972180605,
                  "candidate": 0.024138170294463634
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.5639550632521947,
                "cvrmse_percent": 65.57984258658388,
                "rms_normalized_rmse_percent": 6.224640756279076,
                "reference_energy": 0.12393253938807902,
                "candidate_energy": 0.12323361555718293,
                "relative_energy_error_percent": 0.5639550632521947,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3896496966481209e-05,
                  "maximum": 0.0002913446514867246
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.0008885248971637338,
                  "candidate": 0.0005971802456770092
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.50223109167169,
                "cvrmse_percent": 67.348850498086,
                "rms_normalized_rmse_percent": 5.804568961168106,
                "reference_energy": 0.2013732141370994,
                "candidate_energy": 0.20238457302879453,
                "relative_energy_error_percent": 0.50223109167169,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.254555736020848e-08,
                  "p90": 5.595476977759972e-06,
                  "p95": 9.270253030990716e-06,
                  "p99": 5.566095933318138e-05,
                  "maximum": 0.000332484400132671
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": -5.262639024294913e-05,
                  "candidate": 0.00027985800988972187
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 3.371822346742552,
                "cvrmse_percent": 213.39000463669345,
                "rms_normalized_rmse_percent": 13.667690939621298,
                "reference_energy": 0.01207140807127871,
                "candidate_energy": 0.01247843450619257,
                "relative_energy_error_percent": 3.3718223467425523,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 9.281330858357251e-05
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.00030323029204737395,
                  "candidate": 0.00039604360063094646
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -4.31477166543463,
                "cvrmse_percent": 141.38907862282653,
                "rms_normalized_rmse_percent": 11.24968892523676,
                "reference_energy": 0.02743113293659505,
                "candidate_energy": 0.02624754218513914,
                "relative_energy_error_percent": 4.31477166543463,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.632845384046959e-07,
                  "p95": 1.5887346300758054e-06,
                  "p99": 9.588490684109274e-06,
                  "maximum": 0.00011131539940834045
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.00039484970329795033,
                  "candidate": 0.0002835343038896099
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.97804201114923,
            "full": 5557.973999995738
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.49774997867644,
            "full": 5551.494124927558
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 212.9292089957744,
            "full": 5568.833332974464
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 223.7457090523094,
            "full": 5493.544875062071
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.01132641754685282,
                "cvrmse_percent": 3.8354308820273477,
                "rms_normalized_rmse_percent": 0.9175775521582799,
                "reference_energy": 5.712312379698119,
                "candidate_energy": 5.711665379346414,
                "relative_energy_error_percent": 0.01132641754685282,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6798807084560394e-07,
                  "p95": 3.482401371002197e-05,
                  "p99": 0.00010490161366760731,
                  "maximum": 0.00024238089099526405
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 14,
                  "rgb_channel": 0,
                  "reference": 0.0022949574049562216,
                  "candidate": 0.0020525765139609575
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.27614519187738273,
                "cvrmse_percent": 12.300389574343296,
                "rms_normalized_rmse_percent": 1.051330010991815,
                "reference_energy": 3.0319237346367345,
                "candidate_energy": 3.040296246251323,
                "relative_energy_error_percent": 0.27614519187738273,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.740990995813263e-07,
                  "p90": 2.3857901396695524e-05,
                  "p95": 6.311654578894377e-05,
                  "p99": 0.0001704036258161068,
                  "maximum": 0.0005251951515674591
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03444739058613777,
                  "candidate": 0.03497258573770523
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.33983601277128056,
                "cvrmse_percent": 30.02181733866791,
                "rms_normalized_rmse_percent": 2.8531200536016694,
                "reference_energy": 0.12391861868604792,
                "candidate_energy": 0.12349749859322401,
                "relative_energy_error_percent": 0.33983601277128056,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3924607628723606e-05,
                  "maximum": 7.498794002458453e-05
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 15,
                  "rgb_channel": 0,
                  "reference": 0.0012164110084995627,
                  "candidate": 0.0012913989485241473
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.24898772536708824,
                "cvrmse_percent": 44.917776298698726,
                "rms_normalized_rmse_percent": 3.8634368564289367,
                "reference_energy": 0.20253572505782103,
                "candidate_energy": 0.20203143596294382,
                "relative_energy_error_percent": 0.24898772536708821,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.130631576198084e-08,
                  "p90": 4.1188787349710765e-06,
                  "p95": 7.0796345426060725e-06,
                  "p99": 2.989597851410508e-05,
                  "maximum": 0.0002016045618802309
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0027357860235497355,
                  "candidate": 0.0025341814616695046
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.8650303811297768,
                "cvrmse_percent": 118.61413635516537,
                "rms_normalized_rmse_percent": 7.5877248426569555,
                "reference_energy": 0.012067465788277332,
                "candidate_energy": 0.012171853033578373,
                "relative_energy_error_percent": 0.8650303811297767,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.639111284632236e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0003491252427920699,
                  "candidate": 0.00039551635563839227
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.40912401375080765,
                "cvrmse_percent": 108.38859896292051,
                "rms_normalized_rmse_percent": 8.646528375919907,
                "reference_energy": 0.026939879642871034,
                "candidate_energy": 0.027050097159765585,
                "relative_energy_error_percent": 0.40912401375080765,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.265697010121585e-07,
                  "p95": 1.142096152761951e-06,
                  "p99": 6.899157597217709e-06,
                  "maximum": 7.135842315619811e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0003999633408966474,
                  "candidate": 0.0003286049177404493
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 362.91150003671646,
            "full": 9728.385665919632
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 350.44633294455707,
            "full": 9585.997625021264
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 339.4361659884453,
            "full": 9653.27733301092
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 326.4817090239376,
            "full": 9386.859833961353
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2926.290209055878,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10957.92687498033,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 44396.816374966875,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      72,
      146,
      3
    ],
    "gates": {
      "direct": {
        "absolute_nmbe_percent": 2.0,
        "rms_normalized_rmse_percent": 5.0
      },
      "indirect": {
        "absolute_nmbe_percent": 3.0,
        "rms_normalized_rmse_percent": 10.0
      },
      "full": {
        "absolute_nmbe_percent": 5.0,
        "rms_normalized_rmse_percent": 10.0
      }
    },
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.26342384991845025,
            "cvrmse_percent": 3.1683566087371218,
            "rms_normalized_rmse_percent": 0.7587174536485537,
            "reference_energy": 5.71215306269778,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.2634238499184503,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5562469698442936,
            "cvrmse_percent": 16.69835904720798,
            "rms_normalized_rmse_percent": 1.4283196625731525,
            "reference_energy": 3.035945770744174,
            "candidate_energy": 3.0190584143882937,
            "relative_energy_error_percent": 0.5562469698442937,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.667648441791243e-07,
              "p90": 4.063609230797738e-05,
              "p95": 6.612739525735378e-05,
              "p99": 0.00017829917487688363,
              "maximum": 0.000916607677936554
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036637626588344574,
              "candidate": 0.03572101891040802,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3650453712845048,
            "cvrmse_percent": 5.678294601602594,
            "rms_normalized_rmse_percent": 1.3995525564430946,
            "reference_energy": 8.748098833441954,
            "candidate_energy": 8.71616430357508,
            "relative_energy_error_percent": 0.3650453712845048,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.332631923873123e-07,
              "p90": 3.91132925869897e-05,
              "p95": 6.10866118222475e-05,
              "p99": 0.00017296802252531052,
              "maximum": 0.000916607677936554
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036637626588344574,
              "candidate": 0.03572101891040802,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.9756095987047734,
            "cvrmse_percent": 17.91034704080432,
            "rms_normalized_rmse_percent": 1.716377779323156,
            "reference_energy": 0.12372056898993833,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9756095987047735,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
              "maximum": 4.2101954022655264e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.2101954022655264e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.4368652284267178,
            "cvrmse_percent": 52.481267513203385,
            "rms_normalized_rmse_percent": 4.529172640860259,
            "reference_energy": 0.20227106927127636,
            "candidate_energy": 0.2031547212400895,
            "relative_energy_error_percent": 0.4368652284267178,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.922933349860159e-08,
              "p90": 7.288392225746065e-06,
              "p95": 1.2045493349432945e-05,
              "p99": 3.336265217512846e-05,
              "maximum": 0.0002269987016916275
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001683908747509122,
              "candidate": 0.0014569100458174944,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.0991981817538993,
            "cvrmse_percent": 32.287643820022105,
            "rms_normalized_rmse_percent": 4.490798859177468,
            "reference_energy": 0.3259916382612147,
            "candidate_energy": 0.3256682604833898,
            "relative_energy_error_percent": 0.09919818175389929,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.954227973361867e-08,
              "p90": 6.966854925849475e-06,
              "p95": 1.145470014307648e-05,
              "p99": 2.822766691679135e-05,
              "maximum": 0.0002269987016916275
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001683908747509122,
              "candidate": 0.0014569100458174944,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": 0.052057915842491136,
            "cvrmse_percent": 26.76264100280946,
            "rms_normalized_rmse_percent": 1.7015066626799185,
            "reference_energy": 0.012266531306522666,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.05205791584249114,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 7.293337522083766,
            "cvrmse_percent": 161.67086769640437,
            "rms_normalized_rmse_percent": 12.854074604548938,
            "reference_energy": 0.026848116063783678,
            "candidate_energy": 0.028806239786636212,
            "relative_energy_error_percent": 7.293337522083766,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.929278353913105e-07,
              "p95": 2.029178176599089e-06,
              "p99": 1.3591794413514435e-05,
              "maximum": 0.0001146483700722456
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0002980816352646798,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 5.022439304638145,
            "cvrmse_percent": 109.66895816602602,
            "rms_normalized_rmse_percent": 12.703353031877642,
            "reference_energy": 0.039114647370306344,
            "candidate_energy": 0.04107915679370322,
            "relative_energy_error_percent": 5.022439304638144,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.929278353913105e-07,
              "p95": 2.029178176599089e-06,
              "p99": 1.4107703464105725e-05,
              "maximum": 0.0001146483700722456
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0002980816352646798,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      }
    ]
  },
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      72,
      146,
      3
    ],
    "gates": {
      "direct": {
        "absolute_nmbe_percent": 2.0,
        "rms_normalized_rmse_percent": 5.0
      },
      "indirect": {
        "absolute_nmbe_percent": 3.0,
        "rms_normalized_rmse_percent": 10.0
      },
      "full": {
        "absolute_nmbe_percent": 5.0,
        "rms_normalized_rmse_percent": 10.0
      }
    },
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.26342384991845025,
            "cvrmse_percent": 3.1683566087371218,
            "rms_normalized_rmse_percent": 0.7587174536485537,
            "reference_energy": 5.71215306269778,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.2634238499184503,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 78.19557882069832,
            "cvrmse_percent": 439.82674941129955,
            "rms_normalized_rmse_percent": 24.69059184558147,
            "reference_energy": 1.6942386754870569,
            "candidate_energy": 3.0190584143882937,
            "relative_energy_error_percent": 78.19557882069833,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.1301886710698454e-07,
              "p90": 0.00023971000337041914,
              "p95": 0.00032235123217105865,
              "p99": 0.0005423021502792835,
              "maximum": 0.010163076221942902
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01422150433063507,
              "candidate": 0.024384580552577972,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.684354429127776,
            "cvrmse_percent": 100.5935173292081,
            "rms_normalized_rmse_percent": 24.686069248578793,
            "reference_energy": 7.406391738184837,
            "candidate_energy": 8.71616430357508,
            "relative_energy_error_percent": 17.684354429127776,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023947376757860184,
              "p95": 0.000318384263664484,
              "p99": 0.000548485666513443,
              "maximum": 0.010163076221942902
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01422150433063507,
              "candidate": 0.024384580552577972,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.9756095987047734,
            "cvrmse_percent": 17.91034704080432,
            "rms_normalized_rmse_percent": 1.716377779323156,
            "reference_energy": 0.12372056898993833,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9756095987047735,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
              "maximum": 4.2101954022655264e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.2101954022655264e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 135.82694970948359,
            "cvrmse_percent": 835.7985548891625,
            "rms_normalized_rmse_percent": 39.62394249462046,
            "reference_energy": 0.08614567651846272,
            "candidate_energy": 0.2031547212400895,
            "relative_energy_error_percent": 135.82694970948359,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9799999790848233e-05,
              "p95": 3.603000004659407e-05,
              "p99": 9.876536205410957e-05,
              "maximum": 0.001706358976662159
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0035567008890211582,
              "candidate": 0.005263059865683317,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 55.178961578341635,
            "cvrmse_percent": 343.1030232103541,
            "rms_normalized_rmse_percent": 39.626865491107985,
            "reference_energy": 0.20986624550840105,
            "candidate_energy": 0.3256682604833898,
            "relative_energy_error_percent": 55.17896157834164,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9529999917722307e-05,
              "p95": 3.571272736735409e-05,
              "p99": 9.914928477883223e-05,
              "maximum": 0.001706358976662159
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0035567008890211582,
              "candidate": 0.005263059865683317,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": 0.052057915842491136,
            "cvrmse_percent": 26.76264100280946,
            "rms_normalized_rmse_percent": 1.7015066626799185,
            "reference_energy": 0.012266531306522666,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.05205791584249114,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 129.26963317705076,
            "cvrmse_percent": 1024.9000289350188,
            "rms_normalized_rmse_percent": 46.70653464530157,
            "reference_energy": 0.012564350275027891,
            "candidate_energy": 0.028806239786636212,
            "relative_energy_error_percent": 129.26963317705074,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.400000185953104e-07,
              "p95": 3.0258961487561464e-06,
              "p99": 5.5483569667558186e-05,
              "maximum": 0.0002426778810331598
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00011599210847634822,
              "candidate": 0.000358669989509508,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 65.4357565146829,
            "cvrmse_percent": 517.3774717580205,
            "rms_normalized_rmse_percent": 46.596764135684445,
            "reference_energy": 0.024830881581550557,
            "candidate_energy": 0.04107915679370322,
            "relative_energy_error_percent": 65.4357565146829,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.499999696847226e-07,
              "p95": 3.0399999104702147e-06,
              "p99": 5.5483569667558186e-05,
              "maximum": 0.0002426778810331598
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00011599210847634822,
              "candidate": 0.000358669989509508,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      }
    ]
  },
  "controlled_skies": {
    "uniform": {
      "bias_percent": -0.14285745063359942,
      "rms_normalized_error_percent": 0.23884166376199478,
      "absolute_error": {
        "p95": 0.08294996169918668,
        "p99": 0.12752854231676447,
        "maximum": 0.1323968541725975
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.707942667390184,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23884166376199478
    },
    "overcast": {
      "bias_percent": -0.12199264935488821,
      "rms_normalized_error_percent": 0.1965008753788183,
      "absolute_error": {
        "p95": 0.04671456813812256,
        "p99": 0.07486962318420416,
        "maximum": 0.08223724365234375
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6785192489624023,
      "reference_fraction_of_uniform": 0.6444562673568726,
      "rms_normalized_to_uniform_percent": 0.1386034151321233
    },
    "horizon": {
      "bias_percent": -0.21622655631643803,
      "rms_normalized_error_percent": 1.932410021693753,
      "absolute_error": {
        "p95": 0.03716965531048765,
        "p99": 0.047266272546019845,
        "maximum": 0.053834355489216
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5005053603884722,
      "reference_fraction_of_uniform": 0.08768577218686674,
      "rms_normalized_to_uniform_percent": 0.10279894193830659
    },
    "north": {
      "bias_percent": -61.37212835712533,
      "rms_normalized_error_percent": 99.39583427370114,
      "absolute_error": {
        "p95": 4.4519041694002226e-05,
        "p99": 0.00013435381340968944,
        "maximum": 0.00019774245447479188
      },
      "worst_index": [
        65
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1531529708008748e-05,
      "reference_fraction_of_uniform": 2.02026035367453e-06,
      "rms_normalized_to_uniform_percent": 0.00019686722448939063
    },
    "east": {
      "bias_percent": 0.02355742122834375,
      "rms_normalized_error_percent": 0.28438969182403256,
      "absolute_error": {
        "p95": 0.023824095726013187,
        "p99": 0.03004972636699682,
        "maximum": 0.03633308410644531
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1664032936096191,
      "reference_fraction_of_uniform": 0.2043474167585373,
      "rms_normalized_to_uniform_percent": 0.061054229713068196
    },
    "south": {
      "bias_percent": -0.20220520148399293,
      "rms_normalized_error_percent": 0.3157660627565931,
      "absolute_error": {
        "p95": 0.08052244186401368,
        "p99": 0.1020069837570191,
        "maximum": 0.10818052291870117
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9011409282684326,
      "reference_fraction_of_uniform": 0.6834583282470703,
      "rms_normalized_to_uniform_percent": 0.20555359893329497
    },
    "west": {
      "bias_percent": -0.08502717255792767,
      "rms_normalized_error_percent": 0.3586404386990356,
      "absolute_error": {
        "p95": 0.025673905014991765,
        "p99": 0.04045167207717915,
        "maximum": 0.0627131462097168
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1304644346237183,
      "reference_fraction_of_uniform": 0.19805112481117249,
      "rms_normalized_to_uniform_percent": 0.07375963697286789
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.1674691413878313,
          "cvrmse_percent": 1.4599463166514361,
          "absolute_error_percentiles_lux": {
            "p50": 2.7788162231445312,
            "p90": 27.853631591796876,
            "p95": 42.51716308593748,
            "p99": 86.08421752929661
          },
          "maximum_absolute_error_lux": 367.267578125,
          "worst": {
            "sensor_index": 14,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 4212.77978515625,
            "radiance_lux": 4580.04736328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2541894977168937,
            "maximum_error_percentage_points": 1.0091780821917808,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07833287863493836,
            "maximum_error_percentage_points": 0.44940189255963503,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07892123287671253,
            "maximum_error_percentage_points": 0.3039726027397265,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08186643835616358,
            "maximum_error_percentage_points": 0.27246575342466883,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.043139269406392435,
            "maximum_error_percentage_points": 0.2776712328767097,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.7123465735748449,
          "cvrmse_percent": 9.392433365106328,
          "absolute_error_percentiles_lux": {
            "p50": 0.49991703033447266,
            "p90": 5.066214084625246,
            "p95": 7.733053398132323,
            "p99": 14.9530712890625
          },
          "maximum_absolute_error_lux": 65.502197265625,
          "worst": {
            "sensor_index": 10,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 1621.7669677734375,
            "radiance_lux": 1556.2647705078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.034560502283104956,
            "maximum_error_percentage_points": 0.22054794520547816,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.26267163276012206,
            "maximum_error_percentage_points": 0.6601240560563255,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.19394977168949948,
            "maximum_error_percentage_points": 1.508767123287683,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.19405821917808244,
            "maximum_error_percentage_points": 1.5087671232876705,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00010844748858447491,
            "maximum_error_percentage_points": 0.002191780821917802,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 4.075631965204529,
          "cvrmse_percent": 25.415220354445463,
          "absolute_error_percentiles_lux": {
            "p50": 0.10664033889770508,
            "p90": 0.891256332397461,
            "p95": 1.636664950847622,
            "p99": 4.0966203784942525
          },
          "maximum_absolute_error_lux": 43.273529052734375,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              11.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 334.171875,
            "radiance_lux": 290.8983459472656
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.005416666666666667,
            "maximum_error_percentage_points": 0.08,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09681287811853904,
            "maximum_error_percentage_points": 0.39769119305067724,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.039001141552513253,
            "maximum_error_percentage_points": 0.2510958904109515,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.03900114155251143,
            "maximum_error_percentage_points": 0.2510958904109589,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "failed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049893982769688705,
      "metrics": {
        "da": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0049893982769688705,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004983721171339939,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.002191780821917816,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        ]
      }
    },
    "stock": {
      "status": "not_applicable",
      "passed": true
    }
  },
  "darkness": {
    "required": false,
    "passed": true,
    "maximum_lux": null,
    "tolerance_lux": 1e-06
  },
  "performance": {
    "candidate_cold": {
      "study_preparation_seconds": 0.015200415975414217,
      "weather_seconds": 0.15085724997334182,
      "metric_reduction_seconds": 0.07773279200773686,
      "write_seconds": 0.05919812491629273,
      "total_seconds": 0.28801529109477997,
      "cold_end_to_end_seconds": 0.3032157070701942,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.026991834049113095,
      "engine_upload_seconds": 0.000320208,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.058010750100947917,
      "engine_annual_reduction_seconds": 0.0005839999066665769,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.058010750100947917
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.015200415975414217,
      "weather_seconds": 0.13256104104220867,
      "metric_reduction_seconds": 0.013155416934750974,
      "write_seconds": 0.04489304102025926,
      "total_seconds": 0.190937582985498,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.190937582985498,
      "raw_export_seconds": 0.020200124941766262,
      "engine_upload_seconds": 6.05e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006018750136718154,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011363624944351614,
      "full": 0.05310587503481656
    }
  },
  "elapsed_seconds": 147.48497966688592,
  "result_class": "accuracy_failure"
}
```
