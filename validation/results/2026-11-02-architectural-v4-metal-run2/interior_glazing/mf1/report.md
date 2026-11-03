# Foton report

Status: **failed**

```json
{
  "scene": "interior_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "interior_glazing",
    "category": "connections",
    "question": "Does daylight pass through a shared glazed wall exactly once?",
    "interactions": [
      "borrowed_light",
      "paired_apertures",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 3,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 8.999999999999996
  },
  "sky_density": 1,
  "status": "failed",
  "passed": false,
  "model_sha256": "af65586b86a7343b6dbb02eb2bd7490480c9aaaf810cb68c4f0db396a505f09c",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 14976319759523577797,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 14976319759523577797,
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
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.03254693500733346,
        "rms_normalized_error_percent": 0.3334157331607479,
        "absolute_error": {
          "p95": 1.3630085959448458e-06,
          "p99": 2.2667227312922478e-05,
          "maximum": 0.00012598984176293015
        },
        "worst_index": [
          16,
          94,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.12119452503198108,
        "rms_normalized_error_percent": 1.2060619661767238,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 2.5623623514547944e-05
        },
        "worst_index": [
          19,
          21,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      4096,
      16384
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.017715060637763715,
        "rms_normalized_error_percent": 1.0540653127996151,
        "absolute_error": {
          "p95": 4.447242245078086e-05,
          "p99": 0.00014786142855882645,
          "maximum": 0.0003548208624124527
        },
        "worst_index": [
          14,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.5013219289005713,
        "rms_normalized_error_percent": 4.075754325804379,
        "absolute_error": {
          "p95": 4.782846622219948e-06,
          "p99": 1.3809702068101615e-05,
          "maximum": 0.00010033161379396915
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": 0.034483561277408634,
        "rms_normalized_error_percent": 0.9053422015988052,
        "absolute_error": {
          "p95": 4.114469047635793e-05,
          "p99": 0.00011799484491348267,
          "maximum": 0.000399269163608551
        },
        "worst_index": [
          22,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": -0.1683244167707291,
        "rms_normalized_error_percent": 3.0759134695893793,
        "absolute_error": {
          "p95": 4.224652457196497e-06,
          "p99": 1.3888042303733528e-05,
          "maximum": 0.00010075094178318977
        },
        "worst_index": [
          2,
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08612833973478541,
                "cvrmse_percent": 18.60693506431097,
                "rms_normalized_rmse_percent": 3.8086465144896424,
                "reference_energy": 6.027310040775774,
                "candidate_energy": 6.022118818706986,
                "relative_energy_error_percent": 0.08612833973478543,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.391875064466148e-05,
                  "p99": 0.00037773256190121174,
                  "maximum": 0.0009763306006789207
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 0.015656590461730957,
                  "candidate": 0.014680259861052036
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.35735325252987743,
                "cvrmse_percent": 75.83133155022512,
                "rms_normalized_rmse_percent": 4.095209385212861,
                "reference_energy": 2.0122220665967347,
                "candidate_energy": 2.019412807599842,
                "relative_energy_error_percent": 0.35735325252987743,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8580198229756206e-05,
                  "p95": 0.0001584567478857934,
                  "p99": 0.0005235308781266212,
                  "maximum": 0.0010549710132181644
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": -0.0006167604587972164,
                  "candidate": 0.00043821055442094803
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -1.4553160323637369,
                "cvrmse_percent": 215.5806881507277,
                "rms_normalized_rmse_percent": 13.800845982301444,
                "reference_energy": 0.06458921547346108,
                "candidate_energy": 0.06364923826549784,
                "relative_energy_error_percent": 1.4553160323637366,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0003747869050130248
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.0024210429983213544,
                  "candidate": 0.0020462560933083296
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.6182297286831333,
                "cvrmse_percent": 324.0086632718678,
                "rms_normalized_rmse_percent": 14.615834001457818,
                "reference_energy": 0.07230132990656557,
                "candidate_energy": 0.06968530169365295,
                "relative_energy_error_percent": 3.6182297286831333,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.9969254683237523e-05,
                  "maximum": 0.00045547750778496265
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0033534790854901075,
                  "candidate": 0.002898001577705145
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.3252500044182,
            "full": 395.25312499608845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.62300000619143,
            "full": 393.11458298470825
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 120.62316702213138,
            "full": 385.92229201458395
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 121.54604203533381,
            "full": 379.88949997816235
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.01653788150355212,
                "cvrmse_percent": 8.301913962123068,
                "rms_normalized_rmse_percent": 1.6990249954062264,
                "reference_energy": 6.023855427834974,
                "candidate_energy": 6.0248516459075745,
                "relative_energy_error_percent": 0.016537881503552124,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.617455997504293e-05,
                  "p99": 0.00016250531189143658,
                  "maximum": 0.0003918129950761795
                },
                "worst": {
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0013138874783180654,
                  "candidate": 0.0009220744832418859
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.062256750428929176,
                "cvrmse_percent": 21.56798688159631,
                "rms_normalized_rmse_percent": 1.8051461869167655,
                "reference_energy": 3.6229902675329058,
                "candidate_energy": 3.625245823541828,
                "relative_energy_error_percent": 0.062256750428929176,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.240236298689524e-07,
                  "p90": 2.9393449949566275e-05,
                  "p95": 7.881952333264041e-05,
                  "p99": 0.0002721552737057209,
                  "maximum": 0.0005271853879094124
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02324269525706768,
                  "candidate": 0.023769880644977093
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.019868284741977514,
                "cvrmse_percent": 99.97203637205524,
                "rms_normalized_rmse_percent": 6.486748593405923,
                "reference_energy": 0.06502364540847339,
                "candidate_energy": 0.06501072632545402,
                "relative_energy_error_percent": 0.019868284741977518,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00013324388419277966
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 20,
                  "rgb_channel": 0,
                  "reference": 0.001111391989979893,
                  "candidate": 0.0009781481057871133
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.148564069827591,
                "cvrmse_percent": 101.1166361073153,
                "rms_normalized_rmse_percent": 8.44213713733904,
                "reference_energy": 0.16685082868480805,
                "candidate_energy": 0.16326593172947668,
                "relative_energy_error_percent": 2.148564069827591,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.838758402707754e-06,
                  "p95": 6.587311099792712e-06,
                  "p99": 2.582956130936509e-05,
                  "maximum": 0.00038321816828101873
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.004344514571130276,
                  "candidate": 0.003961296402849257
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 182.05537495668977,
            "full": 4993.773708003573
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.35849993489683,
            "full": 4965.962333022617
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 178.52612491697073,
            "full": 5043.7076250091195
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 183.94358397927135,
            "full": 5028.290208079852
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.12456067138988924,
                "cvrmse_percent": 7.6473972579895335,
                "rms_normalized_rmse_percent": 1.5650914810556387,
                "reference_energy": 6.019533746492925,
                "candidate_energy": 6.027031718142098,
                "relative_energy_error_percent": 0.12456067138988924,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6267019843071416e-05,
                  "p99": 0.00015462003648281097,
                  "maximum": 0.00032761250622570515
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0016163575346581638,
                  "candidate": 0.001943970040883869
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.3622190096396149,
                "cvrmse_percent": 21.638617272859555,
                "rms_normalized_rmse_percent": 1.813001836474696,
                "reference_energy": 3.6300539661953657,
                "candidate_energy": 3.6169052206696293,
                "relative_energy_error_percent": 0.36221900963961495,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.3437624996347495e-07,
                  "p90": 2.95147328870371e-05,
                  "p95": 7.23429722711443e-05,
                  "p99": 0.00024951971136033535,
                  "maximum": 0.0005616650450974703
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.0007075655739754438,
                  "candidate": 0.00014590052887797356
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.6762695910170372,
                "cvrmse_percent": 95.68569558043224,
                "rms_normalized_rmse_percent": 6.178400556632119,
                "reference_energy": 0.06458106865102309,
                "candidate_energy": 0.06414432652218238,
                "relative_energy_error_percent": 0.6762695910170372,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00011607559281401336
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.0008157737029250711,
                  "candidate": 0.0009318492957390845
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.25421579001238154,
                "cvrmse_percent": 68.73613583580587,
                "rms_normalized_rmse_percent": 5.722606730777388,
                "reference_energy": 0.16665445599628725,
                "candidate_energy": 0.16707811793818905,
                "relative_energy_error_percent": 0.25421579001238154,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.943324713873153e-06,
                  "p95": 6.7708327264881484e-06,
                  "p99": 2.70627442660043e-05,
                  "maximum": 0.00018014595843851566
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.004202783573418856,
                  "candidate": 0.00402263761498034
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 181.81558302603662,
            "full": 5393.832833040506
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.9042090056464,
            "full": 5383.793332963251
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 193.02266603335738,
            "full": 5358.511833008379
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 175.62925000675023,
            "full": 5325.634957989678
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.004596272723524306,
                "cvrmse_percent": 4.463928149019431,
                "rms_normalized_rmse_percent": 0.9134057220592965,
                "reference_energy": 6.024350122620376,
                "candidate_energy": 6.024073227058921,
                "relative_energy_error_percent": 0.004596272723524307,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3278058506548405e-05,
                  "p99": 8.715945295989513e-05,
                  "maximum": 0.0002172302920371294
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 0.007521581836044788,
                  "candidate": 0.007304351544007659
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.10342041632430668,
                "cvrmse_percent": 13.770794851819591,
                "rms_normalized_rmse_percent": 1.1529060066246735,
                "reference_energy": 3.627753104064997,
                "candidate_energy": 3.624001266701555,
                "relative_energy_error_percent": 0.1034204163243067,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6226022658827333e-07,
                  "p90": 1.946300471900031e-05,
                  "p95": 4.920647043036292e-05,
                  "p99": 0.00016374513506889343,
                  "maximum": 0.0004585292190313339
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02875866461545229,
                  "candidate": 0.028300135396420956
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.47274822242510844,
                "cvrmse_percent": 43.60369047137622,
                "rms_normalized_rmse_percent": 2.8233739375227915,
                "reference_energy": 0.06402599111061136,
                "candidate_energy": 0.06432867284547683,
                "relative_energy_error_percent": 0.4727482224251084,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.9258134569972754e-05
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.0007506001566071063,
                  "candidate": 0.0008098582911770791
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5698720548344269,
                "cvrmse_percent": 54.27704603226212,
                "rms_normalized_rmse_percent": 4.557654925715683,
                "reference_energy": 0.16713867843529684,
                "candidate_energy": 0.1661862018140745,
                "relative_energy_error_percent": 0.5698720548344269,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.552713678800501e-15,
                  "p90": 2.8102107307859114e-06,
                  "p95": 4.612232919498632e-06,
                  "p99": 1.3887894056097139e-05,
                  "maximum": 0.0001592210028320551
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.001975188497453928,
                  "candidate": 0.001815967494621873
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 286.165792029351,
            "full": 9412.800958030857
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 290.53941601887345,
            "full": 9633.149542030878
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 314.60004195105284,
            "full": 9378.35116602946
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 298.4084169147536,
            "full": 9347.092374926433
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2811.4002919755876,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10849.895583931357,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 42719.17137503624,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_16384/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf1/direct_16384/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 16384,
      "elapsed_ms": 173242.8658750141,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1512314075330195,
            "cvrmse_percent": 3.1505312748739747,
            "rms_normalized_rmse_percent": 0.645093105705596,
            "reference_energy": 6.023460207225753,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.1512314075330195,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.406652831472425e-06,
              "p99": 5.430757300928235e-05,
              "maximum": 0.00028031491092406213
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 42,
              "rgb_channel": 0,
              "reference": 0.00028031491092406213,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3788899010147744,
            "cvrmse_percent": 27.282230339109386,
            "rms_normalized_rmse_percent": 2.2840099877021514,
            "reference_energy": 3.6266286746642713,
            "candidate_energy": 3.5766214581220197,
            "relative_energy_error_percent": 1.3788899010147744,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.60316436803987e-07,
              "p90": 3.697641659528017e-05,
              "p95": 5.6125234550563544e-05,
              "p99": 0.00014357417239807546,
              "maximum": 0.0014414414763450623
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031303521245718,
              "candidate": 0.02986207976937294,
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
            "nmbe_percent": -0.6126014062603341,
            "cvrmse_percent": 10.235830332888515,
            "rms_normalized_rmse_percent": 2.280181555226015,
            "reference_energy": 9.650088881890024,
            "candidate_energy": 9.590972301694194,
            "relative_energy_error_percent": 0.6126014062603341,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.54045755052357e-07,
              "p90": 3.641593502834439e-05,
              "p95": 5.519389487744763e-05,
              "p99": 0.0001413028803654015,
              "maximum": 0.0014414414763450623
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031303521245718,
              "candidate": 0.02986207976937294,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21038794101712327,
            "cvrmse_percent": 15.406792473770276,
            "rms_normalized_rmse_percent": 0.999138626469515,
            "reference_energy": 0.06411396764679012,
            "candidate_energy": 0.06397907959035365,
            "relative_energy_error_percent": 0.21038794101712327,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.9536237232387066e-05
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 12,
              "sky_patch_index": 20,
              "rgb_channel": 0,
              "reference": 0.0007786959176883101,
              "candidate": 0.0007591596804559231,
              "position": [
                8.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5302325654279585,
            "cvrmse_percent": 66.17914519103259,
            "rms_normalized_rmse_percent": 5.5536883706752365,
            "reference_energy": 0.166725803476254,
            "candidate_energy": 0.16584176897125147,
            "relative_energy_error_percent": 0.5302325654279584,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 4.982099198969081e-06,
              "p95": 8.387987645619428e-06,
              "p99": 2.2359919967129827e-05,
              "maximum": 0.0001862610224634409
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0014333210419863462,
              "candidate": 0.0012470600195229053,
              "position": [
                7.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.44139818562541794,
            "cvrmse_percent": 47.98976955832285,
            "rms_normalized_rmse_percent": 5.575923852077721,
            "reference_energy": 0.2308397711230441,
            "candidate_energy": 0.22982084856160512,
            "relative_energy_error_percent": 0.44139818562541794,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 4.982661266694777e-06,
              "p95": 8.418805259680078e-06,
              "p99": 2.281737033626996e-05,
              "maximum": 0.0001862610224634409
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0014333210419863462,
              "candidate": 0.0012470600195229053,
              "position": [
                7.5,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1512314075330195,
            "cvrmse_percent": 3.1505312748739747,
            "rms_normalized_rmse_percent": 0.645093105705596,
            "reference_energy": 6.023460207225753,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.1512314075330195,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.406652831472425e-06,
              "p99": 5.430757300928235e-05,
              "maximum": 0.00028031491092406213
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 42,
              "rgb_channel": 0,
              "reference": 0.00028031491092406213,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.31751997912231,
            "cvrmse_percent": 409.56592999699143,
            "rms_normalized_rmse_percent": 22.168064905407768,
            "reference_energy": 2.017071668125709,
            "candidate_energy": 3.5766214581220197,
            "relative_energy_error_percent": 77.31751997912231,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021116000425536186,
              "p95": 0.00027896050305571386,
              "p99": 0.0005133052472956479,
              "maximum": 0.007752569392323494
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017212269827723503,
              "candidate": 0.024964839220046997,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.282809276531346,
            "cvrmse_percent": 102.7045340877683,
            "rms_normalized_rmse_percent": 22.159350524468238,
            "reference_energy": 8.040531875351462,
            "candidate_energy": 9.590972301694194,
            "relative_energy_error_percent": 19.28280927653135,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002070399932563305,
              "p95": 0.00027801209434983313,
              "p99": 0.000519597320817411,
              "maximum": 0.007752569392323494
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017212269827723503,
              "candidate": 0.024964839220046997,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21038794101712327,
            "cvrmse_percent": 15.406792473770276,
            "rms_normalized_rmse_percent": 0.999138626469515,
            "reference_energy": 0.06411396764679012,
            "candidate_energy": 0.06397907959035365,
            "relative_energy_error_percent": 0.21038794101712327,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.9536237232387066e-05
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 12,
              "sky_patch_index": 20,
              "rgb_channel": 0,
              "reference": 0.0007786959176883101,
              "candidate": 0.0007591596804559231,
              "position": [
                8.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 133.58464295850706,
            "cvrmse_percent": 834.378232563068,
            "rms_normalized_rmse_percent": 37.96014939703133,
            "reference_energy": 0.07099857545031796,
            "candidate_energy": 0.16584176897125147,
            "relative_energy_error_percent": 133.5846429585071,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1070000255131163e-05,
              "p95": 1.980550032385506e-05,
              "p99": 6.679999933112413e-05,
              "maximum": 0.0012060878798365593
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002619622042402625,
              "candidate": 0.0038257099222391844,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 70.09586474619776,
            "cvrmse_percent": 438.2705970523971,
            "rms_normalized_rmse_percent": 37.94489158245524,
            "reference_energy": 0.13511254309710807,
            "candidate_energy": 0.22982084856160512,
            "relative_energy_error_percent": 70.09586474619776,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1061169061576948e-05,
              "p95": 1.9799188976321582e-05,
              "p99": 6.679999933112413e-05,
              "maximum": 0.0012060878798365593
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002619622042402625,
              "candidate": 0.0038257099222391844,
              "position": [
                6.5,
                3.5,
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
      "bias_percent": -0.03335552322090424,
      "rms_normalized_error_percent": 0.2439991507191143,
      "absolute_error": {
        "p95": 0.09964191924027585,
        "p99": 0.13318246584528715,
        "maximum": 0.1395504472442033
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.043143671229155,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2439991507191143
    },
    "overcast": {
      "bias_percent": -0.05601353977969244,
      "rms_normalized_error_percent": 0.1981453068532404,
      "absolute_error": {
        "p95": 0.04889512062072756,
        "p99": 0.07623987674713144,
        "maximum": 0.08594250679016113
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8542933464050293,
      "reference_fraction_of_uniform": 0.6377960443496704,
      "rms_normalized_to_uniform_percent": 0.13994128490820898
    },
    "horizon": {
      "bias_percent": 0.29327650354112517,
      "rms_normalized_error_percent": 2.5144531693843235,
      "absolute_error": {
        "p95": 0.03993553649397441,
        "p99": 0.07609730864533838,
        "maximum": 0.0953392223766405
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5701654595425631,
      "reference_fraction_of_uniform": 0.09434914848327501,
      "rms_normalized_to_uniform_percent": 0.13533311296530656
    },
    "north": {
      "bias_percent": -58.779279724243544,
      "rms_normalized_error_percent": 103.15507636947068,
      "absolute_error": {
        "p95": 3.941505467537355e-05,
        "p99": 0.00021078227667203702,
        "maximum": 0.00047970263403840363
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.267913648916874e-05,
      "reference_fraction_of_uniform": 2.0981026409572223e-06,
      "rms_normalized_to_uniform_percent": 0.00039151927699051674
    },
    "east": {
      "bias_percent": 0.040194052108948664,
      "rms_normalized_error_percent": 0.3317156705414351,
      "absolute_error": {
        "p95": 0.023637551069259646,
        "p99": 0.03582096815109259,
        "maximum": 0.04262709617614746
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.225099802017212,
      "reference_fraction_of_uniform": 0.2027255743741989,
      "rms_normalized_to_uniform_percent": 0.07106728272524566
    },
    "south": {
      "bias_percent": 0.03515329340831149,
      "rms_normalized_error_percent": 0.2911144325587274,
      "absolute_error": {
        "p95": 0.0768882751464844,
        "p99": 0.10085203886032112,
        "maximum": 0.10961365699768066
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.172391891479492,
      "reference_fraction_of_uniform": 0.6904339790344238,
      "rms_normalized_to_uniform_percent": 0.189594926768611
    },
    "west": {
      "bias_percent": -0.49359931324276857,
      "rms_normalized_error_percent": 0.580242327953651,
      "absolute_error": {
        "p95": 0.032950910925865176,
        "p99": 0.07338920712471021,
        "maximum": 0.08811640739440918
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2041206359863281,
      "reference_fraction_of_uniform": 0.19925400614738464,
      "rms_normalized_to_uniform_percent": 0.11806408395489817
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.13845120286580198,
          "cvrmse_percent": 1.7590795153267873,
          "absolute_error_percentiles_lux": {
            "p50": 2.59637451171875,
            "p90": 24.969964599609376,
            "p95": 37.33833312988281,
            "p99": 70.73169921874995
          },
          "maximum_absolute_error_lux": 423.0283203125,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5108.640625,
            "radiance_lux": 5531.6689453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.523763318112633,
            "maximum_error_percentage_points": 2.0308219178082183,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.21956878667824775,
            "maximum_error_percentage_points": 0.7547548551863699,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13910197869101923,
            "maximum_error_percentage_points": 0.6568493150684915,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14240487062404839,
            "maximum_error_percentage_points": 0.5984931506849307,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0312785388127854,
            "maximum_error_percentage_points": 0.13369863013698635,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 52.77777777777778,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "adjacent_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.828047118470063,
          "cvrmse_percent": 15.72723619193076,
          "absolute_error_percentiles_lux": {
            "p50": 0.34995919466018677,
            "p90": 3.3674956321716314,
            "p95": 5.122459030151363,
            "p99": 10.236684837341251
          },
          "maximum_absolute_error_lux": 46.90978240966797,
          "worst": {
            "sensor_index": 3,
            "position": [
              6.5,
              2.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 147.13394165039062,
            "radiance_lux": 100.22415924072266
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.00926179604261797,
            "maximum_error_percentage_points": 0.07821917808219192,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15352416565189536,
            "maximum_error_percentage_points": 0.44625437509336807,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09767503805174964,
            "maximum_error_percentage_points": 2.031780821917806,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09767503805175057,
            "maximum_error_percentage_points": 2.0317808219178133,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
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
    "numerical_correctness": "failed",
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
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004109589041095929,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.0048204730308327726,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004751520026220035,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0,
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
      "study_preparation_seconds": 0.05024220794439316,
      "weather_seconds": 0.17056633299216628,
      "metric_reduction_seconds": 0.07377020793501288,
      "write_seconds": 0.06028704100754112,
      "total_seconds": 0.3048229579580948,
      "cold_end_to_end_seconds": 0.35506516590248793,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.020216708071529865,
      "engine_upload_seconds": 0.000273542,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.05636420822702348,
      "engine_annual_reduction_seconds": 0.0005905000725761056,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05636420822702348
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.05024220794439316,
      "weather_seconds": 0.08459924999624491,
      "metric_reduction_seconds": 0.012674084049649537,
      "write_seconds": 0.044236083049327135,
      "total_seconds": 0.1416995000327006,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1416995000327006,
      "raw_export_seconds": 0.019431416993029416,
      "engine_upload_seconds": 5.7667e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006187499966472387,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.009326500003226101,
      "full": 0.047233875025995076
    }
  },
  "elapsed_seconds": 315.3508012909442,
  "result_class": "accuracy_failure"
}
```
