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
  "sky_density": 2,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "281c2b6a979d5d59d7552610a29ed1b614fb82d01d4516558c00438a322cc156",
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
      "scene_fingerprint": 1666965602579954223,
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
      "scene_fingerprint": 1666965602579954223,
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "c73e78d0633e70c94d7b9a9722cc6b7d5c69587d8d1b9d2393006289ce4d078c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "e75d8c9643462ce1ef94674e2df8fd73709d93c53864d1bdf54a08ec7317fa65",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 12
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 1.200605765916407e-07,
          "p99": 9.124496136790706e-06
        },
        "bias_percent": -0.04453063170271223,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.745993439904148,
        "worst_index": [
          11,
          543,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 2.361941005801782e-05,
          "p95": 0.0,
          "p99": 1.0848380043171035e-07
        },
        "bias_percent": 0.49130191256348316,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4185961332525538,
        "worst_index": [
          17,
          153,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 9.880026482278481e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.39350986750028416,
        "identifier": "three_room_chain_2_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.743436849982268,
        "worst_index": [
          11,
          89,
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
          "maximum": 0.0004243087023496628,
          "p95": 3.4488504752516747e-05,
          "p99": 0.00010948056587949385
        },
        "bias_percent": 0.035205678493143856,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6328193107415667,
        "worst_index": [
          7,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0001586833968758583,
          "p95": 3.0226556191337295e-06,
          "p99": 1.0903861402766652e-05
        },
        "bias_percent": 0.7219096371953452,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 4.329166776176263,
        "worst_index": [
          11,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 7.107639976311475e-05,
          "p95": 4.866872131970013e-07,
          "p99": 1.9616367126217876e-06
        },
        "bias_percent": -0.7889985327014579,
        "identifier": "three_room_chain_2_grid",
        "passed": false,
        "rms_normalized_error_percent": 10.368941857914729,
        "worst_index": [
          11,
          91,
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
          "maximum": 0.0004832819104194641,
          "p95": 2.895425132010132e-05,
          "p99": 9.316978394053854e-05
        },
        "bias_percent": -0.01716275813960776,
        "identifier": "three_room_chain_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4046892211342745,
        "worst_index": [
          10,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00010965252295136452,
          "p95": 2.659129734183807e-06,
          "p99": 9.075434172700493e-06
        },
        "bias_percent": -0.3323457519856325,
        "identifier": "three_room_chain_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.796068433558398,
        "worst_index": [
          12,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 5.328716360963881e-05,
          "p95": 4.0975949033850156e-07,
          "p99": 1.7681911231192323e-06
        },
        "bias_percent": 1.3624333354408436,
        "identifier": "three_room_chain_2_grid",
        "passed": false,
        "rms_normalized_error_percent": 9.993060973542415,
        "worst_index": [
          11,
          0,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036201179803659533,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.39381692558527e-05,
                  "p99": 0.0001523515238659453
                },
                "candidate_energy": 5.714523459722841,
                "cvrmse_percent": 20.36231482090884,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04345471065272287,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.712041308699781,
                "relative_energy_error_percent": 0.04345471065272273,
                "rms_normalized_rmse_percent": 4.606510509727311,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0032824570080265403,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0036444688060631356,
                  "rgb_channel": 0,
                  "sky_patch_index": 415
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000550360147220393,
                  "p50": 0.0,
                  "p90": 7.156610081437975e-06,
                  "p95": 6.457213263881081e-05,
                  "p99": 0.00023314410682360147
                },
                "candidate_energy": 1.6984282237642248,
                "cvrmse_percent": 103.70721987976982,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3514141993120835,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7044177898935118,
                "relative_energy_error_percent": 0.35141419931208545,
                "rms_normalized_rmse_percent": 3.997426971120015,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00023065850837156177,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": -0.00031970163884883124,
                  "rgb_channel": 0,
                  "sky_patch_index": 204
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
                  "maximum": 0.0002049125760095194,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.820809782463213e-07
                },
                "candidate_energy": 0.12358170932020585,
                "cvrmse_percent": 179.79819292146132,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.2571263467105736,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.12326476313796775,
                "relative_energy_error_percent": 0.2571263467105735,
                "rms_normalized_rmse_percent": 13.500592948647544,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0007974662003107369,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.0005925536243012175,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00029042038174035645,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4783907450540206e-05
                },
                "candidate_energy": 0.08518294110983504,
                "cvrmse_percent": 371.9815176841515,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -1.8193181828821299,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0867614071661329,
                "relative_energy_error_percent": 1.8193181828821308,
                "rms_normalized_rmse_percent": 11.102570905141027,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00013067964270400503,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": -0.00015974073903635144,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
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
                  "maximum": 5.659910190540056e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012423895148458541,
                "cvrmse_percent": 386.6840429878319,
                "energy_difference_negligible": true,
                "nmbe_percent": 3.0961862792496286,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012050780534991645,
                "relative_energy_error_percent": 3.096186279249627,
                "rms_normalized_rmse_percent": 18.410888900079602,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 7.928528187524837e-05,
                  "global_sensor_index": 57,
                  "local_sensor_index": 9,
                  "reference": 0.00013588438378064893,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 5.918800646516806e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.056033230886283e-07
                },
                "candidate_energy": 0.012544720291600697,
                "cvrmse_percent": 528.0073962194547,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.4980195604239277,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012359571493050225,
                "relative_energy_error_percent": 1.498019560423926,
                "rms_normalized_rmse_percent": 16.699887498113377,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00019519958368618973,
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "reference": 0.00013601157722102167,
                  "rgb_channel": 0,
                  "sky_patch_index": 31
                }
              }
            },
            "start_sensor_index": 48
          }
        ],
        "half_run_count": 6,
        "oracle_stable": true,
        "run_count": 12,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.82291689701378,
            "full": 414.75208301562816
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.39799998421222,
            "full": 407.1347080171108
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.99291593953967,
            "full": 433.76270798034966
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.11079192440957,
            "full": 404.9526669550687
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.70879201125354,
            "full": 412.0353750186041
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.47095795813948,
            "full": 405.33037506975234
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.3057499481365,
            "full": 428.9021249860525
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.678542050533,
            "full": 412.89579099975526
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.55412504728884,
            "full": 417.8212909027934
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.897709001787,
            "full": 454.79758305009454
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.53154207393527,
            "full": 432.701374986209
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.240916993469,
            "full": 403.59729202464223
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036213849671185017,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.336118399805855e-05,
                  "p99": 0.00013998392387293263
                },
                "candidate_energy": 5.713127053215544,
                "cvrmse_percent": 19.328183011326928,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02658842449924656,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.711608426521366,
                "relative_energy_error_percent": 0.02658842449924656,
                "rms_normalized_rmse_percent": 4.370479134470445,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036686910316348076,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.004030829528346658,
                  "rgb_channel": 0,
                  "sky_patch_index": 314
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007498450577259064,
                  "p50": 4.901119332600956e-08,
                  "p90": 1.670283018029295e-05,
                  "p95": 6.238347850739956e-05,
                  "p99": 0.0002119970376952546
                },
                "candidate_energy": 3.031622259165257,
                "cvrmse_percent": 56.2661937161844,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.27908417119716916,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.040106715796547,
                "relative_energy_error_percent": 0.2790841711971691,
                "rms_normalized_rmse_percent": 2.9981844669361872,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.027785465121269226,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.028535310178995132,
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
                  "maximum": 0.00013703558943234384,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.548439242547835e-07
                },
                "candidate_energy": 0.12303979571385071,
                "cvrmse_percent": 165.12666008814512,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.45437062101451164,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.12360140418161336,
                "relative_energy_error_percent": 0.45437062101451164,
                "rms_normalized_rmse_percent": 12.343324919219699,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005687696975655854,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.0007058052869979292,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004362170584499836,
                  "p50": 0.0,
                  "p90": 2.592055778904978e-06,
                  "p95": 4.383006398711586e-06,
                  "p99": 1.8514736602526027e-05
                },
                "candidate_energy": 0.20192341651607393,
                "cvrmse_percent": 184.38467784177502,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.753665719131002,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.20041297264456048,
                "relative_energy_error_percent": 0.7536657191310019,
                "rms_normalized_rmse_percent": 9.078855177641378,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.005695690400898457,
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "reference": 0.005259473342448473,
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
                  "maximum": 0.0001182177074952051,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012880976396445476,
                "cvrmse_percent": 694.7030740618646,
                "energy_difference_negligible": true,
                "nmbe_percent": 3.4742922232980793,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012448479829799908,
                "relative_energy_error_percent": 3.4742922232980797,
                "rms_normalized_rmse_percent": 32.15293518483462,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0002866304566850886,
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "reference": 0.00016841274918988347,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00020536880037980154,
                  "p50": 0.0,
                  "p90": 1.824219992840881e-07,
                  "p95": 5.100460285234476e-07,
                  "p99": 2.45177565716401e-06
                },
                "candidate_energy": 0.025900921577839853,
                "cvrmse_percent": 493.70861861597376,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -5.956883870537984,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0275415390768039,
                "relative_energy_error_percent": 5.956883870537984,
                "rms_normalized_rmse_percent": 25.17828157445311,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00012864870950579643,
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "reference": 7.672009087400511e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.53891701437533,
            "full": 5166.397624998353
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.26587497908622,
            "full": 5180.401833029464
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.5167500069365,
            "full": 5248.420082964003
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.5172090018168,
            "full": 5192.733083968051
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003630864666774869,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4429092667996883e-05,
                  "p99": 0.000147398916305974
                },
                "candidate_energy": 5.7188866458158145,
                "cvrmse_percent": 19.671170686261608,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.09566844369428028,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.713420705145495,
                "relative_energy_error_percent": 0.09566844369428028,
                "rms_normalized_rmse_percent": 4.447558362170961,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037360225105658174,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.004099108977243304,
                  "rgb_channel": 0,
                  "sky_patch_index": 314
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006850678473711014,
                  "p50": 4.9999993478877514e-08,
                  "p90": 1.659184090385679e-05,
                  "p95": 6.901990855112672e-05,
                  "p99": 0.00022001529287081088
                },
                "candidate_energy": 3.0264190990882334,
                "cvrmse_percent": 55.59433079769495,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5742199365911744,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0438977669153147,
                "relative_energy_error_percent": 0.5742199365911744,
                "rms_normalized_rmse_percent": 2.959928003758768,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03215928561985493,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.03284435346722603,
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
                  "maximum": 0.00015829769836273044,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.1493545975530153e-07
                },
                "candidate_energy": 0.12399484877738587,
                "cvrmse_percent": 159.71250774853272,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.28941540317145265,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.12363702418537059,
                "relative_energy_error_percent": 0.28941540317145265,
                "rms_normalized_rmse_percent": 11.932988219682276,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0003003073943546042,
                  "global_sensor_index": 36,
                  "local_sensor_index": 12,
                  "reference": 0.00014200969599187374,
                  "rgb_channel": 0,
                  "sky_patch_index": 31
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00023706001229584217,
                  "p50": 0.0,
                  "p90": 2.562966187724669e-06,
                  "p95": 4.362644631328294e-06,
                  "p99": 1.5136005822569098e-05
                },
                "candidate_energy": 0.2031058985682428,
                "cvrmse_percent": 168.53677819053627,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0892182794656128,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.2029248525062286,
                "relative_energy_error_percent": 0.0892182794656128,
                "rms_normalized_rmse_percent": 8.317148981547197,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.005314630456268787,
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "reference": 0.0055516904685646296,
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
                  "maximum": 5.899905590922572e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012622009086044272,
                "cvrmse_percent": 468.6111597410739,
                "energy_difference_negligible": true,
                "nmbe_percent": 4.390827725424167,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.01209110930631141,
                "relative_energy_error_percent": 4.390827725424166,
                "rms_normalized_rmse_percent": 21.419676869163855,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00017711195687297732,
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "reference": 0.0001181129009637516,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00012083960245945491,
                  "p50": 0.0,
                  "p90": 1.7896070403367048e-07,
                  "p95": 5.041710444686487e-07,
                  "p99": 2.3764721095886773e-06
                },
                "candidate_energy": 0.02614323020699061,
                "cvrmse_percent": 381.782848181772,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -4.216408970617659,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.027294059374920465,
                "relative_energy_error_percent": 4.216408970617659,
                "rms_normalized_rmse_percent": 19.675227097575494,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -1.252740912605077e-05,
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "reference": 0.00010831219333340414,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.77275004144758,
            "full": 5484.870666987263
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.62195799220353,
            "full": 5439.972124993801
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.18891693651676,
            "full": 5459.755041985773
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.91045906301588,
            "full": 5434.5906670205295
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
            "identifier": "three_room_chain_0_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021877599647268653,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2898660972714424e-05,
                  "p99": 8.432502800132737e-05
                },
                "candidate_energy": 5.713483051549247,
                "cvrmse_percent": 11.237620619940213,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06943925510800508,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.709518404498908,
                "relative_energy_error_percent": 0.0694392551080051,
                "rms_normalized_rmse_percent": 2.5422020780119565,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013690044870600104,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.001587780483532697,
                  "rgb_channel": 0,
                  "sky_patch_index": 214
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005888352170586586,
                  "p50": 3.3358261930516164e-08,
                  "p90": 1.1562700819922611e-05,
                  "p95": 3.89464694308117e-05,
                  "p99": 0.0001274777168873693
                },
                "candidate_energy": 3.0371138351865063,
                "cvrmse_percent": 33.792206407235675,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07866820612073872,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.03950495921287,
                "relative_energy_error_percent": 0.07866820612073872,
                "rms_normalized_rmse_percent": 1.8018009609751477,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.027437915094196796,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.026849079877138138,
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
                  "maximum": 9.037509153131396e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.403533513501145e-07
                },
                "candidate_energy": 0.12410768104030012,
                "cvrmse_percent": 93.10161052010953,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.7178227551622562,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.1232231571784439,
                "relative_energy_error_percent": 0.7178227551622561,
                "rms_normalized_rmse_percent": 6.969185638211576,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0004309898504288867,
                  "global_sensor_index": 41,
                  "local_sensor_index": 17,
                  "reference": 0.00034061475889757276,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00039058993570506573,
                  "p50": 0.0,
                  "p90": 1.7337401914119255e-06,
                  "p95": 3.0008750400156714e-06,
                  "p99": 1.0199097062013532e-05
                },
                "candidate_energy": 0.20230901870638007,
                "cvrmse_percent": 133.6233981147755,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2272339375328717,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.20185034621674802,
                "relative_energy_error_percent": 0.2272339375328717,
                "rms_normalized_rmse_percent": 6.665159878306104,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.005606830352917314,
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "reference": 0.005216240417212248,
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
                  "maximum": 5.4572396038565785e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.012448044149550697,
                "cvrmse_percent": 311.0953379010274,
                "energy_difference_negligible": true,
                "nmbe_percent": 2.4804511806465923,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.012146749947078206,
                "relative_energy_error_percent": 2.4804511806465928,
                "rms_normalized_rmse_percent": 14.801997942016646,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00027280714857624844,
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "reference": 0.00021823475253768265,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 6.402484359568916e-05,
                  "p50": 0.0,
                  "p90": 1.7722329559433092e-07,
                  "p95": 4.5902997669600154e-07,
                  "p99": 1.7896649389114844e-06
                },
                "candidate_energy": 0.027547856025719852,
                "cvrmse_percent": 214.59339153875223,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.755845731087082,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.027072504609240156,
                "relative_energy_error_percent": 1.755845731087082,
                "rms_normalized_rmse_percent": 10.962536131610412,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 2.8609698347281665e-05,
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "reference": -3.54151452484075e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 332.55037502385676,
            "full": 9538.006542017683
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 335.6977499788627,
            "full": 9713.916791952215
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 376.8854170339182,
            "full": 9589.475916931406
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 349.6567499823868,
            "full": 9470.868707983755
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
    "/content/suite-vulkan-0.3.3/three_room_chain/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11117.823707987554,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 43345.719999982975,
      "invocation_count": 5,
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
    "passed": false,
    "matrix_shape": [
      72,
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2448804731699679,
            "cvrmse_percent": 3.4138956272511325,
            "rms_normalized_rmse_percent": 0.7731947466354423,
            "reference_energy": 5.711498077331143,
            "candidate_energy": 5.697511733814281,
            "relative_energy_error_percent": 0.2448804731699679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
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
            "nmbe_percent": -0.6774298436386301,
            "cvrmse_percent": 33.187222193956366,
            "rms_normalized_rmse_percent": 1.7684510242719518,
            "reference_energy": 3.0383120522718823,
            "candidate_energy": 3.017729619686923,
            "relative_energy_error_percent": 0.6774298436386301,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 1.2222280929563567e-05,
              "p95": 2.159532596124336e-05,
              "p99": 6.07257359661158e-05,
              "maximum": 0.000862903892993927
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032444894313812256,
              "candidate": 0.03158199042081833,
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
            "nmbe_percent": -0.39508029991262855,
            "cvrmse_percent": 11.372011618276133,
            "rms_normalized_rmse_percent": 1.745121548624021,
            "reference_energy": 8.749810129603025,
            "candidate_energy": 8.715241353501204,
            "relative_energy_error_percent": 0.39508029991262855,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.1432981409598142e-05,
              "p95": 2.003058762056753e-05,
              "p99": 5.81109430640935e-05,
              "maximum": 0.000862903892993927
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032444894313812256,
              "candidate": 0.03158199042081833,
              "position": [
                1.5,
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
            "nmbe_percent": -1.0918922670345363,
            "cvrmse_percent": 22.680069603761705,
            "rms_normalized_rmse_percent": 1.7143493775967928,
            "reference_energy": 0.12371659678625235,
            "candidate_energy": 0.12236574483290497,
            "relative_energy_error_percent": 1.0918922670345363,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0022908099926213e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.9440859198032808,
            "cvrmse_percent": 67.60120759404565,
            "rms_normalized_rmse_percent": 3.355387041713242,
            "reference_energy": 0.20202850468273326,
            "candidate_energy": 0.20393582734943205,
            "relative_energy_error_percent": 0.9440859198032807,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9034466731682187e-06,
              "p95": 3.2289940463670064e-06,
              "p99": 1.0153052426176064e-05,
              "maximum": 0.0001237745163962245
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0018249654676765203,
              "candidate": 0.0019487399840727448,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.17083010944506588,
            "cvrmse_percent": 41.06921549841494,
            "rms_normalized_rmse_percent": 3.2867738283450576,
            "reference_energy": 0.3257451014689856,
            "candidate_energy": 0.326301572182337,
            "relative_energy_error_percent": 0.1708301094450659,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8592254491522908e-06,
              "p95": 3.134690814476926e-06,
              "p99": 8.671398495607679e-06,
              "maximum": 0.0001237745163962245
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0018249654676765203,
              "candidate": 0.0019487399840727448,
              "position": [
                3.5,
                6.5,
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
            "nmbe_percent": -0.20369524204265252,
            "cvrmse_percent": 32.40889657703593,
            "rms_normalized_rmse_percent": 1.5352127310331811,
            "reference_energy": 0.012260786407566115,
            "candidate_energy": 0.012235811769016891,
            "relative_energy_error_percent": 0.2036952420426525,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955620847293176e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627296943450347e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 4.715906565079044,
            "cvrmse_percent": 165.13208838354325,
            "rms_normalized_rmse_percent": 8.445656569887719,
            "reference_energy": 0.027346790895238726,
            "candidate_energy": 0.028636440002405728,
            "relative_energy_error_percent": 4.7159065650790435,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.923615684518154e-07,
              "p95": 4.461127502963791e-07,
              "p99": 1.823376839382711e-06,
              "maximum": 5.098598194308579e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00038012402364984155,
              "candidate": 0.00043111000559292734,
              "position": [
                2.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 3.1930114254380766,
            "cvrmse_percent": 113.44777052951629,
            "rms_normalized_rmse_percent": 8.403686030151706,
            "reference_energy": 0.03960757730280484,
            "candidate_energy": 0.04087225177142262,
            "relative_energy_error_percent": 3.1930114254380766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9281544894056424e-07,
              "p95": 4.4456598402575764e-07,
              "p99": 1.8407131797459612e-06,
              "maximum": 5.098598194308579e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00038012402364984155,
              "candidate": 0.00043111000559292734,
              "position": [
                2.5,
                11.5,
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2448804731699679,
            "cvrmse_percent": 3.4138956272511325,
            "rms_normalized_rmse_percent": 0.7731947466354423,
            "reference_energy": 5.711498077331143,
            "candidate_energy": 5.697511733814281,
            "relative_energy_error_percent": 0.2448804731699679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
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
            "nmbe_percent": 77.17923255843529,
            "cvrmse_percent": 845.7014265317861,
            "rms_normalized_rmse_percent": 32.592196318420484,
            "reference_energy": 1.7032072981192359,
            "candidate_energy": 3.017729619686923,
            "relative_energy_error_percent": 77.17923255843529,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.175308953970671e-05,
              "p95": 8.177780546247959e-05,
              "p99": 0.0001480759106925681,
              "maximum": 0.009829163551330566
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014388445764780045,
              "candidate": 0.02421760931611061,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.53995488960111,
            "cvrmse_percent": 194.24735633798596,
            "rms_normalized_rmse_percent": 32.58952802816003,
            "reference_energy": 7.414705375450379,
            "candidate_energy": 8.715241353501204,
            "relative_energy_error_percent": 17.539954889601113,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.098999801906757e-05,
              "p95": 8.144821913447231e-05,
              "p99": 0.00014806967228650999,
              "maximum": 0.009829163551330566
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014388445764780045,
              "candidate": 0.02421760931611061,
              "position": [
                5.5,
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
            "nmbe_percent": -1.0918922670345363,
            "cvrmse_percent": 22.680069603761705,
            "rms_normalized_rmse_percent": 1.7143493775967928,
            "reference_energy": 0.12371659678625235,
            "candidate_energy": 0.12236574483290497,
            "relative_energy_error_percent": 1.0918922670345363,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0022908099926213e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 138.02364126071043,
            "cvrmse_percent": 1641.0630514480486,
            "rms_normalized_rmse_percent": 48.29431230865658,
            "reference_energy": 0.08567881167991143,
            "candidate_energy": 0.20393582734943205,
            "relative_energy_error_percent": 138.02364126071043,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.579999767884146e-06,
              "p95": 8.689999958733097e-06,
              "p99": 2.2141250173035432e-05,
              "maximum": 0.0016061330679804087
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037462867330759764,
              "candidate": 0.005352419801056385,
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
            "nmbe_percent": 55.83033771968506,
            "cvrmse_percent": 671.389841526567,
            "rms_normalized_rmse_percent": 48.28799850844945,
            "reference_energy": 0.20939540846616378,
            "candidate_energy": 0.326301572182337,
            "relative_energy_error_percent": 55.83033771968506,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.4899998101755045e-06,
              "p95": 8.459999662591144e-06,
              "p99": 2.1849671747986287e-05,
              "maximum": 0.0016061330679804087
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037462867330759764,
              "candidate": 0.005352419801056385,
              "position": [
                3.5,
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
            "nmbe_percent": -0.20369524204265252,
            "cvrmse_percent": 32.40889657703593,
            "rms_normalized_rmse_percent": 1.5352127310331811,
            "reference_energy": 0.012260786407566115,
            "candidate_energy": 0.012235811769016891,
            "relative_energy_error_percent": 0.2036952420426525,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955620847293176e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627296943450347e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 130.40580844998846,
            "cvrmse_percent": 1808.389781303847,
            "rms_normalized_rmse_percent": 56.81495267463772,
            "reference_energy": 0.012428697086697582,
            "candidate_energy": 0.028636440002405728,
            "relative_energy_error_percent": 130.40580844998846,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.500000053056283e-07,
              "p95": 4.700000033608376e-07,
              "p99": 5.331444071998523e-06,
              "maximum": 0.0002025084540946409
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00016092155419755727,
              "candidate": 0.0003634300082921982,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 65.54518761366066,
            "cvrmse_percent": 909.6943887123354,
            "rms_normalized_rmse_percent": 56.774395902601945,
            "reference_energy": 0.024689483494263698,
            "candidate_energy": 0.04087225177142262,
            "relative_energy_error_percent": 65.54518761366066,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.500000053056283e-07,
              "p95": 4.700000033608376e-07,
              "p99": 4.9124921247311815e-06,
              "maximum": 0.0002025084540946409
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00016092155419755727,
              "candidate": 0.0003634300082921982,
              "position": [
                2.5,
                8.5,
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
      "bias_percent": -0.030448193326375605,
      "rms_normalized_error_percent": 0.2023613894334459,
      "absolute_error": {
        "p95": 0.06498762031882378,
        "p99": 0.12518658343666325,
        "maximum": 0.1324329655917591
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.707879131221393,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2023613894334459
    },
    "overcast": {
      "bias_percent": -0.039149654708229314,
      "rms_normalized_error_percent": 0.14218008135989055,
      "absolute_error": {
        "p95": 0.03032728433609009,
        "p99": 0.06680956840515145,
        "maximum": 0.07744288444519043
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6918563842773438,
      "reference_fraction_of_uniform": 0.6468000411987305,
      "rms_normalized_to_uniform_percent": 0.1010976615329589
    },
    "horizon": {
      "bias_percent": 0.5923372411411058,
      "rms_normalized_error_percent": 1.886230273965168,
      "absolute_error": {
        "p95": 0.04273987333929754,
        "p99": 0.07638625212442803,
        "maximum": 0.0866155825421524
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6118609881012154,
      "reference_fraction_of_uniform": 0.1071958557696871,
      "rms_normalized_to_uniform_percent": 0.12404631496613147
    },
    "north": {
      "bias_percent": -89.8693866180831,
      "rms_normalized_error_percent": 99.21855339849294,
      "absolute_error": {
        "p95": 3.65858602890512e-05,
        "p99": 9.593774178256354e-05,
        "maximum": 9.71217014011927e-05
      },
      "worst_index": [
        55
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 7.181067758210702e-06,
      "reference_fraction_of_uniform": 1.2580974271259038e-06,
      "rms_normalized_to_uniform_percent": 0.00013643582242504738
    },
    "east": {
      "bias_percent": 0.1542894774744646,
      "rms_normalized_error_percent": 0.19836567570322086,
      "absolute_error": {
        "p95": 0.015211331844329838,
        "p99": 0.02302090406417847,
        "maximum": 0.02348184585571289
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.087052583694458,
      "reference_fraction_of_uniform": 0.19044771790504456,
      "rms_normalized_to_uniform_percent": 0.04004414761504207
    },
    "south": {
      "bias_percent": -0.04871912436282547,
      "rms_normalized_error_percent": 0.2890997568728099,
      "absolute_error": {
        "p95": 0.07043323516845704,
        "p99": 0.11530158996582039,
        "maximum": 0.12401056289672852
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9264891147613525,
      "reference_fraction_of_uniform": 0.6879068613052368,
      "rms_normalized_to_uniform_percent": 0.18867115189979858
    },
    "west": {
      "bias_percent": 0.016056157752837134,
      "rms_normalized_error_percent": 0.15700026461829483,
      "absolute_error": {
        "p95": 0.011463655531406405,
        "p99": 0.01539807081222535,
        "maximum": 0.016280174255371094
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1000711917877197,
      "reference_fraction_of_uniform": 0.19272853434085846,
      "rms_normalized_to_uniform_percent": 0.03194087453190417
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
          "nmbe_percent": -0.028120759390245543,
          "cvrmse_percent": 1.6493832566661506,
          "absolute_error_percentiles_lux": {
            "p50": 2.4667205810546875,
            "p90": 28.852032470703136,
            "p95": 46.070431518554656,
            "p99": 105.78763427734374
          },
          "maximum_absolute_error_lux": 620.4404296875,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              3.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 10219.7197265625,
            "radiance_lux": 10840.16015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.18934931506849395,
            "maximum_error_percentage_points": 0.7126027397260302,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08626097017658048,
            "maximum_error_percentage_points": 0.2999627037734385,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0561073059360729,
            "maximum_error_percentage_points": 0.32890410958904326,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.059320776255708196,
            "maximum_error_percentage_points": 0.278630136986294,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027488584474885724,
            "maximum_error_percentage_points": 0.11123287671232873,
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
          "nmbe_percent": -0.5759179313294367,
          "cvrmse_percent": 10.220208406213246,
          "absolute_error_percentiles_lux": {
            "p50": 0.37699127197265625,
            "p90": 4.835018920898439,
            "p95": 7.403493499755855,
            "p99": 15.620696392059301
          },
          "maximum_absolute_error_lux": 113.9443359375,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 4916.8896484375,
            "radiance_lux": 4802.9453125
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.03480022831050227,
            "maximum_error_percentage_points": 0.219041095890411,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15106215643959756,
            "maximum_error_percentage_points": 0.4366000479500798,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.20626712328767263,
            "maximum_error_percentage_points": 1.7491780821917757,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2071061643835618,
            "maximum_error_percentage_points": 1.7491780821917828,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0013584474885844748,
            "maximum_error_percentage_points": 0.031369863013698596,
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
          "nmbe_percent": 1.8245409855016483,
          "cvrmse_percent": 23.20871217775693,
          "absolute_error_percentiles_lux": {
            "p50": 0.07573521137237549,
            "p90": 0.7354948997497559,
            "p95": 1.2810009241104123,
            "p99": 2.9471092796325675
          },
          "maximum_absolute_error_lux": 36.53326416015625,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              8.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 558.4498291015625,
            "radiance_lux": 594.9830932617188
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.005559360730593608,
            "maximum_error_percentage_points": 0.08136986301369861,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.060808211542125644,
            "maximum_error_percentage_points": 0.3235576412585264,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.012773972602740121,
            "maximum_error_percentage_points": 0.11164383561643376,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.012773972602739736,
            "maximum_error_percentage_points": 0.11164383561643842,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004717465753415695,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004729539008989647,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.00478594218214895,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0045205479452054,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.003972602739725994,
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
      "study_preparation_seconds": 0.35730147499998566,
      "weather_seconds": 0.2332839979999335,
      "metric_reduction_seconds": 1.8050931539999056,
      "write_seconds": 0.013585216000137734,
      "total_seconds": 2.0523744429999624,
      "cold_end_to_end_seconds": 2.409675917999948,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00251400799993462,
      "engine_upload_seconds": 0.045684199,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.069467728,
      "engine_annual_reduction_seconds": 0.082668851,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.069467728
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35730147499998566,
      "weather_seconds": 0.2284677779998674,
      "metric_reduction_seconds": 1.6973761649999233,
      "write_seconds": 0.014184080999939397,
      "total_seconds": 1.9404338619999635,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.9404338619999635,
      "raw_export_seconds": 0.002756747999910658,
      "engine_upload_seconds": 0.04562175,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.04e-07,
      "engine_annual_reduction_seconds": 0.085765096,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02251799500004381,
      "full": 0.10226834200011581
    }
  },
  "elapsed_seconds": 8.01559764600006,
  "result_class": "unstable_reference"
}
```
