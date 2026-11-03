# Foton report

Status: **passed**

```json
{
  "scene": "stacked_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "stacked_rooms",
    "category": "connections",
    "question": "Does an opaque shared slab isolate two storeys?",
    "interactions": [
      "stacked_zones",
      "opaque_adjacency",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 2,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 5.999999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "451c8e7f6a724727378bd675a5f4598137f9290890d3221f5e8099f48c88beb1",
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
      "scene_fingerprint": 6348620744982744529,
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
      "scene_fingerprint": 6348620744982744529,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.07931914448047922,
        "rms_normalized_error_percent": 1.0753890946716322,
        "absolute_error": {
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05,
          "maximum": 0.0003254120238125324
        },
        "worst_index": [
          9,
          72,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.0793895981759524,
        "rms_normalized_error_percent": 1.0753908507263903,
        "absolute_error": {
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05,
          "maximum": 0.0003254120238125324
        },
        "worst_index": [
          9,
          72,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": 0.030664434638164255,
        "rms_normalized_error_percent": 1.0455199059434122,
        "absolute_error": {
          "p95": 4.384664352983231e-05,
          "p99": 0.00014102633576840162,
          "maximum": 0.0005949176847934723
        },
        "worst_index": [
          19,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": 0.05287188894966211,
        "rms_normalized_error_percent": 1.1462103431463342,
        "absolute_error": {
          "p95": 4.787624420714557e-05,
          "p99": 0.00016609951853752136,
          "maximum": 0.0005907770246267319
        },
        "worst_index": [
          27,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.02527621117745279,
        "rms_normalized_error_percent": 0.8864530817817833,
        "absolute_error": {
          "p95": 3.933369007427243e-05,
          "p99": 0.00012204796075820923,
          "maximum": 0.00034997984766960144
        },
        "worst_index": [
          24,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": 0.023100171774437548,
        "rms_normalized_error_percent": 0.9994054911418954,
        "absolute_error": {
          "p95": 4.274194798199439e-05,
          "p99": 0.00013043940998613834,
          "maximum": 0.0005314536392688751
        },
        "worst_index": [
          27,
          0,
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06272969776216655,
                "cvrmse_percent": 21.345709793744327,
                "rms_normalized_rmse_percent": 4.356406716375269,
                "reference_energy": 6.01287330523337,
                "candidate_energy": 6.016645162484565,
                "relative_energy_error_percent": 0.06272969776216655,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.00010242202697554333,
                  "p99": 0.0004371847026050091,
                  "maximum": 0.0008423952385783195
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 98,
                  "rgb_channel": 0,
                  "reference": 0.015384715050458908,
                  "candidate": 0.014542319811880589
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.24251719123705068,
                "cvrmse_percent": 85.62485608330037,
                "rms_normalized_rmse_percent": 4.75229386548823,
                "reference_energy": 2.085268940121523,
                "candidate_energy": 2.0802118044582016,
                "relative_energy_error_percent": 0.24251719123705062,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3253203835338354e-05,
                  "p95": 0.00016672176134306858,
                  "p99": 0.0006276085041463375,
                  "maximum": 0.0013908627443015575
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": -0.0007378081791102886,
                  "candidate": 0.0006530545651912689
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.2455595454090037,
                "cvrmse_percent": 16.983268643339162,
                "rms_normalized_rmse_percent": 3.4716962688429787,
                "reference_energy": 6.010903170035817,
                "candidate_energy": 6.025663516535133,
                "relative_energy_error_percent": 0.2455595454090037,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.30898240767418e-05,
                  "p99": 0.0003481353633105755,
                  "maximum": 0.0008763077203184366
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.007231414085254073,
                  "candidate": 0.00810772180557251
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.8764519308246314,
                "cvrmse_percent": 71.75565447456292,
                "rms_normalized_rmse_percent": 3.974938186384289,
                "reference_energy": 2.078199719091103,
                "candidate_energy": 2.0599852975267368,
                "relative_energy_error_percent": 0.8764519308246314,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7743110220180824e-05,
                  "p95": 0.00014633756763941962,
                  "p99": 0.0005061943084001541,
                  "maximum": 0.0011256607249379158
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.025354520417749882,
                  "candidate": 0.024228859692811966
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.06983300857246,
            "full": 387.7816249150783
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.8131250049919,
            "full": 399.7899160021916
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.58674999512732,
            "full": 402.1085420390591
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.80658301059157,
            "full": 400.98137501627207
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02608292703515428,
                "cvrmse_percent": 7.107518299919888,
                "rms_normalized_rmse_percent": 1.453522076907425,
                "reference_energy": 6.015693014622229,
                "candidate_energy": 6.014123945802567,
                "relative_energy_error_percent": 0.026082927035154278,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4245808385312555e-05,
                  "p99": 0.0001494720345363021,
                  "maximum": 0.00032835034653544426
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 77,
                  "rgb_channel": 0,
                  "reference": 0.010820429772138596,
                  "candidate": 0.01114878011867404
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.17834993216591574,
                "cvrmse_percent": 20.45374264515655,
                "rms_normalized_rmse_percent": 1.768650136121776,
                "reference_energy": 3.8156713827462454,
                "candidate_energy": 3.8224766300690476,
                "relative_energy_error_percent": 0.17834993216591574,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.1190551535710256e-07,
                  "p90": 3.0479597626253963e-05,
                  "p95": 8.133556475513585e-05,
                  "p99": 0.00024952052626758814,
                  "maximum": 0.0007350156083703041
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.021281039342284203,
                  "candidate": 0.022016054950654507
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03764408055728625,
                "cvrmse_percent": 8.399134424005405,
                "rms_normalized_rmse_percent": 1.7164449750794912,
                "reference_energy": 6.015378039579446,
                "candidate_energy": 6.01764247333449,
                "relative_energy_error_percent": 0.03764408055728624,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.620858817361292e-05,
                  "p99": 0.0001759009901434183,
                  "maximum": 0.00044897838961333036
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 27,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.004349838942289352,
                  "candidate": 0.003900860552676022
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.07176678760689403,
                "cvrmse_percent": 22.378814110755314,
                "rms_normalized_rmse_percent": 1.9355931598670448,
                "reference_energy": 3.8192278703356557,
                "candidate_energy": 3.821968807489583,
                "relative_energy_error_percent": 0.07176678760689403,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.281816620097743e-07,
                  "p90": 2.987279003718868e-05,
                  "p95": 9.020892612170415e-05,
                  "p99": 0.000279795378446579,
                  "maximum": 0.0006009549833834171
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.00010086456313729286,
                  "candidate": 0.00070181954652071
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.04633404966444,
            "full": 4851.8318749265745
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 206.69945795089006,
            "full": 4872.177999932319
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.15529203414917,
            "full": 4785.202333005145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.24133400432765,
            "full": 4847.355457954109
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.055377229662407934,
                "cvrmse_percent": 8.97341743369095,
                "rms_normalized_rmse_percent": 1.8336833954577474,
                "reference_energy": 6.0124420982547235,
                "candidate_energy": 6.015771622123793,
                "relative_energy_error_percent": 0.05537722966240794,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.930514842271805e-05,
                  "p99": 0.000185834476724267,
                  "maximum": 0.000408099964261055
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 0.00967432465404272,
                  "candidate": 0.010082424618303776
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.11802605231862526,
                "cvrmse_percent": 22.507398505513617,
                "rms_normalized_rmse_percent": 1.9482868777304643,
                "reference_energy": 3.820636489926759,
                "candidate_energy": 3.8251458363492645,
                "relative_energy_error_percent": 0.11802605231862527,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.2608082872466184e-07,
                  "p90": 3.0039751436561346e-05,
                  "p95": 9.368336759507624e-05,
                  "p99": 0.0002719339681789279,
                  "maximum": 0.0006358260288834572
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03194166533648968,
                  "candidate": 0.03130583930760622
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02130506364015645,
                "cvrmse_percent": 8.648533310237687,
                "rms_normalized_rmse_percent": 1.768466439876223,
                "reference_energy": 6.015734667382276,
                "candidate_energy": 6.014453011282967,
                "relative_energy_error_percent": 0.02130506364015645,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.614308127202092e-05,
                  "p99": 0.00018387602176517248,
                  "maximum": 0.00042873015627264977
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 0.013399739749729633,
                  "candidate": 0.013828469906002283
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.10779501400203326,
                "cvrmse_percent": 21.570891264896286,
                "rms_normalized_rmse_percent": 1.8678922510194464,
                "reference_energy": 3.829279711152619,
                "candidate_energy": 3.825151938551805,
                "relative_energy_error_percent": 0.10779501400203324,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.507838274823371e-07,
                  "p90": 3.0322102247737348e-05,
                  "p95": 8.366538695554482e-05,
                  "p99": 0.00026092492043972015,
                  "maximum": 0.000766996294260025
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03485722094774246,
                  "candidate": 0.03409022465348244
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.27558294311166,
            "full": 5073.212792049162
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 206.76441700197756,
            "full": 5195.040249964222
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.3558330256492,
            "full": 5101.468207896687
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 205.54033294320107,
            "full": 5171.1195420939475
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.004427536965579868,
                "cvrmse_percent": 4.564881007245518,
                "rms_normalized_rmse_percent": 0.9333215859312158,
                "reference_energy": 6.013827643484547,
                "candidate_energy": 6.014093907926508,
                "relative_energy_error_percent": 0.004427536965579868,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3331475676968674e-05,
                  "p99": 9.244680404663086e-05,
                  "maximum": 0.0002038870006799698
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.007613369962200522,
                  "candidate": 0.007409482961520553
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.20844100427252812,
                "cvrmse_percent": 12.705963598098442,
                "rms_normalized_rmse_percent": 1.098891364328406,
                "reference_energy": 3.8165732088831597,
                "candidate_energy": 3.824528512408552,
                "relative_energy_error_percent": 0.2084410042725281,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5984034540394987e-07,
                  "p90": 2.0216240955051035e-05,
                  "p95": 4.7655485104769394e-05,
                  "p99": 0.00015073036774992943,
                  "maximum": 0.00040181446820497513
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.01801931019872427,
                  "candidate": 0.018421124666929245
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.014444636799393921,
                "cvrmse_percent": 4.226937977193911,
                "rms_normalized_rmse_percent": 0.8644269489764909,
                "reference_energy": 6.016190425241803,
                "candidate_energy": 6.017059442097889,
                "relative_energy_error_percent": 0.014444636799393923,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2682559210807063e-05,
                  "p99": 8.354755118489265e-05,
                  "maximum": 0.00018785218708217144
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 10,
                  "sky_patch_index": 41,
                  "rgb_channel": 0,
                  "reference": 0.0026227683993056417,
                  "candidate": 0.002810620586387813
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.12025560705711243,
                "cvrmse_percent": 13.41137259252488,
                "rms_normalized_rmse_percent": 1.1612005507338208,
                "reference_energy": 3.8256580016386117,
                "candidate_energy": 3.830258569892411,
                "relative_energy_error_percent": 0.12025560705711243,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5811010811717097e-07,
                  "p90": 2.027068694587797e-05,
                  "p95": 4.7403026837855573e-05,
                  "p99": 0.00016447948291897774,
                  "maximum": 0.00043708086013793945
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03454647958278656,
                  "candidate": 0.03410939872264862
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 328.47449998371303,
            "full": 9119.072875007987
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 327.39658292848617,
            "full": 9194.38708294183
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 325.11145900934935,
            "full": 8986.357041983865
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 320.74525009375066,
            "full": 9027.306500007398
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2966.9716249918565,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/stacked_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10953.258124995045,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6021984782308624,
            "cvrmse_percent": 35.549988406770524,
            "rms_normalized_rmse_percent": 3.0740243699743366,
            "reference_energy": 3.8174038695385235,
            "candidate_energy": 3.7944155215282365,
            "relative_energy_error_percent": 0.6021984782308623,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.299221411154576e-07,
              "p90": 7.018359610810876e-05,
              "p95": 0.0001029773258778732,
              "p99": 0.00022949418053030968,
              "maximum": 0.0019469168037176132
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02086532674729824,
              "candidate": 0.018918409943580627,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.26178466946610435,
            "cvrmse_percent": 13.796282278290217,
            "rms_normalized_rmse_percent": 3.073368263244153,
            "reference_energy": 9.834511608809137,
            "candidate_energy": 9.80876636510041,
            "relative_energy_error_percent": 0.26178466946610435,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.254756783619086e-07,
              "p90": 7.077277405187488e-05,
              "p95": 0.00010329890574212172,
              "p99": 0.00022443593479692936,
              "maximum": 0.0019469168037176132
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02086532674729824,
              "candidate": 0.018918409943580627,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.32048456297228317,
            "cvrmse_percent": 35.1133884866722,
            "rms_normalized_rmse_percent": 3.042065561776597,
            "reference_energy": 3.827479751836144,
            "candidate_energy": 3.815213270080619,
            "relative_energy_error_percent": 0.32048456297228317,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.403181203040731e-07,
              "p90": 6.891414523124695e-05,
              "p95": 0.00010293520426785089,
              "p99": 0.00024269343703053892,
              "maximum": 0.0015237145125865936
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0289638452231884,
              "candidate": 0.027440130710601807,
              "position": [
                3.5,
                0.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.15256242377060286,
            "cvrmse_percent": 13.60848946664683,
            "rms_normalized_rmse_percent": 3.0324258043914085,
            "reference_energy": 9.844583248466769,
            "candidate_energy": 9.829564113652793,
            "relative_energy_error_percent": 0.15256242377060286,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.403181203040731e-07,
              "p90": 6.871660298202187e-05,
              "p95": 0.00010096935293404381,
              "p99": 0.0002481243573129177,
              "maximum": 0.0015237145125865936
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0289638452231884,
              "candidate": 0.027440130710601807,
              "position": [
                3.5,
                0.5,
                3.75
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.38946175160619,
            "cvrmse_percent": 441.4189713346173,
            "rms_normalized_rmse_percent": 24.447043261163966,
            "reference_energy": 2.080391863152599,
            "candidate_energy": 3.7944155215282365,
            "relative_energy_error_percent": 82.38946175160618,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022752357108402066,
              "p95": 0.0003236516815377396,
              "p99": 0.000565017107874155,
              "maximum": 0.00853351503610611
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016120264306664467,
              "candidate": 0.024653779342770576,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.133273809178007,
            "cvrmse_percent": 113.39623943490727,
            "rms_normalized_rmse_percent": 24.44442285530074,
            "reference_energy": 8.097499602423213,
            "candidate_energy": 9.80876636510041,
            "relative_energy_error_percent": 21.133273809178007,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002268899988848716,
              "p95": 0.00032092222263599955,
              "p99": 0.0005675493739545345,
              "maximum": 0.00853351503610611
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016120264306664467,
              "candidate": 0.024653779342770576,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 84.28557271214876,
            "cvrmse_percent": 459.8010558826375,
            "rms_normalized_rmse_percent": 25.401316245101928,
            "reference_energy": 2.0702723571529518,
            "candidate_energy": 3.815213270080619,
            "relative_energy_error_percent": 84.28557271214876,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002303200017195195,
              "p95": 0.0003192379939719103,
              "p99": 0.0006210505962371826,
              "maximum": 0.008942462503910065
            },
            "worst": {
              "global_sensor_index": 67,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010587707161903381,
              "candidate": 0.019530169665813446,
              "position": [
                5.5,
                4.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.542071141087817,
            "cvrmse_percent": 117.68562532482817,
            "rms_normalized_rmse_percent": 25.397432820596848,
            "reference_energy": 8.087375853783577,
            "candidate_energy": 9.829564113652793,
            "relative_energy_error_percent": 21.542071141087817,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022919000184629112,
              "p95": 0.00031701539410278196,
              "p99": 0.0006154528819024563,
              "maximum": 0.008942462503910065
            },
            "worst": {
              "global_sensor_index": 67,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010587707161903381,
              "candidate": 0.019530169665813446,
              "position": [
                5.5,
                4.5,
                3.75
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
      "bias_percent": 0.18631893183578702,
      "rms_normalized_error_percent": 0.4549386828470529,
      "absolute_error": {
        "p95": 0.170340501274745,
        "p99": 0.2153670134558767,
        "maximum": 0.24947104860717983
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 12.029705496282109,
      "rms_normalized_to_uniform_percent": 0.4549386828470529
    },
    "overcast": {
      "bias_percent": 0.12035193989518247,
      "rms_normalized_error_percent": 0.3820630193248458,
      "absolute_error": {
        "p95": 0.10742402076721191,
        "p99": 0.12178265571594259,
        "maximum": 0.14531421661376953
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.680765151977539,
      "rms_normalized_to_uniform_percent": 0.2695243602169208
    },
    "horizon": {
      "bias_percent": 1.4636471629570265,
      "rms_normalized_error_percent": 4.0550743306655965,
      "absolute_error": {
        "p95": 0.08822265445945596,
        "p99": 0.12669952711303342,
        "maximum": 0.19576151621092008
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.1213162085007662,
      "rms_normalized_to_uniform_percent": 0.22960789871653864
    },
    "north": {
      "bias_percent": 11.62714384103895,
      "rms_normalized_error_percent": 318.9217306064281,
      "absolute_error": {
        "p95": 6.169021198729754e-05,
        "p99": 0.00021137648195008302,
        "maximum": 0.00021970817329020065
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 9.979901733458973e-06,
      "rms_normalized_to_uniform_percent": 0.00021627874221287954
    },
    "east": {
      "bias_percent": 0.1781793911047038,
      "rms_normalized_error_percent": 0.7412198085093302,
      "absolute_error": {
        "p95": 0.07176654338836672,
        "p99": 0.09323288440704378,
        "maximum": 0.12907123565673828
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.451479911804199,
      "rms_normalized_to_uniform_percent": 0.1584913060251748
    },
    "south": {
      "bias_percent": 0.2280946125513917,
      "rms_normalized_error_percent": 0.5250944978433583,
      "absolute_error": {
        "p95": 0.12687201499938966,
        "p99": 0.18221697092056321,
        "maximum": 0.23693633079528809
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 8.30610179901123,
      "rms_normalized_to_uniform_percent": 0.34218022448990787
    },
    "west": {
      "bias_percent": 0.08354560852631669,
      "rms_normalized_error_percent": 0.6357785399569631,
      "absolute_error": {
        "p95": 0.05637612938880921,
        "p99": 0.07128492593765261,
        "maximum": 0.07392311096191406
      },
      "worst_index": [
        59
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.3691625595092773,
      "rms_normalized_to_uniform_percent": 0.13022082166792845
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
        "identifier": "stacked_rooms_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.032268753263355814,
          "cvrmse_percent": 2.9299243077281716,
          "absolute_error_percentiles_lux": {
            "p50": 5.12419319152832,
            "p90": 47.41649169921876,
            "p95": 68.56060791015624,
            "p99": 122.03854431152342
          },
          "maximum_absolute_error_lux": 422.091796875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 9204.1376953125,
            "radiance_lux": 9626.2294921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7307115677321158,
            "maximum_error_percentage_points": 2.764520547945203,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3317807756555615,
            "maximum_error_percentage_points": 1.6222658911034458,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.24711187214611885,
            "maximum_error_percentage_points": 0.7993150684931507,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.24054414003044144,
            "maximum_error_percentage_points": 0.765068493150693,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.043584474885844736,
            "maximum_error_percentage_points": 0.19589041095890636,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 52.77777777777778,
          "radiance_percent": 55.55555555555556,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.01652345889854443,
          "cvrmse_percent": 2.810067213657622,
          "absolute_error_percentiles_lux": {
            "p50": 4.507843017578125,
            "p90": 45.407525634765626,
            "p95": 67.19591369628903,
            "p99": 118.82116455078122
          },
          "maximum_absolute_error_lux": 414.367431640625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              3.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 3829.708251953125,
            "radiance_lux": 4244.07568359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.8395357686453576,
            "maximum_error_percentage_points": 3.7761643835616425,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3746071793568958,
            "maximum_error_percentage_points": 1.8550997848162751,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21500761035007582,
            "maximum_error_percentage_points": 1.2336986301369848,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22779299847792955,
            "maximum_error_percentage_points": 1.1480821917808157,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.041027397260274094,
            "maximum_error_percentage_points": 0.16876712328767063,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 58.333333333333336,
          "radiance_percent": 55.55555555555556,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
      "maximum_error_percentage_points": 0.0049852846746460955,
      "metrics": {
        "da": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.0049852846746460955,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004288045804798912,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.008779332973062992,
      "weather_seconds": 0.10410774999763817,
      "metric_reduction_seconds": 0.042950417031534016,
      "write_seconds": 0.049722541007213295,
      "total_seconds": 0.1969647080404684,
      "cold_end_to_end_seconds": 0.2057440410135314,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.019154916051775217,
      "engine_upload_seconds": 0.000261792,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024665208300575614,
      "engine_annual_reduction_seconds": 0.0006048749200999737,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024665208300575614
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008779332973062992,
      "weather_seconds": 0.10493962501641363,
      "metric_reduction_seconds": 0.012939499923959374,
      "write_seconds": 0.02893408399540931,
      "total_seconds": 0.14697929099202156,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14697929099202156,
      "raw_export_seconds": 0.016715875011868775,
      "engine_upload_seconds": 5.65e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006583749782294035,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015689834021031857,
      "full": 0.016952625010162592
    }
  },
  "elapsed_seconds": 97.38020200002939,
  "result_class": "passed"
}
```
