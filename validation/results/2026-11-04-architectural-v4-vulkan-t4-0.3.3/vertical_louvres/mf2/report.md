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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "04441f9f59dede71304e252d24d4a12d5c191c45989ebb3e961da55f1a28b750",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 3773948157984095676,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 3773948157984095676,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
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
    "model_sha256": "03fd66d43132917beb8d3fbd505eb50f3ce96c124a8afc3befa7608317acf207",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00019560952205210924,
          "p95": 0.0,
          "p99": 1.1983021977357566e-05
        },
        "bias_percent": -0.18915669137121993,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7016252083337124,
        "worst_index": [
          10,
          357,
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
          "maximum": 0.00028386758640408516,
          "p95": 1.2266703379282262e-05,
          "p99": 6.573391146957874e-05
        },
        "bias_percent": 0.142136759898829,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.301688737944874,
        "worst_index": [
          23,
          92,
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
          "maximum": 0.00038665346801280975,
          "p95": 1.0377361832070164e-05,
          "p99": 5.268142558634281e-05
        },
        "bias_percent": -0.1426464633738446,
        "identifier": "vertical_louvres_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9395278844812305,
        "worst_index": [
          17,
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004861384513787925,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011615005860221572
                },
                "candidate_energy": 2.626039881502038,
                "cvrmse_percent": 52.008037724052606,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.00021036316442650963,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.626034357293065,
                "relative_energy_error_percent": 0.0002103631644265096,
                "rms_normalized_rmse_percent": 6.8476961115156865,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001732283504679799,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0022184219560585916,
                  "rgb_channel": 0,
                  "sky_patch_index": 359
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007880927296355367,
                  "p50": 0.0,
                  "p90": 9.031171839524183e-06,
                  "p95": 1.8498994677429437e-05,
                  "p99": 0.00017314089927822351
                },
                "candidate_energy": 0.9655978488379571,
                "cvrmse_percent": 216.34267141660072,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.28487634309793713,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9628549030009488,
                "relative_energy_error_percent": 0.28487634309793713,
                "rms_normalized_rmse_percent": 7.1332333023694305,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00037261025863699615,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": -0.0004154824709985405,
                  "rgb_channel": 0,
                  "sky_patch_index": 359
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.19999999552965,
            "full": 237.94866702519357
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.49866696540266,
            "full": 226.95754107553512
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.40758395008743,
            "full": 233.60570799559355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.08979098126292,
            "full": 229.81795901432633
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.19079091399908,
            "full": 229.7650419641286
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.59075002372265,
            "full": 255.4452499607578
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.71600000932813,
            "full": 241.44158302806318
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.99391693156213,
            "full": 232.29366703890264
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00027601851616054773,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.011083966470324e-05
                },
                "candidate_energy": 2.6236024969525715,
                "cvrmse_percent": 37.18692071076024,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.05459068468753221,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6221710358304335,
                "relative_energy_error_percent": 0.054590684687532205,
                "rms_normalized_rmse_percent": 4.881888337525336,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003535831463523209,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0032598129473626614,
                  "rgb_channel": 0,
                  "sky_patch_index": 264
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004310249350965023,
                  "p50": 6.759571107295415e-07,
                  "p90": 9.52207076352356e-06,
                  "p95": 1.8397695384919643e-05,
                  "p99": 0.0001315910012635868
                },
                "candidate_energy": 1.7950595367576874,
                "cvrmse_percent": 87.28595554297536,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1355933632825985,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7926288510074322,
                "relative_energy_error_percent": 0.13559336328259852,
                "rms_normalized_rmse_percent": 4.341610949269108,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015321414917707443,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.014890389982610941,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.4538750005886,
            "full": 2452.1582500310615
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.24954102933407,
            "full": 2420.4526250250638
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.1683339914307,
            "full": 2455.379582941532
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.30195795930922,
            "full": 2428.7597499787807
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003009084612131119,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.199845953844488e-05
                },
                "candidate_energy": 2.622564009169764,
                "cvrmse_percent": 41.74221780177413,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.13758007352217405,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6261771055624195,
                "relative_energy_error_percent": 0.13758007352217405,
                "rms_normalized_rmse_percent": 5.48079396569115,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014126034802757204,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0011116950190626085,
                  "rgb_channel": 0,
                  "sky_patch_index": 209
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00048640090972185135,
                  "p50": 6.775349881138482e-07,
                  "p90": 9.619531374482942e-06,
                  "p95": 1.8276570244779577e-05,
                  "p99": 0.00013213478450779803
                },
                "candidate_energy": 1.8027464661197925,
                "cvrmse_percent": 91.22728658746327,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4578653790797215,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7945299348309796,
                "relative_energy_error_percent": 0.4578653790797216,
                "rms_normalized_rmse_percent": 4.542746965086564,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.016445609740912914,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.016932010650634766,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.25933301914483,
            "full": 2572.25887500681
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.19866699445993,
            "full": 2572.4928750423715
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.88616700470448,
            "full": 2587.0110830292106
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.32408297155052,
            "full": 2562.294999952428
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
            "identifier": "vertical_louvres_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00015129019448067993,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.0582246331032366e-05
                },
                "candidate_energy": 2.623074406682008,
                "cvrmse_percent": 23.107927912675205,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1320322478631099,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6196156692285513,
                "relative_energy_error_percent": 0.1320322478631099,
                "rms_normalized_rmse_percent": 3.034599614111811,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0004998949443688616,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0006511851388495415,
                  "rgb_channel": 0,
                  "sky_patch_index": 88
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004929900169372559,
                  "p50": 5.713928885597852e-07,
                  "p90": 6.932460610187281e-06,
                  "p95": 1.2755442753586976e-05,
                  "p99": 7.94099469203502e-05
                },
                "candidate_energy": 1.7934205591279877,
                "cvrmse_percent": 54.27098871072288,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.21519921336258133,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7972883094317424,
                "relative_energy_error_percent": 0.21519921336258135,
                "rms_normalized_rmse_percent": 2.7040696362636836,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.012861944735050201,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.013354934751987457,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.33216698095202,
            "full": 4446.659375098534
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.92329202592373,
            "full": 4384.0576249640435
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.1674590818584,
            "full": 4504.308582982048
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.71575005166233,
            "full": 4464.638666948304
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
    "/content/suite-vulkan-0.3.3/vertical_louvres/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2556.0356250498444,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/vertical_louvres/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10837.811792036518,
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
        "identifier": "vertical_louvres_grid",
        "full_identifier": "vertical_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.12300663661415101,
            "cvrmse_percent": 6.6336675699423,
            "rms_normalized_rmse_percent": 0.8713387963654421,
            "reference_energy": 2.6192402014489744,
            "candidate_energy": 2.6224620407256225,
            "relative_energy_error_percent": 0.12300663661415104,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.399307262152433e-06,
              "maximum": 7.983611430972815e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 514,
              "rgb_channel": 0,
              "reference": 0.0013412853004410863,
              "candidate": 0.0014211214147508144,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4438572837523102,
            "cvrmse_percent": 40.609965340652224,
            "rms_normalized_rmse_percent": 2.024251634002538,
            "reference_energy": 1.7974592767154327,
            "candidate_energy": 1.7894811227932497,
            "relative_energy_error_percent": 0.44385728375231015,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.48515168677477e-07,
              "p90": 6.294063814493717e-06,
              "p95": 1.0825828212546185e-05,
              "p99": 3.4805736504495144e-05,
              "maximum": 0.0006241500377655029
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012533679604530334,
              "candidate": 0.011909529566764832,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.10768934289166718,
            "cvrmse_percent": 16.354776618180196,
            "rms_normalized_rmse_percent": 2.0031583721999877,
            "reference_energy": 4.416699478164407,
            "candidate_energy": 4.411943163518872,
            "relative_energy_error_percent": 0.10768934289166716,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.481210732545151e-07,
              "p90": 6.240730999707013e-06,
              "p95": 1.0659336112439632e-05,
              "p99": 3.3919495763257146e-05,
              "maximum": 0.0006241500377655029
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012533679604530334,
              "candidate": 0.011909529566764832,
              "position": [
                1.5,
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
        "identifier": "vertical_louvres_grid",
        "full_identifier": "vertical_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.12300663661415101,
            "cvrmse_percent": 6.6336675699423,
            "rms_normalized_rmse_percent": 0.8713387963654421,
            "reference_energy": 2.6192402014489744,
            "candidate_energy": 2.6224620407256225,
            "relative_energy_error_percent": 0.12300663661415104,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.399307262152433e-06,
              "maximum": 7.983611430972815e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 514,
              "rgb_channel": 0,
              "reference": 0.0013412853004410863,
              "candidate": 0.0014211214147508144,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 84.2881782275826,
            "cvrmse_percent": 903.3294536121712,
            "rms_normalized_rmse_percent": 30.105749670869585,
            "reference_energy": 0.9710232853804488,
            "candidate_energy": 1.7894811227932497,
            "relative_energy_error_percent": 84.28817822758262,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4500000133921276e-06,
              "p90": 2.6722348229668648e-05,
              "p95": 4.731444641947746e-05,
              "p99": 9.971817780751735e-05,
              "maximum": 0.0037898197770118713
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014442039653658867,
              "candidate": 0.018231859430670738,
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
            "nmbe_percent": 22.886333543588407,
            "cvrmse_percent": 244.29566088922434,
            "rms_normalized_rmse_percent": 30.103410876785862,
            "reference_energy": 3.590263486829423,
            "candidate_energy": 4.411943163518872,
            "relative_energy_error_percent": 22.886333543588407,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4500000133921276e-06,
              "p90": 2.6722348229668648e-05,
              "p95": 4.7241803258657455e-05,
              "p99": 9.899004362523556e-05,
              "maximum": 0.0037898197770118713
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014442039653658867,
              "candidate": 0.018231859430670738,
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
      "bias_percent": 0.3540375427684458,
      "rms_normalized_error_percent": 0.3276163248859727,
      "absolute_error": {
        "p95": 0.07089521720172431,
        "p99": 0.09374111444152922,
        "maximum": 0.10428197570217801
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.360578771504434,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3276163248859727
    },
    "overcast": {
      "bias_percent": 0.2583494483200837,
      "rms_normalized_error_percent": 0.23883076791338712,
      "absolute_error": {
        "p95": 0.04592451453208923,
        "p99": 0.05320868492126465,
        "maximum": 0.054309844970703125
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.638111114501953,
      "reference_fraction_of_uniform": 0.6786788105964661,
      "rms_normalized_to_uniform_percent": 0.17794322547486846
    },
    "horizon": {
      "bias_percent": 1.8070187212148192,
      "rms_normalized_error_percent": 3.7172599083214326,
      "absolute_error": {
        "p95": 0.04552263678936097,
        "p99": 0.06744905636628126,
        "maximum": 0.07605748756089381
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48030356938403973,
      "reference_fraction_of_uniform": 0.08959919998512468,
      "rms_normalized_to_uniform_percent": 0.1911858629545656
    },
    "north": {
      "bias_percent": -2.132692455255099,
      "rms_normalized_error_percent": 7.297801703865389,
      "absolute_error": {
        "p95": 0.0013383871410042048,
        "p99": 0.0017995200119912617,
        "maximum": 0.0019615450873970985
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.0074820611625909805,
      "reference_fraction_of_uniform": 0.0013957562623545527,
      "rms_normalized_to_uniform_percent": 0.006832567697676745
    },
    "east": {
      "bias_percent": 0.2947734387254844,
      "rms_normalized_error_percent": 0.5944443358433874,
      "absolute_error": {
        "p95": 0.011632714420557022,
        "p99": 0.013921821117401121,
        "maximum": 0.014520883560180664
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5544812679290771,
      "reference_fraction_of_uniform": 0.10343683511018753,
      "rms_normalized_to_uniform_percent": 0.05716017172687953
    },
    "south": {
      "bias_percent": 0.459403125951108,
      "rms_normalized_error_percent": 0.4278341616221853,
      "absolute_error": {
        "p95": 0.06845608353614807,
        "p99": 0.08953238129615779,
        "maximum": 0.09995388984680176
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9319889545440674,
      "reference_fraction_of_uniform": 0.7335008382797241,
      "rms_normalized_to_uniform_percent": 0.2917853319399351
    },
    "west": {
      "bias_percent": 0.2923240321702714,
      "rms_normalized_error_percent": 0.5753147566391767,
      "absolute_error": {
        "p95": 0.01191680133342743,
        "p99": 0.013897594809532161,
        "maximum": 0.01491403579711914
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5674636363983154,
      "reference_fraction_of_uniform": 0.10585865378379822,
      "rms_normalized_to_uniform_percent": 0.056052988738493605
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
          "nmbe_percent": 0.3102248465901241,
          "cvrmse_percent": 3.138102759479175,
          "absolute_error_percentiles_lux": {
            "p50": 1.4154281616210938,
            "p90": 15.893525695800784,
            "p95": 26.36600646972654,
            "p99": 63.5614984130859
          },
          "maximum_absolute_error_lux": 253.45703125,
          "worst": {
            "sensor_index": 22,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2603.5,
            "foton_lux": 17742.6328125,
            "radiance_lux": 17489.17578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4252929984779293,
            "maximum_error_percentage_points": 1.1524657534246572,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2818198919799668,
            "maximum_error_percentage_points": 1.457232696286063,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4125266362252672,
            "maximum_error_percentage_points": 1.6412328767123299,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.418554033485541,
            "maximum_error_percentage_points": 1.6412328767123299,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0204261796042617,
            "maximum_error_percentage_points": 0.10643835616438357,
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
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.004884952910956031,
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
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "vertical_louvres_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.3847842509999282,
      "weather_seconds": 0.2534350480000285,
      "metric_reduction_seconds": 1.0193932590000259,
      "write_seconds": 0.013399533999972846,
      "total_seconds": 1.286559380999961,
      "cold_end_to_end_seconds": 1.6713436319998891,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016313839998929325,
      "engine_upload_seconds": 0.045145459000000006,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.035705607,
      "engine_annual_reduction_seconds": 0.036706741,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.035705607
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3847842509999282,
      "weather_seconds": 0.2574672959999589,
      "metric_reduction_seconds": 1.0113829110000552,
      "write_seconds": 0.012200529999972787,
      "total_seconds": 1.2813427359999423,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2813427359999423,
      "raw_export_seconds": 0.0014929940000456554,
      "engine_upload_seconds": 0.045886409,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.12e-07,
      "engine_annual_reduction_seconds": 0.039095862,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019495549000112078,
      "full": 0.053742372999977306
    }
  },
  "elapsed_seconds": 5.8060655609999685,
  "result_class": "passed"
}
```
