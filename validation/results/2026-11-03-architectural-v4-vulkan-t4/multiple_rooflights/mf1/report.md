# Foton report

Status: **passed**

```json
{
  "scene": "multiple_rooflights",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "multiple_rooflights",
    "category": "openings",
    "question": "How do four separated rooflights combine across the workplane?",
    "interactions": [
      "roof_glazing",
      "multiple_openings",
      "punched_roof"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 4,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.0
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "070aee3a8b52580322c24ff502ab658f2645eb8404312a179c2aeb6956e0d417",
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
      "scene_fingerprint": 9669362914231080515,
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
      "scene_fingerprint": 9669362914231080515,
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
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "fcfd891186ba4925b6420263eed28dbc7254f2d162a9c861464a733f0c9743d5",
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
          "maximum": 0.0012363409623503685,
          "p95": 0.00017110169865190982,
          "p99": 0.0004342496395111084
        },
        "bias_percent": 0.055662588455103565,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.4941691066431813,
        "worst_index": [
          13,
          137,
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
          "maximum": 0.0003863181918859482,
          "p95": 7.272375514730809e-05,
          "p99": 0.0001647835597395897
        },
        "bias_percent": 0.010592270153245124,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1451839812904219,
        "worst_index": [
          7,
          145,
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
          "maximum": 0.00025012530386447906,
          "p95": 6.330441974569107e-05,
          "p99": 0.00013283360749483109
        },
        "bias_percent": 0.07120962016667523,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9600593060024347,
        "worst_index": [
          25,
          140,
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007059401832520962,
                  "p50": 0.0,
                  "p90": 4.347553476691246e-05,
                  "p95": 0.00012268536083865893,
                  "p99": 0.00027575530111789703
                },
                "candidate_energy": 12.072576270504214,
                "cvrmse_percent": 7.162649947260427,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02496149186110164,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.075590518048557,
                "relative_energy_error_percent": 0.02496149186110164,
                "rms_normalized_rmse_percent": 1.8571634848911072,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00818826537579298,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.008894205559045076,
                  "rgb_channel": 0,
                  "sky_patch_index": 144
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010763239115476608,
                  "p50": 8.338975021615624e-06,
                  "p90": 8.622169843874872e-05,
                  "p95": 0.00018484284519217905,
                  "p99": 0.0004166205180808902
                },
                "candidate_energy": 1.3599918830989388,
                "cvrmse_percent": 105.24807035091457,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03785364378630795,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3605068845286965,
                "relative_energy_error_percent": 0.03785364378630795,
                "rms_normalized_rmse_percent": 3.0270122962623045,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004721549339592457,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": -0.0006041689775884151,
                  "rgb_channel": 0,
                  "sky_patch_index": 144
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.05695893336087,
            "full": 241.44637503195554
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.45004194322973,
            "full": 244.68004191294312
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.94362501334399,
            "full": 243.88112500309944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.14979208167642,
            "full": 241.14970804657787
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042268959805369377,
                  "p50": 0.0,
                  "p90": 3.5206654501962475e-05,
                  "p95": 9.235544566763552e-05,
                  "p99": 0.0002251151017844677
                },
                "candidate_energy": 12.060008018634107,
                "cvrmse_percent": 5.701242831347866,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02523364537103608,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.06305196638823,
                "relative_energy_error_percent": 0.02523364537103608,
                "rms_normalized_rmse_percent": 1.4786182449437435,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012897204607725143,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.01247451500967145,
                  "rgb_channel": 0,
                  "sky_patch_index": 142
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007420293986797333,
                  "p50": 1.2181189958937466e-05,
                  "p90": 6.516464054584503e-05,
                  "p95": 0.00012256095360498875,
                  "p99": 0.00032034964533522725
                },
                "candidate_energy": 3.7896756731565766,
                "cvrmse_percent": 26.55694453457794,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.29426700497330605,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8008603510749026,
                "relative_energy_error_percent": 0.2942670049733061,
                "rms_normalized_rmse_percent": 2.072181725451534,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005808500573039055,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": -0.0001611793413758278,
                  "rgb_channel": 0,
                  "sky_patch_index": 145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.5080829206854,
            "full": 2341.146165970713
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.67708299588412,
            "full": 2373.0473750038072
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.45175000745803,
            "full": 2346.885957987979
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.67791694309562,
            "full": 2315.4976250370964
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003994246944785118,
                  "p50": 0.0,
                  "p90": 2.3348298782366328e-05,
                  "p95": 8.852910104906186e-05,
                  "p99": 0.00019693141803145409
                },
                "candidate_energy": 12.064545354382062,
                "cvrmse_percent": 5.2677244181920235,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.043898644487517506,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.069843852224949,
                "relative_energy_error_percent": 0.043898644487517506,
                "rms_normalized_rmse_percent": 1.3673068246311382,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01299137994647026,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.012591955251991749,
                  "rgb_channel": 0,
                  "sky_patch_index": 139
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006419597193598747,
                  "p50": 1.2264597899047658e-05,
                  "p90": 6.850344652775675e-05,
                  "p95": 0.00012647061666939404,
                  "p99": 0.00029290933161973953
                },
                "candidate_energy": 3.7932452099109355,
                "cvrmse_percent": 25.9444132154675,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10356335428541898,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7893208621214853,
                "relative_energy_error_percent": 0.10356335428541898,
                "rms_normalized_rmse_percent": 2.0185429080175896,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00022118492051959038,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0008631446398794651,
                  "rgb_channel": 0,
                  "sky_patch_index": 139
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.27883392758667,
            "full": 2493.1975830113515
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.19229192938656,
            "full": 2584.7074170596898
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.52312505617738,
            "full": 2508.691499941051
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.4161250302568,
            "full": 2551.3364580692723
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002881898544728756,
                  "p50": 0.0,
                  "p90": 2.2144788090372458e-05,
                  "p95": 5.6278633019246605e-05,
                  "p99": 0.00012590503320097923
                },
                "candidate_energy": 12.062816187359203,
                "cvrmse_percent": 3.4232692306991734,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.007631618498904174,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.061895669497972,
                "relative_energy_error_percent": 0.007631618498904175,
                "rms_normalized_rmse_percent": 0.8879775653698435,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.011520605068653822,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.011808794923126698,
                  "rgb_channel": 0,
                  "sky_patch_index": 129
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004196641966700554,
                  "p50": 9.068678991752677e-06,
                  "p90": 4.611746408045292e-05,
                  "p95": 8.50186763273086e-05,
                  "p99": 0.000197472982108593
                },
                "candidate_energy": 3.8097121914375656,
                "cvrmse_percent": 17.260522989534454,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12076999396024983,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8051167521657945,
                "relative_energy_error_percent": 0.12076999396024983,
                "rms_normalized_rmse_percent": 1.348521840237135,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006237495690584183,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.00020408537238836288,
                  "rgb_channel": 0,
                  "sky_patch_index": 129
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.74116696603596,
            "full": 4323.050125036389
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.70154197979718,
            "full": 4353.501208941452
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.6220419658348,
            "full": 4424.274750053883
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.55720905214548,
            "full": 4400.048499926925
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/multiple_rooflights/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 795.1836250722408,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2786.7176251020283,
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
        "identifier": "multiple_rooflights_grid",
        "full_identifier": "multiple_rooflights_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.07742571457276608,
            "cvrmse_percent": 7.986109280208777,
            "rms_normalized_rmse_percent": 2.069072020085611,
            "reference_energy": 12.056036345935354,
            "candidate_energy": 12.065370818225347,
            "relative_energy_error_percent": 0.07742571457276609,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.077741712331772e-05,
              "p95": 0.00010056446626549587,
              "p99": 0.00033161602914333344,
              "maximum": 0.0005127545446157455
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 140,
              "rgb_channel": 0,
              "reference": 0.016565946862101555,
              "candidate": 0.01605319231748581,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4076216081186973,
            "cvrmse_percent": 27.828468214569682,
            "rms_normalized_rmse_percent": 2.1790685395264715,
            "reference_energy": 3.8137340398257624,
            "candidate_energy": 3.7981884358032545,
            "relative_energy_error_percent": 0.40762160811869724,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.210201637353748e-05,
              "p90": 8.545350283384323e-05,
              "p95": 0.00012885838314105055,
              "p99": 0.00030272454023361206,
              "maximum": 0.0006470261141657829
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0010002460330724716,
              "candidate": 0.0003532199189066887,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.03913813232035114,
            "cvrmse_percent": 5.2745423174890655,
            "rms_normalized_rmse_percent": 1.7186467051649166,
            "reference_energy": 15.869770385761116,
            "candidate_energy": 15.863559254028601,
            "relative_energy_error_percent": 0.03913813232035114,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.1820098936586874e-05,
              "p90": 7.942412048578262e-05,
              "p95": 0.0001111995370592921,
              "p99": 0.0001882445067167282,
              "maximum": 0.00046731624752283096
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 124,
              "rgb_channel": 0,
              "reference": 0.013497591018676758,
              "candidate": 0.013030274771153927,
              "position": [
                5.5,
                3.5,
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
        "identifier": "multiple_rooflights_grid",
        "full_identifier": "multiple_rooflights_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.07742571457276608,
            "cvrmse_percent": 7.986109280208777,
            "rms_normalized_rmse_percent": 2.069072020085611,
            "reference_energy": 12.056036345935354,
            "candidate_energy": 12.065370818225347,
            "relative_energy_error_percent": 0.07742571457276609,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.077741712331772e-05,
              "p95": 0.00010056446626549587,
              "p99": 0.00033161602914333344,
              "maximum": 0.0005127545446157455
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 140,
              "rgb_channel": 0,
              "reference": 0.016565946862101555,
              "candidate": 0.01605319231748581,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 175.57122531864502,
            "cvrmse_percent": 239.39466487668875,
            "rms_normalized_rmse_percent": 6.976783410099822,
            "reference_energy": 1.3782964572630476,
            "candidate_energy": 3.7981884358032545,
            "relative_energy_error_percent": 175.571225318645,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.00012585932199726813,
              "p90": 0.0003521589587762719,
              "p95": 0.0004051136351336025,
              "p99": 0.0005729459226131439,
              "maximum": 0.0009772256016731262
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 140,
              "rgb_channel": 0,
              "reference": -0.0006423164159059525,
              "candidate": 0.00033490918576717377,
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
            "nmbe_percent": 18.08222623643697,
            "cvrmse_percent": 24.21477070584813,
            "rms_normalized_rmse_percent": 6.878513549058862,
            "reference_energy": 13.434332803198402,
            "candidate_energy": 15.863559254028601,
            "relative_energy_error_percent": 18.08222623643697,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.00012706397092188126,
              "p90": 0.00035106297582387924,
              "p95": 0.0004006547122116899,
              "p99": 0.000536074978299439,
              "maximum": 0.0009818486869335175
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 142,
              "rgb_channel": 0,
              "reference": 0.012439239770174026,
              "candidate": 0.013421088457107544,
              "position": [
                1.5,
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
      "bias_percent": -0.03911137979644042,
      "rms_normalized_error_percent": 0.4541933130275072,
      "absolute_error": {
        "p95": 0.21187041574701126,
        "p99": 0.2589265269871013,
        "maximum": 0.2759218698812944
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.302668232102725,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.4541933130275072
    },
    "overcast": {
      "bias_percent": -0.03639431419993665,
      "rms_normalized_error_percent": 0.4321204555830472,
      "absolute_error": {
        "p95": 0.16861534118652344,
        "p99": 0.2078019142150878,
        "maximum": 0.22574424743652344
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 22.257770538330078,
      "reference_fraction_of_uniform": 0.8462172150611877,
      "rms_normalized_to_uniform_percent": 0.36677482261917294
    },
    "horizon": {
      "bias_percent": 0.8061388456312207,
      "rms_normalized_error_percent": 14.605690130606474,
      "absolute_error": {
        "p95": 0.02387744838324268,
        "p99": 0.033141991362501504,
        "maximum": 0.03720984858976349
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.09170088843214047,
      "reference_fraction_of_uniform": 0.003486372090578188,
      "rms_normalized_to_uniform_percent": 0.05062466391463547
    },
    "north": {
      "bias_percent": -0.02637025010064745,
      "rms_normalized_error_percent": 0.6866794049794582,
      "absolute_error": {
        "p95": 0.06983065605163574,
        "p99": 0.0748967170715332,
        "maximum": 0.07587337493896484
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.746884822845459,
      "reference_fraction_of_uniform": 0.18047161400318146,
      "rms_normalized_to_uniform_percent": 0.14100898480277796
    },
    "east": {
      "bias_percent": -0.05573206284598716,
      "rms_normalized_error_percent": 0.6518629262108165,
      "absolute_error": {
        "p95": 0.08248162269592285,
        "p99": 0.08636345863342285,
        "maximum": 0.0864706039428711
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.879534721374512,
      "reference_fraction_of_uniform": 0.18551482260227203,
      "rms_normalized_to_uniform_percent": 0.13654652164570874
    },
    "south": {
      "bias_percent": -0.0936523955848756,
      "rms_normalized_error_percent": 0.62591528458806,
      "absolute_error": {
        "p95": 0.06325304508209229,
        "p99": 0.06434502601623535,
        "maximum": 0.06455230712890625
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.7296929359436035,
      "reference_fraction_of_uniform": 0.17981798946857452,
      "rms_normalized_to_uniform_percent": 0.12844051038703674
    },
    "west": {
      "bias_percent": -0.06487416856835511,
      "rms_normalized_error_percent": 0.8393965225409219,
      "absolute_error": {
        "p95": 0.09243643283843994,
        "p99": 0.10296928882598876,
        "maximum": 0.10638141632080078
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.733675003051758,
      "reference_fraction_of_uniform": 0.17996938526630402,
      "rms_normalized_to_uniform_percent": 0.17265876885581666
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
        "identifier": "multiple_rooflights_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.04467544582101403,
          "cvrmse_percent": 2.9739564238569205,
          "absolute_error_percentiles_lux": {
            "p50": 5.0079803466796875,
            "p90": 42.47648925781251,
            "p95": 64.00958251953118,
            "p99": 122.12273437499994
          },
          "maximum_absolute_error_lux": 424.57373046875,
          "worst": {
            "sensor_index": 0,
            "position": [
              0.5,
              5.5,
              0.75
            ],
            "hour_of_year": 4449.5,
            "foton_lux": 7062.7861328125,
            "radiance_lux": 7487.35986328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1964954337899546,
            "maximum_error_percentage_points": 0.5190410958904081,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0862003725679467,
            "maximum_error_percentage_points": 0.29066304015245237,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06033485540334856,
            "maximum_error_percentage_points": 0.3310958904109569,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10391171993911602,
            "maximum_error_percentage_points": 0.3523287671232822,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.09842465753424665,
            "maximum_error_percentage_points": 0.3023287671232877,
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
      "maximum_error_percentage_points": 0.00497404751710917,
      "metrics": {
        "da": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.00497404751710917,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "multiple_rooflights_grid",
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
      "study_preparation_seconds": 0.3810212780008442,
      "weather_seconds": 0.23585643799742684,
      "metric_reduction_seconds": 0.16145666900047217,
      "write_seconds": 0.03421044999777223,
      "total_seconds": 0.4319560949988954,
      "cold_end_to_end_seconds": 0.8129773729997396,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.015206893000140553,
      "engine_upload_seconds": 0.014253217,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.011343258,
      "engine_annual_reduction_seconds": 0.006958845,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.011343258
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3810212780008442,
      "weather_seconds": 0.2144792149993009,
      "metric_reduction_seconds": 0.1417603660011082,
      "write_seconds": 0.021227534998615738,
      "total_seconds": 0.37780741499955184,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.37780741499955184,
      "raw_export_seconds": 0.008721816000615945,
      "engine_upload_seconds": 0.013790333,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.006925611,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014629812001658138,
      "full": 0.024060666000877973
    }
  },
  "elapsed_seconds": 2.4879940610007907,
  "result_class": "passed"
}
```
