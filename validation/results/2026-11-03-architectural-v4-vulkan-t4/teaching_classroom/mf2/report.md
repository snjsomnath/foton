# Foton report

Status: **passed**

```json
{
  "scene": "teaching_classroom",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_classroom",
    "category": "teaching",
    "question": "How is a 9 x 7 m classroom with three windows lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 3,
    "shades": 0,
    "sensors": 63,
    "floor_area": 63.0,
    "aperture_area": 11.520000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2bcb2a24e7adf03fc874a9e0baaa279ad48c82fac4cac67d688d5287569788b7",
  "weather_sha256": "98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee",
  "gpu_executed": true,
  "candidate": {
    "capabilities": {
      "name": "Vulkan device: Tesla T4",
      "hardware_acceleration": true,
      "supports_ray_tracing": true,
      "supports_async_jobs": true
    },
    "direct": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.0",
      "scene_fingerprint": 117564074192331588,
      "basis": "ReinhartMf2",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
      "used_reference_fallback": false
    },
    "full": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.0",
      "scene_fingerprint": 117564074192331588,
      "basis": "ReinhartMf2",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
      "used_reference_fallback": false
    }
  },
  "sky_bin_audit": {
    "passed": true,
    "ray_count": 9248,
    "command": [
      "/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "498a85b8f85c453dbf933ad47ef2d37922a017b4fcfa2c57d17b809b2104a50a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ea42e09dbe931b70ba70272788b8827813b1766f826a508ce4884363a557779a",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013817357830703259,
          "p95": 2.44686380028723e-06,
          "p99": 2.4068605853244662e-05
        },
        "bias_percent": 0.024707531623630725,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7650893574334957,
        "worst_index": [
          5,
          356,
          0
        ]
      }
    ],
    "passed": true,
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0008470229804515839,
          "p95": 6.0673973348457274e-05,
          "p99": 0.00013337284326553345
        },
        "bias_percent": 0.06672484964576007,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.188940132420948,
        "worst_index": [
          27,
          0,
          0
        ]
      }
    ],
    "passed": true
  },
  "sample_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006679147481918335,
          "p95": 4.891807620879243e-05,
          "p99": 0.00010832736734300852
        },
        "bias_percent": -0.006624235557337425,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9828856696750672,
        "worst_index": [
          25,
          0,
          0
        ]
      }
    ],
    "passed": true
  },
  "oracle_levels": [
    {
      "material_bounces": 1,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000693134032189846,
                  "p50": 0.0,
                  "p90": 4.421529592946172e-05,
                  "p95": 0.00010479135671630472,
                  "p99": 0.00026166997849941254
                },
                "candidate_energy": 23.03604892486328,
                "cvrmse_percent": 24.454942505899247,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.057215856685032006,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.04923674312522,
                "relative_energy_error_percent": 0.057215856685032006,
                "rms_normalized_rmse_percent": 6.927255911411204,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002544765011407435,
                  "global_sensor_index": 45,
                  "local_sensor_index": 45,
                  "reference": 0.001851630979217589,
                  "rgb_channel": 0,
                  "sky_patch_index": 214
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001295110210776329,
                  "p50": 0.0,
                  "p90": 6.80922603351064e-05,
                  "p95": 0.00018159575429308443,
                  "p99": 0.0003911969834007323
                },
                "candidate_energy": 8.684108160290663,
                "cvrmse_percent": 100.94453335308597,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.13903115142548703,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.696198585314072,
                "relative_energy_error_percent": 0.13903115142548703,
                "rms_normalized_rmse_percent": 4.324840948442159,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03678290545940399,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.03548779524862766,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.1074589844793,
            "full": 368.82383306510746
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.05004099477082,
            "full": 372.87945800926536
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.64699995331466,
            "full": 384.0389590477571
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.30520794447511,
            "full": 364.51670806854963
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 20000
    },
    {
      "material_bounces": 8,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043752091005444527,
                  "p50": 0.0,
                  "p90": 2.34440085478127e-05,
                  "p95": 8.571432263124705e-05,
                  "p99": 0.00018209055997431278
                },
                "candidate_energy": 23.06627672313698,
                "cvrmse_percent": 17.263867829458956,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03283916407074696,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.05870443735421,
                "relative_energy_error_percent": 0.03283916407074697,
                "rms_normalized_rmse_percent": 4.896270249735342,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003011395107023418,
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "reference": 0.003448916017077863,
                  "rgb_channel": 0,
                  "sky_patch_index": 260
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009336695075035095,
                  "p50": 5.000000058430487e-08,
                  "p90": 4.648062167689204e-05,
                  "p95": 0.0001228257904585916,
                  "p99": 0.0002623570617288351
                },
                "candidate_energy": 15.382840342101822,
                "cvrmse_percent": 39.18680332943932,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03279029069620084,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.38788607467771,
                "relative_energy_error_percent": 0.03279029069620084,
                "rms_normalized_rmse_percent": 2.259900755359122,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07018974050879478,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.0711234100162983,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 255.68254198879004,
            "full": 4278.152624960057
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.85116706229746,
            "full": 4249.249416985549
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 235.67758302669972,
            "full": 4176.862291991711
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.13845798373222,
            "full": 4245.698250015266
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 40000
    },
    {
      "material_bounces": 12,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00034817447885870934,
                  "p50": 0.0,
                  "p90": 2.3439002688974142e-05,
                  "p95": 7.045020174700767e-05,
                  "p99": 0.00016388104995712638
                },
                "candidate_energy": 23.082645796598626,
                "cvrmse_percent": 15.984979964790146,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05383217164584539,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.0702265926202,
                "relative_energy_error_percent": 0.05383217164584539,
                "rms_normalized_rmse_percent": 4.5351837454980775,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003383544972166419,
                  "global_sensor_index": 62,
                  "local_sensor_index": 62,
                  "reference": 0.0037317194510251284,
                  "rgb_channel": 0,
                  "sky_patch_index": 415
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011651627719402313,
                  "p50": 5.000000058430487e-08,
                  "p90": 4.4871310819871724e-05,
                  "p95": 0.0001156715006800368,
                  "p99": 0.0002519287809263915
                },
                "candidate_energy": 15.383364280925946,
                "cvrmse_percent": 37.43645690221972,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17789507466335766,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.4107792982648,
                "relative_energy_error_percent": 0.17789507466335766,
                "rms_normalized_rmse_percent": 2.159450102215414,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0624086819589138,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.06124351918697357,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.96979189943522,
            "full": 4448.608582955785
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 242.47433291748166,
            "full": 4475.389875005931
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.2178329033777,
            "full": 4391.536750015803
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.97950001060963,
            "full": 4480.51420901902
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 40000
    },
    {
      "material_bounces": 12,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002228909870609641,
                  "p50": 0.0,
                  "p90": 1.2046482879668474e-05,
                  "p95": 4.568509757518768e-05,
                  "p99": 9.93469511740841e-05
                },
                "candidate_energy": 23.060476549244868,
                "cvrmse_percent": 9.335976957708908,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.012368577379732737,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.057624649098216,
                "relative_energy_error_percent": 0.012368577379732739,
                "rms_normalized_rmse_percent": 2.6491383330777114,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016290320199914277,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.0014061410329304636,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007110405713319778,
                  "p50": 5.000000058430487e-08,
                  "p90": 2.6735826395452023e-05,
                  "p95": 6.764461140846828e-05,
                  "p99": 0.0001456781756132841
                },
                "candidate_energy": 15.4073146025098,
                "cvrmse_percent": 22.342899559268783,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05960310270313654,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.416503316814953,
                "relative_energy_error_percent": 0.05960310270313653,
                "rms_normalized_rmse_percent": 1.2883959682384816,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04938413389027119,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.050095174461603165,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 355.0915829837322,
            "full": 7891.497667063959
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 355.41750001721084,
            "full": 7843.697541975416
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 377.8668330051005,
            "full": 7897.587749990635
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 364.282957976684,
            "full": 7788.252791040577
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 80000
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/teaching_classroom/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 8579.085792065598,
      "invocation_count": 4,
      "sample_count": 256,
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "worker_pool_size": 12
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 34271.45479095634,
      "invocation_count": 4,
      "sample_count": 1024,
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "worker_pool_size": 12
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      63,
      578,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0012212706380211487,
            "cvrmse_percent": 1.5292991799710522,
            "rms_normalized_rmse_percent": 0.43408052330862146,
            "reference_energy": 23.06225351042906,
            "candidate_energy": 23.062535162959648,
            "relative_energy_error_percent": 0.0012212706380211487,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.587935447692871e-08,
              "p95": 1.7873616855013e-06,
              "p99": 1.48756371345371e-05,
              "maximum": 7.128791185095906e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888362295926,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.432112899485063,
            "cvrmse_percent": 46.96869608836547,
            "rms_normalized_rmse_percent": 2.7078290161686107,
            "reference_energy": 15.408706009230041,
            "candidate_energy": 15.188035942828128,
            "relative_energy_error_percent": 1.4321128994850627,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.072431719099768e-08,
              "p90": 1.8143487977795303e-05,
              "p95": 3.100537578575313e-05,
              "p99": 6.366634625010192e-05,
              "maximum": 0.0025103986263275146
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07118833065032959,
              "candidate": 0.06867793202400208,
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
            "nmbe_percent": -0.5728695530942075,
            "cvrmse_percent": 18.804494851836242,
            "rms_normalized_rmse_percent": 2.706707052590678,
            "reference_energy": 38.470959519659104,
            "candidate_energy": 38.25057110578777,
            "relative_energy_error_percent": 0.5728695530942306,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.1015604185522534e-08,
              "p90": 1.813791459426284e-05,
              "p95": 3.0849984614178536e-05,
              "p99": 6.235961336642504e-05,
              "maximum": 0.0025103986263275146
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07118833065032959,
              "candidate": 0.06867793202400208,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      }
    ]
  },
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      63,
      578,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0012212706380211487,
            "cvrmse_percent": 1.5292991799710522,
            "rms_normalized_rmse_percent": 0.43408052330862146,
            "reference_energy": 23.06225351042906,
            "candidate_energy": 23.062535162959648,
            "relative_energy_error_percent": 0.0012212706380211487,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.587935447692871e-08,
              "p95": 1.7873616855013e-06,
              "p99": 1.48756371345371e-05,
              "maximum": 7.128791185095906e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888362295926,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 75.16822591138697,
            "cvrmse_percent": 748.3672723829051,
            "rms_normalized_rmse_percent": 31.97640126720811,
            "reference_energy": 8.67054276756297,
            "candidate_energy": 15.188035942828128,
            "relative_energy_error_percent": 75.16822591138695,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012754999625030905,
              "p95": 0.0001788735418813301,
              "p99": 0.0002916458761319518,
              "maximum": 0.017359957098960876
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045459672808647156,
              "candidate": 0.06281962990760803,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.53955400178863,
            "cvrmse_percent": 204.48270524936413,
            "rms_normalized_rmse_percent": 31.976685054567035,
            "reference_energy": 31.73279627799203,
            "candidate_energy": 38.25057110578777,
            "relative_energy_error_percent": 20.539554001788613,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012739235535264015,
              "p95": 0.00017867954356916006,
              "p99": 0.0002916691591963172,
              "maximum": 0.017359957098960876
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045459672808647156,
              "candidate": 0.06281962990760803,
              "position": [
                0.5,
                1.5,
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
      "bias_percent": 0.13091347100326428,
      "rms_normalized_error_percent": 0.19587422144629282,
      "absolute_error": {
        "p95": 0.15653009808585824,
        "p99": 0.18227833917967057,
        "maximum": 0.19601594500092645
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.720834366505294,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19587422144629282
    },
    "overcast": {
      "bias_percent": 0.07941514084109857,
      "rms_normalized_error_percent": 0.12497809070684679,
      "absolute_error": {
        "p95": 0.05934338569641113,
        "p99": 0.0717722320556641,
        "maximum": 0.08089447021484375
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.26297950744629,
      "reference_fraction_of_uniform": 0.6460493803024292,
      "rms_normalized_to_uniform_percent": 0.08800592907265907
    },
    "horizon": {
      "bias_percent": 0.9583324554253433,
      "rms_normalized_error_percent": 1.7499487998524865,
      "absolute_error": {
        "p95": 0.13617599428224988,
        "p99": 0.1477305398696204,
        "maximum": 0.1539984594971524
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.9995586327642494,
      "reference_fraction_of_uniform": 0.1122554255463,
      "rms_normalized_to_uniform_percent": 0.15080226463347227
    },
    "north": {
      "bias_percent": -48.59842518644256,
      "rms_normalized_error_percent": 94.15917960909971,
      "absolute_error": {
        "p95": 4.833125444747565e-05,
        "p99": 0.00012829783281858944,
        "maximum": 0.00021108377040945925
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3424632925307378e-05,
      "reference_fraction_of_uniform": 5.024032248002186e-07,
      "rms_normalized_to_uniform_percent": 8.904439845587032e-05
    },
    "east": {
      "bias_percent": -0.011987849175055132,
      "rms_normalized_error_percent": 0.23537058165467897,
      "absolute_error": {
        "p95": 0.029224681854248046,
        "p99": 0.05784494400024417,
        "maximum": 0.0642242431640625
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.906745433807373,
      "reference_fraction_of_uniform": 0.18362994492053986,
      "rms_normalized_to_uniform_percent": 0.04718746286155057
    },
    "south": {
      "bias_percent": 0.174373226213997,
      "rms_normalized_error_percent": 0.2858385699327537,
      "absolute_error": {
        "p95": 0.1558600902557373,
        "p99": 0.17777082443237305,
        "maximum": 0.1806645393371582
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.516395568847656,
      "reference_fraction_of_uniform": 0.6929572224617004,
      "rms_normalized_to_uniform_percent": 0.1822927555106839
    },
    "west": {
      "bias_percent": 0.18874749671384253,
      "rms_normalized_error_percent": 0.24982973219267737,
      "absolute_error": {
        "p95": 0.03611496686935424,
        "p99": 0.05463450431823735,
        "maximum": 0.06424188613891602
      },
      "worst_index": [
        59
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.959685325622559,
      "reference_fraction_of_uniform": 0.18561117351055145,
      "rms_normalized_to_uniform_percent": 0.05040966025709495
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": true,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "teaching_classroom_grid",
        "sensor_count": 63,
        "illuminance": {
          "nmbe_percent": 0.012730848749942864,
          "cvrmse_percent": 1.1929140658497202,
          "absolute_error_percentiles_lux": {
            "p50": 3.685302734375,
            "p90": 38.81916503906251,
            "p95": 59.412109375,
            "p99": 120.39950195312457
          },
          "maximum_absolute_error_lux": 388.244140625,
          "worst": {
            "sensor_index": 5,
            "position": [
              0.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5244.5,
            "foton_lux": 18069.55859375,
            "radiance_lux": 17681.314453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07039791258969334,
            "maximum_error_percentage_points": 0.5186301369862889,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03462045436890503,
            "maximum_error_percentage_points": 0.24736561044714733,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.033820395738203814,
            "maximum_error_percentage_points": 0.33178082191781044,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.05766253533376717,
            "maximum_error_percentage_points": 0.2735616438356203,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05769080234833651,
            "maximum_error_percentage_points": 0.22164383561643852,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004881207191772319,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.37352366000050097,
      "weather_seconds": 0.2381179219992191,
      "metric_reduction_seconds": 1.7279932880010165,
      "write_seconds": 0.052244311998947524,
      "total_seconds": 2.018756666999252,
      "cold_end_to_end_seconds": 2.392280326999753,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03928769100093632,
      "engine_upload_seconds": 0.046354807,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.094411294,
      "engine_annual_reduction_seconds": 0.030747466000000005,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.094411294
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37352366000050097,
      "weather_seconds": 0.25045938800030854,
      "metric_reduction_seconds": 1.7032862699998077,
      "write_seconds": 0.02325917800044408,
      "total_seconds": 1.9772918700000446,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.9772918700000446,
      "raw_export_seconds": 0.010383959001046605,
      "engine_upload_seconds": 0.047241173,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.3e-08,
      "engine_annual_reduction_seconds": 0.031026036,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020951180998963537,
      "full": 0.1082861779977975
    }
  },
  "elapsed_seconds": 7.2707455919990025,
  "result_class": "passed"
}
```
