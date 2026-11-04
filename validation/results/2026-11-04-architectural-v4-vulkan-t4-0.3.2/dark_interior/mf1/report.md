# Foton report

Status: **passed**

```json
{
  "scene": "dark_interior",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "dark_interior",
    "category": "materials",
    "question": "How does a dark finish suppress indirect illumination?",
    "interactions": [
      "low_reflectance",
      "direct_indirect_separation"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0d4a84c87b59cfb8dd98bb35074f89432951d3568626cd5e73b7513a5935c454",
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
      "scene_fingerprint": 15135344251000409996,
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
      "scene_fingerprint": 15135344251000409996,
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
    "model_sha256": "7b42d19ab34b506135ecc31d7991bdcf8c1f1501fc44ac10eb6a2d9019eb1f43",
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
          "maximum": 0.0003254120238125324,
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05
        },
        "bias_percent": -0.07931914448047922,
        "identifier": "dark_interior_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0753890946716322,
        "worst_index": [
          9,
          72,
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
          "maximum": 0.0003019657451659441,
          "p95": 3.205028478987503e-05,
          "p99": 9.844452142715454e-05
        },
        "bias_percent": -0.005115461987773941,
        "identifier": "dark_interior_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0176795318751484,
        "worst_index": [
          24,
          47,
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
          "maximum": 0.0001729035284370184,
          "p95": 2.252713311463593e-05,
          "p99": 6.91520981490612e-05
        },
        "bias_percent": -0.002675966085883456,
        "identifier": "dark_interior_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6883450411876088,
        "worst_index": [
          25,
          47,
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
            "identifier": "dark_interior_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008344030939042568,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.430596255697309e-05,
                  "p99": 0.00042813364416360855
                },
                "candidate_energy": 6.0106778996487265,
                "cvrmse_percent": 19.393420155161287,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06970029184979407,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.006491357642517,
                "relative_energy_error_percent": 0.06970029184979408,
                "rms_normalized_rmse_percent": 3.9622831020251605,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003151573007926345,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.002317169914022088,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009527700021862984,
                  "p50": 0.0,
                  "p90": 3.6474375519901514e-06,
                  "p95": 0.0001401701458235038,
                  "p99": 0.0005174560355953872
                },
                "candidate_energy": 0.4261368414502549,
                "cvrmse_percent": 344.2915148354547,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6436674911549904,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4288975153267849,
                "relative_energy_error_percent": 0.6436674911549903,
                "rms_normalized_rmse_percent": 4.943661727009816,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0003791600465774536,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0005736099556088448,
                  "rgb_channel": 0,
                  "sky_patch_index": 117
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.92854104470462,
            "full": 225.28150002472103
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.50024995952845,
            "full": 230.31091690063477
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.29470898211002,
            "full": 222.845415933989
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.69212504662573,
            "full": 227.26133302785456
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
            "identifier": "dark_interior_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004773200489580631,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.669650079449637e-05,
                  "p99": 0.0001876835012808442
                },
                "candidate_energy": 6.017883255442939,
                "cvrmse_percent": 9.519689663250995,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0022651282375236205,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.017746945757608,
                "relative_energy_error_percent": 0.00226512823752362,
                "rms_normalized_rmse_percent": 1.9461316921987681,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013352729845792055,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.013830049894750118,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006325249560177326,
                  "p50": 0.0,
                  "p90": 3.07374466501642e-06,
                  "p95": 6.97128358297047e-05,
                  "p99": 0.00025961536448448896
                },
                "candidate_energy": 0.453443786868565,
                "cvrmse_percent": 171.53232227843498,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.19456977173315435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4525632356140825,
                "relative_energy_error_percent": 0.19456977173315435,
                "rms_normalized_rmse_percent": 2.598932069772151,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00036980025470256805,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": -0.00026272470131516457,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.49333294760436,
            "full": 779.8605000134557
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.38733401987702,
            "full": 761.7061670171097
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.34033298492432,
            "full": 792.9362080758438
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.92341700475663,
            "full": 779.8628329765052
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
            "identifier": "dark_interior_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00030958279967308044,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.385504871606827e-05,
                  "p99": 0.00014808261767029762
                },
                "candidate_energy": 6.015610548599398,
                "cvrmse_percent": 7.030630438512992,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02411760074147536,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.01706171952128,
                "relative_energy_error_percent": 0.024117600741475363,
                "rms_normalized_rmse_percent": 1.4387056020598308,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00580237980466336,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0061119626043364406,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00047022756189107895,
                  "p50": 2.7181954465049785e-09,
                  "p90": 2.232607641872164e-06,
                  "p95": 5.112998696858949e-05,
                  "p99": 0.0001948827994056046
                },
                "candidate_energy": 0.4561875473828909,
                "cvrmse_percent": 126.79851088963733,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9006794207302411,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.45211543668670906,
                "relative_energy_error_percent": 0.9006794207302413,
                "rms_normalized_rmse_percent": 1.9198336691020164,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0001772468676790595,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": -0.00029298069421201944,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.84383397735655,
            "full": 756.1567089287564
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.30645798891783,
            "full": 759.276874945499
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.56791704893112,
            "full": 783.9196249842644
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.54670796636492,
            "full": 780.2687080111355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.07304091379046,
            "full": 787.7469159429893
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.97899999190122,
            "full": 773.3175830217078
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.15204200241715,
            "full": 782.9926250269637
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.70945896208286,
            "full": 762.6400829758495
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
            "identifier": "dark_interior_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002523893490433693,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.15376091748476e-05,
                  "p99": 0.00011242064647376537
                },
                "candidate_energy": 6.015490914732254,
                "cvrmse_percent": 5.288431941757062,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02799186246498889,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.013807537997309,
                "relative_energy_error_percent": 0.027991862464988887,
                "rms_normalized_rmse_percent": 1.081064038176165,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018260099925100803,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.018007710576057434,
                  "rgb_channel": 0,
                  "sky_patch_index": 118
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004185587167739868,
                  "p50": 0.0,
                  "p90": 2.208944920312206e-06,
                  "p95": 4.236436798237239e-05,
                  "p99": 0.00014872988685965538
                },
                "candidate_energy": 0.45436248602630513,
                "cvrmse_percent": 92.63932171826784,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5701699210359937,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4569679799970139,
                "relative_energy_error_percent": 0.5701699210359937,
                "rms_normalized_rmse_percent": 1.41697771100322,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0001988448202610016,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.00021971389651298523,
                  "rgb_channel": 0,
                  "sky_patch_index": 118
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.33495796006173,
            "full": 1390.5737500172108
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.91875004861504,
            "full": 1372.3875830182806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.23041700106114,
            "full": 1377.9731669928879
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.70074996631593,
            "full": 1358.6639579152688
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
    "/content/suite-vulkan-0.3.2/dark_interior/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 788.2172499084845,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/dark_interior/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2859.660124988295,
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
        "identifier": "dark_interior_grid",
        "full_identifier": "dark_interior_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04581959575153105,
            "cvrmse_percent": 3.4361128668008196,
            "rms_normalized_rmse_percent": 0.7026163886487695,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350724828546,
            "relative_energy_error_percent": 0.04581959575153105,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.314149893820286e-05,
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
            "nmbe_percent": -1.0829619186303725,
            "cvrmse_percent": 58.23783755544355,
            "rms_normalized_rmse_percent": 0.8835963341540549,
            "reference_energy": 0.4532067294837816,
            "candidate_energy": 0.4482986731908021,
            "relative_energy_error_percent": 1.0829619186303725,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5000003905640824e-08,
              "p90": 3.833915116047137e-06,
              "p95": 2.0731371478177543e-05,
              "p99": 7.899757474660873e-05,
              "maximum": 0.00029024318791925907
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00401800312101841,
              "candidate": 0.0037277599330991507,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.11846519627542952,
            "cvrmse_percent": 3.896756137550059,
            "rms_normalized_rmse_percent": 0.8440747942760185,
            "reference_energy": 6.470314468754395,
            "candidate_energy": 6.462649398019348,
            "relative_energy_error_percent": 0.1184651962754295,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5000003905640824e-08,
              "p90": 3.849655513477046e-06,
              "p95": 1.9948731642216226e-05,
              "p99": 7.879338227212429e-05,
              "maximum": 0.00029024318791925907
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00401800312101841,
              "candidate": 0.0037277599330991507,
              "position": [
                3.5,
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
        "identifier": "dark_interior_grid",
        "full_identifier": "dark_interior_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04581959575153105,
            "cvrmse_percent": 3.4361128668008196,
            "rms_normalized_rmse_percent": 0.7026163886487695,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350724828546,
            "relative_energy_error_percent": 0.04581959575153105,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.314149893820286e-05,
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
            "nmbe_percent": 6.9940375535854,
            "cvrmse_percent": 124.63425959089608,
            "rms_normalized_rmse_percent": 1.7486237761399948,
            "reference_energy": 0.4189940705492887,
            "candidate_energy": 0.4482986731908021,
            "relative_energy_error_percent": 6.994037553585399,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.77718957781326e-06,
              "p95": 5.660673487000159e-05,
              "p99": 0.00017439387738704681,
              "maximum": 0.0003866457846015692
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 15,
              "rgb_channel": 0,
              "reference": -0.0003737758379429579,
              "candidate": 1.2869946658611298e-05,
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
            "nmbe_percent": 0.41247930787764114,
            "cvrmse_percent": 7.99319575746273,
            "rms_normalized_rmse_percent": 1.7226395690136118,
            "reference_energy": 6.4361018098199025,
            "candidate_energy": 6.462649398019348,
            "relative_energy_error_percent": 0.41247930787764114,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.609999895270448e-06,
              "p95": 5.403866234701115e-05,
              "p99": 0.0001728711649775505,
              "maximum": 0.0003809622721746564
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 47,
              "rgb_channel": 0,
              "reference": 0.0013267097529023886,
              "candidate": 0.001707672025077045,
              "position": [
                4.5,
                5.5,
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
      "bias_percent": 0.039987038964333387,
      "rms_normalized_error_percent": 0.11903988205007357,
      "absolute_error": {
        "p95": 0.04459500078392953,
        "p99": 0.0732988044986477,
        "maximum": 0.08477585225647033
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.100243696584755,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.11903988205007357
    },
    "overcast": {
      "bias_percent": 0.012608797550610753,
      "rms_normalized_error_percent": 0.11399257871882121,
      "absolute_error": {
        "p95": 0.03486347198486328,
        "p99": 0.051033782958984364,
        "maximum": 0.0544891357421875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.563780307769775,
      "reference_fraction_of_uniform": 0.6498635411262512,
      "rms_normalized_to_uniform_percent": 0.0812126533567215
    },
    "horizon": {
      "bias_percent": 0.6068305839714268,
      "rms_normalized_error_percent": 1.0461400211157368,
      "absolute_error": {
        "p95": 0.018126905921312303,
        "p99": 0.026105352960180295,
        "maximum": 0.029073740645285007
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.70748014357499,
      "reference_fraction_of_uniform": 0.07004584887533097,
      "rms_normalized_to_uniform_percent": 0.043658927789277165
    },
    "north": {
      "bias_percent": 0.0,
      "rms_normalized_error_percent": 0.0,
      "absolute_error": {
        "p95": 9.32674538489664e-07,
        "p99": 3.236380530324818e-06,
        "maximum": 4.476837602851447e-06
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.1302558650404535e-07,
      "reference_fraction_of_uniform": 2.1091134172479542e-08,
      "rms_normalized_to_uniform_percent": 3.974386160300851e-06
    },
    "east": {
      "bias_percent": 0.02154000918311553,
      "rms_normalized_error_percent": 0.14122767768056058,
      "absolute_error": {
        "p95": 0.013310343027114868,
        "p99": 0.019358766078948975,
        "maximum": 0.019467830657958984
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.016220808029175,
      "reference_fraction_of_uniform": 0.19962100684642792,
      "rms_normalized_to_uniform_percent": 0.029830164293800754
    },
    "south": {
      "bias_percent": 0.06723732116761777,
      "rms_normalized_error_percent": 0.12874557585279633,
      "absolute_error": {
        "p95": 0.02892613410949707,
        "p99": 0.04522976875305172,
        "maximum": 0.0533905029296875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.943057060241699,
      "reference_fraction_of_uniform": 0.687414824962616,
      "rms_normalized_to_uniform_percent": 0.08345941151163765
    },
    "west": {
      "bias_percent": -0.039890966159713284,
      "rms_normalized_error_percent": 0.160369800729004,
      "absolute_error": {
        "p95": 0.01636826992034912,
        "p99": 0.02016315460205078,
        "maximum": 0.020578384399414062
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9604517221450806,
      "reference_fraction_of_uniform": 0.19409945607185364,
      "rms_normalized_to_uniform_percent": 0.032434154247499146
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
        "identifier": "dark_interior_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.02902607379604583,
          "cvrmse_percent": 1.1090049019490236,
          "absolute_error_percentiles_lux": {
            "p50": 0.38701820373535156,
            "p90": 4.240289306640628,
            "p95": 11.881604003906247,
            "p99": 43.65644531249984
          },
          "maximum_absolute_error_lux": 282.736572265625,
          "worst": {
            "sensor_index": 22,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 3698.76904296875,
            "radiance_lux": 3981.505615234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07617960426179647,
            "maximum_error_percentage_points": 0.35999999999999943,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08594422327396639,
            "maximum_error_percentage_points": 0.4093391881414199,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13175799086757933,
            "maximum_error_percentage_points": 0.6273972602739661,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1340068493150684,
            "maximum_error_percentage_points": 0.6273972602739732,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01846270928462714,
            "maximum_error_percentage_points": 0.08191780821917805,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 25.0,
          "radiance_percent": 25.0,
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
      "maximum_error_percentage_points": 0.004998394691781982,
      "metrics": {
        "da": [
          {
            "identifier": "dark_interior_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "dark_interior_grid",
            "maximum_error_percentage_points": 0.004998394691781982,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "dark_interior_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "dark_interior_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "dark_interior_grid",
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
      "study_preparation_seconds": 0.3967777559996648,
      "weather_seconds": 0.2319655229998716,
      "metric_reduction_seconds": 0.16120576499997696,
      "write_seconds": 0.013422418000118341,
      "total_seconds": 0.4069114260000788,
      "cold_end_to_end_seconds": 0.8036891819997436,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001591446000020369,
      "engine_upload_seconds": 0.014099396,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.009488962,
      "engine_annual_reduction_seconds": 0.005914733,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.009488962
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3967777559996648,
      "weather_seconds": 0.2348083769998084,
      "metric_reduction_seconds": 0.15486288600004627,
      "write_seconds": 0.011908649999895715,
      "total_seconds": 0.4018634919998476,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4018634919998476,
      "raw_export_seconds": 0.0014003300002514152,
      "engine_upload_seconds": 0.014248577,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.8e-08,
      "engine_annual_reduction_seconds": 0.006142626,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01415988799999468,
      "full": 0.020480707999922743
    }
  },
  "elapsed_seconds": 2.819121295000059,
  "result_class": "passed"
}
```
