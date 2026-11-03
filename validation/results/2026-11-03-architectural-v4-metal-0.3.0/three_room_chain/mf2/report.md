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
  "model_sha256": "c73e78d0633e70c94d7b9a9722cc6b7d5c69587d8d1b9d2393006289ce4d078c",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1666965602579954223,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1666965602579954223,
      "basis": "ReinhartMf2",
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": false,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.04453063170271223,
        "rms_normalized_error_percent": 0.745993439904148,
        "absolute_error": {
          "p95": 1.200605765916407e-07,
          "p99": 9.124496136790706e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          11,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.49130191256348316,
        "rms_normalized_error_percent": 1.4185961332525538,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.0848380043171035e-07,
          "maximum": 2.361941005801782e-05
        },
        "worst_index": [
          17,
          153,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.39350986750028416,
        "rms_normalized_error_percent": 2.743436849982268,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 9.880026482278481e-06
        },
        "worst_index": [
          11,
          89,
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
    "passed": false,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.035205678493143856,
        "rms_normalized_error_percent": 1.6328193107415667,
        "absolute_error": {
          "p95": 3.4488504752516747e-05,
          "p99": 0.00010948056587949385,
          "maximum": 0.0004243087023496628
        },
        "worst_index": [
          7,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.7219096371953452,
        "rms_normalized_error_percent": 4.329166776176263,
        "absolute_error": {
          "p95": 3.0226556191337295e-06,
          "p99": 1.0903861402766652e-05,
          "maximum": 0.0001586833968758583
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": -0.7889985327014579,
        "rms_normalized_error_percent": 10.368941857914729,
        "absolute_error": {
          "p95": 4.866872131970013e-07,
          "p99": 1.9616367126217876e-06,
          "maximum": 7.107639976311475e-05
        },
        "worst_index": [
          11,
          91,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": false,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.01716275813960776,
        "rms_normalized_error_percent": 1.4046892211342745,
        "absolute_error": {
          "p95": 2.895425132010132e-05,
          "p99": 9.316978394053854e-05,
          "maximum": 0.0004832819104194641
        },
        "worst_index": [
          10,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": -0.3323457519856325,
        "rms_normalized_error_percent": 3.796068433558398,
        "absolute_error": {
          "p95": 2.659129734183807e-06,
          "p99": 9.075434172700493e-06,
          "maximum": 0.00010965252295136452
        },
        "worst_index": [
          12,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 1.3624333354408436,
        "rms_normalized_error_percent": 9.993060973542415,
        "absolute_error": {
          "p95": 4.0975949033850156e-07,
          "p99": 1.7681911231192323e-06,
          "maximum": 5.328716360963881e-05
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": false
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 12,
        "half_run_count": 6,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04345471065272287,
                "cvrmse_percent": 20.36231482090884,
                "rms_normalized_rmse_percent": 4.606510509727311,
                "reference_energy": 5.712041308699781,
                "candidate_energy": 5.714523459722841,
                "relative_energy_error_percent": 0.04345471065272273,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.39381692558527e-05,
                  "p99": 0.0001523515238659453,
                  "maximum": 0.00036201179803659533
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 415,
                  "rgb_channel": 0,
                  "reference": 0.0036444688060631356,
                  "candidate": 0.0032824570080265403
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.3514141993120835,
                "cvrmse_percent": 103.70721987976982,
                "rms_normalized_rmse_percent": 3.997426971120015,
                "reference_energy": 1.7044177898935118,
                "candidate_energy": 1.6984282237642248,
                "relative_energy_error_percent": 0.35141419931208545,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.156610081437975e-06,
                  "p95": 6.457213263881081e-05,
                  "p99": 0.00023314410682360147,
                  "maximum": 0.000550360147220393
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 204,
                  "rgb_channel": 0,
                  "reference": -0.00031970163884883124,
                  "candidate": 0.00023065850837156177
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.2571263467105736,
                "cvrmse_percent": 179.79819292146132,
                "rms_normalized_rmse_percent": 13.500592948647544,
                "reference_energy": 0.12326476313796775,
                "candidate_energy": 0.12358170932020585,
                "relative_energy_error_percent": 0.2571263467105735,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.820809782463213e-07,
                  "maximum": 0.0002049125760095194
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.0005925536243012175,
                  "candidate": 0.0007974662003107369
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.8193181828821299,
                "cvrmse_percent": 371.9815176841515,
                "rms_normalized_rmse_percent": 11.102570905141027,
                "reference_energy": 0.0867614071661329,
                "candidate_energy": 0.08518294110983504,
                "relative_energy_error_percent": 1.8193181828821308,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4783907450540206e-05,
                  "maximum": 0.00029042038174035645
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 150,
                  "rgb_channel": 0,
                  "reference": -0.00015974073903635144,
                  "candidate": 0.00013067964270400503
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 3.0961862792496286,
                "cvrmse_percent": 386.6840429878319,
                "rms_normalized_rmse_percent": 18.410888900079602,
                "reference_energy": 0.012050780534991645,
                "candidate_energy": 0.012423895148458541,
                "relative_energy_error_percent": 3.096186279249627,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.659910190540056e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 9,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00013588438378064893,
                  "candidate": 7.928528187524837e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.4980195604239277,
                "cvrmse_percent": 528.0073962194547,
                "rms_normalized_rmse_percent": 16.699887498113377,
                "reference_energy": 0.012359571493050225,
                "candidate_energy": 0.012544720291600697,
                "relative_energy_error_percent": 1.498019560423926,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.056033230886283e-07,
                  "maximum": 5.918800646516806e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.00013601157722102167,
                  "candidate": 0.00019519958368618973
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.82291689701378,
            "full": 414.75208301562816
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.39799998421222,
            "full": 407.1347080171108
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.99291593953967,
            "full": 433.76270798034966
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.11079192440957,
            "full": 404.9526669550687
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.70879201125354,
            "full": 412.0353750186041
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.47095795813948,
            "full": 405.33037506975234
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.3057499481365,
            "full": 428.9021249860525
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.678542050533,
            "full": 412.89579099975526
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.55412504728884,
            "full": 417.8212909027934
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.897709001787,
            "full": 454.79758305009454
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.53154207393527,
            "full": 432.701374986209
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.240916993469,
            "full": 403.59729202464223
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.02658842449924656,
                "cvrmse_percent": 19.328183011326928,
                "rms_normalized_rmse_percent": 4.370479134470445,
                "reference_energy": 5.711608426521366,
                "candidate_energy": 5.713127053215544,
                "relative_energy_error_percent": 0.02658842449924656,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.336118399805855e-05,
                  "p99": 0.00013998392387293263,
                  "maximum": 0.00036213849671185017
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 314,
                  "rgb_channel": 0,
                  "reference": 0.004030829528346658,
                  "candidate": 0.0036686910316348076
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.27908417119716916,
                "cvrmse_percent": 56.2661937161844,
                "rms_normalized_rmse_percent": 2.9981844669361872,
                "reference_energy": 3.040106715796547,
                "candidate_energy": 3.031622259165257,
                "relative_energy_error_percent": 0.2790841711971691,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.901119332600956e-08,
                  "p90": 1.670283018029295e-05,
                  "p95": 6.238347850739956e-05,
                  "p99": 0.0002119970376952546,
                  "maximum": 0.0007498450577259064
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028535310178995132,
                  "candidate": 0.027785465121269226
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.45437062101451164,
                "cvrmse_percent": 165.12666008814512,
                "rms_normalized_rmse_percent": 12.343324919219699,
                "reference_energy": 0.12360140418161336,
                "candidate_energy": 0.12303979571385071,
                "relative_energy_error_percent": 0.45437062101451164,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.548439242547835e-07,
                  "maximum": 0.00013703558943234384
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.0007058052869979292,
                  "candidate": 0.0005687696975655854
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.753665719131002,
                "cvrmse_percent": 184.38467784177502,
                "rms_normalized_rmse_percent": 9.078855177641378,
                "reference_energy": 0.20041297264456048,
                "candidate_energy": 0.20192341651607393,
                "relative_energy_error_percent": 0.7536657191310019,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.592055778904978e-06,
                  "p95": 4.383006398711586e-06,
                  "p99": 1.8514736602526027e-05,
                  "maximum": 0.0004362170584499836
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.005259473342448473,
                  "candidate": 0.005695690400898457
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 3.4742922232980793,
                "cvrmse_percent": 694.7030740618646,
                "rms_normalized_rmse_percent": 32.15293518483462,
                "reference_energy": 0.012448479829799908,
                "candidate_energy": 0.012880976396445476,
                "relative_energy_error_percent": 3.4742922232980797,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0001182177074952051
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00016841274918988347,
                  "candidate": 0.0002866304566850886
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -5.956883870537984,
                "cvrmse_percent": 493.70861861597376,
                "rms_normalized_rmse_percent": 25.17828157445311,
                "reference_energy": 0.0275415390768039,
                "candidate_energy": 0.025900921577839853,
                "relative_energy_error_percent": 5.956883870537984,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.824219992840881e-07,
                  "p95": 5.100460285234476e-07,
                  "p99": 2.45177565716401e-06,
                  "maximum": 0.00020536880037980154
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 7.672009087400511e-05,
                  "candidate": -0.00012864870950579643
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.53891701437533,
            "full": 5166.397624998353
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.26587497908622,
            "full": 5180.401833029464
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.5167500069365,
            "full": 5248.420082964003
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 212.5172090018168,
            "full": 5192.733083968051
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09566844369428028,
                "cvrmse_percent": 19.671170686261608,
                "rms_normalized_rmse_percent": 4.447558362170961,
                "reference_energy": 5.713420705145495,
                "candidate_energy": 5.7188866458158145,
                "relative_energy_error_percent": 0.09566844369428028,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4429092667996883e-05,
                  "p99": 0.000147398916305974,
                  "maximum": 0.0003630864666774869
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 314,
                  "rgb_channel": 0,
                  "reference": 0.004099108977243304,
                  "candidate": 0.0037360225105658174
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.5742199365911744,
                "cvrmse_percent": 55.59433079769495,
                "rms_normalized_rmse_percent": 2.959928003758768,
                "reference_energy": 3.0438977669153147,
                "candidate_energy": 3.0264190990882334,
                "relative_energy_error_percent": 0.5742199365911744,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.9999993478877514e-08,
                  "p90": 1.659184090385679e-05,
                  "p95": 6.901990855112672e-05,
                  "p99": 0.00022001529287081088,
                  "maximum": 0.0006850678473711014
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03284435346722603,
                  "candidate": 0.03215928561985493
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.28941540317145265,
                "cvrmse_percent": 159.71250774853272,
                "rms_normalized_rmse_percent": 11.932988219682276,
                "reference_energy": 0.12363702418537059,
                "candidate_energy": 0.12399484877738587,
                "relative_energy_error_percent": 0.28941540317145265,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.1493545975530153e-07,
                  "maximum": 0.00015829769836273044
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 12,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.00014200969599187374,
                  "candidate": 0.0003003073943546042
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0892182794656128,
                "cvrmse_percent": 168.53677819053627,
                "rms_normalized_rmse_percent": 8.317148981547197,
                "reference_energy": 0.2029248525062286,
                "candidate_energy": 0.2031058985682428,
                "relative_energy_error_percent": 0.0892182794656128,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.562966187724669e-06,
                  "p95": 4.362644631328294e-06,
                  "p99": 1.5136005822569098e-05,
                  "maximum": 0.00023706001229584217
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0055516904685646296,
                  "candidate": 0.005314630456268787
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 4.390827725424167,
                "cvrmse_percent": 468.6111597410739,
                "rms_normalized_rmse_percent": 21.419676869163855,
                "reference_energy": 0.01209110930631141,
                "candidate_energy": 0.012622009086044272,
                "relative_energy_error_percent": 4.390827725424166,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.899905590922572e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.0001181129009637516,
                  "candidate": 0.00017711195687297732
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -4.216408970617659,
                "cvrmse_percent": 381.782848181772,
                "rms_normalized_rmse_percent": 19.675227097575494,
                "reference_energy": 0.027294059374920465,
                "candidate_energy": 0.02614323020699061,
                "relative_energy_error_percent": 4.216408970617659,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7896070403367048e-07,
                  "p95": 5.041710444686487e-07,
                  "p99": 2.3764721095886773e-06,
                  "maximum": 0.00012083960245945491
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00010831219333340414,
                  "candidate": -1.252740912605077e-05
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.77275004144758,
            "full": 5484.870666987263
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.62195799220353,
            "full": 5439.972124993801
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.18891693651676,
            "full": 5459.755041985773
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 225.91045906301588,
            "full": 5434.5906670205295
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06943925510800508,
                "cvrmse_percent": 11.237620619940213,
                "rms_normalized_rmse_percent": 2.5422020780119565,
                "reference_energy": 5.709518404498908,
                "candidate_energy": 5.713483051549247,
                "relative_energy_error_percent": 0.0694392551080051,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2898660972714424e-05,
                  "p99": 8.432502800132737e-05,
                  "maximum": 0.00021877599647268653
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 214,
                  "rgb_channel": 0,
                  "reference": 0.001587780483532697,
                  "candidate": 0.0013690044870600104
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.07866820612073872,
                "cvrmse_percent": 33.792206407235675,
                "rms_normalized_rmse_percent": 1.8018009609751477,
                "reference_energy": 3.03950495921287,
                "candidate_energy": 3.0371138351865063,
                "relative_energy_error_percent": 0.07866820612073872,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.3358261930516164e-08,
                  "p90": 1.1562700819922611e-05,
                  "p95": 3.89464694308117e-05,
                  "p99": 0.0001274777168873693,
                  "maximum": 0.0005888352170586586
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.026849079877138138,
                  "candidate": 0.027437915094196796
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.7178227551622562,
                "cvrmse_percent": 93.10161052010953,
                "rms_normalized_rmse_percent": 6.969185638211576,
                "reference_energy": 0.1232231571784439,
                "candidate_energy": 0.12410768104030012,
                "relative_energy_error_percent": 0.7178227551622561,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.403533513501145e-07,
                  "maximum": 9.037509153131396e-05
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 17,
                  "sky_patch_index": 93,
                  "rgb_channel": 0,
                  "reference": 0.00034061475889757276,
                  "candidate": 0.0004309898504288867
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2272339375328717,
                "cvrmse_percent": 133.6233981147755,
                "rms_normalized_rmse_percent": 6.665159878306104,
                "reference_energy": 0.20185034621674802,
                "candidate_energy": 0.20230901870638007,
                "relative_energy_error_percent": 0.2272339375328717,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7337401914119255e-06,
                  "p95": 3.0008750400156714e-06,
                  "p99": 1.0199097062013532e-05,
                  "maximum": 0.00039058993570506573
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.005216240417212248,
                  "candidate": 0.005606830352917314
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 2.4804511806465923,
                "cvrmse_percent": 311.0953379010274,
                "rms_normalized_rmse_percent": 14.801997942016646,
                "reference_energy": 0.012146749947078206,
                "candidate_energy": 0.012448044149550697,
                "relative_energy_error_percent": 2.4804511806465928,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.4572396038565785e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.00021823475253768265,
                  "candidate": 0.00027280714857624844
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.755845731087082,
                "cvrmse_percent": 214.59339153875223,
                "rms_normalized_rmse_percent": 10.962536131610412,
                "reference_energy": 0.027072504609240156,
                "candidate_energy": 0.027547856025719852,
                "relative_energy_error_percent": 1.755845731087082,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7722329559433092e-07,
                  "p95": 4.5902997669600154e-07,
                  "p99": 1.7896649389114844e-06,
                  "maximum": 6.402484359568916e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": -3.54151452484075e-05,
                  "candidate": 2.8609698347281665e-05
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 332.55037502385676,
            "full": 9538.006542017683
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 335.6977499788627,
            "full": 9713.916791952215
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 376.8854170339182,
            "full": 9589.475916931406
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 349.6567499823868,
            "full": 9470.868707983755
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/three_room_chain/mf2/oracle/scene.rad"
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 11117.823707987554,
      "worker_pool_size": 12,
      "invocation_count": 5
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 43345.719999982975,
      "worker_pool_size": 12,
      "invocation_count": 5
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
            "nmbe_percent": -0.2448785728803501,
            "cvrmse_percent": 3.4138967425627205,
            "rms_normalized_rmse_percent": 0.7731949992363285,
            "reference_energy": 5.711498077331143,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.2448785728803501,
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
            "nmbe_percent": -0.6768505138115741,
            "cvrmse_percent": 33.170700376657216,
            "rms_normalized_rmse_percent": 1.7675706244435252,
            "reference_energy": 3.0383120522718823,
            "candidate_energy": 3.017747221534881,
            "relative_energy_error_percent": 0.676850513811574,
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
            "nmbe_percent": -0.39487789114374666,
            "cvrmse_percent": 11.366185517261743,
            "rms_normalized_rmse_percent": 1.7442274891764968,
            "reference_energy": 8.749810129603025,
            "candidate_energy": 8.715259063884167,
            "relative_energy_error_percent": 0.39487789114374666,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.1432981409598142e-05,
              "p95": 2.003058762056753e-05,
              "p99": 5.81107451580464e-05,
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
            "nmbe_percent": -1.0918839533869233,
            "cvrmse_percent": 22.680064446312752,
            "rms_normalized_rmse_percent": 1.7143489877536593,
            "reference_energy": 0.12371659678625235,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0918839533869236,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
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
            "nmbe_percent": 0.9450512682762388,
            "cvrmse_percent": 67.60852564789035,
            "rms_normalized_rmse_percent": 3.3557502734352034,
            "reference_energy": 0.20202850468273326,
            "candidate_energy": 0.20393777762851695,
            "relative_energy_error_percent": 0.9450512682762388,
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
            "nmbe_percent": 0.17143198018324393,
            "cvrmse_percent": 41.0738486373877,
            "rms_normalized_rmse_percent": 3.28714461896606,
            "reference_energy": 0.3257451014689856,
            "candidate_energy": 0.3263035327467838,
            "relative_energy_error_percent": 0.17143198018324393,
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
            "nmbe_percent": -0.2036838689882519,
            "cvrmse_percent": 32.408839648835645,
            "rms_normalized_rmse_percent": 1.5352100343385366,
            "reference_energy": 0.012260786407566115,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.2036838689882519,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 4.716016235449035,
            "cvrmse_percent": 165.13412989668728,
            "rms_normalized_rmse_percent": 8.445760982779642,
            "reference_energy": 0.027346790895238726,
            "candidate_energy": 0.028636469993732483,
            "relative_energy_error_percent": 4.716016235449034,
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
            "nmbe_percent": 3.1930906672266453,
            "cvrmse_percent": 113.44919955459311,
            "rms_normalized_rmse_percent": 8.40379188571871,
            "reference_energy": 0.03960757730280484,
            "candidate_energy": 0.04087228315717528,
            "relative_energy_error_percent": 3.1930906672266453,
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
            "nmbe_percent": -0.2448785728803501,
            "cvrmse_percent": 3.4138967425627205,
            "rms_normalized_rmse_percent": 0.7731949992363285,
            "reference_energy": 5.711498077331143,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.2448785728803501,
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
            "nmbe_percent": 77.1802635763863,
            "cvrmse_percent": 845.7240843356051,
            "rms_normalized_rmse_percent": 32.593069452446706,
            "reference_energy": 1.7032073215275831,
            "candidate_energy": 3.017747221534881,
            "relative_energy_error_percent": 77.1802635763863,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.175308953970671e-05,
              "p95": 8.177780546247959e-05,
              "p99": 0.00014807579427724628,
              "maximum": 0.009829162620007992
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01438844669610262,
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
            "nmbe_percent": 17.540193373368854,
            "cvrmse_percent": 194.25256276202708,
            "rms_normalized_rmse_percent": 32.590401115019894,
            "reference_energy": 7.414705398858726,
            "candidate_energy": 8.715259063884167,
            "relative_energy_error_percent": 17.54019337336885,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.098999801906757e-05,
              "p95": 8.144819003064185e-05,
              "p99": 0.00014806985273025882,
              "maximum": 0.009829162620007992
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01438844669610262,
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
            "nmbe_percent": -1.0918839533869233,
            "cvrmse_percent": 22.680064446312752,
            "rms_normalized_rmse_percent": 1.7143489877536593,
            "reference_energy": 0.12371659678625235,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0918839533869236,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
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
            "nmbe_percent": 138.02591699019038,
            "cvrmse_percent": 1641.0566685210003,
            "rms_normalized_rmse_percent": 48.29412364481266,
            "reference_energy": 0.0856788118736338,
            "candidate_energy": 0.20393777762851695,
            "relative_energy_error_percent": 138.02591699019035,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.579999767884146e-06,
              "p95": 8.689999958733097e-06,
              "p99": 2.2141250173035432e-05,
              "maximum": 0.0016061326023191214
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037462871987372637,
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
            "nmbe_percent": 55.831273873243106,
            "cvrmse_percent": 671.3872328920492,
            "rms_normalized_rmse_percent": 48.287810001925465,
            "reference_energy": 0.20939540865988615,
            "candidate_energy": 0.3263035327467838,
            "relative_energy_error_percent": 55.83127387324311,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.4899998101755045e-06,
              "p95": 8.459999662591144e-06,
              "p99": 2.1849665563422314e-05,
              "maximum": 0.0016061326023191214
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037462871987372637,
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
            "nmbe_percent": -0.2036838689882519,
            "cvrmse_percent": 32.408839648835645,
            "rms_normalized_rmse_percent": 1.5352100343385366,
            "reference_energy": 0.012260786407566115,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.2036838689882519,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 130.40603945746435,
            "cvrmse_percent": 1808.3913497348324,
            "rms_normalized_rmse_percent": 56.81500258942401,
            "reference_energy": 0.012428697642285158,
            "candidate_energy": 0.028636469993732483,
            "relative_energy_error_percent": 130.40603945746435,
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
            "nmbe_percent": 65.54531101034284,
            "cvrmse_percent": 909.6952123560458,
            "rms_normalized_rmse_percent": 56.774446684470156,
            "reference_energy": 0.024689484049851274,
            "candidate_energy": 0.04087228315717528,
            "relative_energy_error_percent": 65.54531101034284,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.500000053056283e-07,
              "p95": 4.700000033608376e-07,
              "p99": 4.9124925112664296e-06,
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
      "bias_percent": -0.03041689824811685,
      "rms_normalized_error_percent": 0.2024149666545925,
      "absolute_error": {
        "p95": 0.06498749808892043,
        "p99": 0.12519715110080487,
        "maximum": 0.13247400540556242
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.707879131221393,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2024149666545925
    },
    "overcast": {
      "bias_percent": -0.039043659776372766,
      "rms_normalized_error_percent": 0.14224922624700206,
      "absolute_error": {
        "p95": 0.03038243055343628,
        "p99": 0.06681984663009653,
        "maximum": 0.07748007774353027
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6918563842773438,
      "reference_fraction_of_uniform": 0.6468000411987305,
      "rms_normalized_to_uniform_percent": 0.10114682186125468
    },
    "horizon": {
      "bias_percent": 0.5915544531781042,
      "rms_normalized_error_percent": 1.8863700017926304,
      "absolute_error": {
        "p95": 0.042739872167140966,
        "p99": 0.07638627869331548,
        "maximum": 0.0866155721229811
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6118609881012154,
      "reference_fraction_of_uniform": 0.1071958557696871,
      "rms_normalized_to_uniform_percent": 0.12405550404677246
    },
    "north": {
      "bias_percent": -89.86938699687427,
      "rms_normalized_error_percent": 99.21855345471104,
      "absolute_error": {
        "p95": 3.65858602890512e-05,
        "p99": 9.593773983397114e-05,
        "maximum": 9.712169412523508e-05
      },
      "worst_index": [
        55
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 7.181068667705404e-06,
      "reference_fraction_of_uniform": 1.2580975408127415e-06,
      "rms_normalized_to_uniform_percent": 0.00013643582242504738
    },
    "east": {
      "bias_percent": 0.15445917981448504,
      "rms_normalized_error_percent": 0.1985769042398215,
      "absolute_error": {
        "p95": 0.015211331844329838,
        "p99": 0.023106219768524172,
        "maximum": 0.02348184585571289
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0870524644851685,
      "reference_fraction_of_uniform": 0.19044770300388336,
      "rms_normalized_to_uniform_percent": 0.04008678767957489
    },
    "south": {
      "bias_percent": -0.048761317144348115,
      "rms_normalized_error_percent": 0.28911468161696247,
      "absolute_error": {
        "p95": 0.07043406963348389,
        "p99": 0.11531505584716804,
        "maximum": 0.1240091323852539
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9264891147613525,
      "reference_fraction_of_uniform": 0.6879068613052368,
      "rms_normalized_to_uniform_percent": 0.1886809076906741
    },
    "west": {
      "bias_percent": 0.015953411273853826,
      "rms_normalized_error_percent": 0.1569259928168408,
      "absolute_error": {
        "p95": 0.011463655531406405,
        "p99": 0.015397794246673592,
        "maximum": 0.016279220581054688
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1000711917877197,
      "reference_fraction_of_uniform": 0.19272853434085846,
      "rms_normalized_to_uniform_percent": 0.03192576412819314
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
          "nmbe_percent": -0.027986252313013524,
          "cvrmse_percent": 1.6494404620852858,
          "absolute_error_percentiles_lux": {
            "p50": 2.46881103515625,
            "p90": 28.84755859375001,
            "p95": 46.070028686523386,
            "p99": 105.78751831054686
          },
          "maximum_absolute_error_lux": 620.44140625,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              3.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 10219.71875,
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
          "nmbe_percent": -0.5756690424976282,
          "cvrmse_percent": 10.220198618115361,
          "absolute_error_percentiles_lux": {
            "p50": 0.37710046768188477,
            "p90": 4.835005187988282,
            "p95": 7.402688598632803,
            "p99": 15.620696392059301
          },
          "maximum_absolute_error_lux": 113.94384765625,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 4916.88916015625,
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
          "nmbe_percent": 1.8246279031799404,
          "cvrmse_percent": 23.20874660794723,
          "absolute_error_percentiles_lux": {
            "p50": 0.07573509216308594,
            "p90": 0.7354948997497559,
            "p95": 1.2810009241104123,
            "p99": 2.947109642028808
          },
          "maximum_absolute_error_lux": 36.533203125,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              8.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 558.4498901367188,
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
      "study_preparation_seconds": 0.014486207976005971,
      "weather_seconds": 0.14062333293259144,
      "metric_reduction_seconds": 0.2636523339897394,
      "write_seconds": 0.05837966699618846,
      "total_seconds": 0.4629421670688316,
      "cold_end_to_end_seconds": 0.4774283750448376,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02424408309161663,
      "engine_upload_seconds": 0.000862416,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.20898541656788439,
      "engine_annual_reduction_seconds": 0.002999125048518181,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.20898541656788439
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.014486207976005971,
      "weather_seconds": 0.13230795797426254,
      "metric_reduction_seconds": 0.04847787495236844,
      "write_seconds": 0.05011583294253796,
      "total_seconds": 0.23115841706749052,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.23115841706749052,
      "raw_export_seconds": 0.020759165985509753,
      "engine_upload_seconds": 9.6625e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0030898749828338623,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02476562501396984,
      "full": 0.20051795803010464
    }
  },
  "elapsed_seconds": 149.77288012497593,
  "result_class": "unstable_reference"
}
```
