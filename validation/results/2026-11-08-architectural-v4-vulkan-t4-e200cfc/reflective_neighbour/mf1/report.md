# Foton report

Status: **passed**

```json
{
  "scene": "reflective_neighbour",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "reflective_neighbour",
    "category": "context",
    "question": "Does a bright neighbouring facade contribute reflected daylight?",
    "interactions": [
      "external_obstruction",
      "context_reflection",
      "high_reflectance"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "7edc4ec81c88f69ea8e6cd143c17ad8d4702344372890e99c2588fe0ae48143d",
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 13318971096555845098,
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 13318971096555845098,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.5)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "c28e68ac087cdcbfca1e5b7520b6801497c79a4525ce6ced31e3734484e7ecba",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00035545602440834045,
          "p95": 0.0,
          "p99": 1.7517711967229843e-05
        },
        "bias_percent": -0.4575824892542755,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7263588325986352,
        "worst_index": [
          17,
          116,
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
          "maximum": 0.00114411860704422,
          "p95": 0.00010034487640950825,
          "p99": 0.00022249016910791397
        },
        "bias_percent": 0.15172143580808392,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8772833444374668,
        "worst_index": [
          16,
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
          "maximum": 0.0006111450493335724,
          "p95": 8.764769736444559e-05,
          "p99": 0.00019966624677181244
        },
        "bias_percent": 0.21788714936996953,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5602002731782638,
        "worst_index": [
          16,
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005235129501670599,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.649874997790903e-05
                },
                "candidate_energy": 0.8503917375064702,
                "cvrmse_percent": 26.14384141021806,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.3928099142022502,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8470643846239909,
                "relative_energy_error_percent": 0.3928099142022502,
                "rms_normalized_rmse_percent": 2.039596333910212,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007319218944758177,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.006795705994591117,
                  "rgb_channel": 0,
                  "sky_patch_index": 101
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014154352247714996,
                  "p50": 0.0,
                  "p90": 0.00010008030767494347,
                  "p95": 0.0001568748228237381,
                  "p99": 0.00034243299160152674
                },
                "candidate_energy": 3.460499087373165,
                "cvrmse_percent": 37.62885410578748,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6216312502396295,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4821451900532523,
                "relative_energy_error_percent": 0.6216312502396295,
                "rms_normalized_rmse_percent": 3.8983280276138723,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.041303372010588646,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.039887936785817146,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.41754102613777,
            "full": 234.14466599933803
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.86129200924188,
            "full": 234.88529201131314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.97245797887444,
            "full": 226.07974999118596
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.73795802239329,
            "full": 238.3997499709949
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.90787501819432,
            "full": 243.4875420294702
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.43379208259284,
            "full": 230.0044170115143
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.09841600246727,
            "full": 228.63133309874684
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.01554198749363,
            "full": 229.64570799376816
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022721034474670887,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.196846228092909e-05
                },
                "candidate_energy": 0.8481764016632951,
                "cvrmse_percent": 19.250675877538736,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0556842546386696,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8477043638067698,
                "relative_energy_error_percent": 0.0556842546386696,
                "rms_normalized_rmse_percent": 1.5012228655438968,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005034081870689988,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.004806871525943279,
                  "rgb_channel": 0,
                  "sky_patch_index": 68
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.004010144621133804,
                  "p50": 1.3150549875717843e-05,
                  "p90": 9.699679503683001e-05,
                  "p95": 0.00015592140262015163,
                  "p99": 0.0003435190883465111
                },
                "candidate_energy": 5.975043248314382,
                "cvrmse_percent": 26.070661115553218,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2475912032262512,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.960286104233184,
                "relative_energy_error_percent": 0.2475912032262512,
                "rms_normalized_rmse_percent": 3.2437971830785917,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.10203460231423378,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.10604474693536758,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.6680829776451,
            "full": 2377.6964579010382
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.89087502844632,
            "full": 2368.234333000146
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.5992910163477,
            "full": 2333.645625039935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.78524998854846,
            "full": 2300.264082965441
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020593544468283653,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.4464912712574005e-05
                },
                "candidate_energy": 0.8471048467472428,
                "cvrmse_percent": 17.562423757595997,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06507546283931406,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8465539478474966,
                "relative_energy_error_percent": 0.06507546283931406,
                "rms_normalized_rmse_percent": 1.3688762510725763,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013905375264585018,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.013699439819902182,
                  "rgb_channel": 0,
                  "sky_patch_index": 132
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001685289666056633,
                  "p50": 1.2806927770725451e-05,
                  "p90": 9.509841038379818e-05,
                  "p95": 0.00015220445711747706,
                  "p99": 0.00031608552671968937
                },
                "candidate_energy": 5.975034396240865,
                "cvrmse_percent": 21.70009316385047,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.13644961392927843,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.983198447422996,
                "relative_energy_error_percent": 0.13644961392927843,
                "rms_normalized_rmse_percent": 2.701780033157404,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.060185929760336876,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.05850064009428024,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.12604203727096,
            "full": 2529.556875000708
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.2628749385476,
            "full": 2457.998500089161
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.41950001288205,
            "full": 2550.2007919130847
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.95012502931058,
            "full": 2471.4788750279695
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001411852426826954,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.185895573347807e-05
                },
                "candidate_energy": 0.8494111707004777,
                "cvrmse_percent": 10.977335341338524,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06713376102292327,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8488413116028823,
                "relative_energy_error_percent": 0.06713376102292329,
                "rms_normalized_rmse_percent": 0.8568191227891402,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006628596922382712,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.006487411679700017,
                  "rgb_channel": 0,
                  "sky_patch_index": 120
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013807397335767746,
                  "p50": 9.254348242393462e-06,
                  "p90": 6.607749674003571e-05,
                  "p95": 0.00010415844153612845,
                  "p99": 0.00023925199639052153
                },
                "candidate_energy": 5.9902003189962265,
                "cvrmse_percent": 17.200769073415334,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04979300263192923,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.993184505514794,
                "relative_energy_error_percent": 0.04979300263192922,
                "rms_normalized_rmse_percent": 2.143130311858579,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03869299031794071,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.04007373005151749,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.73579194303602,
            "full": 4383.830291917548
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.8699580449611,
            "full": 4410.111166071147
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.27516698930413,
            "full": 4330.594166996889
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.79900001734495,
            "full": 4330.890916986391
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
    "/content/suite-vulkan/reflective_neighbour/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 809.7839170368388,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2742.0617080060765,
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
        "identifier": "reflective_neighbour_grid",
        "full_identifier": "reflective_neighbour_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04624710441052017,
            "cvrmse_percent": 13.77053660142539,
            "rms_normalized_rmse_percent": 1.0744564373700007,
            "reference_energy": 0.849546850695333,
            "candidate_energy": 0.8499397415143903,
            "relative_energy_error_percent": 0.04624710441052017,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1757860193029046e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.816802923302274,
            "cvrmse_percent": 17.98981474991517,
            "rms_normalized_rmse_percent": 2.241937353049969,
            "reference_energy": 5.991271826742352,
            "candidate_energy": 5.942334943318535,
            "relative_energy_error_percent": 0.8168029233022739,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4271107829699758e-05,
              "p90": 7.093799649737775e-05,
              "p95": 0.0001039419352309778,
              "p99": 0.00022339040879160166,
              "maximum": 0.0018024295568466187
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10460879653692245,
              "candidate": 0.10280636698007584,
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
            "nmbe_percent": -0.7096225597217917,
            "cvrmse_percent": 15.728907179984889,
            "rms_normalized_rmse_percent": 2.2381252465031727,
            "reference_energy": 6.840818677437685,
            "candidate_energy": 6.792274684832925,
            "relative_energy_error_percent": 0.7096225597217918,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4236990864446852e-05,
              "p90": 7.114582695066929e-05,
              "p95": 0.00010377421422163017,
              "p99": 0.00022334419190883636,
              "maximum": 0.0018024295568466187
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10460879653692245,
              "candidate": 0.10280636698007584,
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
        "identifier": "reflective_neighbour_grid",
        "full_identifier": "reflective_neighbour_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04624710441052017,
            "cvrmse_percent": 13.77053660142539,
            "rms_normalized_rmse_percent": 1.0744564373700007,
            "reference_energy": 0.849546850695333,
            "candidate_energy": 0.8499397415143903,
            "relative_energy_error_percent": 0.04624710441052017,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1757860193029046e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 71.22400946242576,
            "cvrmse_percent": 475.5269260237055,
            "rms_normalized_rmse_percent": 49.174801642826814,
            "reference_energy": 3.4705033260084655,
            "candidate_energy": 5.942334943318535,
            "relative_energy_error_percent": 71.22400946242576,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.02500006405171e-05,
              "p90": 0.00019509356934577227,
              "p95": 0.0002493655701982789,
              "p99": 0.0004777089925482869,
              "maximum": 0.023067235946655273
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07973913103342056,
              "candidate": 0.10280636698007584,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 57.22675448217679,
            "cvrmse_percent": 382.0203740124897,
            "rms_normalized_rmse_percent": 49.17567785502881,
            "reference_energy": 4.320050176703798,
            "candidate_energy": 6.792274684832925,
            "relative_energy_error_percent": 57.22675448217679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.022670393373119e-05,
              "p90": 0.0001949311699718237,
              "p95": 0.00024905421014409485,
              "p99": 0.0005030045285820961,
              "maximum": 0.023067235946655273
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07973913103342056,
              "candidate": 0.10280636698007584,
              "position": [
                2.5,
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
      "bias_percent": -0.16473361195687578,
      "rms_normalized_error_percent": 0.5480641550566402,
      "absolute_error": {
        "p95": 0.0934960745113137,
        "p99": 0.2088029287305034,
        "maximum": 0.2679379024136068
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.333447630434318,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5480641550566402
    },
    "overcast": {
      "bias_percent": -0.16973062810794276,
      "rms_normalized_error_percent": 0.47326714508759404,
      "absolute_error": {
        "p95": 0.07020223140716553,
        "p99": 0.1217012643814086,
        "maximum": 0.14429473876953125
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.438845157623291,
      "reference_fraction_of_uniform": 0.7008576393127441,
      "rms_normalized_to_uniform_percent": 0.3451858195196823
    },
    "horizon": {
      "bias_percent": -0.8465151566564257,
      "rms_normalized_error_percent": 2.6602912362548468,
      "absolute_error": {
        "p95": 0.06056626335232124,
        "p99": 0.08411052191995395,
        "maximum": 0.0952502469017662
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7288064542888804,
      "reference_fraction_of_uniform": 0.11507262660335636,
      "rms_normalized_to_uniform_percent": 0.2689658824536536
    },
    "north": {
      "bias_percent": -0.16864352834656954,
      "rms_normalized_error_percent": 0.9056454794471578,
      "absolute_error": {
        "p95": 0.06782802939414978,
        "p99": 0.12120623588562005,
        "maximum": 0.13692188262939453
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6968586444854736,
      "reference_fraction_of_uniform": 0.42581212520599365,
      "rms_normalized_to_uniform_percent": 0.34376931986467707
    },
    "east": {
      "bias_percent": -0.3731590952248274,
      "rms_normalized_error_percent": 1.4723101378326322,
      "absolute_error": {
        "p95": 0.08761268854141235,
        "p99": 0.11359891891479489,
        "maximum": 0.12213516235351562
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4763299226760864,
      "reference_fraction_of_uniform": 0.2331005185842514,
      "rms_normalized_to_uniform_percent": 0.33171232342476875
    },
    "south": {
      "bias_percent": 0.0917302198115791,
      "rms_normalized_error_percent": 0.7944271292285963,
      "absolute_error": {
        "p95": 0.015795528888702393,
        "p99": 0.05247237682342522,
        "maximum": 0.07190322875976562
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6466735005378723,
      "reference_fraction_of_uniform": 0.10210449993610382,
      "rms_normalized_to_uniform_percent": 0.12271713088825581
    },
    "west": {
      "bias_percent": -0.11661852006638118,
      "rms_normalized_error_percent": 1.058558407420564,
      "absolute_error": {
        "p95": 0.04611825942993164,
        "p99": 0.07899432182312008,
        "maximum": 0.08838939666748047
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4165092706680298,
      "reference_fraction_of_uniform": 0.2236553281545639,
      "rms_normalized_to_uniform_percent": 0.22607915160600825
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
        "identifier": "reflective_neighbour_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.22529571777165278,
          "cvrmse_percent": 4.835867306080299,
          "absolute_error_percentiles_lux": {
            "p50": 1.9564170837402344,
            "p90": 16.73287963867188,
            "p95": 25.94764823913574,
            "p99": 54.027911682128824
          },
          "maximum_absolute_error_lux": 230.4267578125,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4452.5,
            "foton_lux": 8952.111328125,
            "radiance_lux": 8721.6845703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.37376331811263375,
            "maximum_error_percentage_points": 1.6465753424657539,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.41660715242438545,
            "maximum_error_percentage_points": 1.2940135001210855,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5130745814307465,
            "maximum_error_percentage_points": 2.552739726027397,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5184703196347031,
            "maximum_error_percentage_points": 2.552739726027397,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006811263318112619,
            "maximum_error_percentage_points": 0.08465753424657407,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.88888888888889,
          "radiance_percent": 13.88888888888889,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
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
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004597602739728757,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.00424657534246542,
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
      "study_preparation_seconds": 0.37810685900012686,
      "weather_seconds": 0.2451691410001331,
      "metric_reduction_seconds": 0.08943455200005701,
      "write_seconds": 0.01288624200014965,
      "total_seconds": 0.3478306599999996,
      "cold_end_to_end_seconds": 0.7259375190001265,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016010929998628853,
      "engine_upload_seconds": 0.023147844,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010090851,
      "engine_annual_reduction_seconds": 0.006635641,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010090851
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37810685900012686,
      "weather_seconds": 0.2609060899999349,
      "metric_reduction_seconds": 0.08083445700003722,
      "write_seconds": 0.013092436000079033,
      "total_seconds": 0.3550980649997655,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3550980649997655,
      "raw_export_seconds": 0.0015714549999756855,
      "engine_upload_seconds": 0.024322735,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.2e-08,
      "engine_annual_reduction_seconds": 0.006488987,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.024088303000098676,
      "full": 0.03578253499972561
    }
  },
  "elapsed_seconds": 2.808796967000035,
  "result_class": "passed"
}
```
