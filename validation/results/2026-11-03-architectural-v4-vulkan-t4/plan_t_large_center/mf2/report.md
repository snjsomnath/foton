# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "45559f777f80254baca02843a0fb3b47f04bf5e8e3489d5e28f6717239e04945",
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
      "scene_fingerprint": 6671821952119421462,
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
      "scene_fingerprint": 6671821952119421462,
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
    "model_sha256": "7cbfd943d3a19137251a25e782841903bfb0b7bfcd9534ce4b91b8689daa79ea",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
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
          "p95": 0.0,
          "p99": 4.707835614681244e-07
        },
        "bias_percent": -0.015477625651356687,
        "identifier": "plan_t_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5891497019676059,
        "worst_index": [
          25,
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
          "maximum": 0.0005505979061126709,
          "p95": 9.041403245646507e-06,
          "p99": 7.325271144509315e-05
        },
        "bias_percent": 0.06925250106708786,
        "identifier": "plan_t_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2293554299834648,
        "worst_index": [
          36,
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
          "maximum": 0.00045981258153915405,
          "p95": 7.670954801142216e-06,
          "p99": 5.7441648095846176e-05
        },
        "bias_percent": -0.007450061651966718,
        "identifier": "plan_t_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9918553947854714,
        "worst_index": [
          26,
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
            "identifier": "plan_t_large_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005781788495369256,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012334296479821205
                },
                "candidate_energy": 5.130687001070328,
                "cvrmse_percent": 40.26503585968289,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.014289642160153816,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.131420262663596,
                "relative_energy_error_percent": 0.014289642160153816,
                "rms_normalized_rmse_percent": 5.603814058870598,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013328909990377724,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0007547121495008469,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014677811414003372,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0340299922972918e-05,
                  "p99": 0.00020343478536233306
                },
                "candidate_energy": 1.865844180491365,
                "cvrmse_percent": 204.14888618213064,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.16717960525806808,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8627300757037801,
                "relative_energy_error_percent": 0.1671796052580681,
                "rms_normalized_rmse_percent": 4.624759847026544,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.045341501012444496,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.04387371987104416,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.32662500906736,
            "full": 317.72074999753386
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.9274170063436,
            "full": 443.270375020802
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.59591693151742,
            "full": 314.25795797258615
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.0553340120241,
            "full": 317.2444589436054
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
            "identifier": "plan_t_large_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003383528674021363,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.259107173420489e-05
                },
                "candidate_energy": 5.131570194447704,
                "cvrmse_percent": 30.788467212033414,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04400155341406162,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.1338291590273,
                "relative_energy_error_percent": 0.04400155341406162,
                "rms_normalized_rmse_percent": 4.292169757513998,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003895347355864942,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0035569944884628057,
                  "rgb_channel": 0,
                  "sky_patch_index": 315
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007606372237205505,
                  "p50": 0.0,
                  "p90": 4.5829001464881e-06,
                  "p95": 1.2821149539377075e-05,
                  "p99": 0.00013005180517211556
                },
                "candidate_energy": 3.421523434819406,
                "cvrmse_percent": 71.93214925653537,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0857504688109313,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4244599252595584,
                "relative_energy_error_percent": 0.0857504688109313,
                "rms_normalized_rmse_percent": 2.2375085517801026,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06855149567127228,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.06931213289499283,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.31745892204344,
            "full": 3848.0874170782045
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.57270807027817,
            "full": 3851.569499936886
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.93566700071096,
            "full": 4063.692749943584
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.60016701184213,
            "full": 4073.1246249051765
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
            "identifier": "plan_t_large_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004251869395375252,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010803586337715387
                },
                "candidate_energy": 5.132088296160873,
                "cvrmse_percent": 35.02231314150398,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.05950591103980219,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.1290362164327234,
                "relative_energy_error_percent": 0.05950591103980219,
                "rms_normalized_rmse_percent": 4.880050357371002,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0033695504534989595,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0029443635139614344,
                  "rgb_channel": 0,
                  "sky_patch_index": 310
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006772056221961975,
                  "p50": 0.0,
                  "p90": 4.745345449919114e-06,
                  "p95": 1.3388491424848326e-05,
                  "p99": 0.000152272405102849
                },
                "candidate_energy": 3.4299358726559284,
                "cvrmse_percent": 79.81543321211302,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06516295837769005,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4321723777138686,
                "relative_energy_error_percent": 0.06516295837769005,
                "rms_normalized_rmse_percent": 2.4945192508879206,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0771191455423832,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.076441939920187,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.95712508633733,
            "full": 4247.435041004792
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.09720801841468,
            "full": 4688.601459027268
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.90041703544557,
            "full": 4214.4468339392915
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 253.7450409727171,
            "full": 4303.328334004618
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
            "identifier": "plan_t_large_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024102849420160055,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.6333490647375584e-05
                },
                "candidate_energy": 5.132631974293872,
                "cvrmse_percent": 18.980221350740933,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.011223653570821623,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.13320810778896,
                "relative_energy_error_percent": 0.011223653570821624,
                "rms_normalized_rmse_percent": 2.6463423242142747,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015609479742124677,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0018019764684140682,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004233904182910919,
                  "p50": 0.0,
                  "p90": 3.2781390473246574e-06,
                  "p95": 9.117465197050478e-06,
                  "p99": 7.966882549226284e-05
                },
                "candidate_energy": 3.4279652448695686,
                "cvrmse_percent": 43.34901305485275,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.005440280874127347,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4281517459533397,
                "relative_energy_error_percent": 0.005440280874127347,
                "rms_normalized_rmse_percent": 1.3512206602868435,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07640338689088821,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.07597999647259712,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 303.1722920713946,
            "full": 8029.33937497437
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 306.3128750072792,
            "full": 7848.492000019178
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 319.34099993668497,
            "full": 7898.673707968555
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 279.6192920068279,
            "full": 7508.382290950976
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_t_large_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6800.4075000062585,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_large_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 27202.914374996908,
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
      54,
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
        "identifier": "plan_t_large_center_grid",
        "full_identifier": "plan_t_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": 0.015387163164476199,
            "cvrmse_percent": 2.2823776044060953,
            "rms_normalized_rmse_percent": 0.31819087006014796,
            "reference_energy": 5.1316115850931965,
            "candidate_energy": 5.132401194540762,
            "relative_energy_error_percent": 0.0153871631644762,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.648471415042877e-07,
              "maximum": 6.0508144088089466e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": 0.0003328037273604423,
              "candidate": 0.0002722955832723528,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.7135192987757024,
            "cvrmse_percent": 81.05709367236307,
            "rms_normalized_rmse_percent": 2.5277776390458695,
            "reference_energy": 3.4293669583984485,
            "candidate_energy": 3.3706040937404538,
            "relative_energy_error_percent": 1.7135192987757026,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.096075826964807e-06,
              "p95": 9.527189831715077e-06,
              "p99": 3.671273589134216e-05,
              "maximum": 0.0019864551723003387
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06364985555410385,
              "candidate": 0.06166340038180351,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6771802419070724,
            "cvrmse_percent": 32.452587583336445,
            "rms_normalized_rmse_percent": 2.5264262197876395,
            "reference_energy": 8.560978543491645,
            "candidate_energy": 8.503005288281216,
            "relative_energy_error_percent": 0.6771802419070724,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.126872340748378e-06,
              "p95": 9.548930393066257e-06,
              "p99": 3.550352994352579e-05,
              "maximum": 0.0019864551723003387
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06364985555410385,
              "candidate": 0.06166340038180351,
              "position": [
                5.5,
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
      54,
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
        "identifier": "plan_t_large_center_grid",
        "full_identifier": "plan_t_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": 0.015387163164476199,
            "cvrmse_percent": 2.2823776044060953,
            "rms_normalized_rmse_percent": 0.31819087006014796,
            "reference_energy": 5.1316115850931965,
            "candidate_energy": 5.132401194540762,
            "relative_energy_error_percent": 0.0153871631644762,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.648471415042877e-07,
              "maximum": 6.0508144088089466e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": 0.0003328037273604423,
              "candidate": 0.0002722955832723528,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.8526770974387,
            "cvrmse_percent": 1492.3929685946346,
            "rms_normalized_rmse_percent": 33.810014888809356,
            "reference_energy": 1.8637291677603756,
            "candidate_energy": 3.3706040937404538,
            "relative_energy_error_percent": 80.85267709743871,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.1969999579596333e-05,
              "p95": 6.153999856906012e-05,
              "p99": 0.00016382074682042003,
              "maximum": 0.018482152372598648
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.056121330708265305,
              "candidate": 0.07460348308086395,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.552410221226612,
            "cvrmse_percent": 397.61240497413286,
            "rms_normalized_rmse_percent": 33.810233144405764,
            "reference_energy": 6.995340752853572,
            "candidate_energy": 8.503005288281216,
            "relative_energy_error_percent": 21.55241022122661,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.1899999410379678e-05,
              "p95": 6.169930202304386e-05,
              "p99": 0.00016482267528772354,
              "maximum": 0.018482152372598648
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.056121330708265305,
              "candidate": 0.07460348308086395,
              "position": [
                6.5,
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
      "bias_percent": -0.06195261843834538,
      "rms_normalized_error_percent": 0.11316201553182521,
      "absolute_error": {
        "p95": 0.04693413687115308,
        "p99": 0.05644001762297142,
        "maximum": 0.05680668998593141
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.930992148595464,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.11316201553182521
    },
    "overcast": {
      "bias_percent": -0.04891769655594,
      "rms_normalized_error_percent": 0.08827803145514808,
      "absolute_error": {
        "p95": 0.02625821828842161,
        "p99": 0.03956845283508299,
        "maximum": 0.04482460021972656
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.536346912384033,
      "reference_fraction_of_uniform": 0.6545017957687378,
      "rms_normalized_to_uniform_percent": 0.062495397227831054
    },
    "horizon": {
      "bias_percent": -0.08639507969398023,
      "rms_normalized_error_percent": 1.197800081796671,
      "absolute_error": {
        "p95": 0.037645426336492184,
        "p99": 0.04856507536750585,
        "maximum": 0.0511626511390203
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8033363731984257,
      "reference_fraction_of_uniform": 0.11590496078706689,
      "rms_normalized_to_uniform_percent": 0.08335273667508805
    },
    "north": {
      "bias_percent": -83.59633732056948,
      "rms_normalized_error_percent": 99.46888082090682,
      "absolute_error": {
        "p95": 0.0001479382093748424,
        "p99": 0.00024204480636399239,
        "maximum": 0.0002447600127197802
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.0301029508118518e-05,
      "reference_fraction_of_uniform": 2.9290222300915048e-06,
      "rms_normalized_to_uniform_percent": 0.0002898775475225532
    },
    "east": {
      "bias_percent": -0.1512086549616486,
      "rms_normalized_error_percent": 0.16591719314137,
      "absolute_error": {
        "p95": 0.013041472434997547,
        "p99": 0.02077268123626709,
        "maximum": 0.021347880363464355
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0910797119140625,
      "reference_fraction_of_uniform": 0.15742042660713196,
      "rms_normalized_to_uniform_percent": 0.029994378693040964
    },
    "south": {
      "bias_percent": -0.06599457421041231,
      "rms_normalized_error_percent": 0.13430466099486452,
      "absolute_error": {
        "p95": 0.03947097063064574,
        "p99": 0.04367844223976135,
        "maximum": 0.04545629024505615
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.960701942443848,
      "reference_fraction_of_uniform": 0.7157275676727295,
      "rms_normalized_to_uniform_percent": 0.08713668592732547
    },
    "west": {
      "bias_percent": -0.13757473781407653,
      "rms_normalized_error_percent": 0.18610446552945029,
      "absolute_error": {
        "p95": 0.01432924270629882,
        "p99": 0.024638304710388182,
        "maximum": 0.025457382202148438
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1091811656951904,
      "reference_fraction_of_uniform": 0.16003209352493286,
      "rms_normalized_to_uniform_percent": 0.03398411187987723
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
        "identifier": "plan_t_large_center_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.11502616879677252,
          "cvrmse_percent": 2.2337306012985585,
          "absolute_error_percentiles_lux": {
            "p50": 0.6879501342773438,
            "p90": 10.041432952880864,
            "p95": 20.137301635742187,
            "p99": 63.26405883789062
          },
          "maximum_absolute_error_lux": 366.5234375,
          "worst": {
            "sensor_index": 38,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 38125.171875,
            "radiance_lux": 38491.6953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.12519279553526122,
            "maximum_error_percentage_points": 1.2083561643835612,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22767636726876997,
            "maximum_error_percentage_points": 1.0489853275366698,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3208650431253179,
            "maximum_error_percentage_points": 3.1787671232876704,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.32739218670725495,
            "maximum_error_percentage_points": 3.178767123287674,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.010233384069000482,
            "maximum_error_percentage_points": 0.1139726027397252,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 18.51851851851852,
          "radiance_percent": 18.51851851851852,
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
      "maximum_error_percentage_points": 0.004937125428085665,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_large_center_grid",
            "maximum_error_percentage_points": 0.004937125428085665,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_large_center_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
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
      "study_preparation_seconds": 0.40532756299944595,
      "weather_seconds": 0.23535998800070956,
      "metric_reduction_seconds": 1.5198306989987032,
      "write_seconds": 0.04540801000257488,
      "total_seconds": 1.8010088930022903,
      "cold_end_to_end_seconds": 2.2063364560017362,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03207080500214943,
      "engine_upload_seconds": 0.04568873,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.056202437,
      "engine_annual_reduction_seconds": 0.026882493,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.056202437
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.40532756299944595,
      "weather_seconds": 0.25484400400091545,
      "metric_reduction_seconds": 1.7698488759997417,
      "write_seconds": 0.032989749997796025,
      "total_seconds": 2.058044992001669,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.058044992001669,
      "raw_export_seconds": 0.011483795999083668,
      "engine_upload_seconds": 0.047201287,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.9e-08,
      "engine_annual_reduction_seconds": 0.051530359,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02057517099819961,
      "full": 0.08321877300113556
    }
  },
  "elapsed_seconds": 7.851386976999493,
  "result_class": "passed"
}
```
