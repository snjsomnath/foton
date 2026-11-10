# Foton report

Status: **passed**

```json
{
  "scene": "north_facing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "north_facing",
    "category": "orientation",
    "question": "Is north-facing glazing assigned to the correct sky patches?",
    "interactions": [
      "north_glazing",
      "sky_patch_order"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "300bcec36c12e4f5b2106a3cfadaa240e0f801069bcfc5bdd7ff1659c422d424",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 14256008842406293211,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 14256008842406293211,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "47bd4795b27a6f765c348cc514fdc9dae9a65a2038f7b7d331c93dea01582927",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00011883559636771679,
          "p95": 3.9814040064811707e-08,
          "p99": 8.134287782013416e-06
        },
        "bias_percent": -0.00293816625518776,
        "identifier": "north_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7961676481493521,
        "worst_index": [
          7,
          341,
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
          "maximum": 0.0004164651036262512,
          "p95": 2.178705472033471e-05,
          "p99": 0.00010424037463963032
        },
        "bias_percent": 0.14549270394408903,
        "identifier": "north_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7896845276684235,
        "worst_index": [
          28,
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
          "maximum": 0.00031381845474243164,
          "p95": 1.7702113837003708e-05,
          "p99": 8.096947567537427e-05
        },
        "bias_percent": -0.07702445262211395,
        "identifier": "north_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3767388127096603,
        "worst_index": [
          8,
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
            "identifier": "north_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004601335385814309,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.005104372277856e-05,
                  "p99": 0.00017181795556098223
                },
                "candidate_energy": 6.016824611309858,
                "cvrmse_percent": 30.62616726061128,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.10636087627751119,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.023230972552483,
                "relative_energy_error_percent": 0.10636087627751119,
                "rms_normalized_rmse_percent": 5.88523848484225,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034005824709311128,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.002940448932349682,
                  "rgb_channel": 0,
                  "sky_patch_index": 243
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008608493953943253,
                  "p50": 0.0,
                  "p90": 5.694351057172774e-06,
                  "p95": 4.8146441258722916e-05,
                  "p99": 0.00032417511101812124
                },
                "candidate_energy": 1.9991020665104458,
                "cvrmse_percent": 183.45831241821492,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.18436521771053654,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0027945229930566,
                "relative_energy_error_percent": 0.18436521771053654,
                "rms_normalized_rmse_percent": 6.82147661983958,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.012467830441892147,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.013328679837286472,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.90670896880329,
            "full": 228.64587500225753
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.39570798352361,
            "full": 223.26687502209097
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.17491696495563,
            "full": 229.2379999998957
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.20741697959602,
            "full": 229.36487500555813
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
            "identifier": "north_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003400474088266492,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.251823025289923e-05,
                  "p99": 0.00012443948071449995
                },
                "candidate_energy": 6.01382262995503,
                "cvrmse_percent": 23.841672004797402,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.022214019984753634,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.015158838541538,
                "relative_energy_error_percent": 0.022214019984753634,
                "rms_normalized_rmse_percent": 4.596150701599548,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003574322909116745,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.003234275500290096,
                  "rgb_channel": 0,
                  "sky_patch_index": 244
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007091499865055084,
                  "p50": 1.5908311112866613e-08,
                  "p90": 1.2988911657885198e-05,
                  "p95": 3.5207562177674845e-05,
                  "p99": 0.00018319325317861512
                },
                "candidate_energy": 3.7425940580420125,
                "cvrmse_percent": 57.82121410121238,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06338193110411394,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7402234322030736,
                "relative_energy_error_percent": 0.06338193110411394,
                "rms_normalized_rmse_percent": 3.1093370483224634,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.031125550158321857,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.03041640017181635,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.8813330391422,
            "full": 2336.727499961853
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.6844169665128,
            "full": 2271.723874961026
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.0094170132652,
            "full": 2252.3401669459417
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.23037508782,
            "full": 2313.4904579492286
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
            "identifier": "north_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002933239156845957,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2406602511182427e-05,
                  "p99": 0.00013135946937836707
                },
                "candidate_energy": 6.010984616178575,
                "cvrmse_percent": 24.13337016014879,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0014264189068853158,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0110703592226855,
                "relative_energy_error_percent": 0.0014264189068853156,
                "rms_normalized_rmse_percent": 4.6531209938940306,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001058240479324013,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.0007649165636394173,
                  "rgb_channel": 0,
                  "sky_patch_index": 115
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006272643804550171,
                  "p50": 1.840286145693426e-08,
                  "p90": 1.3367284873311304e-05,
                  "p95": 3.818122422671877e-05,
                  "p99": 0.00020483866683207452
                },
                "candidate_energy": 3.7559060837452023,
                "cvrmse_percent": 62.0509526603968,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.16798777789328512,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7622261638772194,
                "relative_energy_error_percent": 0.16798777789328515,
                "rms_normalized_rmse_percent": 3.352210070272665,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01995444018393755,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.020581704564392567,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.40691606048495,
            "full": 2432.56616697181
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.99679098278284,
            "full": 2447.249374934472
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.33404196240008,
            "full": 2448.918042005971
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.45399993564934,
            "full": 2508.2835420034826
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
            "identifier": "north_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019744416931644082,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.143224653787911e-05,
                  "p99": 7.326604099944234e-05
                },
                "candidate_energy": 6.0126056360463735,
                "cvrmse_percent": 14.247472886477354,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01847444407975389,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.013716636763547,
                "relative_energy_error_percent": 0.01847444407975389,
                "rms_normalized_rmse_percent": 2.748047065086024,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009763542911969125,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.0011737984605133533,
                  "rgb_channel": 0,
                  "sky_patch_index": 64
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007028756663203239,
                  "p50": 3.059064823673907e-08,
                  "p90": 9.321926336269877e-06,
                  "p95": 2.2115229512564838e-05,
                  "p99": 0.00011637748684734106
                },
                "candidate_energy": 3.749643922216368,
                "cvrmse_percent": 36.69948377860597,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0126323901064803,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7491703123967497,
                "relative_energy_error_percent": 0.0126323901064803,
                "rms_normalized_rmse_percent": 1.9779127931049378,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020834540016949177,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.020131664350628853,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.21304204966873,
            "full": 4274.284875020385
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.31012492068112,
            "full": 4196.375666069798
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.58112500514835,
            "full": 4288.217957946472
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.79437499307096,
            "full": 4315.005165990442
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan-0.3.7/north_facing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2794.5827919756994,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/north_facing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10726.13254096359,
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
      36,
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
        "identifier": "north_facing_grid",
        "full_identifier": "north_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0036619505404567555,
            "cvrmse_percent": 2.358048588994407,
            "rms_normalized_rmse_percent": 0.45487516154501373,
            "reference_energy": 6.016047347356562,
            "candidate_energy": 6.016267652034912,
            "relative_energy_error_percent": 0.0036619505404567555,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.5133991837501526e-08,
              "p99": 5.79573679715395e-06,
              "maximum": 9.540119208395481e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.002735236892476678,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.9175654930067367,
            "cvrmse_percent": 25.212317490239148,
            "rms_normalized_rmse_percent": 1.3579874698561962,
            "reference_energy": 3.746520908135208,
            "candidate_energy": 3.7808976911765395,
            "relative_energy_error_percent": 0.9175654930067367,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.983345080399904e-06,
              "p95": 1.627097481105011e-05,
              "p99": 4.5215943828225136e-05,
              "maximum": 0.0007017944008111954
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017801204696297646,
              "candidate": 0.01850299909710884,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.35438510455709166,
            "cvrmse_percent": 9.65340140896811,
            "rms_normalized_rmse_percent": 1.3548751689768435,
            "reference_energy": 9.76256825549177,
            "candidate_energy": 9.797165343211452,
            "relative_energy_error_percent": 0.3543851045570917,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.929664338415032e-06,
              "p95": 1.6262227291008458e-05,
              "p99": 4.458148032426834e-05,
              "maximum": 0.0007017944008111954
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017801204696297646,
              "candidate": 0.01850299909710884,
              "position": [
                2.5,
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
      36,
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
        "identifier": "north_facing_grid",
        "full_identifier": "north_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0036619505404567555,
            "cvrmse_percent": 2.358048588994407,
            "rms_normalized_rmse_percent": 0.45487516154501373,
            "reference_energy": 6.016047347356562,
            "candidate_energy": 6.016267652034912,
            "relative_energy_error_percent": 0.0036619505404567555,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.5133991837501526e-08,
              "p99": 5.79573679715395e-06,
              "maximum": 9.540119208395481e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.002735236892476678,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.58015535380225,
            "cvrmse_percent": 976.1867745059294,
            "rms_normalized_rmse_percent": 36.40393398963263,
            "reference_energy": 2.004928718020757,
            "candidate_energy": 3.7808976911765395,
            "relative_energy_error_percent": 88.58015535380225,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.665236549248222e-05,
              "p95": 7.906999962870032e-05,
              "p99": 0.00016813725233078003,
              "maximum": 0.008247453719377518
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010854905471205711,
              "candidate": 0.01910235919058323,
              "position": [
                0.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.144303428370574,
            "cvrmse_percent": 244.00880377524638,
            "rms_normalized_rmse_percent": 36.404006092439836,
            "reference_energy": 8.020976065377319,
            "candidate_energy": 9.797165343211452,
            "relative_energy_error_percent": 22.144303428370577,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.647508405672855e-05,
              "p95": 7.929000275908038e-05,
              "p99": 0.00016772677190601826,
              "maximum": 0.008247453719377518
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010854905471205711,
              "candidate": 0.01910235919058323,
              "position": [
                0.5,
                5.5,
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
      "bias_percent": 0.20460221960136168,
      "rms_normalized_error_percent": 0.16077833420568569,
      "absolute_error": {
        "p95": 0.060480173150065264,
        "p99": 0.08464248533561036,
        "maximum": 0.09685048101282989
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.026191687396684,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.16077833420568569
    },
    "overcast": {
      "bias_percent": 0.1810873592431385,
      "rms_normalized_error_percent": 0.12468462015411848,
      "absolute_error": {
        "p95": 0.03785383701324463,
        "p99": 0.04139286279678345,
        "maximum": 0.0422060489654541
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.648181438446045,
      "reference_fraction_of_uniform": 0.6359604001045227,
      "rms_normalized_to_uniform_percent": 0.08827827586670736
    },
    "horizon": {
      "bias_percent": 0.9043954256337476,
      "rms_normalized_error_percent": 1.7982199680433777,
      "absolute_error": {
        "p95": 0.053022535695183504,
        "p99": 0.06908097595438484,
        "maximum": 0.0703084752074501
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4228524892337926,
      "reference_fraction_of_uniform": 0.11831280643272353,
      "rms_normalized_to_uniform_percent": 0.12495285265859732
    },
    "north": {
      "bias_percent": 0.21306179416720133,
      "rms_normalized_error_percent": 0.20061486486776436,
      "absolute_error": {
        "p95": 0.05354660749435425,
        "p99": 0.08192481994628902,
        "maximum": 0.09340071678161621
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.389086723327637,
      "reference_fraction_of_uniform": 0.6975679993629456,
      "rms_normalized_to_uniform_percent": 0.13135535558717557
    },
    "east": {
      "bias_percent": 0.20806410475776374,
      "rms_normalized_error_percent": 0.21977717656331253,
      "absolute_error": {
        "p95": 0.020358800888061523,
        "p99": 0.027447593212127686,
        "maximum": 0.027660131454467773
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.319053888320923,
      "reference_fraction_of_uniform": 0.19283360242843628,
      "rms_normalized_to_uniform_percent": 0.044721372142006846
    },
    "south": {
      "bias_percent": -82.7615419666493,
      "rms_normalized_error_percent": 100.2446799418986,
      "absolute_error": {
        "p95": 4.93213328809361e-05,
        "p99": 0.0001979569749892104,
        "maximum": 0.00027389166643843055
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3581420716946013e-05,
      "reference_fraction_of_uniform": 1.1293201396256336e-06,
      "rms_normalized_to_uniform_percent": 0.00022259022167441282
    },
    "west": {
      "bias_percent": 0.20932361160350604,
      "rms_normalized_error_percent": 0.24343925346543452,
      "absolute_error": {
        "p95": 0.02151419222354889,
        "p99": 0.028343570232391355,
        "maximum": 0.028781414031982422
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.328385353088379,
      "reference_fraction_of_uniform": 0.19360953569412231,
      "rms_normalized_to_uniform_percent": 0.049639096565179015
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
        "identifier": "north_facing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.318332005230442,
          "cvrmse_percent": 1.149734906644845,
          "absolute_error_percentiles_lux": {
            "p50": 0.6321029663085938,
            "p90": 3.1111648559570315,
            "p95": 4.50833358764648,
            "p99": 11.435509643554658
          },
          "maximum_absolute_error_lux": 79.513916015625,
          "worst": {
            "sensor_index": 1,
            "position": [
              0.5,
              4.5,
              0.75
            ],
            "hour_of_year": 4133.5,
            "foton_lux": 3296.78125,
            "radiance_lux": 3376.295166015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.14677701674276983,
            "maximum_error_percentage_points": 1.066438356164383,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.21926927852771674,
            "maximum_error_percentage_points": 0.8980115228372867,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.17292998477929972,
            "maximum_error_percentage_points": 0.9613698630136938,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1735350076103492,
            "maximum_error_percentage_points": 0.9613698630136938,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0007952815829528163,
            "maximum_error_percentage_points": 0.028219178082191793,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 19.444444444444443,
          "radiance_percent": 22.22222222222222,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.0049052868150738504,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.0008219178082191914,
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
      "study_preparation_seconds": 0.36882612799990966,
      "weather_seconds": 0.24335413399990102,
      "metric_reduction_seconds": 0.3030694060000769,
      "write_seconds": 0.012167030999989947,
      "total_seconds": 0.5589096709998103,
      "cold_end_to_end_seconds": 0.9277357989997199,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001549955999962549,
      "engine_upload_seconds": 0.063005236,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.040450047,
      "engine_annual_reduction_seconds": 0.008410898,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.040450047
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.36882612799990966,
      "weather_seconds": 0.24564158800012592,
      "metric_reduction_seconds": 0.2822731679998469,
      "write_seconds": 0.012292758000057802,
      "total_seconds": 0.5404577670001345,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5404577670001345,
      "raw_export_seconds": 0.0015348300000823656,
      "engine_upload_seconds": 0.064813359,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 9.7e-08,
      "engine_annual_reduction_seconds": 0.008364948,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.026650735999965036,
      "full": 0.06136261300002843
    }
  },
  "elapsed_seconds": 4.1776203430001715,
  "result_class": "passed"
}
```
