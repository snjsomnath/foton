# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr40",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr40",
    "category": "teaching",
    "question": "How does a 40% window-to-wall ratio light the base room?",
    "interactions": [
      "multiple_bounces",
      "side_glazing",
      "window"
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 7.1982
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "120629bd9abf61ee5c3dbb05c25e3d9400f130cc15b477f0b4d616c0f5e86d00",
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
      "scene_fingerprint": 16461150684353540723,
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
      "scene_fingerprint": 16461150684353540723,
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
        "identifier": "teaching_wwr40_grid",
        "bias_percent": -0.05104456649172273,
        "rms_normalized_error_percent": 0.6896676693618947,
        "absolute_error": {
          "p95": 3.105087671428919e-07,
          "p99": 2.122711157426238e-05,
          "maximum": 0.00015173666179180145
        },
        "worst_index": [
          5,
          515,
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
        "identifier": "teaching_wwr40_grid",
        "bias_percent": 0.049862552443125846,
        "rms_normalized_error_percent": 1.239565309247768,
        "absolute_error": {
          "p95": 6.459862925112247e-05,
          "p99": 0.00014196336269378662,
          "maximum": 0.0006834119558334351
        },
        "worst_index": [
          20,
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
        "identifier": "teaching_wwr40_grid",
        "bias_percent": -0.004872610045011721,
        "rms_normalized_error_percent": 1.0166351587402658,
        "absolute_error": {
          "p95": 5.419025546871126e-05,
          "p99": 0.0001119859516620636,
          "maximum": 0.0005097240209579468
        },
        "worst_index": [
          13,
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
            "identifier": "teaching_wwr40_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02521027784081911,
                "cvrmse_percent": 23.153335560490746,
                "rms_normalized_rmse_percent": 6.756504886627975,
                "reference_energy": 14.11160678073611,
                "candidate_energy": 14.108049205458883,
                "relative_energy_error_percent": 0.025210277840819112,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.4873686056234916e-05,
                  "p95": 0.00010828895028680563,
                  "p99": 0.0002664912026375532,
                  "maximum": 0.0007461229106411338
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 154,
                  "rgb_channel": 0,
                  "reference": 0.0021442219149321318,
                  "candidate": 0.001398099004290998
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.14562776686495596,
                "cvrmse_percent": 121.40651504062204,
                "rms_normalized_rmse_percent": 5.20211557445306,
                "reference_energy": 4.853959115756762,
                "candidate_energy": 4.861027828021577,
                "relative_energy_error_percent": 0.145627766864956,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.99928093329072e-05,
                  "p95": 0.00021302956156432629,
                  "p99": 0.00045985745964571834,
                  "maximum": 0.0017162710428237915
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05024626851081848,
                  "candidate": 0.05196253955364227
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 128.81720904260874,
            "full": 246.48724996950477
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.47412497829646,
            "full": 235.3611660655588
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 127.9943329282105,
            "full": 257.97341705765575
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 125.08600007276982,
            "full": 238.71225002221763
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
            "identifier": "teaching_wwr40_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0467942071296844,
                "cvrmse_percent": 15.85706117659201,
                "rms_normalized_rmse_percent": 4.6354406238155335,
                "reference_energy": 14.107222497481416,
                "candidate_energy": 14.1006211345657,
                "relative_energy_error_percent": 0.0467942071296844,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3636379773961396e-05,
                  "p95": 8.798099588602781e-05,
                  "p99": 0.00018380099209025502,
                  "maximum": 0.00038339407183229923
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 312,
                  "rgb_channel": 0,
                  "reference": 0.003714614547789097,
                  "candidate": 0.004098008619621396
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1243681206343806,
                "cvrmse_percent": 39.27884459390282,
                "rms_normalized_rmse_percent": 2.2429062504088955,
                "reference_energy": 8.659625186636742,
                "candidate_energy": 8.670394999735343,
                "relative_energy_error_percent": 0.12436812063438059,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.57612120953861e-05,
                  "p95": 0.00012447955668903887,
                  "p99": 0.00026424642419442534,
                  "maximum": 0.0010357871651649475
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06485981866717339,
                  "candidate": 0.06382403150200844
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.60733299329877,
            "full": 2216.959834098816
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 171.84991599060595,
            "full": 2229.6527080470696
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.5022499570623,
            "full": 2159.35575007461
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.87270803190768,
            "full": 2190.779083990492
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
            "identifier": "teaching_wwr40_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07902333043404079,
                "cvrmse_percent": 16.24106640576688,
                "rms_normalized_rmse_percent": 4.745682037395751,
                "reference_energy": 14.099910708726838,
                "candidate_energy": 14.1110529277571,
                "relative_energy_error_percent": 0.07902333043404079,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3917469661682844e-05,
                  "p95": 8.879357483237982e-05,
                  "p99": 0.00018302648095414042,
                  "maximum": 0.00036109250504523516
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 311,
                  "rgb_channel": 0,
                  "reference": 0.0036005679285153747,
                  "candidate": 0.00396166043356061
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.00345171404725205,
                "cvrmse_percent": 39.7495807309243,
                "rms_normalized_rmse_percent": 2.2724958245275064,
                "reference_energy": 8.674952993803142,
                "candidate_energy": 8.674653559232063,
                "relative_energy_error_percent": 0.00345171404725205,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.7826516674831634e-05,
                  "p95": 0.0001258387346751988,
                  "p99": 0.0002609597868286073,
                  "maximum": 0.0008042193949222565
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06928474456071854,
                  "candidate": 0.06848052516579628
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.89379096310586,
            "full": 2342.181041953154
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.5245000468567,
            "full": 2332.204709062353
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.95316598471254,
            "full": 2415.332542033866
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.75591701176018,
            "full": 2309.560500085354
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
            "identifier": "teaching_wwr40_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.006104179880686918,
                "cvrmse_percent": 9.174326547571338,
                "rms_normalized_rmse_percent": 2.682461309409943,
                "reference_energy": 14.102996815688584,
                "candidate_energy": 14.102135943394387,
                "relative_energy_error_percent": 0.006104179880686917,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.920206705108285e-05,
                  "p95": 4.679849371314049e-05,
                  "p99": 0.00010427203960716724,
                  "maximum": 0.0001969535369426012
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 209,
                  "rgb_channel": 0,
                  "reference": 0.0009844802843872458,
                  "candidate": 0.0007875267474446446
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.001794496132754798,
                "cvrmse_percent": 23.11679513593847,
                "rms_normalized_rmse_percent": 1.3206420485967827,
                "reference_energy": 8.676686517326218,
                "candidate_energy": 8.676530814522213,
                "relative_energy_error_percent": 0.001794496132754798,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 2.8381824085954626e-05,
                  "p95": 7.26854195818305e-05,
                  "p99": 0.00014999863924458623,
                  "maximum": 0.0007485151290893555
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05728738009929657,
                  "candidate": 0.056538864970207214
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 248.1112499954179,
            "full": 4095.8071670029312
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 244.18816599063575,
            "full": 4108.05033298675
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 248.08758299332112,
            "full": 4094.7634170297533
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 247.54883302375674,
            "full": 4086.485292064026
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2639.022749965079,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_wwr40/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10382.027707993984,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      36,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.006814921795207477,
            "cvrmse_percent": 1.1690829033107903,
            "rms_normalized_rmse_percent": 0.3419140467397957,
            "reference_energy": 14.10339240577241,
            "candidate_energy": 14.102431270609486,
            "relative_energy_error_percent": 0.006814921795207477,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.759043127298355e-08,
              "p95": 2.867600414901972e-07,
              "p99": 1.0491407010704279e-05,
              "maximum": 5.996040999889374e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 319,
              "rgb_channel": 0,
              "reference": 0.00110444740857929,
              "candidate": 0.0010444869985803962,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.78048994017622,
            "cvrmse_percent": 50.6243657701806,
            "rms_normalized_rmse_percent": 2.892543116921948,
            "reference_energy": 8.675782661036612,
            "candidate_energy": 8.608069050135668,
            "relative_energy_error_percent": 0.78048994017622,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.499999554738679e-08,
              "p90": 5.2489918016362945e-05,
              "p95": 7.783528417348862e-05,
              "p99": 0.00014454714255407453,
              "maximum": 0.0027606189250946045
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06752976775169373,
              "candidate": 0.06476914882659912,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.30148039102580343,
            "cvrmse_percent": 19.288857314496184,
            "rms_normalized_rmse_percent": 2.8937171285021144,
            "reference_energy": 22.779175066809017,
            "candidate_energy": 22.710500320745155,
            "relative_energy_error_percent": 0.30148039102578,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.499999554738679e-08,
              "p90": 5.263173879939136e-05,
              "p95": 7.768842624500394e-05,
              "p99": 0.0001443331129848957,
              "maximum": 0.0027606189250946045
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06752976775169373,
              "candidate": 0.06476914882659912,
              "position": [
                4.5,
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
      36,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.006814921795207477,
            "cvrmse_percent": 1.1690829033107903,
            "rms_normalized_rmse_percent": 0.3419140467397957,
            "reference_energy": 14.10339240577241,
            "candidate_energy": 14.102431270609486,
            "relative_energy_error_percent": 0.006814921795207477,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.759043127298355e-08,
              "p95": 2.867600414901972e-07,
              "p99": 1.0491407010704279e-05,
              "maximum": 5.996040999889374e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 319,
              "rgb_channel": 0,
              "reference": 0.00110444740857929,
              "candidate": 0.0010444869985803962,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.97768385991559,
            "cvrmse_percent": 831.6680981488618,
            "rms_normalized_rmse_percent": 35.700179340348825,
            "reference_energy": 4.863929091166813,
            "candidate_energy": 8.608069050135668,
            "relative_energy_error_percent": 76.97768385991559,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001308115448409811,
              "p95": 0.0001915910979732871,
              "p99": 0.00033020973205566406,
              "maximum": 0.018516743555665016
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02503429539501667,
              "candidate": 0.043551038950681686,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.734883622919405,
            "cvrmse_percent": 213.2716430536281,
            "rms_normalized_rmse_percent": 35.700330811981836,
            "reference_energy": 18.967321496939224,
            "candidate_energy": 22.710500320745155,
            "relative_energy_error_percent": 19.734883622919405,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00013075100141577437,
              "p95": 0.00019163783872500062,
              "p99": 0.00033033883664757013,
              "maximum": 0.018516743555665016
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02503429539501667,
              "candidate": 0.043551038950681686,
              "position": [
                2.5,
                5.5,
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
      "bias_percent": 0.11346199109155428,
      "rms_normalized_error_percent": 0.3413204665293252,
      "absolute_error": {
        "p95": 0.21456925367495971,
        "p99": 0.2553723037025927,
        "maximum": 0.27627326216767223
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 28.069445229343483,
      "rms_normalized_to_uniform_percent": 0.3413204665293252
    },
    "overcast": {
      "bias_percent": 0.07827408451823586,
      "rms_normalized_error_percent": 0.2793706289099333,
      "absolute_error": {
        "p95": 0.12424105405807495,
        "p99": 0.13857606649398801,
        "maximum": 0.14282608032226562
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 17.953083038330078,
      "rms_normalized_to_uniform_percent": 0.1932540770672786
    },
    "horizon": {
      "bias_percent": 0.7694491120922273,
      "rms_normalized_error_percent": 2.5517574499118383,
      "absolute_error": {
        "p95": 0.17556947789585575,
        "p99": 0.24882928951325956,
        "maximum": 0.25148946026380337
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.4370000492703974,
      "rms_normalized_to_uniform_percent": 0.2218564624092418
    },
    "north": {
      "bias_percent": -40.85783677210602,
      "rms_normalized_error_percent": 198.93388275416632,
      "absolute_error": {
        "p95": 8.00751477072481e-05,
        "p99": 0.00018693942729441896,
        "maximum": 0.00023563707509310916
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.1355732567608356e-05,
      "rms_normalized_to_uniform_percent": 0.0001143728613460117
    },
    "east": {
      "bias_percent": -0.018191490565949195,
      "rms_normalized_error_percent": 0.5654717653718069,
      "absolute_error": {
        "p95": 0.09000921249389648,
        "p99": 0.12806758880615227,
        "maximum": 0.14581298828125
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.156425476074219,
      "rms_normalized_to_uniform_percent": 0.11440341825433785
    },
    "south": {
      "bias_percent": 0.15686046404779402,
      "rms_normalized_error_percent": 0.4120754707524718,
      "absolute_error": {
        "p95": 0.1856706142425537,
        "p99": 0.23881876468658436,
        "maximum": 0.2634897232055664
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 19.69602394104004,
      "rms_normalized_to_uniform_percent": 0.2669405118008808
    },
    "west": {
      "bias_percent": 0.10951698517220176,
      "rms_normalized_error_percent": 0.4950251864883912,
      "absolute_error": {
        "p95": 0.07328574359416962,
        "p99": 0.09802750647068018,
        "maximum": 0.11123418807983398
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.220324993133545,
      "rms_normalized_to_uniform_percent": 0.1009693354462521
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
        "identifier": "teaching_wwr40_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.020707752296265272,
          "cvrmse_percent": 2.966660294569431,
          "absolute_error_percentiles_lux": {
            "p50": 9.59478759765625,
            "p90": 111.98793945312501,
            "p95": 166.02904052734362,
            "p99": 298.7403808593749
          },
          "maximum_absolute_error_lux": 981.779296875,
          "worst": {
            "sensor_index": 6,
            "position": [
              1.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 5489.4462890625,
            "radiance_lux": 4507.6669921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15882420091324415,
            "maximum_error_percentage_points": 1.0961643835616428,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08451481891610078,
            "maximum_error_percentage_points": 0.49882059369456044,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07793759512937558,
            "maximum_error_percentage_points": 0.47054794520547816,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.17437214611872293,
            "maximum_error_percentage_points": 0.8790410958904076,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.15186073059360755,
            "maximum_error_percentage_points": 0.8753424657534197,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004925085616434899,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr40_grid",
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
      "study_preparation_seconds": 0.00741325004491955,
      "weather_seconds": 0.12686920806299895,
      "metric_reduction_seconds": 0.06930837500840425,
      "write_seconds": 0.0347877909662202,
      "total_seconds": 0.23113266692962497,
      "cold_end_to_end_seconds": 0.23854591697454453,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02554450009483844,
      "engine_upload_seconds": 0.000806167,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.020128375035710633,
      "engine_annual_reduction_seconds": 0.0014867499703541398,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.020128375035710633
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00741325004491955,
      "weather_seconds": 0.1064392919652164,
      "metric_reduction_seconds": 0.0435064589837566,
      "write_seconds": 0.028677791939117014,
      "total_seconds": 0.1792296669445932,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1792296669445932,
      "raw_export_seconds": 0.009827791014686227,
      "engine_upload_seconds": 6.7209e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0020787917310371995,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01664062507916242,
      "full": 0.011768665979616344
    }
  },
  "elapsed_seconds": 53.68443066708278,
  "result_class": "passed"
}
```
