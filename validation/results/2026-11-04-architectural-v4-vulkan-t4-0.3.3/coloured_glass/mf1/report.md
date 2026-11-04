# Foton report

Status: **passed**

```json
{
  "scene": "coloured_glass",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "coloured_glass",
    "category": "materials",
    "question": "Does tinted glass preserve RGB transport and photopic conversion?",
    "interactions": [
      "spectral_glazing",
      "multiple_bounces"
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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c27fe7d4f82ac5076ff5a4398eaf85bb8a03afb379ad3e336fa0b27391615c56",
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
      "scene_fingerprint": 12044007157927277316,
      "basis": "Tregenza",
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
      "scene_fingerprint": 12044007157927277316,
      "basis": "Tregenza",
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "e3f596a61f3feb4a1c2f98a8afc3b5a211be4327e9bcfc7e1d1e61b7ea33b32e",
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
          "maximum": 0.00034986017271876335,
          "p95": 3.060291055589912e-06,
          "p99": 8.318264735862613e-05
        },
        "bias_percent": -0.0785698758948725,
        "identifier": "coloured_glass_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0745982414660906,
        "worst_index": [
          9,
          72,
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
          "maximum": 0.00045735016465187073,
          "p95": 4.087689740117634e-05,
          "p99": 0.00013178879860788583
        },
        "bias_percent": -0.013965417332936438,
        "identifier": "coloured_glass_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.028431661166167,
        "worst_index": [
          14,
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
          "maximum": 0.000443432480096817,
          "p95": 3.148037794744596e-05,
          "p99": 9.867604821920393e-05
        },
        "bias_percent": 0.030184239958271998,
        "identifier": "coloured_glass_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8167500919161762,
        "worst_index": [
          8,
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
            "identifier": "coloured_glass_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009108446538448334,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.760904893279076e-05,
                  "p99": 0.0004162769764661789
                },
                "candidate_energy": 5.4641282858392515,
                "cvrmse_percent": 21.072928226010802,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04090844950409969,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.461893909727223,
                "relative_energy_error_percent": 0.0409084495040997,
                "rms_normalized_rmse_percent": 4.259294037401648,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.011545524932444096,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.012456369586288929,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014556711539626122,
                  "p50": 0.0,
                  "p90": 2.054385340670711e-05,
                  "p95": 0.00015641425270587197,
                  "p99": 0.0005641483236104249
                },
                "candidate_energy": 1.8848322157067798,
                "cvrmse_percent": 87.96192790716579,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10869655958539295,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8827856924347373,
                "relative_energy_error_percent": 0.10869655958539295,
                "rms_normalized_rmse_percent": 4.812374830593963,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008537368848919868,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": -0.0006019342690706253,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.52345811389387,
            "full": 229.03554199729115
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.81358401011676,
            "full": 218.78450002986938
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.50595789775252,
            "full": 222.32379100751132
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.5220410451293,
            "full": 221.7197499703616
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
            "identifier": "coloured_glass_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00044131441973149776,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.123782055103216e-05,
                  "p99": 0.00015708478167653084
                },
                "candidate_energy": 5.453699161489567,
                "cvrmse_percent": 8.739324176814847,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.1598420262751853,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.462430420958299,
                "relative_energy_error_percent": 0.1598420262751853,
                "rms_normalized_rmse_percent": 1.7669042334806975,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006871386431157589,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.006430072011426091,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008491845801472664,
                  "p50": 2.0694966451628716e-07,
                  "p90": 2.677522170415624e-05,
                  "p95": 7.668605539947745e-05,
                  "p99": 0.00025185421458445484
                },
                "candidate_energy": 3.4760252780861656,
                "cvrmse_percent": 22.12318936734442,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14025140465683592,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.471156931731569,
                "relative_energy_error_percent": 0.14025140465683594,
                "rms_normalized_rmse_percent": 1.8930034641170348,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026121179573237896,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.026970364153385162,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.81016697268933,
            "full": 2395.9091670112684
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.35920903086662,
            "full": 2338.673291960731
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.00883400067687,
            "full": 2310.765792033635
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.39629098400474,
            "full": 2312.7650420647115
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
            "identifier": "coloured_glass_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042501650750637054,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.575431812554591e-05,
                  "p99": 0.00017975924944039432
                },
                "candidate_energy": 5.4609112328648735,
                "cvrmse_percent": 9.896167891992551,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.018519567698596646,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.4619227573475655,
                "relative_energy_error_percent": 0.018519567698596643,
                "rms_normalized_rmse_percent": 2.001685395462162,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004070996074005961,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.003645979566499591,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006419196724891663,
                  "p50": 2.014789686199947e-07,
                  "p90": 2.7334725018590695e-05,
                  "p95": 8.716268639545868e-05,
                  "p99": 0.00026632298977347085
                },
                "candidate_energy": 3.4671760884017058,
                "cvrmse_percent": 23.383596179489636,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10461217854467728,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4708069751915342,
                "relative_energy_error_percent": 0.10461217854467726,
                "rms_normalized_rmse_percent": 2.001080013696028,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.016401199623942375,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.01575927995145321,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.16270809061825,
            "full": 2405.4531659930944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.93904203176498,
            "full": 2415.6147920293733
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.15479194838554,
            "full": 2472.2577090142295
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.40966704953462,
            "full": 2424.631208064966
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
            "identifier": "coloured_glass_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002714524744078517,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2876285947859245e-05,
                  "p99": 8.66940594278276e-05
                },
                "candidate_energy": 5.4591144339483435,
                "cvrmse_percent": 4.583463117900563,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05957598520924979,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.462368693913504,
                "relative_energy_error_percent": 0.05957598520924978,
                "rms_normalized_rmse_percent": 0.9269603096299567,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002704316982999444,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0029757694574072957,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004583103582262993,
                  "p50": 1.4080925581083648e-07,
                  "p90": 1.8229835768579514e-05,
                  "p95": 4.137492505833504e-05,
                  "p99": 0.00014908421202562743
                },
                "candidate_energy": 3.4761923424921033,
                "cvrmse_percent": 13.494658965023584,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.22083100494818547,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.468532746770453,
                "relative_energy_error_percent": 0.22083100494818544,
                "rms_normalized_rmse_percent": 1.1547761114673776,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02342873439192772,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.02388704475015402,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.0161670576781,
            "full": 4433.636832982302
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.45341697428375,
            "full": 4400.448875036091
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.66708401869982,
            "full": 4355.151499970816
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.66095909755677,
            "full": 4335.340957972221
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
    "/content/suite-vulkan-0.3.3/coloured_glass/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 793.940749950707,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_glass/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2930.3715829737484,
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
        "identifier": "coloured_glass_grid",
        "full_identifier": "coloured_glass_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04520214328129789,
            "cvrmse_percent": 3.46985891625921,
            "rms_normalized_rmse_percent": 0.7017023424966014,
            "reference_energy": 5.463326635552221,
            "candidate_energy": 5.460857094818493,
            "relative_energy_error_percent": 0.045202143281297895,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.039596438407898e-06,
              "p99": 4.675953474361449e-05,
              "maximum": 0.00034108967520296574
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.0026776306331157684,
              "candidate": 0.003018720308318734,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0961830245037825,
            "cvrmse_percent": 23.984753225469905,
            "rms_normalized_rmse_percent": 2.052835365509306,
            "reference_energy": 3.469777478535054,
            "candidate_energy": 3.4317423668272973,
            "relative_energy_error_percent": 1.0961830245037827,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.078472256059285e-07,
              "p90": 3.429527860134842e-05,
              "p95": 5.222609397605991e-05,
              "p99": 0.00012695269891992205,
              "maximum": 0.0013745557516813278
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02836567535996437,
              "candidate": 0.026991119608283043,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4534219228186256,
            "cvrmse_percent": 9.246472160553749,
            "rms_normalized_rmse_percent": 2.037491026941367,
            "reference_energy": 8.933104114087275,
            "candidate_energy": 8.89259946164579,
            "relative_energy_error_percent": 0.45342192281862553,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.045644968504348e-07,
              "p90": 3.428289455769119e-05,
              "p95": 5.178238498046994e-05,
              "p99": 0.00011495214654132723,
              "maximum": 0.0013745557516813278
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02836567535996437,
              "candidate": 0.026991119608283043,
              "position": [
                3.5,
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
        "identifier": "coloured_glass_grid",
        "full_identifier": "coloured_glass_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04520214328129789,
            "cvrmse_percent": 3.46985891625921,
            "rms_normalized_rmse_percent": 0.7017023424966014,
            "reference_energy": 5.463326635552221,
            "candidate_energy": 5.460857094818493,
            "relative_energy_error_percent": 0.045202143281297895,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.039596438407898e-06,
              "p99": 4.675953474361449e-05,
              "maximum": 0.00034108967520296574
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.0026776306331157684,
              "candidate": 0.003018720308318734,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.2009219905669,
            "cvrmse_percent": 445.1601806260288,
            "rms_normalized_rmse_percent": 24.357028595317846,
            "reference_energy": 1.883493414487205,
            "candidate_energy": 3.4317423668272973,
            "relative_energy_error_percent": 82.20092199056688,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002002626395551488,
              "p95": 0.0002723024954320862,
              "p99": 0.000501590501517057,
              "maximum": 0.008425941690802574
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012471769005060196,
              "candidate": 0.02089771069586277,
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
            "nmbe_percent": 21.040115329870765,
            "cvrmse_percent": 114.11813244569248,
            "rms_normalized_rmse_percent": 24.35555039150756,
            "reference_energy": 7.346820050039426,
            "candidate_energy": 8.89259946164579,
            "relative_energy_error_percent": 21.040115329870765,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001999215800651655,
              "p95": 0.0002712511079153046,
              "p99": 0.0005085819354280829,
              "maximum": 0.008425941690802574
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012471769005060196,
              "candidate": 0.02089771069586277,
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
      "bias_percent": 0.0780816623798177,
      "rms_normalized_error_percent": 0.2040287765002929,
      "absolute_error": {
        "p95": 0.08275654758193662,
        "p99": 0.10613341555371188,
        "maximum": 0.11503965667486993
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.327426112582579,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2040287765002929
    },
    "overcast": {
      "bias_percent": 0.03052756875366197,
      "rms_normalized_error_percent": 0.17111769478786504,
      "absolute_error": {
        "p95": 0.04812011122703552,
        "p99": 0.06294042468070982,
        "maximum": 0.07009124755859375
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.22694206237793,
      "reference_fraction_of_uniform": 0.6380038857460022,
      "rms_normalized_to_uniform_percent": 0.12062715991985236
    },
    "horizon": {
      "bias_percent": 0.8957702186341346,
      "rms_normalized_error_percent": 2.4458495176194788,
      "absolute_error": {
        "p95": 0.06042695632093395,
        "p99": 0.07456254556772116,
        "maximum": 0.07777934276973708
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0610102808071322,
      "reference_fraction_of_uniform": 0.0936673760006746,
      "rms_normalized_to_uniform_percent": 0.1394838668605777
    },
    "north": {
      "bias_percent": -54.286639463251404,
      "rms_normalized_error_percent": 104.25418496564414,
      "absolute_error": {
        "p95": 7.917018592706881e-05,
        "p99": 0.00020334006367193045,
        "maximum": 0.0002604259643703699
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.2549480490852147e-05,
      "reference_fraction_of_uniform": 1.990697683140752e-06,
      "rms_normalized_to_uniform_percent": 0.0002615251082396983
    },
    "east": {
      "bias_percent": -0.04467714350996401,
      "rms_normalized_error_percent": 0.35425699995532317,
      "absolute_error": {
        "p95": 0.03085911273956299,
        "p99": 0.039040672779083255,
        "maximum": 0.03908348083496094
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3053057193756104,
      "reference_fraction_of_uniform": 0.2035154104232788,
      "rms_normalized_to_uniform_percent": 0.07566843811439465
    },
    "south": {
      "bias_percent": 0.14826359353527607,
      "rms_normalized_error_percent": 0.2623186791398659,
      "absolute_error": {
        "p95": 0.07081776857376099,
        "p99": 0.09992834329605099,
        "maximum": 0.10840225219726562
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.831841468811035,
      "reference_fraction_of_uniform": 0.6914052367210388,
      "rms_normalized_to_uniform_percent": 0.17117387809901716
    },
    "west": {
      "bias_percent": -0.04316582552652858,
      "rms_normalized_error_percent": 0.3547539928371447,
      "absolute_error": {
        "p95": 0.032906051725149155,
        "p99": 0.03538453057408332,
        "maximum": 0.03663206100463867
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.228316307067871,
      "reference_fraction_of_uniform": 0.19671867787837982,
      "rms_normalized_to_uniform_percent": 0.07258510401207398
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
        "identifier": "coloured_glass_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.04975724796605454,
          "cvrmse_percent": 1.618958168756376,
          "absolute_error_percentiles_lux": {
            "p50": 2.386505126953125,
            "p90": 23.02570190429688,
            "p95": 34.41541290283203,
            "p99": 63.89991577148389
          },
          "maximum_absolute_error_lux": 295.70166015625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4839.00927734375,
            "radiance_lux": 5134.7109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4607914764079146,
            "maximum_error_percentage_points": 2.1658904109589017,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1756174497769724,
            "maximum_error_percentage_points": 0.8298250655877766,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12224885844748906,
            "maximum_error_percentage_points": 0.6069863013698651,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13935692541856978,
            "maximum_error_percentage_points": 0.6061643835616479,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.042827245053272546,
            "maximum_error_percentage_points": 0.21438356164383698,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 52.77777777777778,
          "radiance_percent": 52.77777777777778,
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
            "identifier": "coloured_glass_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "coloured_glass_grid",
            "maximum_error_percentage_points": 0.004835455907539199,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "coloured_glass_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "coloured_glass_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "coloured_glass_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.3452340000000049,
      "weather_seconds": 0.21347275499999796,
      "metric_reduction_seconds": 0.1531421939999973,
      "write_seconds": 0.011912241000004542,
      "total_seconds": 0.37886470700004793,
      "cold_end_to_end_seconds": 0.7240987070000529,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001384594000001016,
      "engine_upload_seconds": 0.013977676,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010934318,
      "engine_annual_reduction_seconds": 0.0060117,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010934318
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3452340000000049,
      "weather_seconds": 0.21533530500005327,
      "metric_reduction_seconds": 0.14213530600000013,
      "write_seconds": 0.011279871999931856,
      "total_seconds": 0.3689956709999933,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3689956709999933,
      "raw_export_seconds": 0.001417949999904522,
      "engine_upload_seconds": 0.013946235,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.39e-07,
      "engine_annual_reduction_seconds": 0.005868815,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01311660800001846,
      "full": 0.01895025800001804
    }
  },
  "elapsed_seconds": 2.650111180999943,
  "result_class": "passed"
}
```
