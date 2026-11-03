# Foton report

Status: **passed**

```json
{
  "scene": "west_facing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "west_facing",
    "category": "orientation",
    "question": "Is west-facing glazing assigned to the correct sky patches?",
    "interactions": [
      "west_glazing",
      "sky_patch_order"
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
    "aperture_area": 2.9999999999999982
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "08bad6e8d12b91062cabc92803ec96294c27572a86a9938b32d43bfe4aa78a6b",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1295539414187857659,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1295539414187857659,
      "basis": "ReinhartMf2",
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
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "cc89655337835cf98581e8d1a72ff842f12007169ecd7b0d1c42a44280f60591",
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
          "maximum": 0.00019046594388782978,
          "p95": 3.702007234096527e-08,
          "p99": 7.862458005547523e-06
        },
        "bias_percent": -0.032535962950541446,
        "identifier": "west_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7110687728256705,
        "worst_index": [
          15,
          281,
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
          "maximum": 0.00042247772216796875,
          "p95": 2.0910112652927637e-05,
          "p99": 9.57343727350235e-05
        },
        "bias_percent": 0.06882113240053545,
        "identifier": "west_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.644212117977333,
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
          "maximum": 0.0004658438265323639,
          "p95": 1.730816438794136e-05,
          "p99": 8.317595347762108e-05
        },
        "bias_percent": -0.03768678857412148,
        "identifier": "west_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4427053568302342,
        "worst_index": [
          11,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "west_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006715920753777027,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.617929516825825e-05,
                  "p99": 0.0002839957596734166
                },
                "candidate_energy": 6.024221788316936,
                "cvrmse_percent": 57.66595935646542,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.019870254388681168,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0254190544110315,
                "relative_energy_error_percent": 0.019870254388681168,
                "rms_normalized_rmse_percent": 11.093037448927532,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004774550907313824,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.005446142982691526,
                  "rgb_channel": 0,
                  "sky_patch_index": 522
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001234178664162755,
                  "p50": 0.0,
                  "p90": 5.708729622710969e-06,
                  "p95": 8.343392983078957e-05,
                  "p99": 0.0004209785838611424
                },
                "candidate_energy": 2.056450849802907,
                "cvrmse_percent": 241.00908813254676,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.6759447594822788,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0426437067124894,
                "relative_energy_error_percent": 0.6759447594822787,
                "rms_normalized_rmse_percent": 8.981464208266495,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00028973212465643883,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": -0.0009444465395063162,
                  "rgb_channel": 0,
                  "sky_patch_index": 106
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.1236249608919,
            "full": 232.38375002983958
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.71579202264547,
            "full": 233.96629199851304
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.69579197000712,
            "full": 229.45791692472994
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.87695795949548,
            "full": 224.5861659757793
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "west_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003520573955029249,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.316804602742195e-05,
                  "p99": 0.00013815797865390778
                },
                "candidate_energy": 6.018090301105985,
                "cvrmse_percent": 24.737919981511798,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07869419698058466,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.013358137208343,
                "relative_energy_error_percent": 0.07869419698058466,
                "rms_normalized_rmse_percent": 4.769363762737316,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036263414658606052,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.00397839886136353,
                  "rgb_channel": 0,
                  "sky_patch_index": 370
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006057006539776921,
                  "p50": 2.9873721274498166e-08,
                  "p90": 1.3149453207006455e-05,
                  "p95": 3.618140544858761e-05,
                  "p99": 0.00019205095304641873
                },
                "candidate_energy": 3.7844500237527043,
                "cvrmse_percent": 58.525739983766265,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10499960201405524,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7884278579261164,
                "relative_energy_error_percent": 0.10499960201405524,
                "rms_normalized_rmse_percent": 3.149247717810377,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003918388392776251,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": -0.00021386181470006704,
                  "rgb_channel": 0,
                  "sky_patch_index": 370
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.00937489699572,
            "full": 2281.1114590149373
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.91699999012053,
            "full": 2309.530209051445
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.46554191131145,
            "full": 2237.929124967195
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.5385420229286,
            "full": 2311.495832982473
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "west_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003506105567794293,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.053007483482361e-05,
                  "p99": 0.00011742147034965456
                },
                "candidate_energy": 6.016677686225194,
                "cvrmse_percent": 23.676766473202996,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03206342316829447,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.018607457803228,
                "relative_energy_error_percent": 0.03206342316829446,
                "rms_normalized_rmse_percent": 4.563459762684901,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009127774101216346,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.001263387966901064,
                  "rgb_channel": 0,
                  "sky_patch_index": 104
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008299797773361206,
                  "p50": 2.2424272216881036e-08,
                  "p90": 1.3429729369818273e-05,
                  "p95": 3.5728888178709894e-05,
                  "p99": 0.00017904076958075166
                },
                "candidate_energy": 3.7919929804592094,
                "cvrmse_percent": 57.35556697539871,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.038328208943331415,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7905401343164478,
                "relative_energy_error_percent": 0.038328208943331415,
                "rms_normalized_rmse_percent": 3.0824450978020907,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03328140079975128,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0341113805770874,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.02179200947285,
            "full": 2404.111708048731
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.70233302097768,
            "full": 2408.7242909008637
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.73349994700402,
            "full": 2478.6852080142125
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.34945895057172,
            "full": 2437.6995409838855
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "west_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001858002506196499,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1353529771440662e-05,
                  "p99": 7.671653293073177e-05
                },
                "candidate_energy": 6.014563878446097,
                "cvrmse_percent": 13.518602761172696,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.07225326282566295,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.018912739286861,
                "relative_energy_error_percent": 0.07225326282566297,
                "rms_normalized_rmse_percent": 2.6075174128677494,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009647717815823853,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0011505720322020352,
                  "rgb_channel": 0,
                  "sky_patch_index": 109
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006079301238059998,
                  "p50": 1.8232428899978004e-08,
                  "p90": 9.338260679214732e-06,
                  "p95": 2.2966374672250822e-05,
                  "p99": 0.00010877281602006406
                },
                "candidate_energy": 3.7879870290108784,
                "cvrmse_percent": 35.70289690091205,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.02571421157133886,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7889613305437706,
                "relative_energy_error_percent": 0.02571421157133886,
                "rms_normalized_rmse_percent": 1.919956425163423,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.023064279928803444,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.023672210052609444,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.052417030558,
            "full": 4287.950500031002
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.5976669760421,
            "full": 4327.152207959443
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.13625000137836,
            "full": 4224.331999896094
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.53337497543544,
            "full": 4308.781792060472
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/west_facing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2620.8278340054676,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/west_facing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10873.780000023544,
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
        "identifier": "west_facing_grid",
        "full_identifier": "west_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.010589404303434132,
            "cvrmse_percent": 2.0149277782245902,
            "rms_normalized_rmse_percent": 0.38864767269012634,
            "reference_energy": 6.015689356789835,
            "candidate_energy": 6.015052331122206,
            "relative_energy_error_percent": 0.010589404303434134,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.4668330550193787e-08,
              "p99": 5.01162139698863e-06,
              "maximum": 5.7995959650725126e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 281,
              "rgb_channel": 0,
              "reference": 0.000597580976318568,
              "candidate": 0.0005395850166678429,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.21316809280851992,
            "cvrmse_percent": 27.860909174989924,
            "rms_normalized_rmse_percent": 1.499355757509006,
            "reference_energy": 3.789523114463,
            "candidate_energy": 3.781445060313361,
            "relative_energy_error_percent": 0.21316809280851992,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0112777817994357e-05,
              "p95": 1.707968840491958e-05,
              "p99": 4.639721009880304e-05,
              "maximum": 0.0007920842617750168
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03131178393959999,
              "candidate": 0.030519699677824974,
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
            "nmbe_percent": -0.08888211084480852,
            "cvrmse_percent": 10.742045080468102,
            "rms_normalized_rmse_percent": 1.4957838034522897,
            "reference_energy": 9.805212471252835,
            "candidate_energy": 9.796497391435567,
            "relative_energy_error_percent": 0.08888211084480853,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0100293729919949e-05,
              "p95": 1.687253825366497e-05,
              "p99": 4.5684282667934895e-05,
              "maximum": 0.0007920842617750168
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03131178393959999,
              "candidate": 0.030519699677824974,
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
        "identifier": "west_facing_grid",
        "full_identifier": "west_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.010589404303434132,
            "cvrmse_percent": 2.0149277782245902,
            "rms_normalized_rmse_percent": 0.38864767269012634,
            "reference_energy": 6.015689356789835,
            "candidate_energy": 6.015052331122206,
            "relative_energy_error_percent": 0.010589404303434134,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.4668330550193787e-08,
              "p99": 5.01162139698863e-06,
              "maximum": 5.7995959650725126e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 281,
              "rgb_channel": 0,
              "reference": 0.000597580976318568,
              "candidate": 0.0005395850166678429,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 83.6831413994,
            "cvrmse_percent": 894.0975527202808,
            "rms_normalized_rmse_percent": 33.55467868753058,
            "reference_energy": 2.0586783476720925,
            "candidate_energy": 3.781445060313361,
            "relative_energy_error_percent": 83.6831413994,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.775055724370778e-05,
              "p95": 8.091761264950037e-05,
              "p99": 0.00018305517733097076,
              "maximum": 0.008351169526576996
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01020956039428711,
              "candidate": 0.018560729920864105,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.328353500943287,
            "cvrmse_percent": 227.95789129920772,
            "rms_normalized_rmse_percent": 33.553886843609284,
            "reference_energy": 8.074367704461928,
            "candidate_energy": 9.796497391435567,
            "relative_energy_error_percent": 21.328353500943287,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.776199905085403e-05,
              "p95": 8.115999662550166e-05,
              "p99": 0.0001809841487556696,
              "maximum": 0.008351169526576996
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01020956039428711,
              "candidate": 0.018560729920864105,
              "position": [
                5.5,
                2.5,
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
      "bias_percent": 0.08293952762023318,
      "rms_normalized_error_percent": 0.1437459288286999,
      "absolute_error": {
        "p95": 0.06259623931356395,
        "p99": 0.07601142889089867,
        "maximum": 0.08093699652985231
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.033810552929385,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1437459288286999
    },
    "overcast": {
      "bias_percent": 0.05921111432320878,
      "rms_normalized_error_percent": 0.10574650856111135,
      "absolute_error": {
        "p95": 0.02961862087249756,
        "p99": 0.03697240948677063,
        "maximum": 0.0375138521194458
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.6888251304626465,
      "reference_fraction_of_uniform": 0.6389352083206177,
      "rms_normalized_to_uniform_percent": 0.0750432788912527
    },
    "horizon": {
      "bias_percent": 0.9337203792744486,
      "rms_normalized_error_percent": 1.815135318783517,
      "absolute_error": {
        "p95": 0.04503817669549559,
        "p99": 0.06176899397175023,
        "maximum": 0.06533904298913096
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.24568807193391,
      "reference_fraction_of_uniform": 0.10351567913213265,
      "rms_normalized_to_uniform_percent": 0.10841623747934237
    },
    "north": {
      "bias_percent": 0.029533099759363746,
      "rms_normalized_error_percent": 0.19161375272549228,
      "absolute_error": {
        "p95": 0.016335129737854004,
        "p99": 0.0186974287033081,
        "maximum": 0.019661903381347656
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.26313853263855,
      "reference_fraction_of_uniform": 0.18806499242782593,
      "rms_normalized_to_uniform_percent": 0.03815942060120264
    },
    "east": {
      "bias_percent": -30.909568121098378,
      "rms_normalized_error_percent": 119.58760380898681,
      "absolute_error": {
        "p95": 1.6201209575683606e-05,
        "p99": 3.216131830185984e-05,
        "maximum": 3.9730934076942503e-05
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.506500656338176e-06,
      "reference_fraction_of_uniform": 4.575857701638597e-07,
      "rms_normalized_to_uniform_percent": 4.2102421813304234e-05
    },
    "south": {
      "bias_percent": 0.0942549975287486,
      "rms_normalized_error_percent": 0.2436041627808017,
      "absolute_error": {
        "p95": 0.021509140729904175,
        "p99": 0.030231535434722883,
        "maximum": 0.03457450866699219
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.297471523284912,
      "reference_fraction_of_uniform": 0.19091804325580597,
      "rms_normalized_to_uniform_percent": 0.048945526241549214
    },
    "west": {
      "bias_percent": 0.10014573580263363,
      "rms_normalized_error_percent": 0.17854362455251127,
      "absolute_error": {
        "p95": 0.06097590923309326,
        "p99": 0.07092657089233398,
        "maximum": 0.07166624069213867
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.421207427978516,
      "reference_fraction_of_uniform": 0.6997956037521362,
      "rms_normalized_to_uniform_percent": 0.11744834198449522
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
        "identifier": "west_facing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.0004042613807119309,
          "cvrmse_percent": 1.830957410640933,
          "absolute_error_percentiles_lux": {
            "p50": 0.8554000854492188,
            "p90": 13.1561508178711,
            "p95": 23.91467285156247,
            "p99": 60.1657519531249
          },
          "maximum_absolute_error_lux": 269.59765625,
          "worst": {
            "sensor_index": 8,
            "position": [
              1.5,
              3.5,
              0.75
            ],
            "hour_of_year": 5247.5,
            "foton_lux": 25128.513671875,
            "radiance_lux": 24858.916015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20760273972602722,
            "maximum_error_percentage_points": 0.737260273972602,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13425079244941943,
            "maximum_error_percentage_points": 0.6170175009613601,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10243150684931532,
            "maximum_error_percentage_points": 0.4949315068493192,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10244672754946807,
            "maximum_error_percentage_points": 0.49068493150685555,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00794140030441404,
            "maximum_error_percentage_points": 0.08027397260273972,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 30.555555555555557,
          "radiance_percent": 30.555555555555557,
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
      "maximum_error_percentage_points": 0.004931506849313649,
      "metrics": {
        "da": [
          {
            "identifier": "west_facing_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "west_facing_grid",
            "maximum_error_percentage_points": 0.004803082191784824,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "west_facing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "west_facing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "west_facing_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
      "study_preparation_seconds": 0.35865496000042185,
      "weather_seconds": 0.246923031998449,
      "metric_reduction_seconds": 1.0656473319977522,
      "write_seconds": 0.021204589000262786,
      "total_seconds": 1.3340818819997367,
      "cold_end_to_end_seconds": 1.6927368420001585,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00862916899859556,
      "engine_upload_seconds": 0.044506251,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.030067985,
      "engine_annual_reduction_seconds": 0.019521514,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.030067985
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35865496000042185,
      "weather_seconds": 0.24827992499922402,
      "metric_reduction_seconds": 1.0626028980004776,
      "write_seconds": 0.021602011998766102,
      "total_seconds": 1.3328097199992044,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.3328097199992044,
      "raw_export_seconds": 0.007497599999624072,
      "engine_upload_seconds": 0.047614711,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.9e-08,
      "engine_annual_reduction_seconds": 0.020255067,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01782489600009285,
      "full": 0.04847168999913265
    }
  },
  "elapsed_seconds": 5.114775429003203,
  "result_class": "passed"
}
```
