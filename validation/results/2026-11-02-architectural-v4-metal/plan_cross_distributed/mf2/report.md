# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 12,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 14.399999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "7116d2a92a355e29c5a2e22bb268462b975fdfd2fb36c86e6148dc31f2a3dd09",
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
      "scene_fingerprint": 5695616808233762139,
      "basis": "ReinhartMf2",
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
      "scene_fingerprint": 5695616808233762139,
      "basis": "ReinhartMf2",
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_cross_distributed_grid",
        "bias_percent": 0.0012976006492534068,
        "rms_normalized_error_percent": 0.9841365903222667,
        "absolute_error": {
          "p95": 6.11846917308867e-06,
          "p99": 3.543379716575146e-05,
          "maximum": 0.0002025947906076908
        },
        "worst_index": [
          32,
          281,
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
        "identifier": "plan_cross_distributed_grid",
        "bias_percent": 0.10526321695834626,
        "rms_normalized_error_percent": 1.3948935386129764,
        "absolute_error": {
          "p95": 6.814463995397091e-05,
          "p99": 0.0001374336425215006,
          "maximum": 0.0007494240999221802
        },
        "worst_index": [
          37,
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
        "identifier": "plan_cross_distributed_grid",
        "bias_percent": -0.04376469557383763,
        "rms_normalized_error_percent": 1.119087692418808,
        "absolute_error": {
          "p95": 5.5740587413311005e-05,
          "p99": 0.00011077499948441982,
          "maximum": 0.0005626529455184937
        },
        "worst_index": [
          37,
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0585566494036985,
                "cvrmse_percent": 29.69943002822979,
                "rms_normalized_rmse_percent": 9.09797810524704,
                "reference_energy": 17.78866298367781,
                "candidate_energy": 17.778246538660852,
                "relative_energy_error_percent": 0.05855664940369851,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.90990486368537e-05,
                  "p95": 0.0001702640438452363,
                  "p99": 0.0003262339741922915,
                  "maximum": 0.0007762740133330226
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.003145695081911981,
                  "candidate": 0.0023694210685789585
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1446839471249566,
                "cvrmse_percent": 153.0048857274267,
                "rms_normalized_rmse_percent": 6.416272907590756,
                "reference_energy": 5.348271781207451,
                "candidate_energy": 5.34053369049143,
                "relative_energy_error_percent": 0.14468394712495658,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00012267444981262088,
                  "p95": 0.0002373201714362949,
                  "p99": 0.0004908803966827691,
                  "maximum": 0.0023188479244709015
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03768150135874748,
                  "candidate": 0.040000349283218384
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.99341709539294,
            "full": 312.2205419931561
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.45029191300273,
            "full": 309.05499996151775
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.4860830102116,
            "full": 304.2786669684574
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.48962497711182,
            "full": 322.178625036031
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.027034060426352844,
                "cvrmse_percent": 16.53442493261185,
                "rms_normalized_rmse_percent": 5.073602588940389,
                "reference_energy": 17.78781161229016,
                "candidate_energy": 17.783002844550367,
                "relative_energy_error_percent": 0.027034060426352844,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.546899253909942e-05,
                  "p95": 9.11167444428429e-05,
                  "p99": 0.00018429302144795656,
                  "maximum": 0.00040088791865855455
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 285,
                  "rgb_channel": 0,
                  "reference": 0.003433398436754942,
                  "candidate": 0.0030325105180963874
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.12053884729276394,
                "cvrmse_percent": 45.70459176705363,
                "rms_normalized_rmse_percent": 2.5792838110153666,
                "reference_energy": 10.02935618441197,
                "candidate_energy": 10.041445454747546,
                "relative_energy_error_percent": 0.12053884729276393,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.6117731876147445e-06,
                  "p90": 6.890582153573632e-05,
                  "p95": 0.00013279705308377743,
                  "p99": 0.00027511345979291946,
                  "maximum": 0.000966409221291542
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05072204954922199,
                  "candidate": 0.04975564032793045
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.28645804710686,
            "full": 3269.847791059874
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 190.4904160182923,
            "full": 3249.5672500226647
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.23533300869167,
            "full": 3266.3724169833586
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 191.7259170440957,
            "full": 3306.224957923405
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.019538230082767175,
                "cvrmse_percent": 17.02599980883389,
                "rms_normalized_rmse_percent": 5.224614453991994,
                "reference_energy": 17.791219780441665,
                "candidate_energy": 17.78774369098643,
                "relative_energy_error_percent": 0.019538230082767175,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.58565991721116e-05,
                  "p95": 9.242980740964413e-05,
                  "p99": 0.0001866659731604159,
                  "maximum": 0.0004910208808723837
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 119,
                  "rgb_channel": 0,
                  "reference": 0.0008893045887816697,
                  "candidate": 0.0013803254696540534
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.13102484070968293,
                "cvrmse_percent": 44.22853684477793,
                "rms_normalized_rmse_percent": 2.4954916722329563,
                "reference_energy": 10.054024721782614,
                "candidate_energy": 10.067197991659242,
                "relative_energy_error_percent": 0.13102484070968293,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.617334292968735e-06,
                  "p90": 6.830645725131035e-05,
                  "p95": 0.00013284635497257113,
                  "p99": 0.00026695808628574014,
                  "maximum": 0.0008193813264369965
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05907035991549492,
                  "candidate": 0.059889741241931915
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.00274996366352,
            "full": 3434.820458991453
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 185.09916693437845,
            "full": 3435.00687496271
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.75887501053512,
            "full": 3459.282625000924
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.0307499608025,
            "full": 3402.2706659743562
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.025709765973194344,
                "cvrmse_percent": 9.170565001721396,
                "rms_normalized_rmse_percent": 2.815626773556921,
                "reference_energy": 17.78962397423162,
                "candidate_energy": 17.794197644922907,
                "relative_energy_error_percent": 0.025709765973194344,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.338325430173427e-05,
                  "p95": 5.1102309953421354e-05,
                  "p99": 0.00010133394971489906,
                  "maximum": 0.0002443739795126021
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.0018613574793562293,
                  "candidate": 0.0016169834998436272
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.09346039033869355,
                "cvrmse_percent": 25.725949005994362,
                "rms_normalized_rmse_percent": 1.4514743537680699,
                "reference_energy": 10.050690493605146,
                "candidate_energy": 10.041297079038088,
                "relative_energy_error_percent": 0.09346039033869355,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.642455678549595e-06,
                  "p90": 3.902153002854902e-05,
                  "p95": 7.359206210821867e-05,
                  "p99": 0.00015140254981815815,
                  "maximum": 0.0008580498397350311
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.059220729395747185,
                  "candidate": 0.058362679556012154
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 305.98883400671184,
            "full": 6023.758291034028
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 301.37670796830207,
            "full": 5929.907374898903
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 302.26954200770706,
            "full": 6401.421082904562
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 307.7284999890253,
            "full": 5985.243791015819
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4025.528375059366,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 15980.5425000377,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      44,
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
        "identifier": "plan_cross_distributed_grid",
        "full_identifier": "plan_cross_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3229728596790898,
            "cvrmse_percent": 3.1865114786219926,
            "rms_normalized_rmse_percent": 0.9779472448884364,
            "reference_energy": 17.790316563629965,
            "candidate_energy": 17.732858669478446,
            "relative_energy_error_percent": 0.3229728596790898,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8674509192351252e-06,
              "p95": 9.092491382034495e-06,
              "p99": 3.5039527574554086e-05,
              "maximum": 9.509868687018752e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 97,
              "rgb_channel": 0,
              "reference": 0.0010448165703564882,
              "candidate": 0.0009497178834863007,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.35882839026311253,
            "cvrmse_percent": 46.087012676629044,
            "rms_normalized_rmse_percent": 2.6006271847348046,
            "reference_energy": 10.047588061686051,
            "candidate_energy": 10.011534463184034,
            "relative_energy_error_percent": 0.35882839026311253,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.8623364667291753e-05,
              "p90": 5.804231477668509e-05,
              "p95": 7.73424981161952e-05,
              "p99": 0.00012775608047377318,
              "maximum": 0.0025968439877033234
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05879170447587967,
              "candidate": 0.056194860488176346,
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
            "nmbe_percent": -0.3359142647844806,
            "cvrmse_percent": 16.572346183582265,
            "rms_normalized_rmse_percent": 2.590945380191335,
            "reference_energy": 27.837904625316014,
            "candidate_energy": 27.74439313266248,
            "relative_energy_error_percent": 0.33591426478447417,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.859103645074356e-05,
              "p90": 5.7581288274377584e-05,
              "p95": 7.640512012585532e-05,
              "p99": 0.00012613702710950747,
              "maximum": 0.0025968439877033234
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05879170447587967,
              "candidate": 0.056194860488176346,
              "position": [
                1.5,
                5.5,
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
      44,
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
        "identifier": "plan_cross_distributed_grid",
        "full_identifier": "plan_cross_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3229728596790898,
            "cvrmse_percent": 3.1865114786219926,
            "rms_normalized_rmse_percent": 0.9779472448884364,
            "reference_energy": 17.790316563629965,
            "candidate_energy": 17.732858669478446,
            "relative_energy_error_percent": 0.3229728596790898,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8674509192351252e-06,
              "p95": 9.092491382034495e-06,
              "p99": 3.5039527574554086e-05,
              "maximum": 9.509868687018752e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 97,
              "rgb_channel": 0,
              "reference": 0.0010448165703564882,
              "candidate": 0.0009497178834863007,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.5682936850548,
            "cvrmse_percent": 1009.3635126566458,
            "rms_normalized_rmse_percent": 42.236398309933676,
            "reference_energy": 5.33754093855242,
            "candidate_energy": 10.011534463184034,
            "relative_energy_error_percent": 87.5682936850548,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.9716182780248346e-05,
              "p90": 9.860654972726479e-05,
              "p95": 0.000134230125695467,
              "p99": 0.0002287162933498621,
              "maximum": 0.02056693285703659
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04143727570772171,
              "candidate": 0.0620042085647583,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.960930795446448,
            "cvrmse_percent": 232.92621149241862,
            "rms_normalized_rmse_percent": 42.23298928399265,
            "reference_energy": 23.127857502182387,
            "candidate_energy": 27.74439313266248,
            "relative_energy_error_percent": 19.960930795446437,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.9650000215042382e-05,
              "p90": 9.761773981153965e-05,
              "p95": 0.00013219847460277379,
              "p99": 0.00022628798615187407,
              "maximum": 0.02056693285703659
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04143727570772171,
              "candidate": 0.0620042085647583,
              "position": [
                6.5,
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
      "bias_percent": -0.23535134001398897,
      "rms_normalized_error_percent": 0.44701029663957764,
      "absolute_error": {
        "p95": 0.27142436245875595,
        "p99": 0.2835527494485566,
        "maximum": 0.28544678106374555
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 28.30768963786036,
      "rms_normalized_to_uniform_percent": 0.44701029663957764
    },
    "overcast": {
      "bias_percent": -0.1862854620885134,
      "rms_normalized_error_percent": 0.39132081860499374,
      "absolute_error": {
        "p95": 0.1434253692626953,
        "p99": 0.1630866003036499,
        "maximum": 0.17467689514160156
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 18.053781509399414,
      "rms_normalized_to_uniform_percent": 0.2571009239568845
    },
    "horizon": {
      "bias_percent": -1.1558978680911405,
      "rms_normalized_error_percent": 3.3065903349243504,
      "absolute_error": {
        "p95": 0.15695753031863854,
        "p99": 0.19878926704651229,
        "maximum": 0.20821777167637112
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.823893082290476,
      "rms_normalized_to_uniform_percent": 0.29590965205580533
    },
    "north": {
      "bias_percent": -0.1475093374767192,
      "rms_normalized_error_percent": 0.6491649283063715,
      "absolute_error": {
        "p95": 0.12373681068420411,
        "p99": 0.18139163017272952,
        "maximum": 0.20844173431396484
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.628997802734375,
      "rms_normalized_to_uniform_percent": 0.20748339490333761
    },
    "east": {
      "bias_percent": -0.2748962520724763,
      "rms_normalized_error_percent": 0.6580448441125063,
      "absolute_error": {
        "p95": 0.12902913093566895,
        "p99": 0.16246933460235596,
        "maximum": 0.17339324951171875
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.65043830871582,
      "rms_normalized_to_uniform_percent": 0.21098347236684906
    },
    "south": {
      "bias_percent": -0.478217766530405,
      "rms_normalized_error_percent": 0.6634713033243406,
      "absolute_error": {
        "p95": 0.13274186849594116,
        "p99": 0.14999835968017577,
        "maximum": 0.16165447235107422
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.62721586227417,
      "rms_normalized_to_uniform_percent": 0.2118483174954843
    },
    "west": {
      "bias_percent": -0.16074984274189869,
      "rms_normalized_error_percent": 0.4803284145176715,
      "absolute_error": {
        "p95": 0.09215925931930544,
        "p99": 0.12253024101257325,
        "maximum": 0.12540531158447266
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.68495512008667,
      "rms_normalized_to_uniform_percent": 0.15456607984246634
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
        "identifier": "plan_cross_distributed_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.30349984553501325,
          "cvrmse_percent": 3.588817045974937,
          "absolute_error_percentiles_lux": {
            "p50": 16.12890625,
            "p90": 96.45929565429688,
            "p95": 133.99265136718742,
            "p99": 225.34778076171872
          },
          "maximum_absolute_error_lux": 719.357666015625,
          "worst": {
            "sensor_index": 32,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 4453.5,
            "foton_lux": 2459.368408203125,
            "radiance_lux": 1740.0107421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20343711083437135,
            "maximum_error_percentage_points": 1.1215068493150682,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07860639528672277,
            "maximum_error_percentage_points": 0.5977620440748552,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06922166874221664,
            "maximum_error_percentage_points": 0.5721917808219175,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11313823163138133,
            "maximum_error_percentage_points": 0.5230136986301375,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05937733499377358,
            "maximum_error_percentage_points": 0.24876712328767425,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.272727272727273,
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
      "maximum_error_percentage_points": 0.0049721746575386305,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.0049721746575386305,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
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
      "study_preparation_seconds": 0.008849416975863278,
      "weather_seconds": 0.11273495806381106,
      "metric_reduction_seconds": 0.07431900000665337,
      "write_seconds": 0.03147362498566508,
      "total_seconds": 0.21865662501659244,
      "cold_end_to_end_seconds": 0.22750604199245572,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010936665930785239,
      "engine_upload_seconds": 0.000760292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024345749872736633,
      "engine_annual_reduction_seconds": 0.002001499990001321,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024345749872736633
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008849416975863278,
      "weather_seconds": 0.1101890419377014,
      "metric_reduction_seconds": 0.04376937507186085,
      "write_seconds": 0.030940292053855956,
      "total_seconds": 0.18507829203736037,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18507829203736037,
      "raw_export_seconds": 0.01562429207842797,
      "engine_upload_seconds": 6.7833e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0019145833794027567,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014922500005923212,
      "full": 0.01930266700219363
    }
  },
  "elapsed_seconds": 78.19649066706188,
  "result_class": "passed"
}
```
