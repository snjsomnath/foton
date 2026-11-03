# Foton report

Status: **passed**

```json
{
  "scene": "u_shaped_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "u_shaped_plan",
    "category": "form",
    "question": "Do the wings of a U-shaped room occlude one another?",
    "interactions": [
      "concave_plan",
      "self_occlusion",
      "multiple_openings"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 3,
    "shades": 0,
    "sensors": 53,
    "floor_area": 63.0,
    "aperture_area": 9.0
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "4825b75370149c8775e3fc55d3a1a7eb010c36fab3bb3587ad3896dcdcf49cd0",
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
      "scene_fingerprint": 6169704301367242066,
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
      "scene_fingerprint": 6169704301367242066,
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
        "identifier": "u_shaped_plan_grid",
        "bias_percent": -0.013318048735264732,
        "rms_normalized_error_percent": 0.8538041494077923,
        "absolute_error": {
          "p95": 2.674838469829244e-07,
          "p99": 1.4548982107953634e-05,
          "maximum": 0.00019046594388782978
        },
        "worst_index": [
          47,
          281,
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
        "identifier": "u_shaped_plan_grid",
        "bias_percent": 0.09810016195590648,
        "rms_normalized_error_percent": 1.414289880264799,
        "absolute_error": {
          "p95": 3.365614684298629e-05,
          "p99": 0.00010796170681715012,
          "maximum": 0.0008016489446163177
        },
        "worst_index": [
          47,
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
        "identifier": "u_shaped_plan_grid",
        "bias_percent": 0.026005091158736875,
        "rms_normalized_error_percent": 1.1158375099377542,
        "absolute_error": {
          "p95": 2.822331152856346e-05,
          "p99": 8.742744103074074e-05,
          "maximum": 0.0006528608500957489
        },
        "worst_index": [
          47,
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
            "identifier": "u_shaped_plan_grid",
            "start_sensor_index": 0,
            "sensor_count": 53,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02947517022601119,
                "cvrmse_percent": 32.67074061705017,
                "rms_normalized_rmse_percent": 7.037013305337569,
                "reference_energy": 11.5626196235647,
                "candidate_energy": 11.559211521748068,
                "relative_energy_error_percent": 0.029475170226011194,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.677251508837793e-05,
                  "p99": 0.00022264663130044937,
                  "maximum": 0.0007109532598406076
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "sky_patch_index": 98,
                  "rgb_channel": 0,
                  "reference": 0.0005772712174803019,
                  "candidate": 0.0012882244773209095
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.15005304820616633,
                "cvrmse_percent": 168.28114244509825,
                "rms_normalized_rmse_percent": 5.4453293805659,
                "reference_energy": 3.5139807134333623,
                "candidate_energy": 3.5087078782594787,
                "relative_energy_error_percent": 0.1500530482061663,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.336884062970057e-05,
                  "p95": 9.324691200163202e-05,
                  "p99": 0.0003333494532853365,
                  "maximum": 0.0015984335914254189
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03261081874370575,
                  "candidate": 0.03101238515228033
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.6314169811085,
            "full": 313.56533302459866
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.23258394468576,
            "full": 323.6835409188643
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.59858304914087,
            "full": 333.7259590625763
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.9032090390101,
            "full": 315.44658390339464
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
            "identifier": "u_shaped_plan_grid",
            "start_sensor_index": 0,
            "sensor_count": 53,
            "stages": {
              "direct": {
                "nmbe_percent": -0.07011550754035903,
                "cvrmse_percent": 20.92952085345977,
                "rms_normalized_rmse_percent": 4.513662879430134,
                "reference_energy": 11.566196016239104,
                "candidate_energy": 11.558086319199205,
                "relative_energy_error_percent": 0.07011550754035902,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.233308718539761e-05,
                  "p99": 0.0001393071433994919,
                  "maximum": 0.0004008720861747861
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 257,
                  "rgb_channel": 0,
                  "reference": 0.0031431904062628746,
                  "candidate": 0.0035440624924376607
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.07203335185902751,
                "cvrmse_percent": 54.637636684712305,
                "rms_normalized_rmse_percent": 2.529454564559345,
                "reference_energy": 6.783720483092875,
                "candidate_energy": 6.788607024337594,
                "relative_energy_error_percent": 0.07203335185902751,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.091359988298791e-06,
                  "p90": 2.1719313735957257e-05,
                  "p95": 6.357156016747446e-05,
                  "p99": 0.00020801002392545342,
                  "maximum": 0.0006894189864397049
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06191273592412472,
                  "candidate": 0.06260215491056442
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 217.8837499814108,
            "full": 3750.0889590010047
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 197.2055829828605,
            "full": 3661.075875046663
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 211.55012503731996,
            "full": 3776.9329159054905
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.65083304792643,
            "full": 3737.6573339570314
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
            "identifier": "u_shaped_plan_grid",
            "start_sensor_index": 0,
            "sensor_count": 53,
            "stages": {
              "direct": {
                "nmbe_percent": -0.00993447311431049,
                "cvrmse_percent": 21.10626305241536,
                "rms_normalized_rmse_percent": 4.548921626832157,
                "reference_energy": 11.564640590351729,
                "candidate_energy": 11.563491704241514,
                "relative_energy_error_percent": 0.009934473114310489,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.254950854374303e-05,
                  "p99": 0.0001416460145264864,
                  "maximum": 0.0004448940744623542
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 362,
                  "rgb_channel": 0,
                  "reference": 0.0036458639660850167,
                  "candidate": 0.004090758040547371
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1642601601228769,
                "cvrmse_percent": 53.87276662868195,
                "rms_normalized_rmse_percent": 2.4954660908683355,
                "reference_energy": 6.807829843695313,
                "candidate_energy": 6.796647291493166,
                "relative_energy_error_percent": 0.16426016012287692,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.098418462992413e-06,
                  "p90": 2.138298805220984e-05,
                  "p95": 6.17498781139146e-05,
                  "p99": 0.00020363387739052996,
                  "maximum": 0.0008686929941177368
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05095197446644306,
                  "candidate": 0.050083281472325325
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 200.35704202018678,
            "full": 4020.3150409506634
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.4690419724211,
            "full": 4041.3820409448817
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.46274992171675,
            "full": 4043.3002919889987
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 199.68508393503726,
            "full": 4008.786000078544
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
            "identifier": "u_shaped_plan_grid",
            "start_sensor_index": 0,
            "sensor_count": 53,
            "stages": {
              "direct": {
                "nmbe_percent": 0.012332899052043085,
                "cvrmse_percent": 11.314663798800707,
                "rms_normalized_rmse_percent": 2.4391824106006856,
                "reference_energy": 11.562178533774429,
                "candidate_energy": 11.563604485581216,
                "relative_energy_error_percent": 0.012332899052043085,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.141243603546171e-05,
                  "p99": 7.731985533609986e-05,
                  "maximum": 0.00024280149955302477
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 139,
                  "rgb_channel": 0,
                  "reference": 0.0018280110089108348,
                  "candidate": 0.00158520950935781
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0030993831606618877,
                "cvrmse_percent": 31.70452197302196,
                "rms_normalized_rmse_percent": 1.47027390527343,
                "reference_energy": 6.808083807790709,
                "candidate_energy": 6.808294816393811,
                "relative_energy_error_percent": 0.0030993831606618877,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5107239050848875e-06,
                  "p90": 1.4467079381574877e-05,
                  "p95": 3.591747954487784e-05,
                  "p99": 0.00011529854964464903,
                  "maximum": 0.0009353049099445343
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 49,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.052279239520430565,
                  "candidate": 0.0532145444303751
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 311.36337493080646,
            "full": 7068.518250016496
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 313.8258330291137,
            "full": 7106.0511249816045
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 321.7115419683978,
            "full": 6941.392416949384
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 317.32341705355793,
            "full": 7060.649416060187
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 6783.887541969307,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/u_shaped_plan/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 25828.46220897045,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.17310682979761463,
            "cvrmse_percent": 3.2722368548880483,
            "rms_normalized_rmse_percent": 0.7055901092131215,
            "reference_energy": 11.56509473561431,
            "candidate_energy": 11.545074766754396,
            "relative_energy_error_percent": 0.17310682979761463,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.2469764593988233e-07,
              "p99": 1.6958691048785113e-05,
              "maximum": 0.00010280654532834888
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 165,
              "rgb_channel": 0,
              "reference": 0.00010280654532834888,
              "candidate": 0.0,
              "position": [
                7.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.0007328549001430647,
            "cvrmse_percent": 55.59170388613672,
            "rms_normalized_rmse_percent": 2.5766504505632932,
            "reference_energy": 6.805986091711707,
            "candidate_energy": 6.805936213709131,
            "relative_energy_error_percent": 0.0007328549001430647,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.162792487884872e-06,
              "p90": 4.187885133433156e-05,
              "p95": 5.9702689759433176e-05,
              "p99": 0.00010846959776245058,
              "maximum": 0.0019904673099517822
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.061832036823034286,
              "candidate": 0.059841569513082504,
              "position": [
                7.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.10924695749330149,
            "cvrmse_percent": 20.561354314334714,
            "rms_normalized_rmse_percent": 2.572414140477675,
            "reference_energy": 18.37108082732602,
            "candidate_energy": 18.351010980463528,
            "relative_energy_error_percent": 0.10924695749331116,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.113848485256312e-06,
              "p90": 4.179034203843912e-05,
              "p95": 5.953755444352281e-05,
              "p99": 0.0001083774259313941,
              "maximum": 0.0019904673099517822
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.061832036823034286,
              "candidate": 0.059841569513082504,
              "position": [
                7.5,
                3.5,
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
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.17310682979761463,
            "cvrmse_percent": 3.2722368548880483,
            "rms_normalized_rmse_percent": 0.7055901092131215,
            "reference_energy": 11.56509473561431,
            "candidate_energy": 11.545074766754396,
            "relative_energy_error_percent": 0.17310682979761463,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.2469764593988233e-07,
              "p99": 1.6958691048785113e-05,
              "maximum": 0.00010280654532834888
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 165,
              "rgb_channel": 0,
              "reference": 0.00010280654532834888,
              "candidate": 0.0,
              "position": [
                7.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 94.05804797009081,
            "cvrmse_percent": 1236.6378550178238,
            "rms_normalized_rmse_percent": 40.00041076150333,
            "reference_energy": 3.5071651420290983,
            "candidate_energy": 6.805936213709131,
            "relative_energy_error_percent": 94.05804797009081,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.7400000110210385e-06,
              "p90": 7.331999950110912e-05,
              "p95": 0.00010502812874619811,
              "p99": 0.00018781761173158884,
              "maximum": 0.021343592554330826
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034590136259794235,
              "candidate": 0.05593372881412506,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.75354677690684,
            "cvrmse_percent": 287.74211777256806,
            "rms_normalized_rmse_percent": 39.99885023835014,
            "reference_energy": 15.072259877643408,
            "candidate_energy": 18.351010980463528,
            "relative_energy_error_percent": 21.75354677690684,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.7199999951553764e-06,
              "p90": 7.293999806279317e-05,
              "p95": 0.00010519119205127936,
              "p99": 0.0001876900059869513,
              "maximum": 0.021343592554330826
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034590136259794235,
              "candidate": 0.05593372881412506,
              "position": [
                8.5,
                6.5,
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
      "bias_percent": 0.09124183548788273,
      "rms_normalized_error_percent": 0.43213586883607064,
      "absolute_error": {
        "p95": 0.23827325332391894,
        "p99": 0.33575773628064615,
        "maximum": 0.3775903483047003
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 15.54573777327055,
      "rms_normalized_to_uniform_percent": 0.43213586883607064
    },
    "overcast": {
      "bias_percent": 0.09019252898727581,
      "rms_normalized_error_percent": 0.38242012241112594,
      "absolute_error": {
        "p95": 0.1315171718597412,
        "p99": 0.23342247009277337,
        "maximum": 0.24483585357666016
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 10.31460189819336,
      "rms_normalized_to_uniform_percent": 0.2672116737654119
    },
    "horizon": {
      "bias_percent": 0.3465244080307762,
      "rms_normalized_error_percent": 3.7958422627391717,
      "absolute_error": {
        "p95": 0.11693670943302854,
        "p99": 0.16177472114503758,
        "maximum": 0.17336054904871734
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.3280692910896508,
      "rms_normalized_to_uniform_percent": 0.22880884468869847
    },
    "north": {
      "bias_percent": 0.07186376524437682,
      "rms_normalized_error_percent": 0.6091364435907385,
      "absolute_error": {
        "p95": 0.06027419567108154,
        "p99": 0.07103128433227537,
        "maximum": 0.07292008399963379
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.020787000656128,
      "rms_normalized_to_uniform_percent": 0.10434187291024143
    },
    "east": {
      "bias_percent": 0.017250788301415538,
      "rms_normalized_error_percent": 0.557171905398261,
      "absolute_error": {
        "p95": 0.14195432662963867,
        "p99": 0.16677597045898432,
        "maximum": 0.17614173889160156
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.748745441436768,
      "rms_normalized_to_uniform_percent": 0.24070291446089714
    },
    "south": {
      "bias_percent": 0.1848958748821774,
      "rms_normalized_error_percent": 0.48944532057634466,
      "absolute_error": {
        "p95": 0.117186164855957,
        "p99": 0.15662818908691398,
        "maximum": 0.1720867156982422
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.051132678985596,
      "rms_normalized_to_uniform_percent": 0.2105538567492675
    },
    "west": {
      "bias_percent": -0.013121093357508277,
      "rms_normalized_error_percent": 0.5235632341558537,
      "absolute_error": {
        "p95": 0.06564524173736572,
        "p99": 0.07423768997192381,
        "maximum": 0.07657194137573242
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.7933247089385986,
      "rms_normalized_to_uniform_percent": 0.1009752890241623
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
        "identifier": "u_shaped_plan_grid",
        "sensor_count": 53,
        "illuminance": {
          "nmbe_percent": 0.06811677555099827,
          "cvrmse_percent": 4.818125874660716,
          "absolute_error_percentiles_lux": {
            "p50": 7.164794921875,
            "p90": 76.27023773193363,
            "p95": 117.02200622558594,
            "p99": 226.48398437499972
          },
          "maximum_absolute_error_lux": 795.4287109375,
          "worst": {
            "sensor_index": 37,
            "position": [
              7.5,
              6.5,
              0.75
            ],
            "hour_of_year": 3224.5,
            "foton_lux": 3169.83447265625,
            "radiance_lux": 2374.40576171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7244275006461626,
            "maximum_error_percentage_points": 4.9089041095890416,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4929546143006053,
            "maximum_error_percentage_points": 2.635662712996414,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7398655983458263,
            "maximum_error_percentage_points": 5.070684931506854,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7893383303179112,
            "maximum_error_percentage_points": 5.06849315068493,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05707417937451531,
            "maximum_error_percentage_points": 0.4917808219178106,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 49.056603773584904,
          "radiance_percent": 49.056603773584904,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.0048287671232856155,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.009494374971836805,
      "weather_seconds": 0.12026991706807166,
      "metric_reduction_seconds": 0.07686720904894173,
      "write_seconds": 0.026518333004787564,
      "total_seconds": 0.2238393749576062,
      "cold_end_to_end_seconds": 0.233333749929443,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01464983297046274,
      "engine_upload_seconds": 0.000868375,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02191837492864579,
      "engine_annual_reduction_seconds": 0.002218791632913053,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02191837492864579
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009494374971836805,
      "weather_seconds": 0.11643041693605483,
      "metric_reduction_seconds": 0.04863870900589973,
      "write_seconds": 0.02182158292271197,
      "total_seconds": 0.18706470797769725,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18706470797769725,
      "raw_export_seconds": 0.012252792017534375,
      "engine_upload_seconds": 8.8083e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.002301375032402575,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013976624934002757,
      "full": 0.01794787496328354
    }
  },
  "elapsed_seconds": 99.41008237493224,
  "result_class": "passed"
}
```
