# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_context",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_context",
    "category": "context",
    "question": "How does enclosing context restrict a room's courtyard view?",
    "interactions": [
      "closed_context",
      "courtyard",
      "multiple_obstructions"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 18,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "1be6a5ebffee53f3c8296716c1f52f8b0c0edf5e661c0b47752c8088a09f1d52",
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
      "scene_fingerprint": 4828330442288497760,
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
      "scene_fingerprint": 4828330442288497760,
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
        "identifier": "courtyard_context_grid",
        "bias_percent": -0.16227101852864662,
        "rms_normalized_error_percent": 2.0425935331785077,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.62342912517488e-05,
          "maximum": 0.00046600401401519775
        },
        "worst_index": [
          17,
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
        "identifier": "courtyard_context_grid",
        "bias_percent": 0.0938462831702435,
        "rms_normalized_error_percent": 0.9898905285149974,
        "absolute_error": {
          "p95": 2.2861828256282017e-05,
          "p99": 5.869939923286438e-05,
          "maximum": 0.0005559362471103668
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
        "identifier": "courtyard_context_grid",
        "bias_percent": -0.010918170427729409,
        "rms_normalized_error_percent": 0.8342001210232052,
        "absolute_error": {
          "p95": 1.9293707373435583e-05,
          "p99": 5.9743295423686504e-05,
          "maximum": 0.0004455931484699249
        },
        "worst_index": [
          17,
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
            "identifier": "courtyard_context_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.14442030766961805,
                "cvrmse_percent": 22.303178563349736,
                "rms_normalized_rmse_percent": 1.6689579014530709,
                "reference_energy": 1.107251370778613,
                "candidate_energy": 1.1088504666149674,
                "relative_energy_error_percent": 0.14442030766961805,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.899943739175797e-06,
                  "maximum": 0.0003505549393594265
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.002498860005289316,
                  "candidate": 0.0028494149446487427
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.4374045770587553,
                "cvrmse_percent": 37.017136875373374,
                "rms_normalized_rmse_percent": 2.5456312425040464,
                "reference_energy": 1.7113106033605163,
                "candidate_energy": 1.7038252524537256,
                "relative_energy_error_percent": 0.4374045770587553,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.4944323740783148e-05,
                  "p95": 4.4854554698758844e-05,
                  "p99": 0.00015743839321658015,
                  "maximum": 0.0006631843280047178
                },
                "worst": {
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.008432879112660885,
                  "candidate": 0.007769694784656167
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.65337496902794,
            "full": 238.25512500479817
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 104.01983303017914,
            "full": 235.07775005418807
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 105.15433305408806,
            "full": 229.9829579424113
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 99.84408307354897,
            "full": 229.97187497094274
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
            "identifier": "courtyard_context_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.043480088831133225,
                "cvrmse_percent": 15.622327357524215,
                "rms_normalized_rmse_percent": 1.1687006058285236,
                "reference_energy": 1.1059213261351033,
                "candidate_energy": 1.1054404705600973,
                "relative_energy_error_percent": 0.043480088831133225,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.1370884496718645e-05,
                  "maximum": 0.0002919398248195648
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 118,
                  "rgb_channel": 0,
                  "reference": 0.01714698038995266,
                  "candidate": 0.017438920214772224
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.09410141842780972,
                "cvrmse_percent": 18.585851028120402,
                "rms_normalized_rmse_percent": 1.5702571026155796,
                "reference_energy": 2.574991871032296,
                "candidate_energy": 2.577414974907338,
                "relative_energy_error_percent": 0.09410141842780972,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.39213528629989e-06,
                  "p90": 2.0663901523221284e-05,
                  "p95": 3.299070231150834e-05,
                  "p99": 0.00011512046330608428,
                  "maximum": 0.0008902652189135551
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.01943602506071329,
                  "candidate": 0.020326290279626846
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.81966600939631,
            "full": 2388.598083052784
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 129.90312499459833,
            "full": 2431.0177919687703
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 127.97458400018513,
            "full": 2466.6391249047592
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.79966698307544,
            "full": 2421.6002919711173
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
            "identifier": "courtyard_context_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.01312010033778949,
                "cvrmse_percent": 15.103281819659715,
                "rms_normalized_rmse_percent": 1.1307643354069694,
                "reference_energy": 1.105467784396751,
                "candidate_energy": 1.1056128228792659,
                "relative_energy_error_percent": 0.01312010033778949,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.5109699234017171e-05,
                  "maximum": 0.00026841461658477783
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 116,
                  "rgb_channel": 0,
                  "reference": 0.01172061963006854,
                  "candidate": 0.011452205013483763
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.12666294103392128,
                "cvrmse_percent": 16.578026537286735,
                "rms_normalized_rmse_percent": 1.4005118292711247,
                "reference_energy": 2.581434206377157,
                "candidate_energy": 2.578164485890504,
                "relative_energy_error_percent": 0.12666294103392126,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.333589804948133e-06,
                  "p90": 1.992147917917464e-05,
                  "p95": 3.217002595192751e-05,
                  "p99": 9.572946873959154e-05,
                  "maximum": 0.0005247956141829491
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.01260883966460824,
                  "candidate": 0.01313363527879119
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.38574999943376,
            "full": 2592.868582927622
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.54779095202684,
            "full": 2578.41900002677
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.61379196774215,
            "full": 2591.982915997505
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.7650420134887,
            "full": 2588.642750051804
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
            "identifier": "courtyard_context_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0029306417386947355,
                "cvrmse_percent": 9.541505013316788,
                "rms_normalized_rmse_percent": 0.7139430738560991,
                "reference_energy": 1.1057771501564275,
                "candidate_energy": 1.105744743789728,
                "relative_energy_error_percent": 0.002930641738694735,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.109731763601303e-06,
                  "maximum": 0.00021332036703824997
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 117,
                  "rgb_channel": 0,
                  "reference": 0.017847035080194473,
                  "candidate": 0.017633714713156223
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.011502864870855617,
                "cvrmse_percent": 11.115667611485662,
                "rms_normalized_rmse_percent": 0.9391380716691277,
                "reference_energy": 2.579324678424964,
                "candidate_energy": 2.579027982192624,
                "relative_energy_error_percent": 0.011502864870855617,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6984624835458817e-06,
                  "p90": 1.4511308108922094e-05,
                  "p95": 2.2627476937486787e-05,
                  "p99": 6.447621854022145e-05,
                  "maximum": 0.000438617542386055
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.033823685720562935,
                  "candidate": 0.03426230326294899
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.61995793972164,
            "full": 4500.709124957211
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.38112500775605,
            "full": 4478.883208939806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 185.6834590435028,
            "full": 4518.230624962598
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 184.62562502827495,
            "full": 4567.372582969256
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 705.8881670236588,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_context/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2666.873458074406,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.060396282560217666,
            "cvrmse_percent": 13.500669362420979,
            "rms_normalized_rmse_percent": 1.0083603335273357,
            "reference_energy": 1.1059725623790655,
            "candidate_energy": 1.1053045960652526,
            "relative_energy_error_percent": 0.06039628256021766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.585122663527727e-05,
              "maximum": 0.00025024404749274254
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.004304821603000164,
              "candidate": 0.0040545775555074215,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9170337100773738,
            "cvrmse_percent": 42.211300337533196,
            "rms_normalized_rmse_percent": 3.5661073310097637,
            "reference_energy": 2.578964707662859,
            "candidate_energy": 2.5295250848459636,
            "relative_energy_error_percent": 1.9170337100773738,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.425002200354356e-06,
              "p90": 3.829001980193425e-05,
              "p95": 5.3360768993115886e-05,
              "p99": 0.0001300683943554759,
              "maximum": 0.001852935180068016
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02727862447500229,
              "candidate": 0.025425689294934273,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.3597949017497997,
            "cvrmse_percent": 29.420334055230697,
            "rms_normalized_rmse_percent": 3.551386823335755,
            "reference_energy": 3.6849372700419245,
            "candidate_energy": 3.634829680911216,
            "relative_energy_error_percent": 1.3597949017497997,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.417548663899652e-06,
              "p90": 3.792281495407224e-05,
              "p95": 5.259091540210643e-05,
              "p99": 0.00012203259393572807,
              "maximum": 0.001852935180068016
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02727862447500229,
              "candidate": 0.025425689294934273,
              "position": [
                3.5,
                2.5,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.060396282560217666,
            "cvrmse_percent": 13.500669362420979,
            "rms_normalized_rmse_percent": 1.0083603335273357,
            "reference_energy": 1.1059725623790655,
            "candidate_energy": 1.1053045960652526,
            "relative_energy_error_percent": 0.06039628256021766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.585122663527727e-05,
              "maximum": 0.00025024404749274254
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.004304821603000164,
              "candidate": 0.0040545775555074215,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 47.956048136627054,
            "cvrmse_percent": 396.41775415865834,
            "rms_normalized_rmse_percent": 27.268629444049925,
            "reference_energy": 1.7096462880044783,
            "candidate_energy": 2.5295250848459636,
            "relative_energy_error_percent": 47.95604813662707,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.818198471592041e-06,
              "p90": 6.362533895298839e-05,
              "p95": 9.701396938908142e-05,
              "p99": 0.00026390887796878815,
              "maximum": 0.006600493565201759
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02969500608742237,
              "candidate": 0.03629549965262413,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 29.095231778835387,
            "cvrmse_percent": 240.7032735610486,
            "rms_normalized_rmse_percent": 27.268409458859356,
            "reference_energy": 2.8156188503835438,
            "candidate_energy": 3.634829680911216,
            "relative_energy_error_percent": 29.095231778835387,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.8250001277192496e-06,
              "p90": 6.294999911915511e-05,
              "p95": 9.683724892965981e-05,
              "p99": 0.00026308000087738037,
              "maximum": 0.006600493565201759
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02969500608742237,
              "candidate": 0.03629549965262413,
              "position": [
                2.5,
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
      "bias_percent": -0.3564968775172218,
      "rms_normalized_error_percent": 0.6136802013099462,
      "absolute_error": {
        "p95": 0.09471526235634814,
        "p99": 0.11458511787308023,
        "maximum": 0.1218363433693197
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.7380214411790145,
      "rms_normalized_to_uniform_percent": 0.6136802013099462
    },
    "overcast": {
      "bias_percent": -0.3376880703978944,
      "rms_normalized_error_percent": 0.5720967193154128,
      "absolute_error": {
        "p95": 0.06617207825183868,
        "p99": 0.08881143033504482,
        "maximum": 0.09817886352539062
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.256758689880371,
      "rms_normalized_to_uniform_percent": 0.4867181520502446
    },
    "horizon": {
      "bias_percent": 1.4860443302638802,
      "rms_normalized_error_percent": 11.887179394197913,
      "absolute_error": {
        "p95": 0.02498325309229035,
        "p99": 0.02740123248302214,
        "maximum": 0.02834902898798458
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.050071136781158355,
      "rms_normalized_to_uniform_percent": 0.14316521543958013
    },
    "north": {
      "bias_percent": -0.22772338554256305,
      "rms_normalized_error_percent": 2.1987105380392333,
      "absolute_error": {
        "p95": 0.021950744092464447,
        "p99": 0.02839465141296386,
        "maximum": 0.030146360397338867
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.3521348237991333,
      "rms_normalized_to_uniform_percent": 0.16616266454929826
    },
    "east": {
      "bias_percent": -0.490599279535129,
      "rms_normalized_error_percent": 0.9604606056087504,
      "absolute_error": {
        "p95": 0.024198733270168304,
        "p99": 0.028592213243246078,
        "maximum": 0.02885018289089203
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.45321327447891235,
      "rms_normalized_to_uniform_percent": 0.14982841621532497
    },
    "south": {
      "bias_percent": -0.45202233167415395,
      "rms_normalized_error_percent": 0.5764750804050938,
      "absolute_error": {
        "p95": 0.034385353326797485,
        "p99": 0.04330226182937622,
        "maximum": 0.04349160194396973
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.0277049541473389,
      "rms_normalized_to_uniform_percent": 0.24501463570022974
    },
    "west": {
      "bias_percent": -0.03353342860563359,
      "rms_normalized_error_percent": 1.212912557771359,
      "absolute_error": {
        "p95": 0.025440283119678497,
        "p99": 0.031096661090850825,
        "maximum": 0.03231072425842285
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.3885810673236847,
      "rms_normalized_to_uniform_percent": 0.1566517025208876
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
        "identifier": "courtyard_context_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.8671459065921704,
          "cvrmse_percent": 7.404715530384947,
          "absolute_error_percentiles_lux": {
            "p50": 1.1187763214111328,
            "p90": 18.656058502197272,
            "p95": 33.16863174438475,
            "p99": 76.83093475341778
          },
          "maximum_absolute_error_lux": 272.7254638671875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 1289.19140625,
            "radiance_lux": 1561.9168701171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.501114916286149,
            "maximum_error_percentage_points": 1.9678082191780824,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.8022970561104817,
            "maximum_error_percentage_points": 2.4822655592525606,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.3112899543379009,
            "maximum_error_percentage_points": 4.111643835616434,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.3144101978691027,
            "maximum_error_percentage_points": 4.111643835616439,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015167427701674417,
            "maximum_error_percentage_points": 0.16602739726027593,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
      "maximum_error_percentage_points": 0.004931506849314982,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.0045903119648986745,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.0035616438356164126,
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
      "study_preparation_seconds": 0.00907658296637237,
      "weather_seconds": 0.10298433306161314,
      "metric_reduction_seconds": 0.04015533300116658,
      "write_seconds": 0.032212499994784594,
      "total_seconds": 0.17551999993156642,
      "cold_end_to_end_seconds": 0.1845965828979388,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010357250110246241,
      "engine_upload_seconds": 0.000302041,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02192708326037973,
      "engine_annual_reduction_seconds": 0.000355458352714777,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02192708326037973
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00907658296637237,
      "weather_seconds": 0.10022641601972282,
      "metric_reduction_seconds": 0.012357915984466672,
      "write_seconds": 0.022812833078205585,
      "total_seconds": 0.1355373749975115,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1355373749975115,
      "raw_export_seconds": 0.010169624933041632,
      "engine_upload_seconds": 6.65e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00036441662814468145,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02029608399607241,
      "full": 0.015360290999524295
    }
  },
  "elapsed_seconds": 46.36363645805977,
  "result_class": "passed"
}
```
