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
  "model_sha256": "0ee4ec218535d9daea609be93d51186ad56a0458d990e21beec48bbfc71d1a25",
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
      "solver_version": "0.3.0",
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
    "maximum_samples": 262144,
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
          "maximum": 2.7611649784375913e-06
        },
        "worst_index": [
          158,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.08388380555966006,
        "rms_normalized_error_percent": 1.5524566767871126,
        "absolute_error": {
          "p95": 4.350267772679204e-06,
          "p99": 3.662390270619641e-05,
          "maximum": 0.0009296070784330368
        },
        "worst_index": [
          98,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.02557657238517396,
        "rms_normalized_error_percent": 1.04761872938768,
        "absolute_error": {
          "p95": 3.344088327139616e-05,
          "p99": 0.0001171774638351053,
          "maximum": 0.0014346763491630554
        },
        "worst_index": [
          18,
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
          "maximum": 2.7611649784375913e-06
        },
        "worst_index": [
          158,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.02704036605808135,
        "rms_normalized_error_percent": 1.2829253418207973,
        "absolute_error": {
          "p95": 3.7903264001215543e-06,
          "p99": 3.0558401776942866e-05,
          "maximum": 0.0007577612996101379
        },
        "worst_index": [
          3,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.003134946582257075,
        "rms_normalized_error_percent": 0.8680624795204157,
        "absolute_error": {
          "p95": 2.7381509426049888e-05,
          "p99": 9.498139843344688e-05,
          "maximum": 0.0014657005667686462
        },
        "worst_index": [
          140,
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
                "nmbe_percent": 55.00000184178326,
                "cvrmse_percent": 27680.52139869678,
                "rms_normalized_rmse_percent": 174.06895354821506,
                "reference_energy": 0.00011851488307002,
                "candidate_energy": 0.0001836980709413183,
                "relative_energy_error_percent": 55.000001841783266,
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
                  "global_sensor_index": 138,
                  "local_sensor_index": 138,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 1.580198477313388e-05
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
                "nmbe_percent": -0.013342998241853655,
                "cvrmse_percent": 101.46989841386969,
                "rms_normalized_rmse_percent": 8.809913229808396,
                "reference_energy": 33.07942009476437,
                "candidate_energy": 33.07500630832271,
                "relative_energy_error_percent": 0.013342998241853655,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.1015826174984774e-05,
                  "maximum": 0.0007961575174704194
                },
                "worst": {
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "sky_patch_index": 224,
                  "rgb_channel": 0,
                  "reference": 0.0019410229288041592,
                  "candidate": 0.0027371804462745786
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.306787166944342,
                "cvrmse_percent": 266.4888369782645,
                "rms_normalized_rmse_percent": 5.340095502251467,
                "reference_energy": 19.492162140766478,
                "candidate_energy": 19.551961592774333,
                "relative_energy_error_percent": 0.306787166944342,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010107453515956846,
                  "maximum": 0.0021581798791885376
                },
                "worst": {
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.045814041048288345,
                  "candidate": 0.04797222092747688
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
                "nmbe_percent": 0.03686862869471303,
                "cvrmse_percent": 44.354563194828344,
                "rms_normalized_rmse_percent": 9.014574528646436,
                "reference_energy": 166.49316542411748,
                "candidate_energy": 166.55454917107977,
                "relative_energy_error_percent": 0.03686862869471303,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.988993845880032e-05,
                  "p99": 0.00025241087132599205,
                  "maximum": 0.000791262136772275
                },
                "worst": {
                  "global_sensor_index": 1267,
                  "local_sensor_index": 132,
                  "sky_patch_index": 278,
                  "rgb_channel": 0,
                  "reference": 0.0036620701430365443,
                  "candidate": 0.0028708080062642694
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.04174649572080473,
                "cvrmse_percent": 108.7816442300056,
                "rms_normalized_rmse_percent": 3.4584783698583186,
                "reference_energy": 105.28050067346418,
                "candidate_energy": 105.23654975375567,
                "relative_energy_error_percent": 0.041746495720821605,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.277877112850601e-07,
                  "p95": 0.00010074861347675323,
                  "p99": 0.00038361697443178855,
                  "maximum": 0.003430653363466263
                },
                "worst": {
                  "global_sensor_index": 1244,
                  "local_sensor_index": 109,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11845360323786736,
                  "candidate": 0.11502294987440109
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1694.0517909824848,
            "full": 8425.823792000301
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1832.879832945764,
            "full": 8628.57670802623
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1728.0198329826817,
            "full": 8506.165291997604
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1720.9692919859663,
            "full": 8522.83162495587
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.00017628783993117736,
                "candidate_energy": 0.0003353781312398496,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.908738446829375e-06
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 56,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 4.908738446829375e-06
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
                "nmbe_percent": 0.11518735882008227,
                "cvrmse_percent": 60.517341610512176,
                "rms_normalized_rmse_percent": 5.260711611439065,
                "reference_energy": 33.06485517726105,
                "candidate_energy": 33.102941710637424,
                "relative_energy_error_percent": 0.1151873588200823,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6340190747286354e-05,
                  "maximum": 0.0004722324665635824
                },
                "worst": {
                  "global_sensor_index": 180,
                  "local_sensor_index": 5,
                  "sky_patch_index": 378,
                  "rgb_channel": 0,
                  "reference": 0.004173981491476297,
                  "candidate": 0.003701749024912715
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.07492327176969389,
                "cvrmse_percent": 107.2624558726018,
                "rms_normalized_rmse_percent": 2.8246503204170628,
                "reference_energy": 31.108067211181186,
                "candidate_energy": 31.084760029442254,
                "relative_energy_error_percent": 0.07492327176969389,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6478091143644716e-06,
                  "p95": 6.196408537562069e-06,
                  "p99": 7.108543431968373e-05,
                  "maximum": 0.0013467548415064812
                },
                "worst": {
                  "global_sensor_index": 283,
                  "local_sensor_index": 108,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.027036365121603012,
                  "candidate": 0.028383119963109493
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
                "nmbe_percent": -0.036001762380708215,
                "cvrmse_percent": 26.137373578386104,
                "rms_normalized_rmse_percent": 5.31903486928723,
                "reference_energy": 166.55947694794716,
                "candidate_energy": 166.4995126008338,
                "relative_energy_error_percent": 0.036001762380708215,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.714046372100711e-05,
                  "p99": 0.0001500800426583737,
                  "maximum": 0.0004931429866701365
                },
                "worst": {
                  "global_sensor_index": 1163,
                  "local_sensor_index": 28,
                  "sky_patch_index": 370,
                  "rgb_channel": 0,
                  "reference": 0.0044881736394017935,
                  "candidate": 0.003995030652731657
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.08972946702600201,
                "cvrmse_percent": 46.91170151077265,
                "rms_normalized_rmse_percent": 1.8977684261364969,
                "reference_energy": 155.57852893627478,
                "candidate_energy": 155.71812872109612,
                "relative_energy_error_percent": 0.08972946702595633,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.105427357601002e-15,
                  "p90": 1.2419457925716471e-05,
                  "p95": 6.612209108425304e-05,
                  "p99": 0.000230793550144881,
                  "maximum": 0.002762299031019211
                },
                "worst": {
                  "global_sensor_index": 1286,
                  "local_sensor_index": 151,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.10526949912309647,
                  "candidate": 0.10803179815411568
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3288.2069998886436,
            "full": 122359.1992079746
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3243.0434999987483,
            "full": 122055.13699993026
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3191.976208006963,
            "full": 121611.79599992465
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3155.8123340364546,
            "full": 123488.4387080092
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0002923012971081107,
                "candidate_energy": 0.00019485035307909016,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.522329956875183e-06
                },
                "worst": {
                  "global_sensor_index": 158,
                  "local_sensor_index": 158,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 5.522329956875183e-06
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
                "nmbe_percent": -0.02182308126152526,
                "cvrmse_percent": 61.20214497249922,
                "rms_normalized_rmse_percent": 5.3232557062684895,
                "reference_energy": 33.07787334631644,
                "candidate_energy": 33.070654735136486,
                "relative_energy_error_percent": 0.021823081261525257,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.731607186840815e-05,
                  "maximum": 0.0004273009253665805
                },
                "worst": {
                  "global_sensor_index": 196,
                  "local_sensor_index": 21,
                  "sky_patch_index": 321,
                  "rgb_channel": 0,
                  "reference": 0.0040357038378715515,
                  "candidate": 0.003608402912504971
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.16936942373005434,
                "cvrmse_percent": 107.50565618104373,
                "rms_normalized_rmse_percent": 2.8286189516224085,
                "reference_energy": 31.133519534721867,
                "candidate_energy": 31.18625019734471,
                "relative_energy_error_percent": 0.16936942373005434,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.649215502970038e-06,
                  "p95": 6.200030497893727e-06,
                  "p99": 7.066341117024341e-05,
                  "maximum": 0.001398574560880661
                },
                "worst": {
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05315553583204746,
                  "candidate": 0.054554110392928123
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
                "nmbe_percent": 0.03944889022012369,
                "cvrmse_percent": 26.311708545634175,
                "rms_normalized_rmse_percent": 5.351577484342901,
                "reference_energy": 166.4502782260406,
                "candidate_energy": 166.5159410135691,
                "relative_energy_error_percent": 0.03944889022012369,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.759000148624182e-05,
                  "p99": 0.0001503780367784202,
                  "maximum": 0.0005010821332689375
                },
                "worst": {
                  "global_sensor_index": 1221,
                  "local_sensor_index": 86,
                  "sky_patch_index": 105,
                  "rgb_channel": 0,
                  "reference": 0.0013026739470660686,
                  "candidate": 0.0008015918137971312
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.04363856382983777,
                "cvrmse_percent": 45.40342470661991,
                "rms_normalized_rmse_percent": 1.8395813831597139,
                "reference_energy": 155.8111129164606,
                "candidate_energy": 155.7431191844967,
                "relative_energy_error_percent": 0.04363856382975112,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2386198068270464e-05,
                  "p95": 6.661075894953683e-05,
                  "p99": 0.00022915046429261565,
                  "maximum": 0.0021592453122138977
                },
                "worst": {
                  "global_sensor_index": 1247,
                  "local_sensor_index": 112,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.13101769983768463,
                  "candidate": 0.12885845452547073
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3194.0067500108853,
            "full": 125616.24554195441
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3208.2415419863537,
            "full": 127737.7405409934
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3170.4990830039605,
            "full": 128593.08616595808
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3198.5272080637515,
            "full": 127964.73295800388
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
                "reference_energy": 0.00016530728408525874,
                "candidate_energy": 0.00019048862504433828,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.658120019485068e-06
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 4.903284207102843e-06,
                  "candidate": 2.451641876177746e-07
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
                "nmbe_percent": 0.08979350359615612,
                "cvrmse_percent": 34.1539773585334,
                "rms_normalized_rmse_percent": 2.971606590248929,
                "reference_energy": 33.069170995855586,
                "candidate_energy": 33.09886496310297,
                "relative_energy_error_percent": 0.08979350359615612,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.4866007879609233e-05,
                  "maximum": 0.0002579829888418317
                },
                "worst": {
                  "global_sensor_index": 191,
                  "local_sensor_index": 16,
                  "sky_patch_index": 170,
                  "rgb_channel": 0,
                  "reference": 0.0016585830016992986,
                  "candidate": 0.0019165659905411303
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.2076480379853335,
                "cvrmse_percent": 65.27377232830293,
                "rms_normalized_rmse_percent": 1.718508055531025,
                "reference_energy": 31.16511867539728,
                "candidate_energy": 31.100404917932018,
                "relative_energy_error_percent": 0.20764803798533346,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8795001096805396e-06,
                  "p95": 4.391092852529246e-06,
                  "p99": 4.205189698950493e-05,
                  "maximum": 0.0012556836009025574
                },
                "worst": {
                  "global_sensor_index": 222,
                  "local_sensor_index": 47,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04859442077577114,
                  "candidate": 0.0498501043766737
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
                "nmbe_percent": 0.013852794154492433,
                "cvrmse_percent": 14.545350804423137,
                "rms_normalized_rmse_percent": 2.9605550300665726,
                "reference_energy": 166.47355821381075,
                "candidate_energy": 166.49661945315177,
                "relative_energy_error_percent": 0.013852794154492434,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.4544642656110227e-05,
                  "p99": 8.58064740896225e-05,
                  "maximum": 0.0002703930949792266
                },
                "worst": {
                  "global_sensor_index": 1291,
                  "local_sensor_index": 156,
                  "sky_patch_index": 162,
                  "rgb_channel": 0,
                  "reference": 0.0020025790436193347,
                  "candidate": 0.0017321859486401081
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.025917807754644064,
                "cvrmse_percent": 27.428714059811195,
                "rms_normalized_rmse_percent": 1.1106573270636344,
                "reference_energy": 155.78522225251115,
                "candidate_energy": 155.74484613809759,
                "relative_energy_error_percent": 0.025917807754650905,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.59817073433078e-06,
                  "p95": 3.728794399648905e-05,
                  "p99": 0.00012833265645895153,
                  "maximum": 0.0016336999833583832
                },
                "worst": {
                  "global_sensor_index": 1177,
                  "local_sensor_index": 42,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.12411445006728172,
                  "candidate": 0.12248075008392334
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6323.655042098835,
            "full": 234082.2962920647
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6203.988499939442,
            "full": 224509.9283750169
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6258.554000058211,
            "full": 225616.91641702782
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6184.597540996037,
            "full": 226793.5022499878
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/oracle/scene.rad"
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 354868.97050007246,
      "worker_pool_size": 12,
      "invocation_count": 127
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1437409.3449590728,
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
            "reference_energy": 0.00017789795480993575,
            "candidate_energy": 6.360000043947878e-06,
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
            "candidate_energy": 6.360000043947878e-06,
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
            "nmbe_percent": -1.9017604595252393,
            "cvrmse_percent": 90.87481236458774,
            "rms_normalized_rmse_percent": 2.3914784947830294,
            "reference_energy": 31.137647720354312,
            "candidate_energy": 30.545484247982362,
            "relative_energy_error_percent": 1.901760459525208,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.414995117305807e-06,
              "p95": 5.21882948305573e-06,
              "p99": 2.105215789924836e-05,
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
            "nmbe_percent": -0.9715032175739818,
            "cvrmse_percent": 44.004570848381675,
            "rms_normalized_rmse_percent": 2.3882702288713338,
            "reference_energy": 64.21677972050207,
            "candidate_energy": 63.592911639295025,
            "relative_energy_error_percent": 0.9715032175739443,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.4137127638823603e-06,
              "p95": 5.214638713368907e-06,
              "p99": 2.0490316528593167e-05,
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
            "nmbe_percent": -1.647314657387457,
            "cvrmse_percent": 59.817449137262,
            "rms_normalized_rmse_percent": 2.4232192593227153,
            "reference_energy": 155.8360299726017,
            "candidate_energy": 153.26892020937225,
            "relative_energy_error_percent": 1.647314657387496,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.442214675596923e-06,
              "p95": 1.783340485417284e-05,
              "p99": 5.363579839468002e-05,
              "maximum": 0.004110410809516907
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13036200404167175,
              "candidate": 0.12625159323215485,
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
            "nmbe_percent": -0.7934972770124288,
            "cvrmse_percent": 28.917122492709765,
            "rms_normalized_rmse_percent": 2.4223958492410813,
            "reference_energy": 322.2501229144779,
            "candidate_energy": 319.6930769639826,
            "relative_energy_error_percent": 0.7934972770123422,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.385531691601511e-06,
              "p95": 1.7565980670042336e-05,
              "p99": 5.288110696710646e-05,
              "maximum": 0.004110410809516907
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13036200404167175,
              "candidate": 0.12625159323215485,
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
            "candidate_energy": 6.360000043947878e-06,
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
            "candidate_energy": 6.360000043947878e-06,
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
            "nmbe_percent": 56.48186724502119,
            "cvrmse_percent": 1147.546479690993,
            "rms_normalized_rmse_percent": 23.02701090118512,
            "reference_energy": 19.520142995324726,
            "candidate_energy": 30.545484247982362,
            "relative_energy_error_percent": 56.4818672450213,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.249999493476935e-06,
              "p95": 2.3529999452875927e-05,
              "p99": 6.560178193467295e-05,
              "maximum": 0.01060170866549015
            },
            "worst": {
              "global_sensor_index": 961,
              "local_sensor_index": 786,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018231261521577835,
              "candidate": 0.028832970187067986,
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
            "nmbe_percent": 20.900737975511596,
            "cvrmse_percent": 425.84361299183587,
            "rms_normalized_rmse_percent": 23.02577108382986,
            "reference_energy": 52.59927499547253,
            "candidate_energy": 63.592911639295025,
            "relative_energy_error_percent": 20.900737975511586,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.229999704984948e-06,
              "p95": 2.347999907215126e-05,
              "p99": 6.486613594461162e-05,
              "maximum": 0.01060170866549015
            },
            "worst": {
              "global_sensor_index": 961,
              "local_sensor_index": 786,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018231261521577835,
              "candidate": 0.028832970187067986,
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
            "nmbe_percent": 45.460195786175916,
            "cvrmse_percent": 542.3478737394285,
            "rms_normalized_rmse_percent": 17.254520800519874,
            "reference_energy": 105.36828950421265,
            "candidate_energy": 153.26892020937225,
            "relative_energy_error_percent": 45.4601957861758,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.668999801855534e-05,
              "p95": 9.783889981918037e-05,
              "p99": 0.0002253290149383247,
              "maximum": 0.015125621110200882
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022692110389471054,
              "candidate": 0.037817731499671936,
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
            "nmbe_percent": 17.628329727147463,
            "cvrmse_percent": 210.2647461023206,
            "rms_normalized_rmse_percent": 17.254516533541025,
            "reference_energy": 271.782382446089,
            "candidate_energy": 319.6930769639826,
            "relative_energy_error_percent": 17.628329727147495,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.666688248311433e-05,
              "p95": 9.79097094386816e-05,
              "p99": 0.00022524711675941944,
              "maximum": 0.015125621110200882
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022692110389471054,
              "candidate": 0.037817731499671936,
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
      "bias_percent": 0.04240596076484783,
      "rms_normalized_error_percent": 0.17598916017225083,
      "absolute_error": {
        "p95": 0.06464551506204262,
        "p99": 0.12884794514244197,
        "maximum": 0.19149725106940485
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.978601379237025,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17598916017225083
    },
    "overcast": {
      "bias_percent": 0.04129802413292736,
      "rms_normalized_error_percent": 0.11636576037573307,
      "absolute_error": {
        "p95": 0.032574129104614255,
        "p99": 0.05396959781646725,
        "maximum": 0.07097625732421875
      },
      "worst_index": [
        1885
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.3862152099609375,
      "reference_fraction_of_uniform": 0.6285235285758972,
      "rms_normalized_to_uniform_percent": 0.08359005319105263
    },
    "horizon": {
      "bias_percent": 0.06863058616483328,
      "rms_normalized_error_percent": 1.8872740000942967,
      "absolute_error": {
        "p95": 0.05025773742898949,
        "p99": 0.12403387021018511,
        "maximum": 0.19929293425646444
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0325684137451048,
      "reference_fraction_of_uniform": 0.14796208547134357,
      "rms_normalized_to_uniform_percent": 0.15058565871778828
    },
    "north": {
      "bias_percent": -0.054866181842162506,
      "rms_normalized_error_percent": 0.2514940292217616,
      "absolute_error": {
        "p95": 0.019881111383438108,
        "p99": 0.03315522849559782,
        "maximum": 0.0674123764038086
      },
      "worst_index": [
        1893
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3585901260375977,
      "reference_fraction_of_uniform": 0.19467942416667938,
      "rms_normalized_to_uniform_percent": 0.050756302595115994
    },
    "east": {
      "bias_percent": -57.60043249398055,
      "rms_normalized_error_percent": 79.02740782118543,
      "absolute_error": {
        "p95": 3.3911873597958195e-05,
        "p99": 0.00019123001009575062,
        "maximum": 0.0005506478637471446
      },
      "worst_index": [
        1292
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2579372196341865e-05,
      "reference_fraction_of_uniform": 1.8025634744844865e-06,
      "rms_normalized_to_uniform_percent": 0.0002114050233069573
    },
    "south": {
      "bias_percent": 0.05518004638037411,
      "rms_normalized_error_percent": 0.25082702277638885,
      "absolute_error": {
        "p95": 0.01941182017326354,
        "p99": 0.03231926858425139,
        "maximum": 0.08196640014648438
      },
      "worst_index": [
        1917
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3783284425735474,
      "reference_fraction_of_uniform": 0.1975078284740448,
      "rms_normalized_to_uniform_percent": 0.051120830701078555
    },
    "west": {
      "bias_percent": 0.05386877271139749,
      "rms_normalized_error_percent": 0.24231606862934452,
      "absolute_error": {
        "p95": 0.04973100423812864,
        "p99": 0.12552599906921383,
        "maximum": 0.18738961219787598
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.8095550537109375,
      "reference_fraction_of_uniform": 0.6891860961914062,
      "rms_normalized_to_uniform_percent": 0.15104196030554537
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
          "nmbe_percent": -98.78801808768277,
          "cvrmse_percent": 1572.0918375012463,
          "absolute_error_percentiles_lux": {
            "p50": 5.086182864033617e-05,
            "p90": 0.0028332870453596057,
            "p95": 0.006059433612972492,
            "p99": 0.02184732832014561
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
            "foton_lux": 0.0,
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
          "nmbe_percent": -0.30917007020728227,
          "cvrmse_percent": 4.014198876511134,
          "absolute_error_percentiles_lux": {
            "p50": 0.33289849758148193,
            "p90": 3.25921630859375,
            "p95": 6.07911472320556,
            "p99": 19.981812744140598
          },
          "maximum_absolute_error_lux": 395.5390625,
          "worst": {
            "sensor_index": 47,
            "position": [
              2.0449999570846558,
              4.851044178009033,
              0.800000011920929
            ],
            "hour_of_year": 4456.5,
            "foton_lux": 18785.95703125,
            "radiance_lux": 19181.49609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08325171232876707,
            "maximum_error_percentage_points": 1.7787671232876683,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1643786801213575,
            "maximum_error_percentage_points": 1.1876021445573492,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.16886087328767113,
            "maximum_error_percentage_points": 3.204520547945208,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16910587899543383,
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
          "nmbe_percent": -0.14222142738682345,
          "cvrmse_percent": 1.7245887185384978,
          "absolute_error_percentiles_lux": {
            "p50": 1.820404052734375,
            "p90": 12.206439208984378,
            "p95": 20.646093749999977,
            "p99": 58.398901367187364
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
            "mean_absolute_error_percentage_points": 0.3384931506849317,
            "maximum_error_percentage_points": 1.6961643835616442,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.24795661711213815,
            "maximum_error_percentage_points": 1.4231543640404993,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.18133364290689574,
            "maximum_error_percentage_points": 1.1523287671232865,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.18989938859221422,
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
      "maximum_error_percentage_points": 0.0049965887200347225,
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
            "maximum_error_percentage_points": 0.0008108252021547867,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.0049965887200347225,
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
        "maximum_error_percentage_points": 0.0049965887200347225,
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
              "maximum_error_percentage_points": 0.0008108252021547867,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.0049965887200347225,
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
            "nmbe_percent": -98.80236404808838,
            "cvrmse_percent": 1754.7220156853564,
            "absolute_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0017763505619950621,
              "maximum": 1.4226373434066772
            },
            "per_sensor_maximum_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.037299388628452106,
              "maximum": 1.4226373434066772
            },
            "worst": {
              "sensor_index": 142,
              "sun_up_hour_index": 2387,
              "hour_of_year": 4452.5,
              "foton_lux": 0.0,
              "radiance_lux": 1.4226373434066772
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 0.0,
              "maximum_error_percentage_points": 0.0,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 0.0008,
              "maximum_error_percentage_points": 0.14,
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
            "nmbe_percent": 17.102231057237216,
            "cvrmse_percent": 138.97728393814182,
            "absolute_error_lux": {
              "p50": 5.068878099322319,
              "p90": 51.04652252197268,
              "p95": 93.97269897460933,
              "p99": 319.55932922362865,
              "maximum": 12386.0546875
            },
            "per_sensor_maximum_error_lux": {
              "p50": 144.97586059570312,
              "p90": 2405.5761962890633,
              "p95": 4338.0157470703125,
              "p99": 8845.883476562498,
              "maximum": 12386.0546875
            },
            "worst": {
              "sensor_index": 796,
              "sun_up_hour_index": 2389,
              "hour_of_year": 4454.5,
              "foton_lux": 32092.69921875,
              "radiance_lux": 19706.64453125
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.8111249999999999,
              "maximum_error_percentage_points": 32.17,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.05003125,
              "maximum_error_percentage_points": 22.149999999999995,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.326145833333333,
              "maximum_error_percentage_points": 41.73,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.336354166666666,
              "maximum_error_percentage_points": 41.730000000000004,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.06822916666666666,
              "maximum_error_percentage_points": 3.0700000000000003,
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
            "nmbe_percent": 16.132301555065432,
            "cvrmse_percent": 51.72282234663072,
            "absolute_error_lux": {
              "p50": 59.785675048828125,
              "p90": 258.1198028564454,
              "p95": 440.1990234374998,
              "p99": 1563.0882812499967,
              "maximum": 11863.7763671875
            },
            "per_sensor_maximum_error_lux": {
              "p50": 1165.2353515625,
              "p90": 6101.496679687501,
              "p95": 7335.35078125,
              "p99": 8388.990781249999,
              "maximum": 11863.7763671875
            },
            "worst": {
              "sensor_index": 740,
              "sun_up_hour_index": 2012,
              "hour_of_year": 3951.5,
              "foton_lux": 26039.201171875,
              "radiance_lux": 14175.4248046875
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.417593220338983,
              "maximum_error_percentage_points": 37.89,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.577661016949152,
              "maximum_error_percentage_points": 32.71,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 13.44024858757062,
              "maximum_error_percentage_points": 53.48,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 13.396960451977401,
              "maximum_error_percentage_points": 53.48,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.2326553672316384,
              "maximum_error_percentage_points": 2.6300000000000003,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 39.90924740146641,
            "radiance_percent": 31.540953515707987,
            "difference_percentage_points": 8.368293885758423,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 5.4637835409957916,
        "radiance_seconds": 22.5589078750927,
        "speedup": 4.128807026455018,
        "passed": false
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf2/stock/annual_daylight"
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
      "study_preparation_seconds": 0.08798062498681247,
      "weather_seconds": 0.15074712503701448,
      "metric_reduction_seconds": 5.069080541958101,
      "write_seconds": 0.15527929097879678,
      "total_seconds": 5.375802916008979,
      "cold_end_to_end_seconds": 5.4637835409957916,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.11625504191033542,
      "engine_upload_seconds": 0.001967958,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.777550541330129,
      "engine_annual_reduction_seconds": 0.06996708328370005,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 4.777550541330129
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.08798062498681247,
      "weather_seconds": 0.1128854580456391,
      "metric_reduction_seconds": 0.246164417010732,
      "write_seconds": 0.12640029191970825,
      "total_seconds": 0.48573637497611344,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.48573637497611344,
      "raw_export_seconds": 0.10810591699555516,
      "engine_upload_seconds": 0.000889208,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0708862915635109,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.1523569170385599,
      "full": 4.7974509169580415
    }
  },
  "elapsed_seconds": 3859.9121997919865,
  "result_class": "passed"
}
```
