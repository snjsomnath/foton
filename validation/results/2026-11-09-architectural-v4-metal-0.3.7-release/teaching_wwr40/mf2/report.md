# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr40",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr40",
    "category": "teaching",
    "question": "How does a 40% window-to-wall ratio light the base room?",
    "interactions": [
      "multiple_bounces",
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 7.1982
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "4c07f13c2c3e370704489d57a534f7d5baaed463e21e339eb28fedbcbcb2eff2",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 16461150684353540723,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 16461150684353540723,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "35c7034ddfdcfdc2eb85ea4eeffc1d9f1a8f8b74af4e3f732a6dc5204314c196",
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
          "maximum": 0.00015173666179180145,
          "p95": 3.105087671428919e-07,
          "p99": 2.122711157426238e-05
        },
        "bias_percent": -0.05104456649172273,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6896676693618947,
        "worst_index": [
          5,
          515,
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
          "maximum": 0.0007051900029182434,
          "p95": 6.213621236383915e-05,
          "p99": 0.0001386274816468358
        },
        "bias_percent": 0.056835132157229816,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.20587202093952,
        "worst_index": [
          32,
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
          "maximum": 0.0005005672574043274,
          "p95": 5.165970651432872e-05,
          "p99": 0.00011315732263028622
        },
        "bias_percent": -0.026878217397516044,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0070983947888592,
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006548079545609653,
                  "p50": 0.0,
                  "p90": 4.34094341471792e-05,
                  "p95": 9.374547516927123e-05,
                  "p99": 0.00022738345433026552
                },
                "candidate_energy": 14.101271460389398,
                "cvrmse_percent": 19.846731955194954,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01749486394025084,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.098804893656052,
                "relative_energy_error_percent": 0.017494863940250842,
                "rms_normalized_rmse_percent": 5.796944473087119,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0027111175004392862,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002056309545878321,
                  "rgb_channel": 0,
                  "sky_patch_index": 211
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001300860196352005,
                  "p50": 0.0,
                  "p90": 5.335566929716165e-05,
                  "p95": 0.0001674666054896079,
                  "p99": 0.0003717549843713641
                },
                "candidate_energy": 4.856608943975626,
                "cvrmse_percent": 96.61517970778497,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.013059497591958433,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.857243275544231,
                "relative_energy_error_percent": 0.013059497591958437,
                "rms_normalized_rmse_percent": 4.154852462050761,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05288097448647022,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.05418183468282223,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.5878749731928,
            "full": 240.72870903182775
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.0829579718411,
            "full": 255.92045800294727
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.33633298333734,
            "full": 253.19850002415478
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.62066691741347,
            "full": 245.98895804956555
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037515105213969946,
                  "p50": 0.0,
                  "p90": 2.3619586136192142e-05,
                  "p95": 8.857266220729798e-05,
                  "p99": 0.00018637592438608408
                },
                "candidate_energy": 14.095254829864189,
                "cvrmse_percent": 16.618040148476666,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.11167141621165733,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.111012797697185,
                "relative_energy_error_percent": 0.11167141621165733,
                "rms_normalized_rmse_percent": 4.857870768284842,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0032692039385437965,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.003644354990683496,
                  "rgb_channel": 0,
                  "sky_patch_index": 307
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001025080680847168,
                  "p50": 5.000000058430487e-08,
                  "p90": 4.592416589730484e-05,
                  "p95": 0.00012847087054979056,
                  "p99": 0.0002721184864640236
                },
                "candidate_energy": 8.675752954043475,
                "cvrmse_percent": 41.21868394229386,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18752693321596467,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.659514032946085,
                "relative_energy_error_percent": 0.18752693321596464,
                "rms_normalized_rmse_percent": 2.351360404667608,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06825760006904602,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.06928268074989319,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.32324992213398,
            "full": 2214.020916959271
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.5878329826519,
            "full": 2240.3400409966707
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.99325002264231,
            "full": 2241.1469999933615
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.10129095613956,
            "full": 2235.8839579392225
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003502960316836834,
                  "p50": 0.0,
                  "p90": 2.3564910225104545e-05,
                  "p95": 8.69646028149873e-05,
                  "p99": 0.00018212117720395327
                },
                "candidate_energy": 14.086633937589795,
                "cvrmse_percent": 16.18041768886231,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.11033400690734091,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.10219345268797,
                "relative_energy_error_percent": 0.11033400690734092,
                "rms_normalized_rmse_percent": 4.72939451072908,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020093360217288136,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0016590399900451303,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00129757821559906,
                  "p50": 5.000000058430487e-08,
                  "p90": 4.6806070895400186e-05,
                  "p95": 0.00012500397861003876,
                  "p99": 0.00026045460253953934
                },
                "candidate_energy": 8.691562469425975,
                "cvrmse_percent": 40.29690429665397,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05219560930984546,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.687028222114524,
                "relative_energy_error_percent": 0.05219560930984547,
                "rms_normalized_rmse_percent": 2.302967729092716,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0686073862016201,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.06990496441721916,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.72266593761742,
            "full": 2362.410083063878
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.11358295753598,
            "full": 2350.4227499943227
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.18129197880626,
            "full": 2337.416165973991
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.43233301490545,
            "full": 2346.222792053595
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000289366755168885,
                  "p50": 0.0,
                  "p90": 1.2346240691840878e-05,
                  "p95": 4.609161987900734e-05,
                  "p99": 0.0001020865747705102
                },
                "candidate_energy": 14.098168299221925,
                "cvrmse_percent": 8.992510108899218,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09128888143082992,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.111050119033735,
                "relative_energy_error_percent": 0.09128888143082993,
                "rms_normalized_rmse_percent": 2.6306201829882085,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00075285614002496,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.001042222895193845,
                  "rgb_channel": 0,
                  "sky_patch_index": 213
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005815289914608002,
                  "p50": 4.999999525523435e-08,
                  "p90": 2.6673367028706723e-05,
                  "p95": 7.13043991709128e-05,
                  "p99": 0.00015265389811247587
                },
                "candidate_energy": 8.680807074101612,
                "cvrmse_percent": 23.36590766578699,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18074867144568724,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.66514493974418,
                "relative_energy_error_percent": 0.1807486714456872,
                "rms_normalized_rmse_percent": 1.3336402194041275,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04884548485279083,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.04826395586133003,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 240.4359159991145,
            "full": 4098.297124961391
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.92979201488197,
            "full": 4152.865916956216
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 251.18762499187142,
            "full": 4081.0422090580687
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 245.67320803180337,
            "full": 4058.8524589547887
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/suite-metal-0.3.7/teaching_wwr40/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2670.031875022687,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11097.426624968648,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.006814921795207477,
            "cvrmse_percent": 1.1690829033107903,
            "rms_normalized_rmse_percent": 0.3419140467397957,
            "reference_energy": 14.10339240577241,
            "candidate_energy": 14.102431270609486,
            "relative_energy_error_percent": 0.006814921795207477,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.759043127298355e-08,
              "p95": 2.867600414901972e-07,
              "p99": 1.0491407010704279e-05,
              "maximum": 5.996040999889374e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 319,
              "rgb_channel": 0,
              "reference": 0.00110444740857929,
              "candidate": 0.0010444869985803962,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1056767357832813,
            "cvrmse_percent": 39.7667236863729,
            "rms_normalized_rmse_percent": 2.272177282397535,
            "reference_energy": 8.674192803878704,
            "candidate_energy": 8.57828427202923,
            "relative_energy_error_percent": 1.1056767357832813,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.4427928830591554e-08,
              "p90": 1.7406322876922802e-05,
              "p95": 3.061851020902395e-05,
              "p99": 6.633135490119457e-05,
              "maximum": 0.0020918920636177063
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06466323882341385,
              "candidate": 0.06257134675979614,
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
            "nmbe_percent": -0.42528506038188024,
            "cvrmse_percent": 15.140773136391356,
            "rms_normalized_rmse_percent": 2.271689981766958,
            "reference_energy": 22.777585209651114,
            "candidate_energy": 22.680715542638715,
            "relative_energy_error_percent": 0.42528506038188024,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.4323876952366845e-08,
              "p90": 1.73009153513704e-05,
              "p95": 3.034871770069003e-05,
              "p99": 6.5941596403718e-05,
              "maximum": 0.0020918920636177063
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06466323882341385,
              "candidate": 0.06257134675979614,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.006814921795207477,
            "cvrmse_percent": 1.1690829033107903,
            "rms_normalized_rmse_percent": 0.3419140467397957,
            "reference_energy": 14.10339240577241,
            "candidate_energy": 14.102431270609486,
            "relative_energy_error_percent": 0.006814921795207477,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.759043127298355e-08,
              "p95": 2.867600414901972e-07,
              "p99": 1.0491407010704279e-05,
              "maximum": 5.996040999889374e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 319,
              "rgb_channel": 0,
              "reference": 0.00110444740857929,
              "candidate": 0.0010444869985803962,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.74167649185347,
            "cvrmse_percent": 824.6670088033613,
            "rms_normalized_rmse_percent": 35.45463009479268,
            "reference_energy": 4.853571858262093,
            "candidate_energy": 8.57828427202923,
            "relative_energy_error_percent": 76.74167649185347,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012246621772646905,
              "p95": 0.00017117144852818456,
              "p99": 0.00028550950810313225,
              "maximum": 0.01700000837445259
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025012660771608353,
              "candidate": 0.042012669146060944,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.643183511555062,
            "cvrmse_percent": 211.1413755852673,
            "rms_normalized_rmse_percent": 35.45479773369812,
            "reference_energy": 18.956964264034504,
            "candidate_energy": 22.680715542638715,
            "relative_energy_error_percent": 19.643183511555065,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012262335949344584,
              "p95": 0.00017093820497393608,
              "p99": 0.0002855919301509857,
              "maximum": 0.01700000837445259
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025012660771608353,
              "candidate": 0.042012669146060944,
              "position": [
                3.5,
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
      "bias_percent": 0.10574739390042291,
      "rms_normalized_error_percent": 0.15580087289238398,
      "absolute_error": {
        "p95": 0.13793662438359444,
        "p99": 0.1663907609378973,
        "maximum": 0.170421278574036
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.06907877068488,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.15580087289238398
    },
    "overcast": {
      "bias_percent": 0.07101328366782982,
      "rms_normalized_error_percent": 0.10425918158310184,
      "absolute_error": {
        "p95": 0.05576646327972412,
        "p99": 0.059599769115447995,
        "maximum": 0.06017279624938965
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.951967239379883,
      "reference_fraction_of_uniform": 0.639563798904419,
      "rms_normalized_to_uniform_percent": 0.07212010668144053
    },
    "horizon": {
      "bias_percent": 0.7478904839246807,
      "rms_normalized_error_percent": 1.716128601476183,
      "absolute_error": {
        "p95": 0.14467597981377422,
        "p99": 0.18127053533576798,
        "maximum": 0.18137815219351605
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4426857382797795,
      "reference_fraction_of_uniform": 0.1226504712322548,
      "rms_normalized_to_uniform_percent": 0.1494762539416927
    },
    "north": {
      "bias_percent": -62.04374958289287,
      "rms_normalized_error_percent": 88.14695005702113,
      "absolute_error": {
        "p95": 3.085511161771137e-05,
        "p99": 3.72789657717476e-05,
        "maximum": 3.976500897806545e-05
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.702151146484539e-06,
      "reference_fraction_of_uniform": 3.456526371792279e-07,
      "rms_normalized_to_uniform_percent": 3.1483085948292764e-05
    },
    "east": {
      "bias_percent": 0.015232956728124776,
      "rms_normalized_error_percent": 0.17644658600683039,
      "absolute_error": {
        "p95": 0.028538227081298828,
        "p99": 0.03793859481811522,
        "maximum": 0.041266441345214844
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.1549072265625,
      "reference_fraction_of_uniform": 0.18365074694156647,
      "rms_normalized_to_uniform_percent": 0.03569311801295809
    },
    "south": {
      "bias_percent": 0.12833471357323675,
      "rms_normalized_error_percent": 0.22238085254728795,
      "absolute_error": {
        "p95": 0.14330661296844482,
        "p99": 0.1611760377883911,
        "maximum": 0.16268491744995117
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.6972713470459,
      "reference_fraction_of_uniform": 0.7017427086830139,
      "rms_normalized_to_uniform_percent": 0.14406382619102415
    },
    "west": {
      "bias_percent": 0.1208367872856567,
      "rms_normalized_error_percent": 0.16518315307624454,
      "absolute_error": {
        "p95": 0.023489296436309814,
        "p99": 0.036977690458297706,
        "maximum": 0.04276549816131592
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.220654010772705,
      "reference_fraction_of_uniform": 0.18599306046962738,
      "rms_normalized_to_uniform_percent": 0.03368904673060702
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
        "identifier": "teaching_wwr40_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.010083364982559124,
          "cvrmse_percent": 1.0939289629115094,
          "absolute_error_percentiles_lux": {
            "p50": 3.535400390625,
            "p90": 37.0837646484375,
            "p95": 57.509631347656224,
            "p99": 116.4586206054687
          },
          "maximum_absolute_error_lux": 401.60693359375,
          "worst": {
            "sensor_index": 22,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 5254.78955078125,
            "radiance_lux": 5656.396484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06888127853881325,
            "maximum_error_percentage_points": 0.4421917808219149,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03650339603242772,
            "maximum_error_percentage_points": 0.20902228567692305,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03373287671232846,
            "maximum_error_percentage_points": 0.2443835616438328,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09223363774733616,
            "maximum_error_percentage_points": 0.44041095890410986,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0816933028919332,
            "maximum_error_percentage_points": 0.4401369863013702,
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
      "maximum_error_percentage_points": 0.004968428938369129,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004968428938369129,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr40_grid",
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
      "study_preparation_seconds": 0.007331083994358778,
      "weather_seconds": 0.08225745800882578,
      "metric_reduction_seconds": 0.1204292920883745,
      "write_seconds": 0.019934833981096745,
      "total_seconds": 0.22274970798753202,
      "cold_end_to_end_seconds": 0.2300807919818908,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0020189580973237753,
      "engine_upload_seconds": 0.000893041,
      "engine_acceleration_structure_seconds": 0.003159541,
      "engine_tracing_seconds": 0.052054999861866236,
      "engine_annual_reduction_seconds": 0.0016171250026673079,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.052054999861866236
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007331083994358778,
      "weather_seconds": 0.07837458304129541,
      "metric_reduction_seconds": 0.04684424982406199,
      "write_seconds": 0.022668916964903474,
      "total_seconds": 0.14799083303660154,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14799083303660154,
      "raw_export_seconds": 0.001795999938622117,
      "engine_upload_seconds": 5.3209e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015506250783801079,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019285042071714997,
      "full": 0.05921162501908839
    }
  },
  "elapsed_seconds": 1.288714624941349,
  "result_class": "passed"
}
```
