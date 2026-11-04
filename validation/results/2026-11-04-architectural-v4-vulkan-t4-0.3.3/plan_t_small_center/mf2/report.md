# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "d4f5e2203bb548cdd296fdb6031715b87bdd5fa1247d78d04da8a911a06d9ab6",
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
      "scene_fingerprint": 7077756305093146598,
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
      "scene_fingerprint": 7077756305093146598,
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
    "model_sha256": "36f62ce5f70cb040065dba1add956594cc902554565f4c4a0b72ef16f23bc13c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00011640600860118866,
          "p95": 0.0,
          "p99": 1.4668330550193787e-07
        },
        "bias_percent": 0.01536334086782372,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6647713909536093,
        "worst_index": [
          26,
          515,
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
          "maximum": 0.0002567352494224906,
          "p95": 4.187522790743969e-06,
          "p99": 3.2659416319802403e-05
        },
        "bias_percent": 0.09452291136439021,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1102788686885967,
        "worst_index": [
          23,
          149,
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
          "maximum": 0.0003164634108543396,
          "p95": 3.698739419633057e-06,
          "p99": 2.8168782591819763e-05
        },
        "bias_percent": 0.03128628408562928,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8190232636081423,
        "worst_index": [
          37,
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004896800965070724,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.693958908319473e-05
                },
                "candidate_energy": 2.4207465186500485,
                "cvrmse_percent": 61.95200924856491,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.16818768196520878,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4166819572856184,
                "relative_energy_error_percent": 0.1681876819652088,
                "rms_normalized_rmse_percent": 5.842965980918963,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004166576080024242,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.00367689598351717,
                  "rgb_channel": 0,
                  "sky_patch_index": 361
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008434336632490158,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.2896634871140122e-09,
                  "p99": 9.407621837453917e-05
                },
                "candidate_energy": 0.5760239923722068,
                "cvrmse_percent": 431.17159973246345,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.9381127779830327,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5814789204260009,
                "relative_energy_error_percent": 0.9381127779830328,
                "rms_normalized_rmse_percent": 7.330635301401549,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.010627180337905884,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.009783746674656868,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.2599160131067,
            "full": 283.7870829971507
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.31158303841949,
            "full": 292.05120797269046
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.6833330122754,
            "full": 295.86225003004074
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.00541697628796,
            "full": 288.3856249973178
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00033936393447220325,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.0842394810169935e-05
                },
                "candidate_energy": 2.4261890407651663,
                "cvrmse_percent": 44.23010730565351,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.16063522362654253,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4222979769929225,
                "relative_energy_error_percent": 0.16063522362654253,
                "rms_normalized_rmse_percent": 4.182937460123923,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003946737386286259,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0036073734518140554,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007440652698278427,
                  "p50": 0.0,
                  "p90": 2.4079615172922786e-06,
                  "p95": 6.1080829141246795e-06,
                  "p99": 6.498175207525492e-05
                },
                "candidate_energy": 1.0923655946117279,
                "cvrmse_percent": 154.08674790082702,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.29434911062768443,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0891596628308697,
                "relative_energy_error_percent": 0.2943491106276844,
                "rms_normalized_rmse_percent": 4.004726029756013,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015838580206036568,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.015094514936208725,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.87387497443706,
            "full": 3850.994750042446
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.29275000840425,
            "full": 3910.920292022638
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.02962493803352,
            "full": 3849.3307920871302
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.86429196223617,
            "full": 3795.4523330554366
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003791060298681259,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.5027933083474636e-05
                },
                "candidate_energy": 2.4243243004584656,
                "cvrmse_percent": 45.383490149519716,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.022466986688969806,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4237797501846217,
                "relative_energy_error_percent": 0.022466986688969803,
                "rms_normalized_rmse_percent": 4.292870014000615,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003476783982478082,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.003855890012346208,
                  "rgb_channel": 0,
                  "sky_patch_index": 310
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006791353225708008,
                  "p50": 0.0,
                  "p90": 2.454368996041012e-06,
                  "p95": 6.047200486136717e-06,
                  "p99": 6.662961095571518e-05
                },
                "candidate_energy": 1.0904473662759067,
                "cvrmse_percent": 150.559597930297,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6974234818692745,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0981058140790658,
                "relative_energy_error_percent": 0.6974234818692745,
                "rms_normalized_rmse_percent": 3.932258907186228,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024198110215365887,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.024877245537936687,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.47704198677093,
            "full": 4127.775790984742
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.0297079803422,
            "full": 4107.282582903281
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.24604099523276,
            "full": 4200.620874995366
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.752333980985,
            "full": 4115.455791004933
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00014921050751581788,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3125088773667812e-05
                },
                "candidate_energy": 2.4251014418086925,
                "cvrmse_percent": 24.344602984345837,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.009513127399338234,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4248707607639517,
                "relative_energy_error_percent": 0.009513127399338236,
                "rms_normalized_rmse_percent": 2.3038692606678457,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018511179951019585,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0017019074875861406,
                  "rgb_channel": 0,
                  "sky_patch_index": 264
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004752008244395256,
                  "p50": 0.0,
                  "p90": 1.749374860082753e-06,
                  "p95": 4.225994871376315e-06,
                  "p99": 3.8543890696018934e-05
                },
                "candidate_energy": 1.0952859891824218,
                "cvrmse_percent": 88.16601963646242,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15411678108902066,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0936005671902969,
                "relative_energy_error_percent": 0.15411678108902066,
                "rms_normalized_rmse_percent": 2.2980725886575857,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024666905403137207,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.02419170457869768,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.66375000216067,
            "full": 7189.721749979071
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.9032499799505,
            "full": 7319.413582910784
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 280.3215829189867,
            "full": 9031.676625018008
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 254.62962500751019,
            "full": 7630.597791983746
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
    "/content/suite-vulkan-0.3.3/plan_t_small_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 7007.7541670762,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 28585.599625017494,
      "invocation_count": 4,
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
      54,
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
        "identifier": "plan_t_small_center_grid",
        "full_identifier": "plan_t_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03147695264606752,
            "cvrmse_percent": 3.864812025076739,
            "rms_normalized_rmse_percent": 0.3658673406155301,
            "reference_energy": 2.4251935840825354,
            "candidate_energy": 2.4244302070464983,
            "relative_energy_error_percent": 0.031476952646067514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.725275069475174e-07,
              "maximum": 7.083220407366753e-05
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0015869324561208487,
              "candidate": 0.0015161002520471811,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3565535401892725,
            "cvrmse_percent": 87.47245967497123,
            "rms_normalized_rmse_percent": 2.2795074694578212,
            "reference_energy": 1.0942357890739984,
            "candidate_energy": 1.079391894739297,
            "relative_energy_error_percent": 1.3565535401892725,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.2646645447821356e-06,
              "p95": 5.054287612438202e-06,
              "p99": 2.1485378965735435e-05,
              "maximum": 0.0006719175726175308
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021091967821121216,
              "candidate": 0.020420050248503685,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4434602805153184,
            "cvrmse_percent": 27.178211631488253,
            "rms_normalized_rmse_percent": 2.277990434697556,
            "reference_energy": 3.519429373156534,
            "candidate_energy": 3.5038221017857953,
            "relative_energy_error_percent": 0.44346028051531833,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.2643362171947956e-06,
              "p95": 5.066802259534597e-06,
              "p99": 2.161890733987093e-05,
              "maximum": 0.0006719175726175308
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021091967821121216,
              "candidate": 0.020420050248503685,
              "position": [
                5.5,
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
      54,
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
        "identifier": "plan_t_small_center_grid",
        "full_identifier": "plan_t_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03147695264606752,
            "cvrmse_percent": 3.864812025076739,
            "rms_normalized_rmse_percent": 0.3658673406155301,
            "reference_energy": 2.4251935840825354,
            "candidate_energy": 2.4244302070464983,
            "relative_energy_error_percent": 0.031476952646067514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.725275069475174e-07,
              "maximum": 7.083220407366753e-05
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0015869324561208487,
              "candidate": 0.0015161002520471811,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.61515200644713,
            "cvrmse_percent": 1697.281173587766,
            "rms_normalized_rmse_percent": 28.326725398728744,
            "reference_energy": 0.5722721018205377,
            "candidate_energy": 1.079391894739297,
            "relative_energy_error_percent": 88.61515200644715,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.159999768191483e-06,
              "p95": 2.1449585801747162e-05,
              "p99": 6.790999759687111e-05,
              "maximum": 0.006656765937805176
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0173629242926836,
              "candidate": 0.024019690230488777,
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
            "nmbe_percent": 16.89281776482348,
            "cvrmse_percent": 324.0248937717001,
            "rms_normalized_rmse_percent": 28.32517494532515,
            "reference_energy": 2.997465685903073,
            "candidate_energy": 3.5038221017857953,
            "relative_energy_error_percent": 16.89281776482348,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.170000117184827e-06,
              "p95": 2.1440000637085177e-05,
              "p99": 6.591474812012166e-05,
              "maximum": 0.006656765937805176
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0173629242926836,
              "candidate": 0.024019690230488777,
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
      "bias_percent": 0.010556173064779233,
      "rms_normalized_error_percent": 0.10792888352036571,
      "absolute_error": {
        "p95": 0.02615218305122954,
        "p99": 0.03460835952848689,
        "maximum": 0.03528541487358616
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0752029972149213,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.10792888352036571
    },
    "overcast": {
      "bias_percent": -0.003994683994223595,
      "rms_normalized_error_percent": 0.070725915297003,
      "absolute_error": {
        "p95": 0.011257995292544353,
        "p99": 0.01579167306423187,
        "maximum": 0.01688385009765625
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.069119691848755,
      "reference_fraction_of_uniform": 0.6728400588035583,
      "rms_normalized_to_uniform_percent": 0.051652476682082116
    },
    "horizon": {
      "bias_percent": 0.5706589377149953,
      "rms_normalized_error_percent": 2.0411123929067867,
      "absolute_error": {
        "p95": 0.02162883377060524,
        "p99": 0.030081353190177247,
        "maximum": 0.03305764168354697
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.25350209983948574,
      "reference_fraction_of_uniform": 0.08243426533762865,
      "rms_normalized_to_uniform_percent": 0.08725486106753845
    },
    "north": {
      "bias_percent": -86.92076046713943,
      "rms_normalized_error_percent": 101.83391668610467,
      "absolute_error": {
        "p95": 4.5799842882843105e-05,
        "p99": 8.992046059574932e-05,
        "maximum": 8.992046059574932e-05
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 7.75864737079246e-06,
      "reference_fraction_of_uniform": 2.5229708171536913e-06,
      "rms_normalized_to_uniform_percent": 0.00021440057200761595
    },
    "east": {
      "bias_percent": -0.11998887466590358,
      "rms_normalized_error_percent": 0.24418532147625235,
      "absolute_error": {
        "p95": 0.011653473228216154,
        "p99": 0.020084931850433335,
        "maximum": 0.026412248611450195
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4456706941127777,
      "reference_fraction_of_uniform": 0.14492399990558624,
      "rms_normalized_to_uniform_percent": 0.051685604264096525
    },
    "south": {
      "bias_percent": 0.04504859986123029,
      "rms_normalized_error_percent": 0.1433860829031218,
      "absolute_error": {
        "p95": 0.01854009628295893,
        "p99": 0.032260093986988064,
        "maximum": 0.03387877345085144
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1923375129699707,
      "reference_fraction_of_uniform": 0.7129082679748535,
      "rms_normalized_to_uniform_percent": 0.09295442646855888
    },
    "west": {
      "bias_percent": -0.1041235345596827,
      "rms_normalized_error_percent": 0.19757975123929253,
      "absolute_error": {
        "p95": 0.007275124639272669,
        "p99": 0.016929390132427204,
        "maximum": 0.022049903869628906
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.45316943526268005,
      "reference_fraction_of_uniform": 0.14736245572566986,
      "rms_normalized_to_uniform_percent": 0.042109760629548486
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
        "identifier": "plan_t_small_center_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.06892616416542317,
          "cvrmse_percent": 3.173159556507872,
          "absolute_error_percentiles_lux": {
            "p50": 0.31659311056137085,
            "p90": 5.533769798278809,
            "p95": 11.283951950073241,
            "p99": 35.76699584960931
          },
          "maximum_absolute_error_lux": 351.5,
          "worst": {
            "sensor_index": 38,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 38515.56640625,
            "radiance_lux": 38867.06640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06299594114662606,
            "maximum_error_percentage_points": 0.8505479452054789,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.16968084225398258,
            "maximum_error_percentage_points": 0.9606894666745092,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2046347031963464,
            "maximum_error_percentage_points": 2.3582191780821873,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2084297311009639,
            "maximum_error_percentage_points": 2.3582191780821873,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004406392694064085,
            "maximum_error_percentage_points": 0.08054794520547937,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
      "maximum_error_percentage_points": 0.004955987799654338,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004955987799654338,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_small_center_grid",
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
      "study_preparation_seconds": 0.37621776800006046,
      "weather_seconds": 0.24920473700012735,
      "metric_reduction_seconds": 1.4164142029999311,
      "write_seconds": 0.01215219599998818,
      "total_seconds": 1.6781076170000233,
      "cold_end_to_end_seconds": 2.0543253850000838,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0017920140001024265,
      "engine_upload_seconds": 0.044285727,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.058417833,
      "engine_annual_reduction_seconds": 0.062197563,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.058417833
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37621776800006046,
      "weather_seconds": 0.24940352299995538,
      "metric_reduction_seconds": 1.3492430769999828,
      "write_seconds": 0.012424282999973002,
      "total_seconds": 1.6113522540001668,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.6113522540001668,
      "raw_export_seconds": 0.0017748010000104841,
      "engine_upload_seconds": 0.044587421,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.16e-07,
      "engine_annual_reduction_seconds": 0.064156544,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019809718000033172,
      "full": 0.07545741900003122
    }
  },
  "elapsed_seconds": 6.852122280999993,
  "result_class": "passed"
}
```
