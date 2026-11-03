# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_circle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_circle",
    "category": "form",
    "question": "How does a circle opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "circle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 1.4400000000000004
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "7c22d1ffab9a83507a90e1a8acd8e804d68df9419541ccde638797de1adf55d2",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 17537023707857486427,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 17537023707857486427,
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
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "9fabdcb377c0b959f3da2f14ceba2b4c1e0eabafa15fc4f50de41689689d98e4",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "738a59ae8fb6881ea29066a9316dfc51647b6e94d0eae23cc7b76edc5ea48e16",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0005488619208335876,
          "p95": 0.0,
          "p99": 5.369284190237522e-05
        },
        "bias_percent": -0.17408138247002838,
        "identifier": "plan_l_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4526703356126804,
        "worst_index": [
          39,
          120,
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
          "maximum": 0.0002979375422000885,
          "p95": 1.387211523251608e-05,
          "p99": 7.86585733294487e-05
        },
        "bias_percent": 0.1267138513096481,
        "identifier": "plan_l_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1894114038959205,
        "worst_index": [
          36,
          72,
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
          "maximum": 0.0002560671418905258,
          "p95": 1.167398295365274e-05,
          "p99": 6.742682307958603e-05
        },
        "bias_percent": 0.006963253007901328,
        "identifier": "plan_l_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0298561041097722,
        "worst_index": [
          38,
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_l_circle_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006560760084539652,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014067284791963175
                },
                "candidate_energy": 2.6100909259384935,
                "cvrmse_percent": 24.348501968651092,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.10783906619733918,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.612908662240443,
                "relative_energy_error_percent": 0.10783906619733917,
                "rms_normalized_rmse_percent": 2.726490383227215,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003459700499661267,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0028036244912073016,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007894798181951046,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.174296539829811e-05,
                  "p99": 0.00021413969807326794
                },
                "candidate_energy": 0.6298661773133745,
                "cvrmse_percent": 151.44875182292085,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0418350185658786,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6296027828722686,
                "relative_energy_error_percent": 0.04183501856587861,
                "rms_normalized_rmse_percent": 3.7479761455882237,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003503449261188507,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": -0.0004391348920762539,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.00470806844532,
            "full": 270.51179099362344
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.65870794281363,
            "full": 278.2698329538107
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.35279202833772,
            "full": 299.2363329976797
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.6642498942092,
            "full": 278.82379200309515
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_l_circle_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00030013459036126733,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.970360300329048e-05
                },
                "candidate_energy": 2.6155097376549747,
                "cvrmse_percent": 12.881799081544132,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10147373457834459,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6128583726849683,
                "relative_energy_error_percent": 0.10147373457834456,
                "rms_normalized_rmse_percent": 1.443675929782255,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020284935599192977,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0017283589695580304,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005105757154524326,
                  "p50": 4.929253449859061e-08,
                  "p90": 9.23663105822927e-06,
                  "p95": 2.0197690901113674e-05,
                  "p99": 0.0001488367561250925
                },
                "candidate_energy": 1.2572739728125875,
                "cvrmse_percent": 46.902036794758814,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6375200729059675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.265340774239025,
                "relative_energy_error_percent": 0.6375200729059673,
                "rms_normalized_rmse_percent": 2.146837632153265,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0001621812116354704,
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "reference": 0.00034839450381696224,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.77341700252146,
            "full": 3208.0728749278933
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.34820794407278,
            "full": 3172.870208043605
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.0208330983296,
            "full": 3170.9740839432925
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.35125000681728,
            "full": 3262.0370420627296
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_l_circle_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004154094494879246,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.115505963563919e-05
                },
                "candidate_energy": 2.616514138822822,
                "cvrmse_percent": 14.631811697161618,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.14283300421729273,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.612782223479371,
                "relative_energy_error_percent": 0.1428330042172927,
                "rms_normalized_rmse_percent": 1.6398776966198252,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014966525137424469,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.015381934586912394,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00048255501314997673,
                  "p50": 5.000000058430487e-08,
                  "p90": 9.910597964335469e-06,
                  "p95": 2.164899979106849e-05,
                  "p99": 0.0001506615626567509
                },
                "candidate_energy": 1.2666295953451403,
                "cvrmse_percent": 47.4469188657481,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1384443461926458,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2648784426550748,
                "relative_energy_error_percent": 0.13844434619264578,
                "rms_normalized_rmse_percent": 2.170320765290343,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002899952232837677,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": -0.00019255978986620903,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.31129204202443,
            "full": 3431.4473749836907
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.87595897726715,
            "full": 3389.1312499763444
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.98308401927352,
            "full": 3471.8223341042176
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.69841601792723,
            "full": 3406.337458989583
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_l_circle_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019696960225701332,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.642516068997793e-05
                },
                "candidate_energy": 2.6136924982824894,
                "cvrmse_percent": 7.91982693466739,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.022331797774561835,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6142763131820175,
                "relative_energy_error_percent": 0.022331797774561835,
                "rms_normalized_rmse_percent": 0.887755406200895,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007485986454412341,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.0076829560566693544,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003885142505168915,
                  "p50": 4.3148801864845154e-08,
                  "p90": 6.719191151205457e-06,
                  "p95": 1.4383251254912466e-05,
                  "p99": 8.133519440889359e-05
                },
                "candidate_energy": 1.2662815101819405,
                "cvrmse_percent": 29.465901831802764,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06416123074841247,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.267094493603782,
                "relative_energy_error_percent": 0.06416123074841247,
                "rms_normalized_rmse_percent": 1.348435105453622,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02026697527617216,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.020655489526689053,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 248.58983303420246,
            "full": 6096.139375003986
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 243.39891597628593,
            "full": 6089.059749967419
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 252.4219169281423,
            "full": 6029.180999961682
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 245.6971249775961,
            "full": 6035.956958075985
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_l_circle/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1312.9925420507789,
      "invocation_count": 3,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_circle/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4854.162291041575,
      "invocation_count": 3,
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
      48,
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
        "identifier": "plan_l_circle_grid",
        "full_identifier": "plan_l_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.11287881098902244,
            "cvrmse_percent": 6.451237147396647,
            "rms_normalized_rmse_percent": 0.7222325752387204,
            "reference_energy": 2.609557222543117,
            "candidate_energy": 2.612502859708002,
            "relative_energy_error_percent": 0.11287881098902246,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.7784728445112705e-05,
              "maximum": 0.0001889411360025406
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 0.004131827969104052,
              "candidate": 0.004320769105106592,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.5191010200536992,
            "cvrmse_percent": 33.11436576436336,
            "rms_normalized_rmse_percent": 1.5215202108079642,
            "reference_energy": 1.271115193925441,
            "candidate_energy": 1.251805670048462,
            "relative_energy_error_percent": 1.519101020053699,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.167847826394791e-08,
              "p90": 1.5136513684410621e-05,
              "p95": 2.7150381356477737e-05,
              "p99": 7.962039671838284e-05,
              "maximum": 0.0003921687602996826
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01618228852748871,
              "candidate": 0.015790119767189026,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.421676579621873,
            "cvrmse_percent": 10.57854223835813,
            "rms_normalized_rmse_percent": 1.4839155379662223,
            "reference_energy": 3.880672416468558,
            "candidate_energy": 3.864308529756464,
            "relative_energy_error_percent": 0.42167657962187294,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.167847826394791e-08,
              "p90": 1.5074924158398074e-05,
              "p95": 2.6180226996075362e-05,
              "p99": 7.063290104269981e-05,
              "maximum": 0.0003921687602996826
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01618228852748871,
              "candidate": 0.015790119767189026,
              "position": [
                4.5,
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
      48,
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
        "identifier": "plan_l_circle_grid",
        "full_identifier": "plan_l_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.11287881098902244,
            "cvrmse_percent": 6.451237147396647,
            "rms_normalized_rmse_percent": 0.7222325752387204,
            "reference_energy": 2.609557222543117,
            "candidate_energy": 2.612502859708002,
            "relative_energy_error_percent": 0.11287881098902246,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.7784728445112705e-05,
              "maximum": 0.0001889411360025406
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 0.004131827969104052,
              "candidate": 0.004320769105106592,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 98.1717864800671,
            "cvrmse_percent": 715.0399411466003,
            "rms_normalized_rmse_percent": 17.775696800343344,
            "reference_energy": 0.6316770375254066,
            "candidate_energy": 1.251805670048462,
            "relative_energy_error_percent": 98.1717864800671,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.509399900096478e-05,
              "p95": 0.00011082999844802544,
              "p99": 0.00023110839538276196,
              "maximum": 0.0050157178193330765
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 41,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010595211759209633,
              "candidate": 0.01561092957854271,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.22336430180668,
            "cvrmse_percent": 139.38670709274797,
            "rms_normalized_rmse_percent": 17.780051786434456,
            "reference_energy": 3.2412342600685236,
            "candidate_energy": 3.864308529756464,
            "relative_energy_error_percent": 19.223364301806676,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.4981992477442e-05,
              "p95": 0.00011002999963238835,
              "p99": 0.00023177266120910645,
              "maximum": 0.0050157178193330765
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 41,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010595211759209633,
              "candidate": 0.01561092957854271,
              "position": [
                5.5,
                0.5,
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
      "bias_percent": -0.010240281890789765,
      "rms_normalized_error_percent": 0.22938433076731696,
      "absolute_error": {
        "p95": 0.045142516459889856,
        "p99": 0.07532069387631388,
        "maximum": 0.10066284788133473
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.752038535610536,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22938433076731696
    },
    "overcast": {
      "bias_percent": -0.027098748998353694,
      "rms_normalized_error_percent": 0.18697311228096133,
      "absolute_error": {
        "p95": 0.03504055738449096,
        "p99": 0.04292965888977052,
        "maximum": 0.047150611877441406
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.503769874572754,
      "reference_fraction_of_uniform": 0.6673092246055603,
      "rms_normalized_to_uniform_percent": 0.13624189546550503
    },
    "horizon": {
      "bias_percent": 0.47641272035277316,
      "rms_normalized_error_percent": 3.801006652433076,
      "absolute_error": {
        "p95": 0.025884591501018146,
        "p99": 0.03739288080869944,
        "maximum": 0.04401885670287986
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.24361485345867273,
      "reference_fraction_of_uniform": 0.0649286650834015,
      "rms_normalized_to_uniform_percent": 0.11891141961320004
    },
    "north": {
      "bias_percent": -93.043746594606,
      "rms_normalized_error_percent": 100.2693358392403,
      "absolute_error": {
        "p95": 7.215711711978646e-05,
        "p99": 0.0003064383834862387,
        "maximum": 0.0004778359434567392
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.8174900105805136e-05,
      "reference_fraction_of_uniform": 4.84400698042009e-06,
      "rms_normalized_to_uniform_percent": 0.0006674859851016142
    },
    "east": {
      "bias_percent": -0.21051987372499517,
      "rms_normalized_error_percent": 0.5533473383348573,
      "absolute_error": {
        "p95": 0.02706632912158966,
        "p99": 0.032660248577594767,
        "maximum": 0.03620338439941406
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.910631000995636,
      "reference_fraction_of_uniform": 0.24270300567150116,
      "rms_normalized_to_uniform_percent": 0.11844759188092281
    },
    "south": {
      "bias_percent": 0.0314921819155677,
      "rms_normalized_error_percent": 0.27146283872718147,
      "absolute_error": {
        "p95": 0.036391645669937134,
        "p99": 0.06389307975769049,
        "maximum": 0.08396244049072266
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.407750368118286,
      "reference_fraction_of_uniform": 0.6417179107666016,
      "rms_normalized_to_uniform_percent": 0.17763450873663533
    },
    "west": {
      "bias_percent": 0.01866181979615048,
      "rms_normalized_error_percent": 0.338140104986703,
      "absolute_error": {
        "p95": 0.02129824757575988,
        "p99": 0.024489004611968995,
        "maximum": 0.024518251419067383
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7222974896430969,
      "reference_fraction_of_uniform": 0.1925080120563507,
      "rms_normalized_to_uniform_percent": 0.06806636361264363
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
        "identifier": "plan_l_circle_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": -0.06348901452950881,
          "cvrmse_percent": 2.7383310121578894,
          "absolute_error_percentiles_lux": {
            "p50": 0.8011054992675781,
            "p90": 10.172221374511725,
            "p95": 17.550764846801727,
            "p99": 38.81212280273415
          },
          "maximum_absolute_error_lux": 309.9228515625,
          "worst": {
            "sensor_index": 36,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6081.5,
            "foton_lux": 9001.3837890625,
            "radiance_lux": 9311.306640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2216210045662099,
            "maximum_error_percentage_points": 1.9473972602739718,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3499683610520821,
            "maximum_error_percentage_points": 1.5728042342755124,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.30865011415525184,
            "maximum_error_percentage_points": 1.6682191780821967,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3135216894977168,
            "maximum_error_percentage_points": 1.6682191780821896,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00658675799086749,
            "maximum_error_percentage_points": 0.07958904109588616,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 12.5,
          "radiance_percent": 12.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
      "maximum_error_percentage_points": 0.004942309235874021,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_circle_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_circle_grid",
            "maximum_error_percentage_points": 0.004942309235874021,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_circle_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_circle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_circle_grid",
            "maximum_error_percentage_points": 0.003972602739725994,
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
      "study_preparation_seconds": 0.007212832919321954,
      "weather_seconds": 0.0973185000475496,
      "metric_reduction_seconds": 0.041496749967336655,
      "write_seconds": 0.051270624971948564,
      "total_seconds": 0.19025683298241347,
      "cold_end_to_end_seconds": 0.19746966590173542,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03023862501140684,
      "engine_upload_seconds": 0.000292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.020734083373099566,
      "engine_annual_reduction_seconds": 0.00043183332309126854,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.020734083373099566
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007212832919321954,
      "weather_seconds": 0.09507649997249246,
      "metric_reduction_seconds": 0.012506040977314115,
      "write_seconds": 0.04820033290889114,
      "total_seconds": 0.1559383749263361,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1559383749263361,
      "raw_export_seconds": 0.022682458977214992,
      "engine_upload_seconds": 6.3709e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004504583775997162,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.009254875010810792,
      "full": 0.022515457938425243
    }
  },
  "elapsed_seconds": 0.7510825829813257,
  "result_class": "passed"
}
```
