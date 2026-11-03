# Foton report

Status: **incomplete**

```json
{
  "scene": "deep_reflective",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "deep_reflective",
    "category": "materials",
    "question": "Does reflected light reach the rear of a deep bright room?",
    "interactions": [
      "deep_plan",
      "multiple_bounces",
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
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "f183c02c2d6f97c824fe68b25c00f3360cca9d3a391b83a30066435724d73d2a",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17209437186486154619,
      "basis": "Tregenza",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17209437186486154619,
      "basis": "Tregenza",
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
  "oracle_stable": false,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "deep_reflective_grid",
        "bias_percent": -0.06712927225850966,
        "rms_normalized_error_percent": 1.100732911914109,
        "absolute_error": {
          "p95": 0.0,
          "p99": 4.836800508201122e-05,
          "maximum": 0.0003254120238125324
        },
        "worst_index": [
          21,
          72,
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
    "passed": false,
    "grids": [
      {
        "identifier": "deep_reflective_grid",
        "bias_percent": 3.607327177468171,
        "rms_normalized_error_percent": 3.8852061822319226,
        "absolute_error": {
          "p95": 9.72669804468751e-05,
          "p99": 0.0002066078595817089,
          "maximum": 0.0027865618467330933
        },
        "worst_index": [
          70,
          0,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "deep_reflective_grid",
        "bias_percent": 0.00733109409790397,
        "rms_normalized_error_percent": 0.8030015432355219,
        "absolute_error": {
          "p95": 6.07762485742569e-05,
          "p99": 0.00013280799612402916,
          "maximum": 0.0009982287883758545
        },
        "worst_index": [
          45,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "deep_reflective_grid",
            "start_sensor_index": 0,
            "sensor_count": 72,
            "stages": {
              "direct": {
                "nmbe_percent": -0.023413585320311178,
                "cvrmse_percent": 17.774429777982167,
                "rms_normalized_rmse_percent": 2.6592221819074497,
                "reference_energy": 6.246122689748518,
                "candidate_energy": 6.244660248483342,
                "relative_energy_error_percent": 0.02341358532031118,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018063513562083244,
                  "maximum": 0.0009249319555237889
                },
                "worst": {
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0022667059674859047,
                  "candidate": 0.0031916379230096936
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5264008676658155,
                "cvrmse_percent": 54.445935257250746,
                "rms_normalized_rmse_percent": 3.1241722773516045,
                "reference_energy": 3.9240306173780937,
                "candidate_energy": 3.903374486160743,
                "relative_energy_error_percent": 0.5264008676658156,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.979834092315286e-06,
                  "p95": 4.779074151883833e-05,
                  "p99": 0.00034571532160043716,
                  "maximum": 0.0016453200951218605
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.01890765968710184,
                  "candidate": 0.0205529797822237
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.71645900793374,
            "full": 353.25074999127537
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.6948749590665,
            "full": 364.86625007819384
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.28662504721433,
            "full": 345.0047499500215
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.20691597275436,
            "full": 364.5755419274792
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "deep_reflective_grid",
            "start_sensor_index": 0,
            "sensor_count": 72,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0673107344046154,
                "cvrmse_percent": 12.089234078016379,
                "rms_normalized_rmse_percent": 1.8101036650567783,
                "reference_energy": 6.250176521927642,
                "candidate_energy": 6.245969482209148,
                "relative_energy_error_percent": 0.0673107344046154,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001284298487007618,
                  "maximum": 0.00037103984504938126
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.015319264959543943,
                  "candidate": 0.014948225114494562
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.13284758797716392,
                "cvrmse_percent": 13.110583904966077,
                "rms_normalized_rmse_percent": 1.6071460765141,
                "reference_energy": 16.708849011562567,
                "candidate_energy": 16.68665170867196,
                "relative_energy_error_percent": 0.1328475879771639,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.730953661104877e-07,
                  "p90": 6.369606126099825e-05,
                  "p95": 0.00010392069816589355,
                  "p99": 0.00025196722708642483,
                  "maximum": 0.00236467644572258
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07502059265971184,
                  "candidate": 0.07265591621398926
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.29833397082984,
            "full": 5410.938916960731
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.8517079707235,
            "full": 5141.863375087269
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 247.23787500988692,
            "full": 5014.506833977066
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 198.7859579967335,
            "full": 4706.959667033516
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "deep_reflective_grid",
            "start_sensor_index": 0,
            "sensor_count": 72,
            "stages": {
              "direct": {
                "nmbe_percent": 0.08407481808353055,
                "cvrmse_percent": 11.742867173637924,
                "rms_normalized_rmse_percent": 1.757152646336066,
                "reference_energy": 6.2417241499924785,
                "candidate_energy": 6.2469718682168605,
                "relative_energy_error_percent": 0.08407481808353055,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013755098916590214,
                  "maximum": 0.0004219803959131241
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 58,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.013111019972711802,
                  "candidate": 0.013533000368624926
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0354268954355436,
                "cvrmse_percent": 10.923379025863637,
                "rms_normalized_rmse_percent": 1.3608303438491993,
                "reference_energy": 17.526101776713165,
                "candidate_energy": 17.53231073046353,
                "relative_energy_error_percent": 0.0354268954355436,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.412187758542132e-07,
                  "p90": 6.559770554304123e-05,
                  "p95": 0.00010789703810587525,
                  "p99": 0.00025676237419247627,
                  "maximum": 0.0010320991277694702
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04342399910092354,
                  "candidate": 0.04239189997315407
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.82487493101507,
            "full": 5269.018999999389
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 183.39154194109142,
            "full": 5272.699667024426
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 181.35104095563293,
            "full": 5394.917499972507
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.55108402203768,
            "full": 5632.083749980666
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "deep_reflective_grid",
            "start_sensor_index": 0,
            "sensor_count": 72,
            "stages": {
              "direct": {
                "nmbe_percent": -0.008598801117188389,
                "cvrmse_percent": 7.275002531178011,
                "rms_normalized_rmse_percent": 1.0896106522645013,
                "reference_energy": 6.248895663113217,
                "candidate_energy": 6.248358333003125,
                "relative_energy_error_percent": 0.008598801117188389,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.629694300703704e-05,
                  "maximum": 0.000231095589697361
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 0.01235560979694128,
                  "candidate": 0.012586705386638641
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.053014873485008496,
                "cvrmse_percent": 7.974665137074568,
                "rms_normalized_rmse_percent": 0.9939172510649527,
                "reference_energy": 17.53131715308447,
                "candidate_energy": 17.522022947475506,
                "relative_energy_error_percent": 0.053014873485008496,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.827942206020452e-07,
                  "p90": 4.515648470260203e-05,
                  "p95": 7.14363413862884e-05,
                  "p99": 0.0001692150253802538,
                  "maximum": 0.000988699495792389
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08424985781311989,
                  "candidate": 0.08523855730891228
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 303.41870803385973,
            "full": 10956.626374972984
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 296.5982089517638,
            "full": 10646.162749966606
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 287.6264590304345,
            "full": 10492.670207982883
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 280.35999997518957,
            "full": 10986.261624959297
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2740.480500040576,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11888.999375049025,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      72,
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
        "identifier": "deep_reflective_grid",
        "full_identifier": "deep_reflective_grid",
        "start_sensor_index": 0,
        "sensor_count": 72,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04460572186459421,
            "cvrmse_percent": 4.7592811319647295,
            "rms_normalized_rmse_percent": 0.712540181711995,
            "reference_energy": 6.249268474763994,
            "candidate_energy": 6.246480943449569,
            "relative_energy_error_percent": 0.0446057218645942,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.165728412568569e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
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
            "nmbe_percent": -5.459547129023107,
            "cvrmse_percent": 41.72450366479953,
            "rms_normalized_rmse_percent": 5.20171244219507,
            "reference_energy": 17.526028586452913,
            "candidate_energy": 16.569186795929454,
            "relative_energy_error_percent": 5.459547129023107,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9396579773456324e-06,
              "p90": 0.00010891660349443555,
              "p95": 0.00015999542665667832,
              "p99": 0.00032897875644266605,
              "maximum": 0.004513334482908249
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 55,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05504060536623001,
              "candidate": 0.05052727088332176,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -4.036245348973009,
            "cvrmse_percent": 30.7441634370565,
            "rms_normalized_rmse_percent": 5.199484373501686,
            "reference_energy": 23.775297061216907,
            "candidate_energy": 22.815667739379023,
            "relative_energy_error_percent": 4.036245348973009,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9038101299884147e-06,
              "p90": 0.00010878892135224305,
              "p95": 0.00016195280477404594,
              "p99": 0.00032271817326545715,
              "maximum": 0.004513334482908249
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 55,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05504060536623001,
              "candidate": 0.05052727088332176,
              "position": [
                4.5,
                4.5,
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
      72,
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
        "identifier": "deep_reflective_grid",
        "full_identifier": "deep_reflective_grid",
        "start_sensor_index": 0,
        "sensor_count": 72,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04460572186459421,
            "cvrmse_percent": 4.7592811319647295,
            "rms_normalized_rmse_percent": 0.712540181711995,
            "reference_energy": 6.249268474763994,
            "candidate_energy": 6.246480943449569,
            "relative_energy_error_percent": 0.0446057218645942,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.165728412568569e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
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
            "nmbe_percent": 323.7832768035492,
            "cvrmse_percent": 1943.6790302782938,
            "rms_normalized_rmse_percent": 111.2620823634246,
            "reference_energy": 3.909825541230674,
            "candidate_energy": 16.569186795929454,
            "relative_energy_error_percent": 323.7832768035492,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008354444289579988,
              "p95": 0.0010931023862212896,
              "p99": 0.0017021000385284424,
              "maximum": 0.04417217895388603
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 70,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026255641132593155,
              "candidate": 0.07042782008647919,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 124.58368535085518,
            "cvrmse_percent": 748.0317549400736,
            "rms_normalized_rmse_percent": 111.26031095435886,
            "reference_energy": 10.159094015994668,
            "candidate_energy": 22.815667739379023,
            "relative_energy_error_percent": 124.58368535085518,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008356799953617156,
              "p95": 0.0010924236848950386,
              "p99": 0.001691146520897746,
              "maximum": 0.04417217895388603
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 70,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026255641132593155,
              "candidate": 0.07042782008647919,
              "position": [
                5.5,
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
      "bias_percent": -2.9872825620982892,
      "rms_normalized_error_percent": 2.0363404319260603,
      "absolute_error": {
        "p95": 0.5697927600022105,
        "p99": 0.6642631348857809,
        "maximum": 0.7156674527727365
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.473345607998972,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.0363404319260603
    },
    "overcast": {
      "bias_percent": -2.8631689729944285,
      "rms_normalized_error_percent": 1.7695907053037054,
      "absolute_error": {
        "p95": 0.34250835180282596,
        "p99": 0.4025254392623904,
        "maximum": 0.43462276458740234
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.065602779388428,
      "reference_fraction_of_uniform": 0.6158275604248047,
      "rms_normalized_to_uniform_percent": 1.2056337461461164
    },
    "horizon": {
      "bias_percent": -5.334456320297941,
      "rms_normalized_error_percent": 5.82397672343184,
      "absolute_error": {
        "p95": 0.15408683887249755,
        "p99": 0.17327703398422506,
        "maximum": 0.19586037040943438
      },
      "worst_index": [
        39
      ],
      "passed": false,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.546304223028475,
      "reference_fraction_of_uniform": 0.13477361145213168,
      "rms_normalized_to_uniform_percent": 0.5189715306709372
    },
    "north": {
      "bias_percent": -65.57974958452536,
      "rms_normalized_error_percent": 107.01180229402311,
      "absolute_error": {
        "p95": 0.00018332058480154958,
        "p99": 0.00043291036650771567,
        "maximum": 0.0007651977939531207
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.969297853880562e-05,
      "reference_fraction_of_uniform": 5.202752618060913e-06,
      "rms_normalized_to_uniform_percent": 0.0006688158516667696
    },
    "east": {
      "bias_percent": -3.470898424253934,
      "rms_normalized_error_percent": 2.3879214880233794,
      "absolute_error": {
        "p95": 0.1617935121059418,
        "p99": 0.1876537895202637,
        "maximum": 0.19157695770263672
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3880772590637207,
      "reference_fraction_of_uniform": 0.20814131200313568,
      "rms_normalized_to_uniform_percent": 0.5202524152557867
    },
    "south": {
      "bias_percent": -2.8687589705714185,
      "rms_normalized_error_percent": 2.1077595155496653,
      "absolute_error": {
        "p95": 0.4030102610588074,
        "p99": 0.46490679740905794,
        "maximum": 0.4991745948791504
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.05582046508789,
      "reference_fraction_of_uniform": 0.7021334767341614,
      "rms_normalized_to_uniform_percent": 1.3938370969810998
    },
    "west": {
      "bias_percent": -2.8814544767931376,
      "rms_normalized_error_percent": 2.051734291250193,
      "absolute_error": {
        "p95": 0.1351893067359925,
        "p99": 0.16750970482826236,
        "maximum": 0.1705334186553955
      },
      "worst_index": [
        68
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.285738945007324,
      "reference_fraction_of_uniform": 0.1992216557264328,
      "rms_normalized_to_uniform_percent": 0.4286702038737139
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
        "identifier": "deep_reflective_grid",
        "sensor_count": 72,
        "illuminance": {
          "nmbe_percent": -2.886885563071968,
          "cvrmse_percent": 5.908928586121877,
          "absolute_error_percentiles_lux": {
            "p50": 16.46961212158203,
            "p90": 96.36660156250001,
            "p95": 134.62653198242185,
            "p99": 220.4534814453087
          },
          "maximum_absolute_error_lux": 698.017822265625,
          "worst": {
            "sensor_index": 45,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 3375.031494140625,
            "radiance_lux": 4073.04931640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.4169311263318112,
            "maximum_error_percentage_points": 4.769041095890408,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.7573696347422317,
            "maximum_error_percentage_points": 2.361979401389135,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.547861491628615,
            "maximum_error_percentage_points": 1.6168493150684924,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6583047945205492,
            "maximum_error_percentage_points": 1.9134246575342502,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.21769786910197875,
            "maximum_error_percentage_points": 1.9997260273972604,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 86.11111111111111,
          "radiance_percent": 100.0,
          "difference_percentage_points": 13.888888888888886,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 10,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004977525684935813,
      "metrics": {
        "da": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004977525684935813,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
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
      "study_preparation_seconds": 0.007903749938122928,
      "weather_seconds": 0.10702183295506984,
      "metric_reduction_seconds": 0.06620775000192225,
      "write_seconds": 0.038930792012251914,
      "total_seconds": 0.21241183299571276,
      "cold_end_to_end_seconds": 0.22031558293383569,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013057166012004018,
      "engine_upload_seconds": 0.00030975,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.04521625000052154,
      "engine_annual_reduction_seconds": 0.0006407499313354492,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.04521625000052154
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007903749938122928,
      "weather_seconds": 0.09684416593518108,
      "metric_reduction_seconds": 0.013729707919992507,
      "write_seconds": 0.021348666050471365,
      "total_seconds": 0.1321375840343535,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1321375840343535,
      "raw_export_seconds": 0.011812416953034699,
      "engine_upload_seconds": 6.475e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0007037499453872442,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015170916100032628,
      "full": 0.04244004201609641
    }
  },
  "elapsed_seconds": 105.92384737497196,
  "result_class": "unstable_reference"
}
```
