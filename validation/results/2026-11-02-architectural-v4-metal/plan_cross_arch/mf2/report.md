# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_arch",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_arch",
    "category": "form",
    "question": "How does a arch opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "arch"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "119e23184f8d9bc6d7dc0b23424da8ae403e6effb3b4ba8e216c7371d17e9edb",
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
      "scene_fingerprint": 3167779511141355274,
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
      "scene_fingerprint": 3167779511141355274,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.0417184612529181,
        "rms_normalized_error_percent": 0.9238426291090699,
        "absolute_error": {
          "p95": 0.0,
          "p99": 5.430774763226509e-07,
          "maximum": 0.00019649998284876347
        },
        "worst_index": [
          21,
          517,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.017216425079988034,
        "rms_normalized_error_percent": 2.3459547622974464,
        "absolute_error": {
          "p95": 5.364598109736107e-06,
          "p99": 4.634144715964794e-05,
          "maximum": 0.0004817713052034378
        },
        "worst_index": [
          20,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": -0.002933343735071348,
        "rms_normalized_error_percent": 1.804792742857653,
        "absolute_error": {
          "p95": 4.536472260951996e-06,
          "p99": 3.840378485620022e-05,
          "maximum": 0.00025174580514431
        },
        "worst_index": [
          21,
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.009055930013536667,
                "cvrmse_percent": 51.66712362072624,
                "rms_normalized_rmse_percent": 5.530581795571864,
                "reference_energy": 2.4627021459600655,
                "candidate_energy": 2.4629251665428455,
                "relative_energy_error_percent": 0.009055930013536667,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.512893691658974e-05,
                  "maximum": 0.00041118054650723934
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.0032307615038007498,
                  "candidate": 0.003641942050307989
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.020367292237465532,
                "cvrmse_percent": 363.5772332253459,
                "rms_normalized_rmse_percent": 6.897216710000724,
                "reference_energy": 0.5828314653618065,
                "candidate_energy": 0.5827127583740044,
                "relative_energy_error_percent": 0.020367292237465532,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.2427549285785062e-06,
                  "p99": 0.00012915796833112836,
                  "maximum": 0.0006096898578107357
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.014793239999562502,
                  "candidate": 0.014183550141751766
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 123.40024998411536,
            "full": 274.19775002636015
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.03508308529854,
            "full": 284.5037919469178
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.03108400292695,
            "full": 284.0963329654187
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 123.90729202888906,
            "full": 262.1086250292137
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.1443822207767977,
                "cvrmse_percent": 42.34773738744816,
                "rms_normalized_rmse_percent": 4.531156784254321,
                "reference_energy": 2.4661385245926795,
                "candidate_energy": 2.4625778590234404,
                "relative_energy_error_percent": 0.14438222077679766,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6998255129437894e-05,
                  "maximum": 0.00040925602661445737
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 160,
                  "rgb_channel": 0,
                  "reference": 0.001371090009342879,
                  "candidate": 0.0017803460359573364
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5316918626129618,
                "cvrmse_percent": 150.1366914517538,
                "rms_normalized_rmse_percent": 4.489806996683668,
                "reference_energy": 1.1169826260124722,
                "candidate_energy": 1.122921531741781,
                "relative_energy_error_percent": 0.5316918626129616,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.847610059892759e-06,
                  "p95": 8.10188930699951e-06,
                  "p99": 9.520142339169979e-05,
                  "maximum": 0.000498151988722384
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 160,
                  "rgb_channel": 0,
                  "reference": 0.0003311819746159017,
                  "candidate": -0.00016697001410648227
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.11820793896914,
            "full": 3212.8429579315707
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.9436669293791,
            "full": 3200.2906249836087
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.7796670300886,
            "full": 3223.7845840863883
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.55183397978544,
            "full": 3211.9133749511093
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04136231819037361,
                "cvrmse_percent": 41.187899504327774,
                "rms_normalized_rmse_percent": 4.409259182546792,
                "reference_energy": 2.4647149179290864,
                "candidate_energy": 2.465734381155926,
                "relative_energy_error_percent": 0.04136231819037361,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.706979962065816e-05,
                  "maximum": 0.000415262533351779
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 306,
                  "rgb_channel": 0,
                  "reference": 0.003493071999400854,
                  "candidate": 0.003077809466049075
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5232509558656069,
                "cvrmse_percent": 134.11502693942384,
                "rms_normalized_rmse_percent": 4.024120601642342,
                "reference_energy": 1.1226398244934899,
                "candidate_energy": 1.1167656008808997,
                "relative_energy_error_percent": 0.5232509558656069,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.7933480712126766e-06,
                  "p95": 7.982758233993081e-06,
                  "p99": 8.995050302473828e-05,
                  "maximum": 0.0005491184419952333
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": -0.0002481324481777847,
                  "candidate": 0.0003009859938174486
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.69504195265472,
            "full": 3487.8689580364153
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.00241696927696,
            "full": 3454.7552909934893
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.3831670852378,
            "full": 3433.2917920546606
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.5040830373764,
            "full": 3434.8701250273734
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05446216514942987,
                "cvrmse_percent": 22.130062136877637,
                "rms_normalized_rmse_percent": 2.3677694816320316,
                "reference_energy": 2.4619967059661576,
                "candidate_energy": 2.4633375626781344,
                "relative_energy_error_percent": 0.05446216514942988,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.375829692231491e-05,
                  "maximum": 0.00020925002172589302
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 450,
                  "rgb_channel": 0,
                  "reference": 0.004700514487922192,
                  "candidate": 0.004909764509648085
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.03749156130388557,
                "cvrmse_percent": 80.84465234646721,
                "rms_normalized_rmse_percent": 2.4325847481272103,
                "reference_energy": 1.1223654565084118,
                "candidate_energy": 1.1219446641752313,
                "relative_energy_error_percent": 0.03749156130388557,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.7311443773214705e-06,
                  "p95": 5.47203489986714e-06,
                  "p99": 5.552524817176163e-05,
                  "maximum": 0.00040619540959596634
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020376939326524734,
                  "candidate": 0.0207831347361207
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 227.0482089370489,
            "full": 5996.839625062421
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 232.20295796636492,
            "full": 6135.799666051753
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.32308305986226,
            "full": 6236.40087491367
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.9946660688147,
            "full": 6089.26124998834
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4128.384207957424,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 16196.731459000148,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013216562780059352,
            "cvrmse_percent": 3.687777062731175,
            "rms_normalized_rmse_percent": 0.3947583360449308,
            "reference_energy": 2.462973442323573,
            "candidate_energy": 2.463298962754834,
            "relative_energy_error_percent": 0.01321656278005935,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.974128048866987e-07,
              "maximum": 5.561765283346176e-05
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.00033255162998102605,
              "candidate": 0.0003881692828144878,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8510532756931463,
            "cvrmse_percent": 137.17128491958212,
            "rms_normalized_rmse_percent": 4.119361186440247,
            "reference_energy": 1.121848759366502,
            "candidate_energy": 1.1123012287515905,
            "relative_energy_error_percent": 0.8510532756931461,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0781472155940719e-05,
              "p95": 2.3122887796489522e-05,
              "p99": 5.996332038193941e-05,
              "maximum": 0.0012862235307693481
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024200696498155594,
              "candidate": 0.025486920028924942,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2572515361934243,
            "cvrmse_percent": 42.95368404731327,
            "rms_normalized_rmse_percent": 4.121927917415069,
            "reference_energy": 3.5848222016900753,
            "candidate_energy": 3.5756001915064246,
            "relative_energy_error_percent": 0.2572515361934243,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0734771478837501e-05,
              "p95": 2.2919591174286325e-05,
              "p99": 6.001438669045456e-05,
              "maximum": 0.0012862235307693481
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024200696498155594,
              "candidate": 0.025486920028924942,
              "position": [
                5.5,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013216562780059352,
            "cvrmse_percent": 3.687777062731175,
            "rms_normalized_rmse_percent": 0.3947583360449308,
            "reference_energy": 2.462973442323573,
            "candidate_energy": 2.463298962754834,
            "relative_energy_error_percent": 0.01321656278005935,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.974128048866987e-07,
              "maximum": 5.561765283346176e-05
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.00033255162998102605,
              "candidate": 0.0003881692828144878,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 90.91618437990456,
            "cvrmse_percent": 1590.4368499544853,
            "rms_normalized_rmse_percent": 30.209913924147695,
            "reference_energy": 0.5826123292607921,
            "candidate_energy": 1.1123012287515905,
            "relative_energy_error_percent": 90.91618437990456,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.680000064487103e-06,
              "p95": 3.158999970764853e-05,
              "p99": 0.00010519707575440407,
              "maximum": 0.008203553035855293
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01728336699306965,
              "candidate": 0.025486920028924942,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.402708696210414,
            "cvrmse_percent": 304.27014627743137,
            "rms_normalized_rmse_percent": 30.212284482637003,
            "reference_energy": 3.0455857715843653,
            "candidate_energy": 3.5756001915064246,
            "relative_energy_error_percent": 17.402708696210414,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.740000339457765e-06,
              "p95": 3.1579998903907835e-05,
              "p99": 0.00010484378435648978,
              "maximum": 0.008203553035855293
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01728336699306965,
              "candidate": 0.025486920028924942,
              "position": [
                5.5,
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
      "bias_percent": -0.24923131491427483,
      "rms_normalized_error_percent": 0.325569807118913,
      "absolute_error": {
        "p95": 0.07034236467402856,
        "p99": 0.10755856032469792,
        "maximum": 0.11345111224426985
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.8241138623114392,
      "rms_normalized_to_uniform_percent": 0.325569807118913
    },
    "overcast": {
      "bias_percent": -0.25801573264686445,
      "rms_normalized_error_percent": 0.21115263311002264,
      "absolute_error": {
        "p95": 0.03972514867782594,
        "p99": 0.04301918268203735,
        "maximum": 0.043186187744140625
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.5337798595428467,
      "rms_normalized_to_uniform_percent": 0.15115998852020773
    },
    "horizon": {
      "bias_percent": -0.2225831710317064,
      "rms_normalized_error_percent": 5.505268378938313,
      "absolute_error": {
        "p95": 0.06364441522950252,
        "p99": 0.08425587380266653,
        "maximum": 0.09595742965897569
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.3511872322759519,
      "rms_normalized_to_uniform_percent": 0.2641882103697329
    },
    "north": {
      "bias_percent": -31.999049299844124,
      "rms_normalized_error_percent": 194.08872283628506,
      "absolute_error": {
        "p95": 5.723424037569204e-05,
        "p99": 0.0001299238074838627,
        "maximum": 0.00017969178233556704
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 6.013750407873886e-06,
      "rms_normalized_to_uniform_percent": 0.00027701967785672755
    },
    "east": {
      "bias_percent": -0.9796923349745587,
      "rms_normalized_error_percent": 0.7162225483652616,
      "absolute_error": {
        "p95": 0.0293623611330986,
        "p99": 0.06568328946828843,
        "maximum": 0.07778668403625488
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.5636802315711975,
      "rms_normalized_to_uniform_percent": 0.1533539389069149
    },
    "south": {
      "bias_percent": -0.16471156429391323,
      "rms_normalized_error_percent": 0.4476061565007428,
      "absolute_error": {
        "p95": 0.06453306823968888,
        "p99": 0.10239047050476074,
        "maximum": 0.10729789733886719
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.7602415084838867,
      "rms_normalized_to_uniform_percent": 0.29592239982083557
    },
    "west": {
      "bias_percent": -0.1340979008102245,
      "rms_normalized_error_percent": 0.5621819500752007,
      "absolute_error": {
        "p95": 0.031542086601257326,
        "p99": 0.039494485557079316,
        "maximum": 0.04101535677909851
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.5724401473999023,
      "rms_normalized_to_uniform_percent": 0.1214421180487349
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
        "identifier": "plan_cross_arch_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.1747165319410017,
          "cvrmse_percent": 7.120156529793895,
          "absolute_error_percentiles_lux": {
            "p50": 1.737381935119629,
            "p90": 26.36240768432618,
            "p95": 47.60596466064452,
            "p99": 114.53779785156242
          },
          "maximum_absolute_error_lux": 495.275390625,
          "worst": {
            "sensor_index": 21,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4449.5,
            "foton_lux": 29491.234375,
            "radiance_lux": 28995.958984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2540379825653804,
            "maximum_error_percentage_points": 1.4238356164383603,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.48367208966984604,
            "maximum_error_percentage_points": 1.5123214689529938,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.9933219178082194,
            "maximum_error_percentage_points": 6.24369863013699,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.0050809464508097,
            "maximum_error_percentage_points": 6.243698630136986,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.018331257783312564,
            "maximum_error_percentage_points": 0.24780821917808282,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.636363636363637,
          "radiance_percent": 13.636363636363637,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004917861729452078,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.009448916069231927,
      "weather_seconds": 0.11685479199513793,
      "metric_reduction_seconds": 0.06817700003739446,
      "write_seconds": 0.029752249945886433,
      "total_seconds": 0.2149289579829201,
      "cold_end_to_end_seconds": 0.22437787405215204,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013461625087074935,
      "engine_upload_seconds": 0.000830084,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01676816667895764,
      "engine_annual_reduction_seconds": 0.001994249993003905,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01676816667895764
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009448916069231927,
      "weather_seconds": 0.12054999999236315,
      "metric_reduction_seconds": 0.044033583952113986,
      "write_seconds": 0.025491208070889115,
      "total_seconds": 0.19021733291447163,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19021733291447163,
      "raw_export_seconds": 0.013655500020831823,
      "engine_upload_seconds": 7.6333e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0018774583004415035,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01974941696971655,
      "full": 0.010374416946433485
    }
  },
  "elapsed_seconds": 77.60455354105216,
  "result_class": "passed"
}
```
