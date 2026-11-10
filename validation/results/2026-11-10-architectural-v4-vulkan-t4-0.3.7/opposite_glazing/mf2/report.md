# Foton report

Status: **passed**

```json
{
  "scene": "opposite_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "opposite_glazing",
    "category": "openings",
    "question": "How does glazing on opposite facades balance daylight?",
    "interactions": [
      "two_aspects",
      "bilateral_lighting"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 2,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 5.999999999999998
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "7fe40a2e16b9c3279005a83f177ada9632c78f979b01eb04e88956dba30ba49c",
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
      "scene_fingerprint": 6289786852115784515,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 6289786852115784515,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
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
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "e681fd9367c36c6ee9ccaa90de7f187b6d12beb4e2725d221a5707965aa9b569",
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
          "p95": 6.07222318649292e-07,
          "p99": 1.695746323093772e-05
        },
        "bias_percent": -0.014236103922258709,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7779311445677104,
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
          "maximum": 0.0007197856903076172,
          "p95": 5.413696635514498e-05,
          "p99": 0.0001237295800819993
        },
        "bias_percent": 0.02341626502546276,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3366140557355757,
        "worst_index": [
          22,
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
          "maximum": 0.0007412880659103394,
          "p95": 4.6001048758625984e-05,
          "p99": 0.00010128034045919776
        },
        "bias_percent": 0.039793321622469374,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1096895892187706,
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0010355322738178074,
                  "p50": 0.0,
                  "p90": 4.596771032083786e-05,
                  "p95": 0.00017065659631043673,
                  "p99": 0.00037235207855701447
                },
                "candidate_energy": 12.042184288405451,
                "cvrmse_percent": 38.92491806682478,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02860966808578052,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.038740044836914,
                "relative_energy_error_percent": 0.02860966808578052,
                "rms_normalized_rmse_percent": 10.601366500804158,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005652116960845888,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.0016007439699023962,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016124248504638672,
                  "p50": 0.0,
                  "p90": 6.44562096567825e-05,
                  "p95": 0.00021241838112473488,
                  "p99": 0.0005028959130868316
                },
                "candidate_energy": 3.967158781022121,
                "cvrmse_percent": 160.0432320601708,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3439128525226926,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.953561973263618,
                "relative_energy_error_percent": 0.34391285252269255,
                "rms_normalized_rmse_percent": 6.574620457204548,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04381661117076874,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.04220418632030487,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.4068749351427,
            "full": 242.7793750539422
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.35766698420048,
            "full": 244.4520000135526
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.1243749819696,
            "full": 241.43408297095448
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.63162494450808,
            "full": 241.10933300107718
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003695829364005476,
                  "p50": 0.0,
                  "p90": 2.2507231915369717e-05,
                  "p95": 6.996290176175535e-05,
                  "p99": 0.00017288647359237075
                },
                "candidate_energy": 12.040810868707354,
                "cvrmse_percent": 17.29902301683639,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03415524234470239,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.036699704752891,
                "relative_energy_error_percent": 0.03415524234470239,
                "rms_normalized_rmse_percent": 4.718535217863131,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008309395343530923,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.00120052247075364,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011151712387800217,
                  "p50": 3.7565141610684805e-06,
                  "p90": 3.413361173443285e-05,
                  "p95": 0.00010664143337635323,
                  "p99": 0.0002616805722936988
                },
                "candidate_energy": 7.1697476600893815,
                "cvrmse_percent": 45.73534992522938,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3289074932431842,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.193407315770454,
                "relative_energy_error_percent": 0.3289074932431842,
                "rms_normalized_rmse_percent": 2.580586363669451,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04819156974554062,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.04930674098432064,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.14479100238532,
            "full": 2313.3435000199825
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.00354096386582,
            "full": 2297.803874942474
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.14820797275752,
            "full": 2330.9491249965504
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.92670789454132,
            "full": 2302.9323749942705
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00047277085832320154,
                  "p50": 0.0,
                  "p90": 2.229421734227799e-05,
                  "p95": 7.007195381447673e-05,
                  "p99": 0.000179190537892282
                },
                "candidate_energy": 12.04895235941217,
                "cvrmse_percent": 17.821161610087557,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.025024693796754545,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.045937900337663,
                "relative_energy_error_percent": 0.02502469379675454,
                "rms_normalized_rmse_percent": 4.86045820685698,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0012828870094381273,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0008101161511149257,
                  "rgb_channel": 0,
                  "sky_patch_index": 115
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009720828384160995,
                  "p50": 3.8052512536523864e-06,
                  "p90": 3.3761603845050565e-05,
                  "p95": 0.00010570813901722431,
                  "p99": 0.0002471600309945643
                },
                "candidate_energy": 7.179110996995021,
                "cvrmse_percent": 43.314498130246754,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04801452443968625,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.175665635264867,
                "relative_energy_error_percent": 0.04801452443968625,
                "rms_normalized_rmse_percent": 2.4373591808277792,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05183626897633076,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.05086418613791466,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.09287496004254,
            "full": 2391.6872499976307
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.7622499698773,
            "full": 2458.40116601903
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.84445900842547,
            "full": 2456.960791023448
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.08554100617766,
            "full": 2443.4233750216663
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020682445028796792,
                  "p50": 0.0,
                  "p90": 1.1426206037867818e-05,
                  "p95": 4.219706170260906e-05,
                  "p99": 9.426336328033358e-05
                },
                "candidate_energy": 12.037214518058306,
                "cvrmse_percent": 9.793354170613927,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.0594463789478134,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.044374462543203,
                "relative_energy_error_percent": 0.0594463789478134,
                "rms_normalized_rmse_percent": 2.6731703970348653,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018249789718538523,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0016181545215658844,
                  "rgb_channel": 0,
                  "sky_patch_index": 125
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006047803908586502,
                  "p50": 2.6723273549578153e-06,
                  "p90": 2.193195687141284e-05,
                  "p95": 6.310084427241236e-05,
                  "p99": 0.00014030374586582184
                },
                "candidate_energy": 7.197427618056743,
                "cvrmse_percent": 26.015542351272597,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15971301457294498,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.185950719536844,
                "relative_energy_error_percent": 0.159713014572945,
                "rms_normalized_rmse_percent": 1.4646832588839138,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04290921427309513,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.04351399466395378,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 222.53112494945526,
            "full": 4274.72999994643
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 218.93579105380923,
            "full": 4228.930875076912
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.32045909389853,
            "full": 4251.3870829716325
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.50075007975101,
            "full": 4250.0084158964455
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
    "/content/suite-vulkan-0.3.7/opposite_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2658.6458750534803,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10705.617833998986,
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
        "identifier": "opposite_glazing_grid",
        "full_identifier": "opposite_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1071051937988481,
            "cvrmse_percent": 2.021402763936447,
            "rms_normalized_rmse_percent": 0.5518084260527796,
            "reference_energy": 12.043795670928375,
            "candidate_energy": 12.03089614023429,
            "relative_energy_error_percent": 0.10710519379884811,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.651649992913681e-08,
              "p95": 1.079140929505229e-06,
              "p99": 1.8889200873672962e-05,
              "maximum": 9.540119208395481e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.002735236892476678,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.28729544522828,
            "cvrmse_percent": 22.8292369838043,
            "rms_normalized_rmse_percent": 1.2856662900773743,
            "reference_energy": 7.188688024255454,
            "candidate_energy": 7.168035250990097,
            "relative_energy_error_percent": 0.28729544522828,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.533487415552372e-06,
              "p90": 1.6110574324557103e-05,
              "p95": 2.652584225870669e-05,
              "p99": 5.931250052526593e-05,
              "maximum": 0.0012627467513084412
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05137287825345993,
              "candidate": 0.05011013150215149,
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
            "nmbe_percent": -0.17445642742358855,
            "cvrmse_percent": 8.529172910401575,
            "rms_normalized_rmse_percent": 1.2850780803927875,
            "reference_energy": 19.232483695183824,
            "candidate_energy": 19.198931391224384,
            "relative_energy_error_percent": 0.17445642742357467,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.536649899160693e-06,
              "p90": 1.6119515930768136e-05,
              "p95": 2.6475870981812477e-05,
              "p99": 5.8457255363464355e-05,
              "maximum": 0.0012627467513084412
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05137287825345993,
              "candidate": 0.05011013150215149,
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
        "identifier": "opposite_glazing_grid",
        "full_identifier": "opposite_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1071051937988481,
            "cvrmse_percent": 2.021402763936447,
            "rms_normalized_rmse_percent": 0.5518084260527796,
            "reference_energy": 12.043795670928375,
            "candidate_energy": 12.03089614023429,
            "relative_energy_error_percent": 0.10710519379884811,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.651649992913681e-08,
              "p95": 1.079140929505229e-06,
              "p99": 1.8889200873672962e-05,
              "maximum": 9.540119208395481e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.002735236892476678,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.14699364648745,
            "cvrmse_percent": 853.6537543217041,
            "rms_normalized_rmse_percent": 35.03677379314726,
            "reference_energy": 3.957026891088617,
            "candidate_energy": 7.168035250990097,
            "relative_energy_error_percent": 81.14699364648745,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3470000087399967e-05,
              "p90": 7.447000098181888e-05,
              "p95": 0.00010066351387649775,
              "p99": 0.0002061526756733656,
              "maximum": 0.01495574414730072
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01845204457640648,
              "candidate": 0.0334077887237072,
              "position": [
                0.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.987152640509343,
            "cvrmse_percent": 211.10147268416304,
            "rms_normalized_rmse_percent": 35.03538749374537,
            "reference_energy": 16.000822562016992,
            "candidate_energy": 19.198931391224384,
            "relative_energy_error_percent": 19.987152640509333,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.341335516575782e-05,
              "p90": 7.44400022085756e-05,
              "p95": 0.00010009000106947497,
              "p99": 0.00020538223907351494,
              "maximum": 0.01495574414730072
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01845204457640648,
              "candidate": 0.0334077887237072,
              "position": [
                0.5,
                5.5,
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
      "bias_percent": 0.0710918630019645,
      "rms_normalized_error_percent": 0.12559417836810313,
      "absolute_error": {
        "p95": 0.07183652005751129,
        "p99": 0.0754400906759412,
        "maximum": 0.07664151407475739
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.74303557882919,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.12559417836810313
    },
    "overcast": {
      "bias_percent": 0.07561970316949312,
      "rms_normalized_error_percent": 0.09707355192266251,
      "absolute_error": {
        "p95": 0.03839290142059326,
        "p99": 0.0426478624343872,
        "maximum": 0.04325151443481445
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.20216178894043,
      "reference_fraction_of_uniform": 0.6402787566184998,
      "rms_normalized_to_uniform_percent": 0.06735123643206463
    },
    "horizon": {
      "bias_percent": 0.3380391469731497,
      "rms_normalized_error_percent": 1.0818033158702873,
      "absolute_error": {
        "p95": 0.05043619926697629,
        "p99": 0.0665415024546144,
        "maximum": 0.07505301998480629
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.682105250110478,
      "reference_fraction_of_uniform": 0.1129638727619991,
      "rms_normalized_to_uniform_percent": 0.09043852769466884
    },
    "north": {
      "bias_percent": 0.06720467418476911,
      "rms_normalized_error_percent": 0.15598960916451327,
      "absolute_error": {
        "p95": 0.04529595375061035,
        "p99": 0.049600279331207274,
        "maximum": 0.049944162368774414
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.249391555786133,
      "reference_fraction_of_uniform": 0.34744468331336975,
      "rms_normalized_to_uniform_percent": 0.06719854635499263
    },
    "east": {
      "bias_percent": 0.1418551598156453,
      "rms_normalized_error_percent": 0.22436519091724288,
      "absolute_error": {
        "p95": 0.024724245071411133,
        "p99": 0.041793823242187465,
        "maximum": 0.04978466033935547
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.559504508972168,
      "reference_fraction_of_uniform": 0.19203543663024902,
      "rms_normalized_to_uniform_percent": 0.04549288126002286
    },
    "south": {
      "bias_percent": 0.02904084224849849,
      "rms_normalized_error_percent": 0.17936252191501867,
      "absolute_error": {
        "p95": 0.046630144119262695,
        "p99": 0.05359075069427489,
        "maximum": 0.05732297897338867
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.229677200317383,
      "reference_fraction_of_uniform": 0.34661436080932617,
      "rms_normalized_to_uniform_percent": 0.07709137383023952
    },
    "west": {
      "bias_percent": 0.11213892063557031,
      "rms_normalized_error_percent": 0.18432259612820576,
      "absolute_error": {
        "p95": 0.024783849716186523,
        "p99": 0.03254148960113524,
        "maximum": 0.03633546829223633
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.597842693328857,
      "reference_fraction_of_uniform": 0.19365015625953674,
      "rms_normalized_to_uniform_percent": 0.03759034737301453
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
        "identifier": "opposite_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.025788114799840795,
          "cvrmse_percent": 1.4663871097950967,
          "absolute_error_percentiles_lux": {
            "p50": 2.7905426025390625,
            "p90": 23.385675048828126,
            "p95": 37.370312499999955,
            "p99": 82.19432800292941
          },
          "maximum_absolute_error_lux": 345.798828125,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 31355.939453125,
            "radiance_lux": 31701.73828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08650304414003113,
            "maximum_error_percentage_points": 0.820547945205476,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03619958621303196,
            "maximum_error_percentage_points": 0.26413496484485677,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.038987823439878166,
            "maximum_error_percentage_points": 0.19013698630136844,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.05545662100456599,
            "maximum_error_percentage_points": 0.22205479452054533,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03289954337899543,
            "maximum_error_percentage_points": 0.10465753424657542,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 97.22222222222223,
          "radiance_percent": 97.22222222222223,
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
      "maximum_error_percentage_points": 0.004987692636987617,
      "metrics": {
        "da": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004987692636987617,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "opposite_glazing_grid",
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
      "study_preparation_seconds": 0.38801395099994807,
      "weather_seconds": 0.2589681780000319,
      "metric_reduction_seconds": 0.30934762000015326,
      "write_seconds": 0.012567927999953099,
      "total_seconds": 0.5812556460000451,
      "cold_end_to_end_seconds": 0.9692695969999932,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014734230001067772,
      "engine_upload_seconds": 0.063231214,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.039176284,
      "engine_annual_reduction_seconds": 0.008882238,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.039176284
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38801395099994807,
      "weather_seconds": 0.24748155099996438,
      "metric_reduction_seconds": 0.26826919200016164,
      "write_seconds": 0.011587345999942045,
      "total_seconds": 0.5276824729999134,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5276824729999134,
      "raw_export_seconds": 0.0015621800000644726,
      "engine_upload_seconds": 0.064233101,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 3.8e-08,
      "engine_annual_reduction_seconds": 0.008628859,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.027499007999949754,
      "full": 0.060895955999967555
    }
  },
  "elapsed_seconds": 4.321020156000031,
  "result_class": "passed"
}
```
