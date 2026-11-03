# Foton report

Status: **passed**

```json
{
  "scene": "teaching_overhang100",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_overhang100",
    "category": "teaching",
    "question": "What does a 1.0 m overhang remove from the base room?",
    "interactions": [
      "multiple_bounces",
      "overhang",
      "side_glazing"
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
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "56362c1e97ff034560f6617d5d9c629f5559ff098c480dfefc7f1b80af10c447",
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
      "scene_fingerprint": 18413353015155885056,
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
      "scene_fingerprint": 18413353015155885056,
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
        "identifier": "teaching_overhang100_grid",
        "bias_percent": -0.09571524593148503,
        "rms_normalized_error_percent": 1.448056337746342,
        "absolute_error": {
          "p95": 9.785384463611966e-06,
          "p99": 0.00011097453534603119,
          "maximum": 0.0005787150003015995
        },
        "worst_index": [
          16,
          70,
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
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_overhang100_grid",
        "bias_percent": 0.09827961469973134,
        "rms_normalized_error_percent": 0.9383235447191185,
        "absolute_error": {
          "p95": 5.4677968728355805e-05,
          "p99": 0.00016026897355914116,
          "maximum": 0.0007681883871555328
        },
        "worst_index": [
          11,
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
        "identifier": "teaching_overhang100_grid",
        "bias_percent": 0.02270563555793385,
        "rms_normalized_error_percent": 0.7426843083167324,
        "absolute_error": {
          "p95": 4.1106165735982354e-05,
          "p99": 0.00013829534873366356,
          "maximum": 0.0004886239767074585
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
            "identifier": "teaching_overhang100_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.007829432486533757,
                "cvrmse_percent": 14.327472560696553,
                "rms_normalized_rmse_percent": 3.1624732709271646,
                "reference_energy": 5.153268854272028,
                "candidate_energy": 5.153672325977823,
                "relative_energy_error_percent": 0.007829432486533757,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.707148372195654e-05,
                  "p99": 0.00024658022448420525,
                  "maximum": 0.0006499465089291334
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.0023233649553731084,
                  "candidate": 0.002973311464302242
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1204668569790044,
                "cvrmse_percent": 38.80343472991181,
                "rms_normalized_rmse_percent": 2.8203601331122687,
                "reference_energy": 3.4963352354849917,
                "candidate_energy": 3.4921233103173535,
                "relative_energy_error_percent": 0.1204668569790044,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.9114975657430477e-05,
                  "p95": 0.0001431441225577142,
                  "p99": 0.0004489280399866402,
                  "maximum": 0.0010598096996545792
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.027487849816679955,
                  "candidate": 0.028547659516334534
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 107.98941703978926,
            "full": 237.11929202545434
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.9857080001384,
            "full": 229.34929199982435
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.3712079776451,
            "full": 226.59920796286315
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.51454201433808,
            "full": 231.6530420212075
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
            "identifier": "teaching_overhang100_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.034317876143579784,
                "cvrmse_percent": 11.318867168045248,
                "rms_normalized_rmse_percent": 2.4972457925048515,
                "reference_energy": 5.153772021343684,
                "candidate_energy": 5.152003356244677,
                "relative_energy_error_percent": 0.034317876143579784,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.122189759276764e-05,
                  "p99": 0.0002092702779918909,
                  "maximum": 0.00039575924165546894
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007831297116354108,
                  "candidate": 0.007435537874698639
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.07773869581933315,
                "cvrmse_percent": 17.446161338918973,
                "rms_normalized_rmse_percent": 1.609448212474664,
                "reference_energy": 5.615266470211633,
                "candidate_energy": 5.619631705132356,
                "relative_energy_error_percent": 0.07773869581933315,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.2234801261001849e-07,
                  "p90": 3.2350253604818135e-05,
                  "p95": 0.00011166939948452619,
                  "p99": 0.00033384724520146847,
                  "maximum": 0.000686300452798605
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 73,
                  "rgb_channel": 0,
                  "reference": 0.0007774904370307922,
                  "candidate": 9.118998423218727e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.9536659438163,
            "full": 2226.9515830557793
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.61779200751334,
            "full": 2324.9953750055283
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.0974580105394,
            "full": 2259.702124982141
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.41783306654543,
            "full": 2275.3208340145648
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
            "identifier": "teaching_overhang100_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10095600264036102,
                "cvrmse_percent": 9.123037592117639,
                "rms_normalized_rmse_percent": 2.013669388713169,
                "reference_energy": 5.149585731067418,
                "candidate_energy": 5.144386915160794,
                "relative_energy_error_percent": 0.10095600264036102,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.737651906907553e-05,
                  "p99": 0.0001595970243215561,
                  "maximum": 0.0003284565173089504
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.002035144018009305,
                  "candidate": 0.0023636005353182554
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.021001243097880297,
                "cvrmse_percent": 15.567323435851801,
                "rms_normalized_rmse_percent": 1.4376143898219587,
                "reference_energy": 5.633343952148586,
                "candidate_energy": 5.634527024406516,
                "relative_energy_error_percent": 0.021001243097880297,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1073147909712588e-07,
                  "p90": 2.9069502488709986e-05,
                  "p95": 9.389917249791323e-05,
                  "p99": 0.0002767980331555009,
                  "maximum": 0.0008534640073776245
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03935611434280872,
                  "candidate": 0.0385026503354311
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.93429201096296,
            "full": 2379.5745000243187
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.02979190647602,
            "full": 2355.102875037119
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 130.6110000004992,
            "full": 2402.4534999625757
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.4065829915926,
            "full": 2374.3437910452485
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
            "identifier": "teaching_overhang100_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.003286173983454747,
                "cvrmse_percent": 6.108715718447483,
                "rms_normalized_rmse_percent": 1.348718343014043,
                "reference_energy": 5.1523325105454205,
                "candidate_energy": 5.152501825155923,
                "relative_energy_error_percent": 0.003286173983454747,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.388059558346867e-05,
                  "p99": 0.0001034904271364212,
                  "maximum": 0.00029207998886704445
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 13,
                  "rgb_channel": 0,
                  "reference": 0.002022408996708691,
                  "candidate": 0.0023144889855757356
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.05709721014660299,
                "cvrmse_percent": 9.628730050446539,
                "rms_normalized_rmse_percent": 0.8888759467622935,
                "reference_energy": 5.632560560383666,
                "candidate_energy": 5.629344525443869,
                "relative_energy_error_percent": 0.057097210146602996,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.050498306351074e-08,
                  "p90": 2.0575200323946774e-05,
                  "p95": 5.450961762107883e-05,
                  "p99": 0.00016086502000689507,
                  "maximum": 0.0005430616438388824
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05569830909371376,
                  "candidate": 0.05624137073755264
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 196.39383303001523,
            "full": 4220.603417023085
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 193.74050002079457,
            "full": 4147.258750046603
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.7456249129027,
            "full": 4188.176583964378
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.99350001104176,
            "full": 4569.49229107704
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 774.6235829545185,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_overhang100/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2811.8139170110226,
      "worker_pool_size": 12,
      "invocation_count": 3
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
        "identifier": "teaching_overhang100_grid",
        "full_identifier": "teaching_overhang100_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.054825361397700355,
            "cvrmse_percent": 4.192957358379689,
            "rms_normalized_rmse_percent": 0.9257446061562035,
            "reference_energy": 5.150337977747768,
            "candidate_energy": 5.147514286338264,
            "relative_energy_error_percent": 0.05482536139770036,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.612474003806648e-06,
              "p99": 5.642976611852646e-05,
              "maximum": 0.00029316358268260956
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.004271685611456633,
              "candidate": 0.004564849194139242,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9834151816032757,
            "cvrmse_percent": 22.110419985534012,
            "rms_normalized_rmse_percent": 2.0419963940532373,
            "reference_energy": 5.633031733472851,
            "candidate_energy": 5.577635644221349,
            "relative_energy_error_percent": 0.9834151816032757,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4362827844015555e-07,
              "p90": 3.4189855796284974e-05,
              "p95": 5.492454220075158e-05,
              "p99": 0.00013664900325238705,
              "maximum": 0.001782294362783432
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05070004239678383,
              "candidate": 0.0489177480340004,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5399034088613776,
            "cvrmse_percent": 11.539950940308616,
            "rms_normalized_rmse_percent": 2.0402070261136735,
            "reference_energy": 10.783369711220619,
            "candidate_energy": 10.725149930559613,
            "relative_energy_error_percent": 0.5399034088613777,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4635555462282355e-07,
              "p90": 3.36462544510141e-05,
              "p95": 5.5904817418195155e-05,
              "p99": 0.00014090724289417267,
              "maximum": 0.001782294362783432
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05070004239678383,
              "candidate": 0.0489177480340004,
              "position": [
                3.5,
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
        "identifier": "teaching_overhang100_grid",
        "full_identifier": "teaching_overhang100_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.054825361397700355,
            "cvrmse_percent": 4.192957358379689,
            "rms_normalized_rmse_percent": 0.9257446061562035,
            "reference_energy": 5.150337977747768,
            "candidate_energy": 5.147514286338264,
            "relative_energy_error_percent": 0.05482536139770036,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.612474003806648e-06,
              "p99": 5.642976611852646e-05,
              "maximum": 0.00029316358268260956
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.004271685611456633,
              "candidate": 0.004564849194139242,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.48122783113938,
            "cvrmse_percent": 412.1093500526079,
            "rms_normalized_rmse_percent": 29.96182862325711,
            "reference_energy": 3.497361865138771,
            "candidate_energy": 5.577635644221349,
            "relative_energy_error_percent": 59.48122783113938,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023129076907935087,
              "p95": 0.0003278318495176791,
              "p99": 0.0006855390965938568,
              "maximum": 0.012378593906760216
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02101079560816288,
              "candidate": 0.033389389514923096,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.023152114627944,
            "cvrmse_percent": 166.66847536304795,
            "rms_normalized_rmse_percent": 29.96189978245833,
            "reference_energy": 8.647699842886539,
            "candidate_energy": 10.725149930559613,
            "relative_energy_error_percent": 24.02315211462794,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022792999516241252,
              "p95": 0.00032895151155116754,
              "p99": 0.000687113031744957,
              "maximum": 0.012378593906760216
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02101079560816288,
              "candidate": 0.033389389514923096,
              "position": [
                5.5,
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
      "bias_percent": 0.23272189868408238,
      "rms_normalized_error_percent": 0.368472562373907,
      "absolute_error": {
        "p95": 0.12540914536077685,
        "p99": 0.14286406229975646,
        "maximum": 0.1484082261980193
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.569104459049683,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.368472562373907
    },
    "overcast": {
      "bias_percent": 0.1689553522287779,
      "rms_normalized_error_percent": 0.34085346679367573,
      "absolute_error": {
        "p95": 0.06806325912475586,
        "p99": 0.08782439231872557,
        "maximum": 0.09115123748779297
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.94355583190918,
      "reference_fraction_of_uniform": 0.5623518824577332,
      "rms_normalized_to_uniform_percent": 0.20833160694874453
    },
    "horizon": {
      "bias_percent": 1.0801507990891888,
      "rms_normalized_error_percent": 2.0885258747613324,
      "absolute_error": {
        "p95": 0.07825766467113693,
        "p99": 0.10043168174047594,
        "maximum": 0.1110600143797873
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.5992752637629604,
      "reference_fraction_of_uniform": 0.151316061825238,
      "rms_normalized_to_uniform_percent": 0.21545475285790444
    },
    "north": {
      "bias_percent": -98.7568129048926,
      "rms_normalized_error_percent": 99.88841954528401,
      "absolute_error": {
        "p95": 2.000867789320182e-05,
        "p99": 6.029478854543406e-05,
        "maximum": 7.886827370384708e-05
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.335873644682579e-06,
      "reference_fraction_of_uniform": 7.887019819463603e-07,
      "rms_normalized_to_uniform_percent": 9.502386962128277e-05
    },
    "east": {
      "bias_percent": 0.06062877427595392,
      "rms_normalized_error_percent": 0.4334100940545141,
      "absolute_error": {
        "p95": 0.029181450605392456,
        "p99": 0.039959126710891704,
        "maximum": 0.04439067840576172
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2864606380462646,
      "reference_fraction_of_uniform": 0.21633438766002655,
      "rms_normalized_to_uniform_percent": 0.10442233832344003
    },
    "south": {
      "bias_percent": 0.3076429374085622,
      "rms_normalized_error_percent": 0.4305767289681179,
      "absolute_error": {
        "p95": 0.10225695371627808,
        "p99": 0.13172851800918578,
        "maximum": 0.13696503639221191
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.006758689880371,
      "reference_fraction_of_uniform": 0.7575626373291016,
      "rms_normalized_to_uniform_percent": 0.310472534922672
    },
    "west": {
      "bias_percent": 0.15610326934982113,
      "rms_normalized_error_percent": 0.39694267279004497,
      "absolute_error": {
        "p95": 0.030430585145950317,
        "p99": 0.03318106532096863,
        "maximum": 0.03361177444458008
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2250401973724365,
      "reference_fraction_of_uniform": 0.2105230689048767,
      "rms_normalized_to_uniform_percent": 0.0946017209070848
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
        "identifier": "teaching_overhang100_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.06628946094455439,
          "cvrmse_percent": 1.7789620259744818,
          "absolute_error_percentiles_lux": {
            "p50": 2.607452392578125,
            "p90": 21.12000732421875,
            "p95": 32.407336425781224,
            "p99": 66.33572143554682
          },
          "maximum_absolute_error_lux": 297.30810546875,
          "worst": {
            "sensor_index": 29,
            "position": [
              4.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5656.49365234375,
            "radiance_lux": 5953.8017578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3601940639269401,
            "maximum_error_percentage_points": 2.3605479452054823,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13045379580139974,
            "maximum_error_percentage_points": 0.7959355998256257,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10038432267884304,
            "maximum_error_percentage_points": 0.32917808219178113,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10863013698630158,
            "maximum_error_percentage_points": 0.35630136986301153,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03906392694063942,
            "maximum_error_percentage_points": 0.3515068493150686,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 69.44444444444444,
          "radiance_percent": 66.66666666666667,
          "difference_percentage_points": 2.7777777777777715,
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
      "maximum_error_percentage_points": 0.004931506849302991,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004734053938349803,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.007161415996961296,
      "weather_seconds": 0.10343800007831305,
      "metric_reduction_seconds": 0.046785625047050416,
      "write_seconds": 0.04020120808854699,
      "total_seconds": 0.19055429205764085,
      "cold_end_to_end_seconds": 0.19771570805460215,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00951158395037055,
      "engine_upload_seconds": 0.000290833,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.028344208258204162,
      "engine_annual_reduction_seconds": 0.0003309166058897972,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.028344208258204162
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007161415996961296,
      "weather_seconds": 0.1040423329686746,
      "metric_reduction_seconds": 0.012199709075503051,
      "write_seconds": 0.030736958025954664,
      "total_seconds": 0.14715091697871685,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14715091697871685,
      "raw_export_seconds": 0.00976770801935345,
      "engine_upload_seconds": 5.275e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00035241676960140467,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.008357416954822838,
      "full": 0.021849584067240357
    }
  },
  "elapsed_seconds": 44.304576250026,
  "result_class": "passed"
}
```
