# Foton report

Status: **passed**

```json
{
  "scene": "reflective_neighbour",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "reflective_neighbour",
    "category": "context",
    "question": "Does a bright neighbouring facade contribute reflected daylight?",
    "interactions": [
      "external_obstruction",
      "context_reflection",
      "high_reflectance"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "7edc4ec81c88f69ea8e6cd143c17ad8d4702344372890e99c2588fe0ae48143d",
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 13318971096555845098,
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 13318971096555845098,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.5)",
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
    "model_sha256": "c28e68ac087cdcbfca1e5b7520b6801497c79a4525ce6ced31e3734484e7ecba",
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
          "maximum": 0.00021733436733484268,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.09782542200423092,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.0392927119777826,
        "worst_index": [
          17,
          447,
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
          "maximum": 0.0011888034641742706,
          "p95": 5.089376645628363e-05,
          "p99": 0.00010852800187421963
        },
        "bias_percent": 0.3032676377825211,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9592318022041575,
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
          "maximum": 0.000756535679101944,
          "p95": 4.433942376635969e-05,
          "p99": 9.517837315797806e-05
        },
        "bias_percent": -0.03784006515564866,
        "identifier": "reflective_neighbour_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6522141033124407,
        "worst_index": [
          22,
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00048551824875175953,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8537273427682521,
                "cvrmse_percent": 106.4360129243236,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.3317925476988976,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8509041063553013,
                "relative_energy_error_percent": 0.3317925476988976,
                "rms_normalized_rmse_percent": 7.509147196749757,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0038476178888231516,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.004333136137574911,
                  "rgb_channel": 0,
                  "sky_patch_index": 456
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.004788968712091446,
                  "p50": 0.0,
                  "p90": 7.773607503622771e-05,
                  "p95": 0.0001176059158751741,
                  "p99": 0.0002485598888597451
                },
                "candidate_energy": 3.471951828100508,
                "cvrmse_percent": 129.20699716194898,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2397135476896894,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.463648992221735,
                "relative_energy_error_percent": 0.23971354768968944,
                "rms_normalized_rmse_percent": 7.038920185442185,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08298062533140182,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.07819165661931038,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.3787920223549,
            "full": 237.61429195292294
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.55350000504404,
            "full": 228.44683297444135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.97025004308671,
            "full": 246.6178749455139
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.46079106908292,
            "full": 233.98970894049853
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024065293837338686,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8485876998797721,
                "cvrmse_percent": 44.61058936505207,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03759330187200175,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8489068319877333,
                "relative_energy_error_percent": 0.03759330187200175,
                "rms_normalized_rmse_percent": 3.145071679374501,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036061675054952502,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.003846820443868637,
                  "rgb_channel": 0,
                  "sky_patch_index": 490
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.003177151083946228,
                  "p50": 5.605455044133123e-06,
                  "p90": 4.6086140082479733e-05,
                  "p95": 7.183855450421106e-05,
                  "p99": 0.00015337701188400388
                },
                "candidate_energy": 5.975008053000199,
                "cvrmse_percent": 47.5948124451104,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.24560028268538622,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.9603693689808885,
                "relative_energy_error_percent": 0.24560028268538622,
                "rms_normalized_rmse_percent": 3.0615067733751973,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.10566115006804466,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.10248399898409843,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.42066600266844,
            "full": 2410.5729160364717
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.98483295552433,
            "full": 2354.6417920151725
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.01770806033164,
            "full": 2312.114833970554
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.80679104011506,
            "full": 2343.0749169783667
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002455465728417039,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8494032959652031,
                "cvrmse_percent": 49.756450786900814,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.2811860212940549,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8470215896577429,
                "relative_energy_error_percent": 0.28118602129405484,
                "rms_normalized_rmse_percent": 3.5035645009222924,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00390469201374799,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.004150238586589694,
                  "rgb_channel": 0,
                  "sky_patch_index": 446
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011699050664901733,
                  "p50": 5.600909645409047e-06,
                  "p90": 4.750404768856243e-05,
                  "p95": 7.388010999420658e-05,
                  "p99": 0.0001608480524737388
                },
                "candidate_energy": 5.9872586274116415,
                "cvrmse_percent": 41.22992275345281,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.054651825496428906,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.9905325628141775,
                "relative_energy_error_percent": 0.054651825496428906,
                "rms_normalized_rmse_percent": 2.6601713194443257,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.058121295645833015,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.05929120071232319,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.90033303201199,
            "full": 2494.82700007502
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.41075007338077,
            "full": 2515.3307920554653
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.86250005289912,
            "full": 2483.3848329726607
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.41937505174428,
            "full": 2500.5432500038296
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
            "identifier": "reflective_neighbour_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00010347762145102024,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8495422539594983,
                "cvrmse_percent": 22.79686724243971,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1050305161960326,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8486509115264198,
                "relative_energy_error_percent": 0.1050305161960326,
                "rms_normalized_rmse_percent": 1.6091666047822863,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003947180463001132,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004050658084452152,
                  "rgb_channel": 0,
                  "sky_patch_index": 456
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007016714662313461,
                  "p50": 4.3857959894921805e-06,
                  "p90": 3.2879759783099874e-05,
                  "p95": 5.1999744755448774e-05,
                  "p99": 0.00011396192712709308
                },
                "candidate_energy": 5.987577687479426,
                "cvrmse_percent": 29.071594382773306,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07198095036820816,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.983270872242482,
                "relative_energy_error_percent": 0.07198095036820817,
                "rms_normalized_rmse_percent": 1.8760348933119295,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033935099840164185,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.03463677130639553,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.79345802310854,
            "full": 4365.529167000204
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.44850002601743,
            "full": 4432.34408297576
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.2528750039637,
            "full": 4401.868082932197
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.8595830211416,
            "full": 4339.402374927886
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
    "/content/suite-vulkan/reflective_neighbour/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2876.2428750051185,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/reflective_neighbour/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10964.127582963556,
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
        "identifier": "reflective_neighbour_grid",
        "full_identifier": "reflective_neighbour_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08744985246123152,
            "cvrmse_percent": 12.760743970253344,
            "rms_normalized_rmse_percent": 0.9006240056013579,
            "reference_energy": 0.8487971900273692,
            "candidate_energy": 0.8480549181369952,
            "relative_energy_error_percent": 0.08744985246123152,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6102858255575506,
            "cvrmse_percent": 25.319439814725666,
            "rms_normalized_rmse_percent": 1.6334025905692888,
            "reference_energy": 5.985723666709557,
            "candidate_energy": 5.949193643614585,
            "relative_energy_error_percent": 0.6102858255575506,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.989654715041979e-06,
              "p90": 2.261121735500638e-05,
              "p95": 3.317580558359623e-05,
              "p99": 6.570742698386312e-05,
              "maximum": 0.0013559870421886444
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.059462785720825195,
              "candidate": 0.05810679867863655,
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
            "nmbe_percent": -0.5453534456421486,
            "cvrmse_percent": 22.16754889914353,
            "rms_normalized_rmse_percent": 1.6328572991677597,
            "reference_energy": 6.834520856736926,
            "candidate_energy": 6.79724856175158,
            "relative_energy_error_percent": 0.5453534456421486,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.989654715041979e-06,
              "p90": 2.258710737805815e-05,
              "p95": 3.305211430415511e-05,
              "p99": 6.570742698386312e-05,
              "maximum": 0.0013559870421886444
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.059462785720825195,
              "candidate": 0.05810679867863655,
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
        "identifier": "reflective_neighbour_grid",
        "full_identifier": "reflective_neighbour_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08744985246123152,
            "cvrmse_percent": 12.760743970253344,
            "rms_normalized_rmse_percent": 0.9006240056013579,
            "reference_energy": 0.8487971900273692,
            "candidate_energy": 0.8480549181369952,
            "relative_energy_error_percent": 0.08744985246123152,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 71.38136005358169,
            "cvrmse_percent": 942.0612979023804,
            "rms_normalized_rmse_percent": 51.116872828396545,
            "reference_energy": 3.4713189589314695,
            "candidate_energy": 5.949193643614585,
            "relative_energy_error_percent": 71.38136005358169,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2668504496105015e-05,
              "p90": 5.807400011690342e-05,
              "p95": 7.808941882103682e-05,
              "p99": 0.00014487560838460922,
              "maximum": 0.023156948387622833
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07992132008075714,
              "candidate": 0.10307826846837997,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 57.33948642537628,
            "cvrmse_percent": 756.9660062704796,
            "rms_normalized_rmse_percent": 51.11665124166475,
            "reference_energy": 4.320116148958839,
            "candidate_energy": 6.79724856175158,
            "relative_energy_error_percent": 57.33948642537627,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2656601029448211e-05,
              "p90": 5.810224465676585e-05,
              "p95": 7.800033199600875e-05,
              "p99": 0.0001451558928238228,
              "maximum": 0.023156948387622833
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07992132008075714,
              "candidate": 0.10307826846837997,
              "position": [
                2.5,
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
      "bias_percent": -0.17191392955143084,
      "rms_normalized_error_percent": 0.36237163095925884,
      "absolute_error": {
        "p95": 0.07744285078353885,
        "p99": 0.11814207778228344,
        "maximum": 0.1394413292527492
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.335867532410835,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.36237163095925884
    },
    "overcast": {
      "bias_percent": -0.12871469683702055,
      "rms_normalized_error_percent": 0.3343003570697925,
      "absolute_error": {
        "p95": 0.05355963110923767,
        "p99": 0.08155235648155207,
        "maximum": 0.09598588943481445
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.452753067016602,
      "reference_fraction_of_uniform": 0.702785074710846,
      "rms_normalized_to_uniform_percent": 0.244463106793328
    },
    "horizon": {
      "bias_percent": -0.806358123933787,
      "rms_normalized_error_percent": 2.173595851377084,
      "absolute_error": {
        "p95": 0.0388497230861794,
        "p99": 0.0852148537110119,
        "maximum": 0.1045000050648941
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6916629094463284,
      "reference_fraction_of_uniform": 0.10916625164717522,
      "rms_normalized_to_uniform_percent": 0.21300345035974824
    },
    "north": {
      "bias_percent": -0.21418629024601132,
      "rms_normalized_error_percent": 0.5975467377384561,
      "absolute_error": {
        "p95": 0.05065512657165527,
        "p99": 0.06701717376708981,
        "maximum": 0.0752863883972168
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6929771900177,
      "reference_fraction_of_uniform": 0.42503684759140015,
      "rms_normalized_to_uniform_percent": 0.22639140947449313
    },
    "east": {
      "bias_percent": -0.07296350507082199,
      "rms_normalized_error_percent": 0.9545304260565928,
      "absolute_error": {
        "p95": 0.055722951889038086,
        "p99": 0.07470724582672117,
        "maximum": 0.08078432083129883
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4320671558380127,
      "reference_fraction_of_uniform": 0.22602543234825134,
      "rms_normalized_to_uniform_percent": 0.20677067078549116
    },
    "south": {
      "bias_percent": -0.14200383270493774,
      "rms_normalized_error_percent": 0.27790777411995216,
      "absolute_error": {
        "p95": 0.010767452418804169,
        "p99": 0.014018917083740227,
        "maximum": 0.015729904174804688
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6434364318847656,
      "reference_fraction_of_uniform": 0.10155459493398666,
      "rms_normalized_to_uniform_percent": 0.043053530531545744
    },
    "west": {
      "bias_percent": -0.37677438649484896,
      "rms_normalized_error_percent": 0.8189900684214598,
      "absolute_error": {
        "p95": 0.04276168346405029,
        "p99": 0.062080049514770495,
        "maximum": 0.06464719772338867
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4415512084960938,
      "reference_fraction_of_uniform": 0.22752231359481812,
      "rms_normalized_to_uniform_percent": 0.17892775656102222
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
        "identifier": "reflective_neighbour_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.34523849173894156,
          "cvrmse_percent": 4.790761846817267,
          "absolute_error_percentiles_lux": {
            "p50": 1.3982372283935547,
            "p90": 15.306818389892578,
            "p95": 24.075132751464835,
            "p99": 52.443784332274994
          },
          "maximum_absolute_error_lux": 249.8759765625,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3828.5,
            "foton_lux": 9286.5869140625,
            "radiance_lux": 9536.462890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2468949771689498,
            "maximum_error_percentage_points": 1.5294520547945218,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22462335546805662,
            "maximum_error_percentage_points": 0.8775152984764532,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.39595509893455233,
            "maximum_error_percentage_points": 1.8121917808219195,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.39912480974124925,
            "maximum_error_percentage_points": 1.8121917808219195,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004878234398782365,
            "maximum_error_percentage_points": 0.10547945205479436,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.88888888888889,
          "radiance_percent": 13.88888888888889,
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
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004450516374145508,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "reflective_neighbour_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "reflective_neighbour_grid",
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
      "study_preparation_seconds": 0.3846463549998589,
      "weather_seconds": 0.2554603799999313,
      "metric_reduction_seconds": 0.3506471240002611,
      "write_seconds": 0.01597091299981912,
      "total_seconds": 0.622453600999961,
      "cold_end_to_end_seconds": 1.00709995599982,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0018438540000715875,
      "engine_upload_seconds": 0.063481569,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.039031603,
      "engine_annual_reduction_seconds": 0.00909067,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.039031603
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3846463549998589,
      "weather_seconds": 0.24452130100007707,
      "metric_reduction_seconds": 0.3003446500001701,
      "write_seconds": 0.012664540000059787,
      "total_seconds": 0.5578614860000926,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5578614860000926,
      "raw_export_seconds": 0.0015629419999640959,
      "engine_upload_seconds": 0.064398904,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 3.32e-07,
      "engine_annual_reduction_seconds": 0.010999245,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02897109300010925,
      "full": 0.06047032100013894
    }
  },
  "elapsed_seconds": 4.488024712999959,
  "result_class": "passed"
}
```
