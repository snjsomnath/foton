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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0c71fae282bea61650b507f9fb98cf426890001b0b838bb97259344f8e75998b",
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
      "scene_fingerprint": 6169704301367242066,
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
      "scene_fingerprint": 6169704301367242066,
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
    "model_sha256": "a42ccfeab8ae79ba3fcaa01e5cba3aeca3609463ed2b42d1d5355c23044cd9f2",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "41ef2f2774bff44b552e4bcb5440641cfa316a6a7716fe665a18b2f1b83a474a",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0007328237406909466,
          "p95": 2.1042651496827463e-05,
          "p99": 0.00012266170233488083
        },
        "bias_percent": -0.1641994051391909,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3341431807614936,
        "worst_index": [
          38,
          105,
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
          "maximum": 0.0007546320557594299,
          "p95": 5.9503992088138924e-05,
          "p99": 0.00014960533007979393
        },
        "bias_percent": 0.05701406317474002,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9121748198573155,
        "worst_index": [
          48,
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
          "maximum": 0.0006979778409004211,
          "p95": 5.0072259909938994e-05,
          "p99": 0.00013414118438959122
        },
        "bias_percent": 0.015564848662210244,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8772662744594474,
        "worst_index": [
          37,
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000579402782022953,
                  "p50": 0.0,
                  "p90": 5.086441524326834e-06,
                  "p95": 9.193918849632601e-05,
                  "p99": 0.0002808007411658764
                },
                "candidate_energy": 11.549583050735492,
                "cvrmse_percent": 10.690186585474589,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.024328649536300435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.552393592085565,
                "relative_energy_error_percent": 0.02432864953630044,
                "rms_normalized_rmse_percent": 2.4472631988384332,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008048419374972582,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.008627822156995535,
                  "rgb_channel": 0,
                  "sky_patch_index": 102
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001803755760192871,
                  "p50": 0.0,
                  "p90": 6.245167242013863e-05,
                  "p95": 0.00017477440705988525,
                  "p99": 0.0004580484237521887
                },
                "candidate_energy": 3.527761645298451,
                "cvrmse_percent": 62.918718215425095,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11222036230473253,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.523807216073653,
                "relative_energy_error_percent": 0.11222036230473251,
                "rms_normalized_rmse_percent": 3.189657192623036,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.043763959780335426,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.041960204020142555,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.35733409784734,
            "full": 306.8689170759171
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.29441701434553,
            "full": 320.22704102564603
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.89295805245638,
            "full": 307.6828340999782
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.8763749487698,
            "full": 318.03529092576355
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042283255606889725,
                  "p50": 0.0,
                  "p90": 5.691800868135033e-06,
                  "p95": 6.775592919439073e-05,
                  "p99": 0.00019914144650101662
                },
                "candidate_energy": 11.56014271186907,
                "cvrmse_percent": 7.39445302679185,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06589065170483847,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.56776478747522,
                "relative_energy_error_percent": 0.06589065170483849,
                "rms_normalized_rmse_percent": 1.6939176385013557,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007119044661521912,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.006696212105453014,
                  "rgb_channel": 0,
                  "sky_patch_index": 50
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000745430588722229,
                  "p50": 4.654663825931493e-06,
                  "p90": 4.891906719421982e-05,
                  "p95": 0.0001113350948799045,
                  "p99": 0.00030453060753643513
                },
                "candidate_energy": 6.794100992759798,
                "cvrmse_percent": 20.53337519258041,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05852616154860287,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.790126992067066,
                "relative_energy_error_percent": 0.05852616154860288,
                "rms_normalized_rmse_percent": 1.6227266450740552,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05628187023103237,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.0570273008197546,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.4996250141412,
            "full": 3773.945041000843
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.18670900631696,
            "full": 3805.8215000201017
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.27783295232803,
            "full": 3720.10274999775
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.45254101324826,
            "full": 3641.162791987881
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041736854473128915,
                  "p50": 0.0,
                  "p90": 7.906246901257257e-06,
                  "p95": 7.016257150098675e-05,
                  "p99": 0.00019538996275514364
                },
                "candidate_energy": 11.555676070304251,
                "cvrmse_percent": 7.331462782968131,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06276990720412318,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.562934113317255,
                "relative_energy_error_percent": 0.06276990720412319,
                "rms_normalized_rmse_percent": 1.6793182918866283,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020063374540768564,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.0024237059988081455,
                  "rgb_channel": 0,
                  "sky_patch_index": 12
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001514112576842308,
                  "p50": 4.745767682834412e-06,
                  "p90": 5.118149629197434e-05,
                  "p95": 0.00011189511278644197,
                  "p99": 0.0002956691896542907
                },
                "candidate_energy": 6.813027550271496,
                "cvrmse_percent": 21.650149609149302,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.17053448889857883,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.801428768483362,
                "relative_energy_error_percent": 0.17053448889857883,
                "rms_normalized_rmse_percent": 1.713556716537505,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06312152743339539,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.06160741485655308,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.84966608230025,
            "full": 3978.222207981162
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.6469579814002,
            "full": 4008.8263330981135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.31550001353025,
            "full": 4007.9257499892265
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.65499999001622,
            "full": 3978.0385409248993
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020941859111189842,
                  "p50": 0.0,
                  "p90": 3.442220258875809e-06,
                  "p95": 3.47261331626213e-05,
                  "p99": 0.00010484457015991211
                },
                "candidate_energy": 11.56005445038683,
                "cvrmse_percent": 3.9800401034993618,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.023164936326195443,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.557377191319482,
                "relative_energy_error_percent": 0.02316493632619544,
                "rms_normalized_rmse_percent": 0.9113702025253435,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00748596154153347,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.007695380132645369,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005000550299882889,
                  "p50": 3.2844027373357676e-06,
                  "p90": 3.174516532453714e-05,
                  "p95": 6.324275982478862e-05,
                  "p99": 0.00015788013115525246
                },
                "candidate_energy": 6.809920306631817,
                "cvrmse_percent": 11.531575719403225,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.022192541036441596,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.811431936459485,
                "relative_energy_error_percent": 0.022192541036441596,
                "rms_normalized_rmse_percent": 0.9140229659540186,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04079931043088436,
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "reference": 0.04029925540089607,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 291.8307089712471,
            "full": 7052.034000051208
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 290.9834160236642,
            "full": 6950.57733298745
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 299.8219169676304,
            "full": 7125.716041889973
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 319.0604579867795,
            "full": 7085.119750001468
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
    "/content/suite-vulkan-0.3.2/u_shaped_plan/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1745.4322919948027,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6012.671582982875,
      "invocation_count": 4,
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
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.151879378804343,
            "cvrmse_percent": 3.9452707040154857,
            "rms_normalized_rmse_percent": 0.9034920267620642,
            "reference_energy": 11.561360763334477,
            "candidate_energy": 11.543801440425796,
            "relative_energy_error_percent": 0.151879378804343,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.159527063369751e-07,
              "p95": 1.9227081793360266e-05,
              "p99": 9.747035801410675e-05,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                7.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.46273272737168697,
            "cvrmse_percent": 18.120420991719044,
            "rms_normalized_rmse_percent": 1.4352585977208985,
            "reference_energy": 6.808031234383348,
            "candidate_energy": 6.77652824577217,
            "relative_energy_error_percent": 0.462732727371687,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.676348445784242e-06,
              "p90": 4.8274922301061464e-05,
              "p95": 7.317833078559485e-05,
              "p99": 0.0001597902737557888,
              "maximum": 0.0014097169041633606
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07492837309837341,
              "candidate": 0.07351865619421005,
              "position": [
                7.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2670872913265461,
            "cvrmse_percent": 6.512390425176884,
            "rms_normalized_rmse_percent": 1.391795875717381,
            "reference_energy": 18.369391997717827,
            "candidate_energy": 18.320329686197965,
            "relative_energy_error_percent": 0.26708729132655573,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.641909178346395e-06,
              "p90": 4.602449771482505e-05,
              "p95": 6.771138760086613e-05,
              "p99": 0.00014059440582059324,
              "maximum": 0.0014097169041633606
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07492837309837341,
              "candidate": 0.07351865619421005,
              "position": [
                7.5,
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
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.151879378804343,
            "cvrmse_percent": 3.9452707040154857,
            "rms_normalized_rmse_percent": 0.9034920267620642,
            "reference_energy": 11.561360763334477,
            "candidate_energy": 11.543801440425796,
            "relative_energy_error_percent": 0.151879378804343,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.159527063369751e-07,
              "p95": 1.9227081793360266e-05,
              "p99": 9.747035801410675e-05,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                7.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 92.76626116873277,
            "cvrmse_percent": 614.7069143821175,
            "rms_normalized_rmse_percent": 31.101643212009492,
            "reference_energy": 3.5154119837602273,
            "candidate_energy": 6.77652824577217,
            "relative_energy_error_percent": 92.76626116873277,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.8147563657275896e-05,
              "p90": 0.00022535822081977134,
              "p95": 0.0002899429593526291,
              "p99": 0.0005031246691942215,
              "maximum": 0.022406425327062607
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034713685512542725,
              "candidate": 0.05712011083960533,
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
            "nmbe_percent": 21.513602370429673,
            "cvrmse_percent": 143.3088958759647,
            "rms_normalized_rmse_percent": 31.097147001449304,
            "reference_energy": 15.076772747094704,
            "candidate_energy": 18.320329686197965,
            "relative_energy_error_percent": 21.51360237042967,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.7757816755856766e-05,
              "p90": 0.0002242230257252232,
              "p95": 0.0002876218080928083,
              "p99": 0.0004896683312836103,
              "maximum": 0.022406425327062607
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.034713685512542725,
              "candidate": 0.05712011083960533,
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
      "bias_percent": -0.004396684241855177,
      "rms_normalized_error_percent": 0.19642587157084104,
      "absolute_error": {
        "p95": 0.11190233915690832,
        "p99": 0.14734519752000627,
        "maximum": 0.16501272673921363
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.547150058028427,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19642587157084104
    },
    "overcast": {
      "bias_percent": 0.01799854102080306,
      "rms_normalized_error_percent": 0.17640935729335921,
      "absolute_error": {
        "p95": 0.06276283264160154,
        "p99": 0.10365859985351555,
        "maximum": 0.11454582214355469
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.259133338928223,
      "reference_fraction_of_uniform": 0.65987229347229,
      "rms_normalized_to_uniform_percent": 0.1223348678746844
    },
    "horizon": {
      "bias_percent": -0.5332500618091452,
      "rms_normalized_error_percent": 1.8956825696349036,
      "absolute_error": {
        "p95": 0.07295006667179937,
        "p99": 0.0838500411191456,
        "maximum": 0.0846536333595358
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2366395953529872,
      "reference_fraction_of_uniform": 0.07954124008177281,
      "rms_normalized_to_uniform_percent": 0.11687240047978635
    },
    "north": {
      "bias_percent": -0.2318614545521677,
      "rms_normalized_error_percent": 0.39611212832687964,
      "absolute_error": {
        "p95": 0.04073708057403564,
        "p99": 0.04889292716979976,
        "maximum": 0.05669546127319336
      },
      "worst_index": [
        50
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.024549722671509,
      "reference_fraction_of_uniform": 0.13021999597549438,
      "rms_normalized_to_uniform_percent": 0.0678469842558462
    },
    "east": {
      "bias_percent": -0.025553299619871687,
      "rms_normalized_error_percent": 0.28626552324222126,
      "absolute_error": {
        "p95": 0.07284460067749023,
        "p99": 0.10149513244628892,
        "maximum": 0.12459564208984375
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.853060245513916,
      "reference_fraction_of_uniform": 0.376471608877182,
      "rms_normalized_to_uniform_percent": 0.12451850620687747
    },
    "south": {
      "bias_percent": 0.0739418500964846,
      "rms_normalized_error_percent": 0.24376748070527984,
      "absolute_error": {
        "p95": 0.05623927116394042,
        "p99": 0.07714309692382809,
        "maximum": 0.08204269409179688
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.035159587860107,
      "reference_fraction_of_uniform": 0.3881843090057373,
      "rms_normalized_to_uniform_percent": 0.10477808116266989
    },
    "west": {
      "bias_percent": -0.12490309218356098,
      "rms_normalized_error_percent": 0.35023825591554253,
      "absolute_error": {
        "p95": 0.041601467132568355,
        "p99": 0.05289134979248041,
        "maximum": 0.06246614456176758
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8037056922912598,
      "reference_fraction_of_uniform": 0.18033567070960999,
      "rms_normalized_to_uniform_percent": 0.06759751494553656
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
          "nmbe_percent": -0.039461704502362714,
          "cvrmse_percent": 1.5981438600038724,
          "absolute_error_percentiles_lux": {
            "p50": 2.669219970703125,
            "p90": 24.42261047363282,
            "p95": 37.81601562499998,
            "p99": 74.43981445312468
          },
          "maximum_absolute_error_lux": 322.41796875,
          "worst": {
            "sensor_index": 33,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4210.41748046875,
            "radiance_lux": 4532.83544921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.25605324373223026,
            "maximum_error_percentage_points": 1.5919178082191792,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.24083833691535725,
            "maximum_error_percentage_points": 1.4412419503879796,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.28679245283018917,
            "maximum_error_percentage_points": 2.108493150684936,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.30460325665546645,
            "maximum_error_percentage_points": 2.1084931506849314,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.029842336521064872,
            "maximum_error_percentage_points": 0.2147945205479438,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 50.943396226415096,
          "radiance_percent": 50.943396226415096,
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
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004872377996576915,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "u_shaped_plan_grid",
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
      "study_preparation_seconds": 0.3798939200000859,
      "weather_seconds": 0.23764955799993004,
      "metric_reduction_seconds": 0.22330884100006188,
      "write_seconds": 0.011819831999900998,
      "total_seconds": 0.47310399299999517,
      "cold_end_to_end_seconds": 0.8529979130000811,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0018624879999151744,
      "engine_upload_seconds": 0.013897285,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.015405455,
      "engine_annual_reduction_seconds": 0.007538458,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.015405455
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3798939200000859,
      "weather_seconds": 0.2515377740000986,
      "metric_reduction_seconds": 0.19574514000009913,
      "write_seconds": 0.013001124000084019,
      "total_seconds": 0.4605262219999986,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4605262219999986,
      "raw_export_seconds": 0.002033890999882715,
      "engine_upload_seconds": 0.01364902,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.3e-08,
      "engine_annual_reduction_seconds": 0.007534451,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013965378999955647,
      "full": 0.024690982000038275
    }
  },
  "elapsed_seconds": 3.077424221000001,
  "result_class": "passed"
}
```
