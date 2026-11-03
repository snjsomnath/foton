# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 6,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 7.199999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "42366c3fe6521a2b59b8941896e17ac4ef4fa651260e0df490a72e1b5e812cdf",
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
      "scene_fingerprint": 16609558811435530087,
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
      "scene_fingerprint": 16609558811435530087,
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
    "model_sha256": "63500a2338c49a83abc067a45b369e227c59a944c9cd7e3b2c344bd71899e25f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "738a59ae8fb6881ea29066a9316dfc51647b6e94d0eae23cc7b76edc5ea48e16",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013830000534653664,
          "p95": 1.0354851838201284e-06,
          "p99": 1.6205012798309326e-05
        },
        "bias_percent": 0.02240261507224657,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8140958491552015,
        "worst_index": [
          5,
          522,
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
          "maximum": 0.0007016845047473907,
          "p95": 4.243757575750351e-05,
          "p99": 0.00011139741400256753
        },
        "bias_percent": 0.04753250077638773,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6320055782780956,
        "worst_index": [
          42,
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
          "maximum": 0.0005546547472476959,
          "p95": 3.3210173569386825e-05,
          "p99": 9.157450404018164e-05
        },
        "bias_percent": 0.028406538996942277,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3348697079601222,
        "worst_index": [
          42,
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006514255073852837,
                  "p50": 0.0,
                  "p90": 1.3586560498879408e-06,
                  "p95": 9.132403647527099e-05,
                  "p99": 0.00023686308122705668
                },
                "candidate_energy": 11.714590195364508,
                "cvrmse_percent": 33.54763572033625,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02876169718029066,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.711221849200129,
                "relative_energy_error_percent": 0.028761697180290657,
                "rms_normalized_rmse_percent": 7.8135814469571905,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0025588220451027155,
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "reference": 0.0019073965377174318,
                  "rgb_channel": 0,
                  "sky_patch_index": 183
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013455000007525086,
                  "p50": 0.0,
                  "p90": 2.3497879737988114e-05,
                  "p95": 0.00011785885544668417,
                  "p99": 0.00032499252120032907
                },
                "candidate_energy": 3.460020265851309,
                "cvrmse_percent": 153.13487583596813,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5470143690225081,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4411964269297144,
                "relative_energy_error_percent": 0.5470143690225081,
                "rms_normalized_rmse_percent": 5.951628656378272,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0005542720318771899,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.0007912279688753188,
                  "rgb_channel": 0,
                  "sky_patch_index": 125
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.01800006069243,
            "full": 290.06899998057634
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.85537500493228,
            "full": 292.2595830168575
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.9534579049796,
            "full": 297.1729579148814
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.03608298581094,
            "full": 299.34662498999387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.87066606245935,
            "full": 291.2412090227008
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.526917017065,
            "full": 301.13604199141264
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.41358306631446,
            "full": 304.10325003322214
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.3795840619132,
            "full": 292.5550830550492
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00034938438329845667,
                  "p50": 0.0,
                  "p90": 1.234002411365509e-06,
                  "p95": 5.130103090777993e-05,
                  "p99": 0.00015438348054885864
                },
                "candidate_energy": 11.719457110349175,
                "cvrmse_percent": 20.494076305690733,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05056593562469323,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.713534052260933,
                "relative_energy_error_percent": 0.05056593562469323,
                "rms_normalized_rmse_percent": 4.7772360113277434,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0030754770850762725,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.003424861468374729,
                  "rgb_channel": 0,
                  "sky_patch_index": 246
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007104258984327316,
                  "p50": 3.861862296616891e-06,
                  "p90": 2.2836742573417723e-05,
                  "p95": 8.179841097444296e-05,
                  "p99": 0.00022787085617892444
                },
                "candidate_energy": 6.6316510414629946,
                "cvrmse_percent": 55.81465749425497,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0021479307336144705,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.631508601251646,
                "relative_energy_error_percent": 0.002147930733614471,
                "rms_normalized_rmse_percent": 3.0519375903892856,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03211299516260624,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.03140256926417351,
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.27466601133347,
            "full": 3240.233291988261
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.57187499292195,
            "full": 3166.5292500983924
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.67083300836384,
            "full": 3186.3639580551535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.57829198613763,
            "full": 3216.4515419863164
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00044030603021383286,
                  "p50": 0.0,
                  "p90": 1.38175437314203e-06,
                  "p95": 4.9299036618322134e-05,
                  "p99": 0.00015462050214409828
                },
                "candidate_energy": 11.718181912891936,
                "cvrmse_percent": 20.858604837535925,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02744421900149418,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.72139875923746,
                "relative_energy_error_percent": 0.02744421900149418,
                "rms_normalized_rmse_percent": 4.864550108649164,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002065384527668357,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.0025056905578821898,
                  "rgb_channel": 0,
                  "sky_patch_index": 227
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009641749784350395,
                  "p50": 3.8817322547402e-06,
                  "p90": 2.3419532226398587e-05,
                  "p95": 7.718754932284355e-05,
                  "p99": 0.00022583080135518685
                },
                "candidate_energy": 6.627561762737905,
                "cvrmse_percent": 55.51958539640882,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2842017187407642,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.6464510909737164,
                "relative_energy_error_percent": 0.2842017187407642,
                "rms_normalized_rmse_percent": 3.0417863536479657,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028037399984896183,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.029001574963331223,
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.10233297478408,
            "full": 3374.3004580028355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.56241689436138,
            "full": 3426.6369589604437
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.9630839470774,
            "full": 3459.8617909941822
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.46879197657108,
            "full": 3385.0534999510273
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021245400421321392,
                  "p50": 0.0,
                  "p90": 8.114438969641924e-07,
                  "p95": 3.160515188938007e-05,
                  "p99": 8.163851452991366e-05
                },
                "candidate_energy": 11.717693467664631,
                "cvrmse_percent": 11.31274651139753,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.010156717293758047,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.718883721554214,
                "relative_energy_error_percent": 0.010156717293758045,
                "rms_normalized_rmse_percent": 2.6386727699898387,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015429750201292336,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.0017554290243424475,
                  "rgb_channel": 0,
                  "sky_patch_index": 142
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006571058183908463,
                  "p50": 2.7469341148389503e-06,
                  "p90": 1.5611702110618353e-05,
                  "p95": 4.301011358620599e-05,
                  "p99": 0.00012166495434939861
                },
                "candidate_energy": 6.645415137667602,
                "cvrmse_percent": 30.94375028004169,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05096101303524817,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.64203029174482,
                "relative_energy_error_percent": 0.05096101303524817,
                "rms_normalized_rmse_percent": 1.6933358467063813,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0329629797488451,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.03362008556723595,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 291.250207927078,
            "full": 5959.940375061706
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 277.75995898991823,
            "full": 5954.379541915841
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 282.9842079663649,
            "full": 6019.9590410338715
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 294.567208038643,
            "full": 5944.846875034273
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_l_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4577.491000061855,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18962.533292011358,
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
        "identifier": "plan_l_distributed_grid",
        "full_identifier": "plan_l_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1445532788499928,
            "cvrmse_percent": 2.9824048212010665,
            "rms_normalized_rmse_percent": 0.6954762104986967,
            "reference_energy": 11.718186119141109,
            "candidate_energy": 11.701247096884146,
            "relative_energy_error_percent": 0.14455327884999283,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.2294622138142586e-06,
              "p99": 1.6238438547588885e-05,
              "maximum": 9.953993139788508e-05
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.0004760126175824553,
              "candidate": 0.0003764726861845702,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.3530195983966673,
            "cvrmse_percent": 19.641175647970606,
            "rms_normalized_rmse_percent": 1.0751017035068022,
            "reference_energy": 6.643825162621242,
            "candidate_energy": 6.667279167528505,
            "relative_energy_error_percent": 0.3530195983966673,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.4321677730986266e-06,
              "p90": 1.3858847523806617e-05,
              "p95": 2.2271611669566482e-05,
              "p99": 5.623835022561252e-05,
              "maximum": 0.0007336996495723724
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03702041134238243,
              "candidate": 0.0377541109919548,
              "position": [
                0.5,
                7.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.03548076814858456,
            "cvrmse_percent": 6.933145558054063,
            "rms_normalized_rmse_percent": 1.0488525619727145,
            "reference_energy": 18.362011281762353,
            "candidate_energy": 18.36852626441265,
            "relative_energy_error_percent": 0.035480768148579714,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.4253229159730836e-06,
              "p90": 1.3580502127297223e-05,
              "p95": 2.1440231648739427e-05,
              "p99": 5.337758921086788e-05,
              "maximum": 0.0007336996495723724
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03702041134238243,
              "candidate": 0.0377541109919548,
              "position": [
                0.5,
                7.5,
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
        "identifier": "plan_l_distributed_grid",
        "full_identifier": "plan_l_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1445532788499928,
            "cvrmse_percent": 2.9824048212010665,
            "rms_normalized_rmse_percent": 0.6954762104986967,
            "reference_energy": 11.718186119141109,
            "candidate_energy": 11.701247096884146,
            "relative_energy_error_percent": 0.14455327884999283,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.2294622138142586e-06,
              "p99": 1.6238438547588885e-05,
              "maximum": 9.953993139788508e-05
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.0004760126175824553,
              "candidate": 0.0003764726861845702,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 93.51651585076418,
            "cvrmse_percent": 1097.5799057677546,
            "rms_normalized_rmse_percent": 42.654824314579926,
            "reference_energy": 3.4453282388931434,
            "candidate_energy": 6.667279167528505,
            "relative_energy_error_percent": 93.51651585076418,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.764999979059212e-05,
              "p90": 4.463000004761852e-05,
              "p95": 5.8530960814096034e-05,
              "p99": 0.00012643146328628063,
              "maximum": 0.014250101521611214
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02848229743540287,
              "candidate": 0.042732398957014084,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.13633970795333,
            "cvrmse_percent": 249.3680418021272,
            "rms_normalized_rmse_percent": 42.65226197845546,
            "reference_energy": 15.163514358034252,
            "candidate_energy": 18.36852626441265,
            "relative_energy_error_percent": 21.136339707953336,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.759000042511616e-05,
              "p90": 4.4448766857385635e-05,
              "p95": 5.7906145229935646e-05,
              "p99": 0.00012387172318995,
              "maximum": 0.014250101521611214
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02848229743540287,
              "candidate": 0.042732398957014084,
              "position": [
                6.5,
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
      "bias_percent": 0.04780896278222286,
      "rms_normalized_error_percent": 0.1775276796077444,
      "absolute_error": {
        "p95": 0.07846476508992412,
        "p99": 0.125576887863975,
        "maximum": 0.14516923093284007
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.29957134350894,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1775276796077444
    },
    "overcast": {
      "bias_percent": 0.036711229248413885,
      "rms_normalized_error_percent": 0.12937202320642943,
      "absolute_error": {
        "p95": 0.04536540508270263,
        "p99": 0.05438164234161378,
        "maximum": 0.057713985443115234
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.128602027893066,
      "reference_fraction_of_uniform": 0.643287718296051,
      "rms_normalized_to_uniform_percent": 0.08933014921661263
    },
    "horizon": {
      "bias_percent": 0.5315499984366735,
      "rms_normalized_error_percent": 1.590365716040986,
      "absolute_error": {
        "p95": 0.06227710820799179,
        "p99": 0.09509542401204352,
        "maximum": 0.11684638043700879
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8205801263015864,
      "reference_fraction_of_uniform": 0.10523845303165245,
      "rms_normalized_to_uniform_percent": 0.12291140398452059
    },
    "north": {
      "bias_percent": -0.006424021514833966,
      "rms_normalized_error_percent": 0.32202864091282607,
      "absolute_error": {
        "p95": 0.051750433444976804,
        "p99": 0.0794020748138428,
        "maximum": 0.09360504150390625
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.4411444664001465,
      "reference_fraction_of_uniform": 0.3145247995853424,
      "rms_normalized_to_uniform_percent": 0.1118605168480061
    },
    "east": {
      "bias_percent": 0.08811244339573406,
      "rms_normalized_error_percent": 0.32755922731951864,
      "absolute_error": {
        "p95": 0.0551905632019043,
        "p99": 0.1083589553833009,
        "maximum": 0.1546025276184082
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.86308479309082,
      "reference_fraction_of_uniform": 0.33891502022743225,
      "rms_normalized_to_uniform_percent": 0.1374684656818444
    },
    "south": {
      "bias_percent": 0.017206929607858943,
      "rms_normalized_error_percent": 0.105311556465802,
      "absolute_error": {
        "p95": 0.014256641268730162,
        "p99": 0.020804767608642586,
        "maximum": 0.02463531494140625
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.565431594848633,
      "reference_fraction_of_uniform": 0.20609940588474274,
      "rms_normalized_to_uniform_percent": 0.032416360821299374
    },
    "west": {
      "bias_percent": 0.07569145024914678,
      "rms_normalized_error_percent": 0.26277313955250026,
      "absolute_error": {
        "p95": 0.04111343622207639,
        "p99": 0.06212538957595825,
        "maximum": 0.062496185302734375
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7381465435028076,
      "reference_fraction_of_uniform": 0.21608318388462067,
      "rms_normalized_to_uniform_percent": 0.07179910847460297
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
        "identifier": "plan_l_distributed_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.042523371965673545,
          "cvrmse_percent": 1.751005814373806,
          "absolute_error_percentiles_lux": {
            "p50": 2.86224365234375,
            "p90": 20.226791381835938,
            "p95": 30.888745117187483,
            "p99": 68.04688476562444
          },
          "maximum_absolute_error_lux": 336.0791015625,
          "worst": {
            "sensor_index": 4,
            "position": [
              0.5,
              7.5,
              0.75
            ],
            "hour_of_year": 2718.5,
            "foton_lux": 9487.048828125,
            "radiance_lux": 9150.9697265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.27457191780821816,
            "maximum_error_percentage_points": 1.345616438356167,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09228710202242851,
            "maximum_error_percentage_points": 0.5238755807265676,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06815353881278548,
            "maximum_error_percentage_points": 0.38232876712329045,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07418093607305787,
            "maximum_error_percentage_points": 0.38232876712328334,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.012051940639269593,
            "maximum_error_percentage_points": 0.0849315068493155,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 68.75,
          "radiance_percent": 70.83333333333333,
          "difference_percentage_points": 2.0833333333333286,
          "tolerance_percentage_points": 2.0833333333333335,
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
      "maximum_error_percentage_points": 0.0049999999999954525,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.0049999999999954525,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
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
      "study_preparation_seconds": 0.4417225500001223,
      "weather_seconds": 0.46467023299919674,
      "metric_reduction_seconds": 2.1076888060015335,
      "write_seconds": 0.0334810300009849,
      "total_seconds": 2.6062589100001787,
      "cold_end_to_end_seconds": 3.047981460000301,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.018615290999150602,
      "engine_upload_seconds": 0.054898207,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.049335835,
      "engine_annual_reduction_seconds": 0.057794065,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.049335835
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.4417225500001223,
      "weather_seconds": 0.2566125119992648,
      "metric_reduction_seconds": 1.2873973880014091,
      "write_seconds": 0.022976399999606656,
      "total_seconds": 1.567354446000536,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.567354446000536,
      "raw_export_seconds": 0.01025745500010089,
      "engine_upload_seconds": 0.046333309,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.5e-08,
      "engine_annual_reduction_seconds": 0.039534669,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02242972599924542,
      "full": 0.06892295700163231
    }
  },
  "elapsed_seconds": 7.1978816630035,
  "result_class": "passed"
}
```
