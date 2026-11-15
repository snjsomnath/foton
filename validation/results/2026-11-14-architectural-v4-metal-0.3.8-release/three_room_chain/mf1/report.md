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
  "model_sha256": "9d36791ff7ebbb2030a91a8f1b9355787b720e7199365792a93ee2b7bb9ebba9",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 1666965602579954223,
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 1666965602579954223,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.8)",
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/52e717d2-b26e-4bbc-9536-f9b0a23834d6/scratchpad/refx/foton-references-corpus4-2026-11-03",
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
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/three_room_chain/mf1/oracle/scene.rad"
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
            "nmbe_percent": -0.26343085725956705,
            "cvrmse_percent": 3.168352977710586,
            "rms_normalized_rmse_percent": 0.7587166214327794,
            "reference_energy": 5.71215346402505,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.26343085725956705,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
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
            "nmbe_percent": -0.592709141223506,
            "cvrmse_percent": 16.49985707248041,
            "rms_normalized_rmse_percent": 1.4112527643935888,
            "reference_energy": 3.037059342737079,
            "candidate_energy": 3.0190584143882937,
            "relative_energy_error_percent": 0.5927091412235059,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.469169413023337e-07,
              "p90": 4.25481703132391e-05,
              "p95": 6.491552630905062e-05,
              "p99": 0.00017260480672121048,
              "maximum": 0.000886622816324234
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036607641726732254,
              "candidate": 0.03572101891040802,
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
            "nmbe_percent": -0.3777311618424205,
            "cvrmse_percent": 5.6140157921782325,
            "rms_normalized_rmse_percent": 1.3832922872050293,
            "reference_energy": 8.749212806762129,
            "candidate_energy": 8.71616430357508,
            "relative_energy_error_percent": 0.3777311618424205,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.301990254087286e-07,
              "p90": 4.051392897963524e-05,
              "p95": 6.106108776293695e-05,
              "p99": 0.00017082880367524922,
              "maximum": 0.000886622816324234
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036607641726732254,
              "candidate": 0.03572101891040802,
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
            "nmbe_percent": -0.9758117611384617,
            "cvrmse_percent": 17.90931156727025,
            "rms_normalized_rmse_percent": 1.7162786696063175,
            "reference_energy": 0.12372082157116893,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9758117611384617,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
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
            "nmbe_percent": 0.22506269380453064,
            "cvrmse_percent": 52.474452094415255,
            "rms_normalized_rmse_percent": 4.525320046505741,
            "reference_energy": 0.20269852248508258,
            "candidate_energy": 0.2031547212400895,
            "relative_energy_error_percent": 0.22506269380453064,
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
            "nmbe_percent": -0.23009775202913674,
            "cvrmse_percent": 32.169950985168704,
            "rms_normalized_rmse_percent": 4.467628890608246,
            "reference_energy": 0.3264193440562515,
            "candidate_energy": 0.3256682604833898,
            "relative_energy_error_percent": 0.23009775202913674,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.8898449855319086e-08,
              "p90": 7.261289283633232e-06,
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
            "nmbe_percent": 0.05168759564710006,
            "cvrmse_percent": 26.751297627439904,
            "rms_normalized_rmse_percent": 1.7007929457656985,
            "reference_energy": 0.012266576708498178,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.05168759564710006,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 6.311172981088889,
            "cvrmse_percent": 151.24583427650103,
            "rms_normalized_rmse_percent": 12.039967983366914,
            "reference_energy": 0.027096154598689637,
            "candidate_energy": 0.028806239786636212,
            "relative_energy_error_percent": 6.31117298108889,
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
            "nmbe_percent": 4.360534519620537,
            "cvrmse_percent": 103.21019461468968,
            "rms_normalized_rmse_percent": 11.935539965788738,
            "reference_energy": 0.039362731307187815,
            "candidate_energy": 0.04107915679370322,
            "relative_energy_error_percent": 4.360534519620537,
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
            "nmbe_percent": -0.26343085725956705,
            "cvrmse_percent": 3.168352977710586,
            "rms_normalized_rmse_percent": 0.7587166214327794,
            "reference_energy": 5.71215346402505,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.26343085725956705,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
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
            "nmbe_percent": 78.27080775925712,
            "cvrmse_percent": 440.8359521743366,
            "rms_normalized_rmse_percent": 24.75258930252214,
            "reference_energy": 1.6935237195230144,
            "candidate_energy": 3.0190584143882937,
            "relative_energy_error_percent": 78.27080775925712,
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
            "nmbe_percent": 17.695709488097897,
            "cvrmse_percent": 100.7852846462252,
            "rms_normalized_rmse_percent": 24.746526583227816,
            "reference_energy": 7.405677183548065,
            "candidate_energy": 8.71616430357508,
            "relative_energy_error_percent": 17.6957094880979,
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
            "nmbe_percent": -0.9758117611384617,
            "cvrmse_percent": 17.90931156727025,
            "rms_normalized_rmse_percent": 1.7162786696063175,
            "reference_energy": 0.12372082157116893,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9758117611384617,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
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
            "nmbe_percent": 135.4789126589497,
            "cvrmse_percent": 855.1985577494439,
            "rms_normalized_rmse_percent": 40.86498474606756,
            "reference_energy": 0.08627299954213896,
            "candidate_energy": 0.2031547212400895,
            "relative_energy_error_percent": 135.4789126589497,
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
            "nmbe_percent": 55.08468713832615,
            "cvrmse_percent": 351.24851017001515,
            "rms_normalized_rmse_percent": 40.85361487625322,
            "reference_energy": 0.2099938211133079,
            "candidate_energy": 0.3256682604833898,
            "relative_energy_error_percent": 55.084687138326146,
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
            "nmbe_percent": 0.05168759564710006,
            "cvrmse_percent": 26.751297627439904,
            "rms_normalized_rmse_percent": 1.7007929457656985,
            "reference_energy": 0.012266576708498178,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.05168759564710006,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 147.46905705818432,
            "cvrmse_percent": 1130.956743051285,
            "rms_normalized_rmse_percent": 49.469789795570065,
            "reference_energy": 0.011640340060722565,
            "candidate_energy": 0.028806239786636212,
            "relative_energy_error_percent": 147.46905705818432,
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
            "nmbe_percent": 71.82958886020421,
            "cvrmse_percent": 549.5464953668675,
            "rms_normalized_rmse_percent": 49.36923695423591,
            "reference_energy": 0.023906916769220743,
            "candidate_energy": 0.04107915679370322,
            "relative_energy_error_percent": 71.82958886020421,
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
      "bias_percent": -0.14597432677220346,
      "rms_normalized_error_percent": 0.2735947450595933,
      "absolute_error": {
        "p95": 0.10111218880177147,
        "p99": 0.13985584578882063,
        "maximum": 0.1565990112914264
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.708120836975041,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2735947450595933
    },
    "overcast": {
      "bias_percent": -0.13700025056902473,
      "rms_normalized_error_percent": 0.23422975060456352,
      "absolute_error": {
        "p95": 0.05608161687850953,
        "p99": 0.09507478713989266,
        "maximum": 0.10405731201171875
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.679072141647339,
      "reference_fraction_of_uniform": 0.6445329785346985,
      "rms_normalized_to_uniform_percent": 0.1652256352126455
    },
    "horizon": {
      "bias_percent": -0.4872777902861951,
      "rms_normalized_error_percent": 2.0819563907122363,
      "absolute_error": {
        "p95": 0.038688998595584057,
        "p99": 0.047982603592523446,
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
      "rms_normalized_to_uniform_percent": 0.11090100521131054
    },
    "north": {
      "bias_percent": -43.671379822724575,
      "rms_normalized_error_percent": 115.7972901233924,
      "absolute_error": {
        "p95": 4.886485426141011e-05,
        "p99": 8.221710158977667e-05,
        "maximum": 9.344917634734884e-05
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
      "bias_percent": 0.024111533770588296,
      "rms_normalized_error_percent": 0.32880836020951015,
      "absolute_error": {
        "p95": 0.023908144235610974,
        "p99": 0.03533921480178834,
        "maximum": 0.03635978698730469
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1663968563079834,
      "reference_fraction_of_uniform": 0.2043399065732956,
      "rms_normalized_to_uniform_percent": 0.07058770289466854
    },
    "south": {
      "bias_percent": -0.19612751731717165,
      "rms_normalized_error_percent": 0.3534891959387208,
      "absolute_error": {
        "p95": 0.08965225219726566,
        "p99": 0.11120517730712896,
        "maximum": 0.11719894409179688
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9009029865264893,
      "reference_fraction_of_uniform": 0.6833953261375427,
      "rms_normalized_to_uniform_percent": 0.23010343441871628
    },
    "west": {
      "bias_percent": -0.07082168132293543,
      "rms_normalized_error_percent": 0.3856836830460828,
      "absolute_error": {
        "p95": 0.02903908789157869,
        "p99": 0.0463793754577638,
        "maximum": 0.060916900634765625
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1303037405014038,
      "reference_fraction_of_uniform": 0.19801679253578186,
      "rms_normalized_to_uniform_percent": 0.07933130236158105
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
          "nmbe_percent": -0.19947957513899914,
          "cvrmse_percent": 1.554857527244437,
          "absolute_error_percentiles_lux": {
            "p50": 2.9668731689453125,
            "p90": 28.643786621093827,
            "p95": 44.465423583984354,
            "p99": 91.69357910156245
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
          "nmbe_percent": -0.5680397637773117,
          "cvrmse_percent": 9.943867632536966,
          "absolute_error_percentiles_lux": {
            "p50": 0.4755210876464844,
            "p90": 5.2125925064086935,
            "p95": 8.151696014404287,
            "p99": 16.056361923217768
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
            "mean_absolute_error_percentage_points": 0.25844168155239156,
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
          "nmbe_percent": 3.856763212614678,
          "cvrmse_percent": 26.1002588414847,
          "absolute_error_percentiles_lux": {
            "p50": 0.10750171542167664,
            "p90": 0.9653019428253176,
            "p95": 1.6732381820678708,
            "p99": 4.191096954345699
          },
          "maximum_absolute_error_lux": 42.43170166015625,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              11.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 334.171875,
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
            "maximum_error_percentage_points": 0.004983721171339939,
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
      "study_preparation_seconds": 0.013472583144903183,
      "weather_seconds": 0.0747636251617223,
      "metric_reduction_seconds": 0.05633212486281991,
      "write_seconds": 0.03461470897309482,
      "total_seconds": 0.16584237501956522,
      "cold_end_to_end_seconds": 0.1793149581644684,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010299792047590017,
      "engine_upload_seconds": 0.000301834,
      "engine_acceleration_structure_seconds": 0.003075333,
      "engine_tracing_seconds": 0.0331454579718411,
      "engine_annual_reduction_seconds": 0.0006346667651087046,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0331454579718411
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.013472583144903183,
      "weather_seconds": 0.0739121250808239,
      "metric_reduction_seconds": 0.013925333973020315,
      "write_seconds": 0.014201583107933402,
      "total_seconds": 0.10219595790840685,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.10219595790840685,
      "raw_export_seconds": 0.002991250017657876,
      "engine_upload_seconds": 3.8333e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006148749962449074,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022075457964092493,
      "full": 0.035946834133937955
    }
  },
  "elapsed_seconds": 0.9174817919265479,
  "result_class": "unstable_reference"
}
```
