# Foton report

Status: **passed**

```json
{
  "scene": "teaching_office",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_office",
    "category": "teaching",
    "question": "How is a 12 x 8 m open-plan office with a ribbon window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
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
    "sensors": 96,
    "floor_area": 96.0,
    "aperture_area": 17.6
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "3291c716440a2b808a82d9b3f08a4be392139c86d69afb2b625eff05703af9e3",
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
      "scene_fingerprint": 17113111844658936175,
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
      "scene_fingerprint": 17113111844658936175,
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
    "model_sha256": "825ad310dbb74f08c550af303c2dbd0c86b8b317ca49c6afd9c865e96c466ecd",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "4265e63cc63ede966c40bbb0f0c0b2ace848568cf0a2cd56b667f1cf881eec43",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013817357830703259,
          "p95": 1.038727532431949e-06,
          "p99": 2.4425185984000564e-05
        },
        "bias_percent": 0.033900770041301743,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7639001981790288,
        "worst_index": [
          6,
          356,
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
          "maximum": 0.0007904171943664551,
          "p95": 6.36223703622818e-05,
          "p99": 0.00013304996071383338
        },
        "bias_percent": 0.0689597867356234,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0094879958336664,
        "worst_index": [
          68,
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
          "maximum": 0.000677250325679779,
          "p95": 5.3087715059518814e-05,
          "p99": 0.00011264751316048122
        },
        "bias_percent": -0.017256824341356544,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8553421057049212,
        "worst_index": [
          23,
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008858575019985437,
                  "p50": 0.0,
                  "p90": 4.747293351101701e-05,
                  "p95": 0.00017259863670915365,
                  "p99": 0.00036186401383019983
                },
                "candidate_energy": 37.0828926899469,
                "cvrmse_percent": 32.689260673872006,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.014129498280919826,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.088133057069626,
                "relative_energy_error_percent": 0.014129498280919825,
                "rms_normalized_rmse_percent": 9.557698440448512,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015878690173849463,
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "reference": 0.00247372651938349,
                  "rgb_channel": 0,
                  "sky_patch_index": 212
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001721397042274475,
                  "p50": 0.0,
                  "p90": 8.944460932980298e-05,
                  "p95": 0.00022616609930992126,
                  "p99": 0.00046845218574162554
                },
                "candidate_energy": 15.524541051710965,
                "cvrmse_percent": 104.69121323212242,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.02175910402513076,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.52116378553696,
                "relative_energy_error_percent": 0.021759104025130763,
                "rms_normalized_rmse_percent": 4.067424839751606,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08448318764567375,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.08620458468794823,
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.6978329643607,
            "full": 485.66708294674754
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.19437507167459,
            "full": 488.8526670401916
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.57045798096806,
            "full": 497.8313749888912
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.2176660047844,
            "full": 494.9076659977436
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003856169059872627,
                  "p50": 0.0,
                  "p90": 3.2805398222990873e-05,
                  "p95": 8.769950363785028e-05,
                  "p99": 0.00017693565838271708
                },
                "candidate_energy": 37.083694507397354,
                "cvrmse_percent": 16.178815036296726,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0007639166029962812,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.08341122106208,
                "relative_energy_error_percent": 0.0007639166029962812,
                "rms_normalized_rmse_percent": 4.7353687548640195,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035868240520358086,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.003972440958023071,
                  "rgb_channel": 0,
                  "sky_patch_index": 365
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012247562408447266,
                  "p50": 5.000000058430487e-08,
                  "p90": 5.00361340527891e-05,
                  "p95": 0.00012404775770846754,
                  "p99": 0.0002636938676005223
                },
                "candidate_energy": 26.784432608573574,
                "cvrmse_percent": 34.44726492426008,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.035205570746653245,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.775006314783003,
                "relative_energy_error_percent": 0.03520557074665325,
                "rms_normalized_rmse_percent": 1.8827378632018732,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07998544722795486,
                  "global_sensor_index": 85,
                  "local_sensor_index": 85,
                  "reference": 0.07876069098711014,
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 282.20391692593694,
            "full": 5656.799916992895
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 282.02225000131875,
            "full": 5678.109416970983
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 295.0114590348676,
            "full": 5637.642291025259
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 281.1940419487655,
            "full": 5769.937624922022
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037179107312113047,
                  "p50": 0.0,
                  "p90": 3.53580253431576e-05,
                  "p95": 8.969410555437207e-05,
                  "p99": 0.00018138115643523547
                },
                "candidate_energy": 37.08928457519835,
                "cvrmse_percent": 16.41978531370862,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01956722500668532,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.09654333930325,
                "relative_energy_error_percent": 0.01956722500668532,
                "rms_normalized_rmse_percent": 4.806190966140084,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0021346694556996226,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.002506460528820753,
                  "rgb_channel": 0,
                  "sky_patch_index": 210
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014390423893928528,
                  "p50": 5.000000058430487e-08,
                  "p90": 5.163014866411691e-05,
                  "p95": 0.0001281563818338327,
                  "p99": 0.0002666148467687889
                },
                "candidate_energy": 26.829176926020335,
                "cvrmse_percent": 34.97267632995882,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11028976943661357,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.79961968725737,
                "relative_energy_error_percent": 0.11028976943661359,
                "rms_normalized_rmse_percent": 1.9111632390906446,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07996375858783722,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.07852471619844437,
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 298.97820798214525,
            "full": 6190.939250052907
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 291.8105829739943,
            "full": 6087.1652089990675
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 288.2475829683244,
            "full": 6104.30816700682
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 288.3604590315372,
            "full": 6035.10937502142
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024308939464390278,
                  "p50": 0.0,
                  "p90": 2.0716150174848735e-05,
                  "p95": 4.677602555602789e-05,
                  "p99": 0.00010361927241319684
                },
                "candidate_energy": 37.070447336660095,
                "cvrmse_percent": 9.410998893147955,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.029506286462336568,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.08138867742747,
                "relative_energy_error_percent": 0.029506286462336568,
                "rms_normalized_rmse_percent": 2.7551471939109184,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001006061618681997,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0012491510133258998,
                  "rgb_channel": 0,
                  "sky_patch_index": 202
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010989867150783539,
                  "p50": 5.000000058430487e-08,
                  "p90": 3.0299849822768182e-05,
                  "p95": 7.258751429617405e-05,
                  "p99": 0.00015215062638162586
                },
                "candidate_energy": 26.836042509244276,
                "cvrmse_percent": 20.831526442811832,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1169678106192195,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.804689650616673,
                "relative_energy_error_percent": 0.11696781061921951,
                "rms_normalized_rmse_percent": 1.1389172567331538,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07929807528853416,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.07819908857345581,
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 489.3600409850478,
            "full": 10695.86995895952
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 525.5429170792922,
            "full": 10674.26604195498
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 510.2935420582071,
            "full": 10969.371292041615
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 503.3002910204232,
            "full": 10970.426707994193
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/teaching_office/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 15754.007459036075,
      "invocation_count": 6,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 66433.34487499669,
      "invocation_count": 6,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01319661295141117,
            "cvrmse_percent": 1.453344716835372,
            "rms_normalized_rmse_percent": 0.4256384177558553,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796618528851,
            "relative_energy_error_percent": 0.01319661295141117,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9075632863157423,
            "cvrmse_percent": 63.50055483299384,
            "rms_normalized_rmse_percent": 3.471109998899636,
            "reference_energy": 26.813211485065203,
            "candidate_energy": 26.301732506893906,
            "relative_energy_error_percent": 1.9075632863157324,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.10976345680092e-08,
              "p90": 1.839788601500916e-05,
              "p95": 3.190804272890091e-05,
              "p99": 6.699242163449515e-05,
              "maximum": 0.00472191721200943
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10907280445098877,
              "candidate": 0.10435088723897934,
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
            "nmbe_percent": -0.7928243040501443,
            "cvrmse_percent": 26.641911834945084,
            "rms_normalized_rmse_percent": 3.4704277814106166,
            "reference_energy": 63.896283960808596,
            "candidate_energy": 63.38969869218242,
            "relative_energy_error_percent": 0.7928243040501289,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.095055044535002e-08,
              "p90": 1.8293666653335097e-05,
              "p95": 3.140978515148163e-05,
              "p99": 6.601458415389055e-05,
              "maximum": 0.00472191721200943
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10907280445098877,
              "candidate": 0.10435088723897934,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01319661295141117,
            "cvrmse_percent": 1.453344716835372,
            "rms_normalized_rmse_percent": 0.4256384177558553,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796618528851,
            "relative_energy_error_percent": 0.01319661295141117,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.41215076106494,
            "cvrmse_percent": 592.1799698679389,
            "rms_normalized_rmse_percent": 23.02058324241776,
            "reference_energy": 15.525292836869342,
            "candidate_energy": 26.301732506893906,
            "relative_energy_error_percent": 69.41215076106494,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015659483906347324,
              "p95": 0.00022462999913841486,
              "p99": 0.000354554757941514,
              "maximum": 0.01887592300772667
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05774024501442909,
              "candidate": 0.07661616802215576,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.493572296923045,
            "cvrmse_percent": 174.76247937875505,
            "rms_normalized_rmse_percent": 23.021086317150967,
            "reference_energy": 52.60836531261273,
            "candidate_energy": 63.38969869218242,
            "relative_energy_error_percent": 20.493572296923066,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015658881748095157,
              "p95": 0.00022513000294566154,
              "p99": 0.0003554787964094426,
              "maximum": 0.01887592300772667
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05774024501442909,
              "candidate": 0.07661616802215576,
              "position": [
                0.5,
                1.5,
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
      "bias_percent": 0.14721650481119386,
      "rms_normalized_error_percent": 0.18693221919910066,
      "absolute_error": {
        "p95": 0.14327705702519178,
        "p99": 0.18578431988289512,
        "maximum": 0.19639338286038033
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.44113234550767,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.18693221919910066
    },
    "overcast": {
      "bias_percent": 0.10593522915757897,
      "rms_normalized_error_percent": 0.1450879419559876,
      "absolute_error": {
        "p95": 0.07764244079589844,
        "p99": 0.10217971801757808,
        "maximum": 0.11637115478515625
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.157854080200195,
      "reference_fraction_of_uniform": 0.6384364366531372,
      "rms_normalized_to_uniform_percent": 0.10163379420186926
    },
    "horizon": {
      "bias_percent": 0.8165732124588354,
      "rms_normalized_error_percent": 1.642293009412077,
      "absolute_error": {
        "p95": 0.14545600611148712,
        "p99": 0.18727667438691997,
        "maximum": 0.19219206913248854
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4819081981431794,
      "reference_fraction_of_uniform": 0.12242509038825782,
      "rms_normalized_to_uniform_percent": 0.15064452413907672
    },
    "north": {
      "bias_percent": -62.920401962031306,
      "rms_normalized_error_percent": 91.96883935205206,
      "absolute_error": {
        "p95": 6.098712992752553e-05,
        "p99": 0.0001559317787723555,
        "maximum": 0.0002427612907922594
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3995208973938134e-05,
      "reference_fraction_of_uniform": 4.920763672089379e-07,
      "rms_normalized_to_uniform_percent": 9.103786726103462e-05
    },
    "east": {
      "bias_percent": 0.07551568436030709,
      "rms_normalized_error_percent": 0.18186835763078327,
      "absolute_error": {
        "p95": 0.031490445137023926,
        "p99": 0.040304958820343,
        "maximum": 0.04742264747619629
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.44733190536499,
      "reference_fraction_of_uniform": 0.19153006374835968,
      "rms_normalized_to_uniform_percent": 0.037185587149523074
    },
    "south": {
      "bias_percent": 0.19137283477470968,
      "rms_normalized_error_percent": 0.2591264654687297,
      "absolute_error": {
        "p95": 0.14481830596923828,
        "p99": 0.18765823841094967,
        "maximum": 0.1960916519165039
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.6885986328125,
      "reference_fraction_of_uniform": 0.6922579407691956,
      "rms_normalized_to_uniform_percent": 0.16430869568108952
    },
    "west": {
      "bias_percent": 0.10299994180355193,
      "rms_normalized_error_percent": 0.16506945308484253,
      "absolute_error": {
        "p95": 0.02588355541229248,
        "p99": 0.043592047691345205,
        "maximum": 0.04636573791503906
      },
      "worst_index": [
        95
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.5115203857421875,
      "reference_fraction_of_uniform": 0.19378696382045746,
      "rms_normalized_to_uniform_percent": 0.03400956220756528
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
        "identifier": "teaching_office_grid",
        "sensor_count": 96,
        "illuminance": {
          "nmbe_percent": -0.015961545049776014,
          "cvrmse_percent": 1.1167434538955476,
          "absolute_error_percentiles_lux": {
            "p50": 3.8672027587890625,
            "p90": 38.80126953125,
            "p95": 59.62318115234372,
            "p99": 118.53760742187563
          },
          "maximum_absolute_error_lux": 403.3056640625,
          "worst": {
            "sensor_index": 45,
            "position": [
              5.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1857.5,
            "foton_lux": 14900.673828125,
            "radiance_lux": 14497.3681640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06737300228310494,
            "maximum_error_percentage_points": 0.5169863013698617,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03163129192486499,
            "maximum_error_percentage_points": 0.24125263675693986,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.030709189497716782,
            "maximum_error_percentage_points": 0.25068493150685,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07004851598173445,
            "maximum_error_percentage_points": 0.49561643835615854,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07111729452054813,
            "maximum_error_percentage_points": 0.49246575342465704,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004851508989730746,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_office_grid",
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
      "study_preparation_seconds": 0.3086168779991567,
      "weather_seconds": 0.2817877790002967,
      "metric_reduction_seconds": 2.6945434839981317,
      "write_seconds": 0.02496696699745371,
      "total_seconds": 3.001628661997529,
      "cold_end_to_end_seconds": 3.3102455399966857,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012171013000624953,
      "engine_upload_seconds": 0.048720586,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.157024743,
      "engine_annual_reduction_seconds": 0.044915616,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.157024743
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3086168779991567,
      "weather_seconds": 0.2548866779980017,
      "metric_reduction_seconds": 2.533487515000161,
      "write_seconds": 0.02459236799768405,
      "total_seconds": 2.813354284000525,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.813354284000525,
      "raw_export_seconds": 0.011748328000976471,
      "engine_upload_seconds": 0.047565445,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.9e-08,
      "engine_annual_reduction_seconds": 0.045451248,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022388091001630528,
      "full": 0.17186722900078166
    }
  },
  "elapsed_seconds": 10.651863200000662,
  "result_class": "passed"
}
```
