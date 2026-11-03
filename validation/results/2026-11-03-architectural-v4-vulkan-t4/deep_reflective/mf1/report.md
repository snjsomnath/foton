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
  "model_sha256": "596e2dd8121225f5d627905fde0220cd23a2b09a4bc182e491d3776e02a3db71",
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
      "scene_fingerprint": 17209437186486154619,
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
      "scene_fingerprint": 17209437186486154619,
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "f183c02c2d6f97c824fe68b25c00f3360cca9d3a391b83a30066435724d73d2a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "bc8dc63ed3373f853fc8759757ef0d2a72678922d616cafd9d7d27a1c69847a7",
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
          "p95": 0.0,
          "p99": 4.836800508201122e-05
        },
        "bias_percent": -0.06712927225850966,
        "identifier": "deep_reflective_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.100732911914109,
        "worst_index": [
          21,
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
          "maximum": 0.0027865618467330933,
          "p95": 9.72669804468751e-05,
          "p99": 0.0002066078595817089
        },
        "bias_percent": 3.607327177468171,
        "identifier": "deep_reflective_grid",
        "passed": false,
        "rms_normalized_error_percent": 3.8852061822319226,
        "worst_index": [
          70,
          0,
          0
        ]
      }
    ],
    "passed": false
  },
  "sample_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0009982287883758545,
          "p95": 6.07762485742569e-05,
          "p99": 0.00013280799612402916
        },
        "bias_percent": 0.00733109409790397,
        "identifier": "deep_reflective_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8030015432355219,
        "worst_index": [
          45,
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009249319555237889,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018063513562083244
                },
                "candidate_energy": 6.244660248483342,
                "cvrmse_percent": 17.774429777982167,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.023413585320311178,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.246122689748518,
                "relative_energy_error_percent": 0.02341358532031118,
                "rms_normalized_rmse_percent": 2.6592221819074497,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0031916379230096936,
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "reference": 0.0022667059674859047,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016453200951218605,
                  "p50": 0.0,
                  "p90": 8.979834092315286e-06,
                  "p95": 4.779074151883833e-05,
                  "p99": 0.00034571532160043716
                },
                "candidate_energy": 3.903374486160743,
                "cvrmse_percent": 54.445935257250746,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5264008676658155,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.9240306173780937,
                "relative_energy_error_percent": 0.5264008676658156,
                "rms_normalized_rmse_percent": 3.1241722773516045,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0205529797822237,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.01890765968710184,
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
          "timings_ms": {
            "direct": 152.71645900793374,
            "full": 353.25074999127537
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
          "timings_ms": {
            "direct": 131.6948749590665,
            "full": 364.86625007819384
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
          "timings_ms": {
            "direct": 126.28662504721433,
            "full": 345.0047499500215
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
          "timings_ms": {
            "direct": 134.20691597275436,
            "full": 364.5755419274792
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037103984504938126,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001284298487007618
                },
                "candidate_energy": 6.245969482209148,
                "cvrmse_percent": 12.089234078016379,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0673107344046154,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.250176521927642,
                "relative_energy_error_percent": 0.0673107344046154,
                "rms_normalized_rmse_percent": 1.8101036650567783,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014948225114494562,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.015319264959543943,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00236467644572258,
                  "p50": 6.730953661104877e-07,
                  "p90": 6.369606126099825e-05,
                  "p95": 0.00010392069816589355,
                  "p99": 0.00025196722708642483
                },
                "candidate_energy": 16.68665170867196,
                "cvrmse_percent": 13.110583904966077,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.13284758797716392,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 16.708849011562567,
                "relative_energy_error_percent": 0.1328475879771639,
                "rms_normalized_rmse_percent": 1.6071460765141,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07265591621398926,
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "reference": 0.07502059265971184,
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
          "timings_ms": {
            "direct": 187.29833397082984,
            "full": 5410.938916960731
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
          "timings_ms": {
            "direct": 220.8517079707235,
            "full": 5141.863375087269
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
          "timings_ms": {
            "direct": 247.23787500988692,
            "full": 5014.506833977066
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
          "timings_ms": {
            "direct": 198.7859579967335,
            "full": 4706.959667033516
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004219803959131241,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013755098916590214
                },
                "candidate_energy": 6.2469718682168605,
                "cvrmse_percent": 11.742867173637924,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.08407481808353055,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.2417241499924785,
                "relative_energy_error_percent": 0.08407481808353055,
                "rms_normalized_rmse_percent": 1.757152646336066,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013533000368624926,
                  "global_sensor_index": 58,
                  "local_sensor_index": 58,
                  "reference": 0.013111019972711802,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010320991277694702,
                  "p50": 6.412187758542132e-07,
                  "p90": 6.559770554304123e-05,
                  "p95": 0.00010789703810587525,
                  "p99": 0.00025676237419247627
                },
                "candidate_energy": 17.53231073046353,
                "cvrmse_percent": 10.923379025863637,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0354268954355436,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.526101776713165,
                "relative_energy_error_percent": 0.0354268954355436,
                "rms_normalized_rmse_percent": 1.3608303438491993,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04239189997315407,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.04342399910092354,
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
          "timings_ms": {
            "direct": 188.82487493101507,
            "full": 5269.018999999389
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
          "timings_ms": {
            "direct": 183.39154194109142,
            "full": 5272.699667024426
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
          "timings_ms": {
            "direct": 181.35104095563293,
            "full": 5394.917499972507
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
          "timings_ms": {
            "direct": 188.55108402203768,
            "full": 5632.083749980666
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000231095589697361,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.629694300703704e-05
                },
                "candidate_energy": 6.248358333003125,
                "cvrmse_percent": 7.275002531178011,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.008598801117188389,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.248895663113217,
                "relative_energy_error_percent": 0.008598801117188389,
                "rms_normalized_rmse_percent": 1.0896106522645013,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012586705386638641,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.01235560979694128,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000988699495792389,
                  "p50": 4.827942206020452e-07,
                  "p90": 4.515648470260203e-05,
                  "p95": 7.14363413862884e-05,
                  "p99": 0.0001692150253802538
                },
                "candidate_energy": 17.522022947475506,
                "cvrmse_percent": 7.974665137074568,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.053014873485008496,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.53131715308447,
                "relative_energy_error_percent": 0.053014873485008496,
                "rms_normalized_rmse_percent": 0.9939172510649527,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08523855730891228,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.08424985781311989,
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
          "timings_ms": {
            "direct": 303.41870803385973,
            "full": 10956.626374972984
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
          "timings_ms": {
            "direct": 296.5982089517638,
            "full": 10646.162749966606
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
          "timings_ms": {
            "direct": 287.6264590304345,
            "full": 10492.670207982883
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
          "timings_ms": {
            "direct": 280.35999997518957,
            "full": 10986.261624959297
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/deep_reflective/mf1/oracle/scene.rad"
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
      "elapsed_ms": 2740.480500040576,
      "invocation_count": 5,
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
      "elapsed_ms": 11888.999375049025,
      "invocation_count": 5,
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
            "nmbe_percent": -0.044607787023079604,
            "cvrmse_percent": 4.7592804962705495,
            "rms_normalized_rmse_percent": 0.7125400865384521,
            "reference_energy": 6.249268474763994,
            "candidate_energy": 6.246480814392271,
            "relative_energy_error_percent": 0.0446077870230796,
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
            "nmbe_percent": -5.4596887371483325,
            "cvrmse_percent": 41.726008983012036,
            "rms_normalized_rmse_percent": 5.2019001072788384,
            "reference_energy": 17.526028586452913,
            "candidate_energy": 16.569161977648946,
            "relative_energy_error_percent": 5.459688737148333,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9396579773456324e-06,
              "p90": 0.00010887792450375855,
              "p95": 0.00015999542665667832,
              "p99": 0.0003289789892733097,
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
            "nmbe_percent": -4.0363502786306364,
            "cvrmse_percent": 30.74527368699806,
            "rms_normalized_rmse_percent": 5.199672140107651,
            "reference_energy": 23.775297061216907,
            "candidate_energy": 22.815642792041217,
            "relative_energy_error_percent": 4.0363502786306364,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9038101299884147e-06,
              "p90": 0.00010874577856156975,
              "p95": 0.00016195327043533325,
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
            "nmbe_percent": -0.044607787023079604,
            "cvrmse_percent": 4.7592804962705495,
            "rms_normalized_rmse_percent": 0.7125400865384521,
            "reference_energy": 6.249268474763994,
            "candidate_energy": 6.246480814392271,
            "relative_energy_error_percent": 0.0446077870230796,
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
            "nmbe_percent": 323.7826420365949,
            "cvrmse_percent": 1943.6635736550818,
            "rms_normalized_rmse_percent": 111.26119757943604,
            "reference_energy": 3.909825541230674,
            "candidate_energy": 16.569161977648946,
            "relative_energy_error_percent": 323.78264203659484,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008354444289579988,
              "p95": 0.0010931023862212896,
              "p99": 0.0017021000385284424,
              "maximum": 0.04417215660214424
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 70,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026255641132593155,
              "candidate": 0.0704277977347374,
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
            "nmbe_percent": 124.58343978429414,
            "cvrmse_percent": 748.0258055717253,
            "rms_normalized_rmse_percent": 111.2594260606788,
            "reference_energy": 10.159094015994668,
            "candidate_energy": 22.815642792041217,
            "relative_energy_error_percent": 124.58343978429414,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008356799953617156,
              "p95": 0.0010924236848950386,
              "p99": 0.001691146520897746,
              "maximum": 0.04417215660214424
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 70,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026255641132593155,
              "candidate": 0.0704277977347374,
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
      "bias_percent": -2.9870963975554536,
      "rms_normalized_error_percent": 2.036259589143401,
      "absolute_error": {
        "p95": 0.5697937737875889,
        "p99": 0.6642649995006987,
        "maximum": 0.7156694949303333
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.473345607998972,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.036259589143401
    },
    "overcast": {
      "bias_percent": -2.862941549465954,
      "rms_normalized_error_percent": 1.7694979958133168,
      "absolute_error": {
        "p95": 0.3425089955329896,
        "p99": 0.40252633094787627,
        "maximum": 0.43462467193603516
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.065602779388428,
      "reference_fraction_of_uniform": 0.6158275604248047,
      "rms_normalized_to_uniform_percent": 1.2055706063925298
    },
    "horizon": {
      "bias_percent": -5.334467396069938,
      "rms_normalized_error_percent": 5.823984664893001,
      "absolute_error": {
        "p95": 0.15408690347136011,
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
      "rms_normalized_to_uniform_percent": 0.5189722383304026
    },
    "north": {
      "bias_percent": -65.57974919472706,
      "rms_normalized_error_percent": 107.01180310893126,
      "absolute_error": {
        "p95": 0.00018332058643864005,
        "p99": 0.00043291033274727234,
        "maximum": 0.0007651976775377989
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.969297853880562e-05,
      "reference_fraction_of_uniform": 5.202752618060913e-06,
      "rms_normalized_to_uniform_percent": 0.0006688157718997377
    },
    "east": {
      "bias_percent": -3.471594000911415,
      "rms_normalized_error_percent": 2.3886587706429676,
      "absolute_error": {
        "p95": 0.16232452392578128,
        "p99": 0.187655143737793,
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
      "rms_normalized_to_uniform_percent": 0.5204130009680135
    },
    "south": {
      "bias_percent": -2.8686599618886626,
      "rms_normalized_error_percent": 2.107777109855569,
      "absolute_error": {
        "p95": 0.4030102610588074,
        "p99": 0.46490856647491485,
        "maximum": 0.499176025390625
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.05582046508789,
      "reference_fraction_of_uniform": 0.7021334767341614,
      "rms_normalized_to_uniform_percent": 1.3938488591085467
    },
    "west": {
      "bias_percent": -2.8803257963466984,
      "rms_normalized_error_percent": 2.0505018630256826,
      "absolute_error": {
        "p95": 0.13518984317779548,
        "p99": 0.16711814284324647,
        "maximum": 0.16918087005615234
      },
      "worst_index": [
        68
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.285738706588745,
      "reference_fraction_of_uniform": 0.1992216408252716,
      "rms_normalized_to_uniform_percent": 0.42841270313221097
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
          "nmbe_percent": -2.886663177520793,
          "cvrmse_percent": 5.909158998188629,
          "absolute_error_percentiles_lux": {
            "p50": 16.46990966796875,
            "p90": 96.3671752929688,
            "p95": 134.6308441162108,
            "p99": 220.45362548827745
          },
          "maximum_absolute_error_lux": 698.018310546875,
          "worst": {
            "sensor_index": 45,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 3375.031005859375,
            "radiance_lux": 4073.04931640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.417347792998478,
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
      "study_preparation_seconds": 0.3987572200021532,
      "weather_seconds": 0.22782446800192702,
      "metric_reduction_seconds": 0.3139838349998172,
      "write_seconds": 0.025457996998738963,
      "total_seconds": 0.5677185300010024,
      "cold_end_to_end_seconds": 0.9664757500031556,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01151145599942538,
      "engine_upload_seconds": 0.014747713,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.022289134,
      "engine_annual_reduction_seconds": 0.011262841,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.022289134
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3987572200021532,
      "weather_seconds": 0.23906623199945898,
      "metric_reduction_seconds": 0.32160161799765774,
      "write_seconds": 0.024360624000109965,
      "total_seconds": 0.5853173680006876,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5853173680006876,
      "raw_export_seconds": 0.011310353002045304,
      "engine_upload_seconds": 0.014379095,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5e-08,
      "engine_annual_reduction_seconds": 0.011670723,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015273028999217786,
      "full": 0.03323684000133653
    }
  },
  "elapsed_seconds": 3.1307382869999856,
  "result_class": "unstable_reference"
}
```
