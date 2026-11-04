# Foton report

Status: **passed**

```json
{
  "scene": "teaching_living_room",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_living_room",
    "category": "teaching",
    "question": "How is a 5 x 4.5 m living room with a tall window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
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
    "sensors": 20,
    "floor_area": 22.5,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "5cb219674cfc082dfd0d289cfc98f3e88d02e0ce785e1c9729b898364e688242",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5011208731090707716,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5011208731090707716,
      "basis": "ReinhartMf2",
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
    "ray_count": 9248,
    "command": [
      "/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
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
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "59ff7b6ed290a327e1a4a6f5e8eaf4153d34bbea3bab25ed8c13123f0b99cc89",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "7b1607c11eb2f886cb1b00285cf77b48f28c7f9f5caae4c4b229203928ac8536",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00018102512694895267,
          "p95": 1.0758230928331486e-07,
          "p99": 1.5528392395935953e-05
        },
        "bias_percent": -0.07050147925083113,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9042252351251191,
        "worst_index": [
          3,
          445,
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
          "maximum": 0.0006983652710914612,
          "p95": 4.9941393081098163e-05,
          "p99": 0.0001254224916920066
        },
        "bias_percent": 0.010338928953574045,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0360276165384172,
        "worst_index": [
          10,
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
          "maximum": 0.0004818364977836609,
          "p95": 4.1935872286558046e-05,
          "p99": 0.00010170112363994122
        },
        "bias_percent": 0.0006701724090792711,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8619841743883887,
        "worst_index": [
          8,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003749739844352007,
                  "p50": 0.0,
                  "p90": 1.8149148672819138e-07,
                  "p95": 7.434027211274709e-05,
                  "p99": 0.00018796854419633746
                },
                "candidate_energy": 6.351920865192369,
                "cvrmse_percent": 20.55068972145182,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04938929871162203,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.348785244683313,
                "relative_energy_error_percent": 0.04938929871162203,
                "rms_normalized_rmse_percent": 5.319989928680282,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00206144992262125,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.0016864759381860495,
                  "rgb_channel": 0,
                  "sky_patch_index": 153
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009574294090270996,
                  "p50": 0.0,
                  "p90": 2.5697556429805018e-05,
                  "p95": 0.00011735108128050336,
                  "p99": 0.000294307479634881
                },
                "candidate_energy": 2.865147492299883,
                "cvrmse_percent": 72.01097708693908,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2470487843919032,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8580866240383287,
                "relative_energy_error_percent": 0.24704878439190323,
                "rms_normalized_rmse_percent": 3.0922285784028745,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03357947990298271,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.03262205049395561,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.07529104407877,
            "full": 188.24987497646362
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.70987503789365,
            "full": 195.25524997152388
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.55437499657273,
            "full": 182.2569160722196
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.30904098879546,
            "full": 185.43975008651614
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003211670555174351,
                  "p50": 0.0,
                  "p90": 3.4911900002048434e-07,
                  "p95": 6.936525060154957e-05,
                  "p99": 0.00016861106269061565
                },
                "candidate_energy": 6.3502536849791795,
                "cvrmse_percent": 18.422161514235214,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04404599868561851,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.347457883763127,
                "relative_energy_error_percent": 0.044045998685618516,
                "rms_normalized_rmse_percent": 4.775287277686047,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0031705695437267423,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.002849402488209307,
                  "rgb_channel": 0,
                  "sky_patch_index": 266
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007957015186548233,
                  "p50": 5.000000058430487e-08,
                  "p90": 2.9182455546106303e-05,
                  "p95": 9.988154779421068e-05,
                  "p99": 0.00024931534426286817
                },
                "candidate_energy": 5.051896027673926,
                "cvrmse_percent": 34.10099456696565,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.004022257187994449,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.052099236098595,
                "relative_energy_error_percent": 0.004022257187994449,
                "rms_normalized_rmse_percent": 1.9496745164129756,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04913979396224022,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.04993549548089504,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.30587497353554,
            "full": 1468.6622499721125
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.77983300760388,
            "full": 1459.4835829921067
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.1535840490833,
            "full": 1453.6944999126717
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.33287505805492,
            "full": 1452.7239999733865
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00038340315222740173,
                  "p50": 0.0,
                  "p90": 5.901034455747986e-07,
                  "p95": 6.461188313550931e-05,
                  "p99": 0.0001557141076773405
                },
                "candidate_energy": 6.343903896104166,
                "cvrmse_percent": 16.757089987803727,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06953320023697243,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.348318084829771,
                "relative_energy_error_percent": 0.06953320023697243,
                "rms_normalized_rmse_percent": 4.342962737092129,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036695689195767045,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.004052972071804106,
                  "rgb_channel": 0,
                  "sky_patch_index": 314
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007205680012702942,
                  "p50": 5.000000058430487e-08,
                  "p90": 2.8579071476997466e-05,
                  "p95": 9.847264445852423e-05,
                  "p99": 0.00024258799385279417
                },
                "candidate_energy": 5.057908184026754,
                "cvrmse_percent": 33.078174868704096,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07863152261237759,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.053934198614556,
                "relative_energy_error_percent": 0.07863152261237759,
                "rms_normalized_rmse_percent": 1.8956686183308553,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07016511633992195,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.06944454833865166,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.88083400949836,
            "full": 1497.8070000652224
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.1978339618072,
            "full": 1544.9476670473814
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.97599990013987,
            "full": 1528.5646660486236
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.76974999159575,
            "full": 1496.1667089955881
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001618449459783733,
                  "p50": 0.0,
                  "p90": 1.778826117515564e-07,
                  "p95": 3.4890446113422475e-05,
                  "p99": 9.046308696269989e-05
                },
                "candidate_energy": 6.347832074395228,
                "cvrmse_percent": 9.332448644282302,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.016630046161592537,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.3467766025164565,
                "relative_energy_error_percent": 0.016630046161592534,
                "rms_normalized_rmse_percent": 2.4198918207847018,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002089884481392801,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0019280395354144275,
                  "rgb_channel": 0,
                  "sky_patch_index": 220
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008024238049983978,
                  "p50": 5.000000058430487e-08,
                  "p90": 1.9804453404503977e-05,
                  "p95": 5.6815921561792187e-05,
                  "p99": 0.00014186091721057892
                },
                "candidate_energy": 5.050798133308277,
                "cvrmse_percent": 20.703724987391297,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.15838094211353615,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.058810324760369,
                "relative_energy_error_percent": 0.15838094211353615,
                "rms_normalized_rmse_percent": 1.1857938657689293,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05014590360224247,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.04934347979724407,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.12225004471838,
            "full": 2643.9789169235155
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.33779194857925,
            "full": 2696.4701659744605
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.97358297929168,
            "full": 2653.2802500296384
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.08120793197304,
            "full": 2664.803499937989
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
    "/content/suite-vulkan-0.3.3/teaching_living_room/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1333.6954159894958,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4974.351292010397,
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
      20,
      578,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.030671259279922324,
            "cvrmse_percent": 1.6741299558240168,
            "rms_normalized_rmse_percent": 0.4341809827412328,
            "reference_energy": 6.344422547339491,
            "candidate_energy": 6.346368461628799,
            "relative_energy_error_percent": 0.030671259279922328,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.2118911147117615e-09,
              "p95": 9.824289008973098e-08,
              "p99": 9.323819540441036e-06,
              "maximum": 0.00010466063395142555
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 445,
              "rgb_channel": 0,
              "reference": 0.0028061899356544018,
              "candidate": 0.0029108505696058273,
              "position": [
                0.5,
                0.5625,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0723026878738455,
            "cvrmse_percent": 39.68868388884265,
            "rms_normalized_rmse_percent": 2.2745414165613154,
            "reference_energy": 5.057686050877999,
            "candidate_energy": 5.003452347410214,
            "relative_energy_error_percent": 1.0723026878738455,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.6825385286174424e-08,
              "p90": 1.6593017790000926e-05,
              "p95": 2.8013030532747504e-05,
              "p99": 6.246636621654034e-05,
              "maximum": 0.002678424119949341
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07618241012096405,
              "candidate": 0.07350398600101471,
              "position": [
                2.5,
                1.6875,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.458579996217991,
            "cvrmse_percent": 17.60048079649425,
            "rms_normalized_rmse_percent": 2.2739713508252013,
            "reference_energy": 11.40210859821749,
            "candidate_energy": 11.349820809039013,
            "relative_energy_error_percent": 0.45857999621799095,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.6825385286174424e-08,
              "p90": 1.654575462453074e-05,
              "p95": 2.761029900284467e-05,
              "p99": 6.217206828296185e-05,
              "maximum": 0.002678424119949341
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07618241012096405,
              "candidate": 0.07350398600101471,
              "position": [
                2.5,
                1.6875,
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
      20,
      578,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.030671259279922324,
            "cvrmse_percent": 1.6741299558240168,
            "rms_normalized_rmse_percent": 0.4341809827412328,
            "reference_energy": 6.344422547339491,
            "candidate_energy": 6.346368461628799,
            "relative_energy_error_percent": 0.030671259279922328,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.2118911147117615e-09,
              "p95": 9.824289008973098e-08,
              "p99": 9.323819540441036e-06,
              "maximum": 0.00010466063395142555
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 445,
              "rgb_channel": 0,
              "reference": 0.0028061899356544018,
              "candidate": 0.0029108505696058273,
              "position": [
                0.5,
                0.5625,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 74.48541899202124,
            "cvrmse_percent": 779.124705871399,
            "rms_normalized_rmse_percent": 33.610891652658104,
            "reference_energy": 2.8675475442672997,
            "candidate_energy": 5.003452347410214,
            "relative_energy_error_percent": 74.48541899202124,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012365035945549607,
              "p95": 0.0001662022004552454,
              "p99": 0.0002991452347487211,
              "maximum": 0.017638124525547028
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030130796134471893,
              "candidate": 0.04776892066001892,
              "position": [
                3.5,
                3.9375,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.207312835069455,
            "cvrmse_percent": 242.53264533540064,
            "rms_normalized_rmse_percent": 33.611287881744516,
            "reference_energy": 9.21197009160679,
            "candidate_energy": 11.349820809039013,
            "relative_energy_error_percent": 23.207312835069455,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012413293961799381,
              "p95": 0.0001662253286554001,
              "p99": 0.00029953732155263424,
              "maximum": 0.017638124525547028
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030130796134471893,
              "candidate": 0.04776892066001892,
              "position": [
                3.5,
                3.9375,
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
      "bias_percent": 0.2180839464538673,
      "rms_normalized_error_percent": 0.22898328871641604,
      "absolute_error": {
        "p95": 0.14308513215604202,
        "p99": 0.18560072866702979,
        "maximum": 0.19622962779477682
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.713403553708073,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22898328871641604
    },
    "overcast": {
      "bias_percent": 0.1619145595479751,
      "rms_normalized_error_percent": 0.15210197371896506,
      "absolute_error": {
        "p95": 0.06265122890472413,
        "p99": 0.07730037212371824,
        "maximum": 0.0809626579284668
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.373817443847656,
      "reference_fraction_of_uniform": 0.6483176350593567,
      "rms_normalized_to_uniform_percent": 0.10628202052882021
    },
    "horizon": {
      "bias_percent": 1.0656115455512378,
      "rms_normalized_error_percent": 1.7634131932523804,
      "absolute_error": {
        "p95": 0.104059939948796,
        "p99": 0.12854967003757917,
        "maximum": 0.13467210255977502
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.693671171583957,
      "reference_fraction_of_uniform": 0.11359276897907583,
      "rms_normalized_to_uniform_percent": 0.1488524245041164
    },
    "north": {
      "bias_percent": -51.13586356464871,
      "rms_normalized_error_percent": 99.07668497696784,
      "absolute_error": {
        "p95": 3.7760237100314985e-05,
        "p99": 7.458502050383225e-05,
        "maximum": 8.379121635471165e-05
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1038723641831893e-05,
      "reference_fraction_of_uniform": 4.6550565002689837e-07,
      "rms_normalized_to_uniform_percent": 6.511397648296684e-05
    },
    "east": {
      "bias_percent": 0.09371444421127668,
      "rms_normalized_error_percent": 0.24180303223460659,
      "absolute_error": {
        "p95": 0.028858327865600587,
        "p99": 0.02941134452819824,
        "maximum": 0.029549598693847656
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.317532062530518,
      "reference_fraction_of_uniform": 0.18207137286663055,
      "rms_normalized_to_uniform_percent": 0.04996240989752678
    },
    "south": {
      "bias_percent": 0.2772151320276563,
      "rms_normalized_error_percent": 0.3169793143378966,
      "absolute_error": {
        "p95": 0.14148473739624026,
        "p99": 0.18009443283081047,
        "maximum": 0.18974685668945312
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.465112686157227,
      "reference_fraction_of_uniform": 0.694337785243988,
      "rms_normalized_to_uniform_percent": 0.20845373460317912
    },
    "west": {
      "bias_percent": 0.20718639723271018,
      "rms_normalized_error_percent": 0.23143024960637404,
      "absolute_error": {
        "p95": 0.03032670021057129,
        "p99": 0.03318020820617675,
        "maximum": 0.033893585205078125
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.3688788414001465,
      "reference_fraction_of_uniform": 0.18423669040203094,
      "rms_normalized_to_uniform_percent": 0.04821331215131624
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
        "identifier": "teaching_living_room_grid",
        "sensor_count": 20,
        "illuminance": {
          "nmbe_percent": 0.09917743780542669,
          "cvrmse_percent": 1.260231275323898,
          "absolute_error_percentiles_lux": {
            "p50": 3.506805419921875,
            "p90": 36.70417480468752,
            "p95": 56.299267578125026,
            "p99": 113.20997558593723
          },
          "maximum_absolute_error_lux": 462.71875,
          "worst": {
            "sensor_index": 11,
            "position": [
              2.5,
              0.5625,
              0.75
            ],
            "hour_of_year": 2724.5,
            "foton_lux": 42090.1328125,
            "radiance_lux": 41627.4140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.11013698630137156,
            "maximum_error_percentage_points": 0.49589041095890707,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04066907621898963,
            "maximum_error_percentage_points": 0.14981628439745975,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03112328767123316,
            "maximum_error_percentage_points": 0.160273972602738,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.056794520547944316,
            "maximum_error_percentage_points": 0.1673972602739724,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04990410958904088,
            "maximum_error_percentage_points": 0.16438356164383805,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 5.0,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004570312499993179,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
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
      "study_preparation_seconds": 0.3716308670000217,
      "weather_seconds": 0.2431799299999966,
      "metric_reduction_seconds": 0.6325595589999011,
      "write_seconds": 0.01228608700012046,
      "total_seconds": 0.8883717690000594,
      "cold_end_to_end_seconds": 1.260002636000081,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0012034349999794358,
      "engine_upload_seconds": 0.044380479,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02411107,
      "engine_annual_reduction_seconds": 0.026545836,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02411107
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3716308670000217,
      "weather_seconds": 0.24980117600011909,
      "metric_reduction_seconds": 0.6184855470000912,
      "write_seconds": 0.012372807000019748,
      "total_seconds": 0.8809515609998471,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.8809515609998471,
      "raw_export_seconds": 0.0012653030000819854,
      "engine_upload_seconds": 0.044708237,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.13e-07,
      "engine_annual_reduction_seconds": 0.02620098,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01772507299983772,
      "full": 0.03769308200003252
    }
  },
  "elapsed_seconds": 4.378261977999955,
  "result_class": "passed"
}
```
