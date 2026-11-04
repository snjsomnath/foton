# Foton report

Status: **passed**

```json
{
  "scene": "shallow_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "shallow_plan",
    "category": "form",
    "question": "How evenly does side lighting illuminate a shallow room?",
    "interactions": [
      "shallow_plan",
      "daylight_penetration"
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
    "sensors": 24,
    "floor_area": 24.0,
    "aperture_area": 2.9999999999999987
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "8f4bc86df26c7057953f46e581dd98847e8cf31e29a64b20221c4ff1a3666f9f",
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
      "scene_fingerprint": 1786167869922741379,
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
      "scene_fingerprint": 1786167869922741379,
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
    "model_sha256": "29dd1cb729988861b01d9c279904ca7b5421cc8b2287041945f494d12c1eb0a3",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "6c88af558bce1a42e600f067e4c484531c274a7df792ca0c76f1c07e92171d91",
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
          "p95": 7.2587281465530396e-06,
          "p99": 0.00011639855802059174
        },
        "bias_percent": -0.0847704889086791,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0242394974213487,
        "worst_index": [
          6,
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
          "maximum": 0.0006548408418893814,
          "p95": 5.959789268672466e-05,
          "p99": 0.0001617148518562317
        },
        "bias_percent": -0.011193819317810074,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.049717835874575,
        "worst_index": [
          17,
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
          "maximum": 0.0006330534815788269,
          "p95": 4.978012293577194e-05,
          "p99": 0.0001291641965508461
        },
        "bias_percent": 0.0088886680658888,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8060514885989586,
        "worst_index": [
          17,
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009957320289686322,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0001676629763096571,
                  "p99": 0.00046280096285045147
                },
                "candidate_energy": 5.465555563609087,
                "cvrmse_percent": 16.954308857598264,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.024261503346011237,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.464229859298939,
                "relative_energy_error_percent": 0.02426150334601124,
                "rms_normalized_rmse_percent": 3.927930891048671,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017228239448741078,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.00271855597384274,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014921501278877258,
                  "p50": 0.0,
                  "p90": 4.723234451375902e-05,
                  "p95": 0.0002455923240631819,
                  "p99": 0.0007377557922154665
                },
                "candidate_energy": 1.7559556199319672,
                "cvrmse_percent": 80.99389054773572,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4575255777804728,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7640264923332154,
                "relative_energy_error_percent": 0.45752557778047287,
                "rms_normalized_rmse_percent": 4.716115513838479,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0009602205827832222,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0005319295451045036,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 98.42337493319064,
            "full": 169.0916670486331
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.98358306661248,
            "full": 170.99899996537715
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 98.82666706107557,
            "full": 181.97841697838157
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.36987495329231,
            "full": 175.93608400784433
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005848815198987722,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.408500485122204e-05,
                  "p99": 0.00019558635540306568
                },
                "candidate_energy": 5.462767216718021,
                "cvrmse_percent": 7.625939930390545,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05772124582565388,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.459615858427242,
                "relative_energy_error_percent": 0.05772124582565388,
                "rms_normalized_rmse_percent": 1.7664407995996496,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0024802780244499445,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0018953965045511723,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008177608251571655,
                  "p50": 2.9321103767188106e-07,
                  "p90": 3.690834273584187e-05,
                  "p95": 0.00010497402399778366,
                  "p99": 0.0003184424713253975
                },
                "candidate_energy": 3.195115977805763,
                "cvrmse_percent": 19.9085727533282,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.31495448493746575,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2052109333921877,
                "relative_energy_error_percent": 0.31495448493746575,
                "rms_normalized_rmse_percent": 1.759288979995705,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0422268807888031,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.041409119963645935,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.21258296631277,
            "full": 1606.253125006333
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.73924990929663,
            "full": 1555.1809169119224
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.7124999538064,
            "full": 1532.8420829027891
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.53791589662433,
            "full": 1521.2227500742301
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032477843342348933,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.202992517501116e-05,
                  "p99": 0.00019851000979542732
                },
                "candidate_energy": 5.459148365453075,
                "cvrmse_percent": 6.948797134627485,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04222932886624966,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.461454701119692,
                "relative_energy_error_percent": 0.042229328866249666,
                "rms_normalized_rmse_percent": 1.6108934220805073,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019854370621033013,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0023102154955267906,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008998261764645576,
                  "p50": 2.650828321293375e-07,
                  "p90": 3.8218604458961636e-05,
                  "p95": 0.00011886982247233391,
                  "p99": 0.00029760273173451424
                },
                "candidate_energy": 3.200884393469572,
                "cvrmse_percent": 20.994183277481117,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05003881943343987,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.1992835097709538,
                "relative_energy_error_percent": 0.05003881943343987,
                "rms_normalized_rmse_percent": 1.854366867789014,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030288799665868282,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.03118862584233284,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.27737503498793,
            "full": 1637.5667499378324
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.78383299801499,
            "full": 1662.4602089868858
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.42679196223617,
            "full": 1649.8606250388548
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.41029208619148,
            "full": 1627.9226249316707
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002347399713471532,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.353343345224857e-05,
                  "p99": 0.00010554702021181583
                },
                "candidate_energy": 5.45775154651983,
                "cvrmse_percent": 3.906736107884771,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06958558003878304,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.461551999157564,
                "relative_energy_error_percent": 0.06958558003878305,
                "rms_normalized_rmse_percent": 0.9052863457805365,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022295699454844,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0019948299741372466,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006204303354024887,
                  "p50": 2.2345061267969868e-07,
                  "p90": 2.373207826167345e-05,
                  "p95": 6.166007369756699e-05,
                  "p99": 0.00018222536891698837
                },
                "candidate_energy": 3.201506635974134,
                "cvrmse_percent": 12.78498451003795,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.00019614651527718235,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2015003563427484,
                "relative_energy_error_percent": 0.00019614651527718232,
                "rms_normalized_rmse_percent": 1.1302730943777526,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03382330574095249,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.03444373607635498,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.8863330669701,
            "full": 2871.9373329076916
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.3690410098061,
            "full": 2821.886167046614
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.60750001575798,
            "full": 2893.6698749894276
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.88887505512685,
            "full": 2896.751291002147
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/shallow_plan/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 474.90370797459036,
      "invocation_count": 2,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1571.2445829994977,
      "invocation_count": 2,
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
      24,
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
        "identifier": "shallow_plan_grid",
        "full_identifier": "shallow_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08939205047327413,
            "cvrmse_percent": 2.9809800053390223,
            "rms_normalized_rmse_percent": 0.6906912875368817,
            "reference_energy": 5.461538826516517,
            "candidate_energy": 5.4566566449720995,
            "relative_energy_error_percent": 0.08939205047327413,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.682457074522972e-06,
              "p99": 5.921628326177597e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.42604871203522854,
            "cvrmse_percent": 15.065975421968288,
            "rms_normalized_rmse_percent": 1.3311142086128687,
            "reference_energy": 3.1996164432403447,
            "candidate_energy": 3.2132483678868375,
            "relative_energy_error_percent": 0.4260487120352285,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.905904399445717e-07,
              "p90": 4.034527228213847e-05,
              "p95": 6.346963346004486e-05,
              "p99": 0.000168744008988142,
              "maximum": 0.0008291266858577728
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.041793301701545715,
              "candidate": 0.04262242838740349,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.1010228177368929,
            "cvrmse_percent": 5.468086771570978,
            "rms_normalized_rmse_percent": 1.3077699881572096,
            "reference_energy": 8.661155269756861,
            "candidate_energy": 8.669905012858937,
            "relative_energy_error_percent": 0.10102281773689291,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.905904399445717e-07,
              "p90": 4.055141471326351e-05,
              "p95": 6.394926458597183e-05,
              "p99": 0.00015449896454811096,
              "maximum": 0.0008291266858577728
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.041793301701545715,
              "candidate": 0.04262242838740349,
              "position": [
                4.5,
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
      24,
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
        "identifier": "shallow_plan_grid",
        "full_identifier": "shallow_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08939205047327413,
            "cvrmse_percent": 2.9809800053390223,
            "rms_normalized_rmse_percent": 0.6906912875368817,
            "reference_energy": 5.461538826516517,
            "candidate_energy": 5.4566566449720995,
            "relative_energy_error_percent": 0.08939205047327413,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.682457074522972e-06,
              "p99": 5.921628326177597e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.2246067798891,
            "cvrmse_percent": 483.3311065464572,
            "rms_normalized_rmse_percent": 28.192969671293067,
            "reference_energy": 1.7633449316579686,
            "candidate_energy": 3.2132483678868375,
            "relative_energy_error_percent": 82.2246067798891,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002656018186826259,
              "p95": 0.0003563466889318079,
              "p99": 0.0006698258221149445,
              "maximum": 0.012391192838549614
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030231235548853874,
              "candidate": 0.04262242838740349,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.00061596907361,
            "cvrmse_percent": 117.9409480342629,
            "rms_normalized_rmse_percent": 28.18735220610634,
            "reference_energy": 7.224883758174485,
            "candidate_energy": 8.669905012858937,
            "relative_energy_error_percent": 20.00061596907361,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00026547955349087715,
              "p95": 0.0003464299952611327,
              "p99": 0.0006533004343509674,
              "maximum": 0.012391192838549614
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030231235548853874,
              "candidate": 0.04262242838740349,
              "position": [
                4.5,
                2.5,
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
      "bias_percent": 0.3216088206622756,
      "rms_normalized_error_percent": 0.380934752608013,
      "absolute_error": {
        "p95": 0.2735190808307957,
        "p99": 0.3142479326156437,
        "maximum": 0.31837016383193806
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.294629689967095,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.380934752608013
    },
    "overcast": {
      "bias_percent": 0.2339836432695304,
      "rms_normalized_error_percent": 0.2812774702780399,
      "absolute_error": {
        "p95": 0.13448228836059556,
        "p99": 0.15431729316711426,
        "maximum": 0.15691280364990234
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.611858367919922,
      "reference_fraction_of_uniform": 0.6512488126754761,
      "rms_normalized_to_uniform_percent": 0.19787042258536722
    },
    "horizon": {
      "bias_percent": 1.939671192267304,
      "rms_normalized_error_percent": 3.3955158597388557,
      "absolute_error": {
        "p95": 0.09517550925273588,
        "p99": 0.14651082103314184,
        "maximum": 0.16091065606835286
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3509101306325848,
      "reference_fraction_of_uniform": 0.08290523665378939,
      "rms_normalized_to_uniform_percent": 0.19156230433849378
    },
    "north": {
      "bias_percent": -65.2804009681387,
      "rms_normalized_error_percent": 109.03438793894868,
      "absolute_error": {
        "p95": 0.00012657368624786612,
        "p99": 0.00013989676672281347,
        "maximum": 0.00014350803394336253
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.632579708006233e-05,
      "reference_fraction_of_uniform": 1.6156118363142014e-06,
      "rms_normalized_to_uniform_percent": 0.00019383146463076845
    },
    "east": {
      "bias_percent": 0.17477942597413484,
      "rms_normalized_error_percent": 0.37701268482423017,
      "absolute_error": {
        "p95": 0.03914625346660614,
        "p99": 0.048006889820098875,
        "maximum": 0.05061912536621094
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4232728481292725,
      "reference_fraction_of_uniform": 0.21008595824241638,
      "rms_normalized_to_uniform_percent": 0.08067661365134679
    },
    "south": {
      "bias_percent": 0.426268962812438,
      "rms_normalized_error_percent": 0.5148457072834893,
      "absolute_error": {
        "p95": 0.2405107021331784,
        "p99": 0.28493112564086914,
        "maximum": 0.2915382385253906
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.894523620605469,
      "reference_fraction_of_uniform": 0.6685959696769714,
      "rms_normalized_to_uniform_percent": 0.3367075097487195
    },
    "west": {
      "bias_percent": 0.20334100251782689,
      "rms_normalized_error_percent": 0.3761746648164121,
      "absolute_error": {
        "p95": 0.04457900524139404,
        "p99": 0.0487929081916809,
        "maximum": 0.05004739761352539
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.3131000995635986,
      "reference_fraction_of_uniform": 0.20332466065883636,
      "rms_normalized_to_uniform_percent": 0.07704587090773954
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
        "identifier": "shallow_plan_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.1961255637623709,
          "cvrmse_percent": 1.5802259768111475,
          "absolute_error_percentiles_lux": {
            "p50": 3.0498123168945312,
            "p90": 28.99451599121096,
            "p95": 44.437014770507815,
            "p99": 91.72847534179684
          },
          "maximum_absolute_error_lux": 421.43359375,
          "worst": {
            "sensor_index": 12,
            "position": [
              4.5,
              2.5,
              0.75
            ],
            "hour_of_year": 7308.5,
            "foton_lux": 12832.6669921875,
            "radiance_lux": 12411.2333984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3132591324200922,
            "maximum_error_percentage_points": 1.2899999999999991,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10729782241754175,
            "maximum_error_percentage_points": 0.7066933581872306,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09714041095890447,
            "maximum_error_percentage_points": 0.3609589041095944,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09367009132420072,
            "maximum_error_percentage_points": 0.3609589041095944,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04773972602739728,
            "maximum_error_percentage_points": 0.2699999999999996,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 66.66666666666667,
          "radiance_percent": 66.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
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
      "maximum_error_percentage_points": 0.004931506849314982,
      "metrics": {
        "da": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.0045082405821972316,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "shallow_plan_grid",
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
      "study_preparation_seconds": 0.005725083057768643,
      "weather_seconds": 0.12741579196881503,
      "metric_reduction_seconds": 0.03067320806439966,
      "write_seconds": 0.009852124960161746,
      "total_seconds": 0.16814425005577505,
      "cold_end_to_end_seconds": 0.1738693331135437,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014632079983130097,
      "engine_upload_seconds": 0.000257584,
      "engine_acceleration_structure_seconds": 0.002817917,
      "engine_tracing_seconds": 0.009262124774977565,
      "engine_annual_reduction_seconds": 0.00026266672648489475,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.009262124774977565
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005725083057768643,
      "weather_seconds": 0.07333012507297099,
      "metric_reduction_seconds": 0.01113895804155618,
      "write_seconds": 0.010474584065377712,
      "total_seconds": 0.09505416708998382,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09505416708998382,
      "raw_export_seconds": 0.001354791922494769,
      "engine_upload_seconds": 4.0125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003063332987949252,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013644708087667823,
      "full": 0.016329332953318954
    }
  },
  "elapsed_seconds": 0.707463291939348,
  "result_class": "passed"
}
```
