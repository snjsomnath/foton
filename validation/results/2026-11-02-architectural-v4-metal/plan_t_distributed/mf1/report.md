# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 8,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 9.6
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "dd1d4f849dc3aea9d90f21a79d3aad5b55500ff51f60747f6fd09c84734a140b",
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
      "scene_fingerprint": 15359727019794020790,
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
      "scene_fingerprint": 15359727019794020790,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.12369283652481262,
        "rms_normalized_error_percent": 1.4978374183378727,
        "absolute_error": {
          "p95": 4.7414680011570454e-05,
          "p99": 0.0001686424762010605,
          "maximum": 0.0006667673587799072
        },
        "worst_index": [
          52,
          129,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.029874956284702343,
        "rms_normalized_error_percent": 0.9977917645665646,
        "absolute_error": {
          "p95": 7.972260937094688e-05,
          "p99": 0.00017109503736719762,
          "maximum": 0.0006172209978103638
        },
        "worst_index": [
          52,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.006523360515666719,
        "rms_normalized_error_percent": 0.8163858561182057,
        "absolute_error": {
          "p95": 6.150430999696255e-05,
          "p99": 0.00014102396555244984,
          "maximum": 0.0005639269948005676
        },
        "worst_index": [
          5,
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05054472916901429,
                "cvrmse_percent": 9.855032252143955,
                "rms_normalized_rmse_percent": 2.727213895161742,
                "reference_energy": 15.775523645816051,
                "candidate_energy": 15.76754995011428,
                "relative_energy_error_percent": 0.05054472916901429,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.05620477674529e-05,
                  "p95": 0.00014159100828692317,
                  "p99": 0.0003148880240041774,
                  "maximum": 0.0007957248017191887
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 108,
                  "rgb_channel": 0,
                  "reference": 0.014680699910968542,
                  "candidate": 0.01547642471268773
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.11367696985077563,
                "cvrmse_percent": 53.77170354815676,
                "rms_normalized_rmse_percent": 3.3640453217341597,
                "reference_energy": 4.720854949647112,
                "candidate_energy": 4.726221474504921,
                "relative_energy_error_percent": 0.11367696985077562,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00011619766155490652,
                  "p95": 0.00023905758280307055,
                  "p99": 0.0005085901683196486,
                  "maximum": 0.0012555094435811043
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.025478200055658817,
                  "candidate": 0.024222690612077713
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.48824992217124,
            "full": 327.7073339559138
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 140.71329205762595,
            "full": 339.1213750001043
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.857749924995,
            "full": 334.46195803117007
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.93212505616248,
            "full": 334.91095795761794
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": -0.014881201766186467,
                "cvrmse_percent": 6.3470362297266485,
                "rms_normalized_rmse_percent": 1.7567114696094006,
                "reference_energy": 15.777263840709036,
                "candidate_energy": 15.774915994243717,
                "relative_energy_error_percent": 0.014881201766186467,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.579650703817606e-05,
                  "p95": 9.368651080876589e-05,
                  "p99": 0.00020211267517879648,
                  "maximum": 0.0004264123272150755
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 51,
                  "rgb_channel": 0,
                  "reference": 0.005666488548740745,
                  "candidate": 0.00609290087595582
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.02538458404507842,
                "cvrmse_percent": 19.70134243366897,
                "rms_normalized_rmse_percent": 1.8724509780937288,
                "reference_energy": 8.901134741726189,
                "candidate_energy": 8.903394257755668,
                "relative_energy_error_percent": 0.02538458404507842,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0623971320455894e-05,
                  "p90": 7.890816777944565e-05,
                  "p95": 0.00015242502558976412,
                  "p99": 0.0003446933394298021,
                  "maximum": 0.0010266900062561035
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.035109929740428925,
                  "candidate": 0.03613661974668503
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 191.72720797359943,
            "full": 3835.865249973722
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.22733299527317,
            "full": 3791.4229579037055
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 198.8315830240026,
            "full": 3814.977874979377
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.6380419433117,
            "full": 3794.41233293619
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.020774305293674616,
                "cvrmse_percent": 6.622935397210559,
                "rms_normalized_rmse_percent": 1.8322895878785048,
                "reference_energy": 15.76778559507245,
                "candidate_energy": 15.771061242990022,
                "relative_energy_error_percent": 0.020774305293674616,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.615960642695427e-05,
                  "p95": 0.00010428717359900475,
                  "p99": 0.0002166645622492173,
                  "maximum": 0.0004339544102549553
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 123,
                  "rgb_channel": 0,
                  "reference": 0.017942320555448532,
                  "candidate": 0.018376274965703487
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.12341469989805859,
                "cvrmse_percent": 19.951269867502067,
                "rms_normalized_rmse_percent": 1.8996658117447465,
                "reference_energy": 8.921809038291784,
                "candidate_energy": 8.910798214441698,
                "relative_energy_error_percent": 0.12341469989805859,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0429497251607245e-05,
                  "p90": 8.306093513965607e-05,
                  "p95": 0.0001557214418426156,
                  "p99": 0.0003261519363150001,
                  "maximum": 0.0011245012283325195
                },
                "worst": {
                  "global_sensor_index": 50,
                  "local_sensor_index": 50,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.044706739485263824,
                  "candidate": 0.045831240713596344
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.03725001960993,
            "full": 4075.6130409426987
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 192.57887499406934,
            "full": 4024.5826250175014
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.44579106755555,
            "full": 4028.4052500501275
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.5684999395162,
            "full": 4050.824375008233
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.009858178000295585,
                "cvrmse_percent": 3.7232270699169447,
                "rms_normalized_rmse_percent": 1.0301191293836949,
                "reference_energy": 15.770878752984814,
                "candidate_energy": 15.772433474284494,
                "relative_energy_error_percent": 0.009858178000295585,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3873522877693176e-05,
                  "p95": 5.620438605546951e-05,
                  "p99": 0.00012005188036710159,
                  "maximum": 0.00026263645850121975
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 49,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0050277430564165115,
                  "candidate": 0.004765106597915292
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.1286338765675513,
                "cvrmse_percent": 11.897341281390258,
                "rms_normalized_rmse_percent": 1.1315916969533624,
                "reference_energy": 8.909950618862503,
                "candidate_energy": 8.9214118337438,
                "relative_energy_error_percent": 0.12863387656755132,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.399661626550369e-06,
                  "p90": 4.861591150984168e-05,
                  "p95": 8.578511187806726e-05,
                  "p99": 0.0001967310346663047,
                  "maximum": 0.0007746443152427673
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.040823331102728844,
                  "candidate": 0.04159797541797161
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 311.124625033699,
            "full": 7166.508208028972
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 314.45025000721216,
            "full": 7029.960667015985
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 299.4955419562757,
            "full": 7157.108166953549
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 325.5923750111833,
            "full": 7171.871249913238
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1708.7349999928847,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 6514.006667071953,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      54,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21029765851015003,
            "cvrmse_percent": 3.3546279149188942,
            "rms_normalized_rmse_percent": 0.9280042497891544,
            "reference_energy": 15.776926870183388,
            "candidate_energy": 15.743748362390534,
            "relative_energy_error_percent": 0.21029765851015003,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2784759746864438e-05,
              "p95": 3.661305527202785e-05,
              "p99": 0.00010602942202240579,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5062863578695429,
            "cvrmse_percent": 29.768809327314422,
            "rms_normalized_rmse_percent": 2.830783428629624,
            "reference_energy": 8.910410480725545,
            "candidate_energy": 8.865298288031454,
            "relative_energy_error_percent": 0.5062863578695429,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.081796376136481e-05,
              "p90": 9.976932778954506e-05,
              "p95": 0.00014041457325220108,
              "p99": 0.00027047833136748916,
              "maximum": 0.002388646826148033
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030656415969133377,
              "candidate": 0.028267769142985344,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.31712897739481516,
            "cvrmse_percent": 10.598928319776945,
            "rms_normalized_rmse_percent": 2.792438875963145,
            "reference_energy": 24.687337350908933,
            "candidate_energy": 24.609046650421988,
            "relative_energy_error_percent": 0.31712897739481516,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.0223462090361863e-05,
              "p90": 9.775999933481216e-05,
              "p95": 0.00013421638868749142,
              "p99": 0.00025240483460947926,
              "maximum": 0.002388646826148033
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030656415969133377,
              "candidate": 0.028267769142985344,
              "position": [
                6.5,
                8.5,
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
      54,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21029765851015003,
            "cvrmse_percent": 3.3546279149188942,
            "rms_normalized_rmse_percent": 0.9280042497891544,
            "reference_energy": 15.776926870183388,
            "candidate_energy": 15.743748362390534,
            "relative_energy_error_percent": 0.21029765851015003,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2784759746864438e-05,
              "p95": 3.661305527202785e-05,
              "p99": 0.00010602942202240579,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.89783686259901,
            "cvrmse_percent": 512.3226995506886,
            "rms_normalized_rmse_percent": 32.03785432322261,
            "reference_energy": 4.718148136273776,
            "candidate_energy": 8.865298288031454,
            "relative_energy_error_percent": 87.897836862599,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.904447193141095e-05,
              "p90": 0.00021674999152310193,
              "p95": 0.0002765399985946715,
              "p99": 0.0004739608289674007,
              "maximum": 0.01685027778148651
            },
            "worst": {
              "global_sensor_index": 51,
              "local_sensor_index": 51,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01929222047328949,
              "candidate": 0.036142498254776,
              "position": [
                11.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.07297676475289,
            "cvrmse_percent": 117.90338746258993,
            "rms_normalized_rmse_percent": 32.02757421876827,
            "reference_energy": 20.495075006457164,
            "candidate_energy": 24.609046650421988,
            "relative_energy_error_percent": 20.07297676475289,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.812999683665112e-05,
              "p90": 0.00021412999194581062,
              "p95": 0.00026905125014309306,
              "p99": 0.0004624726664042149,
              "maximum": 0.01685027778148651
            },
            "worst": {
              "global_sensor_index": 51,
              "local_sensor_index": 51,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01929222047328949,
              "candidate": 0.036142498254776,
              "position": [
                11.5,
                11.5,
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
      "bias_percent": -0.09238117480989905,
      "rms_normalized_error_percent": 0.4569851644077582,
      "absolute_error": {
        "p95": 0.2257793837017282,
        "p99": 0.2817998541671343,
        "maximum": 0.3016108927557166
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 20.63383977277381,
      "rms_normalized_to_uniform_percent": 0.4569851644077582
    },
    "overcast": {
      "bias_percent": -0.04568354017208394,
      "rms_normalized_error_percent": 0.4081205738654733,
      "absolute_error": {
        "p95": 0.14085862636566157,
        "p99": 0.17215453147888177,
        "maximum": 0.20087051391601562
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 13.233964920043945,
      "rms_normalized_to_uniform_percent": 0.2776089616141054
    },
    "horizon": {
      "bias_percent": -0.8304042514538452,
      "rms_normalized_error_percent": 2.795372343511211,
      "absolute_error": {
        "p95": 0.12383416852849038,
        "p99": 0.16072717440683204,
        "maximum": 0.17993595505378623
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.272013664674685,
      "rms_normalized_to_uniform_percent": 0.2518306790921042
    },
    "north": {
      "bias_percent": -0.009818294805523506,
      "rms_normalized_error_percent": 0.7460857681446437,
      "absolute_error": {
        "p95": 0.08883955478668212,
        "p99": 0.1422091329097747,
        "maximum": 0.18266773223876953
      },
      "worst_index": [
        50
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.9046599864959717,
      "rms_normalized_to_uniform_percent": 0.1864816850246648
    },
    "east": {
      "bias_percent": -0.2955973615756562,
      "rms_normalized_error_percent": 0.660125439478314,
      "absolute_error": {
        "p95": 0.10779665112495417,
        "p99": 0.12387211561203003,
        "maximum": 0.12485432624816895
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.583709716796875,
      "rms_normalized_to_uniform_percent": 0.22554781435423513
    },
    "south": {
      "bias_percent": -0.10809296024538766,
      "rms_normalized_error_percent": 0.5733553418776428,
      "absolute_error": {
        "p95": 0.11074901819229126,
        "p99": 0.17921034812927233,
        "maximum": 0.2317066192626953
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.295307159423828,
      "rms_normalized_to_uniform_percent": 0.2359249592308621
    },
    "west": {
      "bias_percent": -0.06063321195875093,
      "rms_normalized_error_percent": 0.484876736634326,
      "absolute_error": {
        "p95": 0.08245408535003655,
        "p99": 0.10262869834899901,
        "maximum": 0.10405254364013672
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.483987331390381,
      "rms_normalized_to_uniform_percent": 0.16400410098631704
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
        "identifier": "plan_t_distributed_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.11974402947545533,
          "cvrmse_percent": 2.4784881489903094,
          "absolute_error_percentiles_lux": {
            "p50": 9.74420166015625,
            "p90": 53.320928955078124,
            "p95": 74.23587646484371,
            "p99": 126.35379943847656
          },
          "maximum_absolute_error_lux": 445.732421875,
          "worst": {
            "sensor_index": 48,
            "position": [
              10.5,
              11.5,
              0.75
            ],
            "hour_of_year": 1809.5,
            "foton_lux": 9361.318359375,
            "radiance_lux": 9807.05078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3049315068493155,
            "maximum_error_percentage_points": 2.7079452054794473,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.132213660304181,
            "maximum_error_percentage_points": 1.2066646474136888,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09171232876712307,
            "maximum_error_percentage_points": 0.7356164383561641,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10979198376458517,
            "maximum_error_percentage_points": 0.7434246575342485,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.051232876712328845,
            "maximum_error_percentage_points": 0.24273972602739846,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 98.14814814814815,
          "radiance_percent": 100.0,
          "difference_percentage_points": 1.8518518518518476,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.0049745826198659415,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.0049745826198659415,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_distributed_grid",
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
      "study_preparation_seconds": 0.008074249955825508,
      "weather_seconds": 0.10860820801462978,
      "metric_reduction_seconds": 0.036653999937698245,
      "write_seconds": 0.036652915994636714,
      "total_seconds": 0.1820716669317335,
      "cold_end_to_end_seconds": 0.190145916887559,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.020811666967347264,
      "engine_upload_seconds": 0.000276541,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01825062499847263,
      "engine_annual_reduction_seconds": 0.00047774997074157,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01825062499847263
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008074249955825508,
      "weather_seconds": 0.10651466599665582,
      "metric_reduction_seconds": 0.012662415974773467,
      "write_seconds": 0.03524466697126627,
      "total_seconds": 0.15458420803770423,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15458420803770423,
      "raw_export_seconds": 0.019087916938588023,
      "engine_upload_seconds": 6.1375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00047820829786360264,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01781608397141099,
      "full": 0.022468707989901304
    }
  },
  "elapsed_seconds": 74.90075737505686,
  "result_class": "passed"
}
```
