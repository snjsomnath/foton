# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c7e1fab789446e0493454b33f7ebc8fad8745ff95f47ebd7b153bd46314e6706",
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
      "scene_fingerprint": 15456329952842906508,
      "basis": "Tregenza",
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
      "scene_fingerprint": 15456329952842906508,
      "basis": "Tregenza",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "7ef280ef301b48ef82f9441fbef4706bbe2ee9ba8d842fa3ff8c8633f57ea37a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00047375215217471123,
          "p95": 8.67992639541626e-07,
          "p99": 6.115669384598732e-05
        },
        "bias_percent": -0.03381505790352882,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9466113379090904,
        "worst_index": [
          21,
          99,
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
          "maximum": 0.0004827529191970825,
          "p95": 3.2548559829592705e-05,
          "p99": 0.00012043491005897522
        },
        "bias_percent": -0.0257898816484027,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8589026194773917,
        "worst_index": [
          19,
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
          "maximum": 0.00039875321090221405,
          "p95": 2.7616682928055525e-05,
          "p99": 0.00010136375203728676
        },
        "bias_percent": 0.007796640749618773,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7219635563718043,
        "worst_index": [
          6,
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.001412009820342064,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.239649469032884e-05,
                  "p99": 0.0005052658962085843
                },
                "candidate_energy": 6.852349147651694,
                "cvrmse_percent": 28.24873931726952,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02676817744601073,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.8541838877572445,
                "relative_energy_error_percent": 0.026768177446010732,
                "rms_normalized_rmse_percent": 5.104583845379491,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014460129663348198,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.015872139483690262,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016701798886060715,
                  "p50": 0.0,
                  "p90": 1.152237928181421e-05,
                  "p95": 0.00012243911623954773,
                  "p99": 0.0006040135631337762
                },
                "candidate_energy": 2.2832148798801057,
                "cvrmse_percent": 102.35082851621364,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4546264198018559,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.272881758913229,
                "relative_energy_error_percent": 0.4546264198018559,
                "rms_normalized_rmse_percent": 4.609707877203519,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0010110903531312943,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": -0.0006590895354747772,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.6683750282973,
            "full": 289.09720794763416
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.93270802870393,
            "full": 274.1700420156121
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.93391695898026,
            "full": 274.10154207609594
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.21799996122718,
            "full": 277.02987496741116
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00046840799041092396,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2755935788154602e-05,
                  "p99": 0.0001390285324305296
                },
                "candidate_energy": 6.858399724730589,
                "cvrmse_percent": 7.691154726682098,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.0988635396997046,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.865186891498524,
                "relative_energy_error_percent": 0.0988635396997046,
                "rms_normalized_rmse_percent": 1.3928984389711327,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00549835292622447,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.005966760916635394,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007333951070904732,
                  "p50": 1.1107617048367047e-07,
                  "p90": 2.3933054762892425e-05,
                  "p95": 6.000930443406105e-05,
                  "p99": 0.00023154960945248604
                },
                "candidate_energy": 4.264254508439208,
                "cvrmse_percent": 21.59856855050663,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.042612188711208886,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.266072375250307,
                "relative_energy_error_percent": 0.042612188711208886,
                "rms_normalized_rmse_percent": 1.5460493877832033,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.027574115432798862,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.02684072032570839,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.3889590157196,
            "full": 3079.163207905367
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.91929194610566,
            "full": 3070.9673339733854
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.6488750334829,
            "full": 3486.3896659808233
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.9497499410063,
            "full": 3111.332874977961
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00029999413527548313,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.317491453140974e-05,
                  "p99": 0.00016389612574130297
                },
                "candidate_energy": 6.858840367796347,
                "cvrmse_percent": 8.250730261647329,
                "energy_difference_negligible": true,
                "nmbe_percent": 6.546022314727187e-05,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.858835877987076,
                "relative_energy_error_percent": 6.546022314727186e-05,
                "rms_normalized_rmse_percent": 1.4946816632171973,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0057088276371359825,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.005408833501860499,
                  "rgb_channel": 0,
                  "sky_patch_index": 69
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007423297502100468,
                  "p50": 1.1316044634668287e-07,
                  "p90": 2.192755346186459e-05,
                  "p95": 6.063212640583515e-05,
                  "p99": 0.0002553388476371765
                },
                "candidate_energy": 4.266564403973511,
                "cvrmse_percent": 23.2949114570727,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06169895714707903,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.263933601407999,
                "relative_energy_error_percent": 0.06169895714707902,
                "rms_normalized_rmse_percent": 1.6698720200788948,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008163545280694962,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 7.402477785944939e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.05333394464105,
            "full": 3319.0794590627775
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.0192499710247,
            "full": 3310.880708042532
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.54745896812528,
            "full": 3284.1895410092548
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.31612509302795,
            "full": 3255.7977499673143
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002050497569143772,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1710042599588633e-05,
                  "p99": 7.738335989415646e-05
                },
                "candidate_energy": 6.859094972998037,
                "cvrmse_percent": 4.225003384715199,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.016817126565952925,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.857941664268537,
                "relative_energy_error_percent": 0.016817126565952925,
                "rms_normalized_rmse_percent": 0.7649624012207861,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013642259873449802,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.01384730963036418,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00046387314796447754,
                  "p50": 8.604744472506809e-08,
                  "p90": 1.568444713484496e-05,
                  "p95": 3.569014370441437e-05,
                  "p99": 0.00013802014291286469
                },
                "candidate_energy": 4.262729431184976,
                "cvrmse_percent": 12.840228270314553,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17361044356829897,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.270142845119388,
                "relative_energy_error_percent": 0.17361044356829897,
                "rms_normalized_rmse_percent": 0.9214987823126743,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04926043562591076,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.049724308773875237,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 230.25116696953773,
            "full": 5812.922916957177
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.2314589722082,
            "full": 5874.2334169801325
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.7940000258386,
            "full": 5839.774208026938
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.31216608919203,
            "full": 5867.48354206793
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_j_large_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1276.942666969262,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4749.672583071515,
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
      47,
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
        "identifier": "plan_j_large_center_grid",
        "full_identifier": "plan_j_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04105251183138555,
            "cvrmse_percent": 2.9919694884861023,
            "rms_normalized_rmse_percent": 0.5418529738247068,
            "reference_energy": 6.858967140185541,
            "candidate_energy": 6.861782918482277,
            "relative_energy_error_percent": 0.041052511831385544,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 5.364418029785156e-07,
              "p99": 4.669860936701298e-05,
              "maximum": 0.0002032015472650528
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.00414408789947629,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8602890863736916,
            "cvrmse_percent": 20.714404265530266,
            "rms_normalized_rmse_percent": 1.4853438787608344,
            "reference_energy": 4.265987307626668,
            "candidate_energy": 4.229287484393069,
            "relative_energy_error_percent": 0.8602890863736915,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.533511178626213e-07,
              "p90": 2.945610322058201e-05,
              "p95": 4.9756388762034476e-05,
              "p99": 0.00012045804760418832,
              "maximum": 0.0012351199984550476
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03975141793489456,
              "candidate": 0.038516297936439514,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.30457693193995133,
            "cvrmse_percent": 7.885501747995332,
            "rms_normalized_rmse_percent": 1.474560438233847,
            "reference_energy": 11.12495444781221,
            "candidate_energy": 11.091070402875346,
            "relative_energy_error_percent": 0.3045769319399514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.533511178626213e-07,
              "p90": 2.9206275939941406e-05,
              "p95": 4.8076268285512924e-05,
              "p99": 0.00011590076610445976,
              "maximum": 0.0012351199984550476
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03975141793489456,
              "candidate": 0.038516297936439514,
              "position": [
                6.5,
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
      47,
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
        "identifier": "plan_j_large_center_grid",
        "full_identifier": "plan_j_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04105251183138555,
            "cvrmse_percent": 2.9919694884861023,
            "rms_normalized_rmse_percent": 0.5418529738247068,
            "reference_energy": 6.858967140185541,
            "candidate_energy": 6.861782918482277,
            "relative_energy_error_percent": 0.041052511831385544,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 5.364418029785156e-07,
              "p99": 4.669860936701298e-05,
              "maximum": 0.0002032015472650528
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.00414408789947629,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.11973093823877,
            "cvrmse_percent": 529.3477634121042,
            "rms_normalized_rmse_percent": 23.824674504870863,
            "reference_energy": 2.272347731792337,
            "candidate_energy": 4.229287484393069,
            "relative_energy_error_percent": 86.11973093823877,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021606427617371082,
              "p95": 0.000326563254930079,
              "p99": 0.000595566991250962,
              "maximum": 0.010993711650371552
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0501331090927124,
              "candidate": 0.061126820743083954,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.461920417524457,
            "cvrmse_percent": 131.75199906364776,
            "rms_normalized_rmse_percent": 23.828770499880402,
            "reference_energy": 9.131314871977878,
            "candidate_energy": 11.091070402875346,
            "relative_energy_error_percent": 21.46192041752446,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002168805804103613,
              "p95": 0.00032641318193782354,
              "p99": 0.0005999098066240549,
              "maximum": 0.010993711650371552
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0501331090927124,
              "candidate": 0.061126820743083954,
              "position": [
                4.5,
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
      "bias_percent": 0.10372073380949418,
      "rms_normalized_error_percent": 0.19988067060953282,
      "absolute_error": {
        "p95": 0.08407467337793498,
        "p99": 0.11037561180330097,
        "maximum": 0.12515519236268702
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.402307516763376,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19988067060953282
    },
    "overcast": {
      "bias_percent": 0.07847937596393185,
      "rms_normalized_error_percent": 0.161728452970666,
      "absolute_error": {
        "p95": 0.05435017347335815,
        "p99": 0.06141165733337402,
        "maximum": 0.06604576110839844
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.857826232910156,
      "reference_fraction_of_uniform": 0.659260094165802,
      "rms_normalized_to_uniform_percent": 0.11456914256404148
    },
    "horizon": {
      "bias_percent": 0.34678651190536924,
      "rms_normalized_error_percent": 1.4933381641749885,
      "absolute_error": {
        "p95": 0.0300914569400897,
        "p99": 0.04535750383322508,
        "maximum": 0.05481632519533797
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8675247734502763,
      "reference_fraction_of_uniform": 0.08339733968182111,
      "rms_normalized_to_uniform_percent": 0.07635338871381418
    },
    "north": {
      "bias_percent": -16.7368225754609,
      "rms_normalized_error_percent": 148.84370444757948,
      "absolute_error": {
        "p95": 9.610583229004987e-05,
        "p99": 0.0001260619459208101,
        "maximum": 0.00013803645560983568
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.351173978036968e-05,
      "reference_fraction_of_uniform": 1.2989175957045518e-06,
      "rms_normalized_to_uniform_percent": 0.00016972006728287008
    },
    "east": {
      "bias_percent": 0.048753503249621605,
      "rms_normalized_error_percent": 0.29240612479218464,
      "absolute_error": {
        "p95": 0.03134057521820067,
        "p99": 0.04300952434539795,
        "maximum": 0.045144081115722656
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2680342197418213,
      "reference_fraction_of_uniform": 0.2180318385362625,
      "rms_normalized_to_uniform_percent": 0.06446495055364002
    },
    "south": {
      "bias_percent": 0.15236396127378057,
      "rms_normalized_error_percent": 0.24521573680241054,
      "absolute_error": {
        "p95": 0.06041631698608398,
        "p99": 0.09015110015869136,
        "maximum": 0.11203384399414062
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.76556921005249,
      "reference_fraction_of_uniform": 0.6503912210464478,
      "rms_normalized_to_uniform_percent": 0.15658200458137653
    },
    "west": {
      "bias_percent": 0.04885357769353267,
      "rms_normalized_error_percent": 0.2887108888977832,
      "absolute_error": {
        "p95": 0.026608085632324214,
        "p99": 0.03113626480102539,
        "maximum": 0.03248786926269531
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1092581748962402,
      "reference_fraction_of_uniform": 0.20276829600334167,
      "rms_normalized_to_uniform_percent": 0.06011436639308074
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
        "identifier": "plan_j_large_center_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.052558197011352566,
          "cvrmse_percent": 1.6557011498693526,
          "absolute_error_percentiles_lux": {
            "p50": 1.688995361328125,
            "p90": 19.34108886718751,
            "p95": 31.12455444335934,
            "p99": 64.97546142578133
          },
          "maximum_absolute_error_lux": 315.7958984375,
          "worst": {
            "sensor_index": 19,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 11825.984375,
            "radiance_lux": 11510.1884765625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.41435150102011037,
            "maximum_error_percentage_points": 1.9215068493150689,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2917290312664834,
            "maximum_error_percentage_points": 1.2895932157724772,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3577790731565141,
            "maximum_error_percentage_points": 3.0393150684931527,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.35861847857767326,
            "maximum_error_percentage_points": 3.039315068493151,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.020326435441562506,
            "maximum_error_percentage_points": 0.08082191780821918,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 31.914893617021278,
          "radiance_percent": 31.914893617021278,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
          "ambiguous_sensor_count": 2,
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
      "maximum_error_percentage_points": 0.0049694991438258285,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.0049694991438258285,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.004520547945205955,
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
      "study_preparation_seconds": 0.36987079000027734,
      "weather_seconds": 0.23295204200258013,
      "metric_reduction_seconds": 0.19373797299704165,
      "write_seconds": 0.03712174699830939,
      "total_seconds": 0.46423504500126,
      "cold_end_to_end_seconds": 0.8341058350015373,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02438895399973262,
      "engine_upload_seconds": 0.014168017,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.013522534,
      "engine_annual_reduction_seconds": 0.008127248,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.013522534
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.36987079000027734,
      "weather_seconds": 0.23229628999979468,
      "metric_reduction_seconds": 0.19841631799863535,
      "write_seconds": 0.022698519998812117,
      "total_seconds": 0.45371227800205816,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.45371227800205816,
      "raw_export_seconds": 0.01020093400074984,
      "engine_upload_seconds": 0.014397707,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.9e-08,
      "engine_annual_reduction_seconds": 0.008575046,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013794910999422427,
      "full": 0.02496286500172573
    }
  },
  "elapsed_seconds": 2.5928328099980718,
  "result_class": "passed"
}
```
