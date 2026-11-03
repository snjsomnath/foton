# Foton report

Status: **incomplete**

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
  "sky_density": 1,
  "status": "incomplete",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 13596737419153064380,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": false,
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
        "bias_percent": -0.19400505681663066,
        "rms_normalized_error_percent": 1.3833554241804136,
        "absolute_error": {
          "p95": 0.0,
          "p99": 2.764817327260971e-05,
          "maximum": 0.0005996385589241982
        },
        "worst_index": [
          27,
          105,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.11164251042865557,
        "rms_normalized_error_percent": 1.2067994657041696,
        "absolute_error": {
          "p95": 1.4964491128921509e-05,
          "p99": 0.00010448688408359885,
          "maximum": 0.000701497308909893
        },
        "worst_index": [
          7,
          120,
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
        "identifier": "classroom_01",
        "bias_percent": -27.275395349150866,
        "rms_normalized_error_percent": 115.82450373716414,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 1.17809722723905e-05
        },
        "worst_index": [
          163,
          0,
          0
        ],
        "passed": false
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.06898333031850666,
        "rms_normalized_error_percent": 1.2251289098197413,
        "absolute_error": {
          "p95": 1.0990280225087162e-05,
          "p99": 7.51023180782795e-05,
          "maximum": 0.0012587830424308777
        },
        "worst_index": [
          43,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.040604162774103746,
        "rms_normalized_error_percent": 0.8221456972162448,
        "absolute_error": {
          "p95": 6.077613215893507e-05,
          "p99": 0.00017298921011388302,
          "maximum": 0.0016280412673950195
        },
        "worst_index": [
          248,
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
          "maximum": 8.168140084308106e-06
        },
        "worst_index": [
          142,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.018040748917678016,
        "rms_normalized_error_percent": 1.0077582845811435,
        "absolute_error": {
          "p95": 9.442089321964866e-06,
          "p99": 6.249494617804885e-05,
          "maximum": 0.0010525360703468323
        },
        "worst_index": [
          57,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.01473845546939914,
        "rms_normalized_error_percent": 0.6654705074565229,
        "absolute_error": {
          "p95": 4.963390529155731e-05,
          "p99": 0.00014196569100022316,
          "maximum": 0.0014613419771194458
        },
        "worst_index": [
          134,
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
          "rms_normalized_rmse_percent": 5.0,
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
                "nmbe_percent": -100.0,
                "cvrmse_percent": 11302.654555457315,
                "rms_normalized_rmse_percent": 100.0,
                "reference_energy": 9.481190863880329e-05,
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
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
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
                "nmbe_percent": 0.17857024686629014,
                "cvrmse_percent": 37.83834576582713,
                "rms_normalized_rmse_percent": 3.4697083300713607,
                "reference_energy": 33.08818011768847,
                "candidate_energy": 33.147265762608185,
                "relative_energy_error_percent": 0.1785702468662901,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014115823432803154,
                  "maximum": 0.0009019030258059502
                },
                "worst": {
                  "global_sensor_index": 196,
                  "local_sensor_index": 21,
                  "sky_patch_index": 20,
                  "rgb_channel": 0,
                  "reference": 0.0014801659854128957,
                  "candidate": 0.002382069011218846
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5263390526416996,
                "cvrmse_percent": 107.89539377389549,
                "rms_normalized_rmse_percent": 3.6468680361423247,
                "reference_energy": 19.561282403060904,
                "candidate_energy": 19.458323734576066,
                "relative_energy_error_percent": 0.5263390526416997,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.277442457758297e-06,
                  "p99": 0.0002197159337811172,
                  "maximum": 0.001635916531085968
                },
                "worst": {
                  "global_sensor_index": 177,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0358800757676363,
                  "candidate": 0.03424415923655033
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
                "nmbe_percent": -0.07218116949751162,
                "cvrmse_percent": 15.93065023027946,
                "rms_normalized_rmse_percent": 3.382916348949782,
                "reference_energy": 166.51734157053852,
                "candidate_energy": 166.39714740597674,
                "relative_energy_error_percent": 0.07218116949751162,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.458000042475877e-07,
                  "p95": 0.00012242604861967266,
                  "p99": 0.0003531909896992147,
                  "maximum": 0.0010069701820611954
                },
                "worst": {
                  "global_sensor_index": 1158,
                  "local_sensor_index": 23,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 0.01706582959741354,
                  "candidate": 0.016058859415352345
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1622828961278469,
                "cvrmse_percent": 42.38242996021101,
                "rms_normalized_rmse_percent": 2.4858933511057666,
                "reference_energy": 105.15214650678973,
                "candidate_energy": 105.32279045548154,
                "relative_energy_error_percent": 0.16228289612783678,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3943838220930604e-05,
                  "p95": 0.00019872887060046196,
                  "p99": 0.000565224327147007,
                  "maximum": 0.002976667135953903
                },
                "worst": {
                  "global_sensor_index": 1883,
                  "local_sensor_index": 748,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.09652425721287727,
                  "candidate": 0.09354759007692337
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1612.157667055726,
            "full": 8401.604000013322
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1662.92529203929,
            "full": 8496.58483301755
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1704.3231669813395,
            "full": 8791.269209003076
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1782.9433749429882,
            "full": 8748.767041019164
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
          "rms_normalized_rmse_percent": 5.0,
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
                "nmbe_percent": 41.797929779366406,
                "cvrmse_percent": 11796.580579473875,
                "rms_normalized_rmse_percent": 185.61177275022828,
                "reference_energy": 0.00014714569965690316,
                "candidate_energy": 0.00020864955587285294,
                "relative_energy_error_percent": 41.797929779366406,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 2.3561944544781e-05
                },
                "worst": {
                  "global_sensor_index": 163,
                  "local_sensor_index": 163,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 2.3561944544781e-05
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
                "nmbe_percent": 0.017565995457546738,
                "cvrmse_percent": 21.033421622984623,
                "rms_normalized_rmse_percent": 1.9294163361315293,
                "reference_energy": 33.07678197180849,
                "candidate_energy": 33.08259223782716,
                "relative_energy_error_percent": 0.01756599545754674,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.528840797021985e-05,
                  "maximum": 0.00044856721069663763
                },
                "worst": {
                  "global_sensor_index": 1009,
                  "local_sensor_index": 834,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.000904965796507895,
                  "candidate": 0.0013535330072045326
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.16068182792278737,
                "cvrmse_percent": 43.03503517467642,
                "rms_normalized_rmse_percent": 1.9944642306603064,
                "reference_energy": 31.123866908746546,
                "candidate_energy": 31.073856510477317,
                "relative_energy_error_percent": 0.16068182792278737,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.81412953945437e-09,
                  "p90": 6.427844846257371e-06,
                  "p95": 1.612617215869249e-05,
                  "p99": 0.0001389533281326294,
                  "maximum": 0.0014262162148952484
                },
                "worst": {
                  "global_sensor_index": 229,
                  "local_sensor_index": 54,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.045106224715709686,
                  "candidate": 0.046532440930604935
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
                "nmbe_percent": 0.01970525721137384,
                "cvrmse_percent": 8.938556173054677,
                "rms_normalized_rmse_percent": 1.8985884594504134,
                "reference_energy": 166.47264712029903,
                "candidate_energy": 166.50545098360067,
                "relative_energy_error_percent": 0.01970525721137384,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2190503184684002e-07,
                  "p95": 7.14536290615797e-05,
                  "p99": 0.0001991495955735445,
                  "maximum": 0.0007000956684350967
                },
                "worst": {
                  "global_sensor_index": 1255,
                  "local_sensor_index": 120,
                  "sky_patch_index": 81,
                  "rgb_channel": 0,
                  "reference": 0.00941461930051446,
                  "candidate": 0.008714523632079363
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.01373426477496679,
                "cvrmse_percent": 17.522891592988913,
                "rms_normalized_rmse_percent": 1.3280753929725944,
                "reference_energy": 155.65502427144276,
                "candidate_energy": 155.6764023446118,
                "relative_energy_error_percent": 0.013734264775010158,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.952450734421518e-07,
                  "p90": 3.0363558471435682e-05,
                  "p95": 0.00011590542271733284,
                  "p99": 0.0003309333696961403,
                  "maximum": 0.0020098499953746796
                },
                "worst": {
                  "global_sensor_index": 1900,
                  "local_sensor_index": 765,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11124249920248985,
                  "candidate": 0.11325234919786453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3230.157291982323,
            "full": 131806.79525004234
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3690.8672500867397,
            "full": 123013.00645899028
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3168.2052080286667,
            "full": 124683.63112502266
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3086.8849590187892,
            "full": 124003.09662497602
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
          "rms_normalized_rmse_percent": 5.0,
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
                "nmbe_percent": -38.50285303506075,
                "cvrmse_percent": 7816.053296770299,
                "rms_normalized_rmse_percent": 110.19069793006896,
                "reference_energy": 0.00016021997868165272,
                "candidate_energy": 9.85307157570503e-05,
                "relative_energy_error_percent": 38.50285303506075,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 1.6336280168616213e-05
                },
                "worst": {
                  "global_sensor_index": 142,
                  "local_sensor_index": 142,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 1.6336280168616213e-05,
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
                "nmbe_percent": 0.11256448881270865,
                "cvrmse_percent": 22.34972496184476,
                "rms_normalized_rmse_percent": 2.049707925900924,
                "reference_energy": 33.06387113265282,
                "candidate_energy": 33.101089310174984,
                "relative_energy_error_percent": 0.11256448881270864,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.53599451854825e-05,
                  "maximum": 0.0007683050353080034
                },
                "worst": {
                  "global_sensor_index": 228,
                  "local_sensor_index": 53,
                  "sky_patch_index": 81,
                  "rgb_channel": 0,
                  "reference": 0.004741386044770479,
                  "candidate": 0.003973081009462476
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.07402482037307126,
                "cvrmse_percent": 41.5209965089772,
                "rms_normalized_rmse_percent": 1.9247417926005688,
                "reference_energy": 31.151871175112156,
                "candidate_energy": 31.12881105843193,
                "relative_energy_error_percent": 0.07402482037307126,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.923766283582154e-09,
                  "p90": 6.487388964160409e-06,
                  "p95": 1.607075910214915e-05,
                  "p99": 0.00013475597370415926,
                  "maximum": 0.0012662336230278015
                },
                "worst": {
                  "global_sensor_index": 272,
                  "local_sensor_index": 97,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03365900367498398,
                  "candidate": 0.03239277005195618
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
                "nmbe_percent": -0.006928049700819851,
                "cvrmse_percent": 8.877653618059448,
                "rms_normalized_rmse_percent": 1.885838768331825,
                "reference_energy": 166.49892128992497,
                "candidate_energy": 166.48738616190667,
                "relative_energy_error_percent": 0.006928049700819851,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.5762343537063321e-07,
                  "p95": 7.174955680966377e-05,
                  "p99": 0.00019924482330679893,
                  "maximum": 0.0006412917282432318
                },
                "worst": {
                  "global_sensor_index": 1271,
                  "local_sensor_index": 136,
                  "sky_patch_index": 52,
                  "rgb_channel": 0,
                  "reference": 0.008320139721035957,
                  "candidate": 0.0076788479927927256
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.043746546003529306,
                "cvrmse_percent": 17.395661351559248,
                "rms_normalized_rmse_percent": 1.3188378121627713,
                "reference_energy": 155.75834732173954,
                "candidate_energy": 155.82648621880492,
                "relative_energy_error_percent": 0.04374654600349053,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9684053143009805e-07,
                  "p90": 3.0418869573622946e-05,
                  "p95": 0.0001139784581027925,
                  "p99": 0.0003291293978691101,
                  "maximum": 0.001858249306678772
                },
                "worst": {
                  "global_sensor_index": 1186,
                  "local_sensor_index": 51,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.1302080973982811,
                  "candidate": 0.13206634670495987
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3216.1812090780586,
            "full": 134433.90583305154
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3572.7057080948725,
            "full": 132510.9939579852
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3134.916292037815,
            "full": 145604.2791249929
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3152.3158750496805,
            "full": 140297.99495800398
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
          "rms_normalized_rmse_percent": 5.0,
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
                "reference_energy": 5.940966820361382e-05,
                "candidate_energy": 9.543283466939556e-05,
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
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 7.845254913263489e-06
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
                "nmbe_percent": -0.03819937759586218,
                "cvrmse_percent": 12.450562415150358,
                "rms_normalized_rmse_percent": 1.1422126932534888,
                "reference_energy": 33.07850374380928,
                "candidate_energy": 33.06586796126112,
                "relative_energy_error_percent": 0.03819937759586218,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.8290006816387177e-05,
                  "maximum": 0.0002588033676147461
                },
                "worst": {
                  "global_sensor_index": 222,
                  "local_sensor_index": 47,
                  "sky_patch_index": 52,
                  "rgb_channel": 0,
                  "reference": 0.007929095067083836,
                  "candidate": 0.008187898434698582
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.016171285895213716,
                "cvrmse_percent": 26.881950968057318,
                "rms_normalized_rmse_percent": 1.2453049323575918,
                "reference_energy": 31.141567164210283,
                "candidate_energy": 31.13653117235191,
                "relative_energy_error_percent": 0.01617128589521372,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.219131284813102e-08,
                  "p90": 4.55737826996484e-06,
                  "p95": 1.1090666612290054e-05,
                  "p99": 8.216965943574905e-05,
                  "maximum": 0.0010076146572828293
                },
                "worst": {
                  "global_sensor_index": 257,
                  "local_sensor_index": 82,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.038490310311317444,
                  "candidate": 0.03949792496860027
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
                "nmbe_percent": -0.024859756730454548,
                "cvrmse_percent": 4.831641713525585,
                "rms_normalized_rmse_percent": 1.0264409637729768,
                "reference_energy": 166.5258087394352,
                "candidate_energy": 166.48441082848916,
                "relative_energy_error_percent": 0.024859756730454548,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2099044397474555e-07,
                  "p95": 3.717700019478798e-05,
                  "p99": 0.00011013948824256659,
                  "maximum": 0.0003251219750382006
                },
                "worst": {
                  "global_sensor_index": 1176,
                  "local_sensor_index": 41,
                  "sky_patch_index": 24,
                  "rgb_channel": 0,
                  "reference": 0.0018010115018114448,
                  "candidate": 0.0014758895267732441
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.01143923906316494,
                "cvrmse_percent": 10.944361119433092,
                "rms_normalized_rmse_percent": 0.829286075868206,
                "reference_energy": 155.74186859065497,
                "candidate_energy": 155.72405290598545,
                "relative_energy_error_percent": 0.01143923906316722,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5000000175291461e-07,
                  "p90": 2.0312243577791385e-05,
                  "p95": 6.80361408740282e-05,
                  "p99": 0.00019044044893234968,
                  "maximum": 0.0017726495862007141
                },
                "worst": {
                  "global_sensor_index": 1278,
                  "local_sensor_index": 143,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.12190365046262741,
                  "candidate": 0.1201310008764267
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6495.88608299382,
            "full": 236862.3588340124
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6181.85299995821,
            "full": 234972.6148750633
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6234.008166007698,
            "full": 236308.14329104032
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6338.536249939352,
            "full": 240222.76504093315
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 102255.91070798691,
      "worker_pool_size": 12,
      "invocation_count": 127
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 375404.9816249171,
      "worker_pool_size": 12,
      "invocation_count": 127
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      2020,
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
            "reference_energy": 7.742125132992328e-05,
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
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                17.75,
                12.601876258850098,
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
            "reference_energy": 7.742125132992328e-05,
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
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                17.75,
                12.601876258850098,
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
            "nmbe_percent": -0.04855013220906296,
            "cvrmse_percent": 8.874943807167947,
            "rms_normalized_rmse_percent": 0.8142114372162013,
            "reference_energy": 33.0645365740404,
            "candidate_energy": 33.04848369781939,
            "relative_energy_error_percent": 0.04855013220906296,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.6811303794384003e-05,
              "maximum": 0.0004689320921897888
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.008051724173128605,
              "candidate": 0.008520656265318394,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9228845859005557,
            "cvrmse_percent": 76.55986433365406,
            "rms_normalized_rmse_percent": 3.5480066449150205,
            "reference_energy": 31.14669847759285,
            "candidate_energy": 30.547783413550288,
            "relative_energy_error_percent": 1.922884585900573,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.9893471653631425e-05,
              "p95": 4.1295368100691106e-05,
              "p99": 0.00012233000597916543,
              "maximum": 0.004206143319606781
            },
            "worst": {
              "global_sensor_index": 234,
              "local_sensor_index": 59,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04990918189287186,
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
            "nmbe_percent": -0.9577263850618378,
            "cvrmse_percent": 37.02212869758811,
            "rms_normalized_rmse_percent": 3.5370700446000765,
            "reference_energy": 64.21123505163322,
            "candidate_energy": 63.59626711136967,
            "relative_energy_error_percent": 0.9577263850618185,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.9822544527414727e-05,
              "p95": 4.108280372747682e-05,
              "p99": 0.00011972229549428448,
              "maximum": 0.004206143319606781
            },
            "worst": {
              "global_sensor_index": 234,
              "local_sensor_index": 59,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04990918189287186,
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
            "nmbe_percent": -0.10207868578792265,
            "cvrmse_percent": 3.3215082813127226,
            "rms_normalized_rmse_percent": 0.705672955229831,
            "reference_energy": 166.47837410339352,
            "candidate_energy": 166.3084351669877,
            "relative_energy_error_percent": 0.10207868578791197,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0710209608078003e-07,
              "p95": 1.0294141247868538e-05,
              "p99": 5.915109068155289e-05,
              "maximum": 0.00031820032745599747
            },
            "worst": {
              "global_sensor_index": 1201,
              "local_sensor_index": 66,
              "sky_patch_index": 82,
              "rgb_channel": 0,
              "reference": 0.010633326135575771,
              "candidate": 0.010315125808119774,
              "position": [
                1.659999966621399,
                9.095957279205322,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.5703685901001638,
            "cvrmse_percent": 38.26221036228563,
            "rms_normalized_rmse_percent": 2.900368637849505,
            "reference_energy": 155.75969641103174,
            "candidate_energy": 153.31369506255754,
            "relative_energy_error_percent": 1.570368590100153,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.5794899961038027e-07,
              "p90": 5.627726768580038e-05,
              "p95": 9.331200271844864e-05,
              "p99": 0.0002519376575946808,
              "maximum": 0.006335407495498657
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13038484752178192,
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
            "nmbe_percent": -0.8118036086499455,
            "cvrmse_percent": 18.470156012633435,
            "rms_normalized_rmse_percent": 2.896512889923549,
            "reference_energy": 322.23807051442526,
            "candidate_energy": 319.6221302295452,
            "relative_energy_error_percent": 0.8118036086499524,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.569224216766088e-07,
              "p90": 5.536097014555708e-05,
              "p95": 9.051091910805553e-05,
              "p99": 0.0002484999131411314,
              "maximum": 0.006335407495498657
            },
            "worst": {
              "global_sensor_index": 1249,
              "local_sensor_index": 114,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13038484752178192,
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
            "reference_energy": 4.7405954319401644e-05,
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
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                13.25,
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
            "reference_energy": 4.7405954319401644e-05,
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
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 7.90099238656694e-06,
              "candidate": 0.0,
              "position": [
                13.25,
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
            "nmbe_percent": -0.04855013220906296,
            "cvrmse_percent": 8.874943807167947,
            "rms_normalized_rmse_percent": 0.8142114372162013,
            "reference_energy": 33.0645365740404,
            "candidate_energy": 33.04848369781939,
            "relative_energy_error_percent": 0.04855013220906296,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.6811303794384003e-05,
              "maximum": 0.0004689320921897888
            },
            "worst": {
              "global_sensor_index": 971,
              "local_sensor_index": 796,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.008051724173128605,
              "candidate": 0.008520656265318394,
              "position": [
                0.12999999523162842,
                2.2442747354507446,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 56.15089559700656,
            "cvrmse_percent": 584.3944522318704,
            "rms_normalized_rmse_percent": 19.770123262646088,
            "reference_energy": 19.56298956644338,
            "candidate_energy": 30.547783413550288,
            "relative_energy_error_percent": 56.15089559700655,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.225999873597175e-05,
              "p95": 0.00010090041229204862,
              "p99": 0.0002791760489344597,
              "maximum": 0.01124533824622631
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019578002393245697,
              "candidate": 0.030823340639472008,
              "position": [
                1.6424999833106995,
                0.2049015462398529,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.842212764487485,
            "cvrmse_percent": 217.20661131312798,
            "rms_normalized_rmse_percent": 19.767605489496344,
            "reference_energy": 52.62752614048378,
            "candidate_energy": 63.59626711136967,
            "relative_energy_error_percent": 20.84221276448747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.211563391436374e-05,
              "p95": 0.00010038834839178888,
              "p99": 0.00027692000730894506,
              "maximum": 0.01124533824622631
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019578002393245697,
              "candidate": 0.030823340639472008,
              "position": [
                1.6424999833106995,
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
            "nmbe_percent": -0.10207868578792265,
            "cvrmse_percent": 3.3215082813127226,
            "rms_normalized_rmse_percent": 0.705672955229831,
            "reference_energy": 166.47837410339352,
            "candidate_energy": 166.3084351669877,
            "relative_energy_error_percent": 0.10207868578791197,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0710209608078003e-07,
              "p95": 1.0294141247868538e-05,
              "p99": 5.915109068155289e-05,
              "maximum": 0.00031820032745599747
            },
            "worst": {
              "global_sensor_index": 1201,
              "local_sensor_index": 66,
              "sky_patch_index": 82,
              "rgb_channel": 0,
              "reference": 0.010633326135575771,
              "candidate": 0.010315125808119774,
              "position": [
                1.659999966621399,
                9.095957279205322,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 45.7128204687014,
            "cvrmse_percent": 280.61942674519486,
            "rms_normalized_rmse_percent": 16.45953682223463,
            "reference_energy": 105.21633893943383,
            "candidate_energy": 153.31369506255754,
            "relative_energy_error_percent": 45.71282046870137,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023788099788362194,
              "p95": 0.0003911700041498989,
              "p99": 0.000876809936016798,
              "maximum": 0.016408022493124008
            },
            "worst": {
              "global_sensor_index": 1918,
              "local_sensor_index": 783,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024402208626270294,
              "candidate": 0.0408102311193943,
              "position": [
                1.7049999833106995,
                24.131555557250977,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.640172916858738,
            "cvrmse_percent": 108.6507440250282,
            "rms_normalized_rmse_percent": 16.456238867558998,
            "reference_energy": 271.6947130428273,
            "candidate_energy": 319.6221302295452,
            "relative_energy_error_percent": 17.640172916858738,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023643400199944292,
              "p95": 0.00038760999450460076,
              "p99": 0.0008751119021326303,
              "maximum": 0.016408022493124008
            },
            "worst": {
              "global_sensor_index": 1918,
              "local_sensor_index": 783,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024402208626270294,
              "candidate": 0.0408102311193943,
              "position": [
                1.7049999833106995,
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
      "bias_percent": -0.023742132932591746,
      "rms_normalized_error_percent": 0.35839751678929005,
      "absolute_error": {
        "p95": 0.13815182004951881,
        "p99": 0.20065670466253752,
        "maximum": 0.3090384836925306
      },
      "worst_index": [
        250
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.978089859384727,
      "rms_normalized_to_uniform_percent": 0.35839751678929005
    },
    "overcast": {
      "bias_percent": -0.02314974988550985,
      "rms_normalized_error_percent": 0.25907218847076896,
      "absolute_error": {
        "p95": 0.07259778976440427,
        "p99": 0.10322829127311706,
        "maximum": 0.16637849807739258
      },
      "worst_index": [
        250
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.373417854309082,
      "rms_normalized_to_uniform_percent": 0.185445511880193
    },
    "horizon": {
      "bias_percent": -0.0320921144315449,
      "rms_normalized_error_percent": 2.6362994080535542,
      "absolute_error": {
        "p95": 0.09532385579115701,
        "p99": 0.160798024052915,
        "maximum": 0.23772163414134262
      },
      "worst_index": [
        1951
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.2551680650050174,
      "rms_normalized_to_uniform_percent": 0.2638281070703743
    },
    "north": {
      "bias_percent": -0.1655873615438478,
      "rms_normalized_error_percent": 0.650404112499353,
      "absolute_error": {
        "p95": 0.05342870205640792,
        "p99": 0.07962658643722532,
        "maximum": 0.17964839935302734
      },
      "worst_index": [
        962
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.3874961137771606,
      "rms_normalized_to_uniform_percent": 0.13482520019336913
    },
    "east": {
      "bias_percent": -4.35749840615246,
      "rms_normalized_error_percent": 4.675671820114631,
      "absolute_error": {
        "p95": 0.0002685080482478952,
        "p99": 0.0010938823781907522,
        "maximum": 0.0018902942538261414
      },
      "worst_index": [
        1883
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 0.0005811838782392442,
      "rms_normalized_to_uniform_percent": 0.0010951738054713338
    },
    "south": {
      "bias_percent": 0.02059515357921622,
      "rms_normalized_error_percent": 0.6586804942138744,
      "absolute_error": {
        "p95": 0.05112899243831634,
        "p99": 0.08145034790039063,
        "maximum": 0.1501915454864502
      },
      "worst_index": [
        250
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.387076497077942,
      "rms_normalized_to_uniform_percent": 0.13508940515545248
    },
    "west": {
      "bias_percent": -0.0069803566423406,
      "rms_normalized_error_percent": 0.4610011743074979,
      "absolute_error": {
        "p95": 0.10606478452682494,
        "p99": 0.15899612188339232,
        "maximum": 0.23163294792175293
      },
      "worst_index": [
        1971
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.779177188873291,
      "rms_normalized_to_uniform_percent": 0.2850459257984304
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
          "cvrmse_percent": 888.1181177346995,
          "absolute_error_percentiles_lux": {
            "p50": 1.1754943508222875e-38,
            "p90": 0.0008039058302529155,
            "p95": 0.0017998541123233646,
            "p99": 0.007332920106127865
          },
          "maximum_absolute_error_lux": 0.4313282072544098,
          "worst": {
            "sensor_index": 154,
            "position": [
              23.75,
              11.536043643951416,
              0.800000011920929
            ],
            "hour_of_year": 3366.5,
            "foton_lux": 1.1754943508222875e-38,
            "radiance_lux": 0.4313282072544098
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
            "mean_absolute_error_percentage_points": 0.00013756293486583162,
            "maximum_error_percentage_points": 0.0029458335727288744,
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
          "nmbe_percent": -0.30326033449582457,
          "cvrmse_percent": 5.745168225105309,
          "absolute_error_percentiles_lux": {
            "p50": 0.7472386360168457,
            "p90": 7.201171875,
            "p95": 13.603562068939206,
            "p99": 36.30432189941405
          },
          "maximum_absolute_error_lux": 431.806640625,
          "worst": {
            "sensor_index": 827,
            "position": [
              2.104230761528015,
              7.351144790649414,
              0.800000011920929
            ],
            "hour_of_year": 1358.5,
            "foton_lux": 5914.45068359375,
            "radiance_lux": 6346.25732421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.17768921232876705,
            "maximum_error_percentage_points": 4.278082191780822,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.41950896717998193,
            "maximum_error_percentage_points": 2.6491820366333663,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.40743964041095876,
            "maximum_error_percentage_points": 7.97383561643835,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4069366438356165,
            "maximum_error_percentage_points": 7.973835616438354,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004753710045662095,
            "maximum_error_percentage_points": 0.16726027397260168,
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
          "nmbe_percent": -0.18887959513160874,
          "cvrmse_percent": 2.24681325057465,
          "absolute_error_percentiles_lux": {
            "p50": 2.8084640502929688,
            "p90": 21.733135986328136,
            "p95": 35.762646484374955,
            "p99": 74.57426513671874
          },
          "maximum_absolute_error_lux": 468.0,
          "worst": {
            "sensor_index": 784,
            "position": [
              2.209999978542328,
              24.131555557250977,
              0.800000011920929
            ],
            "hour_of_year": 1358.5,
            "foton_lux": 9878.4345703125,
            "radiance_lux": 10346.4345703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5770819596006501,
            "maximum_error_percentage_points": 3.534246575342465,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4348313019899665,
            "maximum_error_percentage_points": 2.545608183216345,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3563591053324045,
            "maximum_error_percentage_points": 3.1550684931506865,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3666750251528519,
            "maximum_error_percentage_points": 3.1550684931506865,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02041328070582768,
            "maximum_error_percentage_points": 0.3876712328767127,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 40.11244725165375,
          "radiance_percent": 40.357247280083136,
          "difference_percentage_points": 0.2448000284293883,
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
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.005002675513694044,
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
            "maximum_error_percentage_points": 0.004997775979237673,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.005002675513694044,
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
            "maximum_error_percentage_points": 0.004931506849315426,
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
        "maximum_error_percentage_points": 0.005002675513694044,
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
              "maximum_error_percentage_points": 0.004997775979237673,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.005002675513694044,
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
              "maximum_error_percentage_points": 0.004931506849315426,
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
            "nmbe_percent": 15.917558466541761,
            "cvrmse_percent": 45.307278968855314,
            "absolute_error_lux": {
              "p50": 5.122928440570831,
              "p90": 51.06165900230412,
              "p95": 90.39502029418945,
              "p99": 230.84055328369124,
              "maximum": 2272.845703125
            },
            "per_sensor_maximum_error_lux": {
              "p50": 112.04190254211426,
              "p90": 664.2611816406251,
              "p95": 948.5814056396474,
              "p99": 1767.1253417968737,
              "maximum": 2272.845703125
            },
            "worst": {
              "sensor_index": 33,
              "sun_up_hour_index": 2390,
              "hour_of_year": 4455.5,
              "foton_lux": 21950.19921875,
              "radiance_lux": 19677.353515625
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.9073229166666663,
              "maximum_error_percentage_points": 33.51,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.2260937499999995,
              "maximum_error_percentage_points": 22.86,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.466968749999999,
              "maximum_error_percentage_points": 43.53,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.451,
              "maximum_error_percentage_points": 43.53,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.03615625000000001,
              "maximum_error_percentage_points": 1.0700000000000012,
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
            "nmbe_percent": 15.38861342312177,
            "cvrmse_percent": 26.87947474353571,
            "absolute_error_lux": {
              "p50": 59.2824821472168,
              "p90": 248.29836425781252,
              "p95": 377.8158203124999,
              "p99": 723.1254003906249,
              "maximum": 3080.689453125
            },
            "per_sensor_maximum_error_lux": {
              "p50": 729.026123046875,
              "p90": 1696.7337890625001,
              "p95": 1903.2703125,
              "p99": 2402.7139062499996,
              "maximum": 3080.689453125
            },
            "worst": {
              "sensor_index": 13,
              "sun_up_hour_index": 2880,
              "hour_of_year": 5150.5,
              "foton_lux": 32207.8046875,
              "radiance_lux": 29127.115234375
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.802112994350281,
              "maximum_error_percentage_points": 39.23,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.600926553672316,
              "maximum_error_percentage_points": 33.07,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 13.131593220338985,
              "maximum_error_percentage_points": 54.599999999999994,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 13.105728813559322,
              "maximum_error_percentage_points": 54.6,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.3677853107344633,
              "maximum_error_percentage_points": 2.42,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 40.11244725165375,
            "radiance_percent": 31.29615331697506,
            "difference_percentage_points": 8.816293934678686,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 0.8530802078312263,
        "radiance_seconds": 21.48324183304794,
        "speedup": 25.183144135607698,
        "passed": true
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/acceptance/mf1/stock/annual_daylight"
      },
      "reference_sky_density": 1,
      "candidate_sky_density": 1
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
      "study_preparation_seconds": 0.14097283291630447,
      "weather_seconds": 0.1348579169716686,
      "metric_reduction_seconds": 0.4372495840070769,
      "write_seconds": 0.1397867500782013,
      "total_seconds": 0.7121073749149218,
      "cold_end_to_end_seconds": 0.8530802078312263,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.09889649995602667,
      "engine_upload_seconds": 0.000518208,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.3489648333052173,
      "engine_annual_reduction_seconds": 0.016242041834630072,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.3489648333052173
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.14097283291630447,
      "weather_seconds": 0.09208804101217538,
      "metric_reduction_seconds": 0.07538216700777411,
      "write_seconds": 0.13084983301814646,
      "total_seconds": 0.2985551250167191,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2985551250167191,
      "raw_export_seconds": 0.09313370799645782,
      "engine_upload_seconds": 0.000300709,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.015234083170071244,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.06050162494648248,
      "full": 0.3709277919260785
    }
  },
  "elapsed_seconds": 2609.3753295830684,
  "result_class": "unstable_reference"
}
```
