# Foton report

Status: **incomplete**

```json
{
  "scene": "three_room_chain",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "three_room_chain",
    "category": "connections",
    "question": "Can daylight cross two successive internal glass partitions?",
    "interactions": [
      "borrowed_light",
      "serial_glazing",
      "paired_apertures"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 14.999999999999996
  },
  "sky_density": 1,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "50bcb10356a2a941b332aed1323063d28f0a420934b3adf95b89c931da67e28e",
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
      "scene_fingerprint": 1666965602579954223,
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
      "scene_fingerprint": 1666965602579954223,
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "c73e78d0633e70c94d7b9a9722cc6b7d5c69587d8d1b9d2393006289ce4d078c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "e75d8c9643462ce1ef94674e2df8fd73709d93c53864d1bdf54a08ec7317fa65",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00023132911883294582,
          "p95": 4.789326339960098e-06,
          "p99": 4.62816096842289e-05
        },
        "bias_percent": -0.019300813276599976,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5180704613284904,
        "worst_index": [
          6,
          96,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 4.955328768119216e-05,
          "p95": 0.0,
          "p99": 5.24311326444149e-06
        },
        "bias_percent": 0.24048792996254612,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.652445237982848,
        "worst_index": [
          13,
          17,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 1.2653428711928427e-05,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": -0.918852422372638,
        "identifier": "three_room_chain_2_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.176845067875099,
        "worst_index": [
          4,
          15,
          0
        ]
      }
    ],
    "passed": true,
    "samples_per_patch": [
      1024,
      4096
    ]
  },
  "depth_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0004716217517852783,
          "p95": 4.8947054892778397e-05,
          "p99": 0.00014189444482326508
        },
        "bias_percent": 0.08010434150210882,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.881270245562517,
        "worst_index": [
          5,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 7.731537334620953e-05,
          "p95": 5.917565431445837e-06,
          "p99": 2.313348522875458e-05
        },
        "bias_percent": -0.04231561075330841,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.3624928964343335,
        "worst_index": [
          15,
          16,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 3.0160881578922272e-05,
          "p95": 1.0132789611816406e-06,
          "p99": 5.918538590776734e-06
        },
        "bias_percent": 1.2936950478748501,
        "identifier": "three_room_chain_2_grid",
        "passed": false,
        "rms_normalized_error_percent": 5.225585696233691,
        "worst_index": [
          15,
          17,
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
          "maximum": 0.0004068668931722641,
          "p95": 4.9881404265761375e-05,
          "p99": 0.00012614205479621887
        },
        "bias_percent": -0.017087724953374406,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8423337560997106,
        "worst_index": [
          16,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00014224974438548088,
          "p95": 5.7669312809593976e-06,
          "p99": 2.1141371689736843e-05
        },
        "bias_percent": 0.43262215182147784,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.658585161983034,
        "worst_index": [
          11,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 5.520592094399035e-05,
          "p95": 9.304951618105406e-07,
          "p99": 6.390182534232736e-06
        },
        "bias_percent": -1.6464047516649734,
        "identifier": "three_room_chain_2_grid",
        "passed": false,
        "rms_normalized_error_percent": 6.555501275194602,
        "worst_index": [
          10,
          16,
          0
        ]
      }
    ],
    "passed": false
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008306666277348995,
                  "p50": 0.0,
                  "p90": 1.506195985712111e-07,
                  "p95": 0.00014107977040112019,
                  "p99": 0.0004028300754725933
                },
                "candidate_energy": 5.717993184356374,
                "cvrmse_percent": 13.99431544059375,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.22664489546442734,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.705062950396268,
                "relative_energy_error_percent": 0.22664489546442737,
                "rms_normalized_rmse_percent": 3.346402105121552,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006274124141782522,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.005443457514047623,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012726886197924614,
                  "p50": 0.0,
                  "p90": 4.2934203520417213e-05,
                  "p95": 0.0002165352925658226,
                  "p99": 0.0005853446200489998
                },
                "candidate_energy": 1.6885736681808794,
                "cvrmse_percent": 71.16341805621704,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6560380128966175,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.699724507061724,
                "relative_energy_error_percent": 0.6560380128966175,
                "rms_normalized_rmse_percent": 4.01116692570185,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0007470441050827503,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0005256445147097111,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "three_room_chain_1_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00028110359562560916,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.817924541886896e-05
                },
                "candidate_energy": 0.12424544898203749,
                "cvrmse_percent": 93.92116699485223,
                "energy_difference_negligible": true,
                "nmbe_percent": -1.5918436513235694,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.126255234923633,
                "relative_energy_error_percent": 1.5918436513235694,
                "rms_normalized_rmse_percent": 8.931159741790074,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.000988196930848062,
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "reference": 0.0012693005264736712,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00045444408897310495,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.101031526535735e-07,
                  "p99": 7.755849219392985e-05
                },
                "candidate_energy": 0.08544986856814418,
                "cvrmse_percent": 275.37872012386055,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.6811395506444586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.08403708784713615,
                "relative_energy_error_percent": 1.6811395506444584,
                "rms_normalized_rmse_percent": 12.746890797159482,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00040804455056786537,
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "reference": -4.639953840523958e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              }
            },
            "start_sensor_index": 24
          },
          {
            "identifier": "three_room_chain_2_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 8.542750583728775e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012170573058028822,
                "cvrmse_percent": 278.71251578935613,
                "energy_difference_negligible": true,
                "nmbe_percent": -3.6209578942195173,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012627821144633344,
                "relative_energy_error_percent": 3.6209578942195177,
                "rms_normalized_rmse_percent": 18.024243527959555,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0003577010502340272,
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "reference": 0.00027227354439673945,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00015861322754062712,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.1797967090387829e-05
                },
                "candidate_energy": 0.01120914566627107,
                "cvrmse_percent": 461.299763574984,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -5.05787664726618,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.011806293424285741,
                "relative_energy_error_percent": 5.0578766472661805,
                "rms_normalized_rmse_percent": 19.94851357886928,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00011872555478475988,
                  "global_sensor_index": 60,
                  "local_sensor_index": 12,
                  "reference": 0.000277338782325387,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              }
            },
            "start_sensor_index": 48
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.011167046614,
            "full": 403.9766669739038
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.16412509046495,
            "full": 415.0082500418648
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.73091704025865,
            "full": 407.708290964365
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.88891698420048,
            "full": 413.67204196285456
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003507320361677557,
                  "p50": 0.0,
                  "p90": 2.976739779114723e-07,
                  "p95": 4.625716246664524e-05,
                  "p99": 0.00014252850087359548
                },
                "candidate_energy": 5.71158300515566,
                "cvrmse_percent": 4.970370194563832,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04705107323796807,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.708896907890448,
                "relative_energy_error_percent": 0.04705107323796806,
                "rms_normalized_rmse_percent": 1.1888186473467186,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019537847547326237,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0023045167909003794,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006082868203520775,
                  "p50": 1.7972298493873495e-07,
                  "p90": 2.67185278062243e-05,
                  "p95": 8.227000944316387e-05,
                  "p99": 0.0002287011593580246
                },
                "candidate_energy": 3.0335604355934933,
                "cvrmse_percent": 15.445162226092462,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.006352131435398797,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0333677520869617,
                "relative_energy_error_percent": 0.0063521314353987965,
                "rms_normalized_rmse_percent": 1.321118942930364,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028504706919193268,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.02789642009884119,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "three_room_chain_1_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00011877674842253327,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3758644854533486e-05
                },
                "candidate_energy": 0.12416889527048625,
                "cvrmse_percent": 47.9786393229709,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.6392146693589059,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.12338023073652948,
                "relative_energy_error_percent": 0.6392146693589059,
                "rms_normalized_rmse_percent": 4.548506679596031,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0012662069930229336,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.0011474302446004003,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0001764455810189247,
                  "p50": 2.5000000292152436e-08,
                  "p90": 3.84901113648084e-06,
                  "p95": 6.806442456763762e-06,
                  "p99": 4.17162027588347e-05
                },
                "candidate_energy": 0.20056182359025776,
                "cvrmse_percent": 50.434168120285904,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.8056457966334626,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.20219076498957733,
                "relative_energy_error_percent": 0.8056457966334625,
                "rms_normalized_rmse_percent": 4.346844149999434,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0053303660824894905,
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "reference": 0.005506811663508415,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 24
          },
          {
            "identifier": "three_room_chain_2_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 6.281109199335333e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012322722041062661,
                "cvrmse_percent": 131.16834080796227,
                "energy_difference_negligible": true,
                "nmbe_percent": -2.7053725203565864,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012665367410590989,
                "relative_energy_error_percent": 2.7053725203565864,
                "rms_normalized_rmse_percent": 8.3490601276775,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.000171898373082513,
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "reference": 0.00010908728108915966,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 5.598487769020721e-05,
                  "p50": 0.0,
                  "p90": 5.988550064728315e-07,
                  "p95": 1.1800626680269488e-06,
                  "p99": 7.562494829471689e-06
                },
                "candidate_energy": 0.027136334207567003,
                "cvrmse_percent": 92.29766615733503,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8913703488058211,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.026896586014988344,
                "relative_energy_error_percent": 0.8913703488058211,
                "rms_normalized_rmse_percent": 7.2479515098203455,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 6.330032192636281e-05,
                  "global_sensor_index": 62,
                  "local_sensor_index": 14,
                  "reference": 0.00011928519961657003,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              }
            },
            "start_sensor_index": 48
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.72766596544534,
            "full": 5149.986374890432
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.81862491741776,
            "full": 5132.796666002832
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.7900840882212,
            "full": 5525.0996249960735
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.26287497766316,
            "full": 5281.003957963549
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.66916694305837,
            "full": 5212.2364999959245
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.17770796082914,
            "full": 5203.666000044905
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.99020796827972,
            "full": 5245.727499946952
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.39975008089095,
            "full": 5205.336416955106
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003594520385377109,
                  "p50": 0.0,
                  "p90": 8.321367204189301e-07,
                  "p95": 6.46479893475771e-05,
                  "p99": 0.0001661553978919983
                },
                "candidate_energy": 5.71423549409144,
                "cvrmse_percent": 6.0539761136005605,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08701626320232558,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.709267502854232,
                "relative_energy_error_percent": 0.0870162632023256,
                "rms_normalized_rmse_percent": 1.448027475436841,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001807424530852586,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0014479724923148751,
                  "rgb_channel": 0,
                  "sky_patch_index": 12
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006549600511789322,
                  "p50": 2.9998996353697294e-07,
                  "p90": 3.899770672433078e-05,
                  "p95": 0.00010641082189977169,
                  "p99": 0.00030080555006861687
                },
                "candidate_energy": 3.038321812631896,
                "cvrmse_percent": 20.091003554907026,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.041768287551182476,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0395913979073548,
                "relative_energy_error_percent": 0.04176828755118247,
                "rms_normalized_rmse_percent": 1.7188096509067627,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036769924685359,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.03611496463418007,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "three_room_chain_1_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00013963400851935148,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.650998067110777e-05
                },
                "candidate_energy": 0.12382383253020635,
                "cvrmse_percent": 60.87281519048047,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.44534206670256943,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.1232748378197357,
                "relative_energy_error_percent": 0.44534206670256943,
                "rms_normalized_rmse_percent": 5.785979050604221,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001173530996311456,
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "reference": 0.0010338969877921045,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002236948348581791,
                  "p50": 2.5445645590593813e-08,
                  "p90": 5.205549769016216e-06,
                  "p95": 9.958058399206493e-06,
                  "p99": 6.339844549074769e-05
                },
                "candidate_energy": 0.2015740618887989,
                "cvrmse_percent": 65.37035226224958,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10939333200955845,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.2013537942641257,
                "relative_energy_error_percent": 0.10939333200955845,
                "rms_normalized_rmse_percent": 5.631459266420192,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.005403236951678991,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.005179542116820812,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 24
          },
          {
            "identifier": "three_room_chain_2_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 4.184364661341533e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012045680318806262,
                "cvrmse_percent": 133.40366081177848,
                "energy_difference_negligible": true,
                "nmbe_percent": -2.446822763755348,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012347809328275616,
                "relative_energy_error_percent": 2.4468227637553475,
                "rms_normalized_rmse_percent": 8.54572453776226,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0001764976477716118,
                  "global_sensor_index": 62,
                  "local_sensor_index": 14,
                  "reference": 0.00013465400115819648,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 7.796093268552795e-05,
                  "p50": 0.0,
                  "p90": 6.744192724283948e-07,
                  "p95": 1.6517847143404651e-06,
                  "p99": 8.404886102653109e-06
                },
                "candidate_energy": 0.02782345787872842,
                "cvrmse_percent": 114.24306217898692,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.010400919646058727,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.027826352075248195,
                "relative_energy_error_percent": 0.010400919646058727,
                "rms_normalized_rmse_percent": 9.069313910613882,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00010961754014715552,
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "reference": 3.165660746162757e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              }
            },
            "start_sensor_index": 48
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.95033406466246,
            "full": 5473.354208050296
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.18604108132422,
            "full": 5489.349292009138
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.50066691916436,
            "full": 5549.858333077282
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.3137080129236,
            "full": 5433.054458000697
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018290395382791758,
                  "p50": 0.0,
                  "p90": 1.9040089682675898e-07,
                  "p95": 3.4190481528639793e-05,
                  "p99": 9.486149065196514e-05
                },
                "candidate_energy": 5.710305102631082,
                "cvrmse_percent": 3.4176273782769044,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02375574081038332,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.708948899527513,
                "relative_energy_error_percent": 0.02375574081038332,
                "rms_normalized_rmse_percent": 0.8174930390368991,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015086860512383282,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0016915900050662458,
                  "rgb_channel": 0,
                  "sky_patch_index": 12
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000680951401591301,
                  "p50": 2.0053721350166143e-07,
                  "p90": 2.4780849344097078e-05,
                  "p95": 5.8379024267196655e-05,
                  "p99": 0.0001781596802175045
                },
                "candidate_energy": 3.0416889487734515,
                "cvrmse_percent": 12.326393210188192,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1384796607027753,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.037482653101531,
                "relative_energy_error_percent": 0.1384796607027753,
                "rms_normalized_rmse_percent": 1.0546912332964224,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.035090046003460884,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.03440909460186958,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "three_room_chain_1_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 7.210200419649482e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.966292858123779e-06
                },
                "candidate_energy": 0.12378214781892893,
                "cvrmse_percent": 29.636479318678635,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05012507228476515,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.12384422482614355,
                "relative_energy_error_percent": 0.05012507228476514,
                "rms_normalized_rmse_percent": 2.8209325495676465,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0011942404671572149,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.0012663424713537097,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002015059581026435,
                  "p50": 2.5698199124235543e-08,
                  "p90": 3.8044014445404173e-06,
                  "p95": 6.753206434950698e-06,
                  "p99": 2.951553324237466e-05
                },
                "candidate_energy": 0.20261124236655803,
                "cvrmse_percent": 39.81694394658455,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.00501865996423562,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.2026010745075446,
                "relative_energy_error_percent": 0.00501865996423562,
                "rms_normalized_rmse_percent": 3.4398727289228646,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0027368415612727404,
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "reference": 0.002535335603170097,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 24
          },
          {
            "identifier": "three_room_chain_2_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 4.584704583976418e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.01229951858658751,
                "cvrmse_percent": 130.54101214980437,
                "energy_difference_negligible": true,
                "nmbe_percent": -2.378306371125149,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012599165338542662,
                "relative_energy_error_percent": 2.378306371125149,
                "rms_normalized_rmse_percent": 8.31317664580127,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0003258877550251782,
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "reference": 0.00037173480086494237,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 9.10552334971726e-05,
                  "p50": 0.0,
                  "p90": 6.003550083732989e-07,
                  "p95": 1.1790053164872916e-06,
                  "p99": 6.145157385617495e-06
                },
                "candidate_energy": 0.027367947192225017,
                "cvrmse_percent": 116.10394436914939,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 3.4359613533041404,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.026458831951824635,
                "relative_energy_error_percent": 3.435961353304141,
                "rms_normalized_rmse_percent": 9.15157484338905,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0001042175863403827,
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "reference": 1.3162352843210101e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              }
            },
            "start_sensor_index": 48
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 335.891459020786,
            "full": 9405.519417021424
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 325.703207985498,
            "full": 9476.718250080012
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 329.89241706673056,
            "full": 9472.549833008088
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 334.4675420084968,
            "full": 9378.470208961517
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
    "/content/suite-vulkan/three_room_chain/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3078.362499945797,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 9996.397959068418,
      "invocation_count": 5,
      "sample_count": 1024,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 41786.604833905585,
      "invocation_count": 5,
      "sample_count": 4096,
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2634327468942186,
            "cvrmse_percent": 3.1683522413792518,
            "rms_normalized_rmse_percent": 0.7587164451055753,
            "reference_energy": 5.71215346402505,
            "candidate_energy": 5.697105781247956,
            "relative_energy_error_percent": 0.2634327468942186,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.166496753692627e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5943178462987071,
            "cvrmse_percent": 16.529295667305313,
            "rms_normalized_rmse_percent": 1.4137706830727632,
            "reference_energy": 3.037059342737079,
            "candidate_energy": 3.01900955706051,
            "relative_energy_error_percent": 0.594317846298707,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.469169413023337e-07,
              "p90": 4.25481703132391e-05,
              "p95": 6.491552630905062e-05,
              "p99": 0.00017260480672121048,
              "maximum": 0.0009022429585456848
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036607641726732254,
              "candidate": 0.03570539876818657,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3782908152386305,
            "cvrmse_percent": 5.6244423111999176,
            "rms_normalized_rmse_percent": 1.3858613792558905,
            "reference_energy": 8.749212806762129,
            "candidate_energy": 8.716115338308466,
            "relative_energy_error_percent": 0.3782908152386305,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.301990254087286e-07,
              "p90": 4.051392897963524e-05,
              "p95": 6.106108776293695e-05,
              "p99": 0.00017082880367524922,
              "maximum": 0.0009022429585456848
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036607641726732254,
              "candidate": 0.03570539876818657,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.9758179140806724,
            "cvrmse_percent": 17.909309886256455,
            "rms_normalized_rmse_percent": 1.7162785085120114,
            "reference_energy": 0.12372082157116893,
            "candidate_energy": 0.12251353163082968,
            "relative_energy_error_percent": 0.9758179140806724,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045360689517111e-06,
              "maximum": 4.2092018702533096e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.2092018702533096e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.22072608660295417,
            "cvrmse_percent": 52.4737041118732,
            "rms_normalized_rmse_percent": 4.525255541584643,
            "reference_energy": 0.20269852248508258,
            "candidate_energy": 0.2031459310013659,
            "relative_energy_error_percent": 0.22072608660295417,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 7.638775969098788e-06,
              "p95": 1.2331547623034567e-05,
              "p99": 3.393382212379947e-05,
              "maximum": 0.0002704731887206435
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001727383234538138,
              "candidate": 0.0014569100458174944,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2327930123911314,
            "cvrmse_percent": 32.16948182715567,
            "rms_normalized_rmse_percent": 4.46756373589619,
            "reference_energy": 0.3264193440562515,
            "candidate_energy": 0.3256594626321956,
            "relative_energy_error_percent": 0.23279301239113137,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.8898449855319086e-08,
              "p90": 7.261405698955059e-06,
              "p95": 1.1445052223280072e-05,
              "p99": 2.7821333787869662e-05,
              "maximum": 0.0002704731887206435
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001727383234538138,
              "candidate": 0.0014569100458174944,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0516752284056226,
            "cvrmse_percent": 26.751324229299385,
            "rms_normalized_rmse_percent": 1.7007946370576719,
            "reference_energy": 0.012266576708498178,
            "candidate_energy": 0.012272915490029845,
            "relative_energy_error_percent": 0.0516752284056226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907285518944263e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211801438592374,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 6.311172215796563,
            "cvrmse_percent": 151.24582177942182,
            "rms_normalized_rmse_percent": 12.039966988533344,
            "reference_energy": 0.027096154598689637,
            "candidate_energy": 0.02880623957927142,
            "relative_energy_error_percent": 6.311172215796563,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.715634637861513e-07,
              "p95": 1.943715346897079e-06,
              "p99": 1.376273576170206e-05,
              "maximum": 0.00010907431715168059
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003036556881852448,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 4.360530138822007,
            "cvrmse_percent": 103.21017048692197,
            "rms_normalized_rmse_percent": 11.935537175580496,
            "reference_energy": 0.039362731307187815,
            "candidate_energy": 0.041079155069301265,
            "relative_energy_error_percent": 4.360530138822007,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.715634637861513e-07,
              "p95": 1.927355697262101e-06,
              "p99": 1.3434328138828278e-05,
              "maximum": 0.00010907431715168059
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003036556881852448,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2634327468942186,
            "cvrmse_percent": 3.1683522413792518,
            "rms_normalized_rmse_percent": 0.7587164451055753,
            "reference_energy": 5.71215346402505,
            "candidate_energy": 5.697105781247956,
            "relative_energy_error_percent": 0.2634327468942186,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.166496753692627e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 78.2679228083574,
            "cvrmse_percent": 440.80725540627105,
            "rms_normalized_rmse_percent": 24.750978001740673,
            "reference_energy": 1.6935237195230144,
            "candidate_energy": 3.01900955706051,
            "relative_energy_error_percent": 78.2679228083574,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.2393035098721157e-07,
              "p90": 0.00023758504539728165,
              "p95": 0.00031462498009204865,
              "p99": 0.0005798088386654854,
              "maximum": 0.01018228754401207
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014360843226313591,
              "candidate": 0.02454313077032566,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.69504830255873,
            "cvrmse_percent": 100.77872008505634,
            "rms_normalized_rmse_percent": 24.744914739911177,
            "reference_energy": 7.405677183548065,
            "candidate_energy": 8.716115338308466,
            "relative_energy_error_percent": 17.69504830255874,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023861462250351906,
              "p95": 0.0003110090037807822,
              "p99": 0.0006260639056563377,
              "maximum": 0.01018228754401207
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014360843226313591,
              "candidate": 0.02454313077032566,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.9758179140806724,
            "cvrmse_percent": 17.909309886256455,
            "rms_normalized_rmse_percent": 1.7162785085120114,
            "reference_energy": 0.12372082157116893,
            "candidate_energy": 0.12251353163082968,
            "relative_energy_error_percent": 0.9758179140806724,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045360689517111e-06,
              "maximum": 4.2092018702533096e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.2092018702533096e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 135.46872379479726,
            "cvrmse_percent": 855.1972187481052,
            "rms_normalized_rmse_percent": 40.86492076295068,
            "reference_energy": 0.08627299954213896,
            "candidate_energy": 0.2031459310013659,
            "relative_energy_error_percent": 135.46872379479728,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.995999991777353e-05,
              "p95": 3.6457338865147904e-05,
              "p99": 9.949310015144874e-05,
              "maximum": 0.0017298401799052954
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003533219685778022,
              "candidate": 0.005263059865683317,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 55.080497562105485,
            "cvrmse_percent": 351.24795707509435,
            "rms_normalized_rmse_percent": 40.85355054593941,
            "reference_energy": 0.2099938211133079,
            "candidate_energy": 0.3256594626321956,
            "relative_energy_error_percent": 55.08049756210548,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9639999663922936e-05,
              "p95": 3.601999924285337e-05,
              "p99": 9.949310015144874e-05,
              "maximum": 0.0017298401799052954
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003533219685778022,
              "candidate": 0.005263059865683317,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0516752284056226,
            "cvrmse_percent": 26.751324229299385,
            "rms_normalized_rmse_percent": 1.7007946370576719,
            "reference_energy": 0.012266576708498178,
            "candidate_energy": 0.012272915490029845,
            "relative_energy_error_percent": 0.0516752284056226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907285518944263e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211801438592374,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 147.4690552767519,
            "cvrmse_percent": 1130.9567262363885,
            "rms_normalized_rmse_percent": 49.4697890600606,
            "reference_energy": 0.011640340060722565,
            "candidate_energy": 0.02880623957927142,
            "relative_energy_error_percent": 147.4690552767519,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.400000185953104e-07,
              "p95": 2.9999998787388904e-06,
              "p99": 5.8899170198856154e-05,
              "maximum": 0.00024599260359536856
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00016673740174155682,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 71.82958164722075,
            "cvrmse_percent": 549.5464581671464,
            "rms_normalized_rmse_percent": 49.369233612349724,
            "reference_energy": 0.023906916769220743,
            "candidate_energy": 0.041079155069301265,
            "relative_energy_error_percent": 71.82958164722075,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.400000185953104e-07,
              "p95": 3.0199998946045525e-06,
              "p99": 5.8899170198856154e-05,
              "maximum": 0.00024599260359536856
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00016673740174155682,
              "candidate": 0.0004127300053369254,
              "position": [
                2.5,
                10.5,
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
      "bias_percent": -0.14611500217393822,
      "rms_normalized_error_percent": 0.2735848807852255,
      "absolute_error": {
        "p95": 0.10111240122262838,
        "p99": 0.13985660831587957,
        "maximum": 0.15659959997461215
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.708120836975041,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2735848807852255
    },
    "overcast": {
      "bias_percent": -0.13720348889554163,
      "rms_normalized_error_percent": 0.2342321766288568,
      "absolute_error": {
        "p95": 0.05608239173889161,
        "p99": 0.09507724761962899,
        "maximum": 0.10406112670898438
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.679072141647339,
      "reference_fraction_of_uniform": 0.6445329785346985,
      "rms_normalized_to_uniform_percent": 0.16522734503349942
    },
    "horizon": {
      "bias_percent": -0.48728165769758575,
      "rms_normalized_error_percent": 2.081957687979459,
      "absolute_error": {
        "p95": 0.0386890449608969,
        "p99": 0.04798266277341708,
        "maximum": 0.059364350904623775
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5018686292502754,
      "reference_fraction_of_uniform": 0.08792186493308986,
      "rms_normalized_to_uniform_percent": 0.1109010743137373
    },
    "north": {
      "bias_percent": -43.6713818429528,
      "rms_normalized_error_percent": 115.79728878883385,
      "absolute_error": {
        "p95": 4.886485639872266e-05,
        "p99": 8.221710106226975e-05,
        "maximum": 9.344917452835944e-05
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 7.907853614597116e-06,
      "reference_fraction_of_uniform": 1.3853690461473889e-06,
      "rms_normalized_to_uniform_percent": 0.00013351473018227987
    },
    "east": {
      "bias_percent": 0.024013297211614732,
      "rms_normalized_error_percent": 0.32879716625404143,
      "absolute_error": {
        "p95": 0.023909179866313947,
        "p99": 0.035337991714477546,
        "maximum": 0.03635907173156738
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1663968563079834,
      "reference_fraction_of_uniform": 0.2043399065732956,
      "rms_normalized_to_uniform_percent": 0.07058530422512528
    },
    "south": {
      "bias_percent": -0.1962158233897376,
      "rms_normalized_error_percent": 0.353478991919073,
      "absolute_error": {
        "p95": 0.089643406867981,
        "p99": 0.11120531558990483,
        "maximum": 0.11719942092895508
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9009034633636475,
      "reference_fraction_of_uniform": 0.6833953857421875,
      "rms_normalized_to_uniform_percent": 0.23009679194921187
    },
    "west": {
      "bias_percent": -0.07081165069160261,
      "rms_normalized_error_percent": 0.3856825203502021,
      "absolute_error": {
        "p95": 0.029039046168327348,
        "p99": 0.046379237174987924,
        "maximum": 0.06091642379760742
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1303037405014038,
      "reference_fraction_of_uniform": 0.19801679253578186,
      "rms_normalized_to_uniform_percent": 0.07933106249462672
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
        "identifier": "three_room_chain_0_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.19956646798251648,
          "cvrmse_percent": 1.5549381898171661,
          "absolute_error_percentiles_lux": {
            "p50": 2.9674606323242188,
            "p90": 28.65577392578125,
            "p95": 44.46540527343748,
            "p99": 91.72516357421871
          },
          "maximum_absolute_error_lux": 395.66259765625,
          "worst": {
            "sensor_index": 14,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4964.70556640625,
            "radiance_lux": 5360.3681640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.25442922374429094,
            "maximum_error_percentage_points": 0.9315068493150704,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08714205167293976,
            "maximum_error_percentage_points": 0.4817034645547267,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08577054794520562,
            "maximum_error_percentage_points": 0.3587671232876737,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10340753424657508,
            "maximum_error_percentage_points": 0.3272602739726125,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.055707762557077524,
            "maximum_error_percentage_points": 0.30506849315068507,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.5697433931995596,
          "cvrmse_percent": 9.945085648503982,
          "absolute_error_percentiles_lux": {
            "p50": 0.4755821228027344,
            "p90": 5.215610122680666,
            "p95": 8.154434204101559,
            "p99": 16.05636337280273
          },
          "maximum_absolute_error_lux": 59.298583984375,
          "worst": {
            "sensor_index": 10,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1115.5,
            "foton_lux": 1318.1224365234375,
            "radiance_lux": 1258.8238525390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.03230022831050227,
            "maximum_error_percentage_points": 0.3027397260273972,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2580250148857249,
            "maximum_error_percentage_points": 0.6715712990064411,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.26105022831050356,
            "maximum_error_percentage_points": 1.810136986301373,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2611586757990871,
            "maximum_error_percentage_points": 1.8101369863013694,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00010844748858447491,
            "maximum_error_percentage_points": 0.002191780821917802,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 3.8567570506151676,
          "cvrmse_percent": 26.10024851999503,
          "absolute_error_percentiles_lux": {
            "p50": 0.10750168561935425,
            "p90": 0.9653016805648806,
            "p95": 1.6732345581054684,
            "p99": 4.191096954345699
          },
          "maximum_absolute_error_lux": 42.431671142578125,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              11.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 334.1718444824219,
            "radiance_lux": 291.74017333984375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.005416666666666667,
            "maximum_error_percentage_points": 0.08,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10992231857562036,
            "maximum_error_percentage_points": 0.4089773543959887,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.04249429223744391,
            "maximum_error_percentage_points": 0.2510958904109515,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.042494292237442936,
            "maximum_error_percentage_points": 0.2510958904109589,
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
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049893982769688705,
      "metrics": {
        "da": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0049893982769688705,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004983668915213069,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.002191780821917816,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
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
      "study_preparation_seconds": 0.4902401539998209,
      "weather_seconds": 0.4227299630001653,
      "metric_reduction_seconds": 0.1289953250002327,
      "write_seconds": 0.01481719699995665,
      "total_seconds": 0.5670657629998459,
      "cold_end_to_end_seconds": 1.0573059169996668,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002968485000110377,
      "engine_upload_seconds": 0.025341916,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024268934,
      "engine_annual_reduction_seconds": 0.007984908,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024268934
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.4902401539998209,
      "weather_seconds": 0.22806644599995707,
      "metric_reduction_seconds": 0.10650639699997555,
      "write_seconds": 0.015257730000030278,
      "total_seconds": 0.3501421070000106,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3501421070000106,
      "raw_export_seconds": 0.0029893179998907726,
      "engine_upload_seconds": 0.024664434,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 9.4e-08,
      "engine_annual_reduction_seconds": 0.008386794,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02678349200004959,
      "full": 0.0460545330001878
    }
  },
  "elapsed_seconds": 3.6061814159997994,
  "result_class": "unstable_reference"
}
```
