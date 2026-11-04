# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 1.4399999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "abe428d0b7550dbc1f2bd4e2f77378503230030852f9ad0f67b96c2709aea90a",
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
      "scene_fingerprint": 10502512291607635887,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 10502512291607635887,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
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
    "model_sha256": "090621f52b868c79cb64c8103e2b1dff5aaf91689b84c136b129c52a4f6ec8f1",
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
          "maximum": 0.00036203162744641304,
          "p95": 0.0,
          "p99": 2.140237484127283e-05
        },
        "bias_percent": 0.05783225529673018,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1779573612941556,
        "worst_index": [
          11,
          119,
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
          "maximum": 0.0002727014943957329,
          "p95": 1.2265285477042198e-05,
          "p99": 6.749358726665378e-05
        },
        "bias_percent": 0.11710502690687388,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3157480214513104,
        "worst_index": [
          29,
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
          "maximum": 0.0003253091126680374,
          "p95": 1.0664487490430474e-05,
          "p99": 6.0390448197722435e-05
        },
        "bias_percent": -0.056162547372310814,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2314862427162394,
        "worst_index": [
          11,
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005164799513295293,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010188252599618863
                },
                "candidate_energy": 1.4654770705506053,
                "cvrmse_percent": 38.05315138084582,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.44577869468926695,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4720391072683014,
                "relative_energy_error_percent": 0.445778694689267,
                "rms_normalized_rmse_percent": 3.5101496954558558,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008455280330963433,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0013620079844258726,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014973962679505348,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.2822899760940345e-06,
                  "p99": 0.0001733407552819699
                },
                "candidate_energy": 0.698694012198132,
                "cvrmse_percent": 134.8145276906586,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9153467474222505,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6923565490458756,
                "relative_energy_error_percent": 0.9153467474222506,
                "rms_normalized_rmse_percent": 4.7367772444570955,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.022750229574739933,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.024247625842690468,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.90837508346885,
            "full": 274.2108330130577
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.5236250013113,
            "full": 274.23199999611825
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.22100000083447,
            "full": 266.50725002400577
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.5238750372082,
            "full": 269.549542106688
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.42433298565447,
            "full": 279.30362499319017
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.29787502717227,
            "full": 266.9879160821438
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.61174996010959,
            "full": 271.97616593912244
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.86937495041639,
            "full": 271.3284590281546
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022729532793164253,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.732946399599314e-05
                },
                "candidate_energy": 1.4699364590096593,
                "cvrmse_percent": 18.470001397449597,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07750495997951364,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4687980676551433,
                "relative_energy_error_percent": 0.07750495997951364,
                "rms_normalized_rmse_percent": 1.7021643709797167,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013355790171772242,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.013128494843840599,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004633339121937752,
                  "p50": 6.125946327983911e-08,
                  "p90": 9.546052751829848e-06,
                  "p95": 1.7988144463743083e-05,
                  "p99": 0.00010724485036917031
                },
                "candidate_energy": 1.4059960761837011,
                "cvrmse_percent": 36.1750845017874,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.373837531454622,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4112719403676834,
                "relative_energy_error_percent": 0.373837531454622,
                "rms_normalized_rmse_percent": 2.2502324347953473,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.022724300622940063,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.02318763453513384,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.1219170857221,
            "full": 2988.6645830702037
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.6088749524206,
            "full": 3047.269457951188
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.020250024274,
            "full": 3046.727167093195
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.39029097836465,
            "full": 3079.733708058484
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003260248340666294,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.201444193720818e-05
                },
                "candidate_energy": 1.4715519672747632,
                "cvrmse_percent": 19.575064392550942,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.30596935900561884,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4670632033951279,
                "relative_energy_error_percent": 0.3059693590056189,
                "rms_normalized_rmse_percent": 1.804256837354958,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015252329874783754,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.014926305040717125,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005751382559537888,
                  "p50": 5.000000058430487e-08,
                  "p90": 9.224840323440732e-06,
                  "p95": 1.7975729861063883e-05,
                  "p99": 0.00012044503091601655
                },
                "candidate_energy": 1.4092086953758987,
                "cvrmse_percent": 37.18985057474501,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4035973771145621,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4149192724477864,
                "relative_energy_error_percent": 0.40359737711456223,
                "rms_normalized_rmse_percent": 2.316160928379006,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.009104572236537933,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.009679710492491722,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.3978750659153,
            "full": 3344.231209019199
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.04516699910164,
            "full": 3218.430499895476
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.84937508031726,
            "full": 3215.32316703815
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.89033292699605,
            "full": 3246.5773329604417
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019835494458675385,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.52489878423512e-05
                },
                "candidate_energy": 1.469785764897665,
                "cvrmse_percent": 11.172308237334754,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.11919446227533821,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4680359473442195,
                "relative_energy_error_percent": 0.1191944622753382,
                "rms_normalized_rmse_percent": 1.0278638182451472,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007497068494558334,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.007695423439145088,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003096270374953747,
                  "p50": 5.3490120777155425e-08,
                  "p90": 6.684387653876917e-06,
                  "p95": 1.1885859748872463e-05,
                  "p99": 6.690842565149069e-05
                },
                "candidate_energy": 1.4113612438466419,
                "cvrmse_percent": 22.446673479048602,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07356863174894368,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4103236880061445,
                "relative_energy_error_percent": 0.07356863174894367,
                "rms_normalized_rmse_percent": 1.3978957714320437,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.009271457325667143,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.009581084363162518,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 218.23729202151299,
            "full": 5643.411415978335
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.8852080097422,
            "full": 5768.495834083296
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.7841249704361,
            "full": 5737.46829200536
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.9877919368446,
            "full": 5721.509707975201
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
    "/content/suite-vulkan-0.3.3/plan_l_offset_low/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1250.2929160837084,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4865.509583964013,
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
        "identifier": "plan_l_offset_low_grid",
        "full_identifier": "plan_l_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.004717026958393744,
            "cvrmse_percent": 5.404590687084255,
            "rms_normalized_rmse_percent": 0.49832008579454434,
            "reference_energy": 1.4707211123336492,
            "candidate_energy": 1.4706517380222976,
            "relative_energy_error_percent": 0.004717026958393745,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0928342817351222e-05,
              "maximum": 0.0001364145427942276
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313623558729887,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.297003699204032,
            "cvrmse_percent": 48.373793808818256,
            "rms_normalized_rmse_percent": 3.0090584391195754,
            "reference_energy": 1.4090322108001025,
            "candidate_energy": 1.3766666887950478,
            "relative_energy_error_percent": 2.297003699204032,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1633952112788393e-07,
              "p90": 1.5297431457383946e-05,
              "p95": 2.5372719392180443e-05,
              "p99": 6.569200195372105e-05,
              "maximum": 0.0012904778122901917
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023201268166303635,
              "candidate": 0.021910790354013443,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.1263081478489478,
            "cvrmse_percent": 23.692085420816,
            "rms_normalized_rmse_percent": 3.012021931568583,
            "reference_energy": 2.8797533231337518,
            "candidate_energy": 2.8473184268173455,
            "relative_energy_error_percent": 1.1263081478489476,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1555819767750108e-07,
              "p90": 1.5374936083389932e-05,
              "p95": 2.5385386834386736e-05,
              "p99": 6.311236938927323e-05,
              "maximum": 0.0012904778122901917
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023201268166303635,
              "candidate": 0.021910790354013443,
              "position": [
                0.5,
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
        "identifier": "plan_l_offset_low_grid",
        "full_identifier": "plan_l_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.004717026958393744,
            "cvrmse_percent": 5.404590687084255,
            "rms_normalized_rmse_percent": 0.49832008579454434,
            "reference_energy": 1.4707211123336492,
            "candidate_energy": 1.4706517380222976,
            "relative_energy_error_percent": 0.004717026958393745,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0928342817351222e-05,
              "maximum": 0.0001364145427942276
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313623558729887,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 98.49215988204917,
            "cvrmse_percent": 627.2870014621271,
            "rms_normalized_rmse_percent": 22.14245162531031,
            "reference_energy": 0.6935622493166029,
            "candidate_energy": 1.3766666887950478,
            "relative_energy_error_percent": 98.49215988204915,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.436243525058674e-05,
              "p95": 0.00010840445247595198,
              "p99": 0.00025317890685983,
              "maximum": 0.004655021242797375
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011263118125498295,
              "candidate": 0.01591813936829567,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 31.559410254223067,
            "cvrmse_percent": 201.01284423154857,
            "rms_normalized_rmse_percent": 22.141747777171616,
            "reference_energy": 2.164283361650252,
            "candidate_energy": 2.8473184268173455,
            "relative_energy_error_percent": 31.559410254223064,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.396948019755657e-05,
              "p95": 0.00010910789205809124,
              "p99": 0.0002481081464793533,
              "maximum": 0.004655021242797375
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011263118125498295,
              "candidate": 0.01591813936829567,
              "position": [
                1.5,
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
      "bias_percent": -0.11242121151020626,
      "rms_normalized_error_percent": 0.2775775324233189,
      "absolute_error": {
        "p95": 0.03803572709226406,
        "p99": 0.05310071236101572,
        "maximum": 0.054332205309457926
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.339921395909417,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2775775324233189
    },
    "overcast": {
      "bias_percent": -0.09130114186812724,
      "rms_normalized_error_percent": 0.2676946074060879,
      "absolute_error": {
        "p95": 0.02356492280960083,
        "p99": 0.03261930465698243,
        "maximum": 0.03455519676208496
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4174809455871582,
      "reference_fraction_of_uniform": 0.6057814359664917,
      "rms_normalized_to_uniform_percent": 0.1729167442559146
    },
    "horizon": {
      "bias_percent": 0.2473659212064857,
      "rms_normalized_error_percent": 1.9589778289118003,
      "absolute_error": {
        "p95": 0.020165922829005763,
        "p99": 0.022907150612567706,
        "maximum": 0.02482532154423492
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3016355336418407,
      "reference_fraction_of_uniform": 0.1289084044315126,
      "rms_normalized_to_uniform_percent": 0.12915129505650116
    },
    "north": {
      "bias_percent": -96.66761107613478,
      "rms_normalized_error_percent": 99.92199693796914,
      "absolute_error": {
        "p95": 6.452225375142001e-05,
        "p99": 0.0001491162062302466,
        "maximum": 0.000206092037842609
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2827909813495353e-05,
      "reference_fraction_of_uniform": 5.482196684170049e-06,
      "rms_normalized_to_uniform_percent": 0.00045777747401641746
    },
    "east": {
      "bias_percent": -0.8557833487897804,
      "rms_normalized_error_percent": 0.4210197988613797,
      "absolute_error": {
        "p95": 0.01479133367538452,
        "p99": 0.021057941317558296,
        "maximum": 0.02406024932861328
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3701833486557007,
      "reference_fraction_of_uniform": 0.15820331871509552,
      "rms_normalized_to_uniform_percent": 0.09443207151011827
    },
    "south": {
      "bias_percent": -0.09974457030851179,
      "rms_normalized_error_percent": 0.3004070168396219,
      "absolute_error": {
        "p95": 0.03134602606296538,
        "p99": 0.04503812253475191,
        "maximum": 0.050694942474365234
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7384823560714722,
      "reference_fraction_of_uniform": 0.7429661154747009,
      "rms_normalized_to_uniform_percent": 0.21965508285363422
    },
    "west": {
      "bias_percent": 0.22963479152435573,
      "rms_normalized_error_percent": 0.43811942148197125,
      "absolute_error": {
        "p95": 0.014402139559388159,
        "p99": 0.019258116781711587,
        "maximum": 0.022510409355163574
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.537034809589386,
      "reference_fraction_of_uniform": 0.22950975596904755,
      "rms_normalized_to_uniform_percent": 0.0998861853519471
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
        "identifier": "plan_l_offset_low_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": -0.2011442588468228,
          "cvrmse_percent": 4.365714109445588,
          "absolute_error_percentiles_lux": {
            "p50": 1.0325889587402344,
            "p90": 10.802428054809582,
            "p95": 16.76121826171875,
            "p99": 36.73604591369625
          },
          "maximum_absolute_error_lux": 241.0830078125,
          "worst": {
            "sensor_index": 23,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 14704.5576171875,
            "radiance_lux": 14945.640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.14530821917808207,
            "maximum_error_percentage_points": 2.385616438356166,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4910880913765894,
            "maximum_error_percentage_points": 1.701729244118873,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7123230593607305,
            "maximum_error_percentage_points": 4.24506849315069,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7121033105022834,
            "maximum_error_percentage_points": 4.245068493150683,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0047345890410959044,
            "maximum_error_percentage_points": 0.1083561643835651,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 8.333333333333334,
          "radiance_percent": 8.333333333333334,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004930570419521274,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
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
      "study_preparation_seconds": 0.35909901900004115,
      "weather_seconds": 0.2285211949999848,
      "metric_reduction_seconds": 0.1961340249999921,
      "write_seconds": 0.012466121999977986,
      "total_seconds": 0.43747703300005014,
      "cold_end_to_end_seconds": 0.7965760520000913,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001850570999977208,
      "engine_upload_seconds": 0.014128307,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.014656092,
      "engine_annual_reduction_seconds": 0.010384209,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014656092
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35909901900004115,
      "weather_seconds": 0.23082199100008438,
      "metric_reduction_seconds": 0.175421692999862,
      "write_seconds": 0.012272273999997196,
      "total_seconds": 0.4187744359999215,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4187744359999215,
      "raw_export_seconds": 0.0017347539999263972,
      "engine_upload_seconds": 0.01409803,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.3e-07,
      "engine_annual_reduction_seconds": 0.010380834,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013720221000085076,
      "full": 0.023700854000026084
    }
  },
  "elapsed_seconds": 2.899360307999814,
  "result_class": "passed"
}
```
