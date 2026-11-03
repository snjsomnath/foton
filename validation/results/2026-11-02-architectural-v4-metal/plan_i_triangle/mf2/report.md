# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_triangle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_triangle",
    "category": "form",
    "question": "How does a triangle opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "triangle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4400000000000002
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "8c3c47518bd3b0c29681c0235b7353ca7e10c6a1aca557d408027137d6c8d9cf",
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
      "scene_fingerprint": 9377062490896781742,
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
      "scene_fingerprint": 9377062490896781742,
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
        "identifier": "plan_i_triangle_grid",
        "bias_percent": 0.0718603497205187,
        "rms_normalized_error_percent": 1.2035155312483643,
        "absolute_error": {
          "p95": 0.0,
          "p99": 8.686911314725876e-07,
          "maximum": 0.00016772851813584566
        },
        "worst_index": [
          36,
          364,
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
        "identifier": "plan_i_triangle_grid",
        "bias_percent": -0.020823854269702912,
        "rms_normalized_error_percent": 2.941555074971266,
        "absolute_error": {
          "p95": 4.514340616879053e-06,
          "p99": 3.9305465179495906e-05,
          "maximum": 0.0003834841772913933
        },
        "worst_index": [
          57,
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
        "identifier": "plan_i_triangle_grid",
        "bias_percent": 0.025028162876232295,
        "rms_normalized_error_percent": 2.2534141774016647,
        "absolute_error": {
          "p95": 3.8710822991561145e-06,
          "p99": 3.163190558552872e-05,
          "maximum": 0.00027159787714481354
        },
        "worst_index": [
          47,
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
            "identifier": "plan_i_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05771605032775093,
                "cvrmse_percent": 72.57330462847852,
                "rms_normalized_rmse_percent": 6.898251330401514,
                "reference_energy": 2.8553639786314307,
                "candidate_energy": 2.8537159753204833,
                "relative_energy_error_percent": 0.057716050327750935,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7337609430542216e-05,
                  "maximum": 0.0005162943853065372
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.002156211412511766,
                  "candidate": 0.0016399170272052288
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.35469170507175657,
                "cvrmse_percent": 521.9530273693895,
                "rms_normalized_rmse_percent": 9.025116360460556,
                "reference_energy": 0.6607039766904848,
                "candidate_energy": 0.6583605144900844,
                "relative_energy_error_percent": 0.35469170507175657,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.507894283160704e-05,
                  "maximum": 0.0007785144844092429
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 146,
                  "rgb_channel": 0,
                  "reference": -0.000320032995659858,
                  "candidate": 0.0004584814887493849
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.89116696454585,
            "full": 390.279583982192
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.2112079942599,
            "full": 373.68820898700505
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 129.71458304673433,
            "full": 375.34020794555545
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.73058298788965,
            "full": 375.4918749909848
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
            "identifier": "plan_i_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.051047123312847484,
                "cvrmse_percent": 54.601930131064066,
                "rms_normalized_rmse_percent": 5.2054912489638845,
                "reference_energy": 2.8578961747662106,
                "candidate_energy": 2.8564373009817245,
                "relative_energy_error_percent": 0.05104712331284749,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.673406256188178e-05,
                  "maximum": 0.0003039590083062649
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 150,
                  "rgb_channel": 0,
                  "reference": 0.0017762435018084943,
                  "candidate": 0.0014722844935022295
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.015675446730248743,
                "cvrmse_percent": 177.17233786683485,
                "rms_normalized_rmse_percent": 5.244824780710368,
                "reference_energy": 1.3066145726358727,
                "candidate_energy": 1.3064097549645695,
                "relative_energy_error_percent": 0.015675446730248743,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.019139452220543e-06,
                  "p95": 6.350785042741336e-06,
                  "p99": 7.258557907334866e-05,
                  "maximum": 0.00044840280315838754
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": -0.00029807325336150825,
                  "candidate": 0.0001503295497968793
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.65737498365343,
            "full": 5036.667458945885
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.26958409044892,
            "full": 5188.546917052008
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.07799996063113,
            "full": 5175.596166984178
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.82466694433242,
            "full": 5186.3695830106735
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
            "identifier": "plan_i_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04902048332772192,
                "cvrmse_percent": 51.693833710548205,
                "rms_normalized_rmse_percent": 4.919809730761691,
                "reference_energy": 2.855999920408067,
                "candidate_energy": 2.85739994537289,
                "relative_energy_error_percent": 0.049020483327721916,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.639290273189545e-05,
                  "maximum": 0.00032478407956659794
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 212,
                  "rgb_channel": 0,
                  "reference": 0.002134918002411723,
                  "candidate": 0.002459702081978321
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.7261853374676537,
                "cvrmse_percent": 174.4349955765439,
                "rms_normalized_rmse_percent": 5.145870968639934,
                "reference_energy": 1.3013867096214575,
                "candidate_energy": 1.3108371890904813,
                "relative_energy_error_percent": 0.7261853374676537,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.026616155921147e-06,
                  "p95": 6.362480235111434e-06,
                  "p99": 6.972215305722904e-05,
                  "maximum": 0.0004909653216600418
                },
                "worst": {
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.009663620498031378,
                  "candidate": 0.01015458581969142
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 191.5339579572901,
            "full": 5497.5957500282675
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.42300000973046,
            "full": 5603.386709000915
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 185.68516592495143,
            "full": 5635.69708308205
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 205.59195801615715,
            "full": 5624.271292006597
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
            "identifier": "plan_i_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.011599034224861391,
                "cvrmse_percent": 30.39687234715719,
                "rms_normalized_rmse_percent": 2.896091078843099,
                "reference_energy": 2.857627435839504,
                "candidate_energy": 2.857295978655202,
                "relative_energy_error_percent": 0.011599034224861391,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.350480353925379e-05,
                  "maximum": 0.00019766599871218204
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.0018148584640584886,
                  "candidate": 0.0016171924653463066
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.35046708775012,
                "cvrmse_percent": 102.03420884105292,
                "rms_normalized_rmse_percent": 3.020709025326611,
                "reference_energy": 1.3041068160940235,
                "candidate_energy": 1.308677281273539,
                "relative_energy_error_percent": 0.35046708775012,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.1133123482286464e-06,
                  "p95": 4.431930278769869e-06,
                  "p99": 4.159483858075101e-05,
                  "maximum": 0.0002912352792918682
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.013813769910484552,
                  "candidate": 0.01410500518977642
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 299.95054204482585,
            "full": 10067.70650006365
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 298.0771670117974,
            "full": 10033.025291981176
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 299.4649999309331,
            "full": 9840.36679205019
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 298.4414170496166,
            "full": 10145.56879189331
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 11365.5633329181,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_triangle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 45014.59541602526,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      74,
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
        "identifier": "plan_i_triangle_grid",
        "full_identifier": "plan_i_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013094850410736667,
            "cvrmse_percent": 6.825480617550058,
            "rms_normalized_rmse_percent": 0.6502254978088472,
            "reference_energy": 2.856727819191107,
            "candidate_energy": 2.856353734956542,
            "relative_energy_error_percent": 0.013094850410736667,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.685578798875467e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2760882735153356,
            "cvrmse_percent": 186.03187057695632,
            "rms_normalized_rmse_percent": 5.5155693346193715,
            "reference_energy": 1.307125930177186,
            "candidate_energy": 1.2904458494621167,
            "relative_energy_error_percent": 1.2760882735153356,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.599785815022187e-06,
              "p95": 1.870122014224762e-05,
              "p99": 4.4310383054835465e-05,
              "maximum": 0.0013602804392576218
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0074473898857831955,
              "candidate": 0.008807670325040817,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4095764639241141,
            "cvrmse_percent": 58.31163324520363,
            "rms_normalized_rmse_percent": 5.5072683416997785,
            "reference_energy": 4.163853749368293,
            "candidate_energy": 4.146799584418659,
            "relative_energy_error_percent": 0.40957646392411406,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.588741536641464e-06,
              "p95": 1.85335647984175e-05,
              "p99": 4.425578226801069e-05,
              "maximum": 0.0013602804392576218
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0074473898857831955,
              "candidate": 0.008807670325040817,
              "position": [
                3.5,
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
      74,
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
        "identifier": "plan_i_triangle_grid",
        "full_identifier": "plan_i_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013094850410736667,
            "cvrmse_percent": 6.825480617550058,
            "rms_normalized_rmse_percent": 0.6502254978088472,
            "reference_energy": 2.856727819191107,
            "candidate_energy": 2.856353734956542,
            "relative_energy_error_percent": 0.013094850410736667,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.685578798875467e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 96.3119853910979,
            "cvrmse_percent": 1339.9908997372484,
            "rms_normalized_rmse_percent": 23.081070066830115,
            "reference_energy": 0.6573444035478815,
            "candidate_energy": 1.2904458494621167,
            "relative_energy_error_percent": 96.31198539109789,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.181502726576582e-06,
              "p95": 2.990000029967632e-05,
              "p99": 8.262635897153817e-05,
              "maximum": 0.00394524447619915
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004862425848841667,
              "candidate": 0.008807670325040817,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 18.0055309502575,
            "cvrmse_percent": 250.60700181042515,
            "rms_normalized_rmse_percent": 23.076237731793622,
            "reference_energy": 3.5140722227389887,
            "candidate_energy": 4.146799584418659,
            "relative_energy_error_percent": 18.005530950257498,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.129999746917747e-06,
              "p95": 2.995000068040099e-05,
              "p99": 8.250522587332015e-05,
              "maximum": 0.00394524447619915
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004862425848841667,
              "candidate": 0.008807670325040817,
              "position": [
                3.5,
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
      "bias_percent": -0.014814491677374553,
      "rms_normalized_error_percent": 0.3055151650550404,
      "absolute_error": {
        "p95": 0.057150203746425925,
        "p99": 0.07976962069451808,
        "maximum": 0.08297206682915714
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.615006005947961,
      "rms_normalized_to_uniform_percent": 0.3055151650550404
    },
    "overcast": {
      "bias_percent": -0.09216914678118472,
      "rms_normalized_error_percent": 0.2738530272558361,
      "absolute_error": {
        "p95": 0.039013715088367464,
        "p99": 0.05147201120853421,
        "maximum": 0.05731624364852905
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.647700548171997,
      "rms_normalized_to_uniform_percent": 0.18696255666403988
    },
    "horizon": {
      "bias_percent": 1.0527659983671618,
      "rms_normalized_error_percent": 2.8594943839249036,
      "absolute_error": {
        "p95": 0.03886081176159919,
        "p99": 0.05210575031565774,
        "maximum": 0.07233774150489604
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.32168892715454367,
      "rms_normalized_to_uniform_percent": 0.18933431995516556
    },
    "north": {
      "bias_percent": -100.0,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 6.691489088552738e-05,
        "p99": 0.00029287185214343285,
        "maximum": 0.0006511706160381436
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.8161694242735393e-05,
      "rms_normalized_to_uniform_percent": 0.0008685084742574946
    },
    "east": {
      "bias_percent": 0.08368594033486589,
      "rms_normalized_error_percent": 0.5928012363448396,
      "absolute_error": {
        "p95": 0.02324067950248718,
        "p99": 0.04774447083473204,
        "maximum": 0.050589680671691895
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.4734984338283539,
      "rms_normalized_to_uniform_percent": 0.12089839996899335
    },
    "south": {
      "bias_percent": -0.02524015734058749,
      "rms_normalized_error_percent": 0.33660630658393675,
      "absolute_error": {
        "p95": 0.04397697672247885,
        "p99": 0.04987894773483274,
        "maximum": 0.05357933044433594
      },
      "worst_index": [
        53
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.8681985139846802,
      "rms_normalized_to_uniform_percent": 0.23485042495862193
    },
    "west": {
      "bias_percent": 0.0313060388184573,
      "rms_normalized_error_percent": 0.5934125750957322,
      "absolute_error": {
        "p95": 0.027371922135353086,
        "p99": 0.029313130378723143,
        "maximum": 0.029554009437561035
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.48109179735183716,
      "rms_normalized_to_uniform_percent": 0.12259920737580668
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
        "identifier": "plan_i_triangle_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.2040229404207649,
          "cvrmse_percent": 8.905445736152435,
          "absolute_error_percentiles_lux": {
            "p50": 0.8032991886138916,
            "p90": 23.140258026123075,
            "p95": 42.84218292236326,
            "p99": 96.91625579833972
          },
          "maximum_absolute_error_lux": 443.9609375,
          "worst": {
            "sensor_index": 48,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5243.5,
            "foton_lux": 16419.36328125,
            "radiance_lux": 15975.40234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.33241206960385056,
            "maximum_error_percentage_points": 3.152602739726028,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5804847415763258,
            "maximum_error_percentage_points": 3.819479775042282,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.8398889300259158,
            "maximum_error_percentage_points": 8.8186301369863,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.8430840429470567,
            "maximum_error_percentage_points": 8.818630136986304,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007239911144020736,
            "maximum_error_percentage_points": 0.2450684931506828,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.405405405405405,
          "radiance_percent": 5.405405405405405,
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
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004930340492562024,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.007994542014785111,
      "weather_seconds": 0.11475120892282575,
      "metric_reduction_seconds": 0.0744856660021469,
      "write_seconds": 0.024200374959036708,
      "total_seconds": 0.21366366592701524,
      "cold_end_to_end_seconds": 0.22165820794180036,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010484667029231787,
      "engine_upload_seconds": 0.000860292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.021216041641309857,
      "engine_annual_reduction_seconds": 0.003118499997071922,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.021216041641309857
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007994542014785111,
      "weather_seconds": 0.10788949998095632,
      "metric_reduction_seconds": 0.04648791695944965,
      "write_seconds": 0.024464874994009733,
      "total_seconds": 0.17899895797017962,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.17899895797017962,
      "raw_export_seconds": 0.011100957985036075,
      "engine_upload_seconds": 8.15e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031464999774470925,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012866375036537647,
      "full": 0.019982416997663677
    }
  },
  "elapsed_seconds": 147.10862183303107,
  "result_class": "passed"
}
```
