# Foton report

Status: **failed**

```json
{
  "scene": "acceptance",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "acceptance",
    "category": "integration",
    "question": "Does the classroom and two-office model retain its Honeybee results?",
    "interactions": [
      "real_hbjson",
      "grid_order",
      "sealed_zone",
      "stock_recipe"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 4,
    "shades": 0,
    "sensors": 2020,
    "floor_area": 491.2443866249562,
    "aperture_area": 28.27294252873692
  },
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "7689ddb81f691ab17fe82bc6c79843e71ceb0e3a6448741666e8d1a3ed70ccac",
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
      "scene_fingerprint": 13596737419153064380,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 13596737419153064380,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "classroom_01",
        "bias_percent": 0.0,
        "rms_normalized_error_percent": 0.0,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 0.0
        },
        "worst_index": [
          0,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.009125976527407225,
        "rms_normalized_error_percent": 0.8506212984587354,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.1541830463100086e-06,
          "maximum": 0.00013248156756162643
        },
        "worst_index": [
          796,
          333,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.01562021644731381,
        "rms_normalized_error_percent": 0.8253725229947633,
        "absolute_error": {
          "p95": 2.1187588572502136e-07,
          "p99": 1.2885488104075193e-05,
          "maximum": 0.0001394996652379632
        },
        "worst_index": [
          3,
          466,
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
        "identifier": "classroom_01",
        "bias_percent": 0.0,
        "rms_normalized_error_percent": 0.0,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 7.893252586654853e-06
        },
        "worst_index": [
          109,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.05808241743647826,
        "rms_normalized_error_percent": 1.564613293288685,
        "absolute_error": {
          "p95": 4.348657103037112e-06,
          "p99": 3.649293095804525e-05,
          "maximum": 0.0008590072393417358
        },
        "worst_index": [
          796,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.02028313109470662,
        "rms_normalized_error_percent": 1.0484152703741154,
        "absolute_error": {
          "p95": 3.368090256117284e-05,
          "p99": 0.00011681573232635856,
          "maximum": 0.0015867352485656738
        },
        "worst_index": [
          205,
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
        "identifier": "classroom_01",
        "bias_percent": 0.0,
        "rms_normalized_error_percent": 0.0,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 7.893252586654853e-06
        },
        "worst_index": [
          109,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.043184119551227314,
        "rms_normalized_error_percent": 1.2783692865733767,
        "absolute_error": {
          "p95": 3.759752598853064e-06,
          "p99": 3.041119005501627e-05,
          "maximum": 0.0010668039321899414
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.005390443921244588,
        "rms_normalized_error_percent": 0.8669346061171166,
        "absolute_error": {
          "p95": 2.75573693215847e-05,
          "p99": 9.427196346223354e-05,
          "maximum": 0.001573704183101654
        },
        "worst_index": [
          209,
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "classroom_01",
            "start_sensor_index": 0,
            "sensor_count": 175,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0,
                "candidate_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0
                },
                "worst": {
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 0.0
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -99.99999999999999,
                "cvrmse_percent": 15902.043893789249,
                "rms_normalized_rmse_percent": 100.0,
                "reference_energy": 0.00018962381727760658,
                "candidate_energy": 0.0,
                "relative_energy_error_percent": 100.0,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 1.580198477313388e-05
                },
                "worst": {
                  "global_sensor_index": 76,
                  "local_sensor_index": 76,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 1.580198477313388e-05,
                  "candidate": 0.0
                },
                "passed": true,
                "negligible_relative_to_direct": true,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_02",
            "start_sensor_index": 175,
            "sensor_count": 960,
            "stages": {
              "direct": {
                "nmbe_percent": -0.21434153449340027,
                "cvrmse_percent": 101.26437704506023,
                "rms_normalized_rmse_percent": 8.807735653663801,
                "reference_energy": 33.13121102381854,
                "candidate_energy": 33.06019707771384,
                "relative_energy_error_percent": 0.21434153449340027,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.392130580729812e-05,
                  "maximum": 0.0007007726235315204
                },
                "worst": {
                  "global_sensor_index": 219,
                  "local_sensor_index": 44,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 0.0008508718456141651,
                  "candidate": 0.0015516444691456854
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5449787065387718,
                "cvrmse_percent": 264.4410965578851,
                "rms_normalized_rmse_percent": 5.296118961968809,
                "reference_energy": 19.483747420910017,
                "candidate_energy": 19.589929695589774,
                "relative_energy_error_percent": 0.5449787065387718,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010353724417654619,
                  "maximum": 0.0013533998280763626
                },
                "worst": {
                  "global_sensor_index": 206,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05624241568148136,
                  "candidate": 0.054889015853405
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "office_01",
            "start_sensor_index": 1135,
            "sensor_count": 885,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04771660187221917,
                "cvrmse_percent": 43.64420001926296,
                "rms_normalized_rmse_percent": 8.869630320022091,
                "reference_energy": 166.50208683337098,
                "candidate_energy": 166.5815359712542,
                "relative_energy_error_percent": 0.04771660187221917,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.733495683874935e-05,
                  "p99": 0.000251209014095366,
                  "maximum": 0.0009225880494341254
                },
                "worst": {
                  "global_sensor_index": 1183,
                  "local_sensor_index": 48,
                  "sky_patch_index": 327,
                  "rgb_channel": 0,
                  "reference": 0.0043258219957351685,
                  "candidate": 0.003403233946301043
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1254387664092828,
                "cvrmse_percent": 106.71122816365182,
                "rms_normalized_rmse_percent": 3.395951266296126,
                "reference_energy": 105.25895884876087,
                "candidate_energy": 105.12692330924573,
                "relative_energy_error_percent": 0.12543876640928617,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.5792105589064957e-07,
                  "p95": 0.00010067399125546217,
                  "p99": 0.00038007067632861435,
                  "maximum": 0.004247650504112244
                },
                "worst": {
                  "global_sensor_index": 1214,
                  "local_sensor_index": 79,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.12048934772610664,
                  "candidate": 0.12473699823021889
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
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1759.2657910427079,
            "full": 8178.507416974753
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1720.7253329688683,
            "full": 8347.33495907858
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1717.6387920044363,
            "full": 8556.539583951235
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1728.0664169229567,
            "full": 8437.339124968275
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
            "identifier": "classroom_01",
            "start_sensor_index": 0,
            "sensor_count": 175,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0,
                "candidate_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0
                },
                "worst": {
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 0.0
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -37.395613811085525,
                "cvrmse_percent": 16049.36140127676,
                "rms_normalized_rmse_percent": 115.8704158973854,
                "reference_energy": 0.0001170240818915147,
                "candidate_energy": 7.326220816139539e-05,
                "relative_energy_error_percent": 37.395613811085525,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 1.5707964848843403e-05
                },
                "worst": {
                  "global_sensor_index": 88,
                  "local_sensor_index": 88,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 1.5707964848843403e-05,
                  "candidate": 0.0
                },
                "passed": true,
                "negligible_relative_to_direct": true,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_02",
            "start_sensor_index": 175,
            "sensor_count": 960,
            "stages": {
              "direct": {
                "nmbe_percent": -0.020142963200466373,
                "cvrmse_percent": 61.29378289941648,
                "rms_normalized_rmse_percent": 5.332065748064387,
                "reference_energy": 33.07464244798774,
                "candidate_energy": 33.06798023493076,
                "relative_energy_error_percent": 0.020142963200466373,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.763152064696969e-05,
                  "maximum": 0.0004010953416582197
                },
                "worst": {
                  "global_sensor_index": 389,
                  "local_sensor_index": 214,
                  "sky_patch_index": 105,
                  "rgb_channel": 0,
                  "reference": 0.0004010603588540107,
                  "candidate": 0.0008021557005122304
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.0227323943473468,
                "cvrmse_percent": 107.50551945680525,
                "rms_normalized_rmse_percent": 2.831605458589019,
                "reference_energy": 31.113921236909196,
                "candidate_energy": 31.1068482976367,
                "relative_energy_error_percent": 0.022732394347346797,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6570104594725322e-06,
                  "p95": 6.175147063913674e-06,
                  "p99": 7.035581802483515e-05,
                  "maximum": 0.0014586001634597778
                },
                "worst": {
                  "global_sensor_index": 180,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05584122985601425,
                  "candidate": 0.05729983001947403
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_01",
            "start_sensor_index": 1135,
            "sensor_count": 885,
            "stages": {
              "direct": {
                "nmbe_percent": -0.00025550806128529107,
                "cvrmse_percent": 26.690749029726963,
                "rms_normalized_rmse_percent": 5.429645672741218,
                "reference_energy": 166.54519721880854,
                "candidate_energy": 166.54477168240396,
                "relative_energy_error_percent": 0.0002555080612852911,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.768150392919779e-05,
                  "p99": 0.00015374342910945415,
                  "maximum": 0.0005255044670775533
                },
                "worst": {
                  "global_sensor_index": 1216,
                  "local_sensor_index": 81,
                  "sky_patch_index": 374,
                  "rgb_channel": 0,
                  "reference": 0.0037277304800227284,
                  "candidate": 0.004253234947100282
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.044707898755458365,
                "cvrmse_percent": 45.70334202153151,
                "rms_normalized_rmse_percent": 1.849405461479837,
                "reference_energy": 155.67612722239076,
                "candidate_energy": 155.60652769704572,
                "relative_energy_error_percent": 0.04470789875548119,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2378998053463895e-05,
                  "p95": 6.64551043882966e-05,
                  "p99": 0.00023060903185978532,
                  "maximum": 0.001762043684720993
                },
                "worst": {
                  "global_sensor_index": 1142,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.09902308881282806,
                  "candidate": 0.09726104512810707
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
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3260.4730828898028,
            "full": 121766.88312506303
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3191.1729999119416,
            "full": 120221.80108400062
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3158.3669160027057,
            "full": 121611.05787497945
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3200.605040998198,
            "full": 121784.67416705098
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
            "identifier": "classroom_01",
            "start_sensor_index": 0,
            "sensor_count": 175,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0,
                "candidate_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0
                },
                "worst": {
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 0.0
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -21.831244737947348,
                "cvrmse_percent": 17211.88521506987,
                "rms_normalized_rmse_percent": 136.92142483200664,
                "reference_energy": 0.00016548978311448082,
                "candidate_energy": 0.00012936130354646025,
                "relative_energy_error_percent": 21.831244737947344,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 1.578650464750808e-05
                },
                "worst": {
                  "global_sensor_index": 109,
                  "local_sensor_index": 109,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 1.578650464750808e-05
                },
                "passed": true,
                "negligible_relative_to_direct": true,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_02",
            "start_sensor_index": 175,
            "sensor_count": 960,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05976570030682431,
                "cvrmse_percent": 60.548620498729505,
                "rms_normalized_rmse_percent": 5.268182870521527,
                "reference_energy": 33.098505257704744,
                "candidate_energy": 33.1182868111631,
                "relative_energy_error_percent": 0.05976570030682431,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7084719117261844e-05,
                  "maximum": 0.0004768751095980406
                },
                "worst": {
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "sky_patch_index": 328,
                  "rgb_channel": 0,
                  "reference": 0.004164179554209113,
                  "candidate": 0.0036873044446110725
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.11500733668147321,
                "cvrmse_percent": 107.93791736838111,
                "rms_normalized_rmse_percent": 2.8388830515680508,
                "reference_energy": 31.128478423125546,
                "candidate_energy": 31.092678389141643,
                "relative_energy_error_percent": 0.11500733668147323,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6435556378601216e-06,
                  "p95": 6.211837274250257e-06,
                  "p99": 6.989532981605953e-05,
                  "maximum": 0.0015060622245073318
                },
                "worst": {
                  "global_sensor_index": 209,
                  "local_sensor_index": 34,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04965517111122608,
                  "candidate": 0.051161233335733414
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_01",
            "start_sensor_index": 1135,
            "sensor_count": 885,
            "stages": {
              "direct": {
                "nmbe_percent": -0.055787539007428874,
                "cvrmse_percent": 26.460291990355085,
                "rms_normalized_rmse_percent": 5.3848609971118355,
                "reference_energy": 166.56401253912497,
                "candidate_energy": 166.47109057565737,
                "relative_energy_error_percent": 0.055787539007428874,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.763187462231144e-05,
                  "p99": 0.00015056446136441082,
                  "maximum": 0.0004915883764624596
                },
                "worst": {
                  "global_sensor_index": 1154,
                  "local_sensor_index": 19,
                  "sky_patch_index": 278,
                  "rgb_channel": 0,
                  "reference": 0.003391500562429428,
                  "candidate": 0.0038830889388918877
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.08293665238344194,
                "cvrmse_percent": 45.94336467875122,
                "rms_normalized_rmse_percent": 1.8595551318400485,
                "reference_energy": 155.66955652554148,
                "candidate_energy": 155.79866364450396,
                "relative_energy_error_percent": 0.0829366523834716,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2452617011149469e-05,
                  "p95": 6.729114102199674e-05,
                  "p99": 0.00023100711405277252,
                  "maximum": 0.0021671243011951447
                },
                "worst": {
                  "global_sensor_index": 1334,
                  "local_sensor_index": 199,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0752766989171505,
                  "candidate": 0.07310957461595535
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
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3129.6120838960633,
            "full": 126826.56983297784
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3253.1937499297783,
            "full": 125569.1030829912
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3170.555458054878,
            "full": 125239.58745796699
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3131.8827079376206,
            "full": 126662.60679101106
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
            "identifier": "classroom_01",
            "start_sensor_index": 0,
            "sensor_count": 175,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0,
                "candidate_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0
                },
                "worst": {
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 0.0
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.00012994353012274473,
                "candidate_energy": 9.833907318324009e-05,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 7.845254913263489e-06
                },
                "worst": {
                  "global_sensor_index": 172,
                  "local_sensor_index": 172,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 7.845254913263489e-06,
                  "candidate": 0.0
                },
                "passed": true,
                "negligible_relative_to_direct": true,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_02",
            "start_sensor_index": 175,
            "sensor_count": 960,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11032906468891936,
                "cvrmse_percent": 34.35032008887812,
                "rms_normalized_rmse_percent": 2.9898635744367783,
                "reference_energy": 33.096395168879624,
                "candidate_energy": 33.05988022564405,
                "relative_energy_error_percent": 0.11032906468891936,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.488699516106859e-05,
                  "maximum": 0.0002333569573238492
                },
                "worst": {
                  "global_sensor_index": 268,
                  "local_sensor_index": 93,
                  "sky_patch_index": 170,
                  "rgb_channel": 0,
                  "reference": 0.0019164769910275936,
                  "candidate": 0.0016831200337037444
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.17834516560415883,
                "cvrmse_percent": 63.78260126879495,
                "rms_normalized_rmse_percent": 1.677186282305718,
                "reference_energy": 31.085384732948032,
                "candidate_energy": 31.1408240138287,
                "relative_energy_error_percent": 0.17834516560415883,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8806034240981277e-06,
                  "p95": 4.425720209155702e-06,
                  "p99": 4.163396923104267e-05,
                  "maximum": 0.0009149052202701569
                },
                "worst": {
                  "global_sensor_index": 206,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06314049661159515,
                  "candidate": 0.06405540183186531
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "office_01",
            "start_sensor_index": 1135,
            "sensor_count": 885,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03291094940590472,
                "cvrmse_percent": 14.683193190386827,
                "rms_normalized_rmse_percent": 2.9886929583176016,
                "reference_energy": 166.53082620557467,
                "candidate_energy": 166.47601932961692,
                "relative_energy_error_percent": 0.03291094940590472,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.4543958716094494e-05,
                  "p99": 8.627149509266019e-05,
                  "maximum": 0.0002630624803714454
                },
                "worst": {
                  "global_sensor_index": 1154,
                  "local_sensor_index": 19,
                  "sky_patch_index": 160,
                  "rgb_channel": 0,
                  "reference": 0.001956177467945963,
                  "candidate": 0.0016931149875745177
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0032261055565847765,
                "cvrmse_percent": 27.343782519842314,
                "rms_normalized_rmse_percent": 1.1070747029034933,
                "reference_energy": 155.7630970808044,
                "candidate_energy": 155.76812216273453,
                "relative_energy_error_percent": 0.0032261055566372362,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.578075812692998e-06,
                  "p95": 3.793393261730671e-05,
                  "p99": 0.0001305196201428771,
                  "maximum": 0.0015881545841693878
                },
                "worst": {
                  "global_sensor_index": 1381,
                  "local_sensor_index": 246,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07583898305892944,
                  "candidate": 0.07425082847476006
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
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6194.183750078082,
            "full": 226466.48787509184
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6202.83762505278,
            "full": 233529.59204104263
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6402.563208015636,
            "full": 235627.56129098125
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "2020",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6221.302082994953,
            "full": 230088.2942500757
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 369755.21212490276,
      "worker_pool_size": 12,
      "invocation_count": 127
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1496503.6181670148,
      "worker_pool_size": 12,
      "invocation_count": 127
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      2020,
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
        "identifier": "classroom_01",
        "full_identifier": "classroom_01",
        "start_sensor_index": 0,
        "sensor_count": 175,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 0.0,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 0.0
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0,
              "candidate": 0.0,
              "position": [
                12.75,
                11.536043643951416,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 0.00011414130167963776,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 3.922627456631744e-06
            },
            "worst": {
              "global_sensor_index": 172,
              "local_sensor_index": 172,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                24.75,
                13.66770887374878,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 0.00011414130167963776,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 3.922627456631744e-06
            },
            "worst": {
              "global_sensor_index": 172,
              "local_sensor_index": 172,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                24.75,
                13.66770887374878,
                0.800000011920929
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "office_02",
        "full_identifier": "office_02",
        "start_sensor_index": 175,
        "sensor_count": 960,
        "stages": {
          "direct": {
            "nmbe_percent": -0.09584474234381887,
            "cvrmse_percent": 6.360732271957698,
            "rms_normalized_rmse_percent": 0.553667998427033,
            "reference_energy": 33.079132000147794,
            "candidate_energy": 33.04742739131268,
            "relative_energy_error_percent": 0.09584474234381887,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.083468466993504e-07,
              "maximum": 8.67685885168612e-05
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 418,
              "rgb_channel": 0,
              "reference": 0.0005653905682265759,
              "candidate": 0.00047862197970971465,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.8138488418876526,
            "cvrmse_percent": 152.87751633580717,
            "rms_normalized_rmse_percent": 4.023146530117601,
            "reference_energy": 31.112110050715096,
            "candidate_energy": 30.54778340287339,
            "relative_energy_error_percent": 1.8138488418876497,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.580914461868825e-06,
              "p95": 1.7965332813218877e-05,
              "p99": 5.229101948316361e-05,
              "maximum": 0.004235006868839264
            },
            "worst": {
              "global_sensor_index": 234,
              "local_sensor_index": 59,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04993804544210434,
              "candidate": 0.045703038573265076,
              "position": [
                2.5549999475479126,
                4.328545093536377,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9285242622421092,
            "cvrmse_percent": 74.06544651868887,
            "rms_normalized_rmse_percent": 4.021464045872626,
            "reference_energy": 64.19124205086288,
            "candidate_energy": 63.59521079418604,
            "relative_energy_error_percent": 0.9285242622421465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.580822875752355e-06,
              "p95": 1.792757036582768e-05,
              "p99": 5.2076281936024285e-05,
              "maximum": 0.004235006868839264
            },
            "worst": {
              "global_sensor_index": 234,
              "local_sensor_index": 59,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04993804544210434,
              "candidate": 0.045703038573265076,
              "position": [
                2.5549999475479126,
                4.328545093536377,
                0.800000011920929
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "office_01",
        "full_identifier": "office_01",
        "start_sensor_index": 1135,
        "sensor_count": 885,
        "stages": {
          "direct": {
            "nmbe_percent": 0.006047452205449321,
            "cvrmse_percent": 2.4283891341434436,
            "rms_normalized_rmse_percent": 0.49432015094395165,
            "reference_energy": 166.41409294187625,
            "candidate_energy": 166.4241567546101,
            "relative_energy_error_percent": 0.006047452205482411,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.069864422082901e-07,
              "p99": 8.189352229237556e-06,
              "maximum": 0.00011912835179828107
            },
            "worst": {
              "global_sensor_index": 1615,
              "local_sensor_index": 480,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.00037786501343362033,
              "candidate": 0.00025873666163533926,
              "position": [
                8.289999961853027,
                8.087984085083008,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.6305190178632702,
            "cvrmse_percent": 75.83802987292077,
            "rms_normalized_rmse_percent": 3.0728644856446183,
            "reference_energy": 155.85493953714925,
            "candidate_energy": 153.31369510771674,
            "relative_energy_error_percent": 1.630519017863264,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 2.7125095948577014e-05,
              "p95": 4.518919377005659e-05,
              "p99": 0.00010224990546703339,
              "maximum": 0.0058776140213012695
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12992705404758453,
              "candidate": 0.12404944002628326,
              "position": [
                2.1699999570846558,
                17.15974235534668,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7854247109093447,
            "cvrmse_percent": 36.66858953144459,
            "rms_normalized_rmse_percent": 3.0721935643154876,
            "reference_energy": 322.26903247902544,
            "candidate_energy": 319.73785186232675,
            "relative_energy_error_percent": 0.7854247109093334,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 2.7038189500672164e-05,
              "p95": 4.5062508434057236e-05,
              "p99": 0.00010158086661249399,
              "maximum": 0.0058776140213012695
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12992705404758453,
              "candidate": 0.12404944002628326,
              "position": [
                2.1699999570846558,
                17.15974235534668,
                0.800000011920929
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
      2020,
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
        "identifier": "classroom_01",
        "full_identifier": "classroom_01",
        "start_sensor_index": 0,
        "sensor_count": 175,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 0.0,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 0.0
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0,
              "candidate": 0.0,
              "position": [
                12.75,
                11.536043643951416,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 9.481190863880329e-05,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 7.90099238656694e-06
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 76,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                17.75,
                14.73354196548462,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "rms_normalized_rmse_percent": 0.0,
            "reference_energy": 9.481190863880329e-05,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 7.90099238656694e-06
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 76,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                17.75,
                14.73354196548462,
                0.800000011920929
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "office_02",
        "full_identifier": "office_02",
        "start_sensor_index": 175,
        "sensor_count": 960,
        "stages": {
          "direct": {
            "nmbe_percent": -0.09584474234381887,
            "cvrmse_percent": 6.360732271957698,
            "rms_normalized_rmse_percent": 0.553667998427033,
            "reference_energy": 33.079132000147794,
            "candidate_energy": 33.04742739131268,
            "relative_energy_error_percent": 0.09584474234381887,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.083468466993504e-07,
              "maximum": 8.67685885168612e-05
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 418,
              "rgb_channel": 0,
              "reference": 0.0005653905682265759,
              "candidate": 0.00047862197970971465,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 56.22739173330783,
            "cvrmse_percent": 1155.6834178305348,
            "rms_normalized_rmse_percent": 23.22993587657648,
            "reference_energy": 19.55341061765968,
            "candidate_energy": 30.54778340287339,
            "relative_energy_error_percent": 56.227391733307805,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.0811431719922275e-06,
              "p95": 2.488999962224625e-05,
              "p99": 8.951306444941954e-05,
              "maximum": 0.010743524879217148
            },
            "worst": {
              "global_sensor_index": 188,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02510734647512436,
              "candidate": 0.03585087135434151,
              "position": [
                1.024999976158142,
                0.6710525751113892,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.828688167288995,
            "cvrmse_percent": 429.3239814907895,
            "rms_normalized_rmse_percent": 23.228764323441684,
            "reference_energy": 52.632542617807474,
            "candidate_energy": 63.59521079418604,
            "relative_energy_error_percent": 20.82868816728892,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.079999937152024e-06,
              "p95": 2.4850000045262277e-05,
              "p99": 8.917107297747701e-05,
              "maximum": 0.010743524879217148
            },
            "worst": {
              "global_sensor_index": 188,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02510734647512436,
              "candidate": 0.03585087135434151,
              "position": [
                1.024999976158142,
                0.6710525751113892,
                0.800000011920929
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "office_01",
        "full_identifier": "office_01",
        "start_sensor_index": 1135,
        "sensor_count": 885,
        "stages": {
          "direct": {
            "nmbe_percent": 0.006047452205449321,
            "cvrmse_percent": 2.4283891341434436,
            "rms_normalized_rmse_percent": 0.49432015094395165,
            "reference_energy": 166.41409294187625,
            "candidate_energy": 166.4241567546101,
            "relative_energy_error_percent": 0.006047452205482411,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.069864422082901e-07,
              "p99": 8.189352229237556e-06,
              "maximum": 0.00011912835179828107
            },
            "worst": {
              "global_sensor_index": 1615,
              "local_sensor_index": 480,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.00037786501343362033,
              "candidate": 0.00025873666163533926,
              "position": [
                8.289999961853027,
                8.087984085083008,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 45.56849117659491,
            "cvrmse_percent": 550.7038292947611,
            "rms_normalized_rmse_percent": 17.526788585934487,
            "reference_energy": 105.32065962113037,
            "candidate_energy": 153.31369510771674,
            "relative_energy_error_percent": 45.568491176594925,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.0918289455003106e-05,
              "p95": 0.00010651197590050288,
              "p99": 0.00023895356571301818,
              "maximum": 0.01654154621064663
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02443944476544857,
              "candidate": 0.0409809909760952,
              "position": [
                2.7149999737739563,
                24.131555557250977,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.665425142185192,
            "cvrmse_percent": 213.4453232533781,
            "rms_normalized_rmse_percent": 17.526795095806484,
            "reference_energy": 271.73475256300674,
            "candidate_energy": 319.73785186232675,
            "relative_energy_error_percent": 17.665425142185153,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.086999928811565e-05,
              "p95": 0.0001064786920323968,
              "p99": 0.00023899524239823222,
              "maximum": 0.01654154621064663
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02443944476544857,
              "candidate": 0.0409809909760952,
              "position": [
                2.7149999737739563,
                24.131555557250977,
                0.800000011920929
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
      "bias_percent": 0.018067829246053303,
      "rms_normalized_error_percent": 0.358449007088882,
      "absolute_error": {
        "p95": 0.13224671508350178,
        "p99": 0.20118555539939736,
        "maximum": 0.26938724542730785
      },
      "worst_index": [
        250
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.978559216681206,
      "rms_normalized_to_uniform_percent": 0.358449007088882
    },
    "overcast": {
      "bias_percent": 0.029663832613894867,
      "rms_normalized_error_percent": 0.25406595257435904,
      "absolute_error": {
        "p95": 0.06877282857894895,
        "p99": 0.10814346313476544,
        "maximum": 0.143035888671875
      },
      "worst_index": [
        1901
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.386198997497559,
      "rms_normalized_to_uniform_percent": 0.1825078266904634
    },
    "horizon": {
      "bias_percent": -0.06300889494233074,
      "rms_normalized_error_percent": 3.3583338001570406,
      "absolute_error": {
        "p95": 0.09796698497989546,
        "p99": 0.15019297313242447,
        "maximum": 0.22648229320863145
      },
      "worst_index": [
        1967
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.0322769734929005,
      "rms_normalized_to_uniform_percent": 0.26787774970593925
    },
    "north": {
      "bias_percent": -0.12759550704175196,
      "rms_normalized_error_percent": 0.6671758757652959,
      "absolute_error": {
        "p95": 0.0535542994737625,
        "p99": 0.08053123712539673,
        "maximum": 0.17006802558898926
      },
      "worst_index": [
        962
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.3586773872375488,
      "rms_normalized_to_uniform_percent": 0.13464837096480797
    },
    "east": {
      "bias_percent": -39.03436368736058,
      "rms_normalized_error_percent": 73.30010708842048,
      "absolute_error": {
        "p95": 1.761016992531946e-05,
        "p99": 0.0001235675001225899,
        "maximum": 0.0005982063012197614
      },
      "worst_index": [
        964
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 8.188531865016557e-06,
      "rms_normalized_to_uniform_percent": 0.0001439709928355269
    },
    "south": {
      "bias_percent": 0.06826127016931748,
      "rms_normalized_error_percent": 0.6643570401095737,
      "absolute_error": {
        "p95": 0.05283746123313903,
        "p99": 0.08229122161865232,
        "maximum": 0.1461479663848877
      },
      "worst_index": [
        1917
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.3782528638839722,
      "rms_normalized_to_uniform_percent": 0.13539652592775098
    },
    "west": {
      "bias_percent": 0.022749720479958144,
      "rms_normalized_error_percent": 0.45409094594391464,
      "absolute_error": {
        "p95": 0.10434308052062986,
        "p99": 0.16229673862457247,
        "maximum": 0.24157357215881348
      },
      "worst_index": [
        1967
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.809545040130615,
      "rms_normalized_to_uniform_percent": 0.28304585469392696
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
        "identifier": "classroom_01",
        "sensor_count": 175,
        "illuminance": {
          "nmbe_percent": -100.0,
          "cvrmse_percent": 1770.14215676491,
          "absolute_error_percentiles_lux": {
            "p50": 1.1754943508222875e-38,
            "p90": 0.0012476275442168114,
            "p95": 0.0029021588619798392,
            "p99": 0.010758179482072592
          },
          "maximum_absolute_error_lux": 1.8407880067825317,
          "worst": {
            "sensor_index": 52,
            "position": [
              16.25,
              13.134792804718018,
              0.800000011920929
            ],
            "hour_of_year": 5247.5,
            "foton_lux": 1.1754943508222875e-38,
            "radiance_lux": 1.8407880067825317
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.00029193454947104103,
            "maximum_error_percentage_points": 0.0061589808917938485,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
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
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "office_02",
        "sensor_count": 960,
        "illuminance": {
          "nmbe_percent": -0.32579614007371466,
          "cvrmse_percent": 9.123930980453979,
          "absolute_error_percentiles_lux": {
            "p50": 0.7671146392822266,
            "p90": 8.85554656982422,
            "p95": 19.556908416748016,
            "p99": 60.01923278808579
          },
          "maximum_absolute_error_lux": 693.369140625,
          "worst": {
            "sensor_index": 831,
            "position": [
              1.608846127986908,
              7.351144790649414,
              0.800000011920929
            ],
            "hour_of_year": 6829.5,
            "foton_lux": 7970.61474609375,
            "radiance_lux": 7277.24560546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2060540810502284,
            "maximum_error_percentage_points": 4.545479452054796,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.42244219866919946,
            "maximum_error_percentage_points": 2.8773970441214516,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.43377925228310493,
            "maximum_error_percentage_points": 7.474794520547945,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4346545376712328,
            "maximum_error_percentage_points": 7.474794520547945,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004408818493150693,
            "maximum_error_percentage_points": 0.21589041095890416,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 6.132365888421612,
          "radiance_percent": 6.132365888421612,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "office_01",
        "sensor_count": 885,
        "illuminance": {
          "nmbe_percent": -0.14745611129800862,
          "cvrmse_percent": 3.6718415515263514,
          "absolute_error_percentiles_lux": {
            "p50": 2.984619140625,
            "p90": 33.188330078125006,
            "p95": 58.01092071533203,
            "p99": 127.07626220703094
          },
          "maximum_absolute_error_lux": 761.14599609375,
          "worst": {
            "sensor_index": 782,
            "position": [
              0.6949999928474426,
              24.131555557250977,
              0.800000011920929
            ],
            "hour_of_year": 1357.5,
            "foton_lux": 7161.44677734375,
            "radiance_lux": 6400.30078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6592265304542994,
            "maximum_error_percentage_points": 3.7215068493150696,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.45153024182612267,
            "maximum_error_percentage_points": 2.5998727476323964,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3721359027939015,
            "maximum_error_percentage_points": 3.694383561643839,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.39286138843742746,
            "maximum_error_percentage_points": 3.694383561643839,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03239965946908132,
            "maximum_error_percentage_points": 0.8252054794520554,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 39.990047350974734,
          "radiance_percent": 40.234847322636284,
          "difference_percentage_points": 0.24479997166154988,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 4,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "failed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049975920376681415,
      "metrics": {
        "da": [
          {
            "identifier": "classroom_01",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "classroom_01",
            "maximum_error_percentage_points": 3.545802942514029e-39,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.004996797744541981,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.0049975920376681415,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "classroom_01",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "classroom_01",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "classroom_01",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ]
      }
    },
    "stock": {
      "schema_version": 1,
      "oracle": "stock",
      "passed": false,
      "structural": {
        "grid_ids_match": true,
        "grid_counts_match": true,
        "sun_up_hours_match": true,
        "model_grid_ids_match": true,
        "model_grid_counts_match": true
      },
      "official_loader": {
        "passed": true,
        "tolerance_percentage_points": 0.05,
        "maximum_error_percentage_points": 0.0049975920376681415,
        "metrics": {
          "da": [
            {
              "identifier": "classroom_01",
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            }
          ],
          "cda": [
            {
              "identifier": "classroom_01",
              "maximum_error_percentage_points": 3.545802942514029e-39,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.004996797744541981,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.0049975920376681415,
              "passed": true
            }
          ],
          "udi": [
            {
              "identifier": "classroom_01",
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            }
          ],
          "udi_lower": [
            {
              "identifier": "classroom_01",
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            }
          ],
          "udi_upper": [
            {
              "identifier": "classroom_01",
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.004931506849317202,
              "passed": true
            }
          ]
        }
      },
      "grids": [
        {
          "identifier": "classroom_01",
          "sensor_count": 175,
          "raw_shape": [
            175,
            4405
          ],
          "illuminance": {
            "nmbe_percent": 0.0,
            "cvrmse_percent": 0.0,
            "absolute_error_lux": {
              "p50": 1.1754943508222875e-38,
              "p90": 1.1754943508222875e-38,
              "p95": 1.1754943508222875e-38,
              "p99": 1.1754943508222875e-38,
              "maximum": 1.1754943508222875e-38
            },
            "per_sensor_maximum_error_lux": {
              "p50": 1.1754943508222875e-38,
              "p90": 1.1754943508222875e-38,
              "p95": 1.1754943508222875e-38,
              "p99": 1.1754943508222875e-38,
              "maximum": 1.1754943508222875e-38
            },
            "worst": {
              "sensor_index": 0,
              "sun_up_hour_index": 0,
              "hour_of_year": 9.5,
              "foton_lux": 1.1754943508222875e-38,
              "radiance_lux": 0.0
            },
            "compatibility_passed": true,
            "strict_passed": true,
            "passed": true
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 0.0,
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 0.0,
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 0.0,
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            "udi": {
              "mean_absolute_error_percentage_points": 0.0,
              "maximum_error_percentage_points": 0.0,
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
            "passed": true
          }
        },
        {
          "identifier": "office_02",
          "sensor_count": 960,
          "raw_shape": [
            960,
            4405
          ],
          "illuminance": {
            "nmbe_percent": 17.278375039879393,
            "cvrmse_percent": 139.84355987236023,
            "absolute_error_lux": {
              "p50": 4.959971845149994,
              "p90": 50.93337745666506,
              "p95": 93.6982452392578,
              "p99": 342.2839947509739,
              "maximum": 11155.80078125
            },
            "per_sensor_maximum_error_lux": {
              "p50": 145.65616607666016,
              "p90": 2366.681542968751,
              "p95": 4220.71373291015,
              "p99": 8951.012910156249,
              "maximum": 11155.80078125
            },
            "worst": {
              "sensor_index": 796,
              "sun_up_hour_index": 2389,
              "hour_of_year": 4454.5,
              "foton_lux": 32131.529296875,
              "radiance_lux": 20975.728515625
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.8101354166666668,
              "maximum_error_percentage_points": 31.53,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.058614583333334,
              "maximum_error_percentage_points": 22.270000000000003,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.302229166666666,
              "maximum_error_percentage_points": 42.910000000000004,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.317114583333334,
              "maximum_error_percentage_points": 42.91,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.072375,
              "maximum_error_percentage_points": 3.09,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 6.132365888421612,
            "radiance_percent": 4.939939392290558,
            "difference_percentage_points": 1.1924264961310538,
            "passed": true
          }
        },
        {
          "identifier": "office_01",
          "sensor_count": 885,
          "raw_shape": [
            885,
            4405
          ],
          "illuminance": {
            "nmbe_percent": 15.944184574942746,
            "cvrmse_percent": 51.84412904264682,
            "absolute_error_lux": {
              "p50": 58.1055908203125,
              "p90": 257.4815795898439,
              "p95": 444.2336669921872,
              "p99": 1575.6474511718657,
              "maximum": 11463.88671875
            },
            "per_sensor_maximum_error_lux": {
              "p50": 1131.4453125,
              "p90": 5970.888671875,
              "p95": 7316.062109375,
              "p99": 8309.848984374994,
              "maximum": 11463.88671875
            },
            "worst": {
              "sensor_index": 740,
              "sun_up_hour_index": 2012,
              "hour_of_year": 3951.5,
              "foton_lux": 25943.8671875,
              "radiance_lux": 14479.98046875
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.312033898305085,
              "maximum_error_percentage_points": 39.18,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.302621468926553,
              "maximum_error_percentage_points": 30.71,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 12.866248587570622,
              "maximum_error_percentage_points": 52.160000000000004,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 12.822158192090397,
              "maximum_error_percentage_points": 52.160000000000004,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.2481694915254237,
              "maximum_error_percentage_points": 2.8199999999999994,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 39.990047350974734,
            "radiance_percent": 31.540953515707987,
            "difference_percentage_points": 8.449093835266748,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 1.090385999996215,
        "radiance_seconds": 23.158748875022866,
        "speedup": 21.23903725387455,
        "passed": true
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf2/stock/annual_daylight"
      },
      "reference_sky_density": 1,
      "candidate_sky_density": 2
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
      "study_preparation_seconds": 0.08972745796199888,
      "weather_seconds": 0.14943200000561774,
      "metric_reduction_seconds": 0.7053078340832144,
      "write_seconds": 0.14480587502475828,
      "total_seconds": 1.0006585420342162,
      "cold_end_to_end_seconds": 1.090385999996215,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.09784670802764595,
      "engine_upload_seconds": 0.001642583,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.42412591667380184,
      "engine_annual_reduction_seconds": 0.06973141664639115,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.42412591667380184
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.08972745796199888,
      "weather_seconds": 0.09509137494023889,
      "metric_reduction_seconds": 0.24590787501074374,
      "write_seconds": 0.09927545790560544,
      "total_seconds": 0.44051570806186646,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.44051570806186646,
      "raw_export_seconds": 0.08052204200066626,
      "engine_upload_seconds": 0.000972792,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0699317081598565,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.1558691250393167,
      "full": 0.440555915934965
    }
  },
  "elapsed_seconds": 3929.01825199998,
  "result_class": "accuracy_failure"
}
```
