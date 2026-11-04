# Foton report

Status: **passed**

```json
{
  "scene": "double_height",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "double_height",
    "category": "form",
    "question": "How does tall glazing light a double-height volume?",
    "interactions": [
      "tall_volume",
      "high_glazing"
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
    "aperture_area": 18.000000000000004
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "d8b50d3498a236c356a5befdaadbfe0c0995543da0693aac8304acbe8189417a",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 457850612654732671,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 457850612654732671,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "a13903cc363eaafaa0c6db1a84e01377701c500d9b5f39527dab9e831cc6316e",
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
          "maximum": 0.0005031544715166092,
          "p95": 2.1678081247955525e-05,
          "p99": 0.00012181699275970459
        },
        "bias_percent": 0.04496058831465672,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7199423715550772,
        "worst_index": [
          34,
          134,
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
          "maximum": 0.0005484670400619507,
          "p95": 0.00010887191165238616,
          "p99": 0.0002345377579331398
        },
        "bias_percent": 0.030293367054421854,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6750334033026618,
        "worst_index": [
          2,
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
          "maximum": 0.0008472427725791931,
          "p95": 9.62366466410458e-05,
          "p99": 0.00019488949328660965
        },
        "bias_percent": -0.0005054711916432203,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.607367767852829,
        "worst_index": [
          32,
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006396300159394741,
                  "p50": 0.0,
                  "p90": 9.319721721112728e-05,
                  "p95": 0.00018494813703000534,
                  "p99": 0.00031256023794412613
                },
                "candidate_energy": 21.70761149971804,
                "cvrmse_percent": 5.176681843725119,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.006216310729160974,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.706262171013805,
                "relative_energy_error_percent": 0.006216310729160974,
                "rms_normalized_rmse_percent": 1.8199852043390403,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01353264506906271,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.014172275085002184,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001080045010894537,
                  "p50": 0.0,
                  "p90": 0.00016273558139801025,
                  "p95": 0.00030029035406187155,
                  "p99": 0.0005885944701731205
                },
                "candidate_energy": 7.691254441361345,
                "cvrmse_percent": 25.724833138254404,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20141982821664337,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.706777419200137,
                "relative_energy_error_percent": 0.20141982821664334,
                "rms_normalized_rmse_percent": 2.261085794505376,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0027439454570412636,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.0016639004461467266,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 299.2322079371661,
            "full": 545.1262920396402
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.56825005821884,
            "full": 277.4992079939693
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.55158400535583,
            "full": 272.1147909760475
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 305.467874975875,
            "full": 400.5069578997791
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003458545543253422,
                  "p50": 0.0,
                  "p90": 6.760400719940662e-05,
                  "p95": 0.00012148212990723516,
                  "p99": 0.00022514956071972847
                },
                "candidate_energy": 21.701602333647315,
                "cvrmse_percent": 3.5864005677065065,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.015143464827909089,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.70488920591015,
                "relative_energy_error_percent": 0.015143464827909089,
                "rms_normalized_rmse_percent": 1.2613773762295095,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012942189816385508,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.012596335262060165,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013250000774860382,
                  "p50": 5.680965102783375e-07,
                  "p90": 0.00011456006905063987,
                  "p95": 0.0002037749658484242,
                  "p99": 0.0004040133208036423
                },
                "candidate_energy": 13.660015349994762,
                "cvrmse_percent": 10.567985122140866,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.009579491546807444,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.661324035375912,
                "relative_energy_error_percent": 0.009579491546807446,
                "rms_normalized_rmse_percent": 1.2411987966520737,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07073279470205307,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.06940779462456703,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.2959170890972,
            "full": 2297.8732500923797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.83179190661758,
            "full": 2209.954292047769
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.0677090222016,
            "full": 2142.0756250154227
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.71358296927065,
            "full": 2166.790207964368
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000505085801705718,
                  "p50": 0.0,
                  "p90": 7.197028025984764e-05,
                  "p95": 0.00011792901204898941,
                  "p99": 0.00025364337489008904
                },
                "candidate_energy": 21.70821788374451,
                "cvrmse_percent": 4.015294465606686,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.018222519407581836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.70426282023982,
                "relative_energy_error_percent": 0.018222519407581836,
                "rms_normalized_rmse_percent": 1.4123036992388103,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006932895630598068,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.007437981432303786,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012945346534252167,
                  "p50": 4.968984512743191e-07,
                  "p90": 0.00012026634067296982,
                  "p95": 0.00021860744454897934,
                  "p99": 0.0004159053787589073
                },
                "candidate_energy": 13.671811436594211,
                "cvrmse_percent": 10.945401280874567,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05010397142975586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.664964746561708,
                "relative_energy_error_percent": 0.05010397142975586,
                "rms_normalized_rmse_percent": 1.2859862225418148,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0828470028936863,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.08155246824026108,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.99779094010592,
            "full": 2229.9217499094084
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.19499999657273,
            "full": 2254.1675840038806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.35687500517815,
            "full": 2205.1596250385046
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.0378749780357,
            "full": 2223.890041001141
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000202057883143425,
                  "p50": 0.0,
                  "p90": 3.508059307932854e-05,
                  "p95": 6.872259546071288e-05,
                  "p99": 0.00013422605115920305
                },
                "candidate_energy": 21.702058277185643,
                "cvrmse_percent": 2.0416653177621713,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0002591583159305229,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.702002034642646,
                "relative_energy_error_percent": 0.0002591583159305229,
                "rms_normalized_rmse_percent": 0.7180914602123446,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007521317107602954,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.007723374990746379,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010054558515548706,
                  "p50": 4.295432347589667e-07,
                  "p90": 6.927872891537845e-05,
                  "p95": 0.00011805037502199388,
                  "p99": 0.00023332051932811737
                },
                "candidate_energy": 13.672837493506616,
                "cvrmse_percent": 6.3245226765215135,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.006115721104176611,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.672001352034567,
                "relative_energy_error_percent": 0.006115721104176611,
                "rms_normalized_rmse_percent": 0.7433756663596878,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0802907645702362,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.07928530871868134,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 259.36483300756663,
            "full": 3906.904458999634
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.95354102086276,
            "full": 3909.3799999682233
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 254.10587503574789,
            "full": 3873.1876669917256
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.68399996962398,
            "full": 3926.1616659350693
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/double_height/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 799.4257080135867,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3055.473415995948,
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
        "identifier": "double_height_grid",
        "full_identifier": "double_height_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.011693766057094488,
            "cvrmse_percent": 1.2160184309675381,
            "rms_normalized_rmse_percent": 0.4277727386923545,
            "reference_energy": 21.701828901466797,
            "candidate_energy": 21.704366662568646,
            "relative_energy_error_percent": 0.011693766057094488,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5739351511001587e-06,
              "p95": 2.0870455773547147e-05,
              "p99": 8.262321352958679e-05,
              "maximum": 0.00024562887847423553
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.011655369773507118,
              "candidate": 0.011900998651981354,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.07468265100982834,
            "cvrmse_percent": 8.266934095360433,
            "rms_normalized_rmse_percent": 0.9714481318725129,
            "reference_energy": 13.672620667529944,
            "candidate_energy": 13.682831743106973,
            "relative_energy_error_percent": 0.07468265100982834,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.6255435184575617e-06,
              "p90": 7.800778257660568e-05,
              "p95": 0.00012010270729660975,
              "p99": 0.00027372571639716625,
              "maximum": 0.0013959705829620361
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07971307635307312,
              "candidate": 0.08110904693603516,
              "position": [
                3.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.036039675059851575,
            "cvrmse_percent": 3.1824536913164176,
            "rms_normalized_rmse_percent": 0.9675538845007482,
            "reference_energy": 35.374449568996745,
            "candidate_energy": 35.38719840567562,
            "relative_energy_error_percent": 0.03603967505984154,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.6312769730575383e-06,
              "p90": 7.702445145696402e-05,
              "p95": 0.00011719417670974504,
              "p99": 0.00027577392756938934,
              "maximum": 0.0013959705829620361
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07971307635307312,
              "candidate": 0.08110904693603516,
              "position": [
                3.5,
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
        "identifier": "double_height_grid",
        "full_identifier": "double_height_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.011693766057094488,
            "cvrmse_percent": 1.2160184309675381,
            "rms_normalized_rmse_percent": 0.4277727386923545,
            "reference_energy": 21.701828901466797,
            "candidate_energy": 21.704366662568646,
            "relative_energy_error_percent": 0.011693766057094488,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5739351511001587e-06,
              "p95": 2.0870455773547147e-05,
              "p99": 8.262321352958679e-05,
              "maximum": 0.00024562887847423553
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.011655369773507118,
              "candidate": 0.011900998651981354,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.60399480248124,
            "cvrmse_percent": 464.7315271758894,
            "rms_normalized_rmse_percent": 40.8363573584447,
            "reference_energy": 7.7041238618106895,
            "candidate_energy": 13.682831743106973,
            "relative_energy_error_percent": 77.60399480248124,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.7773020886124868e-06,
              "p90": 0.0006851125508546829,
              "p95": 0.0008545234566554425,
              "p99": 0.0014751930721104145,
              "maximum": 0.031312357634305954
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0497966893017292,
              "candidate": 0.08110904693603516,
              "position": [
                3.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.34025454148041,
            "cvrmse_percent": 121.7560234357174,
            "rms_normalized_rmse_percent": 40.83638730914747,
            "reference_energy": 29.405952763277487,
            "candidate_energy": 35.38719840567562,
            "relative_energy_error_percent": 20.34025454148041,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.7773020886124868e-06,
              "p90": 0.000685785198584199,
              "p95": 0.0008526159683242437,
              "p99": 0.0014754747971892357,
              "maximum": 0.031312357634305954
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0497966893017292,
              "candidate": 0.08110904693603516,
              "position": [
                3.5,
                4.5,
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
      "bias_percent": 0.13332712475988912,
      "rms_normalized_error_percent": 0.28157238919700495,
      "absolute_error": {
        "p95": 0.2956081942252329,
        "p99": 0.4221286324840107,
        "maximum": 0.440605574055418
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 45.85925097054141,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.28157238919700495
    },
    "overcast": {
      "bias_percent": 0.05769526301962758,
      "rms_normalized_error_percent": 0.20110317355204954,
      "absolute_error": {
        "p95": 0.12030792236328125,
        "p99": 0.17912373542785642,
        "maximum": 0.18645000457763672
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 30.788917541503906,
      "reference_fraction_of_uniform": 0.6713785529136658,
      "rms_normalized_to_uniform_percent": 0.14025798309494164
    },
    "horizon": {
      "bias_percent": 1.8389956067358242,
      "rms_normalized_error_percent": 2.5987966126405966,
      "absolute_error": {
        "p95": 0.1853420870338186,
        "p99": 0.24964198049577915,
        "maximum": 0.277027385726464
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.3579362718431027,
      "reference_fraction_of_uniform": 0.07322265847735147,
      "rms_normalized_to_uniform_percent": 0.16908099789075431
    },
    "north": {
      "bias_percent": -3.517007959800381,
      "rms_normalized_error_percent": 20.320567258198075,
      "absolute_error": {
        "p95": 0.00021036146881669993,
        "p99": 0.0003020414409547811,
        "maximum": 0.0003119195098406635
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.00012887785851489753,
      "reference_fraction_of_uniform": 2.8102915621275315e-06,
      "rms_normalized_to_uniform_percent": 0.0001855448997567848
    },
    "east": {
      "bias_percent": -0.1323933029580709,
      "rms_normalized_error_percent": 0.3387929490957916,
      "absolute_error": {
        "p95": 0.08703827857971191,
        "p99": 0.10009694099426268,
        "maximum": 0.10280227661132812
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.739972114562988,
      "reference_fraction_of_uniform": 0.1905825436115265,
      "rms_normalized_to_uniform_percent": 0.0739700803714575
    },
    "south": {
      "bias_percent": 0.2258422862318017,
      "rms_normalized_error_percent": 0.39834573800601647,
      "absolute_error": {
        "p95": 0.3025674819946289,
        "p99": 0.3992153167724609,
        "maximum": 0.41053199768066406
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 30.81709861755371,
      "reference_fraction_of_uniform": 0.6719930768013,
      "rms_normalized_to_uniform_percent": 0.25667499812577493
    },
    "west": {
      "bias_percent": 0.0645177933078173,
      "rms_normalized_error_percent": 0.2749508686363607,
      "absolute_error": {
        "p95": 0.05605494976043701,
        "p99": 0.07481033802032466,
        "maximum": 0.0842132568359375
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.401952743530273,
      "reference_fraction_of_uniform": 0.18321174383163452,
      "rms_normalized_to_uniform_percent": 0.056937760071734914
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
        "identifier": "double_height_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.061030246626731975,
          "cvrmse_percent": 0.9754212858917944,
          "absolute_error_percentiles_lux": {
            "p50": 5.979217529296875,
            "p90": 52.548876953125,
            "p95": 79.54121093749995,
            "p99": 169.00965332031194
          },
          "maximum_absolute_error_lux": 651.619140625,
          "worst": {
            "sensor_index": 12,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 23866.328125,
            "radiance_lux": 23214.708984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.04523592085235922,
            "maximum_error_percentage_points": 0.19630136986300784,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.018432342752116346,
            "maximum_error_percentage_points": 0.07964355521005473,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.012298325722983419,
            "maximum_error_percentage_points": 0.10602739726027544,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1777359208523606,
            "maximum_error_percentage_points": 0.7635616438356223,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.1757229832572298,
            "maximum_error_percentage_points": 0.7709589041095875,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004990903253428769,
      "metrics": {
        "da": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.004990903253428769,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "double_height_grid",
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
      "study_preparation_seconds": 0.0057302090572193265,
      "weather_seconds": 0.07594312494620681,
      "metric_reduction_seconds": 0.03511037502903491,
      "write_seconds": 0.011432665982283652,
      "total_seconds": 0.12259858404286206,
      "cold_end_to_end_seconds": 0.12832879310008138,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015802079578861594,
      "engine_upload_seconds": 0.000271,
      "engine_acceleration_structure_seconds": 0.002761458,
      "engine_tracing_seconds": 0.013713208376429975,
      "engine_annual_reduction_seconds": 0.00035129161551594734,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.013713208376429975
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0057302090572193265,
      "weather_seconds": 0.07344204105902463,
      "metric_reduction_seconds": 0.012906207935884595,
      "write_seconds": 0.009401416988112032,
      "total_seconds": 0.09585470799356699,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09585470799356699,
      "raw_export_seconds": 0.001719375024549663,
      "engine_upload_seconds": 4.6917e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.000390166649594903,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013074000016786158,
      "full": 0.03559908305760473
    }
  },
  "elapsed_seconds": 0.6819970839424059,
  "result_class": "passed"
}
```
