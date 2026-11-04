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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "84a47a72d0f328513390e2de9ab2f0e1b0934d4c096aaa46fa1c9e974ac31164",
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
      "scene_fingerprint": 457850612654732671,
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
      "scene_fingerprint": 457850612654732671,
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
          "maximum": 0.00021724204998463392,
          "p95": 2.0884908735752106e-07,
          "p99": 1.4642209862358868e-05
        },
        "bias_percent": -0.02181053706149758,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6293936351155377,
        "worst_index": [
          3,
          447,
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
          "maximum": 0.0007299482822418213,
          "p95": 7.671257480978966e-05,
          "p99": 0.00015232199802994728
        },
        "bias_percent": 0.020815192700713404,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0794263821908936,
        "worst_index": [
          34,
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
          "maximum": 0.0006835311651229858,
          "p95": 6.23110681772232e-05,
          "p99": 0.00012327427975833416
        },
        "bias_percent": 0.022241283584617647,
        "identifier": "double_height_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8941525569766038,
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008144598687067628,
                  "p50": 0.0,
                  "p90": 9.246100671589375e-05,
                  "p95": 0.0001880050403997302,
                  "p99": 0.00043733115307986736
                },
                "candidate_energy": 21.705603183216226,
                "cvrmse_percent": 25.29320513262233,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.04405008284216146,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.715168733032442,
                "relative_energy_error_percent": 0.04405008284216146,
                "rms_normalized_rmse_percent": 8.607296706035818,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013586380518972874,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0005441781831905246,
                  "rgb_channel": 0,
                  "sky_patch_index": 85
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.002358820289373398,
                  "p50": 0.0,
                  "p90": 0.0001331878476776188,
                  "p95": 0.0002843384281732142,
                  "p99": 0.0005669196834787726
                },
                "candidate_energy": 7.73826074707085,
                "cvrmse_percent": 99.12101630668445,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3053800350167284,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.71470158865797,
                "relative_energy_error_percent": 0.3053800350167284,
                "rms_normalized_rmse_percent": 5.7027549737318814,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03769854083657265,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.040057361125946045,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.27608406729996,
            "full": 260.097875026986
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.5212080264464,
            "full": 259.0118329972029
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.62804199196398,
            "full": 269.54866701271385
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.25529196299613,
            "full": 257.9278750345111
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041472387965768576,
                  "p50": 0.0,
                  "p90": 4.563844413496554e-05,
                  "p95": 9.832740761339664e-05,
                  "p99": 0.00019997241906821728
                },
                "candidate_energy": 21.71007885725885,
                "cvrmse_percent": 11.847460154153877,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.019570104019500077,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.705831003553158,
                "relative_energy_error_percent": 0.019570104019500077,
                "rms_normalized_rmse_percent": 4.036580264529707,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003713531536050141,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.004128255415707827,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000867694616317749,
                  "p50": 6.772757998874113e-08,
                  "p90": 7.079436036292471e-05,
                  "p95": 0.00014417048078030348,
                  "p99": 0.0002902087289839983
                },
                "candidate_energy": 13.667469862186802,
                "cvrmse_percent": 28.670256754004285,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.141530347440328,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.64815358300159,
                "relative_energy_error_percent": 0.141530347440328,
                "rms_normalized_rmse_percent": 1.9655647848138127,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06737928465008736,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.06651159003376961,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.36141695361584,
            "full": 2203.6496659275144
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.03237491473556,
            "full": 2189.7374999243766
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.47424993105233,
            "full": 2205.76329191681
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.6154999602586,
            "full": 2200.764332897961
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000376472482457757,
                  "p50": 0.0,
                  "p90": 4.659103869926206e-05,
                  "p95": 9.705056436359882e-05,
                  "p99": 0.00019233243074268103
                },
                "candidate_energy": 21.705459365263778,
                "cvrmse_percent": 11.84195553217459,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0288143534436502,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.699206879099165,
                "relative_energy_error_percent": 0.0288143534436502,
                "rms_normalized_rmse_percent": 4.035998578854415,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034623700194060802,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0030858975369483232,
                  "rgb_channel": 0,
                  "sky_patch_index": 271
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009284429252147675,
                  "p50": 7.60114442499571e-08,
                  "p90": 6.858639953861726e-05,
                  "p95": 0.00014322681818157434,
                  "p99": 0.00027964485343545675
                },
                "candidate_energy": 13.67273152688411,
                "cvrmse_percent": 27.932858122301866,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.02833459866628839,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.668858510682846,
                "relative_energy_error_percent": 0.028334598666288395,
                "rms_normalized_rmse_percent": 1.9157565846943272,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0670986995100975,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.06802714243531227,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.3485000533983,
            "full": 2253.4466249635443
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.32758296187967,
            "full": 2265.007790992968
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.00045805517584,
            "full": 2275.2536250045523
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.61637495458126,
            "full": 2303.667625063099
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
            "identifier": "double_height_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002137224655598402,
                  "p50": 0.0,
                  "p90": 2.323666121810676e-05,
                  "p95": 5.573243834078312e-05,
                  "p99": 0.00010234746150672436
                },
                "candidate_energy": 21.704990576049568,
                "cvrmse_percent": 6.368585956558638,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.004930079047432659,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 21.703920555609784,
                "relative_energy_error_percent": 0.004930079047432658,
                "rms_normalized_rmse_percent": 2.171340574999976,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037004309706389904,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.00348670850507915,
                  "rgb_channel": 0,
                  "sky_patch_index": 315
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005807653069496155,
                  "p50": 5.8455155382830526e-08,
                  "p90": 4.205836012260989e-05,
                  "p95": 8.215400157496333e-05,
                  "p99": 0.00015896011609584093
                },
                "candidate_energy": 13.676369618713206,
                "cvrmse_percent": 16.200544304104568,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0024918953402156773,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 13.676710428023057,
                "relative_energy_error_percent": 0.002491895340215677,
                "rms_normalized_rmse_percent": 1.1109545065661566,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07207994908094406,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.07266071438789368,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 287.3820409877226,
            "full": 4030.6869170162827
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 283.54850003961474,
            "full": 4012.4800000339746
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 268.4581249486655,
            "full": 4060.360874980688
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 293.0546250427142,
            "full": 3965.0355000048876
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
    "/content/suite-vulkan-0.3.3/double_height/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2610.444749938324,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/double_height/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10947.985125007108,
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
        "identifier": "double_height_grid",
        "full_identifier": "double_height_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.004219288119396245,
            "cvrmse_percent": 0.8604069418797312,
            "rms_normalized_rmse_percent": 0.29337886041594335,
            "reference_energy": 21.702642030759762,
            "candidate_energy": 21.70355772775656,
            "relative_energy_error_percent": 0.0042192881193962445,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.632158041000366e-08,
              "p95": 3.3510150387883186e-07,
              "p99": 1.2130592949688435e-05,
              "maximum": 9.655102621763945e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 367,
              "rgb_channel": 0,
              "reference": 0.0018896149704232812,
              "candidate": 0.0019861659966409206,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.03302077060766079,
            "cvrmse_percent": 13.364889896070085,
            "rms_normalized_rmse_percent": 0.9165016431535516,
            "reference_energy": 13.678353555810702,
            "candidate_energy": 13.673836858060133,
            "relative_energy_error_percent": 0.033020770607660795,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1859552628834535e-07,
              "p90": 2.5264671421609846e-05,
              "p95": 4.092976450920105e-05,
              "p99": 8.513173088431358e-05,
              "maximum": 0.001149505376815796
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07281084358692169,
              "candidate": 0.0716613382101059,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.010177782433959975,
            "cvrmse_percent": 5.171388920800608,
            "rms_normalized_rmse_percent": 0.9172997762656602,
            "reference_energy": 35.380995586570464,
            "candidate_energy": 35.3773945858167,
            "relative_energy_error_percent": 0.010177782433934872,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2028485940618339e-07,
              "p90": 2.5306252064183356e-05,
              "p95": 4.122479003854096e-05,
              "p99": 8.511822670698166e-05,
              "maximum": 0.001149505376815796
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07281084358692169,
              "candidate": 0.0716613382101059,
              "position": [
                1.5,
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
        "identifier": "double_height_grid",
        "full_identifier": "double_height_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.004219288119396245,
            "cvrmse_percent": 0.8604069418797312,
            "rms_normalized_rmse_percent": 0.29337886041594335,
            "reference_energy": 21.702642030759762,
            "candidate_energy": 21.70355772775656,
            "relative_energy_error_percent": 0.0042192881193962445,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.632158041000366e-08,
              "p95": 3.3510150387883186e-07,
              "p99": 1.2130592949688435e-05,
              "maximum": 9.655102621763945e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 367,
              "rgb_channel": 0,
              "reference": 0.0018896149704232812,
              "candidate": 0.0019861659966409206,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.79646831939648,
            "cvrmse_percent": 906.9995170900526,
            "rms_normalized_rmse_percent": 52.25615188935367,
            "reference_energy": 7.734225116622403,
            "candidate_energy": 13.673836858060133,
            "relative_energy_error_percent": 76.79646831939648,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001757599809934622,
              "p95": 0.00023290139506570995,
              "p99": 0.0003939892631024122,
              "maximum": 0.030392561107873917
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04989318922162056,
              "candidate": 0.08028575032949448,
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
            "nmbe_percent": 20.180569517442088,
            "cvrmse_percent": 238.30465876482995,
            "rms_normalized_rmse_percent": 52.256182690735244,
            "reference_energy": 29.436867147382166,
            "candidate_energy": 35.3773945858167,
            "relative_energy_error_percent": 20.18056951744211,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00017620112048462053,
              "p95": 0.00023242458701133728,
              "p99": 0.00039204611675813794,
              "maximum": 0.030392561107873917
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04989318922162056,
              "candidate": 0.08028575032949448,
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
      "bias_percent": 0.13928505366512947,
      "rms_normalized_error_percent": 0.26573572732551515,
      "absolute_error": {
        "p95": 0.30986410283101673,
        "p99": 0.36722710487193766,
        "maximum": 0.37943558698158597
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 45.855549372119086,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.26573572732551515
    },
    "overcast": {
      "bias_percent": 0.0559110609621363,
      "rms_normalized_error_percent": 0.1772128462209616,
      "absolute_error": {
        "p95": 0.1299889087677002,
        "p99": 0.16209826469421387,
        "maximum": 0.1627187728881836
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 30.93967056274414,
      "reference_fraction_of_uniform": 0.6747203469276428,
      "rms_normalized_to_uniform_percent": 0.12437799451842015
    },
    "horizon": {
      "bias_percent": 1.5738669681476725,
      "rms_normalized_error_percent": 1.9838686024996102,
      "absolute_error": {
        "p95": 0.17797441353746613,
        "p99": 0.20280581182377805,
        "maximum": 0.20658899812442044
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.378190698893574,
      "reference_fraction_of_uniform": 0.0954778812781073,
      "rms_normalized_to_uniform_percent": 0.16714957377497078
    },
    "north": {
      "bias_percent": -37.79005775186461,
      "rms_normalized_error_percent": 90.25207401934308,
      "absolute_error": {
        "p95": 3.816718071902869e-05,
        "p99": 4.080263299783837e-05,
        "maximum": 4.1130752379103797e-05
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.4149005437502638e-05,
      "reference_fraction_of_uniform": 3.0855602517476655e-07,
      "rms_normalized_to_uniform_percent": 3.142123515633429e-05
    },
    "east": {
      "bias_percent": -0.20061621571529123,
      "rms_normalized_error_percent": 0.3501462360521766,
      "absolute_error": {
        "p95": 0.09825491905212402,
        "p99": 0.1146402359008789,
        "maximum": 0.11536788940429688
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.081759452819824,
      "reference_fraction_of_uniform": 0.1762438714504242,
      "rms_normalized_to_uniform_percent": 0.0713213493760589
    },
    "south": {
      "bias_percent": 0.23731369324855214,
      "rms_normalized_error_percent": 0.3903870231181975,
      "absolute_error": {
        "p95": 0.3085808753967285,
        "p99": 0.3524445533752441,
        "maximum": 0.36641883850097656
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 30.966854095458984,
      "reference_fraction_of_uniform": 0.6753131151199341,
      "rms_normalized_to_uniform_percent": 0.25244896878862
    },
    "west": {
      "bias_percent": 0.09838567760474971,
      "rms_normalized_error_percent": 0.20919963967519098,
      "absolute_error": {
        "p95": 0.042658448219299316,
        "p99": 0.05044176578521729,
        "maximum": 0.05091524124145508
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.145157814025879,
      "reference_fraction_of_uniform": 0.17762643098831177,
      "rms_normalized_to_uniform_percent": 0.042832407971762305
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
          "nmbe_percent": 0.06712973797084038,
          "cvrmse_percent": 1.1016078187968799,
          "absolute_error_percentiles_lux": {
            "p50": 5.587646484375,
            "p90": 58.317700195312504,
            "p95": 90.43786621093741,
            "p99": 192.02648437499943
          },
          "maximum_absolute_error_lux": 994.19140625,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              5.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 19367.140625,
            "radiance_lux": 18372.94921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.04247716894977237,
            "maximum_error_percentage_points": 0.16534246575342593,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.01579178395940417,
            "maximum_error_percentage_points": 0.07894164729877673,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.006312785388128134,
            "maximum_error_percentage_points": 0.058630136986300485,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.17935692541856982,
            "maximum_error_percentage_points": 0.660273972602738,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.18307838660578357,
            "maximum_error_percentage_points": 0.6619178082191794,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.00488120719178653,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "double_height_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.3543009269999402,
      "weather_seconds": 0.22466282699997464,
      "metric_reduction_seconds": 1.0169206020000274,
      "write_seconds": 0.011972937999985334,
      "total_seconds": 1.2538947490000965,
      "cold_end_to_end_seconds": 1.6081956760000367,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015393480000511772,
      "engine_upload_seconds": 0.044078272,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.055888123,
      "engine_annual_reduction_seconds": 0.034726284,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.055888123
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3543009269999402,
      "weather_seconds": 0.2423525700000937,
      "metric_reduction_seconds": 0.9040987560000531,
      "write_seconds": 0.011297561999981554,
      "total_seconds": 1.1580089550000139,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.1580089550000139,
      "raw_export_seconds": 0.001419419000058042,
      "engine_upload_seconds": 0.043654305,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.3e-07,
      "engine_annual_reduction_seconds": 0.03197096,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.017604907999952957,
      "full": 0.0682287949999818
    }
  },
  "elapsed_seconds": 5.46742489899998,
  "result_class": "passed"
}
```
