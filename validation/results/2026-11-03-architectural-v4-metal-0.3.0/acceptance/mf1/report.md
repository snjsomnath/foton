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
      "solver_version": "0.3.0",
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
          "maximum": 2.4543692234146874e-06
        },
        "worst_index": [
          24,
          60,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.03850638155714472,
        "rms_normalized_error_percent": 1.155421509035522,
        "absolute_error": {
          "p95": 1.0928690608125163e-05,
          "p99": 7.69327743910253e-05,
          "maximum": 0.0009092241525650024
        },
        "worst_index": [
          19,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": 0.034330123977876485,
        "rms_normalized_error_percent": 0.7907453259226115,
        "absolute_error": {
          "p95": 5.883490666747093e-05,
          "p99": 0.00017355475574731827,
          "maximum": 0.0018055140972137451
        },
        "worst_index": [
          114,
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
          "maximum": 2.4543692234146874e-06
        },
        "worst_index": [
          24,
          60,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_02",
        "bias_percent": 0.0197023215965148,
        "rms_normalized_error_percent": 0.9566435434357288,
        "absolute_error": {
          "p95": 9.482794121140596e-06,
          "p99": 6.361515261232853e-05,
          "maximum": 0.0007454603910446167
        },
        "worst_index": [
          19,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "office_01",
        "bias_percent": -0.00236836719489025,
        "rms_normalized_error_percent": 0.6675692575370138,
        "absolute_error": {
          "p95": 4.974263720214367e-05,
          "p99": 0.00014143437147140503,
          "maximum": 0.0013432279229164124
        },
        "worst_index": [
          91,
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
                "nmbe_percent": -0.029197165541557456,
                "cvrmse_percent": 40.22018913557876,
                "rms_normalized_rmse_percent": 3.690825042537583,
                "reference_energy": 33.0919825331581,
                "candidate_energy": 33.08232061223691,
                "relative_energy_error_percent": 0.029197165541557452,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014348397962749004,
                  "maximum": 0.0009446544572710991
                },
                "worst": {
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "sky_patch_index": 104,
                  "rgb_channel": 0,
                  "reference": 0.015938020311295986,
                  "candidate": 0.016882674768567085
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.021761539348293214,
                "cvrmse_percent": 110.30488442037097,
                "rms_normalized_rmse_percent": 3.7277101652323386,
                "reference_energy": 19.539424225632846,
                "candidate_energy": 19.543676305124137,
                "relative_energy_error_percent": 0.02176153934829321,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.277509532992552e-06,
                  "p99": 0.00023285688075702637,
                  "maximum": 0.0016413666307926178
                },
                "worst": {
                  "global_sensor_index": 235,
                  "local_sensor_index": 60,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03877486661076546,
                  "candidate": 0.03713349997997284
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
                "nmbe_percent": -0.021986345203116906,
                "cvrmse_percent": 16.01727252623777,
                "rms_normalized_rmse_percent": 3.401286359399763,
                "reference_energy": 166.54974312306172,
                "candidate_energy": 166.51312492160378,
                "relative_energy_error_percent": 0.02198634520311691,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6218982636929372e-07,
                  "p95": 0.000126861847093096,
                  "p99": 0.0003531679976731539,
                  "maximum": 0.0011461656540632248
                },
                "worst": {
                  "global_sensor_index": 1170,
                  "local_sensor_index": 35,
                  "sky_patch_index": 105,
                  "rgb_channel": 0,
                  "reference": 0.015227739699184895,
                  "candidate": 0.01637390535324812
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.01892729006479248,
                "cvrmse_percent": 42.6499638511031,
                "rms_normalized_rmse_percent": 2.5020215200367564,
                "reference_energy": 105.221373689913,
                "candidate_energy": 105.24128924452144,
                "relative_energy_error_percent": 0.018927290064789104,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.4832591179803003e-05,
                  "p95": 0.00020029814913868904,
                  "p99": 0.0005781614454463124,
                  "maximum": 0.003412313759326935
                },
                "worst": {
                  "global_sensor_index": 1290,
                  "local_sensor_index": 155,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06789426878094673,
                  "candidate": 0.0644819550216198
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1589.4578750012442,
            "full": 8217.167624970898
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1610.6730001047254,
            "full": 8388.329999987036
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1635.9038749942556,
            "full": 8524.363082950003
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 1632.4872080003843,
            "full": 8360.782625037245
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
                "reference_energy": 0.00013437285397444043,
                "candidate_energy": 0.00025400221628402164,
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
                  "global_sensor_index": 54,
                  "local_sensor_index": 54,
                  "sky_patch_index": 10,
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
                "nmbe_percent": 0.0033717690964674947,
                "cvrmse_percent": 21.773512371639896,
                "rms_normalized_rmse_percent": 1.996528944902432,
                "reference_energy": 33.07385448552054,
                "candidate_energy": 33.074969659525095,
                "relative_energy_error_percent": 0.0033717690964674943,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.527409616159275e-05,
                  "maximum": 0.0005358699709177017
                },
                "worst": {
                  "global_sensor_index": 217,
                  "local_sensor_index": 42,
                  "sky_patch_index": 80,
                  "rgb_channel": 0,
                  "reference": 0.014702050015330315,
                  "candidate": 0.014166180044412613
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.03174555611153855,
                "cvrmse_percent": 41.62966690519281,
                "rms_normalized_rmse_percent": 1.927584919287684,
                "reference_energy": 31.11216303632287,
                "candidate_energy": 31.10228630714866,
                "relative_energy_error_percent": 0.03174555611153854,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.385444978855958e-09,
                  "p90": 6.378861871780844e-06,
                  "p95": 1.5924135186651236e-05,
                  "p99": 0.00013906889944337308,
                  "maximum": 0.0011258460581302643
                },
                "worst": {
                  "global_sensor_index": 245,
                  "local_sensor_index": 70,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.045588329434394836,
                  "candidate": 0.0467141754925251
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
                "nmbe_percent": 0.029753388162705008,
                "cvrmse_percent": 8.729019233551764,
                "rms_normalized_rmse_percent": 1.8541845591488153,
                "reference_energy": 166.50589689088292,
                "candidate_energy": 166.55543803669866,
                "relative_energy_error_percent": 0.029753388162705008,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.5440782590303862e-07,
                  "p95": 7.203296991065145e-05,
                  "p99": 0.00019785587210208178,
                  "maximum": 0.0006823497824370861
                },
                "worst": {
                  "global_sensor_index": 1178,
                  "local_sensor_index": 43,
                  "sky_patch_index": 80,
                  "rgb_channel": 0,
                  "reference": 0.014311815146356821,
                  "candidate": 0.014994164928793907
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.041672701591036324,
                "cvrmse_percent": 17.52897422435359,
                "rms_normalized_rmse_percent": 1.3287158324779607,
                "reference_energy": 155.70876728821773,
                "candidate_energy": 155.64387923827456,
                "relative_energy_error_percent": 0.041672701591077395,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9587960586875397e-07,
                  "p90": 3.099304885836346e-05,
                  "p95": 0.00011709675891324878,
                  "p99": 0.0003306940197944641,
                  "maximum": 0.002160448580980301
                },
                "worst": {
                  "global_sensor_index": 1275,
                  "local_sensor_index": 140,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11565529927611351,
                  "candidate": 0.11781574785709381
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3132.942207972519,
            "full": 121795.29999999795
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3103.1390419229865,
            "full": 120994.838124956
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3041.647542035207,
            "full": 120644.7888329858
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3054.4762500794604,
            "full": 121452.00474990997
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
                "nmbe_percent": 0.0,
                "cvrmse_percent": 0.0,
                "rms_normalized_rmse_percent": 0.0,
                "reference_energy": 0.00011906512798631752,
                "candidate_energy": 0.0001790663857086372,
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
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 60,
                  "rgb_channel": 0,
                  "reference": 4.908738446829375e-06,
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
                "nmbe_percent": 0.06025005698624996,
                "cvrmse_percent": 21.29918974417161,
                "rms_normalized_rmse_percent": 1.954462839308435,
                "reference_energy": 33.09311047480492,
                "candidate_energy": 33.11304909272451,
                "relative_energy_error_percent": 0.06025005698624996,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.524259854108095e-05,
                  "maximum": 0.0004904451780021191
                },
                "worst": {
                  "global_sensor_index": 194,
                  "local_sensor_index": 19,
                  "sky_patch_index": 79,
                  "rgb_channel": 0,
                  "reference": 0.0143075049854815,
                  "candidate": 0.01479795016348362
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.0015205469648492537,
                "cvrmse_percent": 42.983753330400525,
                "rms_normalized_rmse_percent": 1.9890121287339138,
                "reference_energy": 31.103507532670776,
                "candidate_energy": 31.103034589231026,
                "relative_energy_error_percent": 0.0015205469648492539,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.6487792221560085e-09,
                  "p90": 6.4506133412578535e-06,
                  "p95": 1.6279190276691194e-05,
                  "p99": 0.00013417471200227737,
                  "maximum": 0.0016554445028305054
                },
                "worst": {
                  "global_sensor_index": 205,
                  "local_sensor_index": 30,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0624625813215971,
                  "candidate": 0.060807136818766594
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
                "nmbe_percent": -0.023915271764226288,
                "cvrmse_percent": 8.653484171935645,
                "rms_normalized_rmse_percent": 1.8383179193387134,
                "reference_energy": 166.5480780836482,
                "candidate_energy": 166.5082476581564,
                "relative_energy_error_percent": 0.023915271764226288,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2704404070974616e-07,
                  "p95": 7.102690869942307e-05,
                  "p99": 0.00019790465012192726,
                  "maximum": 0.0006012250087223947
                },
                "worst": {
                  "global_sensor_index": 1219,
                  "local_sensor_index": 84,
                  "sky_patch_index": 23,
                  "rgb_channel": 0,
                  "reference": 0.0017784960218705237,
                  "candidate": 0.0023797210305929184
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.04813826041275567,
                "cvrmse_percent": 17.55428645884495,
                "rms_normalized_rmse_percent": 1.3301467430390501,
                "reference_energy": 155.75195398800665,
                "candidate_energy": 155.82693026921527,
                "relative_energy_error_percent": 0.04813826041270321,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9782088322983782e-07,
                  "p90": 3.052785395993856e-05,
                  "p95": 0.00011375258327461779,
                  "p99": 0.0003185553941875696,
                  "maximum": 0.0021212995052337646
                },
                "worst": {
                  "global_sensor_index": 1208,
                  "local_sensor_index": 73,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.12071660161018372,
                  "candidate": 0.12283790111541748
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3050.204625003971,
            "full": 125314.75154100917
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3094.9197500012815,
            "full": 125575.85000002291
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3098.669125000015,
            "full": 126881.3246670179
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 3074.2166249547154,
            "full": 126314.6767920116
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
                "reference_energy": 0.00013721530525145909,
                "candidate_energy": 0.000204616913663358,
                "relative_energy_error_percent": 0.0,
                "physically_near_zero": true,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.001079560111975e-06
                },
                "worst": {
                  "global_sensor_index": 146,
                  "local_sensor_index": 146,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0,
                  "candidate": 4.001079560111975e-06
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
                "nmbe_percent": -0.044921377144061365,
                "cvrmse_percent": 12.846903688929501,
                "rms_normalized_rmse_percent": 1.1789293105160001,
                "reference_energy": 33.096194180792054,
                "candidate_energy": 33.08132691458377,
                "relative_energy_error_percent": 0.04492137714406137,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.923302913084626e-05,
                  "maximum": 0.0003195693716406822
                },
                "worst": {
                  "global_sensor_index": 973,
                  "local_sensor_index": 798,
                  "sky_patch_index": 137,
                  "rgb_channel": 0,
                  "reference": 0.01843968965113163,
                  "candidate": 0.018120120279490948
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.008255311551757703,
                "cvrmse_percent": 27.406468057185272,
                "rms_normalized_rmse_percent": 1.269019828455047,
                "reference_energy": 31.128955443021685,
                "candidate_energy": 31.131525235276314,
                "relative_energy_error_percent": 0.008255311551757703,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3416229904805732e-08,
                  "p90": 4.505953597799825e-06,
                  "p95": 1.1168612763867696e-05,
                  "p99": 8.585036812291946e-05,
                  "maximum": 0.00118197500705719
                },
                "worst": {
                  "global_sensor_index": 232,
                  "local_sensor_index": 57,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05481971986591816,
                  "candidate": 0.05363774485886097
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
                "nmbe_percent": -0.0393246394535471,
                "cvrmse_percent": 4.896290632694195,
                "rms_normalized_rmse_percent": 1.0401614738969056,
                "reference_energy": 166.52756441214723,
                "candidate_energy": 166.46207804785138,
                "relative_energy_error_percent": 0.0393246394535471,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2356322258712488e-07,
                  "p95": 3.73331131413579e-05,
                  "p99": 0.00011120742419734597,
                  "maximum": 0.0003053697291761637
                },
                "worst": {
                  "global_sensor_index": 1220,
                  "local_sensor_index": 85,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.006973217939957976,
                  "candidate": 0.00727858766913414
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.013532968785934504,
                "cvrmse_percent": 10.72146507266932,
                "rms_normalized_rmse_percent": 0.8126631995610195,
                "reference_energy": 155.80460758053283,
                "candidate_energy": 155.8256925694437,
                "relative_energy_error_percent": 0.013532968785902582,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5205682757368777e-07,
                  "p90": 2.0129641052335513e-05,
                  "p95": 6.708735600113869e-05,
                  "p99": 0.0001898405607789755,
                  "maximum": 0.0018127486109733582
                },
                "worst": {
                  "global_sensor_index": 1240,
                  "local_sensor_index": 105,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11796769872307777,
                  "candidate": 0.11615495011210442
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5936.243584030308,
            "full": 224438.57458303683
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5906.33466700092,
            "full": 225060.52583397832
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5947.968749911524,
            "full": 222839.50379199814
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 5902.985208085738,
            "full": 224527.82508300152
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/oracle/scene.rad"
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 92250.29066693969,
      "worker_pool_size": 12,
      "invocation_count": 127
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 358508.1085410202,
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
            "reference_energy": 0.00017091610945740854,
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
            "reference_energy": 0.00017091610945740854,
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
            "nmbe_percent": -1.968205660153676,
            "cvrmse_percent": 53.17210641072305,
            "rms_normalized_rmse_percent": 2.4647441800762446,
            "reference_energy": 31.15446440267408,
            "candidate_energy": 30.54128047091008,
            "relative_energy_error_percent": 1.968205660153693,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.054073600244016e-05,
              "p95": 2.182223397539928e-05,
              "p99": 7.065437239361927e-05,
              "maximum": 0.002500966191291809
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06053117662668228,
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
            "nmbe_percent": -0.9798296429637113,
            "cvrmse_percent": 25.636583414650328,
            "rms_normalized_rmse_percent": 2.449578641654221,
            "reference_energy": 64.2190009767145,
            "candidate_energy": 63.58976416872946,
            "relative_energy_error_percent": 0.9798296429637638,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0548189493420104e-05,
              "p95": 2.159683153877267e-05,
              "p99": 6.735417991876602e-05,
              "maximum": 0.002500966191291809
            },
            "worst": {
              "global_sensor_index": 192,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06053117662668228,
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
            "nmbe_percent": -1.6288157636863554,
            "cvrmse_percent": 31.390314085110933,
            "rms_normalized_rmse_percent": 2.3799780087556037,
            "reference_energy": 155.83159717661235,
            "candidate_energy": 153.29338755699544,
            "relative_energy_error_percent": 1.6288157636863707,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.911594461669665e-07,
              "p90": 3.074610867770391e-05,
              "p95": 5.467332084663212e-05,
              "p99": 0.00016284058801829815,
              "maximum": 0.004774026572704315
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12023860216140747,
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
            "nmbe_percent": -0.8402310810514868,
            "cvrmse_percent": 15.145994291937598,
            "rms_normalized_rmse_percent": 2.3751623002147,
            "reference_energy": 322.3099712800057,
            "candidate_energy": 319.60182272398316,
            "relative_energy_error_percent": 0.8402310810514271,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.9180372368718963e-07,
              "p90": 3.0123302713036586e-05,
              "p95": 5.259449244476855e-05,
              "p99": 0.00014842161908745766,
              "maximum": 0.004774026572704315
            },
            "worst": {
              "global_sensor_index": 1280,
              "local_sensor_index": 145,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.12023860216140747,
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
            "reference_energy": 0.0,
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
            "reference_energy": 0.0,
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
            "nmbe_percent": 56.10827274895548,
            "cvrmse_percent": 576.1742680889607,
            "rms_normalized_rmse_percent": 19.493577004690845,
            "reference_energy": 19.564165263698005,
            "candidate_energy": 30.54128047091008,
            "relative_energy_error_percent": 56.10827274895545,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2290001147193834e-05,
              "p95": 9.713049621495872e-05,
              "p99": 0.00025945485322154127,
              "maximum": 0.01052032969892025
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01967873051762581,
              "candidate": 0.03019906021654606,
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
            "nmbe_percent": 20.827156947145596,
            "cvrmse_percent": 214.13685591098795,
            "rms_normalized_rmse_percent": 19.489039501834462,
            "reference_energy": 52.62870183773841,
            "candidate_energy": 63.58976416872946,
            "relative_energy_error_percent": 20.827156947145543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2269999539712444e-05,
              "p95": 9.706999844638631e-05,
              "p99": 0.0002537892432883382,
              "maximum": 0.01052032969892025
            },
            "worst": {
              "global_sensor_index": 963,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01967873051762581,
              "candidate": 0.03019906021654606,
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
            "nmbe_percent": 45.59934819648095,
            "cvrmse_percent": 277.40734036734233,
            "rms_normalized_rmse_percent": 16.284250149234456,
            "reference_energy": 105.28439134915055,
            "candidate_energy": 153.29338755699544,
            "relative_energy_error_percent": 45.599348196481,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023600937565788628,
              "p95": 0.00038653542287647724,
              "p99": 0.00085347646381706,
              "maximum": 0.01505456306040287
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024879267439246178,
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
            "nmbe_percent": 17.603242001080076,
            "cvrmse_percent": 107.44952844571274,
            "rms_normalized_rmse_percent": 16.280970630908723,
            "reference_energy": 271.76276545254416,
            "candidate_energy": 319.60182272398316,
            "relative_energy_error_percent": 17.603242001080083,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023457042116206155,
              "p95": 0.0003822348080575466,
              "p99": 0.0008508148603141308,
              "maximum": 0.01505456306040287
            },
            "worst": {
              "global_sensor_index": 1923,
              "local_sensor_index": 788,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024879267439246178,
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
      "bias_percent": -0.016262676594198548,
      "rms_normalized_error_percent": 0.2243853679162339,
      "absolute_error": {
        "p95": 0.08588120535356293,
        "p99": 0.13638873358690595,
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
      "rms_normalized_to_uniform_percent": 0.2243853679162339
    },
    "overcast": {
      "bias_percent": -0.02295254873661221,
      "rms_normalized_error_percent": 0.16168009154614296,
      "absolute_error": {
        "p95": 0.04548295736312865,
        "p99": 0.06877021431922913,
        "maximum": 0.107391357421875
      },
      "worst_index": [
        1156
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.373973846435547,
      "reference_fraction_of_uniform": 0.6267101168632507,
      "rms_normalized_to_uniform_percent": 0.11572962414366318
    },
    "horizon": {
      "bias_percent": 0.0373656615323748,
      "rms_normalized_error_percent": 1.690601872679201,
      "absolute_error": {
        "p95": 0.06104826602110955,
        "p99": 0.11750827544521815,
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
      "rms_normalized_to_uniform_percent": 0.1692718141344898
    },
    "north": {
      "bias_percent": -0.12465727295603,
      "rms_normalized_error_percent": 0.36670227522364357,
      "absolute_error": {
        "p95": 0.02933978140354156,
        "p99": 0.04871398925781249,
        "maximum": 0.07668018341064453
      },
      "worst_index": [
        1212
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3877977132797241,
      "reference_fraction_of_uniform": 0.19884590804576874,
      "rms_normalized_to_uniform_percent": 0.07601928363409154
    },
    "east": {
      "bias_percent": -4.464151970825548,
      "rms_normalized_error_percent": 4.111238045337431,
      "absolute_error": {
        "p95": 0.0001641934042709181,
        "p99": 0.0010271255299448938,
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
      "rms_normalized_to_uniform_percent": 0.0009626493120468014
    },
    "south": {
      "bias_percent": -0.02897333342500415,
      "rms_normalized_error_percent": 0.3556423518633313,
      "absolute_error": {
        "p95": 0.0284048855304718,
        "p99": 0.04764072895050045,
        "maximum": 0.07563591003417969
      },
      "worst_index": [
        1974
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3871899843215942,
      "reference_fraction_of_uniform": 0.19875884056091309,
      "rms_normalized_to_uniform_percent": 0.07293048030694262
    },
    "west": {
      "bias_percent": 0.009622448816015943,
      "rms_normalized_error_percent": 0.296465711514621,
      "absolute_error": {
        "p95": 0.06598939895629882,
        "p99": 0.12585289001464833,
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
      "rms_normalized_to_uniform_percent": 0.18332040238236988
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
          "nmbe_percent": -97.33998577732851,
          "cvrmse_percent": 946.2779150434625,
          "absolute_error_percentiles_lux": {
            "p50": 2.261927875224501e-05,
            "p90": 0.0032334220129996492,
            "p95": 0.008633108716458055,
            "p99": 0.035026252269744894
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
            "foton_lux": 0.0,
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
          "nmbe_percent": -0.30280825513135745,
          "cvrmse_percent": 3.2391732953590933,
          "absolute_error_percentiles_lux": {
            "p50": 0.4330883026123047,
            "p90": 3.997672176361084,
            "p95": 7.189271545410151,
            "p99": 19.4819952392578
          },
          "maximum_absolute_error_lux": 276.80224609375,
          "worst": {
            "sensor_index": 33,
            "position": [
              1.534999966621399,
              4.328545093536377,
              0.800000011920929
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5688.880859375,
            "radiance_lux": 5965.68310546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0894152397260274,
            "maximum_error_percentage_points": 1.805068493150685,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22844237641842363,
            "maximum_error_percentage_points": 1.739199683851389,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.23683761415525123,
            "maximum_error_percentage_points": 4.028630136986294,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.23707705479452051,
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
          "nmbe_percent": -0.19789275096760509,
          "cvrmse_percent": 1.4411162806268771,
          "absolute_error_percentiles_lux": {
            "p50": 2.0208282470703125,
            "p90": 12.94140625,
            "p95": 20.623046875,
            "p99": 46.619082031249945
          },
          "maximum_absolute_error_lux": 399.2734375,
          "worst": {
            "sensor_index": 54,
            "position": [
              1.149999976158142,
              19.175687789916992,
              0.800000011920929
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 21788.728515625,
            "radiance_lux": 22188.001953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.37289404844826257,
            "maximum_error_percentage_points": 2.6254794520547975,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2864868787229703,
            "maximum_error_percentage_points": 1.9108703981849544,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21858076000309568,
            "maximum_error_percentage_points": 1.9132876712328724,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22667734695457004,
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
            "nmbe_percent": 16.131022091452277,
            "cvrmse_percent": 46.13935551786828,
            "absolute_error_lux": {
              "p50": 5.1496880650520325,
              "p90": 51.7745849609375,
              "p95": 90.71620438098907,
              "p99": 230.70496294021603,
              "maximum": 3233.7421875
            },
            "per_sensor_maximum_error_lux": {
              "p50": 107.38164043426514,
              "p90": 629.5068969726566,
              "p95": 958.8832641601557,
              "p99": 1504.2532421874985,
              "maximum": 3233.7421875
            },
            "worst": {
              "sensor_index": 34,
              "sun_up_hour_index": 2390,
              "hour_of_year": 4455.5,
              "foton_lux": 20372.591796875,
              "radiance_lux": 17138.849609375
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 1.9312604166666667,
              "maximum_error_percentage_points": 32.38,
              "passed": true
            },
            "cda": {
              "mean_absolute_error_percentage_points": 4.29390625,
              "maximum_error_percentage_points": 23.440000000000005,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 4.524937499999999,
              "maximum_error_percentage_points": 43.07000000000001,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 4.509593749999999,
              "maximum_error_percentage_points": 43.07,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.03529166666666666,
              "maximum_error_percentage_points": 1.2600000000000016,
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
            "nmbe_percent": 15.199304847396045,
            "cvrmse_percent": 26.544157496232298,
            "absolute_error_lux": {
              "p50": 59.125526428222656,
              "p90": 244.93754882812505,
              "p95": 372.636196899414,
              "p99": 712.8118798828124,
              "maximum": 2848.7421875
            },
            "per_sensor_maximum_error_lux": {
              "p50": 732.3075408935547,
              "p90": 1698.862890625,
              "p95": 1921.367578125,
              "p99": 2413.8885937499995,
              "maximum": 2848.7421875
            },
            "worst": {
              "sensor_index": 747,
              "sun_up_hour_index": 2716,
              "hour_of_year": 4911.5,
              "foton_lux": 22567.576171875,
              "radiance_lux": 19718.833984375
            },
            "compatibility_passed": false,
            "strict_passed": false,
            "passed": false
          },
          "metrics": {
            "da": {
              "mean_absolute_error_percentage_points": 10.780870056497175,
              "maximum_error_percentage_points": 38.41,
              "passed": false
            },
            "cda": {
              "mean_absolute_error_percentage_points": 11.538497175141243,
              "maximum_error_percentage_points": 33.58,
              "passed": false
            },
            "udi_lower": {
              "mean_absolute_error_percentage_points": 13.109299435028248,
              "maximum_error_percentage_points": 54.349999999999994,
              "passed": false
            },
            "udi": {
              "mean_absolute_error_percentage_points": 13.081830508474576,
              "maximum_error_percentage_points": 54.35,
              "passed": false
            },
            "udi_upper": {
              "mean_absolute_error_percentage_points": 0.3720564971751413,
              "maximum_error_percentage_points": 2.41,
              "passed": true
            }
          },
          "sda": {
            "foton_percent": 40.23484726586844,
            "radiance_percent": 31.78575360090522,
            "difference_percentage_points": 8.449093664963218,
            "passed": false
          }
        }
      ],
      "performance": {
        "foton_seconds": 1.6403391250642017,
        "radiance_seconds": 23.538626208086498,
        "speedup": 14.349853544562142,
        "passed": true
      },
      "versions": {
        "python": "3.13.5",
        "platform": "macOS-26.6.2-arm64-arm-64bit-Mach-O"
      },
      "folders": {
        "foton": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/annual",
        "radiance": "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/acceptance/mf1/stock/annual_daylight"
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
      "study_preparation_seconds": 0.10710437502712011,
      "weather_seconds": 0.12780370900873095,
      "metric_reduction_seconds": 1.2788206670666113,
      "write_seconds": 0.1263242500135675,
      "total_seconds": 1.5332347500370815,
      "cold_end_to_end_seconds": 1.6403391250642017,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.08564666705206037,
      "engine_upload_seconds": 0.000466792,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.200774666504003,
      "engine_annual_reduction_seconds": 0.01563108351547271,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 1.200774666504003
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.10710437502712011,
      "weather_seconds": 0.10894445795565844,
      "metric_reduction_seconds": 0.07677758298814297,
      "write_seconds": 0.1084645000519231,
      "total_seconds": 0.29439737496431917,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.29439737496431917,
      "raw_export_seconds": 0.08865304093342274,
      "engine_upload_seconds": 0.000306583,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.015596291632391512,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.05645812500733882,
      "full": 1.2010503340279683
    }
  },
  "elapsed_seconds": 2463.0897098750575,
  "result_class": "passed"
}
```
