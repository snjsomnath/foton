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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "697cbb4284d0a8110eaba85b2ed13854f6bc9d8e7ddb0478d07c5f4948d1410c",
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
    "maximum_samples": 65536,
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
    "passed": true,
    "grids": [
      {
        "identifier": "classroom_01",
        "bias_percent": 0.0,
        "rms_normalized_error_percent": 0.0,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 7.853982424421702e-06
        },
        "worst_index": [
          116,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.027392867693978435,
        "rms_normalized_error_percent": 1.1596288652016478,
        "absolute_error": {
          "p95": 1.0983464744640514e-05,
          "p99": 7.379049202427268e-05,
          "maximum": 0.0011086724698543549
        },
        "worst_index": [
          39,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.022861025654036273,
        "rms_normalized_error_percent": 0.8014092584922551,
        "absolute_error": {
          "p95": 6.238557398319244e-05,
          "p99": 0.00017463555559515953,
          "maximum": 0.0017821118235588074
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
          "maximum": 7.853982424421702e-06
        },
        "worst_index": [
          116,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.02581792447198822,
        "rms_normalized_error_percent": 0.980233631455213,
        "absolute_error": {
          "p95": 9.423350638826377e-06,
          "p99": 6.205477984622121e-05,
          "maximum": 0.0006413273513317108
        },
        "worst_index": [
          107,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.004865282405758466,
        "rms_normalized_error_percent": 0.673600265359659,
        "absolute_error": {
          "p95": 5.0737289711833e-05,
          "p99": 0.00014223158359527588,
          "maximum": 0.0012932568788528442
        },
        "worst_index": [
          169,
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 5.925744153501e-05,
                "candidate_energy": 2.9628720767505e-05,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 9.876240255835e-06
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 9.876240255835e-06,
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
                "nmbe_percent": -0.07429340143838747,
                "cvrmse_percent": 39.951314795836836,
                "rms_normalized_rmse_percent": 3.664248424863946,
                "reference_energy": 33.066061729121884,
                "candidate_energy": 33.0414958271416,
                "relative_energy_error_percent": 0.07429340143838746,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001458065235055983,
                  "maximum": 0.0009524779161438346
                },
                "worst": {
                  "global_sensor_index": 286,
                  "local_sensor_index": 111,
                  "sky_patch_index": 53,
                  "rgb_channel": 0,
                  "reference": 0.0035155945224687457,
                  "candidate": 0.00446807243861258
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.16193451573622195,
                "cvrmse_percent": 111.35334268021667,
                "rms_normalized_rmse_percent": 3.7689135204713975,
                "reference_energy": 19.569868828361265,
                "candidate_energy": 19.538178456043845,
                "relative_energy_error_percent": 0.16193451573622195,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.257987934077388e-06,
                  "p99": 0.0002337130717933178,
                  "maximum": 0.0019090697169303894
                },
                "worst": {
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05297512002289295,
                  "candidate": 0.05488418973982334
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
                "nmbe_percent": -0.053075060859058186,
                "cvrmse_percent": 15.649320962826682,
                "rms_normalized_rmse_percent": 3.323514301638492,
                "reference_energy": 166.58437969565307,
                "candidate_energy": 166.49596493474792,
                "relative_energy_error_percent": 0.053075060859058186,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.1689262464642931e-07,
                  "p95": 0.00012230093125253916,
                  "p99": 0.00035176449455320835,
                  "maximum": 0.0010295156389474869
                },
                "worst": {
                  "global_sensor_index": 1880,
                  "local_sensor_index": 745,
                  "sky_patch_index": 136,
                  "rgb_channel": 0,
                  "reference": 0.020366075448691845,
                  "candidate": 0.019336559809744358
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.18187267113273112,
                "cvrmse_percent": 42.1707644711467,
                "rms_normalized_rmse_percent": 2.471022403550008,
                "reference_energy": 105.16020016143783,
                "candidate_energy": 105.35145782643995,
                "relative_energy_error_percent": 0.18187267113272435,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.414599939584201e-05,
                  "p95": 0.00019949954003095627,
                  "p99": 0.0005551415961235762,
                  "maximum": 0.00348774716258049
                },
                "worst": {
                  "global_sensor_index": 1213,
                  "local_sensor_index": 78,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.12323379889130592,
                  "candidate": 0.11974605172872543
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1578.0012080213055,
            "full": 8007.279374985956
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1580.0523329526186,
            "full": 8192.374791018665
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1632.3391669429839,
            "full": 8225.177707965486
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1619.064333033748,
            "full": 8201.112540904433
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.0002814783720133107,
                "candidate_energy": 0.000128906536613016,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 7.853979695937596e-06
                },
                "worst": {
                  "global_sensor_index": 111,
                  "local_sensor_index": 111,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 7.853979695937596e-06,
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
                "nmbe_percent": 0.15664134780889177,
                "cvrmse_percent": 21.88785738168847,
                "rms_normalized_rmse_percent": 2.0076742913634815,
                "reference_energy": 33.06537768613771,
                "candidate_energy": 33.117171739403375,
                "relative_energy_error_percent": 0.15664134780889177,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.535854820162058e-05,
                  "maximum": 0.0006141285412013531
                },
                "worst": {
                  "global_sensor_index": 246,
                  "local_sensor_index": 71,
                  "sky_patch_index": 78,
                  "rgb_channel": 0,
                  "reference": 0.0028268914902582765,
                  "candidate": 0.0022127629490569234
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.2306349737590641,
                "cvrmse_percent": 43.337051716927114,
                "rms_normalized_rmse_percent": 2.007785635973171,
                "reference_energy": 31.1505901206852,
                "candidate_energy": 31.078745965334566,
                "relative_energy_error_percent": 0.2306349737590641,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.46733874734673e-09,
                  "p90": 6.4336246964558345e-06,
                  "p95": 1.60334654538019e-05,
                  "p99": 0.00013957816008769441,
                  "maximum": 0.001309053972363472
                },
                "worst": {
                  "global_sensor_index": 217,
                  "local_sensor_index": 42,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05443541519343853,
                  "candidate": 0.055744469165802
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
                "nmbe_percent": -0.015230713790955487,
                "cvrmse_percent": 8.703933921050638,
                "rms_normalized_rmse_percent": 1.8490211333171453,
                "reference_energy": 166.50316248055276,
                "candidate_energy": 166.47780286042246,
                "relative_energy_error_percent": 0.015230713790955488,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.416541635990468e-07,
                  "p95": 7.102650124579668e-05,
                  "p99": 0.0001977980136871338,
                  "maximum": 0.0005798912607133389
                },
                "worst": {
                  "global_sensor_index": 1157,
                  "local_sensor_index": 22,
                  "sky_patch_index": 56,
                  "rgb_channel": 0,
                  "reference": 0.008006293792277575,
                  "candidate": 0.007426402531564236
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.06365266622476735,
                "cvrmse_percent": 17.895216341223456,
                "rms_normalized_rmse_percent": 1.3561878304772115,
                "reference_energy": 155.67977309238313,
                "candidate_energy": 155.7788674187291,
                "relative_energy_error_percent": 0.06365266622477192,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9371754156338739e-07,
                  "p90": 2.99056719086367e-05,
                  "p95": 0.00011366745457053185,
                  "p99": 0.00033113081008195877,
                  "maximum": 0.0022791512310504913
                },
                "worst": {
                  "global_sensor_index": 1223,
                  "local_sensor_index": 88,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11593849956989288,
                  "candidate": 0.11365934833884239
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3136.035874951631,
            "full": 119221.60254104529
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3057.6674580806866,
            "full": 120190.557874972
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3051.3768329983577,
            "full": 120771.96100004949
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3070.4393750056624,
            "full": 120871.88491702545
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
                "nmbe_percent": -13.37501074361279,
                "cvrmse_percent": 6011.43082349499,
                "rms_normalized_rmse_percent": 124.42409576739706,
                "reference_energy": 0.0002137923910972006,
                "candidate_energy": 0.00018519763581892335,
                "relative_energy_error_percent": 13.375010743612792,
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
                  "global_sensor_index": 116,
                  "local_sensor_index": 116,
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
                "nmbe_percent": 0.12733585016101395,
                "cvrmse_percent": 20.542364624565366,
                "rms_normalized_rmse_percent": 1.8835444566039532,
                "reference_energy": 33.07655236810433,
                "candidate_energy": 33.11867067726621,
                "relative_energy_error_percent": 0.12733585016101395,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.516809273511171e-05,
                  "maximum": 0.00043408479541540146
                },
                "worst": {
                  "global_sensor_index": 223,
                  "local_sensor_index": 48,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.0048564583994448185,
                  "candidate": 0.004422373604029417
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.15538796718681777,
                "cvrmse_percent": 41.55021914630714,
                "rms_normalized_rmse_percent": 1.9251345947697234,
                "reference_energy": 31.150120849102947,
                "candidate_energy": 31.10171730953929,
                "relative_energy_error_percent": 0.15538796718681777,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.310077793614255e-09,
                  "p90": 6.377618774422456e-06,
                  "p95": 1.5803343944753555e-05,
                  "p99": 0.0001364754280075431,
                  "maximum": 0.001451665535569191
                },
                "worst": {
                  "global_sensor_index": 204,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05811556428670883,
                  "candidate": 0.05666389875113964
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
                "nmbe_percent": -0.0026430777816147696,
                "cvrmse_percent": 8.788856970182797,
                "rms_normalized_rmse_percent": 1.8667322762658543,
                "reference_energy": 166.49263931302448,
                "candidate_energy": 166.48823878306678,
                "relative_energy_error_percent": 0.0026430777816147696,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.3063836377115785e-07,
                  "p95": 7.21546821296215e-05,
                  "p99": 0.00019925402011722326,
                  "maximum": 0.0006532843690365553
                },
                "worst": {
                  "global_sensor_index": 1145,
                  "local_sensor_index": 10,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.008053835947066545,
                  "candidate": 0.00740055157802999
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.010380239185216137,
                "cvrmse_percent": 17.78977511484767,
                "rms_normalized_rmse_percent": 1.3484558623598268,
                "reference_energy": 155.8111134403764,
                "candidate_energy": 155.79493987412405,
                "relative_energy_error_percent": 0.010380239185273142,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9194377820497266e-07,
                  "p90": 3.0337534553837343e-05,
                  "p95": 0.00011578504927456379,
                  "p99": 0.0003332594642415643,
                  "maximum": 0.002329304814338684
                },
                "worst": {
                  "global_sensor_index": 1368,
                  "local_sensor_index": 233,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0726950354874134,
                  "candidate": 0.07036573067307472
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3058.714166050777,
            "full": 126046.20954103302
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3075.5430000135675,
            "full": 126377.29983404279
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3067.338459077291,
            "full": 125997.72654194385
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3095.749083906412,
            "full": 125895.76616697013
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
                "reference_energy": 0.00016117822687178318,
                "candidate_energy": 0.0001523351180772181,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 3.922627001884393e-06
                },
                "worst": {
                  "global_sensor_index": 153,
                  "local_sensor_index": 153,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 3.922627001884393e-06
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
                "nmbe_percent": -0.004156664840422302,
                "cvrmse_percent": 12.69289568195191,
                "rms_normalized_rmse_percent": 1.164463420177045,
                "reference_energy": 33.078508853837775,
                "candidate_energy": 33.07713389109051,
                "relative_energy_error_percent": 0.004156664840422302,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.9114925786852837e-05,
                  "maximum": 0.00028279516845941544
                },
                "worst": {
                  "global_sensor_index": 182,
                  "local_sensor_index": 7,
                  "sky_patch_index": 121,
                  "rgb_channel": 0,
                  "reference": 0.018741010688245296,
                  "candidate": 0.01845821551978588
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.02903931497091652,
                "cvrmse_percent": 26.02402690227246,
                "rms_normalized_rmse_percent": 1.2055155715069412,
                "reference_energy": 31.133648529906843,
                "candidate_energy": 31.124607531648305,
                "relative_energy_error_percent": 0.02903931497091652,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4571574169508494e-08,
                  "p90": 4.575371167447895e-06,
                  "p95": 1.1219220004932131e-05,
                  "p99": 8.312903810292482e-05,
                  "maximum": 0.0008143298327922821
                },
                "worst": {
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06043658405542374,
                  "candidate": 0.06125091388821602
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
                "nmbe_percent": 0.024916227416607453,
                "cvrmse_percent": 5.014210545575104,
                "rms_normalized_rmse_percent": 1.0648678592760024,
                "reference_energy": 166.47072057188916,
                "candidate_energy": 166.51219879520892,
                "relative_energy_error_percent": 0.024916227416607456,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.3832541299053883e-07,
                  "p95": 3.745045978575945e-05,
                  "p99": 0.00011223694309592247,
                  "maximum": 0.00033540790900588036
                },
                "worst": {
                  "global_sensor_index": 1288,
                  "local_sensor_index": 153,
                  "sky_patch_index": 25,
                  "rgb_channel": 0,
                  "reference": 0.0024353875778615475,
                  "candidate": 0.002770795486867428
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.011740611998939221,
                "cvrmse_percent": 11.116804054535804,
                "rms_normalized_rmse_percent": 0.8429185162891447,
                "reference_energy": 155.79547141026535,
                "candidate_energy": 155.7771800684551,
                "relative_energy_error_percent": 0.011740611998975706,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5348844506490877e-07,
                  "p90": 2.034263015957552e-05,
                  "p95": 6.938455044291914e-05,
                  "p99": 0.00019594542391132563,
                  "maximum": 0.0017481595277786255
                },
                "worst": {
                  "global_sensor_index": 1215,
                  "local_sensor_index": 80,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.13505179435014725,
                  "candidate": 0.13679995387792587
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5987.250874983147,
            "full": 224692.60208308697
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5970.317875035107,
            "full": 225297.94533294626
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6060.5421249056235,
            "full": 222849.72366690636
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5948.235874995589,
            "full": 224653.13470794354
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 91231.2658749288,
      "worker_pool_size": 12,
      "invocation_count": 127
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 393443.1382500334,
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
            "reference_energy": 0.00015675667220804712,
            "candidate_energy": 1.89599993518641e-05,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.789999820786761e-06
            },
            "worst": {
              "global_sensor_index": 171,
              "local_sensor_index": 171,
              "sky_patch_index": 138,
              "rgb_channel": 0,
              "reference": 0.0,
              "candidate": 4.789999820786761e-06,
              "position": [
                24.75,
                13.134792804718018,
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
            "reference_energy": 0.00015675667220804712,
            "candidate_energy": 1.89599993518641e-05,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.789999820786761e-06
            },
            "worst": {
              "global_sensor_index": 171,
              "local_sensor_index": 171,
              "sky_patch_index": 138,
              "rgb_channel": 0,
              "reference": 0.0,
              "candidate": 4.789999820786761e-06,
              "position": [
                24.75,
                13.134792804718018,
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
            "nmbe_percent": -1.930269309590794,
            "cvrmse_percent": 52.25856864830853,
            "rms_normalized_rmse_percent": 2.4217826483145246,
            "reference_energy": 31.142412909569543,
            "candidate_energy": 30.54128047091008,
            "relative_energy_error_percent": 1.930269309590794,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0439251673233253e-05,
              "p95": 2.194814132963072e-05,
              "p99": 7.091725274221972e-05,
              "maximum": 0.002124253660440445
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06015446409583092,
              "candidate": 0.05803021043539047,
              "position": [
                1.024999976158142,
                2.761048436164856,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9612437903439425,
            "cvrmse_percent": 25.1627855743627,
            "rms_normalized_rmse_percent": 2.4041753932800862,
            "reference_energy": 64.20694948360998,
            "candidate_energy": 63.58976416872946,
            "relative_energy_error_percent": 0.9612437903440089,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.044072068907555e-05,
              "p95": 2.17268834603601e-05,
              "p99": 6.719119846820831e-05,
              "maximum": 0.002124253660440445
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06015446409583092,
              "candidate": 0.05803021043539047,
              "position": [
                1.024999976158142,
                2.761048436164856,
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
            "nmbe_percent": -1.608493639668138,
            "cvrmse_percent": 31.47707637329188,
            "rms_normalized_rmse_percent": 2.3862455392908015,
            "reference_energy": 155.79941117640837,
            "candidate_energy": 153.29338755699544,
            "relative_energy_error_percent": 1.6084936396681315,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.852305496820918e-07,
              "p90": 3.078271038248207e-05,
              "p95": 5.543146107811481e-05,
              "p99": 0.0001598864037077874,
              "maximum": 0.00479646772146225
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1202610433101654,
              "candidate": 0.11546457558870316,
              "position": [
                2.6799999475479126,
                16.6557559967041,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.8303279586880338,
            "cvrmse_percent": 15.188083215865316,
            "rms_normalized_rmse_percent": 2.381706644378942,
            "reference_energy": 322.27778527980195,
            "candidate_energy": 319.60182272398316,
            "relative_energy_error_percent": 0.830327958688034,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.85755104304053e-07,
              "p90": 3.0224957299651758e-05,
              "p95": 5.344906821846962e-05,
              "p99": 0.00014841021038591862,
              "maximum": 0.00479646772146225
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1202610433101654,
              "candidate": 0.11546457558870316,
              "position": [
                2.6799999475479126,
                16.6557559967041,
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
            "reference_energy": 4.44430811512575e-05,
            "candidate_energy": 1.89599993518641e-05,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.9381201279175e-06
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 95,
              "rgb_channel": 0,
              "reference": 4.9381201279175e-06,
              "candidate": 0.0,
              "position": [
                14.25,
                11.536043643951416,
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
            "reference_energy": 4.44430811512575e-05,
            "candidate_energy": 1.89599993518641e-05,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.9381201279175e-06
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 95,
              "rgb_channel": 0,
              "reference": 4.9381201279175e-06,
              "candidate": 0.0,
              "position": [
                14.25,
                11.536043643951416,
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
            "nmbe_percent": 56.27521382414306,
            "cvrmse_percent": 578.3594685043726,
            "rms_normalized_rmse_percent": 19.560783871726773,
            "reference_energy": 19.543265834387707,
            "candidate_energy": 30.54128047091008,
            "relative_energy_error_percent": 56.27521382414303,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.229180303809731e-05,
              "p95": 9.774357386049806e-05,
              "p99": 0.0002566687762737274,
              "maximum": 0.010535459965467453
            },
            "worst": {
              "global_sensor_index": 965,
              "local_sensor_index": 790,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019906289875507355,
              "candidate": 0.030441749840974808,
              "position": [
                2.147499978542328,
                0.2049015462398529,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.875157785610124,
            "cvrmse_percent": 214.81715386341847,
            "rms_normalized_rmse_percent": 19.557366920187633,
            "reference_energy": 52.60780240842811,
            "candidate_energy": 63.58976416872946,
            "relative_energy_error_percent": 20.875157785610092,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.216999877826311e-05,
              "p95": 9.7341001674067e-05,
              "p99": 0.00025320472195744514,
              "maximum": 0.010535459965467453
            },
            "worst": {
              "global_sensor_index": 965,
              "local_sensor_index": 790,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019906289875507355,
              "candidate": 0.030441749840974808,
              "position": [
                2.147499978542328,
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
            "nmbe_percent": 45.553400378378875,
            "cvrmse_percent": 277.31046382129875,
            "rms_normalized_rmse_percent": 16.276566375457136,
            "reference_energy": 105.31762717909425,
            "candidate_energy": 153.29338755699544,
            "relative_energy_error_percent": 45.5534003783789,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023621835341600678,
              "p95": 0.000387185369618237,
              "p99": 0.0008352268487215042,
              "maximum": 0.015515660867094994
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024418169632554054,
              "candidate": 0.03993383049964905,
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
            "nmbe_percent": 17.588861210584533,
            "cvrmse_percent": 107.43163466681895,
            "rms_normalized_rmse_percent": 16.273115897346432,
            "reference_energy": 271.7960012824878,
            "candidate_energy": 319.60182272398316,
            "relative_energy_error_percent": 17.588861210584547,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023526299919467524,
              "p95": 0.0003841039724647999,
              "p99": 0.000832790625281632,
              "maximum": 0.015515660867094994
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024418169632554054,
              "candidate": 0.03993383049964905,
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
      "bias_percent": -0.0072889676138531995,
      "rms_normalized_error_percent": 0.22526810742477885,
      "absolute_error": {
        "p95": 0.08415742272284357,
        "p99": 0.1353130958664388,
        "maximum": 0.22366407184168535
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.9786353144245155,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22526810742477885
    },
    "overcast": {
      "bias_percent": -0.01745459650912838,
      "rms_normalized_error_percent": 0.16181365953643376,
      "absolute_error": {
        "p95": 0.045931941270828246,
        "p99": 0.06836631536483763,
        "maximum": 0.09211349487304688
      },
      "worst_index": [
        1219
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.3737335205078125,
      "reference_fraction_of_uniform": 0.6267319321632385,
      "rms_normalized_to_uniform_percent": 0.11582506555417445
    },
    "horizon": {
      "bias_percent": 0.06254015692358675,
      "rms_normalized_error_percent": 1.6899416366985498,
      "absolute_error": {
        "p95": 0.05903807566619154,
        "p99": 0.12077063062804926,
        "maximum": 0.21645106278178927
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2553926123739887,
      "reference_fraction_of_uniform": 0.17989084624885762,
      "rms_normalized_to_uniform_percent": 0.16915352020866087
    },
    "north": {
      "bias_percent": -0.11846143894856732,
      "rms_normalized_error_percent": 0.3759872848697314,
      "absolute_error": {
        "p95": 0.031098918616771696,
        "p99": 0.04977031707763671,
        "maximum": 0.07214212417602539
      },
      "worst_index": [
        215
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.387711524963379,
      "reference_fraction_of_uniform": 0.19885142147541046,
      "rms_normalized_to_uniform_percent": 0.07794326354228491
    },
    "east": {
      "bias_percent": -4.5205223351525925,
      "rms_normalized_error_percent": 4.211019983316832,
      "absolute_error": {
        "p95": 0.00016007661743060446,
        "p99": 0.0011370241735130493,
        "maximum": 0.0021578408777713776
      },
      "worst_index": [
        1902
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0005860452074557543,
      "reference_fraction_of_uniform": 8.39770509628579e-05,
      "rms_normalized_to_uniform_percent": 0.0009894219364642012
    },
    "south": {
      "bias_percent": -0.02311465654614275,
      "rms_normalized_error_percent": 0.35303038295544414,
      "absolute_error": {
        "p95": 0.029152822494506833,
        "p99": 0.04429245233535765,
        "maximum": 0.07505691051483154
      },
      "worst_index": [
        1000
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3871086835861206,
      "reference_fraction_of_uniform": 0.19876503944396973,
      "rms_normalized_to_uniform_percent": 0.07240075538523848
    },
    "west": {
      "bias_percent": 0.02318768214029491,
      "rms_normalized_error_percent": 0.29572993552371396,
      "absolute_error": {
        "p95": 0.06375313997268676,
        "p99": 0.12447499752044676,
        "maximum": 0.21564650535583496
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.779559135437012,
      "reference_fraction_of_uniform": 0.6848844885826111,
      "rms_normalized_to_uniform_percent": 0.18285980763553147
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
          "nmbe_percent": -95.6951408754031,
          "cvrmse_percent": 1111.6985367810757,
          "absolute_error_percentiles_lux": {
            "p50": 4.098236240679398e-05,
            "p90": 0.0024642026983201504,
            "p95": 0.005394304729998103,
            "p99": 0.018516435809433462
          },
          "maximum_absolute_error_lux": 1.9872518531046808,
          "worst": {
            "sensor_index": 72,
            "position": [
              17.75,
              12.601876258850098,
              0.800000011920929
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 0.007229472044855356,
            "radiance_lux": 1.9944813251495361
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
            "mean_absolute_error_percentage_points": 0.0005701388435417209,
            "maximum_error_percentage_points": 0.014504226871367959,
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
          "nmbe_percent": -0.2907912925499883,
          "cvrmse_percent": 3.1888297430100363,
          "absolute_error_percentiles_lux": {
            "p50": 0.43267059326171875,
            "p90": 4.021477508544923,
            "p95": 7.24407958984375,
            "p99": 19.49591064453125
          },
          "maximum_absolute_error_lux": 204.70703125,
          "worst": {
            "sensor_index": 48,
            "position": [
              2.0449999570846558,
              5.3735432624816895,
              0.800000011920929
            ],
            "hour_of_year": 2727.5,
            "foton_lux": 16399.947265625,
            "radiance_lux": 16604.654296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09157505707762555,
            "maximum_error_percentage_points": 1.7527397260273982,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22570069887370467,
            "maximum_error_percentage_points": 1.5040198609817779,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.23455622146118715,
            "maximum_error_percentage_points": 3.9738356164383504,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2352106164383562,
            "maximum_error_percentage_points": 3.973835616438354,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0030164098173515804,
            "maximum_error_percentage_points": 0.22219178082191804,
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
          "nmbe_percent": -0.18797326246536944,
          "cvrmse_percent": 1.4592614983786116,
          "absolute_error_percentiles_lux": {
            "p50": 1.9854583740234375,
            "p90": 12.9423828125,
            "p95": 20.6953125,
            "p99": 47.397890624999945
          },
          "maximum_absolute_error_lux": 341.95703125,
          "worst": {
            "sensor_index": 44,
            "position": [
              1.149999976158142,
              14.135822296142578,
              0.800000011920929
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 21809.37109375,
            "radiance_lux": 22151.328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3691578051234425,
            "maximum_error_percentage_points": 2.4884931506849313,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2745909877292791,
            "maximum_error_percentage_points": 1.7358011871712904,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21072904573949383,
            "maximum_error_percentage_points": 1.9132876712328724,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.21878693599566598,
            "maximum_error_percentage_points": 1.9132876712328724,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015360266233263614,
            "maximum_error_percentage_points": 0.219726027397261,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 40.23484726586844,
          "radiance_percent": 40.357247280083136,
          "difference_percentage_points": 0.1224000142146977,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.0049970569349326865,
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
            "maximum_error_percentage_points": 0.0031715245687798277,
            "passed": true
          },
          {
            "identifier": "office_02",
            "maximum_error_percentage_points": 0.0049920696101775075,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.0049970569349326865,
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
        "maximum_error_percentage_points": 0.0049970569349326865,
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
              "maximum_error_percentage_points": 0.0031715245687798277,
              "passed": true
            },
            {
              "identifier": "office_02",
              "maximum_error_percentage_points": 0.0049920696101775075,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.0049970569349326865,
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
            "nmbe_percent": "inf",
            "cvrmse_percent": "inf",
            "absolute_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0005862140143290214,
              "maximum": 0.04340900480747223
            },
            "per_sensor_maximum_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.002267934493720452,
              "maximum": 0.04340900480747223
            },
            "worst": {
              "sensor_index": 171,
              "sun_up_hour_index": 2693,
              "hour_of_year": 4881.5,
              "foton_lux": 0.04340900480747223,
              "radiance_lux": 0.0
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
            "nmbe_percent": 15.990532706267055,
            "cvrmse_percent": 44.330191407247554,
            "absolute_error_lux": {
              "p50": 5.0873024463653564,
              "p90": 51.3841688156128,
              "p95": 90.4738546371458,
              "p99": 227.79713134765598,
              "maximum": 3201.609375
            },
            "per_sensor_maximum_error_lux": {
              "p50": 106.28953123092651,
              "p90": 647.5546264648439,
              "p95": 958.4089599609362,
              "p99": 1478.8490966796846,
              "maximum": 3201.609375
            },
            "worst": {
              "sensor_index": 5,
              "sun_up_hour_index": 1159,
              "hour_of_year": 2725.5,
              "foton_lux": 24287.009765625,
              "radiance_lux": 21085.400390625
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.9112604166666667,
              "maximum_error_percentage_points": 32.27,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.263010416666668,
              "maximum_error_percentage_points": 24.140000000000004,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.529104166666667,
              "maximum_error_percentage_points": 44.66,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.512666666666666,
              "maximum_error_percentage_points": 44.660000000000004,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.033333333333333326,
              "maximum_error_percentage_points": 1.3399999999999999,
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
            "nmbe_percent": 15.219217170452922,
            "cvrmse_percent": 26.61229177587038,
            "absolute_error_lux": {
              "p50": 58.96076965332031,
              "p90": 245.9012390136719,
              "p95": 372.77143554687495,
              "p99": 714.7874023437435,
              "maximum": 3254.44140625
            },
            "per_sensor_maximum_error_lux": {
              "p50": 715.238525390625,
              "p90": 1648.7391601562501,
              "p95": 1885.49296875,
              "p99": 2629.539375,
              "maximum": 3254.44140625
            },
            "worst": {
              "sensor_index": 777,
              "sun_up_hour_index": 2944,
              "hour_of_year": 5246.5,
              "foton_lux": 30278.068359375,
              "radiance_lux": 27023.626953125
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.744372881355932,
              "maximum_error_percentage_points": 38.57,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.496587570621468,
              "maximum_error_percentage_points": 32.43,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 12.970666666666668,
              "maximum_error_percentage_points": 52.56999999999999,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 12.940440677966103,
              "maximum_error_percentage_points": 52.57,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.3687344632768362,
              "maximum_error_percentage_points": 2.77,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 40.23484726586844,
            "radiance_percent": 31.90815316097717,
            "difference_percentage_points": 8.326694104891267,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 1.6496933329617605,
        "radiance_seconds": 21.85582529194653,
        "speedup": 13.248417057434482,
        "passed": true
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf1/stock/annual_daylight"
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
      "study_preparation_seconds": 0.12003112502861768,
      "weather_seconds": 0.11613283306360245,
      "metric_reduction_seconds": 1.2680489160120487,
      "write_seconds": 0.14523270807694644,
      "total_seconds": 1.5296622079331428,
      "cold_end_to_end_seconds": 1.6496933329617605,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.09615941706579179,
      "engine_upload_seconds": 0.000501208,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.1891200414393097,
      "engine_annual_reduction_seconds": 0.014917250024154782,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 1.1891200414393097
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.12003112502861768,
      "weather_seconds": 0.09644379105884582,
      "metric_reduction_seconds": 0.07518250006251037,
      "write_seconds": 0.1231827080482617,
      "total_seconds": 0.29575449996627867,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.29575449996627867,
      "raw_export_seconds": 0.09429112507496029,
      "engine_upload_seconds": 0.000247,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.016051791608333588,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.04484624997712672,
      "full": 1.1866602919762954
    }
  },
  "elapsed_seconds": 2491.7666462920606,
  "result_class": "passed"
}
```
