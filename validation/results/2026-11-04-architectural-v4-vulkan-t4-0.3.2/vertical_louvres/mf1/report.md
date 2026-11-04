# Foton report

Status: **passed**

```json
{
  "scene": "vertical_louvres",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "vertical_louvres",
    "category": "shading",
    "question": "How do repeated vertical blades screen oblique sky directions?",
    "interactions": [
      "louvres",
      "azimuth_mask",
      "small_gaps"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 5,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "a0e86f8240399679533bdbed7ff51db5df942dbf0b45e0393437b48c1691c7b9",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 3773948157984095676,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 3773948157984095676,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "03fd66d43132917beb8d3fbd505eb50f3ce96c124a8afc3befa7608317acf207",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0004275278188288212,
          "p95": 6.867700722068517e-06,
          "p99": 0.0001316908746957779
        },
        "bias_percent": 0.02146804367684222,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1434349461035613,
        "worst_index": [
          23,
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
          "maximum": 0.0003169747069478035,
          "p95": 2.7187447267351657e-05,
          "p99": 0.00010866858065128326
        },
        "bias_percent": -0.09653700312126223,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4278390597617736,
        "worst_index": [
          30,
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
          "maximum": 0.0004093814641237259,
          "p95": 2.4320273951161646e-05,
          "p99": 9.521259926259518e-05
        },
        "bias_percent": 0.0009074836011365231,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.275672480909427,
        "worst_index": [
          16,
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006313854828476906,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.3703804001561e-05,
                  "p99": 0.00018483598250895739
                },
                "candidate_energy": 2.625873091606991,
                "cvrmse_percent": 21.57077923153617,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07536965400323264,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6278536958452605,
                "relative_energy_error_percent": 0.07536965400323263,
                "rms_normalized_rmse_percent": 3.094621530415742,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015390555374324322,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.016021940857172012,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007980444934219122,
                  "p50": 0.0,
                  "p90": 2.189075621572556e-05,
                  "p95": 6.0285371000645295e-05,
                  "p99": 0.00032434193417429924
                },
                "candidate_energy": 0.9594260628181672,
                "cvrmse_percent": 96.03723461610099,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.13960604976145452,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9580885132915427,
                "relative_energy_error_percent": 0.13960604976145452,
                "rms_normalized_rmse_percent": 4.323589102722639,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -9.259534999728203e-05,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0007054491434246302,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              }
            },
            "start_sensor_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.91154091991484,
            "full": 230.68195790983737
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.38679201435298,
            "full": 226.02825006470084
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.92049997951835,
            "full": 238.01504203584045
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.34054106008261,
            "full": 234.6277500037104
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003608320839703083,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1889740673941525e-05,
                  "p99": 0.00014052796177566051
                },
                "candidate_energy": 2.622699013698366,
                "cvrmse_percent": 15.377269479887955,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.3629795969557563,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6132135815723814,
                "relative_energy_error_percent": 0.3629795969557564,
                "rms_normalized_rmse_percent": 2.196495911879783,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007944476790726185,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.008305308874696493,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006864771712571383,
                  "p50": 1.9136227962235353e-06,
                  "p90": 2.2064796212362126e-05,
                  "p95": 4.507136582105882e-05,
                  "p99": 0.00021204643417149782
                },
                "candidate_energy": 1.7996774750584237,
                "cvrmse_percent": 35.14700519475354,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5096230991019346,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8088960270510128,
                "relative_energy_error_percent": 0.5096230991019346,
                "rms_normalized_rmse_percent": 2.6450504365057994,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 9.125215001404285e-05,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0007777293212711811,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              }
            },
            "start_sensor_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.87454210594296,
            "full": 2395.079582929611
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.76441698893905,
            "full": 2385.7804998988286
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.04845900367945,
            "full": 2402.3056250298396
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.30695904511958,
            "full": 2373.4051670180634
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003743270062841475,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1658159766957295e-05,
                  "p99": 0.0001263124286197126
                },
                "candidate_energy": 2.620461514940871,
                "cvrmse_percent": 14.414906483725488,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.2007210099999695,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6257319105516217,
                "relative_energy_error_percent": 0.2007210099999695,
                "rms_normalized_rmse_percent": 2.063240256106057,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019417955190874636,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002316122525371611,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004523796960711479,
                  "p50": 1.9110515054876487e-06,
                  "p90": 2.2604327568842564e-05,
                  "p95": 4.807451123269846e-05,
                  "p99": 0.00021809741156175733
                },
                "candidate_energy": 1.7925478481603783,
                "cvrmse_percent": 34.879336130136714,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.25922465927096083,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7972066509777704,
                "relative_energy_error_percent": 0.25922465927096083,
                "rms_normalized_rmse_percent": 2.6086780095899815,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.010723960120230913,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.011176339816302061,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.77045796532184,
            "full": 2555.5936249438673
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.253791003488,
            "full": 2568.266666959971
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.45995801966637,
            "full": 2532.157124951482
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.89654188603163,
            "full": 2555.110750021413
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019821012392640114,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0909319462371053e-05,
                  "p99": 6.859004497528076e-05
                },
                "candidate_energy": 2.621720715424999,
                "cvrmse_percent": 7.482421061419735,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04705483246547707,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6229549424788274,
                "relative_energy_error_percent": 0.04705483246547708,
                "rms_normalized_rmse_percent": 1.0726068025874866,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015324275009334087,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.015126064885407686,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00039296504110097885,
                  "p50": 1.5125472145882668e-06,
                  "p90": 1.5442361473105848e-05,
                  "p95": 3.19810249493457e-05,
                  "p99": 0.00013623948325403035
                },
                "candidate_energy": 1.7973747108852116,
                "cvrmse_percent": 22.073867094549637,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18935563363945057,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7939777130193733,
                "relative_energy_error_percent": 0.18935563363945057,
                "rms_normalized_rmse_percent": 1.6469478667603472,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.011462474707514048,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.011855439748615026,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.87104203086346,
            "full": 4489.683917025104
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.88062492664903,
            "full": 4404.243792057969
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.79287503659725,
            "full": 4576.972917071544
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.81762498617172,
            "full": 4427.78475000523
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
    "/content/suite-vulkan-0.3.2/vertical_louvres/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 812.6266249455512,
      "invocation_count": 3,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2810.0842089625075,
      "invocation_count": 3,
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
        "identifier": "vertical_louvres_grid",
        "full_identifier": "vertical_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.27189702291671225,
            "cvrmse_percent": 9.838959954895653,
            "rms_normalized_rmse_percent": 1.4091272454048949,
            "reference_energy": 2.625669855974593,
            "candidate_energy": 2.6185307378045763,
            "relative_energy_error_percent": 0.2718970229167123,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.6237430069595255e-06,
              "p99": 6.179232150316238e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4084000836689791,
            "cvrmse_percent": 29.364175457762165,
            "rms_normalized_rmse_percent": 2.189135561320762,
            "reference_energy": 1.7923441782555436,
            "candidate_energy": 1.7850242431319119,
            "relative_energy_error_percent": 0.40840008366897906,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.583085461083101e-06,
              "p90": 2.384645995334722e-05,
              "p95": 3.995329934696192e-05,
              "p99": 0.00012686068657785654,
              "maximum": 0.0007452676072716713
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01273052766919136,
              "candidate": 0.01198526006191969,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3272749516326,
            "cvrmse_percent": 11.41648714840099,
            "rms_normalized_rmse_percent": 2.0979397861446034,
            "reference_energy": 4.418014034230136,
            "candidate_energy": 4.403554980936488,
            "relative_energy_error_percent": 0.32727495163260006,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5958197511499748e-06,
              "p90": 2.384645995334722e-05,
              "p95": 3.940740098187222e-05,
              "p99": 0.0001036218018271029,
              "maximum": 0.0007452676072716713
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01273052766919136,
              "candidate": 0.01198526006191969,
              "position": [
                2.5,
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
        "identifier": "vertical_louvres_grid",
        "full_identifier": "vertical_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.27189702291671225,
            "cvrmse_percent": 9.838959954895653,
            "rms_normalized_rmse_percent": 1.4091272454048949,
            "reference_energy": 2.625669855974593,
            "candidate_energy": 2.6185307378045763,
            "relative_energy_error_percent": 0.2718970229167123,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.6237430069595255e-06,
              "p99": 6.179232150316238e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 85.94955257629266,
            "cvrmse_percent": 467.6694246356888,
            "rms_normalized_rmse_percent": 21.106902151596838,
            "reference_energy": 0.9599508137560804,
            "candidate_energy": 1.7850242431319119,
            "relative_energy_error_percent": 85.94955257629265,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.9899999794433825e-06,
              "p90": 0.00011092999920947477,
              "p95": 0.000196567009697901,
              "p99": 0.00038715275877621025,
              "maximum": 0.004095524549484253
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014315364882349968,
              "candidate": 0.01841088943183422,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.81151260953805,
            "cvrmse_percent": 125.11688612248228,
            "rms_normalized_rmse_percent": 21.09195364742052,
            "reference_energy": 3.585620669730673,
            "candidate_energy": 4.403554980936488,
            "relative_energy_error_percent": 22.811512609538045,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.9899999794433825e-06,
              "p90": 0.00011054000060539693,
              "p95": 0.00019566922128433356,
              "p99": 0.0003852800000458956,
              "maximum": 0.004095524549484253
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014315364882349968,
              "candidate": 0.01841088943183422,
              "position": [
                3.5,
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
      "bias_percent": 0.10763158608617338,
      "rms_normalized_error_percent": 0.3934924308422082,
      "absolute_error": {
        "p95": 0.07693764627360278,
        "p99": 0.10457715206438123,
        "maximum": 0.11714416105142966
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.367102663643276,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3934924308422082
    },
    "overcast": {
      "bias_percent": 0.003695995607013987,
      "rms_normalized_error_percent": 0.325237467904859,
      "absolute_error": {
        "p95": 0.048697441816329956,
        "p99": 0.05148220658302307,
        "maximum": 0.05170154571533203
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.63485050201416,
      "reference_fraction_of_uniform": 0.6772463321685791,
      "rms_normalized_to_uniform_percent": 0.24076248183916513
    },
    "horizon": {
      "bias_percent": 2.2696992575242336,
      "rms_normalized_error_percent": 4.2529884320351865,
      "absolute_error": {
        "p95": 0.04636724988773297,
        "p99": 0.08024377665020313,
        "maximum": 0.09362601389644865
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4318590127659178,
      "reference_fraction_of_uniform": 0.0804640864597818,
      "rms_normalized_to_uniform_percent": 0.22664461285723778
    },
    "north": {
      "bias_percent": -8.235114313332703,
      "rms_normalized_error_percent": 10.312743393798806,
      "absolute_error": {
        "p95": 0.0020475564524531364,
        "p99": 0.0027956920908764004,
        "maximum": 0.002824069932103157
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.008129969239234924,
      "reference_fraction_of_uniform": 0.0015147780068218708,
      "rms_normalized_to_uniform_percent": 0.010479791195691071
    },
    "east": {
      "bias_percent": 0.29706959915812503,
      "rms_normalized_error_percent": 0.8184225958650744,
      "absolute_error": {
        "p95": 0.019488748162984848,
        "p99": 0.027998612821102133,
        "maximum": 0.030039161443710327
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6311161518096924,
      "reference_fraction_of_uniform": 0.11758972704410553,
      "rms_normalized_to_uniform_percent": 0.0893460284787652
    },
    "south": {
      "bias_percent": 0.2309574802772486,
      "rms_normalized_error_percent": 0.482972261572704,
      "absolute_error": {
        "p95": 0.061899811029434204,
        "p99": 0.09603883624076837,
        "maximum": 0.11360311508178711
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9089863300323486,
      "reference_fraction_of_uniform": 0.7283234000205994,
      "rms_normalized_to_uniform_percent": 0.3283310916234044
    },
    "west": {
      "bias_percent": -0.47283863299078527,
      "rms_normalized_error_percent": 1.0184173507737893,
      "absolute_error": {
        "p95": 0.02380676567554474,
        "p99": 0.02852502167224883,
        "maximum": 0.030851364135742188
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6600058078765869,
      "reference_fraction_of_uniform": 0.12297245860099792,
      "rms_normalized_to_uniform_percent": 0.11439983226172841
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
        "identifier": "vertical_louvres_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.03671348890468477,
          "cvrmse_percent": 3.0966915497028102,
          "absolute_error_percentiles_lux": {
            "p50": 1.7083454132080078,
            "p90": 17.560176086425788,
            "p95": 28.60647354125976,
            "p99": 61.85100982666003
          },
          "maximum_absolute_error_lux": 254.36328125,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 10341.240234375,
            "radiance_lux": 10086.876953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5287138508371385,
            "maximum_error_percentage_points": 1.504794520547943,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.34568742007051345,
            "maximum_error_percentage_points": 1.4480370917821404,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.45086377473363826,
            "maximum_error_percentage_points": 1.7569863013698637,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4446347031963476,
            "maximum_error_percentage_points": 1.7565753424657515,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.016122526636225334,
            "maximum_error_percentage_points": 0.08657534246575341,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 16.666666666666668,
          "radiance_percent": 16.666666666666668,
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
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.00489458476027238,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.3828388760002781,
      "weather_seconds": 0.21541942000021663,
      "metric_reduction_seconds": 0.14887073599993528,
      "write_seconds": 0.011860175000037998,
      "total_seconds": 0.37658540100028404,
      "cold_end_to_end_seconds": 0.7594242770005621,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016125659999488562,
      "engine_upload_seconds": 0.013438958,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010943107,
      "engine_annual_reduction_seconds": 0.005811168,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010943107
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3828388760002781,
      "weather_seconds": 0.22028326000008747,
      "metric_reduction_seconds": 0.1435818869999821,
      "write_seconds": 0.011999810999895999,
      "total_seconds": 0.3761580899999899,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3761580899999899,
      "raw_export_seconds": 0.0014562619999196613,
      "engine_upload_seconds": 0.014509804,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.2e-08,
      "engine_annual_reduction_seconds": 0.005979361,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013849437999851943,
      "full": 0.02074776400013434
    }
  },
  "elapsed_seconds": 2.731240433000039,
  "result_class": "passed"
}
```
