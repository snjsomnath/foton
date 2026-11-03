# Foton report

Status: **passed**

```json
{
  "scene": "teaching_obstruction30",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_obstruction30",
    "category": "teaching",
    "question": "How does a 30 degree obstruction angle reduce sky access?",
    "interactions": [
      "multiple_bounces",
      "obstruction",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "65d433815849d9b4b8c88ec65b1d31fd41770ec78b45f771527ae685571f46a9",
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
      "scene_fingerprint": 16536123132161339720,
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
      "scene_fingerprint": 16536123132161339720,
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
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": -0.2141990698903249,
        "rms_normalized_error_percent": 1.2974127623121974,
        "absolute_error": {
          "p95": 4.12575900554657e-07,
          "p99": 0.00013335076801013201,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          17,
          121,
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
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": -0.06490525983568414,
        "rms_normalized_error_percent": 0.771358444699986,
        "absolute_error": {
          "p95": 3.982601156167212e-05,
          "p99": 0.00012555229477584362,
          "maximum": 0.00067167729139328
        },
        "worst_index": [
          26,
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
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": 0.07313561118366467,
        "rms_normalized_error_percent": 0.6994872436306051,
        "absolute_error": {
          "p95": 3.470933916105408e-05,
          "p99": 0.00010966882109642029,
          "maximum": 0.0005955882370471954
        },
        "worst_index": [
          27,
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0014850232782594812,
                "cvrmse_percent": 19.845618885180816,
                "rms_normalized_rmse_percent": 3.414004826901339,
                "reference_energy": 5.071695103029924,
                "candidate_energy": 5.0717704188828066,
                "relative_energy_error_percent": 0.0014850232782594812,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.763205652125143e-07,
                  "p99": 0.00034379621502012014,
                  "maximum": 0.0013206209987401962
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 119,
                  "rgb_channel": 0,
                  "reference": 0.017012929543852806,
                  "candidate": 0.018333550542593002
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.38942916442465403,
                "cvrmse_percent": 44.718602207754344,
                "rms_normalized_rmse_percent": 3.0310917779543,
                "reference_energy": 3.170334998344387,
                "candidate_energy": 3.1579887892508722,
                "relative_energy_error_percent": 0.389429164424654,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.35330093750963e-07,
                  "p90": 4.552457721729297e-05,
                  "p95": 8.970903945737513e-05,
                  "p99": 0.0004654102958738804,
                  "maximum": 0.0014356961473822594
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 119,
                  "rgb_channel": 0,
                  "reference": 0.0007083555683493614,
                  "candidate": -0.000727340579032898
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 116.46804097108543,
            "full": 230.91962502803653
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 118.04137495346367,
            "full": 235.25883397087455
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 116.4240000071004,
            "full": 223.90854195691645
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.69475000537932,
            "full": 240.30341708566993
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10681081735313923,
                "cvrmse_percent": 7.205566363015326,
                "rms_normalized_rmse_percent": 1.2386743904163011,
                "reference_energy": 5.074647132771133,
                "candidate_energy": 5.069226860690833,
                "relative_energy_error_percent": 0.10681081735313923,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.881884135305598e-07,
                  "p99": 0.00013275397941470146,
                  "maximum": 0.0003178948536515236
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 100,
                  "rgb_channel": 0,
                  "reference": 0.013447870034724474,
                  "candidate": 0.013765764888375998
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.25850927083078906,
                "cvrmse_percent": 14.306916399625727,
                "rms_normalized_rmse_percent": 1.2811222508900735,
                "reference_energy": 5.085958286822898,
                "candidate_energy": 5.099105960504922,
                "relative_energy_error_percent": 0.25850927083078906,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.179996828199364e-06,
                  "p90": 3.4970893466379493e-05,
                  "p95": 6.312258719844973e-05,
                  "p99": 0.00023749098181724548,
                  "maximum": 0.0006595002487301826
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028675884939730167,
                  "candidate": 0.02933538518846035
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.14487502817065,
            "full": 2236.529916059226
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.18150009866804,
            "full": 2242.6162499468774
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.6347920037806,
            "full": 2258.760540978983
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.74304107110947,
            "full": 2263.2529159309343
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.02627415832259512,
                "cvrmse_percent": 7.624843365096374,
                "rms_normalized_rmse_percent": 1.3095163294892675,
                "reference_energy": 5.068053438655625,
                "candidate_energy": 5.069385027039971,
                "relative_energy_error_percent": 0.026274158322595123,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.860668797043276e-07,
                  "p99": 0.00013228249736130238,
                  "maximum": 0.0003730445168912411
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.01149166515097022,
                  "candidate": 0.011864709667861462
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.17367763568920383,
                "cvrmse_percent": 13.333223729528445,
                "rms_normalized_rmse_percent": 1.194427666978391,
                "reference_energy": 5.093575806471261,
                "candidate_energy": 5.084729404438544,
                "relative_energy_error_percent": 0.17367763568920383,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.1034672828318435e-06,
                  "p90": 3.497439502098132e-05,
                  "p95": 5.664896671078164e-05,
                  "p99": 0.000207266682991758,
                  "maximum": 0.0007019797340035439
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029475269839167595,
                  "candidate": 0.02877329010516405
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.21791593264788,
            "full": 2388.9403329230845
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.95966702513397,
            "full": 2393.76179210376
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.08787498623133,
            "full": 2386.278749909252
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.31770805176347,
            "full": 2741.201166063547
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05765065951805302,
                "cvrmse_percent": 5.113274669383463,
                "rms_normalized_rmse_percent": 0.8791830768029953,
                "reference_energy": 5.068350522370565,
                "candidate_energy": 5.0712724598733985,
                "relative_energy_error_percent": 0.05765065951805302,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.3978652684014095e-07,
                  "p99": 8.050633914535865e-05,
                  "maximum": 0.00032551027834415436
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.011417599860578775,
                  "candidate": 0.01174311013892293
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.08695867662763139,
                "cvrmse_percent": 9.876723949953488,
                "rms_normalized_rmse_percent": 0.8858986435252377,
                "reference_energy": 5.097705814723184,
                "candidate_energy": 5.093272917208331,
                "relative_energy_error_percent": 0.08695867662763139,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.020367098040879e-06,
                  "p90": 2.5303896109107882e-05,
                  "p95": 4.20672718064452e-05,
                  "p99": 0.0001498199999332428,
                  "maximum": 0.00048372335731983185
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043755656108260155,
                  "candidate": 0.04423937946557999
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.01604196801782,
            "full": 4122.6679580286145
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 209.95837496593595,
            "full": 4163.730041938834
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 206.683833966963,
            "full": 4194.162165978923
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.20741706341505,
            "full": 4158.488542074338
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 879.1267500491813,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2907.740625087172,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      36,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18712955930342395,
            "cvrmse_percent": 4.83698174035112,
            "rms_normalized_rmse_percent": 0.8320721092586214,
            "reference_energy": 5.07558257445271,
            "candidate_energy": 5.066084659149055,
            "relative_energy_error_percent": 0.18712955930342395,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.880130290985107e-07,
              "p99": 8.323788642883301e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.064774309394324,
            "cvrmse_percent": 28.000659575594852,
            "rms_normalized_rmse_percent": 2.5081407999345844,
            "reference_energy": 5.089718264174197,
            "candidate_energy": 5.035524251676719,
            "relative_energy_error_percent": 1.0647743093943238,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5542054370598635e-05,
              "p90": 6.310781463980675e-05,
              "p95": 8.907148876460266e-05,
              "p99": 0.0001899278722703457,
              "maximum": 0.002013683319091797
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027262333780527115,
              "candidate": 0.025248650461435318,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6265621530757921,
            "cvrmse_percent": 13.988780266522836,
            "rms_normalized_rmse_percent": 2.5025916580492176,
            "reference_energy": 10.165300838626907,
            "candidate_energy": 10.101608910825775,
            "relative_energy_error_percent": 0.6265621530757922,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5574362805637065e-05,
              "p90": 6.249222133192234e-05,
              "p95": 8.759568445384491e-05,
              "p99": 0.00017319519247394055,
              "maximum": 0.002013683319091797
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027262333780527115,
              "candidate": 0.025248650461435318,
              "position": [
                1.5,
                4.5,
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
      36,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18712955930342395,
            "cvrmse_percent": 4.83698174035112,
            "rms_normalized_rmse_percent": 0.8320721092586214,
            "reference_energy": 5.07558257445271,
            "candidate_energy": 5.066084659149055,
            "relative_energy_error_percent": 0.18712955930342395,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.880130290985107e-07,
              "p99": 8.323788642883301e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.336298063743214,
            "cvrmse_percent": 396.0724860757158,
            "rms_normalized_rmse_percent": 26.805891721414305,
            "reference_energy": 3.16031206502754,
            "candidate_energy": 5.035524251676719,
            "relative_energy_error_percent": 59.33629806374321,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.6933073968393728e-05,
              "p90": 0.00018538000585976988,
              "p95": 0.0002905243003851863,
              "p99": 0.000563653651624918,
              "maximum": 0.011523149907588959
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01868264004588127,
              "candidate": 0.03020578995347023,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.65344996525193,
            "cvrmse_percent": 151.95339880067087,
            "rms_normalized_rmse_percent": 26.800741886960882,
            "reference_energy": 8.23589463948025,
            "candidate_energy": 10.101608910825775,
            "relative_energy_error_percent": 22.65344996525193,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.6937315851682797e-05,
              "p90": 0.00018227999680675566,
              "p95": 0.0002860192049411121,
              "p99": 0.0005478974035213469,
              "maximum": 0.011523149907588959
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01868264004588127,
              "candidate": 0.03020578995347023,
              "position": [
                0.5,
                3.5,
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
      "bias_percent": -0.10240387378121936,
      "rms_normalized_error_percent": 0.41097213453726694,
      "absolute_error": {
        "p95": 0.14439330068384004,
        "p99": 0.1952182865596114,
        "maximum": 0.20651727549628163
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 10.545461783706081,
      "rms_normalized_to_uniform_percent": 0.41097213453726694
    },
    "overcast": {
      "bias_percent": -0.0851651218196513,
      "rms_normalized_error_percent": 0.3909495149469147,
      "absolute_error": {
        "p95": 0.10323089361190796,
        "p99": 0.15052764415740957,
        "maximum": 0.17078161239624023
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.753107070922852,
      "rms_normalized_to_uniform_percent": 0.29946049138541714
    },
    "horizon": {
      "bias_percent": 0.20625173710666136,
      "rms_normalized_error_percent": 6.9760878936473265,
      "absolute_error": {
        "p95": 0.04567831461353216,
        "p99": 0.04899344035948514,
        "maximum": 0.05074056544296862
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.32714137282524125,
      "rms_normalized_to_uniform_percent": 0.13751948261962063
    },
    "north": {
      "bias_percent": -0.16266193622980743,
      "rms_normalized_error_percent": 2.6683398575972346,
      "absolute_error": {
        "p95": 0.032568350434303284,
        "p99": 0.049523705244064305,
        "maximum": 0.056211233139038086
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.5995408296585083,
      "rms_normalized_to_uniform_percent": 0.0905419816283922
    },
    "east": {
      "bias_percent": -0.10839488096430924,
      "rms_normalized_error_percent": 0.7817609932767717,
      "absolute_error": {
        "p95": 0.08672142028808594,
        "p99": 0.09962453842163084,
        "maximum": 0.10400581359863281
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.1854279041290283,
      "rms_normalized_to_uniform_percent": 0.17610886061981232
    },
    "south": {
      "bias_percent": -0.13959340314164612,
      "rms_normalized_error_percent": 0.37596629249691377,
      "absolute_error": {
        "p95": 0.06759918481111526,
        "p99": 0.09421147704124445,
        "maximum": 0.10736393928527832
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.510997295379639,
      "rms_normalized_to_uniform_percent": 0.19848022642242005
    },
    "west": {
      "bias_percent": -0.21905832473746947,
      "rms_normalized_error_percent": 0.6559482309911226,
      "absolute_error": {
        "p95": 0.046779654920101166,
        "p99": 0.07691913396120068,
        "maximum": 0.08674860000610352
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.1179795265197754,
      "rms_normalized_to_uniform_percent": 0.14056098911602322
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
        "identifier": "teaching_obstruction30_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.2145729970159603,
          "cvrmse_percent": 3.149896726045228,
          "absolute_error_percentiles_lux": {
            "p50": 3.9056339263916016,
            "p90": 44.33249511718751,
            "p95": 68.89676513671874,
            "p99": 126.30415771484371
          },
          "maximum_absolute_error_lux": 439.96044921875,
          "worst": {
            "sensor_index": 34,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 7690.90087890625,
            "radiance_lux": 8130.861328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7613051750380517,
            "maximum_error_percentage_points": 2.6312328767123283,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.52464248333931,
            "maximum_error_percentage_points": 2.0888143108941293,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5364155251141545,
            "maximum_error_percentage_points": 3.174383561643836,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5263470319634701,
            "maximum_error_percentage_points": 3.174383561643836,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027560882800609025,
            "maximum_error_percentage_points": 0.19671232876712352,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 27.77777777777778,
          "radiance_percent": 27.77777777777778,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004574325770548171,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.0088478330289945,
      "weather_seconds": 0.10986812494229525,
      "metric_reduction_seconds": 0.04627137503121048,
      "write_seconds": 0.02181954204570502,
      "total_seconds": 0.17816062504425645,
      "cold_end_to_end_seconds": 0.18700845807325095,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010302542010322213,
      "engine_upload_seconds": 0.000299,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.017675208393484354,
      "engine_annual_reduction_seconds": 0.00039425003342330456,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.017675208393484354
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0088478330289945,
      "weather_seconds": 0.10896229196805507,
      "metric_reduction_seconds": 0.012756124953739345,
      "write_seconds": 0.02169433410745114,
      "total_seconds": 0.1439702910138294,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1439702910138294,
      "raw_export_seconds": 0.01089383289217949,
      "engine_upload_seconds": 6.8792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00035633333027362823,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01771141600329429,
      "full": 0.021682457998394966
    }
  },
  "elapsed_seconds": 44.650953999953344,
  "result_class": "passed"
}
```
