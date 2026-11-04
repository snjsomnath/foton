# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 1.4399999999999997
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "04b6b06c6bcf4cd7fde53a88320f7a09257a1962d3609eb282093eec7b90e345",
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
      "scene_fingerprint": 10502512291607635887,
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
      "scene_fingerprint": 10502512291607635887,
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
    "model_sha256": "090621f52b868c79cb64c8103e2b1dff5aaf91689b84c136b129c52a4f6ec8f1",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "738a59ae8fb6881ea29066a9316dfc51647b6e94d0eae23cc7b76edc5ea48e16",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0001382098998874426,
          "p95": 0.0,
          "p99": 1.0381336323916912e-07
        },
        "bias_percent": 0.016714624763828057,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.019371124575243,
        "worst_index": [
          23,
          321,
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
          "maximum": 0.00030483491718769073,
          "p95": 5.3945732361171395e-06,
          "p99": 3.5929959267377853e-05
        },
        "bias_percent": 0.22600613739364134,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.2787197586467505,
        "worst_index": [
          23,
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
          "maximum": 0.0002637444995343685,
          "p95": 4.699819328379817e-06,
          "p99": 2.697855234146118e-05
        },
        "bias_percent": -0.09266817191943612,
        "identifier": "plan_l_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8186785255068525,
        "worst_index": [
          30,
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004704500315710902,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.5785505790263414e-05
                },
                "candidate_energy": 1.4689489967677218,
                "cvrmse_percent": 79.06225293051337,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.15211820935255982,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4667178518352557,
                "relative_energy_error_percent": 0.15211820935255982,
                "rms_normalized_rmse_percent": 6.846562991018837,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001974628074094653,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.001504178042523563,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005937215173617005,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.169560896931216e-05
                },
                "candidate_energy": 0.6964025203909685,
                "cvrmse_percent": 254.0416624496415,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.23338304468359386,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6980316078101296,
                "relative_energy_error_percent": 0.2333830446835939,
                "rms_normalized_rmse_percent": 6.324172478275175,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0004290930228307843,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.00016462849453091621,
                  "rgb_channel": 0,
                  "sky_patch_index": 148
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.93383397627622,
            "full": 284.00879190303385
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.94945805519819,
            "full": 273.819874972105
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.429791954346,
            "full": 285.7400829670951
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.14845900051296,
            "full": 271.0227920906618
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032997445669025183,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.315696423873305e-05
                },
                "candidate_energy": 1.4695724654573041,
                "cvrmse_percent": 63.52742195373538,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.10972501108771368,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4711867252547108,
                "relative_energy_error_percent": 0.10972501108771367,
                "rms_normalized_rmse_percent": 5.524753498148947,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036886880407109857,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0040186624974012375,
                  "rgb_channel": 0,
                  "sky_patch_index": 359
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005349945276975632,
                  "p50": 0.0,
                  "p90": 4.403524144436233e-06,
                  "p95": 7.95367577666184e-06,
                  "p99": 6.844080053269863e-05
                },
                "candidate_energy": 1.4075063204274656,
                "cvrmse_percent": 110.01686018716167,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18037343542133258,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4049721239408015,
                "relative_energy_error_percent": 0.18037343542133258,
                "rms_normalized_rmse_percent": 4.354846674989152,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028153774328529835,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.02761877980083227,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.6919579328969,
            "full": 3154.312124941498
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.64287509489805,
            "full": 3033.274249988608
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.41445803176612,
            "full": 3060.5744579806924
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.55287497024983,
            "full": 3058.3002499770373
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032060896046459675,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.377200871706009e-05
                },
                "candidate_energy": 1.4700123403395082,
                "cvrmse_percent": 64.18386012020152,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06887924430840853,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4690005038935396,
                "relative_energy_error_percent": 0.06887924430840853,
                "rms_normalized_rmse_percent": 5.573649794569884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035175224766135216,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.003196913516148925,
                  "rgb_channel": 0,
                  "sky_patch_index": 263
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005605802871286869,
                  "p50": 0.0,
                  "p90": 4.3459161531700374e-06,
                  "p95": 7.700430614931975e-06,
                  "p99": 6.302793917711824e-05
                },
                "candidate_energy": 1.4136769872197128,
                "cvrmse_percent": 105.73339887443528,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.008950149470746242,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.413550472339594,
                "relative_energy_error_percent": 0.008950149470746242,
                "rms_normalized_rmse_percent": 4.184445084583155,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.009625304490327835,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.009064724203199148,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.4472079090774,
            "full": 3277.253249892965
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.90745799150318,
            "full": 3301.3931250898167
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.53262497391552,
            "full": 3230.3593329852447
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.0432080188766,
            "full": 3260.7092920225114
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
            "identifier": "plan_l_offset_low_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018506200285628438,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.308306284248829e-05
                },
                "candidate_energy": 1.4703051851975033,
                "cvrmse_percent": 38.58645454221555,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.125482993403947,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4721524862046635,
                "relative_energy_error_percent": 0.12548299340394703,
                "rms_normalized_rmse_percent": 3.3588842935016996,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016777419950813055,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0018628039979375899,
                  "rgb_channel": 0,
                  "sky_patch_index": 154
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00037876470014452934,
                  "p50": 0.0,
                  "p90": 3.0861718869346078e-06,
                  "p95": 5.480664015067305e-06,
                  "p99": 4.053305019624531e-05
                },
                "candidate_energy": 1.4092005888368426,
                "cvrmse_percent": 65.3937608198494,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.002695727513516554,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4092385780689227,
                "relative_energy_error_percent": 0.002695727513516554,
                "rms_normalized_rmse_percent": 2.5851779359894387,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.013853540178388357,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.014232304878532887,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.97083399724215,
            "full": 5816.221500048414
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 247.07008292898536,
            "full": 5725.256083998829
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.57208404596895,
            "full": 5785.155416931957
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.48779198527336,
            "full": 5805.7018329855055
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
    "/content/suite-vulkan-0.3.2/plan_l_offset_low/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4583.0356660299,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_offset_low/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18893.04287498817,
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
      48,
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
        "identifier": "plan_l_offset_low_grid",
        "full_identifier": "plan_l_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0121334672895727,
            "cvrmse_percent": 5.372729766925939,
            "rms_normalized_rmse_percent": 0.4671215932314848,
            "reference_energy": 1.4693355714898644,
            "candidate_energy": 1.4695138528408052,
            "relative_energy_error_percent": 0.012133467289572701,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.242204785346985e-08,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.334715480611983,
            "cvrmse_percent": 77.87827895411263,
            "rms_normalized_rmse_percent": 3.08434517994989,
            "reference_energy": 1.4111128495744083,
            "candidate_energy": 1.3781673794264897,
            "relative_energy_error_percent": 2.334715480611983,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.860780225295457e-06,
              "p95": 6.390757334884256e-06,
              "p99": 1.834053546190262e-05,
              "maximum": 0.0011574700474739075
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023231519386172295,
              "candidate": 0.022074049338698387,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.1375724889693024,
            "cvrmse_percent": 38.08072773948388,
            "rms_normalized_rmse_percent": 3.0785784558778233,
            "reference_energy": 2.8804484210642727,
            "candidate_energy": 2.847681232267295,
            "relative_energy_error_percent": 1.1375724889693024,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.854990609397646e-06,
              "p95": 6.333109922707081e-06,
              "p99": 1.7956386727746576e-05,
              "maximum": 0.0011574700474739075
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023231519386172295,
              "candidate": 0.022074049338698387,
              "position": [
                0.5,
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
      48,
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
        "identifier": "plan_l_offset_low_grid",
        "full_identifier": "plan_l_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0121334672895727,
            "cvrmse_percent": 5.372729766925939,
            "rms_normalized_rmse_percent": 0.4671215932314848,
            "reference_energy": 1.4693355714898644,
            "candidate_energy": 1.4695138528408052,
            "relative_energy_error_percent": 0.012133467289572701,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.242204785346985e-08,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 98.09369568075232,
            "cvrmse_percent": 1249.1071991099436,
            "rms_normalized_rmse_percent": 30.999207747772733,
            "reference_energy": 0.6957149114162338,
            "candidate_energy": 1.3781673794264897,
            "relative_energy_error_percent": 98.09369568075232,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5359999451902695e-05,
              "p95": 2.7370000680093654e-05,
              "p99": 6.163000216474757e-05,
              "maximum": 0.004369326867163181
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011195182800292969,
              "candidate": 0.01556450966745615,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 31.52955345618163,
            "cvrmse_percent": 401.3340376625569,
            "rms_normalized_rmse_percent": 30.995139346943535,
            "reference_energy": 2.165050482906098,
            "candidate_energy": 2.847681232267295,
            "relative_energy_error_percent": 31.529553456181628,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.533999966341071e-05,
              "p95": 2.741076605161652e-05,
              "p99": 6.163000216474757e-05,
              "maximum": 0.004369326867163181
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011195182800292969,
              "candidate": 0.01556450966745615,
              "position": [
                1.5,
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
      "bias_percent": -0.22903800619891557,
      "rms_normalized_error_percent": 0.17376095226936078,
      "absolute_error": {
        "p95": 0.02651890204757711,
        "p99": 0.043684186852130796,
        "maximum": 0.04587254561148768
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3397275385076193,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17376095226936078
    },
    "overcast": {
      "bias_percent": -0.21841377633201334,
      "rms_normalized_error_percent": 0.13969379076408903,
      "absolute_error": {
        "p95": 0.016485255956649777,
        "p99": 0.020638723373413086,
        "maximum": 0.021068572998046875
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4183269739151,
      "reference_fraction_of_uniform": 0.6061931848526001,
      "rms_normalized_to_uniform_percent": 0.09108351972129658
    },
    "horizon": {
      "bias_percent": -0.5336400958762775,
      "rms_normalized_error_percent": 1.4194319796567667,
      "absolute_error": {
        "p95": 0.0176669964140557,
        "p99": 0.030323570744152456,
        "maximum": 0.03118896370657054
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3855966281307768,
      "reference_fraction_of_uniform": 0.16480407303182285,
      "rms_normalized_to_uniform_percent": 0.12544288625043984
    },
    "north": {
      "bias_percent": -99.17211427430293,
      "rms_normalized_error_percent": 99.99774138969546,
      "absolute_error": {
        "p95": 3.869571935410931e-06,
        "p99": 0.0001903540248349604,
        "maximum": 0.00034960650373250246
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.280328984255902e-06,
      "reference_fraction_of_uniform": 3.5390139601076953e-06,
      "rms_normalized_to_uniform_percent": 0.0006535569674409877
    },
    "east": {
      "bias_percent": -0.6046705889257898,
      "rms_normalized_error_percent": 0.3079588040969668,
      "absolute_error": {
        "p95": 0.01051316931843757,
        "p99": 0.01886057972908021,
        "maximum": 0.023332595825195312
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.34160712361335754,
      "reference_fraction_of_uniform": 0.14600294828414917,
      "rms_normalized_to_uniform_percent": 0.06511267469313423
    },
    "south": {
      "bias_percent": -0.20673629630154097,
      "rms_normalized_error_percent": 0.18693075110660268,
      "absolute_error": {
        "p95": 0.0183455117046833,
        "p99": 0.03741924285888673,
        "maximum": 0.04152679443359375
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.751458764076233,
      "reference_fraction_of_uniform": 0.7485737800598145,
      "rms_normalized_to_uniform_percent": 0.1371807787864316
    },
    "west": {
      "bias_percent": -0.1039602775606823,
      "rms_normalized_error_percent": 0.23074310159488523,
      "absolute_error": {
        "p95": 0.009368005767464636,
        "p99": 0.01161396861076355,
        "maximum": 0.011801719665527344
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5182685256004333,
      "reference_fraction_of_uniform": 0.22150805592536926,
      "rms_normalized_to_uniform_percent": 0.05167285472768845
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
        "identifier": "plan_l_offset_low_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": -0.3546490815379042,
          "cvrmse_percent": 4.0262844665469775,
          "absolute_error_percentiles_lux": {
            "p50": 0.7697763442993164,
            "p90": 9.003658294677736,
            "p95": 14.493744277954049,
            "p99": 32.810589599609315
          },
          "maximum_absolute_error_lux": 339.43359375,
          "worst": {
            "sensor_index": 11,
            "position": [
              0.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2674.5,
            "foton_lux": 33293.99609375,
            "radiance_lux": 33633.4296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.11269691780821901,
            "maximum_error_percentage_points": 1.7808219178082183,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2654215654860678,
            "maximum_error_percentage_points": 0.9508144797446576,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.30186358447488437,
            "maximum_error_percentage_points": 2.30054794520548,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.30402682648401813,
            "maximum_error_percentage_points": 2.30054794520548,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007157534246575258,
            "maximum_error_percentage_points": 0.13739726027397126,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 8.333333333333334,
          "radiance_percent": 8.333333333333334,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004874384631850859,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_offset_low_grid",
            "maximum_error_percentage_points": 0.003835616438356171,
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
      "study_preparation_seconds": 0.3894911040001716,
      "weather_seconds": 0.2564457220000804,
      "metric_reduction_seconds": 1.2906822559998545,
      "write_seconds": 0.012423568000031082,
      "total_seconds": 1.5599246359997778,
      "cold_end_to_end_seconds": 1.9494157399999494,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016443499998786137,
      "engine_upload_seconds": 0.045304674,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.043128454,
      "engine_annual_reduction_seconds": 0.021577827,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.043128454
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3894911040001716,
      "weather_seconds": 0.2680576570000994,
      "metric_reduction_seconds": 1.842766298999777,
      "write_seconds": 0.020950200999777735,
      "total_seconds": 2.1320185409999795,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.1320185409999795,
      "raw_export_seconds": 0.002581993000148941,
      "engine_upload_seconds": 0.051681494,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.7e-08,
      "engine_annual_reduction_seconds": 0.021084406,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02027165400022568,
      "full": 0.06656549099989206
    }
  },
  "elapsed_seconds": 7.772565774999748,
  "result_class": "passed"
}
```
