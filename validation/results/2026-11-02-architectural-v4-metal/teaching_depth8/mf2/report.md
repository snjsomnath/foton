# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth8",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth8",
    "category": "teaching",
    "question": "How does daylight fall off in an 8 m deep room?",
    "interactions": [
      "multiple_bounces",
      "room",
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
    "shades": 0,
    "sensors": 48,
    "floor_area": 48.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "b5c3b391b2a6487108c0486a7eb4a717a8c559397b0dc58f7bfaafb8b3026994",
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
      "scene_fingerprint": 7711455366643186943,
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
      "scene_fingerprint": 7711455366643186943,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": -0.019574142116088912,
        "rms_normalized_error_percent": 0.7611222174833805,
        "absolute_error": {
          "p95": 6.59783836454153e-08,
          "p99": 9.677314665168524e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          23,
          543,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": 0.05413290867476838,
        "rms_normalized_error_percent": 1.5750930104115894,
        "absolute_error": {
          "p95": 2.713600406423211e-05,
          "p99": 0.00011115451343357563,
          "maximum": 0.0006365850567817688
        },
        "worst_index": [
          36,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": -0.0013203922251076052,
        "rms_normalized_error_percent": 1.3318170097070692,
        "absolute_error": {
          "p95": 2.188887447118759e-05,
          "p99": 8.961628191173077e-05,
          "maximum": 0.00044764578342437744
        },
        "worst_index": [
          21,
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.003515038035448716,
                "cvrmse_percent": 53.96985192498468,
                "rms_normalized_rmse_percent": 11.129892450911697,
                "reference_energy": 9.141292359785439,
                "candidate_energy": 9.14097103988206,
                "relative_energy_error_percent": 0.003515038035448716,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.878330118022859e-05,
                  "p99": 0.0003217696212232113,
                  "maximum": 0.0007444185321219265
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 0.001394663006067276,
                  "candidate": 0.0006502444739453495
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.6237193783076168,
                "cvrmse_percent": 190.72845990773476,
                "rms_normalized_rmse_percent": 7.055618033421893,
                "reference_energy": 3.2838481758020137,
                "candidate_energy": 3.304330173228692,
                "relative_energy_error_percent": 0.6237193783076167,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.665484422934242e-06,
                  "p95": 9.354599751532078e-05,
                  "p99": 0.0004185490615782328,
                  "maximum": 0.001027969759888947
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 360,
                  "rgb_channel": 0,
                  "reference": 0.0004904614761471748,
                  "candidate": -0.0005375082837417722
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.89295797608793,
            "full": 307.1964581031352
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 128.42966697644442,
            "full": 272.0767499413341
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 127.25266697816551,
            "full": 273.1412909924984
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.32220808882266,
            "full": 269.1986249992624
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11650320251714778,
                "cvrmse_percent": 24.193636119993638,
                "rms_normalized_rmse_percent": 4.99877894032982,
                "reference_energy": 9.151635973670636,
                "candidate_energy": 9.140974024678599,
                "relative_energy_error_percent": 0.11650320251714778,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.786105662584305e-05,
                  "p99": 0.00014001390081830323,
                  "maximum": 0.00033679339685477316
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 145,
                  "rgb_channel": 0,
                  "reference": 0.0005157975538168103,
                  "candidate": 0.0008525909506715834
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1717240091962045,
                "cvrmse_percent": 54.64602673195699,
                "rms_normalized_rmse_percent": 2.880653008549898,
                "reference_energy": 6.008097767965712,
                "candidate_energy": 5.997780421602133,
                "relative_energy_error_percent": 0.17172400919620448,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.984597990973725e-08,
                  "p90": 1.5259258361766115e-05,
                  "p95": 5.321833486959804e-05,
                  "p99": 0.00020743723143823445,
                  "maximum": 0.0006050150841474533
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.023305580019950867,
                  "candidate": 0.022700564935803413
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 171.8393329065293,
            "full": 2992.2617089468986
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.55675002280623,
            "full": 2985.513749998063
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.6840000068769,
            "full": 3029.842415940948
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 172.0653329975903,
            "full": 2942.3443749547005
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03315779414040551,
                "cvrmse_percent": 23.45026530334404,
                "rms_normalized_rmse_percent": 4.846393750580661,
                "reference_energy": 9.146118140976796,
                "candidate_energy": 9.143085489951773,
                "relative_energy_error_percent": 0.03315779414040551,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9177160942927e-05,
                  "p99": 0.00014019449008628726,
                  "maximum": 0.00037847855128347874
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 261,
                  "rgb_channel": 0,
                  "reference": 0.0034994945162907243,
                  "candidate": 0.0031210159650072455
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.052719665434998175,
                "cvrmse_percent": 55.6232130527259,
                "rms_normalized_rmse_percent": 2.9337281985367185,
                "reference_energy": 6.011258400441175,
                "candidate_energy": 6.014427515758321,
                "relative_energy_error_percent": 0.05271966543499816,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7343819652969614e-08,
                  "p90": 1.5363424608949572e-05,
                  "p95": 5.0334958359599113e-05,
                  "p99": 0.00021419709082692862,
                  "maximum": 0.0009204428642988205
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.044655684381723404,
                  "candidate": 0.04373524151742458
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.0302909333259,
            "full": 3142.4880831036717
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.24641604255885,
            "full": 3147.82958291471
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.40983295533806,
            "full": 3183.5717079229653
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 176.45537503995,
            "full": 3215.961124980822
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0165972987489988,
                "cvrmse_percent": 12.673820447604943,
                "rms_normalized_rmse_percent": 2.618919600698569,
                "reference_energy": 9.143909198224264,
                "candidate_energy": 9.142391556297298,
                "relative_energy_error_percent": 0.0165972987489988,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1288462448865175e-05,
                  "p99": 7.620151154696941e-05,
                  "maximum": 0.00020348618272691965
                },
                "worst": {
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "sky_patch_index": 314,
                  "rgb_channel": 0,
                  "reference": 0.0037333009531721473,
                  "candidate": 0.003936787135899067
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.027539917766579422,
                "cvrmse_percent": 32.08391945001059,
                "rms_normalized_rmse_percent": 1.6926866117026995,
                "reference_energy": 6.013266219508459,
                "candidate_energy": 6.014922268080397,
                "relative_energy_error_percent": 0.027539917766579426,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.1436690644804912e-08,
                  "p90": 1.0701671271817759e-05,
                  "p95": 2.963394217658788e-05,
                  "p99": 0.00012130301911383867,
                  "maximum": 0.0005451245233416557
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029040484689176083,
                  "candidate": 0.028495360165834427
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 241.5391249815002,
            "full": 5493.84079198353
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.71083405055106,
            "full": 5560.73687504977
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 239.2496659886092,
            "full": 5523.102457984351
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 445.95270801801234,
            "full": 5714.021916035563
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4791.101457900368,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_depth8/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 18509.75904194638,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.024598782884819842,
            "cvrmse_percent": 2.0845939484543328,
            "rms_normalized_rmse_percent": 0.43095403936503857,
            "reference_energy": 9.144224176256103,
            "candidate_energy": 9.141974808404484,
            "relative_energy_error_percent": 0.024598782884819845,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.4354237616062164e-08,
              "p99": 6.828822733950801e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2001865140525352,
            "cvrmse_percent": 67.36579680524977,
            "rms_normalized_rmse_percent": 3.5544922521948172,
            "reference_energy": 6.013020468848936,
            "candidate_energy": 5.940853008094592,
            "relative_energy_error_percent": 1.200186514052535,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.651326915132813e-05,
              "p95": 5.497204256244004e-05,
              "p99": 0.00010677144746296108,
              "maximum": 0.003039941191673279
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.035777200013399124,
              "candidate": 0.032737258821725845,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4909654119094426,
            "cvrmse_percent": 26.707248926578654,
            "rms_normalized_rmse_percent": 3.552179089460809,
            "reference_energy": 15.157244645105038,
            "candidate_energy": 15.082827816499076,
            "relative_energy_error_percent": 0.4909654119094426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.639727435711393e-05,
              "p95": 5.479569153976627e-05,
              "p99": 0.00010605006536934525,
              "maximum": 0.003039941191673279
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.035777200013399124,
              "candidate": 0.032737258821725845,
              "position": [
                5.5,
                1.5,
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
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.024598782884819842,
            "cvrmse_percent": 2.0845939484543328,
            "rms_normalized_rmse_percent": 0.43095403936503857,
            "reference_energy": 9.144224176256103,
            "candidate_energy": 9.141974808404484,
            "relative_energy_error_percent": 0.024598782884819845,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.4354237616062164e-08,
              "p99": 6.828822733950801e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.51834996475229,
            "cvrmse_percent": 819.475549695338,
            "rms_normalized_rmse_percent": 30.371930786724466,
            "reference_energy": 3.2909967375918256,
            "candidate_energy": 5.940853008094592,
            "relative_energy_error_percent": 80.51834996475229,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.499999628635123e-05,
              "p95": 0.00011705339420586824,
              "p99": 0.00022493524011224508,
              "maximum": 0.010917402803897858
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01838233694434166,
              "candidate": 0.029299739748239517,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.291193144005664,
            "cvrmse_percent": 216.87169158017954,
            "rms_normalized_rmse_percent": 30.371435651106815,
            "reference_energy": 12.435220913847928,
            "candidate_energy": 15.082827816499076,
            "relative_energy_error_percent": 21.29119314400566,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.490000280085951e-05,
              "p95": 0.00011687527876347303,
              "p99": 0.00022597214410779998,
              "maximum": 0.010917402803897858
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01838233694434166,
              "candidate": 0.029299739748239517,
              "position": [
                0.5,
                0.5,
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
      "bias_percent": 0.19997133843013123,
      "rms_normalized_error_percent": 0.4137562753429266,
      "absolute_error": {
        "p95": 0.19045551529626956,
        "p99": 0.2512886784266578,
        "maximum": 0.28232464280534764
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 13.782280179270087,
      "rms_normalized_to_uniform_percent": 0.4137562753429266
    },
    "overcast": {
      "bias_percent": 0.15959873503932825,
      "rms_normalized_error_percent": 0.35618834738037874,
      "absolute_error": {
        "p95": 0.11486024856567381,
        "p99": 0.16288235664367676,
        "maximum": 0.16355514526367188
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 8.7694730758667,
      "rms_normalized_to_uniform_percent": 0.25050931688449884
    },
    "horizon": {
      "bias_percent": 0.6863935091692197,
      "rms_normalized_error_percent": 3.084815070519274,
      "absolute_error": {
        "p95": 0.10692218934406518,
        "p99": 0.14675714187512984,
        "maximum": 0.1587707358909729
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.7671042687587475,
      "rms_normalized_to_uniform_percent": 0.2324361403084931
    },
    "north": {
      "bias_percent": -77.72006865182307,
      "rms_normalized_error_percent": 118.68784119330344,
      "absolute_error": {
        "p95": 3.300643675174793e-05,
        "p99": 6.35164503410124e-05,
        "maximum": 6.912522803759202e-05
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 5.977850833005505e-06,
      "rms_normalized_to_uniform_percent": 6.325962210864118e-05
    },
    "east": {
      "bias_percent": 0.10080825920553321,
      "rms_normalized_error_percent": 0.69523069177481,
      "absolute_error": {
        "p95": 0.08140833377838133,
        "p99": 0.09779377698898316,
        "maximum": 0.09878110885620117
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.5794646739959717,
      "rms_normalized_to_uniform_percent": 0.14909194184976252
    },
    "south": {
      "bias_percent": 0.20383339361671785,
      "rms_normalized_error_percent": 0.43034396820251225,
      "absolute_error": {
        "p95": 0.1257819652557373,
        "p99": 0.14698459625244142,
        "maximum": 0.15526962280273438
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 9.658995628356934,
      "rms_normalized_to_uniform_percent": 0.27638725548373333
    },
    "west": {
      "bias_percent": 0.35053962082155743,
      "rms_normalized_error_percent": 0.8553441035900222,
      "absolute_error": {
        "p95": 0.0822811126708984,
        "p99": 0.167558560371399,
        "maximum": 0.19783830642700195
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.6097121238708496,
      "rms_normalized_to_uniform_percent": 0.1849780690683136
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
        "identifier": "teaching_depth8_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.045308940499723796,
          "cvrmse_percent": 4.529297973315414,
          "absolute_error_percentiles_lux": {
            "p50": 6.4570159912109375,
            "p90": 81.47535400390626,
            "p95": 122.62589721679666,
            "p99": 224.6782763671875
          },
          "maximum_absolute_error_lux": 817.595703125,
          "worst": {
            "sensor_index": 6,
            "position": [
              0.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5745.5,
            "foton_lux": 17394.125,
            "radiance_lux": 16576.529296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.9302026255707766,
            "maximum_error_percentage_points": 5.204657534246575,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3245938497473233,
            "maximum_error_percentage_points": 2.0456122151411478,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.23859018264840212,
            "maximum_error_percentage_points": 1.1550684931506865,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.28871289954337764,
            "maximum_error_percentage_points": 1.2042465753424665,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.08251997716894986,
            "maximum_error_percentage_points": 0.6871232876712341,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 62.5,
          "radiance_percent": 62.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004853916952058057,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.008637667051516473,
      "weather_seconds": 0.11453454196453094,
      "metric_reduction_seconds": 0.07050999999046326,
      "write_seconds": 0.042327916948124766,
      "total_seconds": 0.22811216593254358,
      "cold_end_to_end_seconds": 0.23674983298406005,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.014367916039191186,
      "engine_upload_seconds": 0.0008359580000000001,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.019203708390705287,
      "engine_annual_reduction_seconds": 0.0021527500357478857,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.019203708390705287
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008637667051516473,
      "weather_seconds": 0.10878004203550518,
      "metric_reduction_seconds": 0.04366129101254046,
      "write_seconds": 0.03466954198665917,
      "total_seconds": 0.18728162499610335,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18728162499610335,
      "raw_export_seconds": 0.010470665991306305,
      "engine_upload_seconds": 6.6792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.002163624973036349,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014235166949220002,
      "full": 0.01893595897126943
    }
  },
  "elapsed_seconds": 76.90071616601199,
  "result_class": "passed"
}
```
