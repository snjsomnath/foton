# Foton report

Status: **passed**

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
  "status": "passed",
  "passed": true,
  "model_sha256": "3ab6d03092b0661839265c53d4ed693372a3a68d15b1cfa0d809271fbc63fd89",
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
      "scene_fingerprint": 13596737419153064380,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 13596737419153064380,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "0ee4ec218535d9daea609be93d51186ad56a0458d990e21beec48bbfc71d1a25",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "4fe51b0ab73403beef30ac883bb2a4f7b1dc04ecc6ea4eca5f02c3c580f30f24",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0,
        "identifier": "classroom_01",
        "passed": true,
        "rms_normalized_error_percent": 0.0,
        "worst_index": [
          0,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00013248156756162643,
          "p95": 0.0,
          "p99": 1.1541830463100086e-06
        },
        "bias_percent": -0.009125976527407225,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 0.8506212984587354,
        "worst_index": [
          796,
          333,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0001394996652379632,
          "p95": 2.1187588572502136e-07,
          "p99": 1.2885488104075193e-05
        },
        "bias_percent": 0.01562021644731381,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 0.8253725229947633,
        "worst_index": [
          3,
          466,
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
          "maximum": 2.7611649784375913e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0,
        "identifier": "classroom_01",
        "passed": true,
        "rms_normalized_error_percent": 0.0,
        "worst_index": [
          158,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0009296070784330368,
          "p95": 4.350267772679204e-06,
          "p99": 3.662390270619641e-05
        },
        "bias_percent": 0.08388380555966006,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 1.5524566767871126,
        "worst_index": [
          98,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0014346763491630554,
          "p95": 3.344088327139616e-05,
          "p99": 0.0001171774638351053
        },
        "bias_percent": 0.02557657238517396,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 1.04761872938768,
        "worst_index": [
          18,
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
          "maximum": 2.7611649784375913e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0,
        "identifier": "classroom_01",
        "passed": true,
        "rms_normalized_error_percent": 0.0,
        "worst_index": [
          158,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0007577612996101379,
          "p95": 3.7903264001215543e-06,
          "p99": 3.0558401776942866e-05
        },
        "bias_percent": -0.02704036605808135,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 1.2829253418207973,
        "worst_index": [
          3,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0014657005667686462,
          "p95": 2.7381509426049888e-05,
          "p99": 9.498139843344688e-05
        },
        "bias_percent": -0.003134946582257075,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 0.8680624795204157,
        "worst_index": [
          140,
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
            "identifier": "classroom_01",
            "sensor_count": 175,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 1.580198477313388e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0001836980709413183,
                "cvrmse_percent": 27680.52139869678,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 55.00000184178326,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.00011851488307002,
                "relative_energy_error_percent": 55.000001841783266,
                "rms_normalized_rmse_percent": 174.06895354821506,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 1.580198477313388e-05,
                  "global_sensor_index": 138,
                  "local_sensor_index": 138,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "office_02",
            "sensor_count": 960,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007961575174704194,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.1015826174984774e-05
                },
                "candidate_energy": 33.07500630832271,
                "cvrmse_percent": 101.46989841386969,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.013342998241853655,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.07942009476437,
                "relative_energy_error_percent": 0.013342998241853655,
                "rms_normalized_rmse_percent": 8.809913229808396,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0027371804462745786,
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "reference": 0.0019410229288041592,
                  "rgb_channel": 0,
                  "sky_patch_index": 224
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0021581798791885376,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010107453515956846
                },
                "candidate_energy": 19.551961592774333,
                "cvrmse_percent": 266.4888369782645,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.306787166944342,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.492162140766478,
                "relative_energy_error_percent": 0.306787166944342,
                "rms_normalized_rmse_percent": 5.340095502251467,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04797222092747688,
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "reference": 0.045814041048288345,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 175
          },
          {
            "identifier": "office_01",
            "sensor_count": 885,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000791262136772275,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.988993845880032e-05,
                  "p99": 0.00025241087132599205
                },
                "candidate_energy": 166.55454917107977,
                "cvrmse_percent": 44.354563194828344,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03686862869471303,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.49316542411748,
                "relative_energy_error_percent": 0.03686862869471303,
                "rms_normalized_rmse_percent": 9.014574528646436,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0028708080062642694,
                  "global_sensor_index": 1267,
                  "local_sensor_index": 132,
                  "reference": 0.0036620701430365443,
                  "rgb_channel": 0,
                  "sky_patch_index": 278
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.003430653363466263,
                  "p50": 0.0,
                  "p90": 3.277877112850601e-07,
                  "p95": 0.00010074861347675323,
                  "p99": 0.00038361697443178855
                },
                "candidate_energy": 105.23654975375567,
                "cvrmse_percent": 108.7816442300056,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04174649572080473,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 105.28050067346418,
                "relative_energy_error_percent": 0.041746495720821605,
                "rms_normalized_rmse_percent": 3.4584783698583186,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.11502294987440109,
                  "global_sensor_index": 1244,
                  "local_sensor_index": 109,
                  "reference": 0.11845360323786736,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 1135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1694.0517909824848,
            "full": 8425.823792000301
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1832.879832945764,
            "full": 8628.57670802623
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1728.0198329826817,
            "full": 8506.165291997604
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1720.9692919859663,
            "full": 8522.83162495587
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
            "identifier": "classroom_01",
            "sensor_count": 175,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 4.908738446829375e-06,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0003353781312398496,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.00017628783993117736,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 4.908738446829375e-06,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 56
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "office_02",
            "sensor_count": 960,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004722324665635824,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6340190747286354e-05
                },
                "candidate_energy": 33.102941710637424,
                "cvrmse_percent": 60.517341610512176,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.11518735882008227,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.06485517726105,
                "relative_energy_error_percent": 0.1151873588200823,
                "rms_normalized_rmse_percent": 5.260711611439065,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003701749024912715,
                  "global_sensor_index": 180,
                  "local_sensor_index": 5,
                  "reference": 0.004173981491476297,
                  "rgb_channel": 0,
                  "sky_patch_index": 378
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013467548415064812,
                  "p50": 0.0,
                  "p90": 2.6478091143644716e-06,
                  "p95": 6.196408537562069e-06,
                  "p99": 7.108543431968373e-05
                },
                "candidate_energy": 31.084760029442254,
                "cvrmse_percent": 107.2624558726018,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07492327176969389,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.108067211181186,
                "relative_energy_error_percent": 0.07492327176969389,
                "rms_normalized_rmse_percent": 2.8246503204170628,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028383119963109493,
                  "global_sensor_index": 283,
                  "local_sensor_index": 108,
                  "reference": 0.027036365121603012,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 175
          },
          {
            "identifier": "office_01",
            "sensor_count": 885,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004931429866701365,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.714046372100711e-05,
                  "p99": 0.0001500800426583737
                },
                "candidate_energy": 166.4995126008338,
                "cvrmse_percent": 26.137373578386104,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.036001762380708215,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.55947694794716,
                "relative_energy_error_percent": 0.036001762380708215,
                "rms_normalized_rmse_percent": 5.31903486928723,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003995030652731657,
                  "global_sensor_index": 1163,
                  "local_sensor_index": 28,
                  "reference": 0.0044881736394017935,
                  "rgb_channel": 0,
                  "sky_patch_index": 370
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.002762299031019211,
                  "p50": 7.105427357601002e-15,
                  "p90": 1.2419457925716471e-05,
                  "p95": 6.612209108425304e-05,
                  "p99": 0.000230793550144881
                },
                "candidate_energy": 155.71812872109612,
                "cvrmse_percent": 46.91170151077265,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08972946702600201,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.57852893627478,
                "relative_energy_error_percent": 0.08972946702595633,
                "rms_normalized_rmse_percent": 1.8977684261364969,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.10803179815411568,
                  "global_sensor_index": 1286,
                  "local_sensor_index": 151,
                  "reference": 0.10526949912309647,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 1135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3288.2069998886436,
            "full": 122359.1992079746
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3243.0434999987483,
            "full": 122055.13699993026
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3191.976208006963,
            "full": 121611.79599992465
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3155.8123340364546,
            "full": 123488.4387080092
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
            "identifier": "classroom_01",
            "sensor_count": 175,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 5.522329956875183e-06,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.00019485035307909016,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0002923012971081107,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 5.522329956875183e-06,
                  "global_sensor_index": 158,
                  "local_sensor_index": 158,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "office_02",
            "sensor_count": 960,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004273009253665805,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.731607186840815e-05
                },
                "candidate_energy": 33.070654735136486,
                "cvrmse_percent": 61.20214497249922,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02182308126152526,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.07787334631644,
                "relative_energy_error_percent": 0.021823081261525257,
                "rms_normalized_rmse_percent": 5.3232557062684895,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003608402912504971,
                  "global_sensor_index": 196,
                  "local_sensor_index": 21,
                  "reference": 0.0040357038378715515,
                  "rgb_channel": 0,
                  "sky_patch_index": 321
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001398574560880661,
                  "p50": 0.0,
                  "p90": 2.649215502970038e-06,
                  "p95": 6.200030497893727e-06,
                  "p99": 7.066341117024341e-05
                },
                "candidate_energy": 31.18625019734471,
                "cvrmse_percent": 107.50565618104373,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.16936942373005434,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.133519534721867,
                "relative_energy_error_percent": 0.16936942373005434,
                "rms_normalized_rmse_percent": 2.8286189516224085,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.054554110392928123,
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "reference": 0.05315553583204746,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 175
          },
          {
            "identifier": "office_01",
            "sensor_count": 885,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005010821332689375,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.759000148624182e-05,
                  "p99": 0.0001503780367784202
                },
                "candidate_energy": 166.5159410135691,
                "cvrmse_percent": 26.311708545634175,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03944889022012369,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.4502782260406,
                "relative_energy_error_percent": 0.03944889022012369,
                "rms_normalized_rmse_percent": 5.351577484342901,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008015918137971312,
                  "global_sensor_index": 1221,
                  "local_sensor_index": 86,
                  "reference": 0.0013026739470660686,
                  "rgb_channel": 0,
                  "sky_patch_index": 105
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0021592453122138977,
                  "p50": 0.0,
                  "p90": 1.2386198068270464e-05,
                  "p95": 6.661075894953683e-05,
                  "p99": 0.00022915046429261565
                },
                "candidate_energy": 155.7431191844967,
                "cvrmse_percent": 45.40342470661991,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04363856382983777,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.8111129164606,
                "relative_energy_error_percent": 0.04363856382975112,
                "rms_normalized_rmse_percent": 1.8395813831597139,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12885845452547073,
                  "global_sensor_index": 1247,
                  "local_sensor_index": 112,
                  "reference": 0.13101769983768463,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 1135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3194.0067500108853,
            "full": 125616.24554195441
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3208.2415419863537,
            "full": 127737.7405409934
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3170.4990830039605,
            "full": 128593.08616595808
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3198.5272080637515,
            "full": 127964.73295800388
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
            "identifier": "classroom_01",
            "sensor_count": 175,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 4.658120019485068e-06,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.00019048862504433828,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.00016530728408525874,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 2.451641876177746e-07,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 4.903284207102843e-06,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "office_02",
            "sensor_count": 960,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002579829888418317,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.4866007879609233e-05
                },
                "candidate_energy": 33.09886496310297,
                "cvrmse_percent": 34.1539773585334,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.08979350359615612,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.069170995855586,
                "relative_energy_error_percent": 0.08979350359615612,
                "rms_normalized_rmse_percent": 2.971606590248929,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019165659905411303,
                  "global_sensor_index": 191,
                  "local_sensor_index": 16,
                  "reference": 0.0016585830016992986,
                  "rgb_channel": 0,
                  "sky_patch_index": 170
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012556836009025574,
                  "p50": 0.0,
                  "p90": 1.8795001096805396e-06,
                  "p95": 4.391092852529246e-06,
                  "p99": 4.205189698950493e-05
                },
                "candidate_energy": 31.100404917932018,
                "cvrmse_percent": 65.27377232830293,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2076480379853335,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.16511867539728,
                "relative_energy_error_percent": 0.20764803798533346,
                "rms_normalized_rmse_percent": 1.718508055531025,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0498501043766737,
                  "global_sensor_index": 222,
                  "local_sensor_index": 47,
                  "reference": 0.04859442077577114,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 175
          },
          {
            "identifier": "office_01",
            "sensor_count": 885,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002703930949792266,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.4544642656110227e-05,
                  "p99": 8.58064740896225e-05
                },
                "candidate_energy": 166.49661945315177,
                "cvrmse_percent": 14.545350804423137,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.013852794154492433,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.47355821381075,
                "relative_energy_error_percent": 0.013852794154492434,
                "rms_normalized_rmse_percent": 2.9605550300665726,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017321859486401081,
                  "global_sensor_index": 1291,
                  "local_sensor_index": 156,
                  "reference": 0.0020025790436193347,
                  "rgb_channel": 0,
                  "sky_patch_index": 162
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016336999833583832,
                  "p50": 0.0,
                  "p90": 8.59817073433078e-06,
                  "p95": 3.728794399648905e-05,
                  "p99": 0.00012833265645895153
                },
                "candidate_energy": 155.74484613809759,
                "cvrmse_percent": 27.428714059811195,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.025917807754644064,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.78522225251115,
                "relative_energy_error_percent": 0.025917807754650905,
                "rms_normalized_rmse_percent": 1.1106573270636344,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12248075008392334,
                  "global_sensor_index": 1177,
                  "local_sensor_index": 42,
                  "reference": 0.12411445006728172,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 1135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 6323.655042098835,
            "full": 234082.2962920647
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 6203.988499939442,
            "full": 224509.9283750169
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 6258.554000058211,
            "full": 225616.91641702782
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 6184.597540996037,
            "full": 226793.5022499878
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
    "/content/suite-vulkan-0.3.2/acceptance/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 354868.97050007246,
      "invocation_count": 127,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1437409.3449590728,
      "invocation_count": 127,
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
            "reference_energy": 0.00017789795480993575,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 2.5742242542037275e-06
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 2.5742242542037275e-06,
              "candidate": 0.0,
              "position": [
                15.75,
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
            "reference_energy": 0.00017789795480993575,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 2.5742242542037275e-06
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 2.5742242542037275e-06,
              "candidate": 0.0,
              "position": [
                15.75,
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
            "nmbe_percent": -0.0961395696141168,
            "cvrmse_percent": 6.357097878801383,
            "rms_normalized_rmse_percent": 0.5533516437844669,
            "reference_energy": 33.079132000147794,
            "candidate_energy": 33.04732986501077,
            "relative_energy_error_percent": 0.09613956961411681,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.059440344572067e-07,
              "maximum": 8.676867582835257e-05
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 418,
              "rgb_channel": 0,
              "reference": 0.0005653905682265759,
              "candidate": 0.0004786218923982233,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9019594331926204,
            "cvrmse_percent": 90.88197912442328,
            "rms_normalized_rmse_percent": 2.391667096570236,
            "reference_energy": 31.137647720354312,
            "candidate_energy": 30.545422292262746,
            "relative_energy_error_percent": 1.9019594331926233,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.415013659629041e-06,
              "p95": 5.218910791882016e-06,
              "p99": 2.105215860865423e-05,
              "maximum": 0.0017675161361694336
            },
            "worst": {
              "global_sensor_index": 220,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05922563746571541,
              "candidate": 0.057458121329545975,
              "position": [
                2.0449999570846558,
                3.8060461282730103,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9717515670275261,
            "cvrmse_percent": 44.007903807924166,
            "rms_normalized_rmse_percent": 2.388451119353752,
            "reference_energy": 64.21677972050207,
            "candidate_energy": 63.59275215727355,
            "relative_energy_error_percent": 0.9717515670274167,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.413742140561236e-06,
              "p95": 5.214638713368907e-06,
              "p99": 2.0484020933508266e-05,
              "maximum": 0.0017675161361694336
            },
            "worst": {
              "global_sensor_index": 220,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05922563746571541,
              "candidate": 0.057458121329545975,
              "position": [
                2.0449999570846558,
                3.8060461282730103,
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
            "nmbe_percent": 0.006041383670687592,
            "cvrmse_percent": 2.428388024657092,
            "rms_normalized_rmse_percent": 0.49431992509816225,
            "reference_energy": 166.41409294187625,
            "candidate_energy": 166.42414665571303,
            "relative_energy_error_percent": 0.006041383670729222,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.0721927285194397e-07,
              "p99": 8.18941043689847e-06,
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
            "nmbe_percent": -1.6473717472210272,
            "cvrmse_percent": 59.818073628519755,
            "rms_normalized_rmse_percent": 2.4232445576138475,
            "reference_energy": 155.8360299726017,
            "candidate_energy": 153.26883124284205,
            "relative_energy_error_percent": 1.6473717472210956,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.442214675596923e-06,
              "p95": 1.783340485417284e-05,
              "p99": 5.363579839468002e-05,
              "maximum": 0.004110425710678101
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13036200404167175,
              "candidate": 0.12625157833099365,
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
            "nmbe_percent": -0.7935280187934827,
            "cvrmse_percent": 28.91742451536389,
            "rms_normalized_rmse_percent": 2.4224211497675743,
            "reference_energy": 322.2501229144779,
            "candidate_energy": 319.6929778985554,
            "relative_energy_error_percent": 0.7935280187933883,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.385531691601511e-06,
              "p95": 1.7566195310791954e-05,
              "p99": 5.288096144795418e-05,
              "maximum": 0.004110425710678101
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13036200404167175,
              "candidate": 0.12625157833099365,
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
            "reference_energy": 0.00015110647700566915,
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
              "global_sensor_index": 138,
              "local_sensor_index": 138,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                22.25,
                14.2006254196167,
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
            "reference_energy": 0.00015110647700566915,
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
              "global_sensor_index": 138,
              "local_sensor_index": 138,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                22.25,
                14.2006254196167,
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
            "nmbe_percent": -0.0961395696141168,
            "cvrmse_percent": 6.357097878801383,
            "rms_normalized_rmse_percent": 0.5533516437844669,
            "reference_energy": 33.079132000147794,
            "candidate_energy": 33.04732986501077,
            "relative_energy_error_percent": 0.09613956961411681,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.059440344572067e-07,
              "maximum": 8.676867582835257e-05
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 418,
              "rgb_channel": 0,
              "reference": 0.0005653905682265759,
              "candidate": 0.0004786218923982233,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 56.481549851241766,
            "cvrmse_percent": 1147.5332414673824,
            "rms_normalized_rmse_percent": 23.02674525903049,
            "reference_energy": 19.520142995324726,
            "candidate_energy": 30.545422292262746,
            "relative_energy_error_percent": 56.4815498512418,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.249999493476935e-06,
              "p95": 2.3529999452875927e-05,
              "p99": 6.560178415384002e-05,
              "maximum": 0.010601717978715897
            },
            "worst": {
              "global_sensor_index": 961,
              "local_sensor_index": 786,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018231261521577835,
              "candidate": 0.02883297950029373,
              "position": [
                1.137499988079071,
                0.2049015462398529,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.90043477357292,
            "cvrmse_percent": 425.838676037417,
            "rms_normalized_rmse_percent": 23.025504137986754,
            "reference_energy": 52.59927499547253,
            "candidate_energy": 63.59275215727355,
            "relative_energy_error_percent": 20.900434773572993,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.229999704984948e-06,
              "p95": 2.347999907215126e-05,
              "p99": 6.486613594461162e-05,
              "maximum": 0.010601717978715897
            },
            "worst": {
              "global_sensor_index": 961,
              "local_sensor_index": 786,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018231261521577835,
              "candidate": 0.02883297950029373,
              "position": [
                1.137499988079071,
                0.2049015462398529,
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
            "nmbe_percent": 0.006041383670687592,
            "cvrmse_percent": 2.428388024657092,
            "rms_normalized_rmse_percent": 0.49431992509816225,
            "reference_energy": 166.41409294187625,
            "candidate_energy": 166.42414665571303,
            "relative_energy_error_percent": 0.006041383670729222,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.0721927285194397e-07,
              "p99": 8.18941043689847e-06,
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
            "nmbe_percent": 45.46011135230062,
            "cvrmse_percent": 542.3472733880371,
            "rms_normalized_rmse_percent": 17.254501700646767,
            "reference_energy": 105.36828950421265,
            "candidate_energy": 153.26883124284205,
            "relative_energy_error_percent": 45.460111352300466,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.668999801855534e-05,
              "p95": 9.783889981918037e-05,
              "p99": 0.0002253290149383247,
              "maximum": 0.015125598758459091
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022692110389471054,
              "candidate": 0.037817709147930145,
              "position": [
                1.199999988079071,
                24.131555557250977,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.628293276871936,
            "cvrmse_percent": 210.26451245094225,
            "rms_normalized_rmse_percent": 17.254497359896153,
            "reference_energy": 271.782382446089,
            "candidate_energy": 319.6929778985554,
            "relative_energy_error_percent": 17.62829327687198,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.666984125127785e-05,
              "p95": 9.79097094386816e-05,
              "p99": 0.00022524711675941944,
              "maximum": 0.015125598758459091
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022692110389471054,
              "candidate": 0.037817709147930145,
              "position": [
                1.199999988079071,
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
      "bias_percent": 0.042343618189587096,
      "rms_normalized_error_percent": 0.17598284965144645,
      "absolute_error": {
        "p95": 0.06464252783272008,
        "p99": 0.12885043297073528,
        "maximum": 0.19149897902386437
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.978601379237025,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17598284965144645
    },
    "overcast": {
      "bias_percent": 0.041208910402750085,
      "rms_normalized_error_percent": 0.11635544500911331,
      "absolute_error": {
        "p95": 0.03257317543029785,
        "p99": 0.05396959781646725,
        "maximum": 0.0709686279296875
      },
      "worst_index": [
        1885
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.3862152099609375,
      "reference_fraction_of_uniform": 0.6285235285758972,
      "rms_normalized_to_uniform_percent": 0.08358264590155319
    },
    "horizon": {
      "bias_percent": 0.06865761895613465,
      "rms_normalized_error_percent": 1.8872658659413106,
      "absolute_error": {
        "p95": 0.0502576882960843,
        "p99": 0.12403380199066028,
        "maximum": 0.19929109527270983
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0325684137451048,
      "reference_fraction_of_uniform": 0.14796208547134357,
      "rms_normalized_to_uniform_percent": 0.150585009693436
    },
    "north": {
      "bias_percent": -0.05497363314764795,
      "rms_normalized_error_percent": 0.25149373416772347,
      "absolute_error": {
        "p95": 0.019881334900856015,
        "p99": 0.03315522849559782,
        "maximum": 0.06743359565734863
      },
      "worst_index": [
        1893
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3585901260375977,
      "reference_fraction_of_uniform": 0.19467942416667938,
      "rms_normalized_to_uniform_percent": 0.05075624401841974
    },
    "east": {
      "bias_percent": -58.51726182861965,
      "rms_normalized_error_percent": 78.7049084408143,
      "absolute_error": {
        "p95": 3.367138410794723e-05,
        "p99": 0.00019123001009575062,
        "maximum": 0.0005506478636334577
      },
      "worst_index": [
        1292
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2579372196341865e-05,
      "reference_fraction_of_uniform": 1.8025634744844865e-06,
      "rms_normalized_to_uniform_percent": 0.00021054230672294812
    },
    "south": {
      "bias_percent": 0.055149790252226674,
      "rms_normalized_error_percent": 0.25081685178976765,
      "absolute_error": {
        "p95": 0.01941182017326354,
        "p99": 0.03231917202472685,
        "maximum": 0.08196473121643066
      },
      "worst_index": [
        1917
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3783284425735474,
      "reference_fraction_of_uniform": 0.1975078284740448,
      "rms_normalized_to_uniform_percent": 0.051118759216092734
    },
    "west": {
      "bias_percent": 0.05385594145667391,
      "rms_normalized_error_percent": 0.2423137076955162,
      "absolute_error": {
        "p95": 0.04973129034042356,
        "p99": 0.12552599906921383,
        "maximum": 0.18739080429077148
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.8095550537109375,
      "reference_fraction_of_uniform": 0.6891860961914062,
      "rms_normalized_to_uniform_percent": 0.1510404905629847
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
        "identifier": "classroom_01",
        "sensor_count": 175,
        "illuminance": {
          "nmbe_percent": -100.0,
          "cvrmse_percent": 1571.9480429494574,
          "absolute_error_percentiles_lux": {
            "p50": 3.531531183398329e-05,
            "p90": 0.0027668495196849084,
            "p95": 0.006024749763309927,
            "p99": 0.02176821056753397
          },
          "maximum_absolute_error_lux": 3.6098620891571045,
          "worst": {
            "sensor_index": 125,
            "position": [
              21.25,
              14.73354196548462,
              0.800000011920929
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 1.1754943508222875e-38,
            "radiance_lux": 3.6098620891571045
          },
          "physically_dark": true,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0007569044014871638,
            "maximum_error_percentage_points": 0.028633494744708273,
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
          "nmbe_percent": -0.3092349724581916,
          "cvrmse_percent": 4.014226514669109,
          "absolute_error_percentiles_lux": {
            "p50": 0.33300304412841797,
            "p90": 3.259246826171875,
            "p95": 6.079010581970213,
            "p99": 19.98193420410155
          },
          "maximum_absolute_error_lux": 395.54296875,
          "worst": {
            "sensor_index": 47,
            "position": [
              2.0449999570846558,
              4.851044178009033,
              0.800000011920929
            ],
            "hour_of_year": 4456.5,
            "foton_lux": 18785.953125,
            "radiance_lux": 19181.49609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08322046232876708,
            "maximum_error_percentage_points": 1.7787671232876683,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1644099301213575,
            "maximum_error_percentage_points": 1.1876021445573492,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.16894420662100448,
            "maximum_error_percentage_points": 3.204520547945208,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16918921232876716,
            "maximum_error_percentage_points": 3.2045205479452044,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0024727454337899507,
            "maximum_error_percentage_points": 0.14178082191780828,
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
          "nmbe_percent": -0.14224496125141373,
          "cvrmse_percent": 1.7246004325503386,
          "absolute_error_percentiles_lux": {
            "p50": 1.820556640625,
            "p90": 12.2064208984375,
            "p95": 20.646240234375,
            "p99": 58.40015624999978
          },
          "maximum_absolute_error_lux": 540.587890625,
          "worst": {
            "sensor_index": 78,
            "position": [
              1.659999966621399,
              15.14379596710205,
              0.800000011920929
            ],
            "hour_of_year": 3831.5,
            "foton_lux": 23397.55859375,
            "radiance_lux": 23938.146484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.33856094729510117,
            "maximum_error_percentage_points": 1.6961643835616442,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.24797921598219466,
            "maximum_error_percentage_points": 1.4231543640404993,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1813675412119805,
            "maximum_error_percentage_points": 1.1523287671232865,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.18993328689729896,
            "maximum_error_percentage_points": 1.1523287671232865,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.014925315378066704,
            "maximum_error_percentage_points": 0.2724657534246564,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 39.90924740146641,
          "radiance_percent": 40.11244725165375,
          "difference_percentage_points": 0.20319985018733888,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 2,
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
      "maximum_error_percentage_points": 0.004997006769049683,
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
            "maximum_error_percentage_points": 0.004997006769049683,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.00497163955479607,
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
        "maximum_error_percentage_points": 0.004997006769049683,
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
              "maximum_error_percentage_points": 0.004997006769049683,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.00497163955479607,
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
            "nmbe_percent": 18.146441790313236,
            "cvrmse_percent": 140.09989745401734,
            "absolute_error_lux": {
              "p50": 5.321921706199646,
              "p90": 52.02914886474611,
              "p95": 95.0567637443542,
              "p99": 323.3762646484365,
              "maximum": 11746.9609375
            },
            "per_sensor_maximum_error_lux": {
              "p50": 143.53144768625498,
              "p90": 2312.283203125,
              "p95": 4454.209570312496,
              "p99": 8575.925590820298,
              "maximum": 11746.9609375
            },
            "worst": {
              "sensor_index": 796,
              "sun_up_hour_index": 2389,
              "hour_of_year": 4454.5,
              "foton_lux": 32092.697265625,
              "radiance_lux": 20345.736328125
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.8494166666666665,
              "maximum_error_percentage_points": 30.8,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.1822083333333335,
              "maximum_error_percentage_points": 23.630000000000003,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.3706875,
              "maximum_error_percentage_points": 42.85,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.37765625,
              "maximum_error_percentage_points": 42.85,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.07009375,
              "maximum_error_percentage_points": 2.870000000000001,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 6.132365888421612,
            "radiance_percent": 4.826362239923227,
            "difference_percentage_points": 1.3060036484983852,
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
            "nmbe_percent": 15.979606415155889,
            "cvrmse_percent": 51.536832839738096,
            "absolute_error_lux": {
              "p50": 59.127811431884766,
              "p90": 257.46509704589846,
              "p95": 439.68845825195285,
              "p99": 1575.2972656249967,
              "maximum": 11316.6142578125
            },
            "per_sensor_maximum_error_lux": {
              "p50": 1167.695556640625,
              "p90": 6017.40546875,
              "p95": 7213.658984374998,
              "p99": 8089.047578124999,
              "maximum": 11316.6142578125
            },
            "worst": {
              "sensor_index": 740,
              "sun_up_hour_index": 2012,
              "hour_of_year": 3951.5,
              "foton_lux": 26039.203125,
              "radiance_lux": 14722.5888671875
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.394994350282486,
              "maximum_error_percentage_points": 38.76,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.44929943502825,
              "maximum_error_percentage_points": 33.45,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 13.086858757062146,
              "maximum_error_percentage_points": 54.47,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 13.047615819209039,
              "maximum_error_percentage_points": 54.47,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.23950282485875704,
              "maximum_error_percentage_points": 2.69,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 39.90924740146641,
            "radiance_percent": 31.663353246083464,
            "difference_percentage_points": 8.245894155382945,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 53.19051289899994,
        "radiance_seconds": 72.50948634799988,
        "speedup": 1.3632033683465978,
        "passed": false
      },
      "versions": {
        "python": "3.13.16",
        "platform": "Linux-6.6.159+-x86_64-with-glibc2.39"
      },
      "folders": {
        "foton": "/content/suite-vulkan-0.3.2/acceptance/mf2/annual",
        "radiance": "/content/suite-vulkan-0.3.2/acceptance/mf2/stock/annual_daylight"
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
      "study_preparation_seconds": 0.3640286869999727,
      "weather_seconds": 0.265299161999792,
      "metric_reduction_seconds": 52.475860495000006,
      "write_seconds": 0.0848680090000471,
      "total_seconds": 52.82648421199997,
      "cold_end_to_end_seconds": 53.19051289899994,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.058990775999973266,
      "engine_upload_seconds": 0.053883158,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.68459066,
      "engine_annual_reduction_seconds": 1.086328549,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 1.68459066
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3640286869999727,
      "weather_seconds": 0.42955493800013755,
      "metric_reduction_seconds": 50.90851878900003,
      "write_seconds": 0.05627941100010503,
      "total_seconds": 51.394789661000004,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 51.394789661000004,
      "raw_export_seconds": 0.04076976999999715,
      "engine_upload_seconds": 0.071809511,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.9e-08,
      "engine_annual_reduction_seconds": 1.090613366,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.174177711999846,
      "full": 1.7191485169998941
    }
  },
  "elapsed_seconds": 241.35359110800005,
  "result_class": "passed"
}
```
