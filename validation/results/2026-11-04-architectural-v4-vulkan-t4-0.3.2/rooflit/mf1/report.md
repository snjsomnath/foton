# Foton report

Status: **passed**

```json
{
  "scene": "rooflit",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "rooflit",
    "category": "openings",
    "question": "How does a roof opening illuminate the workplane?",
    "interactions": [
      "roof_glazing",
      "zenith_sky"
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
    "aperture_area": 7.200000000000003
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "a7290e9a289b73adf6ccf467340d4d7151a966cd84ed9239b90edf93292c104b",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11178068536730648043,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11178068536730648043,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "a39e81d7129668a92127cb23718f3f106a9f08857afb024976ec3e654e6ebf10",
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
          "maximum": 0.0009158235043287277,
          "p95": 0.0001386985532008105,
          "p99": 0.0004294893005862832
        },
        "bias_percent": 0.18648998907411177,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.517225772056373,
        "worst_index": [
          5,
          111,
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
          "maximum": 0.0003097616136074066,
          "p95": 8.628484793007364e-05,
          "p99": 0.00017111189663410187
        },
        "bias_percent": 0.06329484801900587,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7061830816490274,
        "worst_index": [
          15,
          143,
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
          "maximum": 0.00033317599445581436,
          "p95": 7.292139343917363e-05,
          "p99": 0.00014218036085367203
        },
        "bias_percent": 0.0019157431818606718,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5991640212350081,
        "worst_index": [
          12,
          73,
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007472652941942215,
                  "p50": 0.0,
                  "p90": 7.820152677595615e-05,
                  "p95": 0.00017806830583140252,
                  "p99": 0.000356065109372139
                },
                "candidate_energy": 25.526043616471725,
                "cvrmse_percent": 4.617113373448798,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.02554477372659461,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.519524711628037,
                "relative_energy_error_percent": 0.025544773726594614,
                "rms_normalized_rmse_percent": 1.4197219836414363,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.024393455125391483,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.023646189831197262,
                  "rgb_channel": 0,
                  "sky_patch_index": 127
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013123797252774239,
                  "p50": 8.296737917135033e-06,
                  "p90": 0.0001028347760438919,
                  "p95": 0.00024803609121590807,
                  "p99": 0.0005569653585553169
                },
                "candidate_energy": 1.8916295925772602,
                "cvrmse_percent": 95.08780856780326,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21707351177260611,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8875322600146056,
                "relative_energy_error_percent": 0.21707351177260611,
                "rms_normalized_rmse_percent": 2.1227286767705427,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00036745984107255936,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": -0.0009449198842048645,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.04937495477498,
            "full": 250.95854210667312
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.85054189246148,
            "full": 237.4744579428807
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.06458300817758,
            "full": 283.57541700825095
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.11595892813057,
            "full": 246.1596670327708
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004285350441932678,
                  "p50": 0.0,
                  "p90": 4.4579035602509975e-05,
                  "p95": 0.00010562213137745817,
                  "p99": 0.0002200254239141941
                },
                "candidate_energy": 25.51443477297107,
                "cvrmse_percent": 2.8237466556350834,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0010597926922832162,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.51416437572152,
                "relative_energy_error_percent": 0.001059792692283216,
                "rms_normalized_rmse_percent": 0.8684598685143584,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013057045172899961,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.01348558021709323,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006425902247428894,
                  "p50": 1.4913232007529587e-05,
                  "p90": 8.239921589847654e-05,
                  "p95": 0.0001532454189145935,
                  "p99": 0.0003438028506934643
                },
                "candidate_energy": 5.8389044540126065,
                "cvrmse_percent": 19.5859252897452,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1310004325693785,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.8465634774585205,
                "relative_energy_error_percent": 0.1310004325693785,
                "rms_normalized_rmse_percent": 1.3076896380015097,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009668748825788498,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.0003242846578359604,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.01354103256017,
            "full": 2363.702292088419
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.81416700966656,
            "full": 2267.5489159300923
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.18241694010794,
            "full": 2322.8675411082804
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.43825002759695,
            "full": 2473.5744590871036
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039219949394464493,
                  "p50": 0.0,
                  "p90": 4.387553781270981e-05,
                  "p95": 0.00010242227290291339,
                  "p99": 0.00023172050714492798
                },
                "candidate_energy": 25.505109901196192,
                "cvrmse_percent": 2.851037291740308,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.029039659609301403,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.512518649769845,
                "relative_energy_error_percent": 0.029039659609301403,
                "rms_normalized_rmse_percent": 0.8767182421510453,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.009178346488624811,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.009570545982569456,
                  "rgb_channel": 0,
                  "sky_patch_index": 63
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006460603326559067,
                  "p50": 1.416876239090925e-05,
                  "p90": 7.825484499335289e-05,
                  "p95": 0.00016004247590899464,
                  "p99": 0.0003412701189517975
                },
                "candidate_energy": 5.868926032782838,
                "cvrmse_percent": 19.231057893535638,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.029292866734727724,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.867207359549955,
                "relative_energy_error_percent": 0.029292866734727724,
                "rms_normalized_rmse_percent": 1.2880396073550793,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009073000401258469,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0002612397074699402,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.26845892705023,
            "full": 2535.831707995385
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.6775000402704,
            "full": 2429.302291944623
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.2694160155952,
            "full": 2425.7042080862448
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.11237503681332,
            "full": 2466.5268340613693
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003169253468513489,
                  "p50": 0.0,
                  "p90": 2.4475157260894775e-05,
                  "p95": 7.684403681196272e-05,
                  "p99": 0.00015100790187716484
                },
                "candidate_energy": 25.510571016173344,
                "cvrmse_percent": 1.9467488957360546,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.004837351343412231,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.51180511182065,
                "relative_energy_error_percent": 0.004837351343412232,
                "rms_normalized_rmse_percent": 0.5987326005551677,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.019672419875860214,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.019989345222711563,
                  "rgb_channel": 0,
                  "sky_patch_index": 111
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00047356076538562775,
                  "p50": 1.0161900718230754e-05,
                  "p90": 5.514817894436419e-05,
                  "p95": 0.00011198001448065033,
                  "p99": 0.00022272951900959015
                },
                "candidate_energy": 5.864643457863615,
                "cvrmse_percent": 13.297173954255207,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05625673717887032,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.867944572019297,
                "relative_energy_error_percent": 0.056256737178870315,
                "rms_normalized_rmse_percent": 0.8908957794760366,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.000830015167593956,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.00035645440220832825,
                  "rgb_channel": 0,
                  "sky_patch_index": 111
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 263.45604204107076,
            "full": 4414.6352499956265
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 266.55979198403656,
            "full": 4334.535917034373
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 264.76912503130734,
            "full": 4279.383791028522
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 259.0284999459982,
            "full": 4329.518832964823
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
    "/content/suite-vulkan-0.3.2/rooflit/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 960.63787501771,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2850.709999911487,
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
        "identifier": "rooflit_grid",
        "full_identifier": "rooflit_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0017421096464339991,
            "cvrmse_percent": 2.5553524028639134,
            "rms_normalized_rmse_percent": 0.7859704125178881,
            "reference_energy": 25.510494979055238,
            "candidate_energy": 25.510050558261355,
            "relative_energy_error_percent": 0.0017421096464339991,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2381933629512787e-05,
              "p95": 7.31535255908966e-05,
              "p99": 0.00020339293405413628,
              "maximum": 0.0004570791497826576
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 99,
              "rgb_channel": 0,
              "reference": 0.008959486149251461,
              "candidate": 0.009416565299034119,
              "position": [
                5.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.23270946734404424,
            "cvrmse_percent": 16.019311291336006,
            "rms_normalized_rmse_percent": 1.0731999808361958,
            "reference_energy": 5.866987077430519,
            "candidate_energy": 5.880640111807551,
            "relative_energy_error_percent": 0.23270946734404424,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4705783289391547e-05,
              "p90": 8.700770558789372e-05,
              "p95": 0.0001253765076398849,
              "p99": 0.00023192167282104492,
              "maximum": 0.0005057230591773987
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 99,
              "rgb_channel": 0,
              "reference": 0.001673293299973011,
              "candidate": 0.0011675702407956123,
              "position": [
                5.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.042095836623764565,
            "cvrmse_percent": 2.7335761877506446,
            "rms_normalized_rmse_percent": 0.9794244837716742,
            "reference_energy": 31.377482056485757,
            "candidate_energy": 31.390690670068906,
            "relative_energy_error_percent": 0.042095836623764565,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.445969221298583e-05,
              "p90": 8.177972631528974e-05,
              "p95": 0.00011244666820857671,
              "p99": 0.00019571464508771896,
              "maximum": 0.000439593568444252
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 140,
              "rgb_channel": 0,
              "reference": 0.0185464546084404,
              "candidate": 0.018106861039996147,
              "position": [
                3.5,
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
        "identifier": "rooflit_grid",
        "full_identifier": "rooflit_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0017421096464339991,
            "cvrmse_percent": 2.5553524028639134,
            "rms_normalized_rmse_percent": 0.7859704125178881,
            "reference_energy": 25.510494979055238,
            "candidate_energy": 25.510050558261355,
            "relative_energy_error_percent": 0.0017421096464339991,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2381933629512787e-05,
              "p95": 7.31535255908966e-05,
              "p99": 0.00020339293405413628,
              "maximum": 0.0004570791497826576
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 99,
              "rgb_channel": 0,
              "reference": 0.008959486149251461,
              "candidate": 0.009416565299034119,
              "position": [
                5.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 209.2030525141034,
            "cvrmse_percent": 283.8476762324371,
            "rms_normalized_rmse_percent": 6.383406644868117,
            "reference_energy": 1.9018700054842839,
            "candidate_energy": 5.880640111807551,
            "relative_energy_error_percent": 209.2030525141034,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.00020386558026075363,
              "p90": 0.0005873050540685654,
              "p95": 0.0007259000503609051,
              "p99": 0.0009664390236139297,
              "maximum": 0.0014947913587093353
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 116,
              "rgb_channel": 0,
              "reference": -0.0004858612082898617,
              "candidate": 0.0010089301504194736,
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
            "nmbe_percent": 14.51288747896486,
            "cvrmse_percent": 19.630464838455843,
            "rms_normalized_rmse_percent": 6.363022050072518,
            "reference_energy": 27.412364984539522,
            "candidate_energy": 31.390690670068906,
            "relative_energy_error_percent": 14.512887478964862,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.00020444735491764732,
              "p90": 0.0005847057327628136,
              "p95": 0.0007189823506678288,
              "p99": 0.0009512510150671005,
              "maximum": 0.0012774905189871788
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 116,
              "rgb_channel": 0,
              "reference": 0.004334382712841034,
              "candidate": 0.005611873231828213,
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
      "bias_percent": 0.042152614210748215,
      "rms_normalized_error_percent": 0.17198725926780423,
      "absolute_error": {
        "p95": 0.16792085687496972,
        "p99": 0.23234164907541754,
        "maximum": 0.2665675276968358
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 52.00524222546168,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17198725926780423
    },
    "overcast": {
      "bias_percent": 0.018990063060044804,
      "rms_normalized_error_percent": 0.1531155651846907,
      "absolute_error": {
        "p95": 0.1363229751586914,
        "p99": 0.1795326232910156,
        "maximum": 0.18828582763671875
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 43.92042922973633,
      "reference_fraction_of_uniform": 0.8445385098457336,
      "rms_normalized_to_uniform_percent": 0.13307946011466198
    },
    "horizon": {
      "bias_percent": -1.7932045581206457,
      "rms_normalized_error_percent": 8.256235843985845,
      "absolute_error": {
        "p95": 0.02467250628399046,
        "p99": 0.03458269385199603,
        "maximum": 0.03778099484908537
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.16574454647875603,
      "reference_fraction_of_uniform": 0.003187073829215005,
      "rms_normalized_to_uniform_percent": 0.024132343670027798
    },
    "north": {
      "bias_percent": 0.005061602215740769,
      "rms_normalized_error_percent": 0.2662612126954533,
      "absolute_error": {
        "p95": 0.057497620582580566,
        "p99": 0.07680854797363278,
        "maximum": 0.08565521240234375
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.656062126159668,
      "reference_fraction_of_uniform": 0.185674786567688,
      "rms_normalized_to_uniform_percent": 0.05985073264594192
    },
    "east": {
      "bias_percent": 0.10274036715166517,
      "rms_normalized_error_percent": 0.3252744077394646,
      "absolute_error": {
        "p95": 0.08884143829345703,
        "p99": 0.10952014923095701,
        "maximum": 0.11346817016601562
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.854778289794922,
      "reference_fraction_of_uniform": 0.18949586153030396,
      "rms_normalized_to_uniform_percent": 0.07395743851014583
    },
    "south": {
      "bias_percent": 0.12873303669607225,
      "rms_normalized_error_percent": 0.33778737933852854,
      "absolute_error": {
        "p95": 0.07745170593261719,
        "p99": 0.15571393966674799,
        "maximum": 0.1715240478515625
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.506037712097168,
      "reference_fraction_of_uniform": 0.18278999626636505,
      "rms_normalized_to_uniform_percent": 0.07516743610225228
    },
    "west": {
      "bias_percent": 0.08102527229841314,
      "rms_normalized_error_percent": 0.2885717541268512,
      "absolute_error": {
        "p95": 0.07338428497314453,
        "p99": 0.10250425338745112,
        "maximum": 0.1175079345703125
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.589581489562988,
      "reference_fraction_of_uniform": 0.18439644575119019,
      "rms_normalized_to_uniform_percent": 0.06466862442228713
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
        "identifier": "rooflit_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.18924030087285776,
          "cvrmse_percent": 1.5575844635756677,
          "absolute_error_percentiles_lux": {
            "p50": 5.47601318359375,
            "p90": 43.64722900390625,
            "p95": 67.7924011230468,
            "p99": 136.20078613281248
          },
          "maximum_absolute_error_lux": 402.328125,
          "worst": {
            "sensor_index": 30,
            "position": [
              5.5,
              5.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 30067.81640625,
            "radiance_lux": 30470.14453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0601560121765604,
            "maximum_error_percentage_points": 0.2486301369863,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02593275044425288,
            "maximum_error_percentage_points": 0.12328786440635042,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.025015220700152312,
            "maximum_error_percentage_points": 0.08589041095890515,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06350076103500789,
            "maximum_error_percentage_points": 0.3524657534246529,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0611111111111111,
            "maximum_error_percentage_points": 0.35493150684931507,
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
      "maximum_error_percentage_points": 0.004960937500001705,
      "metrics": {
        "da": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004960937500001705,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
      "study_preparation_seconds": 0.3590283379999164,
      "weather_seconds": 0.23504908800009616,
      "metric_reduction_seconds": 0.15498936400013008,
      "write_seconds": 0.011883588000046075,
      "total_seconds": 0.40223534599999766,
      "cold_end_to_end_seconds": 0.7612636839999141,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015562179999051295,
      "engine_upload_seconds": 0.014061066,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.011547493,
      "engine_annual_reduction_seconds": 0.00590243,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.011547493
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3590283379999164,
      "weather_seconds": 0.23428363099992566,
      "metric_reduction_seconds": 0.15300581899987264,
      "write_seconds": 0.015703604999998788,
      "total_seconds": 0.4032440329999645,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4032440329999645,
      "raw_export_seconds": 0.0018088840001837525,
      "engine_upload_seconds": 0.014076599,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.7e-08,
      "engine_annual_reduction_seconds": 0.006079252,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01360636100002921,
      "full": 0.020045942000024297
    }
  },
  "elapsed_seconds": 2.780260673000157,
  "result_class": "passed"
}
```
