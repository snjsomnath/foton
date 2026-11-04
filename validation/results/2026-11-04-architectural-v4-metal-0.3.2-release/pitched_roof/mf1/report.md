# Foton report

Status: **passed**

```json
{
  "scene": "pitched_roof",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "pitched_roof",
    "category": "form",
    "question": "Do sloped roof surfaces reflect light correctly beneath a ridge?",
    "interactions": [
      "sloped_faces",
      "nonrectangular_faces"
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
    "sensors": 48,
    "floor_area": 48.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0d75be8491d10e87fd9248dea80b4253aa3b02f7178c1beabbc7f41f7cb4313e",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6830033420663156906,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6830033420663156906,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "02bc0c5c87ab1f537b19ea1df748f9f82be10c6b33f79c93824c331d658546b9",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "0b7a9221d18bfb07725467e90f9170b3321a19be933b8beff4de56e3927db8d9",
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
          "p95": 1.178821548819542e-06,
          "p99": 7.012346759438515e-05
        },
        "bias_percent": -0.06250238241035028,
        "identifier": "pitched_roof_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.089180333425455,
        "worst_index": [
          13,
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
          "maximum": 0.0003752857446670532,
          "p95": 3.275985363870859e-05,
          "p99": 0.00013777520507574081
        },
        "bias_percent": 0.14365191675761285,
        "identifier": "pitched_roof_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2035525790048034,
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
          "maximum": 0.00029702670872211456,
          "p95": 3.079860471189022e-05,
          "p99": 0.00010978244245052338
        },
        "bias_percent": -0.08507752282275413,
        "identifier": "pitched_roof_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9785998089693343,
        "worst_index": [
          27,
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
            "identifier": "pitched_roof_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007471146527677774,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.135924973525107e-05,
                  "p99": 0.00022559473291039467
                },
                "candidate_energy": 6.139354342938532,
                "cvrmse_percent": 13.327700422299616,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03827353972108828,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.141704990837752,
                "relative_energy_error_percent": 0.03827353972108828,
                "rms_normalized_rmse_percent": 2.4026515757448927,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004028484225273132,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.003281369572505355,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011813498567789793,
                  "p50": 0.0,
                  "p90": 1.0581665628706107e-05,
                  "p95": 7.388414815068245e-05,
                  "p99": 0.0003684554249048233
                },
                "candidate_energy": 1.8665138568275523,
                "cvrmse_percent": 77.67335600108399,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8205619317130677,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.851322608270884,
                "relative_energy_error_percent": 0.8205619317130676,
                "rms_normalized_rmse_percent": 3.628608269535904,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009939438896253705,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": -0.0001874059671536088,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.8390829116106,
            "full": 279.2967080604285
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.35695794131607,
            "full": 281.973332981579
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.73745897132903,
            "full": 277.61245891451836
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.12479097675532,
            "full": 267.6309170201421
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
            "identifier": "pitched_roof_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039630208630114794,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3397034965455532e-05,
                  "p99": 0.00015977304428815842
                },
                "candidate_energy": 6.145593313825884,
                "cvrmse_percent": 9.709356830471325,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09998071687821786,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.151743871449071,
                "relative_energy_error_percent": 0.09998071687821787,
                "rms_normalized_rmse_percent": 1.7535330983912596,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018896080437116325,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.0014933059574104846,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000797715038061142,
                  "p50": 1.833625162817043e-07,
                  "p90": 2.254892206110531e-05,
                  "p95": 6.0410937294363976e-05,
                  "p99": 0.00024183932691812515
                },
                "candidate_energy": 3.6011227542152078,
                "cvrmse_percent": 27.036840160757336,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21609842759538408,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.5933575650193212,
                "relative_energy_error_percent": 0.21609842759538408,
                "rms_normalized_rmse_percent": 2.1178495648929796,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020936469547450542,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.021734184585511684,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.3564589014277,
            "full": 3114.977457909845
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.30720790755004,
            "full": 3114.804834011011
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.95745894219726,
            "full": 3069.6165000554174
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.56591604743153,
            "full": 3103.385000023991
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
            "identifier": "pitched_roof_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004160605021752417,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3503656848333776e-05,
                  "p99": 0.00015712704043835402
                },
                "candidate_energy": 6.146812161487105,
                "cvrmse_percent": 9.701467582218594,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.055487841447641524,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.150224788466403,
                "relative_energy_error_percent": 0.05548784144764152,
                "rms_normalized_rmse_percent": 1.7526141243563313,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019404769991524518,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.0023565375013276935,
                  "rgb_channel": 0,
                  "sky_patch_index": 18
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006960804457776248,
                  "p50": 1.8129367163055576e-07,
                  "p90": 2.3796249661245396e-05,
                  "p95": 5.607644561678171e-05,
                  "p99": 0.00023332983255386353
                },
                "candidate_energy": 3.615841390635559,
                "cvrmse_percent": 26.725770069169112,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.24679490658074726,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6069396473025748,
                "relative_energy_error_percent": 0.24679490658074726,
                "rms_normalized_rmse_percent": 2.1005517792247943,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006102594779804349,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": -8.582096779718995e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.36537500843406,
            "full": 3321.0046249441803
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.70716706477106,
            "full": 3275.4232499282807
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.84020802937448,
            "full": 3328.1582499621436
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.21908297482878,
            "full": 3288.8194581028074
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
            "identifier": "pitched_roof_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021968083456158638,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.19796022772789e-05,
                  "p99": 8.096056990325451e-05
                },
                "candidate_energy": 6.1445019725024395,
                "cvrmse_percent": 5.050140117048877,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.027986903913906125,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.142782797783184,
                "relative_energy_error_percent": 0.027986903913906125,
                "rms_normalized_rmse_percent": 0.9113632741734672,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007488827686756849,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007708508521318436,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00035915058106184006,
                  "p50": 1.5488735272128906e-07,
                  "p90": 1.5394405272672886e-05,
                  "p95": 3.1525036320090294e-05,
                  "p99": 0.00013651512563228607
                },
                "candidate_energy": 3.607335655094989,
                "cvrmse_percent": 15.247928492451843,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03477574408602481,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.608590569316487,
                "relative_energy_error_percent": 0.0347757440860248,
                "rms_normalized_rmse_percent": 1.1991732245907103,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01843005046248436,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.01807089988142252,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.13866700138897,
            "full": 5796.944124973379
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 227.72249998524785,
            "full": 5795.396749977954
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.41108290757984,
            "full": 5846.672249957919
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 242.43920797016472,
            "full": 5733.6362089263275
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/pitched_roof/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1320.0679590227082,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/pitched_roof/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4716.986916959286,
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
      48,
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
        "identifier": "pitched_roof_grid",
        "full_identifier": "pitched_roof_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.042071536505037824,
            "cvrmse_percent": 3.928366845422273,
            "rms_normalized_rmse_percent": 0.7092652098958904,
            "reference_energy": 6.1476106401287325,
            "candidate_energy": 6.145024245874083,
            "relative_energy_error_percent": 0.042071536505037824,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.443595677614212e-07,
              "p99": 4.457496106624603e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
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
            "nmbe_percent": -0.6731909010206031,
            "cvrmse_percent": 22.66588242690385,
            "rms_normalized_rmse_percent": 1.7803417278886056,
            "reference_energy": 3.60399483189115,
            "candidate_energy": 3.579733066609606,
            "relative_energy_error_percent": 0.6731909010206031,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.9468480395044025e-07,
              "p90": 3.1964314621291165e-05,
              "p95": 4.864035872742534e-05,
              "p99": 0.00011373322922736406,
              "maximum": 0.0008114296942949295
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02134642004966736,
              "candidate": 0.02053499035537243,
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
            "nmbe_percent": -0.27532040352974,
            "cvrmse_percent": 8.270788320387444,
            "rms_normalized_rmse_percent": 1.7578005985039202,
            "reference_energy": 9.751605472019882,
            "candidate_energy": 9.724757312483689,
            "relative_energy_error_percent": 0.27532040352974,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.9104422455693566e-07,
              "p90": 3.1180169025901704e-05,
              "p95": 4.7850568080320954e-05,
              "p99": 0.00011042464757338166,
              "maximum": 0.0008114296942949295
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02134642004966736,
              "candidate": 0.02053499035537243,
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
      48,
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
        "identifier": "pitched_roof_grid",
        "full_identifier": "pitched_roof_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.042071536505037824,
            "cvrmse_percent": 3.928366845422273,
            "rms_normalized_rmse_percent": 0.7092652098958904,
            "reference_energy": 6.1476106401287325,
            "candidate_energy": 6.145024245874083,
            "relative_energy_error_percent": 0.042071536505037824,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.443595677614212e-07,
              "p99": 4.457496106624603e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
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
            "nmbe_percent": 93.3071082711084,
            "cvrmse_percent": 528.4028914377488,
            "rms_normalized_rmse_percent": 24.666547235338744,
            "reference_energy": 1.8518372648713566,
            "candidate_energy": 3.579733066609606,
            "relative_energy_error_percent": 93.3071082711084,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00016257938041235333,
              "p95": 0.00021865102462470531,
              "p99": 0.0004165181890130043,
              "maximum": 0.006522621028125286
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010092529468238354,
              "candidate": 0.01661515049636364,
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
            "nmbe_percent": 21.56785603172924,
            "cvrmse_percent": 122.29892320621153,
            "rms_normalized_rmse_percent": 24.661699709823836,
            "reference_energy": 7.999447905000089,
            "candidate_energy": 9.724757312483689,
            "relative_energy_error_percent": 21.56785603172924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00016214940114878123,
              "p95": 0.00021674999152310193,
              "p99": 0.00039134733378887177,
              "maximum": 0.006522621028125286
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010092529468238354,
              "candidate": 0.01661515049636364,
              "position": [
                1.5,
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
      "bias_percent": 0.10759498264980606,
      "rms_normalized_error_percent": 0.2673520549103225,
      "absolute_error": {
        "p95": 0.09276877060272906,
        "p99": 0.0959693026347023,
        "maximum": 0.09755300365987019
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.125000023395392,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2673520549103225
    },
    "overcast": {
      "bias_percent": 0.10153366662269006,
      "rms_normalized_error_percent": 0.22134626817220135,
      "absolute_error": {
        "p95": 0.055883169174194336,
        "p99": 0.06452008247375489,
        "maximum": 0.06871414184570312
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.793516159057617,
      "reference_fraction_of_uniform": 0.6349058747291565,
      "rms_normalized_to_uniform_percent": 0.1564490723750933
    },
    "horizon": {
      "bias_percent": 0.40596434591858166,
      "rms_normalized_error_percent": 2.374153629807012,
      "absolute_error": {
        "p95": 0.04444361491843402,
        "p99": 0.06352841580680609,
        "maximum": 0.07457241330756181
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9056765927007158,
      "reference_fraction_of_uniform": 0.09925222908259407,
      "rms_normalized_to_uniform_percent": 0.131113375939912
    },
    "north": {
      "bias_percent": -75.67785168124473,
      "rms_normalized_error_percent": 105.53749847019496,
      "absolute_error": {
        "p95": 4.3518007078091604e-05,
        "p99": 0.00010644122800158596,
        "maximum": 0.0001518107164883986
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2824846635339782e-05,
      "reference_fraction_of_uniform": 1.405462626280496e-06,
      "rms_normalized_to_uniform_percent": 0.00015080954272680752
    },
    "east": {
      "bias_percent": 0.1278003101233571,
      "rms_normalized_error_percent": 0.40991516547592816,
      "absolute_error": {
        "p95": 0.03250328972935675,
        "p99": 0.040107569694519056,
        "maximum": 0.04453134536743164
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8482555150985718,
      "reference_fraction_of_uniform": 0.202548548579216,
      "rms_normalized_to_uniform_percent": 0.0875523637891234
    },
    "south": {
      "bias_percent": 0.12045734679570724,
      "rms_normalized_error_percent": 0.3082490249102854,
      "absolute_error": {
        "p95": 0.0737370491027832,
        "p99": 0.08089142084121705,
        "maximum": 0.08110511302947998
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.340223789215088,
      "reference_fraction_of_uniform": 0.6948190331459045,
      "rms_normalized_to_uniform_percent": 0.20056914581026794
    },
    "west": {
      "bias_percent": -0.0375144243260942,
      "rms_normalized_error_percent": 0.3673812608494174,
      "absolute_error": {
        "p95": 0.025415438413619994,
        "p99": 0.03369192957878114,
        "maximum": 0.03715240955352783
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7844163179397583,
      "reference_fraction_of_uniform": 0.19555246829986572,
      "rms_normalized_to_uniform_percent": 0.07515119249609611
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
        "identifier": "pitched_roof_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.029180652097110234,
          "cvrmse_percent": 1.8950936849916675,
          "absolute_error_percentiles_lux": {
            "p50": 2.2592010498046875,
            "p90": 21.042309570312504,
            "p95": 31.994143676757798,
            "p99": 61.01291015624997
          },
          "maximum_absolute_error_lux": 276.93603515625,
          "worst": {
            "sensor_index": 30,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4748.79345703125,
            "radiance_lux": 5025.7294921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6801541095890414,
            "maximum_error_percentage_points": 1.8882191780821902,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.23747261033848988,
            "maximum_error_percentage_points": 0.791537471035177,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.22316780821917773,
            "maximum_error_percentage_points": 0.928082191780824,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22736301369863007,
            "maximum_error_percentage_points": 0.928082191780824,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.020910388127854035,
            "maximum_error_percentage_points": 0.1661643835616431,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 39.583333333333336,
          "radiance_percent": 37.5,
          "difference_percentage_points": 2.0833333333333357,
          "tolerance_percentage_points": 2.0833333333333335,
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
      "maximum_error_percentage_points": 0.0049422089041044615,
      "metrics": {
        "da": [
          {
            "identifier": "pitched_roof_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "pitched_roof_grid",
            "maximum_error_percentage_points": 0.0049422089041044615,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "pitched_roof_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "pitched_roof_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "pitched_roof_grid",
            "maximum_error_percentage_points": 0.00410958904109604,
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
      "study_preparation_seconds": 0.006912874989211559,
      "weather_seconds": 0.0744191249832511,
      "metric_reduction_seconds": 0.03849445900414139,
      "write_seconds": 0.028587541077286005,
      "total_seconds": 0.14176079095341265,
      "cold_end_to_end_seconds": 0.1486736659426242,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002914167009294033,
      "engine_upload_seconds": 0.000283208,
      "engine_acceleration_structure_seconds": 0.003815834,
      "engine_tracing_seconds": 0.01688666653353721,
      "engine_annual_reduction_seconds": 0.00047912506852298975,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01688666653353721
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006912874989211559,
      "weather_seconds": 0.0733747910708189,
      "metric_reduction_seconds": 0.013421874959021807,
      "write_seconds": 0.02811816695611924,
      "total_seconds": 0.11504208296537399,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.11504208296537399,
      "raw_export_seconds": 0.0017273329431191087,
      "engine_upload_seconds": 4.7292e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0005186666967347264,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01071904192212969,
      "full": 0.024738250067457557
    }
  },
  "elapsed_seconds": 0.7985582919791341,
  "result_class": "passed"
}
```
