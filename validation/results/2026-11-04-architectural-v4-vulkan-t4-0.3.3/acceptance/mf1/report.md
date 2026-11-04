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
  "model_sha256": "1ae8ae230d2e63d6fe806655e2e9d36c042cb560710914d49f6e3b2c61fffbbd",
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
      "scene_fingerprint": 13596737419153064380,
      "basis": "Tregenza",
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
      "scene_fingerprint": 13596737419153064380,
      "basis": "Tregenza",
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
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
          "maximum": 0.0005996385589241982,
          "p95": 0.0,
          "p99": 2.764817327260971e-05
        },
        "bias_percent": -0.19400505681663066,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 1.3833554241804136,
        "worst_index": [
          27,
          105,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.000701497308909893,
          "p95": 1.4964491128921509e-05,
          "p99": 0.00010448688408359885
        },
        "bias_percent": -0.11164251042865557,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 1.2067994657041696,
        "worst_index": [
          7,
          120,
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
          "maximum": 2.4543692234146874e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0,
        "identifier": "classroom_01",
        "passed": true,
        "rms_normalized_error_percent": 0.0,
        "worst_index": [
          24,
          60,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0009092241525650024,
          "p95": 1.0928690608125163e-05,
          "p99": 7.69327743910253e-05
        },
        "bias_percent": 0.03850638155714472,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 1.155421509035522,
        "worst_index": [
          19,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0018055140972137451,
          "p95": 5.883490666747093e-05,
          "p99": 0.00017355475574731827
        },
        "bias_percent": 0.034330123977876485,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 0.7907453259226115,
        "worst_index": [
          114,
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
          "maximum": 2.4543692234146874e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0,
        "identifier": "classroom_01",
        "passed": true,
        "rms_normalized_error_percent": 0.0,
        "worst_index": [
          24,
          60,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0007454603910446167,
          "p95": 9.482794121140596e-06,
          "p99": 6.361515261232853e-05
        },
        "bias_percent": 0.0197023215965148,
        "identifier": "office_02",
        "passed": true,
        "rms_normalized_error_percent": 0.9566435434357288,
        "worst_index": [
          19,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0013432279229164124,
          "p95": 4.974263720214367e-05,
          "p99": 0.00014143437147140503
        },
        "bias_percent": -0.00236836719489025,
        "identifier": "office_01",
        "passed": true,
        "rms_normalized_error_percent": 0.6675692575370138,
        "worst_index": [
          91,
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
          "rms_normalized_rmse_percent": 5.0
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
                  "maximum": 0.0,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.0,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
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
                  "maximum": 0.0009446544572710991,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014348397962749004
                },
                "candidate_energy": 33.08232061223691,
                "cvrmse_percent": 40.22018913557876,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.029197165541557456,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.0919825331581,
                "relative_energy_error_percent": 0.029197165541557452,
                "rms_normalized_rmse_percent": 3.690825042537583,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.016882674768567085,
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "reference": 0.015938020311295986,
                  "rgb_channel": 0,
                  "sky_patch_index": 104
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016413666307926178,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.277509532992552e-06,
                  "p99": 0.00023285688075702637
                },
                "candidate_energy": 19.543676305124137,
                "cvrmse_percent": 110.30488442037097,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.021761539348293214,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.539424225632846,
                "relative_energy_error_percent": 0.02176153934829321,
                "rms_normalized_rmse_percent": 3.7277101652323386,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03713349997997284,
                  "global_sensor_index": 235,
                  "local_sensor_index": 60,
                  "reference": 0.03877486661076546,
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
                  "maximum": 0.0011461656540632248,
                  "p50": 0.0,
                  "p90": 1.6218982636929372e-07,
                  "p95": 0.000126861847093096,
                  "p99": 0.0003531679976731539
                },
                "candidate_energy": 166.51312492160378,
                "cvrmse_percent": 16.01727252623777,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.021986345203116906,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.54974312306172,
                "relative_energy_error_percent": 0.02198634520311691,
                "rms_normalized_rmse_percent": 3.401286359399763,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01637390535324812,
                  "global_sensor_index": 1170,
                  "local_sensor_index": 35,
                  "reference": 0.015227739699184895,
                  "rgb_channel": 0,
                  "sky_patch_index": 105
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.003412313759326935,
                  "p50": 0.0,
                  "p90": 2.4832591179803003e-05,
                  "p95": 0.00020029814913868904,
                  "p99": 0.0005781614454463124
                },
                "candidate_energy": 105.24128924452144,
                "cvrmse_percent": 42.6499638511031,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.01892729006479248,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 105.221373689913,
                "relative_energy_error_percent": 0.018927290064789104,
                "rms_normalized_rmse_percent": 2.5020215200367564,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0644819550216198,
                  "global_sensor_index": 1290,
                  "local_sensor_index": 155,
                  "reference": 0.06789426878094673,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1589.4578750012442,
            "full": 8217.167624970898
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1610.6730001047254,
            "full": 8388.329999987036
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1635.9038749942556,
            "full": 8524.363082950003
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 1632.4872080003843,
            "full": 8360.782625037245
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
          "rms_normalized_rmse_percent": 5.0
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
                "candidate_energy": 0.00025400221628402164,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.00013437285397444043,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 4.908738446829375e-06,
                  "global_sensor_index": 54,
                  "local_sensor_index": 54,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 10
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
                  "maximum": 0.0005358699709177017,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.527409616159275e-05
                },
                "candidate_energy": 33.074969659525095,
                "cvrmse_percent": 21.773512371639896,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0033717690964674947,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.07385448552054,
                "relative_energy_error_percent": 0.0033717690964674943,
                "rms_normalized_rmse_percent": 1.996528944902432,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014166180044412613,
                  "global_sensor_index": 217,
                  "local_sensor_index": 42,
                  "reference": 0.014702050015330315,
                  "rgb_channel": 0,
                  "sky_patch_index": 80
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011258460581302643,
                  "p50": 5.385444978855958e-09,
                  "p90": 6.378861871780844e-06,
                  "p95": 1.5924135186651236e-05,
                  "p99": 0.00013906889944337308
                },
                "candidate_energy": 31.10228630714866,
                "cvrmse_percent": 41.62966690519281,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03174555611153855,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.11216303632287,
                "relative_energy_error_percent": 0.03174555611153854,
                "rms_normalized_rmse_percent": 1.927584919287684,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0467141754925251,
                  "global_sensor_index": 245,
                  "local_sensor_index": 70,
                  "reference": 0.045588329434394836,
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
                  "maximum": 0.0006823497824370861,
                  "p50": 0.0,
                  "p90": 1.5440782590303862e-07,
                  "p95": 7.203296991065145e-05,
                  "p99": 0.00019785587210208178
                },
                "candidate_energy": 166.55543803669866,
                "cvrmse_percent": 8.729019233551764,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.029753388162705008,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.50589689088292,
                "relative_energy_error_percent": 0.029753388162705008,
                "rms_normalized_rmse_percent": 1.8541845591488153,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014994164928793907,
                  "global_sensor_index": 1178,
                  "local_sensor_index": 43,
                  "reference": 0.014311815146356821,
                  "rgb_channel": 0,
                  "sky_patch_index": 80
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.002160448580980301,
                  "p50": 1.9587960586875397e-07,
                  "p90": 3.099304885836346e-05,
                  "p95": 0.00011709675891324878,
                  "p99": 0.0003306940197944641
                },
                "candidate_energy": 155.64387923827456,
                "cvrmse_percent": 17.52897422435359,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.041672701591036324,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.70876728821773,
                "relative_energy_error_percent": 0.041672701591077395,
                "rms_normalized_rmse_percent": 1.3287158324779607,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.11781574785709381,
                  "global_sensor_index": 1275,
                  "local_sensor_index": 140,
                  "reference": 0.11565529927611351,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3132.942207972519,
            "full": 121795.29999999795
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3103.1390419229865,
            "full": 120994.838124956
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3041.647542035207,
            "full": 120644.7888329858
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3054.4762500794604,
            "full": 121452.00474990997
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
          "rms_normalized_rmse_percent": 5.0
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
                "candidate_energy": 0.0001790663857086372,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.00011906512798631752,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 4.908738446829375e-06,
                  "rgb_channel": 0,
                  "sky_patch_index": 60
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
                  "maximum": 0.0004904451780021191,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.524259854108095e-05
                },
                "candidate_energy": 33.11304909272451,
                "cvrmse_percent": 21.29918974417161,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06025005698624996,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.09311047480492,
                "relative_energy_error_percent": 0.06025005698624996,
                "rms_normalized_rmse_percent": 1.954462839308435,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01479795016348362,
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "reference": 0.0143075049854815,
                  "rgb_channel": 0,
                  "sky_patch_index": 79
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016554445028305054,
                  "p50": 5.6487792221560085e-09,
                  "p90": 6.4506133412578535e-06,
                  "p95": 1.6279190276691194e-05,
                  "p99": 0.00013417471200227737
                },
                "candidate_energy": 31.103034589231026,
                "cvrmse_percent": 42.983753330400525,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0015205469648492537,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.103507532670776,
                "relative_energy_error_percent": 0.0015205469648492539,
                "rms_normalized_rmse_percent": 1.9890121287339138,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.060807136818766594,
                  "global_sensor_index": 205,
                  "local_sensor_index": 30,
                  "reference": 0.0624625813215971,
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
                  "maximum": 0.0006012250087223947,
                  "p50": 0.0,
                  "p90": 1.2704404070974616e-07,
                  "p95": 7.102690869942307e-05,
                  "p99": 0.00019790465012192726
                },
                "candidate_energy": 166.5082476581564,
                "cvrmse_percent": 8.653484171935645,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.023915271764226288,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.5480780836482,
                "relative_energy_error_percent": 0.023915271764226288,
                "rms_normalized_rmse_percent": 1.8383179193387134,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0023797210305929184,
                  "global_sensor_index": 1219,
                  "local_sensor_index": 84,
                  "reference": 0.0017784960218705237,
                  "rgb_channel": 0,
                  "sky_patch_index": 23
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0021212995052337646,
                  "p50": 1.9782088322983782e-07,
                  "p90": 3.052785395993856e-05,
                  "p95": 0.00011375258327461779,
                  "p99": 0.0003185553941875696
                },
                "candidate_energy": 155.82693026921527,
                "cvrmse_percent": 17.55428645884495,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04813826041275567,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.75195398800665,
                "relative_energy_error_percent": 0.04813826041270321,
                "rms_normalized_rmse_percent": 1.3301467430390501,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12283790111541748,
                  "global_sensor_index": 1208,
                  "local_sensor_index": 73,
                  "reference": 0.12071660161018372,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3050.204625003971,
            "full": 125314.75154100917
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3094.9197500012815,
            "full": 125575.85000002291
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3098.669125000015,
            "full": 126881.3246670179
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 3074.2166249547154,
            "full": 126314.6767920116
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
          "rms_normalized_rmse_percent": 5.0
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
                  "maximum": 4.001079560111975e-06,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.000204616913663358,
                "cvrmse_percent": 0.0,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 0.0,
                "passed": true,
                "physically_near_zero": true,
                "reference_energy": 0.00013721530525145909,
                "relative_energy_error_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 4.001079560111975e-06,
                  "global_sensor_index": 146,
                  "local_sensor_index": 146,
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
                  "maximum": 0.0003195693716406822,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.923302913084626e-05
                },
                "candidate_energy": 33.08132691458377,
                "cvrmse_percent": 12.846903688929501,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.044921377144061365,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 33.096194180792054,
                "relative_energy_error_percent": 0.04492137714406137,
                "rms_normalized_rmse_percent": 1.1789293105160001,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018120120279490948,
                  "global_sensor_index": 973,
                  "local_sensor_index": 798,
                  "reference": 0.01843968965113163,
                  "rgb_channel": 0,
                  "sky_patch_index": 137
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00118197500705719,
                  "p50": 1.3416229904805732e-08,
                  "p90": 4.505953597799825e-06,
                  "p95": 1.1168612763867696e-05,
                  "p99": 8.585036812291946e-05
                },
                "candidate_energy": 31.131525235276314,
                "cvrmse_percent": 27.406468057185272,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.008255311551757703,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 31.128955443021685,
                "relative_energy_error_percent": 0.008255311551757703,
                "rms_normalized_rmse_percent": 1.269019828455047,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05363774485886097,
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "reference": 0.05481971986591816,
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
                  "maximum": 0.0003053697291761637,
                  "p50": 0.0,
                  "p90": 1.2356322258712488e-07,
                  "p95": 3.73331131413579e-05,
                  "p99": 0.00011120742419734597
                },
                "candidate_energy": 166.46207804785138,
                "cvrmse_percent": 4.896290632694195,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0393246394535471,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 166.52756441214723,
                "relative_energy_error_percent": 0.0393246394535471,
                "rms_normalized_rmse_percent": 1.0401614738969056,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00727858766913414,
                  "global_sensor_index": 1220,
                  "local_sensor_index": 85,
                  "reference": 0.006973217939957976,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0018127486109733582,
                  "p50": 1.5205682757368777e-07,
                  "p90": 2.0129641052335513e-05,
                  "p95": 6.708735600113869e-05,
                  "p99": 0.0001898405607789755
                },
                "candidate_energy": 155.8256925694437,
                "cvrmse_percent": 10.72146507266932,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.013532968785934504,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 155.80460758053283,
                "relative_energy_error_percent": 0.013532968785902582,
                "rms_normalized_rmse_percent": 0.8126631995610195,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.11615495011210442,
                  "global_sensor_index": 1240,
                  "local_sensor_index": 105,
                  "reference": 0.11796769872307777,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 5936.243584030308,
            "full": 224438.57458303683
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 5906.33466700092,
            "full": 225060.52583397832
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 5947.968749911524,
            "full": 222839.50379199814
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 5902.985208085738,
            "full": 224527.82508300152
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
    "/content/suite-vulkan-0.3.3/acceptance/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 92250.29066693969,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 358508.1085410202,
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
            "reference_energy": 0.00017091610945740854,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 2.0005397800559876e-06
            },
            "worst": {
              "global_sensor_index": 146,
              "local_sensor_index": 146,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 2.0005397800559876e-06,
              "candidate": 0.0,
              "position": [
                22.75,
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
            "reference_energy": 0.00017091610945740854,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 2.0005397800559876e-06
            },
            "worst": {
              "global_sensor_index": 146,
              "local_sensor_index": 146,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 2.0005397800559876e-06,
              "candidate": 0.0,
              "position": [
                22.75,
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
            "nmbe_percent": -0.04855629390713468,
            "cvrmse_percent": 8.874938804105533,
            "rms_normalized_rmse_percent": 0.8142109782216739,
            "reference_energy": 33.0645365740404,
            "candidate_energy": 33.04848166048248,
            "relative_energy_error_percent": 0.04855629390713469,
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
            "nmbe_percent": -1.968132244236585,
            "cvrmse_percent": 53.1722618131133,
            "rms_normalized_rmse_percent": 2.4647513836113832,
            "reference_energy": 31.15446440267408,
            "candidate_energy": 30.541303343245836,
            "relative_energy_error_percent": 1.9681322442366047,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0539125469222255e-05,
              "p95": 2.182223397539928e-05,
              "p99": 7.065437239361927e-05,
              "maximum": 0.0025009773671627045
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06053117662668228,
              "candidate": 0.05803019925951958,
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
            "nmbe_percent": -0.9797971992966865,
            "cvrmse_percent": 25.636523900188102,
            "rms_normalized_rmse_percent": 2.4495729550401673,
            "reference_energy": 64.2190009767145,
            "candidate_energy": 63.589785003728295,
            "relative_energy_error_percent": 0.9797971992967515,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0547160309215578e-05,
              "p95": 2.1596832993964196e-05,
              "p99": 6.735417991876602e-05,
              "maximum": 0.0025009773671627045
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06053117662668228,
              "candidate": 0.05803019925951958,
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
            "nmbe_percent": -0.10208530943133665,
            "cvrmse_percent": 3.3215083775235894,
            "rms_normalized_rmse_percent": 0.7056729756703661,
            "reference_energy": 166.47837410339352,
            "candidate_energy": 166.30842414005383,
            "relative_energy_error_percent": 0.10208530943132596,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0710209608078003e-07,
              "p95": 1.0293908417224884e-05,
              "p99": 5.91520220041275e-05,
              "maximum": 0.0003182012587785721
            },
            "worst": {
              "global_sensor_index": 1201,
              "local_sensor_index": 66,
              "sky_patch_index": 82,
              "rgb_channel": 0,
              "reference": 0.010633326135575771,
              "candidate": 0.0103151248767972,
              "position": [
                1.659999966621399,
                9.095957279205322,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.628925808733034,
            "cvrmse_percent": 31.391433478447507,
            "rms_normalized_rmse_percent": 2.3800628798886856,
            "reference_energy": 155.83159717661235,
            "candidate_energy": 153.2932160720416,
            "relative_energy_error_percent": 1.6289258087330494,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.9129372453317046e-07,
              "p90": 3.074610867770391e-05,
              "p95": 5.467332084663212e-05,
              "p99": 0.00016284058801829815,
              "maximum": 0.004774041473865509
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12023860216140747,
              "candidate": 0.11546456068754196,
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
            "nmbe_percent": -0.8402877072511016,
            "cvrmse_percent": 15.14653729859569,
            "rms_normalized_rmse_percent": 2.375247453352765,
            "reference_energy": 322.3099712800057,
            "candidate_energy": 319.60164021209545,
            "relative_energy_error_percent": 0.8402877072510417,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.919001869689964e-07,
              "p90": 3.012582892552038e-05,
              "p95": 5.259762838250026e-05,
              "p99": 0.0001483603846281767,
              "maximum": 0.004774041473865509
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12023860216140747,
              "candidate": 0.11546456068754196,
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
            "reference_energy": 0.0,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 0.0,
            "physically_near_zero": true,
            "rms_normalized_to": "full",
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
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
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
            "nmbe_percent": -0.04855629390713468,
            "cvrmse_percent": 8.874938804105533,
            "rms_normalized_rmse_percent": 0.8142109782216739,
            "reference_energy": 33.0645365740404,
            "candidate_energy": 33.04848166048248,
            "relative_energy_error_percent": 0.04855629390713469,
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
            "nmbe_percent": 56.10838965829175,
            "cvrmse_percent": 576.1747011855781,
            "rms_normalized_rmse_percent": 19.493591657553235,
            "reference_energy": 19.564165263698005,
            "candidate_energy": 30.541303343245836,
            "relative_energy_error_percent": 56.10838965829171,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2290001147193834e-05,
              "p95": 9.713049621495872e-05,
              "p99": 0.00025945485322154127,
              "maximum": 0.010520318523049355
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01967873051762581,
              "candidate": 0.030199049040675163,
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
            "nmbe_percent": 20.827196535807513,
            "cvrmse_percent": 214.13699076042298,
            "rms_normalized_rmse_percent": 19.4890517747613,
            "reference_energy": 52.62870183773841,
            "candidate_energy": 63.589785003728295,
            "relative_energy_error_percent": 20.827196535807442,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2269999539712444e-05,
              "p95": 9.706999844638631e-05,
              "p99": 0.0002537892432883382,
              "maximum": 0.010520318523049355
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01967873051762581,
              "candidate": 0.030199049040675163,
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
            "nmbe_percent": -0.10208530943133665,
            "cvrmse_percent": 3.3215083775235894,
            "rms_normalized_rmse_percent": 0.7056729756703661,
            "reference_energy": 166.47837410339352,
            "candidate_energy": 166.30842414005383,
            "relative_energy_error_percent": 0.10208530943132596,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0710209608078003e-07,
              "p95": 1.0293908417224884e-05,
              "p99": 5.91520220041275e-05,
              "maximum": 0.0003182012587785721
            },
            "worst": {
              "global_sensor_index": 1201,
              "local_sensor_index": 66,
              "sky_patch_index": 82,
              "rgb_channel": 0,
              "reference": 0.010633326135575771,
              "candidate": 0.0103151248767972,
              "position": [
                1.659999966621399,
                9.095957279205322,
                0.800000011920929
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 45.599185318630155,
            "cvrmse_percent": 277.405659492265,
            "rms_normalized_rmse_percent": 16.284151479205782,
            "reference_energy": 105.28439134915055,
            "candidate_energy": 153.2932160720416,
            "relative_energy_error_percent": 45.599185318630205,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023600937565788628,
              "p95": 0.00038653332740068436,
              "p99": 0.00085347646381706,
              "maximum": 0.015054641291499138
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024879267439246178,
              "candidate": 0.039933908730745316,
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
            "nmbe_percent": 17.603174842546636,
            "cvrmse_percent": 107.44887546575019,
            "rms_normalized_rmse_percent": 16.280871690059502,
            "reference_energy": 271.76276545254416,
            "candidate_energy": 319.60164021209545,
            "relative_energy_error_percent": 17.603174842546643,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023457042116206155,
              "p95": 0.0003822348080575466,
              "p99": 0.0008508146274834871,
              "maximum": 0.015054641291499138
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024879267439246178,
              "candidate": 0.039933908730745316,
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
      "bias_percent": -0.016273738188909904,
      "rms_normalized_error_percent": 0.2243826038935129,
      "absolute_error": {
        "p95": 0.08588205581843075,
        "p99": 0.13637171262009987,
        "maximum": 0.2052851772504818
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.979261658708775,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2243826038935129
    },
    "overcast": {
      "bias_percent": -0.022974264098145635,
      "rms_normalized_error_percent": 0.16167837843327676,
      "absolute_error": {
        "p95": 0.04548316001892089,
        "p99": 0.06877022027969361,
        "maximum": 0.10744476318359375
      },
      "worst_index": [
        1156
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.373974323272705,
      "reference_fraction_of_uniform": 0.6267101764678955,
      "rms_normalized_to_uniform_percent": 0.11572839937051546
    },
    "horizon": {
      "bias_percent": 0.03742364503863442,
      "rms_normalized_error_percent": 1.6905629296153137,
      "absolute_error": {
        "p95": 0.0610485212908092,
        "p99": 0.11750965741806667,
        "maximum": 0.1957113111536466
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2557085330834694,
      "reference_fraction_of_uniform": 0.17991996782590705,
      "rms_normalized_to_uniform_percent": 0.16926791495327
    },
    "north": {
      "bias_percent": -0.12467518267236513,
      "rms_normalized_error_percent": 0.3667075382841837,
      "absolute_error": {
        "p95": 0.02933969497680664,
        "p99": 0.04871379613876342,
        "maximum": 0.07668590545654297
      },
      "worst_index": [
        1212
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3877977132797241,
      "reference_fraction_of_uniform": 0.19884590804576874,
      "rms_normalized_to_uniform_percent": 0.0760203752797232
    },
    "east": {
      "bias_percent": -4.46499093826386,
      "rms_normalized_error_percent": 4.111347632911952,
      "absolute_error": {
        "p95": 0.00016419338353443889,
        "p99": 0.0010271270386874648,
        "maximum": 0.0018250048160552979
      },
      "worst_index": [
        1905
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0005856994539499283,
      "reference_fraction_of_uniform": 8.391997107537463e-05,
      "rms_normalized_to_uniform_percent": 0.0009626750222983398
    },
    "south": {
      "bias_percent": -0.02900024885226531,
      "rms_normalized_error_percent": 0.3556400205551171,
      "absolute_error": {
        "p95": 0.028404965996742245,
        "p99": 0.04764063835144039,
        "maximum": 0.07563614845275879
      },
      "worst_index": [
        1974
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3871899843215942,
      "reference_fraction_of_uniform": 0.19875884056091309,
      "rms_normalized_to_uniform_percent": 0.07292999572278416
    },
    "west": {
      "bias_percent": 0.009630611661000568,
      "rms_normalized_error_percent": 0.2964633636354469,
      "absolute_error": {
        "p95": 0.06598739624023436,
        "p99": 0.1258527088165282,
        "maximum": 0.19782114028930664
      },
      "worst_index": [
        1997
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.780207633972168,
      "reference_fraction_of_uniform": 0.6849159002304077,
      "rms_normalized_to_uniform_percent": 0.18331897525539775
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
          "nmbe_percent": -100.00000000000001,
          "cvrmse_percent": 945.7656242980854,
          "absolute_error_percentiles_lux": {
            "p50": 1.8337441360927187e-05,
            "p90": 0.0029141669627279036,
            "p95": 0.008060145284980532,
            "p99": 0.03505595393478876
          },
          "maximum_absolute_error_lux": 1.8674331903457642,
          "worst": {
            "sensor_index": 10,
            "position": [
              13.25,
              13.134792804718018,
              0.800000011920929
            ],
            "hour_of_year": 4449.5,
            "foton_lux": 1.1754943508222875e-38,
            "radiance_lux": 1.8674331903457642
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
            "mean_absolute_error_percentage_points": 0.0008653500885032815,
            "maximum_error_percentage_points": 0.022238525585615565,
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
          "nmbe_percent": -0.302737320224976,
          "cvrmse_percent": 3.2392180423157106,
          "absolute_error_percentiles_lux": {
            "p50": 0.43309593200683594,
            "p90": 3.99774169921875,
            "p95": 7.1898193359375,
            "p99": 19.482056884765598
          },
          "maximum_absolute_error_lux": 276.802734375,
          "worst": {
            "sensor_index": 33,
            "position": [
              1.534999966621399,
              4.328545093536377,
              0.800000011920929
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5688.88037109375,
            "radiance_lux": 5965.68310546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0894464897260274,
            "maximum_error_percentage_points": 1.805068493150685,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22844237641842366,
            "maximum_error_percentage_points": 1.739199683851389,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.23680636415525122,
            "maximum_error_percentage_points": 4.028630136986294,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.23704580479452053,
            "maximum_error_percentage_points": 4.028630136986301,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0029950057077625367,
            "maximum_error_percentage_points": 0.14000000000000012,
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
          "nmbe_percent": -0.1979111616602141,
          "cvrmse_percent": 1.4411982569520507,
          "absolute_error_percentiles_lux": {
            "p50": 2.0209808349609375,
            "p90": 12.941964721679689,
            "p95": 20.623779296875,
            "p99": 46.620712890624645
          },
          "maximum_absolute_error_lux": 399.271484375,
          "worst": {
            "sensor_index": 54,
            "position": [
              1.149999976158142,
              19.175687789916992,
              0.800000011920929
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 21788.73046875,
            "radiance_lux": 22188.001953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.37292794675334734,
            "maximum_error_percentage_points": 2.6254794520547975,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2864642798529138,
            "maximum_error_percentage_points": 1.9108703981849544,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21854686169801096,
            "maximum_error_percentage_points": 1.9132876712328724,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22664344864948532,
            "maximum_error_percentage_points": 1.9132876712328724,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015350979026391095,
            "maximum_error_percentage_points": 0.24712328767123282,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 40.23484726586844,
          "radiance_percent": 40.60204753558391,
          "difference_percentage_points": 0.36720026971546815,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 3,
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
      "maximum_error_percentage_points": 0.005002943065072429,
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
            "maximum_error_percentage_points": 0.0049920696101775075,
            "passed": true
          },
          {
            "identifier": "office_01",
            "maximum_error_percentage_points": 0.005002943065072429,
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
        "maximum_error_percentage_points": 0.005002943065072429,
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
              "maximum_error_percentage_points": 0.0049920696101775075,
              "passed": true
            },
            {
              "identifier": "office_01",
              "maximum_error_percentage_points": 0.005002943065072429,
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
            "nmbe_percent": 16.033846662181425,
            "cvrmse_percent": 45.01674621935296,
            "absolute_error_lux": {
              "p50": 5.160102844238281,
              "p90": 51.290994644165046,
              "p95": 90.71461448669427,
              "p99": 228.52846576690655,
              "maximum": 2597.26318359375
            },
            "per_sensor_maximum_error_lux": {
              "p50": 107.57307052612305,
              "p90": 611.4261535644532,
              "p95": 953.3927856445304,
              "p99": 1486.3652758789049,
              "maximum": 2597.26318359375
            },
            "worst": {
              "sensor_index": 60,
              "sun_up_hour_index": 1161,
              "hour_of_year": 2727.5,
              "foton_lux": 8662.4775390625,
              "radiance_lux": 6065.21435546875
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.9243437499999998,
              "maximum_error_percentage_points": 30.32,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.293427083333333,
              "maximum_error_percentage_points": 24.46,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.484520833333334,
              "maximum_error_percentage_points": 43.510000000000005,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.469645833333334,
              "maximum_error_percentage_points": 43.510000000000005,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.037010416666666664,
              "maximum_error_percentage_points": 1.2300000000000004,
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
            "nmbe_percent": 15.320305082663568,
            "cvrmse_percent": 26.60685662280671,
            "absolute_error_lux": {
              "p50": 59.34765625,
              "p90": 246.30777282714843,
              "p95": 375.25306396484336,
              "p99": 712.2654394531237,
              "maximum": 3476.556640625
            },
            "per_sensor_maximum_error_lux": {
              "p50": 740.6820068359375,
              "p90": 1655.89599609375,
              "p95": 1875.6660644531246,
              "p99": 2519.932343749998,
              "maximum": 3476.556640625
            },
            "worst": {
              "sensor_index": 49,
              "sun_up_hour_index": 1161,
              "hour_of_year": 2727.5,
              "foton_lux": 28311.39453125,
              "radiance_lux": 24834.837890625
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.859966101694916,
              "maximum_error_percentage_points": 38.65,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.588745762711865,
              "maximum_error_percentage_points": 32.8,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 13.104011299435028,
              "maximum_error_percentage_points": 53.06999999999999,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 13.067514124293789,
              "maximum_error_percentage_points": 53.07,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.37390960451977406,
              "maximum_error_percentage_points": 2.7700000000000005,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 40.23484726586844,
            "radiance_percent": 31.173753473063897,
            "difference_percentage_points": 9.061093792804542,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 6.3033722100000205,
        "radiance_seconds": 39.75681779199999,
        "speedup": 6.307229918761193,
        "passed": false
      },
      "versions": {
        "python": "3.13.16",
        "platform": "Linux-6.6.159+-x86_64-with-glibc2.39"
      },
      "folders": {
        "foton": "/content/suite-vulkan-0.3.3/acceptance/mf1/annual",
        "radiance": "/content/suite-vulkan-0.3.3/acceptance/mf1/stock/annual_daylight"
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
      "study_preparation_seconds": 0.3547586949999868,
      "weather_seconds": 0.22766118799995638,
      "metric_reduction_seconds": 5.6653952679999975,
      "write_seconds": 0.055149758999959886,
      "total_seconds": 5.948613515000034,
      "cold_end_to_end_seconds": 6.3033722100000205,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.04005694400007087,
      "engine_upload_seconds": 0.015281603,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.414745398,
      "engine_annual_reduction_seconds": 0.200921346,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.414745398
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3547586949999868,
      "weather_seconds": 0.22353780799994638,
      "metric_reduction_seconds": 5.191523851000056,
      "write_seconds": 0.05425614700004644,
      "total_seconds": 5.4697045690001005,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 5.4697045690001005,
      "raw_export_seconds": 0.03985373000000436,
      "engine_upload_seconds": 0.018577813,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.1e-07,
      "engine_annual_reduction_seconds": 0.201722233,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.04954845899999327,
      "full": 0.47661620500002755
    }
  },
  "elapsed_seconds": 72.60022131400001,
  "result_class": "passed"
}
```
