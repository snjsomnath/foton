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
  "model_sha256": "ae0bd42e908e8c15d6604192c7a129fbc3ea59ec589babbf839e94091f489982",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17113111844658936175,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17113111844658936175,
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
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/teaching_office/mf2/oracle/scene.rad"
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
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
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
            "nmbe_percent": -1.9075761961423428,
            "cvrmse_percent": 63.501507917043774,
            "rms_normalized_rmse_percent": 3.47116209702042,
            "reference_energy": 26.813211485065203,
            "candidate_energy": 26.301729045354797,
            "relative_energy_error_percent": 1.9075761961423325,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.116697288087835e-08,
              "p90": 1.839788601500916e-05,
              "p95": 3.190804272890091e-05,
              "p99": 6.699243996990834e-05,
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
            "nmbe_percent": -0.7928286807830325,
            "cvrmse_percent": 26.642309961501994,
            "rms_normalized_rmse_percent": 3.470479642158155,
            "reference_energy": 63.896283960808596,
            "candidate_energy": 63.389695895612746,
            "relative_energy_error_percent": 0.7928286807830173,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.095593813564392e-08,
              "p90": 1.8293585162609817e-05,
              "p95": 3.1409901566803455e-05,
              "p99": 6.601462722755963e-05,
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
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
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
            "nmbe_percent": 69.41212846493728,
            "cvrmse_percent": 592.1797035289413,
            "rms_normalized_rmse_percent": 23.02057288867502,
            "reference_energy": 15.525292836869342,
            "candidate_energy": 26.301729045354797,
            "relative_energy_error_percent": 69.41212846493728,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015659483906347324,
              "p95": 0.00022462999913841486,
              "p99": 0.00035455461125820847,
              "maximum": 0.018875855952501297
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05774024501442909,
              "candidate": 0.07661610096693039,
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
            "nmbe_percent": 20.49356698109607,
            "cvrmse_percent": 174.76240082277533,
            "rms_normalized_rmse_percent": 23.021075969140366,
            "reference_energy": 52.60836531261273,
            "candidate_energy": 63.389695895612746,
            "relative_energy_error_percent": 20.49356698109609,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015658881748095157,
              "p95": 0.00022513000294566154,
              "p99": 0.00035547901643440084,
              "maximum": 0.018875855952501297
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05774024501442909,
              "candidate": 0.07661610096693039,
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
      "bias_percent": 0.14721618162901925,
      "rms_normalized_error_percent": 0.1869261200074916,
      "absolute_error": {
        "p95": 0.14327891505649504,
        "p99": 0.18577935859906486,
        "maximum": 0.19639526742801117
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.44113234550767,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1869261200074916
    },
    "overcast": {
      "bias_percent": 0.10592885572448972,
      "rms_normalized_error_percent": 0.1450795338949178,
      "absolute_error": {
        "p95": 0.07764244079589844,
        "p99": 0.10219421386718745,
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
      "rms_normalized_to_uniform_percent": 0.10162789373677676
    },
    "horizon": {
      "bias_percent": 0.8167184847627571,
      "rms_normalized_error_percent": 1.6424508362568735,
      "absolute_error": {
        "p95": 0.1454560608121369,
        "p99": 0.18727668662944716,
        "maximum": 0.1921921160187603
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4819081981431794,
      "reference_fraction_of_uniform": 0.12242509038825782,
      "rms_normalized_to_uniform_percent": 0.150659001305937
    },
    "north": {
      "bias_percent": -62.92040155256186,
      "rms_normalized_error_percent": 91.96883924659767,
      "absolute_error": {
        "p95": 6.0987127653788775e-05,
        "p99": 0.00015593177731716397,
        "maximum": 0.00024276126168842893
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.399520715494873e-05,
      "reference_fraction_of_uniform": 4.92076310365519e-07,
      "rms_normalized_to_uniform_percent": 9.1037857997091e-05
    },
    "east": {
      "bias_percent": 0.07554238333444857,
      "rms_normalized_error_percent": 0.1818830734774348,
      "absolute_error": {
        "p95": 0.03149104118347168,
        "p99": 0.04030134677886961,
        "maximum": 0.04742288589477539
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.44733190536499,
      "reference_fraction_of_uniform": 0.19153006374835968,
      "rms_normalized_to_uniform_percent": 0.037188594299739024
    },
    "south": {
      "bias_percent": 0.1913788120895487,
      "rms_normalized_error_percent": 0.25912435374684517,
      "absolute_error": {
        "p95": 0.14481806755065918,
        "p99": 0.18765280246734617,
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
      "rms_normalized_to_uniform_percent": 0.16430734862957322
    },
    "west": {
      "bias_percent": 0.10296351687554664,
      "rms_normalized_error_percent": 0.16500527931309739,
      "absolute_error": {
        "p95": 0.025884270668029785,
        "p99": 0.043586301803588856,
        "maximum": 0.04624176025390625
      },
      "worst_index": [
        95
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.5115203857421875,
      "reference_fraction_of_uniform": 0.19378696382045746,
      "rms_normalized_to_uniform_percent": 0.03399633833563773
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
          "nmbe_percent": -0.01595426235824491,
          "cvrmse_percent": 1.1167443414904796,
          "absolute_error_percentiles_lux": {
            "p50": 3.86700439453125,
            "p90": 38.80104980468751,
            "p95": 59.631137084960926,
            "p99": 118.53833007812551
          },
          "maximum_absolute_error_lux": 403.306640625,
          "worst": {
            "sensor_index": 45,
            "position": [
              5.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1857.5,
            "foton_lux": 14900.6748046875,
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
            "mean_absolute_error_percentage_points": 0.07036101598173446,
            "maximum_error_percentage_points": 0.49561643835615854,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07142979452054812,
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
      "study_preparation_seconds": 0.006644333014264703,
      "weather_seconds": 0.09837420901749283,
      "metric_reduction_seconds": 0.2615916249342263,
      "write_seconds": 0.041863708989694715,
      "total_seconds": 0.40196262497920543,
      "cold_end_to_end_seconds": 0.40860695799347013,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.014701624982990324,
      "engine_upload_seconds": 0.000862333,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.20116141682956368,
      "engine_annual_reduction_seconds": 0.0037352084182202816,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.20116141682956368
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006644333014264703,
      "weather_seconds": 0.09785100002773106,
      "metric_reduction_seconds": 0.0502303329994902,
      "write_seconds": 0.03400233306456357,
      "total_seconds": 0.18262433295603842,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18262433295603842,
      "raw_export_seconds": 0.012970416923053563,
      "engine_upload_seconds": 9.15e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0036994999973103404,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022970541031099856,
      "full": 0.2046679159393534
    }
  },
  "elapsed_seconds": 2.1176829170435667,
  "result_class": "passed"
}
```
