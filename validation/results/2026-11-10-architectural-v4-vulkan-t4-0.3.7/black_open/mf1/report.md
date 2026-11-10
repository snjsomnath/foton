# Foton report

Status: **passed**

```json
{
  "scene": "black_open",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "black_open",
    "category": "controls",
    "question": "Is direct sky integration correct without glazing or reflections?",
    "interactions": [
      "open_aperture",
      "direct_sky"
    ],
    "room_count": 1,
    "include_glazing": false,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "4c8f19c3bbe26c085a566b1494c43a9b1819ed80c509c65496f09439cc7d749a",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 17021673487271919861,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 17021673487271919861,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "22ef95e4598ad81e217be9f93f838977f1b277a150a1fde1ced5629a765d95dd",
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
          "maximum": 0.0007113460451364517,
          "p95": 4.942947998642849e-06,
          "p99": 0.00017957016825675964
        },
        "bias_percent": -0.08911790088889197,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.143469017229677,
        "worst_index": [
          23,
          121,
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
          "maximum": 0.0005694134160876274,
          "p95": 7.854029536247253e-05,
          "p99": 0.0002945251762866974
        },
        "bias_percent": 0.041399152407360716,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5424772433100162,
        "worst_index": [
          23,
          15,
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
          "maximum": 0.0006523597985506058,
          "p95": 7.354281842708588e-05,
          "p99": 0.0002790670841932297
        },
        "bias_percent": -0.02690248437844523,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4476641710387226,
        "worst_index": [
          17,
          100,
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007110908627510071,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.901014760136604e-05
                },
                "candidate_energy": 11.384541239138343,
                "cvrmse_percent": 4.344673572940953,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03122072165826873,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.388096685106575,
                "relative_energy_error_percent": 0.03122072165826873,
                "rms_normalized_rmse_percent": 0.8764575104236358,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.03176198899745941,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.03247307986021042,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011851508170366287,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.000158016849309206,
                  "p99": 0.0003950502723455429
                },
                "candidate_energy": -0.0049775787483667955,
                "cvrmse_percent": 37986.71686395252,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 49.998701213061736,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": -0.0033184145650011487,
                "relative_energy_error_percent": 49.998701213061736,
                "rms_normalized_rmse_percent": 2.2334358455833008,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00047405995428562164,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": -0.0007110908627510071,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.21212506480515,
            "full": 103.15199999604374
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 100.02124996390194,
            "full": 96.79120895452797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 98.79754099529237,
            "full": 110.10270903352648
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.87366705015302,
            "full": 116.2552919704467
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000510508893057704,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.853943970985711e-05,
                  "p99": 0.0002356213517487049
                },
                "candidate_energy": 11.384306928590377,
                "cvrmse_percent": 6.253250951330094,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03001955271238971,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.380890436186746,
                "relative_energy_error_percent": 0.030019552712389715,
                "rms_normalized_rmse_percent": 1.2598663722362318,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004594579106196761,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.004084070213139057,
                  "rgb_channel": 0,
                  "sky_patch_index": 21
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00047123897820711136,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.853936403989792e-05,
                  "p99": 0.00023562181740999222
                },
                "candidate_energy": 0.0012959130617673509,
                "cvrmse_percent": 199513.583881626,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -466.6695961706545,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": -0.00035342801129445434,
                "relative_energy_error_percent": 466.6695961706545,
                "rms_normalized_rmse_percent": 1.2483252361115105,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00047123897820711136,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.49924997705966,
            "full": 128.04754101671278
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.27716698404402,
            "full": 136.27158396411687
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.28908307105303,
            "full": 133.99791694246233
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.06729098036885,
            "full": 146.52183291036636
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007853980641812086,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.854029536247253e-05,
                  "p99": 0.0004712305963039398
                },
                "candidate_energy": 11.388076936884318,
                "cvrmse_percent": 10.598123260166169,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.013451145319167135,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.386545316127012,
                "relative_energy_error_percent": 0.013451145319167135,
                "rms_normalized_rmse_percent": 2.1380255688359937,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0032201320864260197,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.002434734022244811,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003926990320906043,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.927014768123627e-05,
                  "p99": 0.0002356152981519699
                },
                "candidate_energy": 0.00011783617810579017,
                "cvrmse_percent": 73754.06041627139,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -85.71214550353868,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0008247296900663059,
                "relative_energy_error_percent": 85.71214550353868,
                "rms_normalized_rmse_percent": 1.078133855724036,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0003926990320906043,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.7560410350561,
            "full": 134.5654169563204
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.63508397620171,
            "full": 134.963791933842
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.51837503816932,
            "full": 136.1762919696048
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.88466603402048,
            "full": 118.56008297763765
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023535965010523796,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9225281216204164e-05,
                  "p99": 0.00011768005788326263
                },
                "candidate_energy": 11.384424705222045,
                "cvrmse_percent": 3.0350522593898845,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01601857106228573,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.386248619548496,
                "relative_energy_error_percent": 0.01601857106228573,
                "rms_normalized_rmse_percent": 0.6122862546209806,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012630860321223736,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.012866219971328974,
                  "rgb_channel": 0,
                  "sky_patch_index": 41
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002942010760307312,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9224978536367416e-05,
                  "p99": 0.00011768005788326263
                },
                "candidate_energy": 0.0,
                "cvrmse_percent": 29655.542427081713,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -100.0,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": -0.001235631576491869,
                "relative_energy_error_percent": 100.0,
                "rms_normalized_rmse_percent": 0.6494399798451534,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": -0.0002942010760307312,
                  "rgb_channel": 0,
                  "sky_patch_index": 132
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.56849995162338,
            "full": 178.9035419933498
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.98308292590082,
            "full": 180.0996249075979
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.74862495996058,
            "full": 184.2628330923617
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.9608329096809,
            "full": 176.7043749568984
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan-0.3.7/black_open/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 800.5276669282466,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2892.7377921063453,
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
        "identifier": "black_open_grid",
        "full_identifier": "black_open_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05473943560389833,
            "cvrmse_percent": 3.7106217787550277,
            "rms_normalized_rmse_percent": 0.7488101232708605,
            "reference_energy": 11.391959422919172,
            "candidate_energy": 11.38572352862684,
            "relative_energy_error_percent": 0.05473943560389833,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.44705006480217e-06,
              "p99": 0.000112973153591156,
              "maximum": 0.0006512640975415707
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.00463413679972291,
              "candidate": 0.003982872702181339,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -100.0,
            "cvrmse_percent": 6886.361241961005,
            "rms_normalized_rmse_percent": 0.8837152898819988,
            "reference_energy": -0.007240609006657905,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 100.0,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.864157479256369e-05,
              "p99": 0.00016103871166706085,
              "maximum": 0.000515379011631012
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": -0.000515379011631012,
              "candidate": 0.0,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": 0.00882511663879693,
            "cvrmse_percent": 3.9896537652218957,
            "rms_normalized_rmse_percent": 0.80501688276056,
            "reference_energy": 11.384718813912514,
            "candidate_energy": 11.38572352862684,
            "relative_energy_error_percent": 0.008825116638796928,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.764157881960268e-05,
              "p99": 0.00015208590775728226,
              "maximum": 0.0005128934280946851
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.0021378318779170513,
              "candidate": 0.0016249384498223662,
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
        "identifier": "black_open_grid",
        "full_identifier": "black_open_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05473943560389833,
            "cvrmse_percent": 3.7106217787550277,
            "rms_normalized_rmse_percent": 0.7488101232708605,
            "reference_energy": 11.391959422919172,
            "candidate_energy": 11.38572352862684,
            "relative_energy_error_percent": 0.05473943560389833,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.44705006480217e-06,
              "p99": 0.000112973153591156,
              "maximum": 0.0006512640975415707
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.00463413679972291,
              "candidate": 0.003982872702181339,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -100.0,
            "cvrmse_percent": 13627.366425746852,
            "rms_normalized_rmse_percent": 2.3639598235220958,
            "reference_energy": -0.009788428258616477,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 100.0,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.00011214932892471536,
              "p99": 0.0004684682935476303,
              "maximum": 0.001038532704114914
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": -0.001038532704114914,
              "candidate": 0.0,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": 0.03121139164006519,
            "cvrmse_percent": 11.643838141457453,
            "rms_normalized_rmse_percent": 2.3487482029473172,
            "reference_energy": 11.382170994660555,
            "candidate_energy": 11.38572352862684,
            "relative_energy_error_percent": 0.03121139164006519,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.00010949407587759164,
              "p99": 0.0004702056758105755,
              "maximum": 0.0010327305644750595
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 0.02603377401828766,
              "candidate": 0.027066504582762718,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      }
    ]
  },
  "controlled_skies": {
    "uniform": {
      "bias_percent": 0.00882511663875645,
      "rms_normalized_error_percent": 0.1049873413846808,
      "absolute_error": {
        "p95": 0.08970022814253831,
        "p99": 0.11257741410016028,
        "maximum": 0.12118061334670216
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.86911749449045,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1049873413846808
    },
    "overcast": {
      "bias_percent": 0.015939599375456543,
      "rms_normalized_error_percent": 0.11700553352963793,
      "absolute_error": {
        "p95": 0.07300472259521484,
        "p99": 0.10015621185302732,
        "maximum": 0.1063232421875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.480623245239258,
      "reference_fraction_of_uniform": 0.6614311933517456,
      "rms_normalized_to_uniform_percent": 0.08468368994511852
    },
    "horizon": {
      "bias_percent": 0.0387625736169426,
      "rms_normalized_error_percent": 0.8838057286678945,
      "absolute_error": {
        "p95": 0.028105886807031077,
        "p99": 0.03629084403763151,
        "maximum": 0.03774132293817711
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1770768595616656,
      "reference_fraction_of_uniform": 0.06238112937212658,
      "rms_normalized_to_uniform_percent": 0.03286270006871009
    },
    "north": {
      "bias_percent": 0.0,
      "rms_normalized_error_percent": 0.0,
      "absolute_error": {
        "p95": 0.0,
        "p99": 0.0,
        "maximum": 0.0
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0,
      "reference_fraction_of_uniform": 0.0,
      "rms_normalized_to_uniform_percent": 0.0
    },
    "east": {
      "bias_percent": 0.002714554460999855,
      "rms_normalized_error_percent": 0.1474293052921571,
      "absolute_error": {
        "p95": 0.028331995010375977,
        "p99": 0.03743348121643066,
        "maximum": 0.03797721862792969
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8980119228363037,
      "reference_fraction_of_uniform": 0.20658156275749207,
      "rms_normalized_to_uniform_percent": 0.032665515562216904
    },
    "south": {
      "bias_percent": 0.007542531194412032,
      "rms_normalized_error_percent": 0.10865819437151776,
      "absolute_error": {
        "p95": 0.05721092224121094,
        "p99": 0.08341789245605469,
        "maximum": 0.0845794677734375
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.458555221557617,
      "reference_fraction_of_uniform": 0.6602616906166077,
      "rms_normalized_to_uniform_percent": 0.06763255296881077
    },
    "west": {
      "bias_percent": -0.04146264333335034,
      "rms_normalized_error_percent": 0.17006151253555324,
      "absolute_error": {
        "p95": 0.030610322952270508,
        "p99": 0.0513102531433105,
        "maximum": 0.06175041198730469
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7882630825042725,
      "reference_fraction_of_uniform": 0.20076525211334229,
      "rms_normalized_to_uniform_percent": 0.03608661549060228
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
        "identifier": "black_open_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.03363136487414367,
          "cvrmse_percent": 1.4213712361960202,
          "absolute_error_percentiles_lux": {
            "p50": 0.5108642578125,
            "p90": 8.272241210937501,
            "p95": 26.56622924804669,
            "p99": 102.69690795898411
          },
          "maximum_absolute_error_lux": 815.0087890625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 8531.6953125,
            "radiance_lux": 9346.7041015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07315829528158362,
            "maximum_error_percentage_points": 0.27767123287671325,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0931884852220426,
            "maximum_error_percentage_points": 0.562683377935425,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12412100456620997,
            "maximum_error_percentage_points": 0.9589041095890423,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14206240487062574,
            "maximum_error_percentage_points": 0.9589041095890423,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.036632420091324086,
            "maximum_error_percentage_points": 0.2976712328767128,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 38.888888888888886,
          "difference_percentage_points": 2.7777777777777715,
          "tolerance_percentage_points": 2.7777777777777777,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004801476883557143,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.3554382219999752,
      "weather_seconds": 0.23724096000000827,
      "metric_reduction_seconds": 0.08556100600003447,
      "write_seconds": 0.012116591999983939,
      "total_seconds": 0.33532463300002746,
      "cold_end_to_end_seconds": 0.6907628550000027,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001488793000135047,
      "engine_upload_seconds": 0.022834851,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.003795455,
      "engine_annual_reduction_seconds": 0.006188384,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.003795455
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3554382219999752,
      "weather_seconds": 0.22548039399998743,
      "metric_reduction_seconds": 0.07984669500001473,
      "write_seconds": 0.012403231999996933,
      "total_seconds": 0.3179953779999778,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3179953779999778,
      "raw_export_seconds": 0.001525913000023138,
      "engine_upload_seconds": 0.023271177,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 3.8e-08,
      "engine_annual_reduction_seconds": 0.006345016,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02066874000001917,
      "full": 0.020066223999947397
    }
  },
  "elapsed_seconds": 2.573556988000064,
  "result_class": "passed"
}
```
