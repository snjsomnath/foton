# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 8,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 9.6
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c32a490ba2a16059a6cabc0f4db5cd8a2c55a338c6dc3a2086bab4493cc09800",
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
      "scene_fingerprint": 12112216450189513340,
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
      "scene_fingerprint": 12112216450189513340,
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
    "model_sha256": "f531a21d60afaa1c32abd8ac8222729e859983cccbc4dbe490b6df200829363a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006667673587799072,
          "p95": 3.8819824112579226e-05,
          "p99": 0.00016517454059794545
        },
        "bias_percent": 0.04968068407318133,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7073717148806293,
        "worst_index": [
          10,
          129,
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
          "maximum": 0.0006571747362613678,
          "p95": 7.234625809360296e-05,
          "p99": 0.00016740686260163784
        },
        "bias_percent": 0.042063657689435784,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0415928891016948,
        "worst_index": [
          14,
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
          "maximum": 0.0005466453731060028,
          "p95": 6.316494545899332e-05,
          "p99": 0.00013961270451545715
        },
        "bias_percent": -0.0037154660406607254,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9218088889876728,
        "worst_index": [
          25,
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007891680579632521,
                  "p50": 0.0,
                  "p90": 4.704833554569632e-05,
                  "p95": 0.00013773207319900393,
                  "p99": 0.00030848695314489305
                },
                "candidate_energy": 11.690483363467123,
                "cvrmse_percent": 10.962065898273124,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06754729838124414,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.698385306696025,
                "relative_energy_error_percent": 0.06754729838124414,
                "rms_normalized_rmse_percent": 2.8026357132721085,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001960841938853264,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002750009996816516,
                  "rgb_channel": 0,
                  "sky_patch_index": 29
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010751942172646523,
                  "p50": 2.562430836405838e-07,
                  "p90": 9.652553126215935e-05,
                  "p95": 0.00022299864576780237,
                  "p99": 0.0004994440823793411
                },
                "candidate_energy": 3.7165591889841103,
                "cvrmse_percent": 58.41038603984983,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04888314210370943,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7147433057351797,
                "relative_energy_error_percent": 0.04888314210370943,
                "rms_normalized_rmse_percent": 3.5541852430159366,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02851242944598198,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.027437235228717327,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.20208395272493,
            "full": 298.5534999752417
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.94079203903675,
            "full": 304.50399999972433
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.12749997526407,
            "full": 302.63762501999736
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.64937498327345,
            "full": 298.7657079938799
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004413304850459099,
                  "p50": 0.0,
                  "p90": 3.81945283152163e-05,
                  "p95": 8.708395762369037e-05,
                  "p99": 0.00018998351879417896
                },
                "candidate_energy": 11.687273610742778,
                "cvrmse_percent": 6.930696505382952,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.04142693112768862,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.692117296122412,
                "relative_energy_error_percent": 0.04142693112768862,
                "rms_normalized_rmse_percent": 1.7707375423900429,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007330720312893391,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.006889389827847481,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007623210549354553,
                  "p50": 1.1295071999484207e-05,
                  "p90": 6.505831697722897e-05,
                  "p95": 0.00013469206169247627,
                  "p99": 0.0003082959447056055
                },
                "candidate_energy": 7.223310194602476,
                "cvrmse_percent": 18.602532285031362,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14047104474112315,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.213177768432125,
                "relative_energy_error_percent": 0.14047104474112315,
                "rms_normalized_rmse_percent": 1.7507379526791262,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04518340528011322,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.045945726335048676,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.87462505232543,
            "full": 3287.957875058055
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.18804202135652,
            "full": 3330.3904159693047
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.91749992687255,
            "full": 3251.8925829790533
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.06083398964256,
            "full": 3285.725750029087
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041494984179735184,
                  "p50": 0.0,
                  "p90": 3.781942359637469e-05,
                  "p95": 8.690729737281799e-05,
                  "p99": 0.0001956028863787651
                },
                "candidate_energy": 11.698235910117013,
                "cvrmse_percent": 6.7304471446696,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03748855949656338,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.693852053432522,
                "relative_energy_error_percent": 0.03748855949656338,
                "rms_normalized_rmse_percent": 1.7200157220875394,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007386407582089305,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.007801357423886657,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008380841463804245,
                  "p50": 1.1163295312144328e-05,
                  "p90": 7.012486457824707e-05,
                  "p95": 0.00014396145706996322,
                  "p99": 0.0003075944259762764
                },
                "candidate_energy": 7.225616849525917,
                "cvrmse_percent": 19.288024092575398,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15991080160628,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.214080755161813,
                "relative_energy_error_percent": 0.15991080160628,
                "rms_normalized_rmse_percent": 1.8147184241634193,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04494304955005646,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.04578113369643688,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.1936249770224,
            "full": 3453.387291985564
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.0956669813022,
            "full": 3431.756583042443
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.72945906128734,
            "full": 3431.440166896209
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.38287497498095,
            "full": 3462.826458038762
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002005849964916706,
                  "p50": 0.0,
                  "p90": 2.0766165107488632e-05,
                  "p95": 4.6863569878041744e-05,
                  "p99": 0.00011508236639201641
                },
                "candidate_energy": 11.696781247037144,
                "cvrmse_percent": 4.026452110275345,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.030845654579427628,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.693174410849004,
                "relative_energy_error_percent": 0.030845654579427628,
                "rms_normalized_rmse_percent": 1.0293522734953509,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007951526436954737,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.008152111433446407,
                  "rgb_channel": 0,
                  "sky_patch_index": 129
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005346406251192093,
                  "p50": 7.604445272590965e-06,
                  "p90": 4.4813205022364855e-05,
                  "p95": 8.160527067957446e-05,
                  "p99": 0.00018903985619544983
                },
                "candidate_energy": 7.2232889752142455,
                "cvrmse_percent": 11.72306684156917,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08526366773909806,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.217135380882809,
                "relative_energy_error_percent": 0.08526366773909806,
                "rms_normalized_rmse_percent": 1.1046069166405026,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03431328013539314,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.03377863951027393,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 263.1032500648871,
            "full": 6085.528458934277
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 262.46937504038215,
            "full": 6129.129959037527
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 263.35250004194677,
            "full": 6047.737917047925
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 276.54495800379664,
            "full": 6061.986375018023
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
    "/content/suite-vulkan-0.3.2/plan_j_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1236.323875025846,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4705.659916973673,
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
      47,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24123231163434583,
            "cvrmse_percent": 4.38611390745844,
            "rms_normalized_rmse_percent": 1.1209766504685317,
            "reference_energy": 11.693484420991894,
            "candidate_energy": 11.665275958212533,
            "relative_energy_error_percent": 0.24123231163434583,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.085386611521244e-05,
              "p95": 3.6797195207327604e-05,
              "p99": 0.0001160530373454094,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.1646834767311412,
            "cvrmse_percent": 15.908654796932934,
            "rms_normalized_rmse_percent": 1.4991126444366532,
            "reference_energy": 7.221705547018303,
            "candidate_energy": 7.233598502792418,
            "relative_energy_error_percent": 0.16468347673114123,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5232697478495538e-05,
              "p90": 5.367211997509003e-05,
              "p95": 7.656542584300041e-05,
              "p99": 0.00017670262604951859,
              "maximum": 0.0011406280100345612
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03787347301840782,
              "candidate": 0.03901410102844238,
              "position": [
                7.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.08625610968136499,
            "cvrmse_percent": 5.62474727799591,
            "rms_normalized_rmse_percent": 1.3882726053508978,
            "reference_energy": 18.915189968010196,
            "candidate_energy": 18.89887446100495,
            "relative_energy_error_percent": 0.08625610968136499,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4923348771844758e-05,
              "p90": 4.9659392971079797e-05,
              "p95": 6.816873792558908e-05,
              "p99": 0.00015073741087689996,
              "maximum": 0.0011406280100345612
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03787347301840782,
              "candidate": 0.03901410102844238,
              "position": [
                7.5,
                6.5,
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
      47,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24123231163434583,
            "cvrmse_percent": 4.38611390745844,
            "rms_normalized_rmse_percent": 1.1209766504685317,
            "reference_energy": 11.693484420991894,
            "candidate_energy": 11.665275958212533,
            "relative_energy_error_percent": 0.24123231163434583,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.085386611521244e-05,
              "p95": 3.6797195207327604e-05,
              "p99": 0.0001160530373454094,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 94.62939803227457,
            "cvrmse_percent": 565.1357052744607,
            "rms_normalized_rmse_percent": 34.381271005240194,
            "reference_energy": 3.7166011794337983,
            "candidate_energy": 7.233598502792418,
            "relative_energy_error_percent": 94.62939803227457,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.700512105657253e-05,
              "p90": 0.00019196898210793734,
              "p95": 0.000242809093009555,
              "p99": 0.0004208486061543226,
              "maximum": 0.01866787299513817
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02948259562253952,
              "candidate": 0.04815046861767769,
              "position": [
                0.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.6396462099009,
            "cvrmse_percent": 136.25176122879313,
            "rms_normalized_rmse_percent": 34.369276999812186,
            "reference_energy": 15.410085600425692,
            "candidate_energy": 18.89887446100495,
            "relative_energy_error_percent": 22.639646209900896,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.627564457379776e-05,
              "p90": 0.00018852487846743315,
              "p95": 0.00023677409626543522,
              "p99": 0.0003925692290067673,
              "maximum": 0.01866787299513817
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02948259562253952,
              "candidate": 0.04815046861767769,
              "position": [
                0.5,
                4.5,
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
      "bias_percent": -0.062265381687181855,
      "rms_normalized_error_percent": 0.3010783566499794,
      "absolute_error": {
        "p95": 0.09747834795767872,
        "p99": 0.24273074566338343,
        "maximum": 0.32936880683706704
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.896639395995418,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3010783566499794
    },
    "overcast": {
      "bias_percent": -0.024731485375088097,
      "rms_normalized_error_percent": 0.2392897975565767,
      "absolute_error": {
        "p95": 0.061502647399902334,
        "p99": 0.12350259780883782,
        "maximum": 0.16329574584960938
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.557656288146973,
      "reference_fraction_of_uniform": 0.6458004117012024,
      "rms_normalized_to_uniform_percent": 0.16388873571052767
    },
    "horizon": {
      "bias_percent": -0.26622618151334887,
      "rms_normalized_error_percent": 1.7933085245004583,
      "absolute_error": {
        "p95": 0.07247963030942792,
        "p99": 0.10402583284918973,
        "maximum": 0.10837829348436645
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.967725914310541,
      "reference_fraction_of_uniform": 0.10994946429723798,
      "rms_normalized_to_uniform_percent": 0.153147305449676
    },
    "north": {
      "bias_percent": -0.3049301759061889,
      "rms_normalized_error_percent": 0.5477953564453322,
      "absolute_error": {
        "p95": 0.09763574600219714,
        "p99": 0.15459329605102531,
        "maximum": 0.19222545623779297
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.098539352416992,
      "reference_fraction_of_uniform": 0.34076452255249023,
      "rms_normalized_to_uniform_percent": 0.20482586970143987
    },
    "east": {
      "bias_percent": 0.03362208541358992,
      "rms_normalized_error_percent": 0.30442087938079065,
      "absolute_error": {
        "p95": 0.04052989482879638,
        "p99": 0.06091098785400389,
        "maximum": 0.0693206787109375
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.325538635253906,
      "reference_fraction_of_uniform": 0.2416955828666687,
      "rms_normalized_to_uniform_percent": 0.0944671734239981
    },
    "south": {
      "bias_percent": 0.0991938269749987,
      "rms_normalized_error_percent": 0.24994856659530137,
      "absolute_error": {
        "p95": 0.03983643054962157,
        "p99": 0.04450143814086914,
        "maximum": 0.046230316162109375
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6229372024536133,
      "reference_fraction_of_uniform": 0.20243674516677856,
      "rms_normalized_to_uniform_percent": 0.07801424798925177
    },
    "west": {
      "bias_percent": -0.10198735064678272,
      "rms_normalized_error_percent": 0.5418725286266681,
      "absolute_error": {
        "p95": 0.06945767402648918,
        "p99": 0.15054430961608878,
        "maximum": 0.19314002990722656
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.111735820770264,
      "reference_fraction_of_uniform": 0.2856254577636719,
      "rms_normalized_to_uniform_percent": 0.16617169340130986
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
        "identifier": "plan_j_distributed_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.0554985452747437,
          "cvrmse_percent": 1.555631367033228,
          "absolute_error_percentiles_lux": {
            "p50": 3.54974365234375,
            "p90": 21.35784912109375,
            "p95": 30.602368164062497,
            "p99": 55.26558593750002
          },
          "maximum_absolute_error_lux": 212.171875,
          "worst": {
            "sensor_index": 18,
            "position": [
              4.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 33917.62890625,
            "radiance_lux": 33705.45703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2997406004080449,
            "maximum_error_percentage_points": 2.6576712328767114,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.12914247052019062,
            "maximum_error_percentage_points": 0.9641219542668082,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08791897406004089,
            "maximum_error_percentage_points": 0.6338356164383612,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10363159428738071,
            "maximum_error_percentage_points": 0.6338356164383612,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027808219178082173,
            "maximum_error_percentage_points": 0.19493150684931493,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 70.2127659574468,
          "radiance_percent": 68.08510638297872,
          "difference_percentage_points": 2.1276595744680833,
          "tolerance_percentage_points": 2.127659574468085,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004919199486295156,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_distributed_grid",
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
      "study_preparation_seconds": 0.38094986400028574,
      "weather_seconds": 0.22450906999984,
      "metric_reduction_seconds": 0.18460045600022568,
      "write_seconds": 0.01295105600001989,
      "total_seconds": 0.42245164499991006,
      "cold_end_to_end_seconds": 0.8034015090001958,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0018361269999331853,
      "engine_upload_seconds": 0.014113591,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.013373842,
      "engine_annual_reduction_seconds": 0.00682709,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.013373842
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38094986400028574,
      "weather_seconds": 0.22576469799969345,
      "metric_reduction_seconds": 0.18604578100030267,
      "write_seconds": 0.012881848000233731,
      "total_seconds": 0.42494888499959416,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.42494888499959416,
      "raw_export_seconds": 0.0017182940000566305,
      "engine_upload_seconds": 0.013882806,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.1e-08,
      "engine_annual_reduction_seconds": 0.006672587,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015487556000152836,
      "full": 0.025487389999852894
    }
  },
  "elapsed_seconds": 3.3217870099997526,
  "result_class": "passed"
}
```
