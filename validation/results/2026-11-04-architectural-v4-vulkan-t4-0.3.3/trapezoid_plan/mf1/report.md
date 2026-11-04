# Foton report

Status: **passed**

```json
{
  "scene": "trapezoid_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "trapezoid_plan",
    "category": "form",
    "question": "How do splayed walls change illumination and reflections?",
    "interactions": [
      "angled_walls",
      "nonorthogonal_plan"
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
    "sensors": 48,
    "floor_area": 56.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "b0d2d08a0940d371e669397f675dfe31ba2347340d40f44e9c6a7fc257f44469",
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
      "scene_fingerprint": 4702131747089679607,
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
      "scene_fingerprint": 4702131747089679607,
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
    "model_sha256": "f3443938a9d3da3c14d3728719ff84e383f4f808542b864281dd393cbfcf455c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "2ac629109977a30bc8fd8526a56056c521e654eb0c97d50fb92079cd8ec06be6",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0003254120238125324,
          "p95": 1.3345852494239807e-06,
          "p99": 7.093889871612191e-05
        },
        "bias_percent": -0.09752576435046319,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.098874659634699,
        "worst_index": [
          14,
          72,
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
          "maximum": 0.0003779549151659012,
          "p95": 3.5375182051211596e-05,
          "p99": 0.00012595579028129578
        },
        "bias_percent": 0.08122113759456774,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0737477629102248,
        "worst_index": [
          3,
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
          "maximum": 0.00047245249152183533,
          "p95": 2.8149690479040146e-05,
          "p99": 0.00010017957538366318
        },
        "bias_percent": 0.03291126890610798,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9323507324522995,
        "worst_index": [
          3,
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
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006288443692028522,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.5274849981069565e-05,
                  "p99": 0.00023231608793139458
                },
                "candidate_energy": 6.16158372181053,
                "cvrmse_percent": 14.008785875226325,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.004817943170071464,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.161880597715935,
                "relative_energy_error_percent": 0.004817943170071464,
                "rms_normalized_rmse_percent": 2.535474016173307,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015162774827331305,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.015791619196534157,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010825693607330322,
                  "p50": 0.0,
                  "p90": 1.07224902421877e-05,
                  "p95": 9.3493377789855e-05,
                  "p99": 0.00041507347486913204
                },
                "candidate_energy": 2.065265746057648,
                "cvrmse_percent": 82.20266179377614,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2314544688314203,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0604966345169373,
                "relative_energy_error_percent": 0.2314544688314203,
                "rms_normalized_rmse_percent": 3.992226372783119,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.012287859804928303,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.01120529044419527,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.80312506482005,
            "full": 278.08366692624986
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.3075000513345,
            "full": 268.7302919803187
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.17929197382182,
            "full": 267.50854204874486
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.02683298103511,
            "full": 262.5050829956308
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
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037882267497479916,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3512751795351505e-05,
                  "p99": 0.00016076897736638784
                },
                "candidate_energy": 6.171184412270122,
                "cvrmse_percent": 9.606463984056957,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.14807782767237954,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.162059768025756,
                "relative_energy_error_percent": 0.14807782767237954,
                "rms_normalized_rmse_percent": 1.7392530666748514,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004058759892359376,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.004437582567334175,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006561046466231346,
                  "p50": 1.920225258800201e-07,
                  "p90": 2.3610281641595133e-05,
                  "p95": 6.29714340902865e-05,
                  "p99": 0.00027002859860658646
                },
                "candidate_energy": 3.7410041735428656,
                "cvrmse_percent": 27.704799265010823,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1607819385609119,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7470287189556366,
                "relative_energy_error_percent": 0.1607819385609119,
                "rms_normalized_rmse_percent": 2.1532625846555495,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020649734884500504,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.01999363023787737,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.12466710526496,
            "full": 2970.9109999239445
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.36912505701184,
            "full": 2959.7391249844804
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.5198340686038,
            "full": 3008.6247499566525
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.34483403805643,
            "full": 3024.1794999456033
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
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004351455718278885,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.337941259611398e-05,
                  "p99": 0.00016262102872133255
                },
                "candidate_energy": 6.168181379199268,
                "cvrmse_percent": 9.97113864579009,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.016358744638621876,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.167172507197392,
                "relative_energy_error_percent": 0.016358744638621876,
                "rms_normalized_rmse_percent": 1.806342156505708,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013977330178022385,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.013542184606194496,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007215896621346474,
                  "p50": 1.8879657659454097e-07,
                  "p90": 2.193259424529972e-05,
                  "p95": 5.688890814781189e-05,
                  "p99": 0.0002460125833749771
                },
                "candidate_energy": 3.7476953509161177,
                "cvrmse_percent": 26.490149802999245,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17663985687627545,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.754326988735688,
                "relative_energy_error_percent": 0.17663985687627548,
                "rms_normalized_rmse_percent": 2.058911149811134,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017256954684853554,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.0179785443469882,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.3629169985652,
            "full": 3209.5953749958426
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.32587495911866,
            "full": 3260.2479160996154
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.74312503263354,
            "full": 3246.747124940157
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.76666597090662,
            "full": 3127.855832921341
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
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024662690702825785,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1704396456480026e-05,
                  "p99": 7.59205431677401e-05
                },
                "candidate_energy": 6.168680097058768,
                "cvrmse_percent": 4.94533365329928,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01521262078111221,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.167741821884647,
                "relative_energy_error_percent": 0.015212620781112206,
                "rms_normalized_rmse_percent": 0.8957119384542901,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00203014153521508,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0022767684422433376,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005365898832678795,
                  "p50": 1.4281845039931795e-07,
                  "p90": 1.6060547204688197e-05,
                  "p95": 3.657548222690821e-05,
                  "p99": 0.00014317501336336136
                },
                "candidate_energy": 3.7504524339330914,
                "cvrmse_percent": 16.574101654478024,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17508786355983585,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7570305384361298,
                "relative_energy_error_percent": 0.17508786355983585,
                "rms_normalized_rmse_percent": 1.2891893113136035,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026367855258286,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.02690444514155388,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 237.3049579327926,
            "full": 5680.7615829166025
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.77170800510794,
            "full": 5619.533082935959
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.20974996406585,
            "full": 5629.607957904227
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 227.71350003313273,
            "full": 5662.18212491367
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
    "/content/suite-vulkan-0.3.3/trapezoid_plan/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1264.4111249828711,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4901.656667003408,
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
        "identifier": "trapezoid_plan_grid",
        "full_identifier": "trapezoid_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0309257155410263,
            "cvrmse_percent": 3.9359485403799774,
            "rms_normalized_rmse_percent": 0.7129903844963904,
            "reference_energy": 6.169869913363982,
            "candidate_energy": 6.167961836945324,
            "relative_energy_error_percent": 0.030925715541026303,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.0028015822172165e-06,
              "p99": 4.457496106624603e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4974576773478832,
            "cvrmse_percent": 32.80049890761838,
            "rms_normalized_rmse_percent": 2.550070356231441,
            "reference_energy": 3.7520825430049562,
            "candidate_energy": 3.695896694904299,
            "relative_energy_error_percent": 1.4974576773478832,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.4799662646255456e-07,
              "p90": 3.0199578031897548e-05,
              "p95": 4.6378256229218096e-05,
              "p99": 0.00010936940088868141,
              "maximum": 0.0013134777545928955
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026397688314318657,
              "candidate": 0.02508421055972576,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.585508999108588,
            "cvrmse_percent": 12.38373531940351,
            "rms_normalized_rmse_percent": 2.5459398101772575,
            "reference_energy": 9.921952456368938,
            "candidate_energy": 9.863858531849623,
            "relative_energy_error_percent": 0.5855089991085879,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.503561257251931e-07,
              "p90": 3.0117772985249844e-05,
              "p95": 4.668440669775009e-05,
              "p99": 0.000112207664642483,
              "maximum": 0.0013134777545928955
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026397688314318657,
              "candidate": 0.02508421055972576,
              "position": [
                4.5,
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
        "identifier": "trapezoid_plan_grid",
        "full_identifier": "trapezoid_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0309257155410263,
            "cvrmse_percent": 3.9359485403799774,
            "rms_normalized_rmse_percent": 0.7129903844963904,
            "reference_energy": 6.169869913363982,
            "candidate_energy": 6.167961836945324,
            "relative_energy_error_percent": 0.030925715541026303,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.0028015822172165e-06,
              "p99": 4.457496106624603e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.87144386026579,
            "cvrmse_percent": 394.17020686567565,
            "rms_normalized_rmse_percent": 19.09205935224506,
            "reference_energy": 2.0547434409741427,
            "candidate_energy": 3.695896694904299,
            "relative_energy_error_percent": 79.8714438602658,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00017249299708055338,
              "p95": 0.0002391701564192772,
              "p99": 0.00046271272003650665,
              "maximum": 0.005828309804201126
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011069990694522858,
              "candidate": 0.016898300498723984,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.930969480125988,
            "cvrmse_percent": 98.4581626477529,
            "rms_normalized_rmse_percent": 19.088798576464203,
            "reference_energy": 8.224613354338125,
            "candidate_energy": 9.863858531849623,
            "relative_energy_error_percent": 19.930969480125984,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00017182825395138936,
              "p95": 0.00023960000544320792,
              "p99": 0.00045283790677785873,
              "maximum": 0.005828309804201126
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011069990694522858,
              "candidate": 0.016898300498723984,
              "position": [
                0.5,
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
      "bias_percent": 0.193967674383891,
      "rms_normalized_error_percent": 0.23329741510511304,
      "absolute_error": {
        "p95": 0.07493770439293757,
        "p99": 0.0862075706139525,
        "maximum": 0.09423539064701458
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.091363828164093,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23329741510511304
    },
    "overcast": {
      "bias_percent": 0.14292085125520987,
      "rms_normalized_error_percent": 0.1947664509664183,
      "absolute_error": {
        "p95": 0.046740740537643426,
        "p99": 0.061217393875122095,
        "maximum": 0.07217788696289062
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.797034740447998,
      "reference_fraction_of_uniform": 0.6376419067382812,
      "rms_normalized_to_uniform_percent": 0.137855595490415
    },
    "horizon": {
      "bias_percent": 1.2311763170877559,
      "rms_normalized_error_percent": 2.380112675435522,
      "absolute_error": {
        "p95": 0.05488032279153485,
        "p99": 0.05880163759228903,
        "maximum": 0.060693560562870896
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8437824847728814,
      "reference_fraction_of_uniform": 0.09281143079533696,
      "rms_normalized_to_uniform_percent": 0.12350574700404121
    },
    "north": {
      "bias_percent": -76.2931696197218,
      "rms_normalized_error_percent": 103.91588404753833,
      "absolute_error": {
        "p95": 0.0002479170354490633,
        "p99": 0.00035926991287851714,
        "maximum": 0.0003907127829734236
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.526574801071547e-05,
      "reference_fraction_of_uniform": 3.879038104059873e-06,
      "rms_normalized_to_uniform_percent": 0.0005122670579373766
    },
    "east": {
      "bias_percent": -0.08707991360946961,
      "rms_normalized_error_percent": 0.27919840906132964,
      "absolute_error": {
        "p95": 0.020238375663757323,
        "p99": 0.023481720685958867,
        "maximum": 0.025107383728027344
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8320914506912231,
      "reference_fraction_of_uniform": 0.20151998102664948,
      "rms_normalized_to_uniform_percent": 0.05923630775576938
    },
    "south": {
      "bias_percent": 0.2768245367182726,
      "rms_normalized_error_percent": 0.3053270457612497,
      "absolute_error": {
        "p95": 0.06742411851882935,
        "p99": 0.0761953926086426,
        "maximum": 0.08199858665466309
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.314180850982666,
      "reference_fraction_of_uniform": 0.6945251226425171,
      "rms_normalized_to_uniform_percent": 0.19870686556639347
    },
    "west": {
      "bias_percent": 0.204462041716333,
      "rms_normalized_error_percent": 0.3932894879584959,
      "absolute_error": {
        "p95": 0.026791707426309583,
        "p99": 0.03469364762306215,
        "maximum": 0.04043078422546387
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.771000862121582,
      "reference_fraction_of_uniform": 0.19480034708976746,
      "rms_normalized_to_uniform_percent": 0.07996077072732045
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
        "identifier": "trapezoid_plan_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.04807081552087216,
          "cvrmse_percent": 1.9134020584736218,
          "absolute_error_percentiles_lux": {
            "p50": 2.258392333984375,
            "p90": 20.628649902343756,
            "p95": 30.836010742187483,
            "p99": 61.09053253173826
          },
          "maximum_absolute_error_lux": 388.29638671875,
          "worst": {
            "sensor_index": 36,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5104.6630859375,
            "radiance_lux": 5492.95947265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6345148401826481,
            "maximum_error_percentage_points": 3.2897260273972613,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3061976848573811,
            "maximum_error_percentage_points": 1.1967103452986905,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2059531963470316,
            "maximum_error_percentage_points": 0.8227397260273932,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2119663242009131,
            "maximum_error_percentage_points": 0.8236986301369882,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.018587328767123313,
            "maximum_error_percentage_points": 0.1675342465753431,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 29.166666666666668,
          "radiance_percent": 29.166666666666668,
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
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004678403253421948,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004794520547945158,
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
      "study_preparation_seconds": 0.3793615829999908,
      "weather_seconds": 0.22894766400008848,
      "metric_reduction_seconds": 0.19043872400004602,
      "write_seconds": 0.013340352999989591,
      "total_seconds": 0.4330732390000094,
      "cold_end_to_end_seconds": 0.8124348220000002,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0017233739999937825,
      "engine_upload_seconds": 0.014193661,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.015724131,
      "engine_annual_reduction_seconds": 0.007366673,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.015724131
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3793615829999908,
      "weather_seconds": 0.23268209600007594,
      "metric_reduction_seconds": 0.16789418500002284,
      "write_seconds": 0.012766015000011066,
      "total_seconds": 0.41360221499996896,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.41360221499996896,
      "raw_export_seconds": 0.0017397489999666504,
      "engine_upload_seconds": 0.013784165,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.03e-07,
      "engine_annual_reduction_seconds": 0.008963682,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013692327999933696,
      "full": 0.024787134000007427
    }
  },
  "elapsed_seconds": 2.9239589359999627,
  "result_class": "passed"
}
```
