# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 1.44
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "de3ccc17f15335ce20380a807ee0c3a1d96a60f402c402915ac605a31aeba304",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 17665444809337020543,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 17665444809337020543,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "60803980e0f8e458f78b83f4f3232332613481acd700f9d549da1598c8351ed0",
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
          "maximum": 0.00011780229397118092,
          "p95": 0.0,
          "p99": 2.310443960595876e-06
        },
        "bias_percent": 0.015670172917802982,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8198716784963621,
        "worst_index": [
          40,
          363,
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
          "maximum": 0.0003224797546863556,
          "p95": 5.9670010159607045e-06,
          "p99": 4.1404273360967636e-05
        },
        "bias_percent": 0.10938455106435833,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.2454115275794724,
        "worst_index": [
          38,
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
          "maximum": 0.00029938947409391403,
          "p95": 5.145295290276408e-06,
          "p99": 3.489098162390292e-05
        },
        "bias_percent": 0.04223248181996284,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9451261509878826,
        "worst_index": [
          41,
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004280300345271826,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.716057446785271e-05
                },
                "candidate_energy": 2.5849021028907373,
                "cvrmse_percent": 49.18784817172346,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.12752181468188215,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5882026258468613,
                "relative_energy_error_percent": 0.12752181468188212,
                "rms_normalized_rmse_percent": 5.28929273655365,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029237830312922597,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0033518130658194423,
                  "rgb_channel": 0,
                  "sky_patch_index": 306
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006128349341452122,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.361974662169814e-08,
                  "p99": 0.00010639353422448039
                },
                "candidate_energy": 0.6344843941787701,
                "cvrmse_percent": 325.5023285506844,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8007347072250396,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6294442158796016,
                "relative_energy_error_percent": 0.8007347072250396,
                "rms_normalized_rmse_percent": 6.5533250878377425,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.013366879895329475,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.013979714829474688,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.50458396133035,
            "full": 261.8277089204639
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.51983301900327,
            "full": 305.9501249808818
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.77829189691693,
            "full": 284.22983398195356
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.1008339934051,
            "full": 277.39341696724296
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004393179842736572,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.362050771713257e-05
                },
                "candidate_energy": 2.5903870562406155,
                "cvrmse_percent": 44.903194369011175,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04599066567654032,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.589196267641455,
                "relative_energy_error_percent": 0.04599066567654032,
                "rms_normalized_rmse_percent": 4.822562759380957,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010638065286912024,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.0006244885444175452,
                  "rgb_channel": 0,
                  "sky_patch_index": 154
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006413096562027931,
                  "p50": 0.0,
                  "p90": 4.202665763841651e-06,
                  "p95": 8.443739716312848e-06,
                  "p99": 9.177450556308031e-05
                },
                "candidate_energy": 1.2612343097473442,
                "cvrmse_percent": 134.72742115590165,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0882262301142867,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2623480318267468,
                "relative_energy_error_percent": 0.08822623011428671,
                "rms_normalized_rmse_percent": 4.524520641714476,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01755176018923521,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.018193069845438004,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.11458288691938,
            "full": 3131.989249959588
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.54970896989107,
            "full": 3090.149166993797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.39749995898455,
            "full": 3056.618833099492
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.48862506169826,
            "full": 3071.8624170403928
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032905349507927895,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.814198473468423e-05
                },
                "candidate_energy": 2.5881640016223173,
                "cvrmse_percent": 40.97742443263873,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0980020715578105,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5907029441755185,
                "relative_energy_error_percent": 0.09800207155781052,
                "rms_normalized_rmse_percent": 4.405189774535936,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017540199914947152,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.0014249664964154363,
                  "rgb_channel": 0,
                  "sky_patch_index": 144
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005232398398220539,
                  "p50": 0.0,
                  "p90": 4.337619685657046e-06,
                  "p95": 8.537837857147679e-06,
                  "p99": 7.84433213993907e-05
                },
                "candidate_energy": 1.268258373580828,
                "cvrmse_percent": 124.40981117360626,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.29988223371382816,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2644664633061033,
                "relative_energy_error_percent": 0.29988223371382816,
                "rms_normalized_rmse_percent": 4.192078448401791,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.012878465000540018,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.012355225160717964,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.89145804289728,
            "full": 3263.39033304248
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.8693750826642,
            "full": 3265.9068750217557
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.23004199936986,
            "full": 3314.206250011921
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.3838750300929,
            "full": 3250.697792042047
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00015969399828463793,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.0021066777408123e-05
                },
                "candidate_energy": 2.5912541057348335,
                "cvrmse_percent": 22.270415722675704,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.113371166422202,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5883196975030387,
                "relative_energy_error_percent": 0.11337116642220199,
                "rms_normalized_rmse_percent": 2.3939984212819594,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002358153462409973,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.002198459464125335,
                  "rgb_channel": 0,
                  "sky_patch_index": 207
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002864670241251588,
                  "p50": 0.0,
                  "p90": 3.0753208193345927e-06,
                  "p95": 6.15445060248021e-06,
                  "p99": 4.949083086103201e-05
                },
                "candidate_energy": 1.267957475401687,
                "cvrmse_percent": 70.97528113719035,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05051641466259735,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2673172721533952,
                "relative_energy_error_percent": 0.05051641466259734,
                "rms_normalized_rmse_percent": 2.3934594818802637,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00014996645040810108,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.0001365005737170577,
                  "rgb_channel": 0,
                  "sky_patch_index": 207
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 254.82141703832895,
            "full": 5816.542292013764
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 246.46166595630348,
            "full": 5924.375292030163
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 239.08870806917548,
            "full": 5894.556166022085
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 257.96120800077915,
            "full": 5855.791749898344
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
    "/content/suite-vulkan-0.3.3/plan_l_small_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4584.55766690895,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18851.8225409789,
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
        "identifier": "plan_l_small_center_grid",
        "full_identifier": "plan_l_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02049869028050196,
            "cvrmse_percent": 4.026728578744333,
            "rms_normalized_rmse_percent": 0.43326039246875225,
            "reference_energy": 2.590175622776769,
            "candidate_energy": 2.589644670698135,
            "relative_energy_error_percent": 0.02049869028050196,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.73368607647717e-06,
              "maximum": 5.773361772298813e-05
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 363,
              "rgb_channel": 0,
              "reference": 0.001065222080796957,
              "candidate": 0.0011229556985199451,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.7759823342704261,
            "cvrmse_percent": 51.25212389014868,
            "rms_normalized_rmse_percent": 1.7281382837692298,
            "reference_energy": 1.2672486583582803,
            "candidate_energy": 1.257415032638141,
            "relative_energy_error_percent": 0.775982334270426,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.895353529514978e-06,
              "p95": 6.985646905377507e-06,
              "p99": 2.1428888430818915e-05,
              "maximum": 0.0003812299109995365
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005881469696760178,
              "candidate": 0.005500239785760641,
              "position": [
                1.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2686916720429708,
            "cvrmse_percent": 16.821487847796334,
            "rms_normalized_rmse_percent": 1.726500068774939,
            "reference_energy": 3.8574242811350494,
            "candidate_energy": 3.847059703336276,
            "relative_energy_error_percent": 0.2686916720429708,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.897415808751248e-06,
              "p95": 6.971271432121284e-06,
              "p99": 2.1384636056609452e-05,
              "maximum": 0.0003812299109995365
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005881469696760178,
              "candidate": 0.005500239785760641,
              "position": [
                1.5,
                3.5,
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
        "identifier": "plan_l_small_center_grid",
        "full_identifier": "plan_l_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02049869028050196,
            "cvrmse_percent": 4.026728578744333,
            "rms_normalized_rmse_percent": 0.43326039246875225,
            "reference_energy": 2.590175622776769,
            "candidate_energy": 2.589644670698135,
            "relative_energy_error_percent": 0.02049869028050196,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.73368607647717e-06,
              "maximum": 5.773361772298813e-05
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 363,
              "rgb_channel": 0,
              "reference": 0.001065222080796957,
              "candidate": 0.0011229556985199451,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 100.11664702937453,
            "cvrmse_percent": 1404.9519162282102,
            "rms_normalized_rmse_percent": 28.237780389063083,
            "reference_energy": 0.628341045736974,
            "candidate_energy": 1.257415032638141,
            "relative_energy_error_percent": 100.11664702937452,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.591000000189524e-05,
              "p95": 2.8646886903516133e-05,
              "p99": 6.690045120194554e-05,
              "maximum": 0.004992092028260231
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015751777216792107,
              "candidate": 0.020743869245052338,
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
            "nmbe_percent": 19.528966277275284,
            "cvrmse_percent": 274.26765997949707,
            "rms_normalized_rmse_percent": 28.236055618230882,
            "reference_energy": 3.218516668513743,
            "candidate_energy": 3.847059703336276,
            "relative_energy_error_percent": 19.528966277275288,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.591000000189524e-05,
              "p95": 2.8720000045723282e-05,
              "p99": 6.702875180053525e-05,
              "maximum": 0.004992092028260231
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015751777216792107,
              "candidate": 0.020743869245052338,
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
      "bias_percent": 0.07393140859447395,
      "rms_normalized_error_percent": 0.14983638905869606,
      "absolute_error": {
        "p95": 0.04140033825317083,
        "p99": 0.05502556939974497,
        "maximum": 0.056147444125727475
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7228261590786276,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.14983638905869606
    },
    "overcast": {
      "bias_percent": 0.03343527814630616,
      "rms_normalized_error_percent": 0.1144453787275708,
      "absolute_error": {
        "p95": 0.025498199462890624,
        "p99": 0.027952580451965334,
        "maximum": 0.028855085372924805
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.487708330154419,
      "reference_fraction_of_uniform": 0.6682311296463013,
      "rms_normalized_to_uniform_percent": 0.08420579529341327
    },
    "horizon": {
      "bias_percent": 0.6835952283765305,
      "rms_normalized_error_percent": 2.298671443365865,
      "absolute_error": {
        "p95": 0.019380577229162685,
        "p99": 0.02695015316391092,
        "maximum": 0.031204664684054695
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.29185336168486264,
      "reference_fraction_of_uniform": 0.07839564599951512,
      "rms_normalized_to_uniform_percent": 0.08576101945260187
    },
    "north": {
      "bias_percent": -96.81048205961159,
      "rms_normalized_error_percent": 99.8864992634152,
      "absolute_error": {
        "p95": 0.00013351147099456272,
        "p99": 0.00030746802338399003,
        "maximum": 0.00036003466811962426
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.2459398678620346e-05,
      "reference_fraction_of_uniform": 6.032889359630644e-06,
      "rms_normalized_to_uniform_percent": 0.0006464924741724711
    },
    "east": {
      "bias_percent": 0.03808738072292371,
      "rms_normalized_error_percent": 0.1584589409931365,
      "absolute_error": {
        "p95": 0.0058612883090972895,
        "p99": 0.00849991112947464,
        "maximum": 0.008757263422012329
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8615507483482361,
      "reference_fraction_of_uniform": 0.23142383992671967,
      "rms_normalized_to_uniform_percent": 0.03286886716937822
    },
    "south": {
      "bias_percent": 0.10732054096061122,
      "rms_normalized_error_percent": 0.18653955863725719,
      "absolute_error": {
        "p95": 0.0337491989135742,
        "p99": 0.043397452831268314,
        "maximum": 0.045827627182006836
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.400636911392212,
      "reference_fraction_of_uniform": 0.6448425650596619,
      "rms_normalized_to_uniform_percent": 0.12077921438425511
    },
    "west": {
      "bias_percent": 0.10980203441240158,
      "rms_normalized_error_percent": 0.22021291690327532,
      "absolute_error": {
        "p95": 0.012709140777587887,
        "p99": 0.017715750932693487,
        "maximum": 0.020462989807128906
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7228870391845703,
      "reference_fraction_of_uniform": 0.19417694211006165,
      "rms_normalized_to_uniform_percent": 0.04580793973056128
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
        "identifier": "plan_l_small_center_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.04801161114291255,
          "cvrmse_percent": 2.821504022751943,
          "absolute_error_percentiles_lux": {
            "p50": 0.5163493156433105,
            "p90": 9.340168762207032,
            "p95": 16.286221313476528,
            "p99": 40.53212188720693
          },
          "maximum_absolute_error_lux": 243.3994140625,
          "worst": {
            "sensor_index": 36,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5842.5,
            "foton_lux": 15121.013671875,
            "radiance_lux": 14877.6142578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.18165239726027393,
            "maximum_error_percentage_points": 1.2890410958904113,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13001285650296437,
            "maximum_error_percentage_points": 0.49201730081202655,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3039697488584469,
            "maximum_error_percentage_points": 1.8946575342465763,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.30462043378995435,
            "maximum_error_percentage_points": 1.8946575342465763,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.008053652968036534,
            "maximum_error_percentage_points": 0.05972602739726085,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004735926797945211,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_small_center_grid",
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
      "study_preparation_seconds": 0.37677762299995265,
      "weather_seconds": 0.24622648500007926,
      "metric_reduction_seconds": 1.2764397569999346,
      "write_seconds": 0.01304618200015284,
      "total_seconds": 1.5360393460000523,
      "cold_end_to_end_seconds": 1.912816969000005,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0019349649999185203,
      "engine_upload_seconds": 0.044268858,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.050537418,
      "engine_annual_reduction_seconds": 0.053525768,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.050537418
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37677762299995265,
      "weather_seconds": 0.22945514599996386,
      "metric_reduction_seconds": 1.2712178869999207,
      "write_seconds": 0.01203332899990528,
      "total_seconds": 1.5130390419999458,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.5130390419999458,
      "raw_export_seconds": 0.0016415579998465546,
      "engine_upload_seconds": 0.045791251,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.35e-07,
      "engine_annual_reduction_seconds": 0.05503927,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01870760900010282,
      "full": 0.06293496100010998
    }
  },
  "elapsed_seconds": 6.464539125999863,
  "result_class": "passed"
}
```
