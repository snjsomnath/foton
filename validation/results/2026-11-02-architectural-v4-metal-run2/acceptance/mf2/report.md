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
          "maximum": 2.5918141091096913e-06
        },
        "worst_index": [
          95,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.03826460368829146,
        "rms_normalized_error_percent": 1.5780904795142972,
        "absolute_error": {
          "p95": 4.3828360503539335e-06,
          "p99": 3.6862047199974696e-05,
          "maximum": 0.0010252110660076141
        },
        "worst_index": [
          5,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.027805600634392757,
        "rms_normalized_error_percent": 1.0224170637300716,
        "absolute_error": {
          "p95": 3.382598515599966e-05,
          "p99": 0.00011711812112480402,
          "maximum": 0.0017795264720916748
        },
        "worst_index": [
          72,
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
          "maximum": 2.5918141091096913e-06
        },
        "worst_index": [
          95,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": -0.036322401688117595,
        "rms_normalized_error_percent": 1.3223235853252882,
        "absolute_error": {
          "p95": 3.782318890443984e-06,
          "p99": 3.082300128880787e-05,
          "maximum": 0.0010313093662261963
        },
        "worst_index": [
          67,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.011533686188374586,
        "rms_normalized_error_percent": 0.8515528821623587,
        "absolute_error": {
          "p95": 2.7708651032298803e-05,
          "p99": 9.490223601460457e-05,
          "maximum": 0.0013369694352149963
        },
        "worst_index": [
          177,
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.00011851488307002,
                "candidate_energy": 5.925744153501e-05,
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
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 35,
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
                "nmbe_percent": -0.21772068712692202,
                "cvrmse_percent": 100.20561235228618,
                "rms_normalized_rmse_percent": 8.711792210509808,
                "reference_energy": 33.14200595820364,
                "candidate_energy": 33.069848955103794,
                "relative_energy_error_percent": 0.21772068712692202,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.055305551650232e-05,
                  "maximum": 0.0008140191785059869
                },
                "worst": {
                  "global_sensor_index": 254,
                  "local_sensor_index": 79,
                  "sky_patch_index": 113,
                  "rgb_channel": 0,
                  "reference": 0.0012913750251755118,
                  "candidate": 0.0004773558466695249
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5367117875399972,
                "cvrmse_percent": 273.2256267264121,
                "rms_normalized_rmse_percent": 5.467515684493467,
                "reference_energy": 19.45008019529996,
                "candidate_energy": 19.55447106839412,
                "relative_energy_error_percent": 0.5367117875399972,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010276628760038745,
                  "maximum": 0.002080533653497696
                },
                "worst": {
                  "global_sensor_index": 206,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05548069067299366,
                  "candidate": 0.057561224326491356
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
                "nmbe_percent": -0.07156793433658463,
                "cvrmse_percent": 43.250361890855146,
                "rms_normalized_rmse_percent": 8.795698521506782,
                "reference_energy": 166.60713401916604,
                "candidate_energy": 166.48789673489114,
                "relative_energy_error_percent": 0.07156793433658463,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.21200306341052e-05,
                  "p99": 0.0002508545803721063,
                  "maximum": 0.0008952990174293518
                },
                "worst": {
                  "global_sensor_index": 1273,
                  "local_sensor_index": 138,
                  "sky_patch_index": 224,
                  "rgb_channel": 0,
                  "reference": 0.003035554545931518,
                  "candidate": 0.0021402555285021663
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.10225482301242528,
                "cvrmse_percent": 105.98617935161924,
                "rms_normalized_rmse_percent": 3.3658102569956143,
                "reference_energy": 105.17105914951816,
                "candidate_energy": 105.27860162991178,
                "relative_energy_error_percent": 0.10225482301241177,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.1659274100096847e-07,
                  "p95": 0.00010058250700240023,
                  "p99": 0.0003753939126909245,
                  "maximum": 0.002811998128890991
                },
                "worst": {
                  "global_sensor_index": 1252,
                  "local_sensor_index": 117,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11416564881801605,
                  "candidate": 0.11135365068912506
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1722.030458971858,
            "full": 8166.45266697742
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1686.7942499229684,
            "full": 8172.121417010203
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1712.800082983449,
            "full": 8394.302667002194
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1688.2762500317767,
            "full": 8294.375624973327
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
                "reference_energy": 7.526948535385714e-05,
                "candidate_energy": 0.00017242228647518232,
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
                  "global_sensor_index": 95,
                  "local_sensor_index": 95,
                  "sky_patch_index": 37,
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
                "nmbe_percent": -0.12930929323017623,
                "cvrmse_percent": 60.46609705998622,
                "rms_normalized_rmse_percent": 5.263227297476107,
                "reference_energy": 33.117484151764444,
                "candidate_energy": 33.07466016707218,
                "relative_energy_error_percent": 0.12930929323017623,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7586597502231355e-05,
                  "maximum": 0.00044873886508867145
                },
                "worst": {
                  "global_sensor_index": 307,
                  "local_sensor_index": 132,
                  "sky_patch_index": 168,
                  "rgb_channel": 0,
                  "reference": 0.0005233859410509467,
                  "candidate": 0.0009721248061396182
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2782929061311347,
                "cvrmse_percent": 106.74644866953129,
                "rms_normalized_rmse_percent": 2.804718056745771,
                "reference_energy": 31.06425256339376,
                "candidate_energy": 31.150702174620346,
                "relative_energy_error_percent": 0.2782929061311347,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.662127172925468e-06,
                  "p95": 6.247052317576106e-06,
                  "p99": 7.107112342055115e-05,
                  "maximum": 0.0013509150594472885
                },
                "worst": {
                  "global_sensor_index": 231,
                  "local_sensor_index": 56,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.052315350621938705,
                  "candidate": 0.053666265681385994
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
                "nmbe_percent": 0.029653562037510985,
                "cvrmse_percent": 26.15355829763779,
                "rms_normalized_rmse_percent": 5.319680459584531,
                "reference_energy": 166.47705677860154,
                "candidate_energy": 166.5264231559116,
                "relative_energy_error_percent": 0.029653562037510982,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.740970325656235e-05,
                  "p99": 0.00015016307588666677,
                  "maximum": 0.0005104254232719541
                },
                "worst": {
                  "global_sensor_index": 1220,
                  "local_sensor_index": 85,
                  "sky_patch_index": 324,
                  "rgb_channel": 0,
                  "reference": 0.003860222059302032,
                  "candidate": 0.004370647482573986
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.048139552349901846,
                "cvrmse_percent": 45.24991219024638,
                "rms_normalized_rmse_percent": 1.8327548756011087,
                "reference_energy": 155.77127263323138,
                "candidate_energy": 155.69628503989583,
                "relative_energy_error_percent": 0.04813955235000904,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.105427357601002e-15,
                  "p90": 1.2331782545516037e-05,
                  "p95": 6.630434654653072e-05,
                  "p99": 0.00022923655342310667,
                  "maximum": 0.0021313540637493134
                },
                "worst": {
                  "global_sensor_index": 1176,
                  "local_sensor_index": 41,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11848484724760056,
                  "candidate": 0.12061620131134987
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3265.44049999211,
            "full": 122689.3244999228
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3156.8526659393683,
            "full": 121244.4901659619
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3196.1617909837514,
            "full": 122617.5906250719
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3177.698750048876,
            "full": 122501.49329192936
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
                "reference_energy": 0.00010325299973956703,
                "candidate_energy": 0.00015534098049485578,
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
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
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
                "nmbe_percent": -0.022088871968579653,
                "cvrmse_percent": 59.764631944803206,
                "rms_normalized_rmse_percent": 5.198184386879306,
                "reference_energy": 33.09300661304724,
                "candidate_energy": 33.08569674118593,
                "relative_energy_error_percent": 0.022088871968579653,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.725437262094939e-05,
                  "maximum": 0.0004464819794520736
                },
                "worst": {
                  "global_sensor_index": 205,
                  "local_sensor_index": 30,
                  "sky_patch_index": 282,
                  "rgb_channel": 0,
                  "reference": 0.0033314955653622746,
                  "candidate": 0.0037779775448143482
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.018738002582093762,
                "cvrmse_percent": 103.81745281061077,
                "rms_normalized_rmse_percent": 2.730901824165924,
                "reference_energy": 31.135847984968336,
                "candidate_energy": 31.141682220967716,
                "relative_energy_error_percent": 0.018738002582093762,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6395952460234522e-06,
                  "p95": 6.183912074675386e-06,
                  "p99": 6.817428715293223e-05,
                  "maximum": 0.0013071149587631226
                },
                "worst": {
                  "global_sensor_index": 230,
                  "local_sensor_index": 55,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05054784007370472,
                  "candidate": 0.0492407251149416
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
                "nmbe_percent": 0.0205226178136893,
                "cvrmse_percent": 26.14474313640799,
                "rms_normalized_rmse_percent": 5.319224028186482,
                "reference_energy": 166.4939904670225,
                "candidate_energy": 166.52815939236882,
                "relative_energy_error_percent": 0.020522617813689303,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.722824814962223e-05,
                  "p99": 0.00015017019904917106,
                  "maximum": 0.0005018244046368636
                },
                "worst": {
                  "global_sensor_index": 1686,
                  "local_sensor_index": 551,
                  "sky_patch_index": 106,
                  "rgb_channel": 0,
                  "reference": 0.00017566975293448195,
                  "candidate": 0.0006774941575713456
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.013747033544705061,
                "cvrmse_percent": 45.71258204142864,
                "rms_normalized_rmse_percent": 1.8509937183521663,
                "reference_energy": 155.82475395790377,
                "candidate_energy": 155.80333267670608,
                "relative_energy_error_percent": 0.013747033544796259,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.105427357601002e-15,
                  "p90": 1.2425246859493236e-05,
                  "p95": 6.532063707709312e-05,
                  "p99": 0.00022795010590925813,
                  "maximum": 0.002779301255941391
                },
                "worst": {
                  "global_sensor_index": 1240,
                  "local_sensor_index": 105,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11509659886360168,
                  "candidate": 0.11787590011954308
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3186.241167015396,
            "full": 128128.02891700994
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3218.130457913503,
            "full": 127955.60304110404
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3166.0297500202432,
            "full": 128307.37908300944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3236.4782919175923,
            "full": 126758.9131250279
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
                "reference_energy": 0.00019985990781279384,
                "candidate_energy": 0.00015692745042628076,
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
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
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
                "nmbe_percent": -0.039270749831766164,
                "cvrmse_percent": 34.50359867771488,
                "rms_normalized_rmse_percent": 3.0036077961683465,
                "reference_energy": 33.09465848347929,
                "candidate_energy": 33.08166196293857,
                "relative_energy_error_percent": 0.03927074983176617,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.4919994466472383e-05,
                  "maximum": 0.0002703149802982807
                },
                "worst": {
                  "global_sensor_index": 275,
                  "local_sensor_index": 100,
                  "sky_patch_index": 162,
                  "rgb_channel": 0,
                  "reference": 0.0017197364941239357,
                  "candidate": 0.0019900514744222164
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.014444076261957118,
                "cvrmse_percent": 64.88446991192893,
                "rms_normalized_rmse_percent": 1.7075787849915145,
                "reference_energy": 31.114380298690936,
                "candidate_energy": 31.118874483509714,
                "relative_energy_error_percent": 0.014444076261957118,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8815939483829474e-06,
                  "p95": 4.395600808493327e-06,
                  "p99": 4.205448982247609e-05,
                  "maximum": 0.001004265621304512
                },
                "worst": {
                  "global_sensor_index": 192,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06106347031891346,
                  "candidate": 0.06005920469760895
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
                "nmbe_percent": 0.012139874129536286,
                "cvrmse_percent": 14.566623156094067,
                "rms_normalized_rmse_percent": 2.9647085727423037,
                "reference_energy": 166.48261972632116,
                "candidate_energy": 166.5028305068035,
                "relative_energy_error_percent": 0.012139874129536286,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.457795199006796e-05,
                  "p99": 8.609658107161522e-05,
                  "maximum": 0.0002593420213088393
                },
                "worst": {
                  "global_sensor_index": 1380,
                  "local_sensor_index": 245,
                  "sky_patch_index": 169,
                  "rgb_channel": 0,
                  "reference": 0.0017446244601160288,
                  "candidate": 0.002003966481424868
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.029660982809507335,
                "cvrmse_percent": 27.505851888376988,
                "rms_normalized_rmse_percent": 1.1139490083478691,
                "reference_energy": 155.81832601975145,
                "candidate_energy": 155.77210877285663,
                "relative_energy_error_percent": 0.029660982809536975,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.601069930591634e-06,
                  "p95": 3.726967770489864e-05,
                  "p99": 0.000127916551718954,
                  "maximum": 0.001548953354358673
                },
                "worst": {
                  "global_sensor_index": 1216,
                  "local_sensor_index": 81,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.13485950231552124,
                  "candidate": 0.1364084556698799
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6128.479874925688,
            "full": 227591.04283410124
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6174.906291998923,
            "full": 225865.71087501943
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6198.511959053576,
            "full": 226750.9924590122
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 6110.914541990496,
            "full": 226216.0897499416
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 346478.1859581126,
      "worker_pool_size": 12,
      "invocation_count": 127
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1438824.749915977,
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
            "reference_energy": 0.0001783936791195373,
            "candidate_energy": 6.360000043947878e-06,
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
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                13.75,
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
            "reference_energy": 0.0001783936791195373,
            "candidate_energy": 6.360000043947878e-06,
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
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 3.922627456631744e-06,
              "candidate": 0.0,
              "position": [
                13.75,
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
            "nmbe_percent": -1.8639650504741563,
            "cvrmse_percent": 88.27904259944816,
            "rms_normalized_rmse_percent": 2.3237591657022905,
            "reference_energy": 31.125655589909194,
            "candidate_energy": 30.545484247982362,
            "relative_energy_error_percent": 1.863965050474056,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.4262922920570425e-06,
              "p95": 5.226919415690619e-06,
              "p99": 2.091131618726631e-05,
              "maximum": 0.0017571598291397095
            },
            "worst": {
              "global_sensor_index": 221,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05512791872024536,
              "candidate": 0.05337075889110565,
              "position": [
                2.0449999570846558,
                4.328545093536377,
                0.800000011920929
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9530067363025337,
            "cvrmse_percent": 42.73042058999117,
            "rms_normalized_rmse_percent": 2.320168758975332,
            "reference_energy": 64.20478759005698,
            "candidate_energy": 63.592911639295025,
            "relative_energy_error_percent": 0.9530067363025019,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.4257021664198064e-06,
              "p95": 5.210392055232634e-06,
              "p99": 2.0544803555821782e-05,
              "maximum": 0.0017571598291397095
            },
            "worst": {
              "global_sensor_index": 221,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05512791872024536,
              "candidate": 0.05337075889110565,
              "position": [
                2.0449999570846558,
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
            "nmbe_percent": -1.6711777850191114,
            "cvrmse_percent": 60.225733722751684,
            "rms_normalized_rmse_percent": 2.439828656972696,
            "reference_energy": 155.8738493524038,
            "candidate_energy": 153.26892020937225,
            "relative_energy_error_percent": 1.6711777850191194,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4761362737990567e-08,
              "p90": 8.447453001281281e-06,
              "p95": 1.7888902220875025e-05,
              "p99": 5.3653959184885025e-05,
              "maximum": 0.004062719643115997
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1207205206155777,
              "candidate": 0.1166578009724617,
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
            "nmbe_percent": -0.8051388183577689,
            "cvrmse_percent": 29.117082640033964,
            "rms_normalized_rmse_percent": 2.4389106181889977,
            "reference_energy": 322.28794229428024,
            "candidate_energy": 319.6930769639826,
            "relative_energy_error_percent": 0.8051388183577382,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.473132099112263e-08,
              "p90": 8.395108125114348e-06,
              "p95": 1.7568469047546387e-05,
              "p99": 5.301600322127342e-05,
              "maximum": 0.004062719643115997
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1207205206155777,
              "candidate": 0.1166578009724617,
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
            "reference_energy": 8.8886162302515e-05,
            "candidate_energy": 6.360000043947878e-06,
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
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 35,
              "rgb_channel": 0,
              "reference": 4.9381201279175e-06,
              "candidate": 0.0,
              "position": [
                13.75,
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
            "reference_energy": 8.8886162302515e-05,
            "candidate_energy": 6.360000043947878e-06,
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
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 35,
              "rgb_channel": 0,
              "reference": 4.9381201279175e-06,
              "candidate": 0.0,
              "position": [
                13.75,
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
            "nmbe_percent": 56.4103284601411,
            "cvrmse_percent": 1147.083154137604,
            "rms_normalized_rmse_percent": 23.041791760799494,
            "reference_energy": 19.529071096968135,
            "candidate_energy": 30.545484247982362,
            "relative_energy_error_percent": 56.41032846014121,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.251445476366167e-06,
              "p95": 2.3496054916449494e-05,
              "p99": 6.49809284004729e-05,
              "maximum": 0.010464807972311974
            },
            "worst": {
              "global_sensor_index": 962,
              "local_sensor_index": 787,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015412602573633194,
              "candidate": 0.025877410545945168,
              "position": [
                0.6324999928474426,
                0.2049015462398529,
                0.800000011920929
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.880219995161347,
            "cvrmse_percent": 425.7978544250712,
            "rms_normalized_rmse_percent": 23.040754467403445,
            "reference_energy": 52.60820309711593,
            "candidate_energy": 63.592911639295025,
            "relative_energy_error_percent": 20.880219995161347,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.24011884819731e-06,
              "p95": 2.3470000087399967e-05,
              "p99": 6.415577496227111e-05,
              "maximum": 0.010464807972311974
            },
            "worst": {
              "global_sensor_index": 962,
              "local_sensor_index": 787,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015412602573633194,
              "candidate": 0.025877410545945168,
              "position": [
                0.6324999928474426,
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
            "nmbe_percent": 45.47405281912467,
            "cvrmse_percent": 542.0887710515492,
            "rms_normalized_rmse_percent": 17.242697757683672,
            "reference_energy": 105.35825271874391,
            "candidate_energy": 153.26892020937225,
            "relative_energy_error_percent": 45.47405281912455,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.6799999583745375e-05,
              "p95": 9.839999984251335e-05,
              "p99": 0.0002242429181933403,
              "maximum": 0.015492584556341171
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022325146943330765,
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
            "nmbe_percent": 17.63267384210017,
            "cvrmse_percent": 210.1524312545412,
            "rms_normalized_rmse_percent": 17.242725971011645,
            "reference_energy": 271.77234566062026,
            "candidate_energy": 319.6930769639826,
            "relative_energy_error_percent": 17.632673842100207,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.678592569893268e-05,
              "p95": 9.83299978543073e-05,
              "p99": 0.000224351417273283,
              "maximum": 0.015492584556341171
            },
            "worst": {
              "global_sensor_index": 1924,
              "local_sensor_index": 789,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022325146943330765,
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
      "bias_percent": 0.03891347795789197,
      "rms_normalized_error_percent": 0.17529378646924668,
      "absolute_error": {
        "p95": 0.06197241916563402,
        "p99": 0.12352553944681013,
        "maximum": 0.17342435305443393
      },
      "worst_index": [
        1963
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.978845010884814,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17529378646924668
    },
    "overcast": {
      "bias_percent": 0.039040278029219666,
      "rms_normalized_error_percent": 0.11550407364990282,
      "absolute_error": {
        "p95": 0.03249495029449461,
        "p99": 0.05168519973754882,
        "maximum": 0.06753647327423096
      },
      "worst_index": [
        1963
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.3863139152526855,
      "reference_fraction_of_uniform": 0.6285157203674316,
      "rms_normalized_to_uniform_percent": 0.08297128151181488
    },
    "horizon": {
      "bias_percent": 0.10474749645007339,
      "rms_normalized_error_percent": 1.895267974488771,
      "absolute_error": {
        "p95": 0.04864323696081025,
        "p99": 0.12133295887314174,
        "maximum": 0.18632690045608236
      },
      "worst_index": [
        1996
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0321958721654567,
      "reference_fraction_of_uniform": 0.14790353855911031,
      "rms_normalized_to_uniform_percent": 0.15116953499242372
    },
    "north": {
      "bias_percent": -0.07014912831111607,
      "rms_normalized_error_percent": 0.2518793677812267,
      "absolute_error": {
        "p95": 0.019846373796463007,
        "p99": 0.03311374008655542,
        "maximum": 0.05305981636047363
      },
      "worst_index": [
        1894
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3587977886199951,
      "reference_fraction_of_uniform": 0.1947023868560791,
      "rms_normalized_to_uniform_percent": 0.05083968886014456
    },
    "east": {
      "bias_percent": -55.99868484577049,
      "rms_normalized_error_percent": 77.69180652803198,
      "absolute_error": {
        "p95": 3.052891601384999e-05,
        "p99": 0.00016387801777455015,
        "maximum": 0.0005663235769191033
      },
      "worst_index": [
        1002
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.212145434692502e-05,
      "reference_fraction_of_uniform": 1.7368854514643317e-06,
      "rms_normalized_to_uniform_percent": 0.0002063181815259638
    },
    "south": {
      "bias_percent": 0.04749191903409211,
      "rms_normalized_error_percent": 0.2483369402382109,
      "absolute_error": {
        "p95": 0.020403581857681274,
        "p99": 0.03272572517395013,
        "maximum": 0.06595635414123535
      },
      "worst_index": [
        1917
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3784343004226685,
      "reference_fraction_of_uniform": 0.19751609861850739,
      "rms_normalized_to_uniform_percent": 0.050614511909288645
    },
    "west": {
      "bias_percent": 0.05144010777827212,
      "rms_normalized_error_percent": 0.24148364345967585,
      "absolute_error": {
        "p95": 0.047261410951614374,
        "p99": 0.12084239959716787,
        "maximum": 0.167128324508667
      },
      "worst_index": [
        1971
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.809671878814697,
      "reference_fraction_of_uniform": 0.6891787648200989,
      "rms_normalized_to_uniform_percent": 0.15052070301685333
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
          "nmbe_percent": -99.01151138363345,
          "cvrmse_percent": 1802.7167044612652,
          "absolute_error_percentiles_lux": {
            "p50": 5.1825729315169156e-05,
            "p90": 0.0028017220553010697,
            "p95": 0.006630875449627631,
            "p99": 0.026832437925040722
          },
          "maximum_absolute_error_lux": 5.3711161613464355,
          "worst": {
            "sensor_index": 79,
            "position": [
              18.25,
              12.601876258850098,
              0.800000011920929
            ],
            "hour_of_year": 4453.5,
            "foton_lux": 0.0,
            "radiance_lux": 5.3711161613464355
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
            "mean_absolute_error_percentage_points": 0.0009646167722476091,
            "maximum_error_percentage_points": 0.024973489020642264,
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
          "nmbe_percent": -0.2973989381337246,
          "cvrmse_percent": 3.930196259663746,
          "absolute_error_percentiles_lux": {
            "p50": 0.33798646926879883,
            "p90": 3.1956523895263675,
            "p95": 6.0393985748291,
            "p99": 19.877747497558573
          },
          "maximum_absolute_error_lux": 305.39453125,
          "worst": {
            "sensor_index": 8,
            "position": [
              0.5149999856948853,
              4.851044178009033,
              0.800000011920929
            ],
            "hour_of_year": 5245.5,
            "foton_lux": 24405.20703125,
            "radiance_lux": 24710.6015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07523886986301369,
            "maximum_error_percentage_points": 1.810410958904109,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1651157761655636,
            "maximum_error_percentage_points": 1.2134022726397156,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.16723787100456605,
            "maximum_error_percentage_points": 2.629178082191771,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16804737442922374,
            "maximum_error_percentage_points": 2.629178082191782,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.002385131278538821,
            "maximum_error_percentage_points": 0.1052054794520565,
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
          "nmbe_percent": -0.14353170862973325,
          "cvrmse_percent": 1.714990227701881,
          "absolute_error_percentiles_lux": {
            "p50": 1.8272857666015625,
            "p90": 12.228857421875006,
            "p95": 20.754785156249994,
            "p99": 58.150332031249945
          },
          "maximum_absolute_error_lux": 464.708984375,
          "worst": {
            "sensor_index": 91,
            "position": [
              1.659999966621399,
              21.6956205368042,
              0.800000011920929
            ],
            "hour_of_year": 3951.5,
            "foton_lux": 17923.908203125,
            "radiance_lux": 18388.6171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.34523690116864036,
            "maximum_error_percentage_points": 1.866575342465751,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2557766804013342,
            "maximum_error_percentage_points": 1.5767593226313323,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1861112916956894,
            "maximum_error_percentage_points": 1.2557534246575344,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.19550979026391171,
            "maximum_error_percentage_points": 1.2557534246575344,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015484714805355586,
            "maximum_error_percentage_points": 0.2191780821917817,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 39.90924740146641,
          "radiance_percent": 40.479647294297834,
          "difference_percentage_points": 0.5703998928314249,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 5,
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
            "nmbe_percent": "inf",
            "cvrmse_percent": "inf",
            "absolute_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0008219292352441719,
              "maximum": 0.11132843792438507
            },
            "per_sensor_maximum_error_lux": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.00650341664440924,
              "maximum": 0.11132843792438507
            },
            "worst": {
              "sensor_index": 124,
              "sun_up_hour_index": 1162,
              "hour_of_year": 2728.5,
              "foton_lux": 0.11132843792438507,
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
            "nmbe_percent": 17.534485091399937,
            "cvrmse_percent": 138.5004326995931,
            "absolute_error_lux": {
              "p50": 5.225525975227356,
              "p90": 51.0090759277344,
              "p95": 93.92219238281247,
              "p99": 324.3112487792921,
              "maximum": 11926.212890625
            },
            "per_sensor_maximum_error_lux": {
              "p50": 134.61079788208008,
              "p90": 2368.1443603515627,
              "p95": 4267.586547851555,
              "p99": 8478.719248046871,
              "maximum": 11926.212890625
            },
            "worst": {
              "sensor_index": 796,
              "sun_up_hour_index": 2389,
              "hour_of_year": 4454.5,
              "foton_lux": 32092.69921875,
              "radiance_lux": 20166.486328125
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.820791666666667,
              "maximum_error_percentage_points": 31.84,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.13096875,
              "maximum_error_percentage_points": 23.02,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.314718749999999,
              "maximum_error_percentage_points": 42.580000000000005,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.324822916666666,
              "maximum_error_percentage_points": 42.58,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.07163541666666665,
              "maximum_error_percentage_points": 2.6799999999999997,
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
            "nmbe_percent": 16.003935234973742,
            "cvrmse_percent": 51.53385037748919,
            "absolute_error_lux": {
              "p50": 58.79296875,
              "p90": 256.98593750000003,
              "p95": 438.7476684570311,
              "p99": 1568.7557910156231,
              "maximum": 11251.33203125
            },
            "per_sensor_maximum_error_lux": {
              "p50": 1153.6010131835938,
              "p90": 6008.143359375,
              "p95": 7326.521679687498,
              "p99": 8265.840390624995,
              "maximum": 11251.33203125
            },
            "worst": {
              "sensor_index": 740,
              "sun_up_hour_index": 2012,
              "hour_of_year": 3951.5,
              "foton_lux": 26039.201171875,
              "radiance_lux": 14787.869140625
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.347853107344632,
              "maximum_error_percentage_points": 38.16,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.408474576271187,
              "maximum_error_percentage_points": 34.620000000000005,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 12.975830508474576,
              "maximum_error_percentage_points": 55.64,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 12.935988700564971,
              "maximum_error_percentage_points": 55.64,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.24585310734463273,
              "maximum_error_percentage_points": 2.69,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 39.90924740146641,
            "radiance_percent": 31.66335347315484,
            "difference_percentage_points": 8.24589392831157,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 5.353294709115289,
        "radiance_seconds": 21.334799082949758,
        "speedup": 3.9853585954500246,
        "passed": false
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/acceptance/mf2/stock/annual_daylight"
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
      "study_preparation_seconds": 0.07812925009056926,
      "weather_seconds": 0.14696629205718637,
      "metric_reduction_seconds": 4.990618083043955,
      "write_seconds": 0.13663424993865192,
      "total_seconds": 5.27516545902472,
      "cold_end_to_end_seconds": 5.353294709115289,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.09650237497407943,
      "engine_upload_seconds": 0.001506625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.72332787537016,
      "engine_annual_reduction_seconds": 0.068761958158575,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 4.72332787537016
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.07812925009056926,
      "weather_seconds": 0.11563249991741031,
      "metric_reduction_seconds": 0.23979983397293836,
      "write_seconds": 0.12344608292914927,
      "total_seconds": 0.47909158293623477,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.47909158293623477,
      "raw_export_seconds": 0.08775370789226145,
      "engine_upload_seconds": 0.000844083,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.06934491673018783,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.153889250010252,
      "full": 4.742104165954515
    }
  },
  "elapsed_seconds": 3845.9632461250294,
  "result_class": "passed"
}
```
