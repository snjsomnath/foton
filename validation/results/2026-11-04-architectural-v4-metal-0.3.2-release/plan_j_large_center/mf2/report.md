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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "8a92f5e3aeb9a96eb56bb8cc2af4aeeed90840685501b7ef903fb21ff3d78a3b",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 15456329952842906508,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 15456329952842906508,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "7ef280ef301b48ef82f9441fbef4706bbe2ee9ba8d842fa3ff8c8633f57ea37a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013817357830703259,
          "p95": 8.381903171539307e-09,
          "p99": 6.103131454437971e-06
        },
        "bias_percent": 0.05769303111791913,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.742177736536679,
        "worst_index": [
          13,
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
          "maximum": 0.0006030164659023285,
          "p95": 1.650722697377205e-05,
          "p99": 8.966214954853058e-05
        },
        "bias_percent": 0.039283153116813255,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4184626677954273,
        "worst_index": [
          12,
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
          "maximum": 0.00031860917806625366,
          "p95": 1.3979384675621986e-05,
          "p99": 7.367867510765791e-05
        },
        "bias_percent": 0.00041428877420842194,
        "identifier": "plan_j_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1549280941307185,
        "worst_index": [
          12,
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000640246958937496,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3801112547516823e-07,
                  "p99": 0.0001863665456767194
                },
                "candidate_energy": 6.8624025091739895,
                "cvrmse_percent": 39.96919103987208,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.026681269430505694,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.864233973934915,
                "relative_energy_error_percent": 0.026681269430505694,
                "rms_normalized_rmse_percent": 7.014695806734324,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018291544984094799,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.001188907539471984,
                  "rgb_channel": 0,
                  "sky_patch_index": 146
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008767107501626015,
                  "p50": 0.0,
                  "p90": 1.5155367236729944e-06,
                  "p95": 2.3682745450059883e-05,
                  "p99": 0.00025718065444380045
                },
                "candidate_energy": 2.280676041763087,
                "cvrmse_percent": 166.53277239512397,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2592887125704361,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.2747777996924263,
                "relative_energy_error_percent": 0.2592887125704361,
                "rms_normalized_rmse_percent": 4.94095428391783,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02587160700932145,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.026748317759484053,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.41491599101573,
            "full": 276.0809580795467
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.36120805796236,
            "full": 275.9758329484612
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.19020805787295,
            "full": 275.65641689579934
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.31483301427215,
            "full": 282.194749917835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.8532919762656,
            "full": 281.09462501015514
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.7509580142796,
            "full": 293.00508403684944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.67241603229195,
            "full": 275.6673749536276
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.50362492725253,
            "full": 273.319625062868
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003065734636038542,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.125154085457325e-07,
                  "p99": 0.00011404097313061357
                },
                "candidate_energy": 6.8539799122690965,
                "cvrmse_percent": 25.00200708844358,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.08367041765222936,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.859719468197909,
                "relative_energy_error_percent": 0.08367041765222938,
                "rms_normalized_rmse_percent": 4.390615385443643,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002255383995361626,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.001948810531757772,
                  "rgb_channel": 0,
                  "sky_patch_index": 260
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010084360837936401,
                  "p50": 0.0,
                  "p90": 1.0133000614587218e-05,
                  "p95": 2.5310684577561915e-05,
                  "p99": 0.00017761992057785392
                },
                "candidate_energy": 4.271189388093706,
                "cvrmse_percent": 62.06777158793096,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4107979045685135,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.253715215123666,
                "relative_energy_error_percent": 0.41079790456851356,
                "rms_normalized_rmse_percent": 2.709946582942354,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05571237578988075,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.05470393970608711,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.58233406208456,
            "full": 3085.8273749472573
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.67112500220537,
            "full": 3024.668083060533
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.35395799856633,
            "full": 3082.2917089099064
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.14470798149705,
            "full": 3114.662625011988
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003579724580049515,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.2852251529693604e-07,
                  "p99": 0.00011538740363903344
                },
                "candidate_energy": 6.858605181555049,
                "cvrmse_percent": 25.296004925709997,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.031781106285516635,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.85642613347818,
                "relative_energy_error_percent": 0.031781106285516635,
                "rms_normalized_rmse_percent": 4.438956918257079,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015002040308900177,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.0018581764888949692,
                  "rgb_channel": 0,
                  "sky_patch_index": 145
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006558485329151154,
                  "p50": 0.0,
                  "p90": 1.0256325367663521e-05,
                  "p95": 2.495965236448683e-05,
                  "p99": 0.0001789947273209691
                },
                "candidate_energy": 4.271554938485156,
                "cvrmse_percent": 62.12715417529656,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2535045727419238,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.260753732938884,
                "relative_energy_error_percent": 0.2535045727419238,
                "rms_normalized_rmse_percent": 2.7155546258382235,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.040074534714221954,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.03941868618130684,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.2108750101179,
            "full": 3274.2517499718815
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.0256669120863,
            "full": 3287.8180419793352
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.6863750340417,
            "full": 3315.046916017309
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.66341697983444,
            "full": 3271.3391670258716
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
            "identifier": "plan_j_large_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001859864278230816,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.9962317310273647e-07,
                  "p99": 6.93413894623518e-05
                },
                "candidate_energy": 6.858137077920219,
                "cvrmse_percent": 14.871663186589545,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.001938042478097661,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.858269994105967,
                "relative_energy_error_percent": 0.001938042478097661,
                "rms_normalized_rmse_percent": 2.6130176175538,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00099966159905307,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0011856480268761516,
                  "rgb_channel": 0,
                  "sky_patch_index": 94
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000523129478096962,
                  "p50": 0.0,
                  "p90": 6.953338015591726e-06,
                  "p95": 1.6239588148891926e-05,
                  "p99": 0.00010409310925751925
                },
                "candidate_energy": 4.266652290941263,
                "cvrmse_percent": 38.08311853731437,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05345412952085218,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.264372807577448,
                "relative_energy_error_percent": 0.05345412952085218,
                "rms_normalized_rmse_percent": 1.662986666480235,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0455571748316288,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.04608030430972576,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.5351669723168,
            "full": 5693.311000009999
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 235.61220907140523,
            "full": 5758.176125003956
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 235.9179169870913,
            "full": 5810.048833955079
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 240.57545908726752,
            "full": 5810.624707955867
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/plan_j_large_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4634.224582929164,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_large_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18848.58029196039,
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
        "identifier": "plan_j_large_center_grid",
        "full_identifier": "plan_j_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.017541142336482365,
            "cvrmse_percent": 2.3901349285550224,
            "rms_normalized_rmse_percent": 0.4200726737071973,
            "reference_energy": 6.859882634452731,
            "candidate_energy": 6.858679332675706,
            "relative_energy_error_percent": 0.017541142336482365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.259629011154175e-09,
              "p99": 4.765985067933798e-06,
              "maximum": 7.128785364329815e-05
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888944372535,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9275819385405434,
            "cvrmse_percent": 40.17340965805401,
            "rms_normalized_rmse_percent": 1.7542544351645786,
            "reference_energy": 4.263833462817219,
            "candidate_energy": 4.224282913726679,
            "relative_energy_error_percent": 0.9275819385405435,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.999995498333192e-09,
              "p90": 7.993363396963105e-06,
              "p95": 1.4466648281086236e-05,
              "p99": 4.212663043290377e-05,
              "maximum": 0.000934995710849762
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03614387661218643,
              "candidate": 0.03520888090133667,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3663690309173513,
            "cvrmse_percent": 15.351213270985147,
            "rms_normalized_rmse_percent": 1.7488246157595453,
            "reference_energy": 11.12371609726995,
            "candidate_energy": 11.082962246402385,
            "relative_energy_error_percent": 0.36636903091735135,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.999993721976352e-09,
              "p90": 7.986040145624429e-06,
              "p95": 1.4459481462836266e-05,
              "p99": 4.052720032632351e-05,
              "maximum": 0.000934995710849762
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03614387661218643,
              "candidate": 0.03520888090133667,
              "position": [
                2.5,
                2.5,
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
        "identifier": "plan_j_large_center_grid",
        "full_identifier": "plan_j_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.017541142336482365,
            "cvrmse_percent": 2.3901349285550224,
            "rms_normalized_rmse_percent": 0.4200726737071973,
            "reference_energy": 6.859882634452731,
            "candidate_energy": 6.858679332675706,
            "relative_energy_error_percent": 0.017541142336482365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.259629011154175e-09,
              "p99": 4.765985067933798e-06,
              "maximum": 7.128785364329815e-05
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888944372535,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 85.18114103379398,
            "cvrmse_percent": 1020.6427907373613,
            "rms_normalized_rmse_percent": 30.396420422118503,
            "reference_energy": 2.2811625903934694,
            "candidate_energy": 4.224282913726679,
            "relative_energy_error_percent": 85.18114103379399,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.2269999287091196e-05,
              "p95": 8.141934085870162e-05,
              "p99": 0.000147351180203259,
              "maximum": 0.011145658791065216
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0499878004193306,
              "candidate": 0.06113345921039581,
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
            "nmbe_percent": 21.24392751364883,
            "cvrmse_percent": 254.6969795180712,
            "rms_normalized_rmse_percent": 30.39569526951037,
            "reference_energy": 9.1410452248462,
            "candidate_energy": 11.082962246402385,
            "relative_energy_error_percent": 21.24392751364883,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.207000140217133e-05,
              "p95": 8.163000165950507e-05,
              "p99": 0.00014639017172157764,
              "maximum": 0.011145658791065216
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0499878004193306,
              "candidate": 0.06113345921039581,
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
      "bias_percent": 0.1607198154256996,
      "rms_normalized_error_percent": 0.1587407086268144,
      "absolute_error": {
        "p95": 0.07936599996151798,
        "p99": 0.09450888749181728,
        "maximum": 0.10052323667282792
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.3980863329449,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1587407086268144
    },
    "overcast": {
      "bias_percent": 0.11183099551829825,
      "rms_normalized_error_percent": 0.12118856802806544,
      "absolute_error": {
        "p95": 0.04200344085693359,
        "p99": 0.057561225891113274,
        "maximum": 0.0635528564453125
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.883207321166992,
      "reference_fraction_of_uniform": 0.6619686484336853,
      "rms_normalized_to_uniform_percent": 0.08644701428374063
    },
    "horizon": {
      "bias_percent": 1.0240150091445306,
      "rms_normalized_error_percent": 1.5980686434056988,
      "absolute_error": {
        "p95": 0.04061617565002844,
        "p99": 0.06408268242459642,
        "maximum": 0.07706721667832106
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0570331499202423,
      "reference_fraction_of_uniform": 0.10165650832992018,
      "rms_normalized_to_uniform_percent": 0.09761232429968705
    },
    "north": {
      "bias_percent": -87.2526360208529,
      "rms_normalized_error_percent": 98.6619416141097,
      "absolute_error": {
        "p95": 3.324230647194769e-05,
        "p99": 0.00012505332331329543,
        "maximum": 0.00018310105338059657
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.320054232375696e-06,
      "reference_fraction_of_uniform": 8.963239679360413e-07,
      "rms_normalized_to_uniform_percent": 0.00013106244616932155
    },
    "east": {
      "bias_percent": 0.13849157692431677,
      "rms_normalized_error_percent": 0.20087444153870135,
      "absolute_error": {
        "p95": 0.02046988010406492,
        "p99": 0.024862132072448726,
        "maximum": 0.026586294174194336
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1344759464263916,
      "reference_fraction_of_uniform": 0.20527583360671997,
      "rms_normalized_to_uniform_percent": 0.04166108147779226
    },
    "south": {
      "bias_percent": 0.21487380098384942,
      "rms_normalized_error_percent": 0.20936838024614873,
      "absolute_error": {
        "p95": 0.07029170989990226,
        "p99": 0.0839826202392578,
        "maximum": 0.089599609375
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.784331798553467,
      "reference_fraction_of_uniform": 0.6524596214294434,
      "rms_normalized_to_uniform_percent": 0.13369112735448524
    },
    "west": {
      "bias_percent": 0.0808035138816423,
      "rms_normalized_error_percent": 0.14556947827617883,
      "absolute_error": {
        "p95": 0.012913924455642697,
        "p99": 0.015568771362304685,
        "maximum": 0.016633033752441406
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.077091932296753,
      "reference_fraction_of_uniform": 0.19975712895393372,
      "rms_normalized_to_uniform_percent": 0.02996481435896838
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
          "nmbe_percent": 0.08291757620173433,
          "cvrmse_percent": 1.7679694236351389,
          "absolute_error_percentiles_lux": {
            "p50": 1.119720458984375,
            "p90": 18.429492187500014,
            "p95": 30.85792541503905,
            "p99": 72.82112548828127
          },
          "maximum_absolute_error_lux": 323.359375,
          "worst": {
            "sensor_index": 17,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2723.5,
            "foton_lux": 36100.98046875,
            "radiance_lux": 35777.62109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24938793354707067,
            "maximum_error_percentage_points": 1.4527397260273993,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.14408695988421,
            "maximum_error_percentage_points": 0.8171197440526079,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.24382978723404305,
            "maximum_error_percentage_points": 3.5042465753424636,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2625182162634804,
            "maximum_error_percentage_points": 3.5042465753424654,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.024628388225007097,
            "maximum_error_percentage_points": 0.2773972602739718,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 29.78723404255319,
          "radiance_percent": 29.78723404255319,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
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
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_large_center_grid",
            "maximum_error_percentage_points": 0.004781142979449982,
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
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_large_center_grid",
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
      "study_preparation_seconds": 0.007148791919462383,
      "weather_seconds": 0.08527487493120134,
      "metric_reduction_seconds": 0.13869008305482566,
      "write_seconds": 0.020542333950288594,
      "total_seconds": 0.24472287495154887,
      "cold_end_to_end_seconds": 0.25187166687101126,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002046499983407557,
      "engine_upload_seconds": 0.000800375,
      "engine_acceleration_structure_seconds": 0.003477125,
      "engine_tracing_seconds": 0.0671416250988841,
      "engine_annual_reduction_seconds": 0.0022452500415965915,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0671416250988841
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007148791919462383,
      "weather_seconds": 0.08585829206276685,
      "metric_reduction_seconds": 0.05512737494427711,
      "write_seconds": 0.020711624994874,
      "total_seconds": 0.16223050002008677,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.16223050002008677,
      "raw_export_seconds": 0.002372541930526495,
      "engine_upload_seconds": 6.4541e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0028566665714606643,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02033866592682898,
      "full": 0.07526379101909697
    }
  },
  "elapsed_seconds": 1.5091899579856545,
  "result_class": "passed"
}
```
