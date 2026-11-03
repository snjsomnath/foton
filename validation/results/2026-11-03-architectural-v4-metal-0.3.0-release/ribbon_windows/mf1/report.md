# Foton report

Status: **passed**

```json
{
  "scene": "ribbon_windows",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "ribbon_windows",
    "category": "openings",
    "question": "Do separated ribbon openings retain their opaque mullion gaps?",
    "interactions": [
      "multiple_openings",
      "punched_faces",
      "mullion_gaps"
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 6.3
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "5b6f6d35fb5d1d731fcbb887ed51053affc1f574644567bfc7269658a0513970",
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
      "scene_fingerprint": 6460232368099317047,
      "basis": "Tregenza",
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
      "scene_fingerprint": 6460232368099317047,
      "basis": "Tregenza",
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "9ca4013b3ed6a7c3b8b266ec42c5c237aa34f86744b49045e25cf8c225529e17",
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
          "maximum": 0.0004925327375531197,
          "p95": 4.009251351817483e-05,
          "p99": 0.0001543750986456871
        },
        "bias_percent": -0.10277271488948277,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.107730963469761,
        "worst_index": [
          10,
          95,
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
          "maximum": 0.0004917308688163757,
          "p95": 8.787894621491432e-05,
          "p99": 0.00018711714074015617
        },
        "bias_percent": -0.004511304650768706,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8133859477976116,
        "worst_index": [
          5,
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
          "maximum": 0.0005346760153770447,
          "p95": 7.242059800773854e-05,
          "p99": 0.00015734881162643433
        },
        "bias_percent": 0.03164919399380666,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.74496379730739,
        "worst_index": [
          7,
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007388221565634012,
                  "p50": 0.0,
                  "p90": 6.903510075062513e-05,
                  "p95": 0.00015279020881280286,
                  "p99": 0.0003397474065423012
                },
                "candidate_energy": 11.974781100697328,
                "cvrmse_percent": 8.838979500242878,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07649803803757024,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.96562763032125,
                "relative_energy_error_percent": 0.07649803803757026,
                "rms_normalized_rmse_percent": 2.4937291500246643,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012733804760500789,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.011994982603937387,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009983042255043983,
                  "p50": 0.0,
                  "p90": 0.00010544102406129241,
                  "p95": 0.00022377301938831783,
                  "p99": 0.00046755443327128887
                },
                "candidate_energy": 4.303922635847838,
                "cvrmse_percent": 35.8914952016291,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.09129970841654228,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.307855695536869,
                "relative_energy_error_percent": 0.0912997084165423,
                "rms_normalized_rmse_percent": 2.4875939195444436,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.039451802149415016,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.040450106374919415,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.16716704238206,
            "full": 241.34445807430893
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.64662505406886,
            "full": 245.8506670081988
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.85274998471141,
            "full": 241.2397499429062
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.8331250557676,
            "full": 237.7401249250397
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.5044160168618,
            "full": 258.5526250768453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.01433401182294,
            "full": 253.22845799382776
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.72033309191465,
            "full": 241.43270798958838
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.02574994787574,
            "full": 237.59408306796104
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004177410155534744,
                  "p50": 0.0,
                  "p90": 4.6538421884179115e-05,
                  "p95": 0.00010673676151782241,
                  "p99": 0.0002251738915219903
                },
                "candidate_energy": 11.973382680951545,
                "cvrmse_percent": 5.922796661644748,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0986050605515504,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.961587949910609,
                "relative_energy_error_percent": 0.09860506055155041,
                "rms_normalized_rmse_percent": 1.670694055331846,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007311440538614988,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.007729181554168463,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008126795291900635,
                  "p50": 3.4487317179809907e-07,
                  "p90": 8.026044815778732e-05,
                  "p95": 0.00017098216922022388,
                  "p99": 0.00033788569271564484
                },
                "candidate_energy": 7.704451045431792,
                "cvrmse_percent": 15.366388184113248,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.039479033230564425,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.707493889505674,
                "relative_energy_error_percent": 0.039479033230564425,
                "rms_normalized_rmse_percent": 1.528403739674761,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009759889217093587,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.00016330939251929522,
                  "rgb_channel": 0,
                  "sky_patch_index": 13
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.35499998927116,
            "full": 2308.185665984638
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.07333298027515,
            "full": 2238.96549991332
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.12762500718236,
            "full": 2262.944541987963
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.83087492268533,
            "full": 2266.5228330297396
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004926072433590889,
                  "p50": 0.0,
                  "p90": 4.5701395720243454e-05,
                  "p95": 0.00010120380902662872,
                  "p99": 0.00020474987104535103
                },
                "candidate_energy": 11.976033655857464,
                "cvrmse_percent": 5.5989884387503,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.051304869757026396,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.969892518091001,
                "relative_energy_error_percent": 0.05130486975702639,
                "rms_normalized_rmse_percent": 1.5798546269859943,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004640375962480903,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.004147768719121814,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008595306426286697,
                  "p50": 3.4079927502261853e-07,
                  "p90": 7.709593046456575e-05,
                  "p95": 0.0001688810443738475,
                  "p99": 0.00034441205207258463
                },
                "candidate_energy": 7.698368791677087,
                "cvrmse_percent": 14.977949561666613,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03216221757787249,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.700845554379622,
                "relative_energy_error_percent": 0.03216221757787249,
                "rms_normalized_rmse_percent": 1.4890960827978599,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04685761407017708,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.04771714471280575,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.3575000250712,
            "full": 2382.8807920217514
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.9334169877693,
            "full": 2375.017249956727
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.49758297856897,
            "full": 2401.3235840247944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.84537493810058,
            "full": 2416.5664160391316
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002499343827366829,
                  "p50": 0.0,
                  "p90": 2.3417058400809765e-05,
                  "p95": 5.453697231132537e-05,
                  "p99": 0.00012498022988438606
                },
                "candidate_energy": 11.97267058805528,
                "cvrmse_percent": 3.1950953572155862,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.020962444847056044,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.975180878742322,
                "relative_energy_error_percent": 0.020962444847056047,
                "rms_normalized_rmse_percent": 0.9017057704925114,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007543664891272783,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.0072937305085361,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007427651435136795,
                  "p50": 2.3124673731445e-07,
                  "p90": 4.455959424376488e-05,
                  "p95": 8.85551562532782e-05,
                  "p99": 0.00020653009414672852
                },
                "candidate_energy": 7.703820218002672,
                "cvrmse_percent": 8.90716521140391,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.027264301164672173,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.705921183561671,
                "relative_energy_error_percent": 0.027264301164672173,
                "rms_normalized_rmse_percent": 0.8849990917697823,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03939171880483627,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.04013448394834995,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.44004200026393,
            "full": 4230.187625042163
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.08195802848786,
            "full": 4203.631874988787
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.27491692826152,
            "full": 4245.010916958563
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.21512507088482,
            "full": 4227.348208078183
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/ribbon_windows/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 791.7804169701412,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2995.2575840288773,
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
        "identifier": "ribbon_windows_grid",
        "full_identifier": "ribbon_windows_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.001033995429448103,
            "cvrmse_percent": 2.3261236757208446,
            "rms_normalized_rmse_percent": 0.6565076137809785,
            "reference_energy": 11.975563358811996,
            "candidate_energy": 11.975439532034216,
            "relative_energy_error_percent": 0.001033995429448103,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.571418685372919e-06,
              "p95": 2.896040678024292e-05,
              "p99": 7.768440991640091e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.284497676541696,
            "cvrmse_percent": 22.69779609469076,
            "rms_normalized_rmse_percent": 2.2543726173861907,
            "reference_energy": 7.703233150983994,
            "candidate_energy": 7.604285300141015,
            "relative_energy_error_percent": 1.284497676541696,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0974908946081996e-06,
              "p90": 5.761580541729927e-05,
              "p95": 8.450644672848283e-05,
              "p99": 0.0001976415514945984,
              "maximum": 0.0030499324202537537
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.061155371367931366,
              "candidate": 0.05810543894767761,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5034437831167294,
            "cvrmse_percent": 8.848640096328518,
            "rms_normalized_rmse_percent": 2.245143135145907,
            "reference_energy": 19.67879650979599,
            "candidate_energy": 19.57972483217523,
            "relative_energy_error_percent": 0.5034437831167294,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0953372111544013e-06,
              "p90": 5.639134906232357e-05,
              "p95": 8.244459750130772e-05,
              "p99": 0.00018384424038231373,
              "maximum": 0.0030499324202537537
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.061155371367931366,
              "candidate": 0.05810543894767761,
              "position": [
                3.5,
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
        "identifier": "ribbon_windows_grid",
        "full_identifier": "ribbon_windows_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.001033995429448103,
            "cvrmse_percent": 2.3261236757208446,
            "rms_normalized_rmse_percent": 0.6565076137809785,
            "reference_energy": 11.975563358811996,
            "candidate_energy": 11.975439532034216,
            "relative_energy_error_percent": 0.001033995429448103,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.571418685372919e-06,
              "p95": 2.896040678024292e-05,
              "p99": 7.768440991640091e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.82203843871433,
            "cvrmse_percent": 417.70682917420925,
            "rms_normalized_rmse_percent": 28.89528520579435,
            "reference_energy": 4.3005302773820375,
            "candidate_energy": 7.604285300141015,
            "relative_energy_error_percent": 76.82203843871434,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.8736637485972096e-07,
              "p90": 0.0004247823144396534,
              "p95": 0.0005447780386020892,
              "p99": 0.0008227510843425989,
              "maximum": 0.0151781365275383
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040887251496315,
              "candidate": 0.0560653880238533,
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
            "nmbe_percent": 20.297445258208228,
            "cvrmse_percent": 110.36244818010397,
            "rms_normalized_rmse_percent": 28.893816194466748,
            "reference_energy": 16.276093636194034,
            "candidate_energy": 19.57972483217523,
            "relative_energy_error_percent": 20.297445258208228,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.8736637485972096e-07,
              "p90": 0.0004247823144396534,
              "p95": 0.0005425779419965689,
              "p99": 0.000818971311673522,
              "maximum": 0.0151781365275383
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040887251496315,
              "candidate": 0.0560653880238533,
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
      "bias_percent": 0.06180807786315757,
      "rms_normalized_error_percent": 0.2464319016914531,
      "absolute_error": {
        "p95": 0.16230995211588684,
        "p99": 0.1761958014674715,
        "maximum": 0.18278581868309995
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 24.156187717112694,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2464319016914531
    },
    "overcast": {
      "bias_percent": 0.027737823926661357,
      "rms_normalized_error_percent": 0.20455046166287416,
      "absolute_error": {
        "p95": 0.09089851379394531,
        "p99": 0.1049478530883789,
        "maximum": 0.10651397705078125
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.54226016998291,
      "reference_fraction_of_uniform": 0.6434069871902466,
      "rms_normalized_to_uniform_percent": 0.14144538981969718
    },
    "horizon": {
      "bias_percent": 1.1936897126065513,
      "rms_normalized_error_percent": 2.2240744358674185,
      "absolute_error": {
        "p95": 0.0964265893683004,
        "p99": 0.1425109364952045,
        "maximum": 0.16583562208408686
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.282624041117414,
      "reference_fraction_of_uniform": 0.09449438246832138,
      "rms_normalized_to_uniform_percent": 0.15645320353091127
    },
    "north": {
      "bias_percent": -22.17039257167912,
      "rms_normalized_error_percent": 147.61568957942796,
      "absolute_error": {
        "p95": 0.00015091149998625042,
        "p99": 0.000299716218250978,
        "maximum": 0.00036750225990545005
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.9497272407752462e-05,
      "reference_fraction_of_uniform": 1.2211063449285575e-06,
      "rms_normalized_to_uniform_percent": 0.00023046788315599033
    },
    "east": {
      "bias_percent": -0.05350029747970132,
      "rms_normalized_error_percent": 0.38655655564646835,
      "absolute_error": {
        "p95": 0.05267396569252014,
        "p99": 0.06486177444458006,
        "maximum": 0.06981182098388672
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.555502414703369,
      "reference_fraction_of_uniform": 0.1885853260755539,
      "rms_normalized_to_uniform_percent": 0.08134403142701116
    },
    "south": {
      "bias_percent": 0.07597883140785132,
      "rms_normalized_error_percent": 0.30021800008472993,
      "absolute_error": {
        "p95": 0.1444629430770874,
        "p99": 0.16488139629364013,
        "maximum": 0.17029857635498047
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.889009475708008,
      "reference_fraction_of_uniform": 0.6991587281227112,
      "rms_normalized_to_uniform_percent": 0.19552666494156618
    },
    "west": {
      "bias_percent": 0.05082524420756447,
      "rms_normalized_error_percent": 0.310884698489043,
      "absolute_error": {
        "p95": 0.037934571504592896,
        "p99": 0.055084824562072726,
        "maximum": 0.062235355377197266
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.442215442657471,
      "reference_fraction_of_uniform": 0.1838955581188202,
      "rms_normalized_to_uniform_percent": 0.06300117158030452
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
        "identifier": "ribbon_windows_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0769299276808612,
          "cvrmse_percent": 1.1782682621803116,
          "absolute_error_percentiles_lux": {
            "p50": 4.055572509765625,
            "p90": 36.175231933593764,
            "p95": 54.00354003906247,
            "p99": 100.62504638671868
          },
          "maximum_absolute_error_lux": 385.71923828125,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5390.06884765625,
            "radiance_lux": 5775.7880859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07580669710806633,
            "maximum_error_percentage_points": 0.5730136986301346,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04931456517320735,
            "maximum_error_percentage_points": 0.2916884080350144,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.037298325722982986,
            "maximum_error_percentage_points": 0.24164383561643632,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09339421613394212,
            "maximum_error_percentage_points": 0.6895890410958856,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.09031963470319658,
            "maximum_error_percentage_points": 0.6841095890410998,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.0050058861301209845,
      "metrics": {
        "da": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.0050058861301209845,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "ribbon_windows_grid",
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
      "study_preparation_seconds": 0.00600795797072351,
      "weather_seconds": 0.09060808294452727,
      "metric_reduction_seconds": 0.03838320809882134,
      "write_seconds": 0.03817133302800357,
      "total_seconds": 0.16729300003498793,
      "cold_end_to_end_seconds": 0.17330095800571144,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.015842625056393445,
      "engine_upload_seconds": 0.000271042,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.019460583571344614,
      "engine_annual_reduction_seconds": 0.00040345825254917145,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.019460583571344614
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00600795797072351,
      "weather_seconds": 0.09028683300130069,
      "metric_reduction_seconds": 0.012239458039402962,
      "write_seconds": 0.03357820794917643,
      "total_seconds": 0.13625441608019173,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13625441608019173,
      "raw_export_seconds": 0.016989666037261486,
      "engine_upload_seconds": 5.2042e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.000488666701130569,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0138242500834167,
      "full": 0.024669750011526048
    }
  },
  "elapsed_seconds": 0.6630445409100503,
  "result_class": "passed"
}
```
