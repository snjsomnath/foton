# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth4",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth4",
    "category": "teaching",
    "question": "How does daylight fall off in a 4 m deep room?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 24,
    "floor_area": 24.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c9fc8d3ed0f677318d9caa17170ff2f05ada7657d7fa94466ea8f4acf71e3c09",
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
      "scene_fingerprint": 1264132388842763511,
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
      "scene_fingerprint": 1264132388842763511,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": -0.06804422780189273,
        "rms_normalized_error_percent": 0.9156604833783333,
        "absolute_error": {
          "p95": 1.6129284631460905e-05,
          "p99": 0.00015342188999056816,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          11,
          121,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": 0.06768560119398422,
        "rms_normalized_error_percent": 0.8127801835763201,
        "absolute_error": {
          "p95": 7.782771717756987e-05,
          "p99": 0.00018181279301643372,
          "maximum": 0.0006156228482723236
        },
        "worst_index": [
          6,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": -0.018317443771285642,
        "rms_normalized_error_percent": 0.762164025912074,
        "absolute_error": {
          "p95": 7.198099046945572e-05,
          "p99": 0.00014249980449676514,
          "maximum": 0.0007103979587554932
        },
        "worst_index": [
          10,
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0910514049327426,
                "cvrmse_percent": 12.239131548850775,
                "rms_normalized_rmse_percent": 3.531767157661053,
                "reference_energy": 8.488578093340038,
                "candidate_energy": 8.496307062952837,
                "relative_energy_error_percent": 0.0910514049327426,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.986704051494598e-05,
                  "p95": 0.0002097530523315072,
                  "p99": 0.0004720049910247326,
                  "maximum": 0.0006939796730875969
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 0.014547820203006268,
                  "candidate": 0.015241799876093864
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.23177379300642936,
                "cvrmse_percent": 57.61315068174243,
                "rms_normalized_rmse_percent": 3.867145657896684,
                "reference_energy": 2.757012013012016,
                "candidate_energy": 2.750621981695815,
                "relative_energy_error_percent": 0.23177379300642936,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00013165827840566635,
                  "p95": 0.0003313319757580757,
                  "p99": 0.00077770184725523,
                  "maximum": 0.0013161487877368927
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03622201830148697,
                  "candidate": 0.034905869513750076
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 109.99258304946125,
            "full": 180.75800000224262
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.94133292417973,
            "full": 182.12216603569686
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.22304193302989,
            "full": 179.00362494401634
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 101.48808395024389,
            "full": 201.739750104025
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0013216774893864544,
                "cvrmse_percent": 5.315809523762699,
                "rms_normalized_rmse_percent": 1.5330545130991258,
                "reference_energy": 8.483425591985906,
                "candidate_energy": 8.483537715512284,
                "relative_energy_error_percent": 0.0013216774893864544,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.223400563001633e-05,
                  "p95": 9.256962221115828e-05,
                  "p99": 0.00020874547772109509,
                  "maximum": 0.0003802347928285599
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.012749805115163326,
                  "candidate": 0.012369570322334766
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.008092838406613808,
                "cvrmse_percent": 16.794965117860414,
                "rms_normalized_rmse_percent": 1.6313447891453972,
                "reference_energy": 4.930804096838067,
                "candidate_energy": 4.93120313884577,
                "relative_energy_error_percent": 0.008092838406613808,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7088503884442616e-07,
                  "p90": 6.794510409235954e-05,
                  "p95": 0.00015850947238504887,
                  "p99": 0.0003725457936525345,
                  "maximum": 0.0010192934423685074
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05508110672235489,
                  "candidate": 0.056100400164723396
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.05191700905561,
            "full": 1500.3609999548644
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 129.6467089559883,
            "full": 1521.990125067532
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 127.07150005735457,
            "full": 1499.5084169786423
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.2673330111429,
            "full": 1522.0389170572162
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.00724597855888876,
                "cvrmse_percent": 5.473562151151977,
                "rms_normalized_rmse_percent": 1.5783690853670134,
                "reference_energy": 8.485306799632781,
                "candidate_energy": 8.484691956121424,
                "relative_energy_error_percent": 0.007245978558888761,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.3791020289063454e-05,
                  "p95": 0.00011299399193376303,
                  "p99": 0.00021080300211906433,
                  "maximum": 0.00036383001133799553
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.0072581099811941385,
                  "candidate": 0.007621939992532134
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.15114375676201394,
                "cvrmse_percent": 16.680629288635718,
                "rms_normalized_rmse_percent": 1.6203248792300486,
                "reference_energy": 4.9423005434283915,
                "candidate_energy": 4.934830564716584,
                "relative_energy_error_percent": 0.15114375676201394,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.705108611029573e-07,
                  "p90": 6.658793427050114e-05,
                  "p95": 0.0001765026245266199,
                  "p99": 0.00037318840622901917,
                  "maximum": 0.0011041685938835144
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04340306483209133,
                  "candidate": 0.04229889623820782
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.28500005044043,
            "full": 1610.8387920539826
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.57166603580117,
            "full": 1585.6069580186158
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.29899993166327,
            "full": 1610.3127910755575
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 128.96929099224508,
            "full": 1603.2297500642017
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08166947054818983,
                "cvrmse_percent": 2.755552173336455,
                "rms_normalized_rmse_percent": 0.7948587064325221,
                "reference_energy": 8.481420509557665,
                "candidate_energy": 8.474493778332544,
                "relative_energy_error_percent": 0.08166947054818983,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.84597447514534e-05,
                  "p95": 4.527461715042591e-05,
                  "p99": 0.00010862821363843977,
                  "maximum": 0.000322599895298481
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 117,
                  "rgb_channel": 0,
                  "reference": 0.017926005646586418,
                  "candidate": 0.017603405751287937
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.24860398262878575,
                "cvrmse_percent": 8.715252397966871,
                "rms_normalized_rmse_percent": 0.8462490339027212,
                "reference_energy": 4.937012114524265,
                "candidate_energy": 4.949285723263838,
                "relative_energy_error_percent": 0.24860398262878572,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.8476074476202484e-07,
                  "p90": 3.844770253635943e-05,
                  "p95": 8.798018097877502e-05,
                  "p99": 0.0001851433189585805,
                  "maximum": 0.0005467496812343597
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.048308610916137695,
                  "candidate": 0.048855360597372055
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.04462505411357,
            "full": 2796.411207993515
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 183.76433302182704,
            "full": 2839.6864579990506
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 193.69058310985565,
            "full": 2821.6275410959497
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.25225008185953,
            "full": 2819.761125021614
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 471.12841601483524,
      "worker_pool_size": 12,
      "invocation_count": 2
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth4/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1585.3654579259455,
      "worker_pool_size": 12,
      "invocation_count": 2
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.3282726027442056,
            "cvrmse_percent": 21.783798606411036,
            "rms_normalized_rmse_percent": 2.113335281661754,
            "reference_energy": 4.934802363818056,
            "candidate_energy": 4.951001967978044,
            "relative_energy_error_percent": 0.32827260274420555,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2781539453499136e-06,
              "p90": 9.61015175562352e-05,
              "p95": 0.00014495663344860077,
              "p99": 0.0003238528734073043,
              "maximum": 0.0021329857409000397
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034340325742959976,
              "candidate": 0.032207340002059937,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.07452912096200845,
            "cvrmse_percent": 8.047060432154888,
            "rms_normalized_rmse_percent": 2.123198498339845,
            "reference_energy": 13.42110608953812,
            "candidate_energy": 13.43110872193003,
            "relative_energy_error_percent": 0.07452912096200846,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.265358321234089e-06,
              "p90": 9.566498920321465e-05,
              "p95": 0.00014418878708966076,
              "p99": 0.0003404873423278332,
              "maximum": 0.0021329857409000397
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034340325742959976,
              "candidate": 0.032207340002059937,
              "position": [
                5.5,
                0.5,
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
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.38699940171942,
            "cvrmse_percent": 450.2497080441249,
            "rms_normalized_rmse_percent": 30.254481178560887,
            "reference_energy": 2.759955840997577,
            "candidate_energy": 4.951001967978044,
            "relative_energy_error_percent": 79.38699940171944,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00040726899169385433,
              "p95": 0.000543949194252491,
              "p99": 0.0009045426268130541,
              "maximum": 0.016524996608495712
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0224040225148201,
              "candidate": 0.03892901912331581,
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
            "nmbe_percent": 19.42734063935593,
            "cvrmse_percent": 110.48282878213337,
            "rms_normalized_rmse_percent": 30.25081117153026,
            "reference_energy": 11.24625956671764,
            "candidate_energy": 13.43110872193003,
            "relative_energy_error_percent": 19.42734063935593,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00040283999987877905,
              "p95": 0.0005457329098135233,
              "p99": 0.0009423792362213135,
              "maximum": 0.016524996608495712
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0224040225148201,
              "candidate": 0.03892901912331581,
              "position": [
                5.5,
                3.5,
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
      "bias_percent": 0.3333313396352245,
      "rms_normalized_error_percent": 0.46098534085838805,
      "absolute_error": {
        "p95": 0.35662883637794884,
        "p99": 0.36804467295437066,
        "maximum": 0.369889856588161
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 25.167078903791406,
      "rms_normalized_to_uniform_percent": 0.46098534085838805
    },
    "overcast": {
      "bias_percent": 0.2542573916153697,
      "rms_normalized_error_percent": 0.3461156044804358,
      "absolute_error": {
        "p95": 0.15462987422943114,
        "p99": 0.18160732269287108,
        "maximum": 0.18950462341308594
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 16.273405075073242,
      "rms_normalized_to_uniform_percent": 0.24068586314238125
    },
    "horizon": {
      "bias_percent": 2.3968951688585842,
      "rms_normalized_error_percent": 4.68683978724689,
      "absolute_error": {
        "p95": 0.17929121460212022,
        "p99": 0.24114708239696778,
        "maximum": 0.25934080106200774
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.1335457892016243,
      "rms_normalized_to_uniform_percent": 0.2964402760504908
    },
    "north": {
      "bias_percent": -85.39949988316232,
      "rms_normalized_error_percent": 104.00720008097049,
      "absolute_error": {
        "p95": 9.745229940563139e-05,
        "p99": 0.00029078088155983997,
        "maximum": 0.00034630746813490987
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 3.346582889207639e-05,
      "rms_normalized_to_uniform_percent": 0.00022326987360276896
    },
    "east": {
      "bias_percent": 0.1802668249933326,
      "rms_normalized_error_percent": 0.5601326548548137,
      "absolute_error": {
        "p95": 0.0645557641983032,
        "p99": 0.12298407554626462,
        "maximum": 0.13980674743652344
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.159787654876709,
      "rms_normalized_to_uniform_percent": 0.12750014717478114
    },
    "south": {
      "bias_percent": 0.3987152210210301,
      "rms_normalized_error_percent": 0.57296816147372,
      "absolute_error": {
        "p95": 0.2922119140624999,
        "p99": 0.3129438781738281,
        "maximum": 0.31778526306152344
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 17.143085479736328,
      "rms_normalized_to_uniform_percent": 0.36857410473436575
    },
    "west": {
      "bias_percent": 0.342278349071421,
      "rms_normalized_error_percent": 0.6421740564068052,
      "absolute_error": {
        "p95": 0.09816027283668516,
        "p99": 0.10523671984672546,
        "maximum": 0.10699605941772461
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.9938740730285645,
      "rms_normalized_to_uniform_percent": 0.14004567616341876
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
        "identifier": "teaching_depth4_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.2032994320459699,
          "cvrmse_percent": 1.9908470570074601,
          "absolute_error_percentiles_lux": {
            "p50": 6.5425872802734375,
            "p90": 62.690551757812585,
            "p95": 93.8907714843746,
            "p99": 182.13643432617187
          },
          "maximum_absolute_error_lux": 660.28515625,
          "worst": {
            "sensor_index": 8,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 14925.9619140625,
            "radiance_lux": 14265.6767578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2417694063926922,
            "maximum_error_percentage_points": 0.9572602739726079,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09263815803479798,
            "maximum_error_percentage_points": 0.3596711885112853,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0897431506849314,
            "maximum_error_percentage_points": 0.4365753424657548,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.15865296803652976,
            "maximum_error_percentage_points": 0.43890410958904624,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.1440011415525114,
            "maximum_error_percentage_points": 0.49616438356164494,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004880672089043969,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.006957791978493333,
      "weather_seconds": 0.10590645798947662,
      "metric_reduction_seconds": 0.035574749927036464,
      "write_seconds": 0.0286371250404045,
      "total_seconds": 0.17034924996551126,
      "cold_end_to_end_seconds": 0.1773070419440046,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.016926625045016408,
      "engine_upload_seconds": 0.000298459,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.017102999961934984,
      "engine_annual_reduction_seconds": 0.00030995835550129414,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.017102999961934984
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006957791978493333,
      "weather_seconds": 0.1111379578942433,
      "metric_reduction_seconds": 0.012523166020400822,
      "write_seconds": 0.02502516598906368,
      "total_seconds": 0.14886612503323704,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14886612503323704,
      "raw_export_seconds": 0.00824108300730586,
      "engine_upload_seconds": 6.2333e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0010607499862089753,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012290665996260941,
      "full": 0.009789417032152414
    }
  },
  "elapsed_seconds": 30.52172179101035,
  "result_class": "passed"
}
```
