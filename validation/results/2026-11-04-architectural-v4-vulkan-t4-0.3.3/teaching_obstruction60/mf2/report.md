# Foton report

Status: **passed**

```json
{
  "scene": "teaching_obstruction60",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_obstruction60",
    "category": "teaching",
    "question": "How does a 60 degree obstruction angle reduce sky access?",
    "interactions": [
      "multiple_bounces",
      "obstruction",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "3f123bfbf00de92b14f76842255c10d28b3e5e9cdeb7af6c9bb246ebada398c6",
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
      "scene_fingerprint": 12158479806775792312,
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
      "scene_fingerprint": 12158479806775792312,
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
    "model_sha256": "ff22f87a8905b0de061a60a41a433c7fe95b67b5b4fbcb49bbc35529bbe47eb7",
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
          "p95": 0.0,
          "p99": 2.389657311141491e-06
        },
        "bias_percent": -0.1534278694428416,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8771821973814538,
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
          "maximum": 0.0006400011479854584,
          "p95": 1.8359452951699495e-05,
          "p99": 4.398822784423828e-05
        },
        "bias_percent": 0.1003597556262982,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7886505313626007,
        "worst_index": [
          27,
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
          "maximum": 0.0007330030202865601,
          "p95": 1.5820187400095165e-05,
          "p99": 3.6187891964800656e-05
        },
        "bias_percent": -0.0604303026228386,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7490445958986185,
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042444298742339015,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.727200601133518e-05
                },
                "candidate_energy": 1.3343355690121825,
                "cvrmse_percent": 60.15163494587716,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.43155350253711905,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3401188990592345,
                "relative_energy_error_percent": 0.43155350253711894,
                "rms_normalized_rmse_percent": 5.471376539356091,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010939569910988212,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0015183999785222113,
                  "rgb_channel": 0,
                  "sky_patch_index": 487
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001386888325214386,
                  "p50": 0.0,
                  "p90": 1.8684646238398277e-05,
                  "p95": 3.477595600998029e-05,
                  "p99": 9.576140291756019e-05
                },
                "candidate_energy": 3.893271205948519,
                "cvrmse_percent": 48.90604624611008,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1871397553460256,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.885998957007626,
                "relative_energy_error_percent": 0.18713975534602562,
                "rms_normalized_rmse_percent": 2.1934978031409944,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06888119876384735,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.06749431043863297,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.40454092249274,
            "full": 229.32508401572704
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.30775000713766,
            "full": 218.42837508302182
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.21604195795953,
            "full": 231.49270797148347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.42237504664809,
            "full": 228.4099169773981
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00025992782320827246,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3879570107965264e-05
                },
                "candidate_energy": 1.339861360694158,
                "cvrmse_percent": 39.91980634876061,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.11730584961990127,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3382914665189674,
                "relative_energy_error_percent": 0.11730584961990129,
                "rms_normalized_rmse_percent": 3.623128067400337,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003613557550124824,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0038734853733330965,
                  "rgb_channel": 0,
                  "sky_patch_index": 491
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011075809597969055,
                  "p50": 1.946662678165012e-06,
                  "p90": 1.6255096170425565e-05,
                  "p95": 2.717280585784465e-05,
                  "p99": 7.043970981612802e-05
                },
                "candidate_energy": 5.3918749866786655,
                "cvrmse_percent": 25.191388360297402,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1498822520827433,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.3999685811999285,
                "relative_energy_error_percent": 0.1498822520827433,
                "rms_normalized_rmse_percent": 1.235379697195086,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05370483919978142,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.05481242015957832,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.35687506757677,
            "full": 2173.1176659232005
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.02170904818922,
            "full": 2190.1593749644235
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.03858298342675,
            "full": 2198.243916966021
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.196874987334,
            "full": 2165.6732090050355
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00030622491613030434,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.0525028705596924e-05
                },
                "candidate_energy": 1.3395872327118923,
                "cvrmse_percent": 41.667978475379684,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09409728277065123,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.340848935125905,
                "relative_energy_error_percent": 0.09409728277065123,
                "rms_normalized_rmse_percent": 3.7835859564562737,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005035002017393708,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004728777101263404,
                  "rgb_channel": 0,
                  "sky_patch_index": 516
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010972917079925537,
                  "p50": 2.020515694312053e-06,
                  "p90": 1.654200839311672e-05,
                  "p95": 2.6840441933018155e-05,
                  "p99": 7.041120261419564e-05
                },
                "candidate_energy": 5.403262323127887,
                "cvrmse_percent": 29.045948783628248,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06381574528609163,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.399816390054493,
                "relative_energy_error_percent": 0.06381574528609163,
                "rms_normalized_rmse_percent": 1.4242781113536933,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07547340542078018,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.07657069712877274,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.5790829770267,
            "full": 2333.5569170303643
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.62683304492384,
            "full": 2323.667582939379
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.40845808852464,
            "full": 2373.36508394219
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.35662494786084,
            "full": 2336.4373330259696
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00013305654283612967,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.8148013623431325e-05
                },
                "candidate_energy": 1.3397907248286174,
                "cvrmse_percent": 23.79434617655799,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.022628876081576932,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3394876138363543,
                "relative_energy_error_percent": 0.022628876081576932,
                "rms_normalized_rmse_percent": 2.158078967510097,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0023460584925487638,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0024791150353848934,
                  "rgb_channel": 0,
                  "sky_patch_index": 485
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006442181766033173,
                  "p50": 1.4817041176229395e-06,
                  "p90": 1.1493294982756198e-05,
                  "p95": 1.8776700017042458e-05,
                  "p99": 4.643487045541406e-05
                },
                "candidate_energy": 5.3964911013476495,
                "cvrmse_percent": 17.59201169184569,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05752761298317127,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.399597360820032,
                "relative_energy_error_percent": 0.05752761298317127,
                "rms_normalized_rmse_percent": 0.8636920067743217,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07621894404292107,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.07557472586631775,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.94645795039833,
            "full": 4093.1582080665976
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.31041705422103,
            "full": 4117.634332971647
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.6929169567302,
            "full": 4128.316416055895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.88141599018127,
            "full": 4084.209583932534
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
    "/content/suite-vulkan-0.3.3/teaching_obstruction60/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2573.7969999900088,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10489.851291989908,
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
        "identifier": "teaching_obstruction60_grid",
        "full_identifier": "teaching_obstruction60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.015003626850555106,
            "cvrmse_percent": 8.655491456984818,
            "rms_normalized_rmse_percent": 0.7852939555215698,
            "reference_energy": 1.3396289326610713,
            "candidate_energy": 1.3394279397348328,
            "relative_energy_error_percent": 0.015003626850555105,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.077002136502415e-06,
              "maximum": 5.524326115846634e-05
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 484,
              "rgb_channel": 0,
              "reference": 0.0036331405863165855,
              "candidate": 0.003577897325158119,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4998510819477973,
            "cvrmse_percent": 43.6555357528868,
            "rms_normalized_rmse_percent": 2.1418196981290096,
            "reference_energy": 5.3980544557573005,
            "candidate_energy": 5.317091677598493,
            "relative_energy_error_percent": 1.4998510819477973,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4668364656245103e-06,
              "p90": 8.032369532884343e-06,
              "p95": 1.1315306437609252e-05,
              "p99": 2.3961649276316166e-05,
              "maximum": 0.0017907395958900452
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05150990933179855,
              "candidate": 0.04971916973590851,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.2046242960089337,
            "cvrmse_percent": 34.95578577261439,
            "rms_normalized_rmse_percent": 2.1406023252472743,
            "reference_energy": 6.737683388418372,
            "candidate_energy": 6.656519617333326,
            "relative_energy_error_percent": 1.2046242960089337,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.46599089489996e-06,
              "p90": 8.02636131993495e-06,
              "p95": 1.1335861927364022e-05,
              "p99": 2.3692729882895947e-05,
              "maximum": 0.0017907395958900452
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05150990933179855,
              "candidate": 0.04971916973590851,
              "position": [
                2.5,
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
        "identifier": "teaching_obstruction60_grid",
        "full_identifier": "teaching_obstruction60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.015003626850555106,
            "cvrmse_percent": 8.655491456984818,
            "rms_normalized_rmse_percent": 0.7852939555215698,
            "reference_energy": 1.3396289326610713,
            "candidate_energy": 1.3394279397348328,
            "relative_energy_error_percent": 0.015003626850555105,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.077002136502415e-06,
              "maximum": 5.524326115846634e-05
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 484,
              "rgb_channel": 0,
              "reference": 0.0036331405863165855,
              "candidate": 0.003577897325158119,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 36.7834435784683,
            "cvrmse_percent": 643.0122212261379,
            "rms_normalized_rmse_percent": 28.87542617886217,
            "reference_energy": 3.8872333803675936,
            "candidate_energy": 5.317091677598493,
            "relative_energy_error_percent": 36.7834435784683,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.740237727673957e-06,
              "p90": 2.288835148647195e-05,
              "p95": 3.104999996139668e-05,
              "p99": 6.391324859578162e-05,
              "maximum": 0.011471934616565704
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017913835123181343,
              "candidate": 0.029385769739747047,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.352113346109117,
            "cvrmse_percent": 478.2060590906657,
            "rms_normalized_rmse_percent": 28.8751796271735,
            "reference_energy": 5.226862313028665,
            "candidate_energy": 6.656519617333326,
            "relative_energy_error_percent": 27.352113346109117,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.749999789055437e-06,
              "p90": 2.2932743195269784e-05,
              "p95": 3.1094612495508045e-05,
              "p99": 6.288858276093379e-05,
              "maximum": 0.011471934616565704
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017913835123181343,
              "candidate": 0.029385769739747047,
              "position": [
                0.5,
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
      "bias_percent": 0.0722756882406527,
      "rms_normalized_error_percent": 0.24043841616477063,
      "absolute_error": {
        "p95": 0.03969231326783129,
        "p99": 0.051100280987694265,
        "maximum": 0.05554276244871481
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.200354817063715,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.24043841616477063
    },
    "overcast": {
      "bias_percent": 0.03838807903872602,
      "rms_normalized_error_percent": 0.21107695679112407,
      "absolute_error": {
        "p95": 0.028728783130645752,
        "p99": 0.03807891607284545,
        "maximum": 0.04049110412597656
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0453248023986816,
      "reference_fraction_of_uniform": 0.7250160574913025,
      "rms_normalized_to_uniform_percent": 0.16384699852331788
    },
    "horizon": {
      "bias_percent": 0.866501671226522,
      "rms_normalized_error_percent": 1.851014067909924,
      "absolute_error": {
        "p95": 0.02528694680501438,
        "p99": 0.02914733649265106,
        "maximum": 0.030029152952478766
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4617953839182978,
      "reference_fraction_of_uniform": 0.10994199395781491,
      "rms_normalized_to_uniform_percent": 0.1407188704858757
    },
    "north": {
      "bias_percent": 0.1334881798402358,
      "rms_normalized_error_percent": 0.6402249262784527,
      "absolute_error": {
        "p95": 0.017584912478923798,
        "p99": 0.03212139606475829,
        "maximum": 0.03422141075134277
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0719949007034302,
      "reference_fraction_of_uniform": 0.2552153170108795,
      "rms_normalized_to_uniform_percent": 0.11813324424509725
    },
    "east": {
      "bias_percent": 0.02893999210248894,
      "rms_normalized_error_percent": 0.5023253082257666,
      "absolute_error": {
        "p95": 0.0202903151512146,
        "p99": 0.03227912187576292,
        "maximum": 0.03744220733642578
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9850068688392639,
      "reference_fraction_of_uniform": 0.23450562357902527,
      "rms_normalized_to_uniform_percent": 0.12323464232436747
    },
    "south": {
      "bias_percent": -0.020738208593394657,
      "rms_normalized_error_percent": 0.2125895260926042,
      "absolute_error": {
        "p95": 0.009682752192020416,
        "p99": 0.010248282551765442,
        "maximum": 0.010302543640136719
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9015742540359497,
      "reference_fraction_of_uniform": 0.21464239060878754,
      "rms_normalized_to_uniform_percent": 0.05796688738082562
    },
    "west": {
      "bias_percent": 0.21836848367114867,
      "rms_normalized_error_percent": 0.4107291323999585,
      "absolute_error": {
        "p95": 0.01841491460800171,
        "p99": 0.023056709766387937,
        "maximum": 0.02394866943359375
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9874557852745056,
      "reference_fraction_of_uniform": 0.23508864641189575,
      "rms_normalized_to_uniform_percent": 0.10125036434171845
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
        "identifier": "teaching_obstruction60_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.5308349270216589,
          "cvrmse_percent": 2.9086579948092157,
          "absolute_error_percentiles_lux": {
            "p50": 1.1033706665039062,
            "p90": 7.837490844726568,
            "p95": 13.171020507812472,
            "p99": 31.15913055419918
          },
          "maximum_absolute_error_lux": 180.494140625,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4090.5,
            "foton_lux": 9521.30859375,
            "radiance_lux": 9340.814453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2715220700152206,
            "maximum_error_percentage_points": 1.5652054794520538,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3650066655575508,
            "maximum_error_percentage_points": 1.0109454004949434,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.40669330289193384,
            "maximum_error_percentage_points": 1.7250684931506868,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.40686453576864573,
            "maximum_error_percentage_points": 1.7250684931506868,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.005742009132420103,
            "maximum_error_percentage_points": 0.056027397260274725,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
      "maximum_error_percentage_points": 0.004898129815924079,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.0045205479452054,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.004898129815924079,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.38439994999998817,
      "weather_seconds": 0.2611142939999809,
      "metric_reduction_seconds": 1.041950376999921,
      "write_seconds": 0.010962907000021005,
      "total_seconds": 1.314390900000035,
      "cold_end_to_end_seconds": 1.698790850000023,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0013587649998498819,
      "engine_upload_seconds": 0.044346019,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.037642575,
      "engine_annual_reduction_seconds": 0.044730618,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.037642575
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38439994999998817,
      "weather_seconds": 0.23492334599995957,
      "metric_reduction_seconds": 0.9932849120000355,
      "write_seconds": 0.011509627000123146,
      "total_seconds": 1.2400280800000019,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2400280800000019,
      "raw_export_seconds": 0.001525732999880347,
      "engine_upload_seconds": 0.046174236,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.02e-07,
      "engine_annual_reduction_seconds": 0.045386855,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01896357599980547,
      "full": 0.050413371000104235
    }
  },
  "elapsed_seconds": 5.648872613000094,
  "result_class": "passed"
}
```
