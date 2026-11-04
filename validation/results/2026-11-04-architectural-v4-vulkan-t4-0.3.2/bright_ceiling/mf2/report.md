# Foton report

Status: **passed**

```json
{
  "scene": "bright_ceiling",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "bright_ceiling",
    "category": "materials",
    "question": "How much does changing only ceiling reflectance redistribute light?",
    "interactions": [
      "ceiling_reflection",
      "surface_specific_materials"
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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "0df946a0f7e7f1f69b5c1a3c9f8b319b912acaad33a677c44268975887401171",
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
      "scene_fingerprint": 2231201896356868392,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 2231201896356868392,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
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
    "model_sha256": "82370d362cdea70b8a5f2183e8f3465cf65a4ccdc7fc6b9d8bdf23696e25626c",
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
          "maximum": 0.00014028436271473765,
          "p95": 3.259629011154175e-08,
          "p99": 7.011898560449481e-06
        },
        "bias_percent": -0.02574736435175291,
        "identifier": "bright_ceiling_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7597631247218805,
        "worst_index": [
          17,
          543,
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
          "maximum": 0.0008914023637771606,
          "p95": 2.5675646611489356e-05,
          "p99": 0.00010892609134316444
        },
        "bias_percent": 0.14471571817437262,
        "identifier": "bright_ceiling_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2697116777331714,
        "worst_index": [
          8,
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
          "maximum": 0.0007976740598678589,
          "p95": 2.254096034448594e-05,
          "p99": 8.125603199005127e-05
        },
        "bias_percent": 0.025500837964338,
        "identifier": "bright_ceiling_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0174531762771934,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "bright_ceiling_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007297985721379519,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.213553620502353e-05,
                  "p99": 0.0001879222982097417
                },
                "candidate_energy": 6.023775100642524,
                "cvrmse_percent": 39.167010218323554,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06900736227353847,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.019621118889518,
                "relative_energy_error_percent": 0.06900736227353847,
                "rms_normalized_rmse_percent": 7.546923569149249,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035469569265842438,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004276755498722196,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011658788716886193,
                  "p50": 0.0,
                  "p90": 5.360834484235984e-06,
                  "p95": 4.678924597101286e-05,
                  "p99": 0.0003011405060533434
                },
                "candidate_energy": 3.1745313508733695,
                "cvrmse_percent": 111.22799782471938,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.640015594716613,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.194979719325083,
                "relative_energy_error_percent": 0.6400155947166131,
                "rms_normalized_rmse_percent": 4.367826947793089,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00043009937508031726,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": -0.000735779496608302,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.05279101058841,
            "full": 257.3917079716921
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.83649997413158,
            "full": 272.15545799117535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.82712503615767,
            "full": 236.60004197154194
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.17887503840029,
            "full": 235.6701249955222
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
            "identifier": "bright_ceiling_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036352750612422824,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.277200110256672e-05,
                  "p99": 0.00013709417544305325
                },
                "candidate_energy": 6.015145111995025,
                "cvrmse_percent": 25.514850857623905,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.018124587941390914,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.016235529894402,
                "relative_energy_error_percent": 0.01812458794139091,
                "rms_normalized_rmse_percent": 4.91856198911401,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013851054827682674,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0017486329888924956,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012113582342863083,
                  "p50": 4.9999993478877514e-08,
                  "p90": 1.9962717578891943e-05,
                  "p95": 4.3225598346907645e-05,
                  "p99": 0.00019990719738416374
                },
                "candidate_energy": 6.563452014209801,
                "cvrmse_percent": 39.356123484366236,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.14513534894954278,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.572991748720732,
                "relative_energy_error_percent": 0.14513534894954275,
                "rms_normalized_rmse_percent": 2.1607596319768376,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05829877592623234,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.059510134160518646,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.36820799205452,
            "full": 2331.8838749546558
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.69191704969853,
            "full": 2370.9977089893073
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.86620796844363,
            "full": 2407.184374984354
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.23666607402265,
            "full": 2355.5918749189004
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
            "identifier": "bright_ceiling_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00033077227999456227,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2694923245580867e-05,
                  "p99": 0.00013638287782669067
                },
                "candidate_energy": 6.019248734080065,
                "cvrmse_percent": 24.63767205723249,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.16580144152121556,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.009285252506288,
                "relative_energy_error_percent": 0.16580144152121556,
                "rms_normalized_rmse_percent": 4.747001206406455,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008163171878550202,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0011470894678495824,
                  "rgb_channel": 0,
                  "sky_patch_index": 84
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012142788618803024,
                  "p50": 4.9999993478877514e-08,
                  "p90": 1.9954553681600384e-05,
                  "p95": 4.310090298531577e-05,
                  "p99": 0.00020438001956790686
                },
                "candidate_energy": 6.585122034196946,
                "cvrmse_percent": 39.48745148208164,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08297160151201857,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.590590352561563,
                "relative_energy_error_percent": 0.08297160151201857,
                "rms_normalized_rmse_percent": 2.171693601633227,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03724073991179466,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.03602646104991436,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.56220804620534,
            "full": 2633.214166969992
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.08729203045368,
            "full": 2741.36983405333
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.77483302168548,
            "full": 2627.1954169496894
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.49429097678512,
            "full": 2646.9211250077933
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
            "identifier": "bright_ceiling_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021118461154401302,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1541516869328916e-05,
                  "p99": 7.32014887034893e-05
                },
                "candidate_energy": 6.0180097867528275,
                "cvrmse_percent": 14.571329775760894,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04208271593230228,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.015478310103617,
                "relative_energy_error_percent": 0.04208271593230228,
                "rms_normalized_rmse_percent": 2.8093749980467955,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003829235560260713,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0036180509487167,
                  "rgb_channel": 0,
                  "sky_patch_index": 310
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007973033934831619,
                  "p50": 5.000000058430487e-08,
                  "p90": 1.382862683385612e-05,
                  "p95": 2.6546273147687316e-05,
                  "p99": 0.0001098335487768054
                },
                "candidate_energy": 6.589144117490534,
                "cvrmse_percent": 24.03380890132252,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.016739993647274607,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.588041279798816,
                "relative_energy_error_percent": 0.016739993647274607,
                "rms_normalized_rmse_percent": 1.3212607214157712,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05929323844611645,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.058495935052633286,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.05704104248434,
            "full": 5048.1296660145745
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.11316700000316,
            "full": 5025.3992499783635
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.1239159880206,
            "full": 4995.28629204724
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.88729192968458,
            "full": 5038.851459044963
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
    "/content/suite-vulkan-0.3.2/bright_ceiling/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2820.63674996607,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/bright_ceiling/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10877.246041083708,
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
        "identifier": "bright_ceiling_grid",
        "full_identifier": "bright_ceiling_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025461117730995884,
            "cvrmse_percent": 2.186222441579374,
            "rms_normalized_rmse_percent": 0.42172699914116524,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628488199378,
            "relative_energy_error_percent": 0.02546111773099588,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.1278988141566515e-06,
              "maximum": 5.949428305029869e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052888810634613,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.664550853186293,
            "cvrmse_percent": 48.84337134725589,
            "rms_normalized_rmse_percent": 2.6851022411996897,
            "reference_energy": 6.5891764760361315,
            "candidate_energy": 6.479496282786322,
            "relative_energy_error_percent": 1.664550853186293,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.999999703159119e-08,
              "p90": 1.4720009312441112e-05,
              "p95": 2.2714499209541827e-05,
              "p99": 4.999293014407158e-05,
              "maximum": 0.002116188406944275
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04896080866456032,
              "candidate": 0.04684462025761604,
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
            "nmbe_percent": -0.8822610386454701,
            "cvrmse_percent": 25.5242476881997,
            "rms_normalized_rmse_percent": 2.684302509616788,
            "reference_energy": 12.605336745884701,
            "candidate_energy": 12.4941247709857,
            "relative_energy_error_percent": 0.8822610386454702,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.999999703159119e-08,
              "p90": 1.4718904822075279e-05,
              "p95": 2.267182571813464e-05,
              "p99": 5.0725764594972134e-05,
              "maximum": 0.002116188406944275
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04896080866456032,
              "candidate": 0.04684462025761604,
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
        "identifier": "bright_ceiling_grid",
        "full_identifier": "bright_ceiling_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025461117730995884,
            "cvrmse_percent": 2.186222441579374,
            "rms_normalized_rmse_percent": 0.42172699914116524,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628488199378,
            "relative_energy_error_percent": 0.02546111773099588,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.1278988141566515e-06,
              "maximum": 5.949428305029869e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052888810634613,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 103.10032847710995,
            "cvrmse_percent": 1235.3646168275968,
            "rms_normalized_rmse_percent": 48.54456264635727,
            "reference_energy": 3.1902933547035506,
            "candidate_energy": 6.479496282786322,
            "relative_energy_error_percent": 103.10032847710995,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.400750059285205e-05,
              "p95": 0.00012579299800563604,
              "p99": 0.00021241465583443642,
              "maximum": 0.016772501170635223
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024784069508314133,
              "candidate": 0.041556570678949356,
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
            "nmbe_percent": 35.71050570076075,
            "cvrmse_percent": 428.0847477191627,
            "rms_normalized_rmse_percent": 48.54415432302545,
            "reference_energy": 9.20645362455212,
            "candidate_energy": 12.4941247709857,
            "relative_energy_error_percent": 35.71050570076075,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.399916889378803e-05,
              "p95": 0.000125639999168925,
              "p99": 0.00021313445176929235,
              "maximum": 0.016772501170635223
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024784069508314133,
              "candidate": 0.041556570678949356,
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
      "bias_percent": 0.10536387781732144,
      "rms_normalized_error_percent": 0.19306100187185268,
      "absolute_error": {
        "p95": 0.08593164191349234,
        "p99": 0.11269675859760274,
        "maximum": 0.1216683513331267
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.165960915696582,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19306100187185268
    },
    "overcast": {
      "bias_percent": 0.06683363072026588,
      "rms_normalized_error_percent": 0.14370024853318294,
      "absolute_error": {
        "p95": 0.04175323247909546,
        "p99": 0.05660679340362547,
        "maximum": 0.061920166015625
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.40465259552002,
      "reference_fraction_of_uniform": 0.6383622288703918,
      "rms_normalized_to_uniform_percent": 0.10157191881849223
    },
    "horizon": {
      "bias_percent": 0.6258132998873892,
      "rms_normalized_error_percent": 1.721211564935544,
      "absolute_error": {
        "p95": 0.056227375395901724,
        "p99": 0.09253147192619576,
        "maximum": 0.11072438335061352
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6495282788770425,
      "reference_fraction_of_uniform": 0.12528734434495087,
      "rms_normalized_to_uniform_percent": 0.13292944969426673
    },
    "north": {
      "bias_percent": -82.90537858364993,
      "rms_normalized_error_percent": 97.33887488370749,
      "absolute_error": {
        "p95": 6.686825327051338e-05,
        "p99": 0.00011930511464015575,
        "maximum": 0.00013438944006338716
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.597868322278373e-05,
      "reference_fraction_of_uniform": 1.2136358691350324e-06,
      "rms_normalized_to_uniform_percent": 0.00014051030140834215
    },
    "east": {
      "bias_percent": -0.06178092718888722,
      "rms_normalized_error_percent": 0.30709923458639654,
      "absolute_error": {
        "p95": 0.024949342012405396,
        "p99": 0.03512458801269529,
        "maximum": 0.040435791015625
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4929072856903076,
      "reference_fraction_of_uniform": 0.1893448680639267,
      "rms_normalized_to_uniform_percent": 0.06167464843803873
    },
    "south": {
      "bias_percent": 0.17414520564298672,
      "rms_normalized_error_percent": 0.2586180996593766,
      "absolute_error": {
        "p95": 0.07303822040557861,
        "p99": 0.1052581906318664,
        "maximum": 0.11857867240905762
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.16873550415039,
      "reference_fraction_of_uniform": 0.6963969469070435,
      "rms_normalized_to_uniform_percent": 0.16965929974449792
    },
    "west": {
      "bias_percent": 0.08750720215949156,
      "rms_normalized_error_percent": 0.26697607617592783,
      "absolute_error": {
        "p95": 0.01945960521697998,
        "p99": 0.037805604934692344,
        "maximum": 0.04742097854614258
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5222551822662354,
      "reference_fraction_of_uniform": 0.19157394766807556,
      "rms_normalized_to_uniform_percent": 0.05404575319813803
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
        "identifier": "bright_ceiling_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.06743619352390194,
          "cvrmse_percent": 2.0368787590658886,
          "absolute_error_percentiles_lux": {
            "p50": 3.00372314453125,
            "p90": 33.706109619140655,
            "p95": 51.39551696777343,
            "p99": 101.45585449218729
          },
          "maximum_absolute_error_lux": 345.21875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 43210.28125,
            "radiance_lux": 43555.5
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.19709665144596655,
            "maximum_error_percentage_points": 1.010958904109593,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07113147778462074,
            "maximum_error_percentage_points": 0.33195101253518544,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.05912861491628618,
            "maximum_error_percentage_points": 0.24712328767123282,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08566971080669737,
            "maximum_error_percentage_points": 0.36027397260274086,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04557458143074619,
            "maximum_error_percentage_points": 0.27602739726027536,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
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
      "maximum_error_percentage_points": 0.004931506849302991,
      "metrics": {
        "da": [
          {
            "identifier": "bright_ceiling_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "bright_ceiling_grid",
            "maximum_error_percentage_points": 0.004337542808215744,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "bright_ceiling_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "bright_ceiling_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "bright_ceiling_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
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
      "study_preparation_seconds": 0.35676514799979486,
      "weather_seconds": 0.2293128539999998,
      "metric_reduction_seconds": 0.9761233620001804,
      "write_seconds": 0.01437996499998917,
      "total_seconds": 1.220171131999905,
      "cold_end_to_end_seconds": 1.5769362799996998,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0017567049999342998,
      "engine_upload_seconds": 0.04861128,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.030655425,
      "engine_annual_reduction_seconds": 0.017431066,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.030655425
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35676514799979486,
      "weather_seconds": 0.26393884700019044,
      "metric_reduction_seconds": 0.9746140160000323,
      "write_seconds": 0.013214048000008916,
      "total_seconds": 1.2520245169998816,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2520245169998816,
      "raw_export_seconds": 0.0016510270002072502,
      "engine_upload_seconds": 0.0441522,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.017579233,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018186630000400328,
      "full": 0.0494156079998902
    }
  },
  "elapsed_seconds": 5.889637424999819,
  "result_class": "passed"
}
```
