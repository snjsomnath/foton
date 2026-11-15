# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_triangle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_triangle",
    "category": "form",
    "question": "How does a triangle opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "triangle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4400000000000002
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "f6221f1bf0769b0e6e5eea86856c4295d6ddd47361f97d0578ba912cb4b05986",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 9377062490896781742,
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 9377062490896781742,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.8)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/52e717d2-b26e-4bbc-9536-f9b0a23834d6/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "ed5a6fc1adeb7a5676b12a2ae35ce646e75102b728358b7ecd68b3605e1ffd37",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "274288e18ebb896ca8da417745929f291321088f610eaef564604626c7d101ce",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00016772851813584566,
          "p95": 0.0,
          "p99": 8.686911314725876e-07
        },
        "bias_percent": 0.0718603497205187,
        "identifier": "plan_i_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2035155312483643,
        "worst_index": [
          36,
          364,
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
          "maximum": 0.00024631968699395657,
          "p95": 4.365505446912721e-06,
          "p99": 3.815406234934942e-05
        },
        "bias_percent": 0.02434674678831472,
        "identifier": "plan_i_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.7566261233622296,
        "worst_index": [
          47,
          266,
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
          "maximum": 0.0002751108258962631,
          "p95": 3.7777863326482475e-06,
          "p99": 2.8291072521824704e-05
        },
        "bias_percent": 0.07182977063836109,
        "identifier": "plan_i_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1845027732963476,
        "worst_index": [
          24,
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
            "identifier": "plan_i_triangle_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006458464777097106,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.002224687719754e-05
                },
                "candidate_energy": 2.857404527523613,
                "cvrmse_percent": 102.37722904130413,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1386563446636245,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.853448040773401,
                "relative_energy_error_percent": 0.1386563446636245,
                "rms_normalized_rmse_percent": 9.720380544105055,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019411714747548103,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0012953249970450997,
                  "rgb_channel": 0,
                  "sky_patch_index": 147
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000841580651467666,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011226352471567229
                },
                "candidate_energy": 0.6582247231506528,
                "cvrmse_percent": 604.2783002196968,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.14607553821006308,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6591876350363464,
                "relative_energy_error_percent": 0.14607553821006308,
                "rms_normalized_rmse_percent": 10.456741442545066,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00014457167708314955,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": -0.0006970089743845165,
                  "rgb_channel": 0,
                  "sky_patch_index": 87
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.54325001034886,
            "full": 392.5675420323387
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.83866694010794,
            "full": 391.49133290629834
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.517874953337,
            "full": 396.3241670280695
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.37016707658768,
            "full": 396.304624970071
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
            "identifier": "plan_i_triangle_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003587366663850844,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.651594426832164e-05
                },
                "candidate_energy": 2.8543486439905337,
                "cvrmse_percent": 55.53100468701282,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.13888137444349596,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.858318315753422,
                "relative_energy_error_percent": 0.138881374443496,
                "rms_normalized_rmse_percent": 5.288723895482952,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010774463298730552,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.0014361829962581396,
                  "rgb_channel": 0,
                  "sky_patch_index": 145
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004991554887965322,
                  "p50": 0.0,
                  "p90": 3.0367104955075774e-06,
                  "p95": 6.196934918989427e-06,
                  "p99": 7.500035389966865e-05
                },
                "candidate_energy": 1.3104159769421955,
                "cvrmse_percent": 179.44310524173076,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.7530491010799334,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3006216572438696,
                "relative_energy_error_percent": 0.7530491010799334,
                "rms_normalized_rmse_percent": 5.295105129091752,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00031405698973685503,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": -0.00018509849905967712,
                  "rgb_channel": 0,
                  "sky_patch_index": 149
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.51100007165223,
            "full": 5266.042541014031
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.86691701039672,
            "full": 5271.367875044234
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.34137498866767,
            "full": 5288.017874932848
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.6642079949379,
            "full": 5292.600083048455
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
            "identifier": "plan_i_triangle_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004093650495633483,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.520681250141962e-05
                },
                "candidate_energy": 2.8580306335707064,
                "cvrmse_percent": 54.84661457717062,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04655267457908652,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.856700762960827,
                "relative_energy_error_percent": 0.04655267457908652,
                "rms_normalized_rmse_percent": 5.219028194134878,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004042776999995112,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.003633411950431764,
                  "rgb_channel": 0,
                  "sky_patch_index": 411
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006029410287737846,
                  "p50": 0.0,
                  "p90": 3.0616889539203385e-06,
                  "p95": 6.436733258396998e-06,
                  "p99": 6.98655412634253e-05
                },
                "candidate_energy": 1.3021248772133625,
                "cvrmse_percent": 177.89932796078818,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5157123828113853,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3088749071852277,
                "relative_energy_error_percent": 0.5157123828113853,
                "rms_normalized_rmse_percent": 5.276480748424449,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00036741996882483363,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": -0.000235521059948951,
                  "rgb_channel": 0,
                  "sky_patch_index": 154
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.15479198284447,
            "full": 5678.3700418891385
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 218.24037504848093,
            "full": 5664.84083305113
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.70683300867677,
            "full": 5722.0758750336245
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.18183410260826,
            "full": 5801.882874919102
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
            "identifier": "plan_i_triangle_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001705389586277306,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3495784080296354e-05
                },
                "candidate_energy": 2.8563512135019664,
                "cvrmse_percent": 31.414619985922627,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06306972170335394,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.854550856221067,
                "relative_energy_error_percent": 0.06306972170335394,
                "rms_normalized_rmse_percent": 2.9910958159922125,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013376045390032232,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0015081434976309538,
                  "rgb_channel": 0,
                  "sky_patch_index": 141
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002923714928328991,
                  "p50": 0.0,
                  "p90": 2.1610521798720583e-06,
                  "p95": 4.4831310290760484e-06,
                  "p99": 4.112139286007735e-05
                },
                "candidate_energy": 1.3067424219503891,
                "cvrmse_percent": 106.03361043418447,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5574014385826486,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3140670505943426,
                "relative_energy_error_percent": 0.5574014385826486,
                "rms_normalized_rmse_percent": 3.1575180006820776,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.008515546564012766,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.008807918056845665,
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 300.86991691496223,
            "full": 10075.705999974161
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 303.5939160035923,
            "full": 10242.30141704902
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 313.6828748974949,
            "full": 10318.606583983637
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 324.8717909445986,
            "full": 10195.9720000159
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
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/plan_i_triangle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10721.816541976295,
      "invocation_count": 5,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_triangle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 45192.805791972205,
      "invocation_count": 5,
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
      74,
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
        "identifier": "plan_i_triangle_grid",
        "full_identifier": "plan_i_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013094850410736667,
            "cvrmse_percent": 6.825480617550058,
            "rms_normalized_rmse_percent": 0.6502254978088472,
            "reference_energy": 2.856727819191107,
            "candidate_energy": 2.856353734956542,
            "relative_energy_error_percent": 0.013094850410736667,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.685578798875467e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2507616315687584,
            "cvrmse_percent": 78.9674875271335,
            "rms_normalized_rmse_percent": 2.3432744900639415,
            "reference_energy": 1.3091279428204938,
            "candidate_energy": 1.2927538728035497,
            "relative_energy_error_percent": 1.2507616315687584,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7353380573913455e-06,
              "p95": 5.309639163897373e-06,
              "p99": 1.995134061871805e-05,
              "maximum": 0.0005226200446486473
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01422100979834795,
              "candidate": 0.013698389753699303,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4020339447235636,
            "cvrmse_percent": 24.652538286286898,
            "rms_normalized_rmse_percent": 2.32786945729618,
            "reference_energy": 4.165855762011601,
            "candidate_energy": 4.149107607760092,
            "relative_energy_error_percent": 0.4020339447235635,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7352848519512918e-06,
              "p95": 5.312209395924583e-06,
              "p99": 1.97726665646771e-05,
              "maximum": 0.0005226200446486473
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01422100979834795,
              "candidate": 0.013698389753699303,
              "position": [
                6.5,
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
      74,
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
        "identifier": "plan_i_triangle_grid",
        "full_identifier": "plan_i_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013094850410736667,
            "cvrmse_percent": 6.825480617550058,
            "rms_normalized_rmse_percent": 0.6502254978088472,
            "reference_energy": 2.856727819191107,
            "candidate_energy": 2.856353734956542,
            "relative_energy_error_percent": 0.013094850410736667,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.685578798875467e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 96.64507766463873,
            "cvrmse_percent": 1307.8616560380005,
            "rms_normalized_rmse_percent": 22.570205222022043,
            "reference_energy": 0.657404644019735,
            "candidate_energy": 1.2927538728035497,
            "relative_energy_error_percent": 96.64507766463875,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.989999853132758e-06,
              "p95": 2.094999945256859e-05,
              "p99": 5.815114072902406e-05,
              "maximum": 0.0028915246948599815
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011015945114195347,
              "candidate": 0.013907469809055328,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 18.069186383744814,
            "cvrmse_percent": 244.6535262418645,
            "rms_normalized_rmse_percent": 22.568907712549628,
            "reference_energy": 3.514132463210842,
            "candidate_energy": 4.149107607760092,
            "relative_energy_error_percent": 18.069186383744814,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0009999641624745e-05,
              "p95": 2.09400004678173e-05,
              "p99": 5.7318941071571394e-05,
              "maximum": 0.0028915246948599815
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011015945114195347,
              "candidate": 0.013907469809055328,
              "position": [
                5.5,
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
      "bias_percent": 0.030760845501898372,
      "rms_normalized_error_percent": 0.1313470894472148,
      "absolute_error": {
        "p95": 0.02477011040721195,
        "p99": 0.03747117220960801,
        "maximum": 0.05183050853714377
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6158454846111447,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1313470894472148
    },
    "overcast": {
      "bias_percent": 0.040721235847048586,
      "rms_normalized_error_percent": 0.11858836512016752,
      "absolute_error": {
        "p95": 0.01609814465045927,
        "p99": 0.023860847949981646,
        "maximum": 0.031726837158203125
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6479099988937378,
      "reference_fraction_of_uniform": 0.6299722194671631,
      "rms_normalized_to_uniform_percent": 0.08095304952228019
    },
    "horizon": {
      "bias_percent": 0.2676382702409207,
      "rms_normalized_error_percent": 1.423435522365978,
      "absolute_error": {
        "p95": 0.019159451448288883,
        "p99": 0.02918004981706739,
        "maximum": 0.042691887957591046
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3216862527813638,
      "reference_fraction_of_uniform": 0.1229760147049296,
      "rms_normalized_to_uniform_percent": 0.09407661033337035
    },
    "north": {
      "bias_percent": -99.89689981263861,
      "rms_normalized_error_percent": 99.9991015894809,
      "absolute_error": {
        "p95": 2.6569467445369802e-05,
        "p99": 5.4745766901760106e-05,
        "maximum": 0.00010085888061439618
      },
      "worst_index": [
        69
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 4.460376203496708e-06,
      "reference_fraction_of_uniform": 1.7051374925358687e-06,
      "rms_normalized_to_uniform_percent": 0.00015351343741306611
    },
    "east": {
      "bias_percent": 0.17253005706503388,
      "rms_normalized_error_percent": 0.18425000473320574,
      "absolute_error": {
        "p95": 0.007429730892181396,
        "p99": 0.013317120373249034,
        "maximum": 0.017108768224716187
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4737229347229004,
      "reference_fraction_of_uniform": 0.18109744787216187,
      "rms_normalized_to_uniform_percent": 0.037555077836356913
    },
    "south": {
      "bias_percent": 0.0089155714672948,
      "rms_normalized_error_percent": 0.13960985793246622,
      "absolute_error": {
        "p95": 0.018245986104011534,
        "p99": 0.03088965103030202,
        "maximum": 0.036151885986328125
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8688995838165283,
      "reference_fraction_of_uniform": 0.7144533395767212,
      "rms_normalized_to_uniform_percent": 0.09741890062271874
    },
    "west": {
      "bias_percent": -0.006558597397434222,
      "rms_normalized_error_percent": 0.1769668706229534,
      "absolute_error": {
        "p95": 0.005885262042284007,
        "p99": 0.012286067605018571,
        "maximum": 0.02031230926513672
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48126304149627686,
      "reference_fraction_of_uniform": 0.18397992849349976,
      "rms_normalized_to_uniform_percent": 0.03657276311930141
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
        "identifier": "plan_i_triangle_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.01854304211354533,
          "cvrmse_percent": 3.6307781692494108,
          "absolute_error_percentiles_lux": {
            "p50": 0.306272029876709,
            "p90": 6.784155654907227,
            "p95": 12.605015182495114,
            "p99": 33.82083374023434
          },
          "maximum_absolute_error_lux": 309.072265625,
          "worst": {
            "sensor_index": 48,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2867.5,
            "foton_lux": 25837.515625,
            "radiance_lux": 25528.443359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08213809700111055,
            "maximum_error_percentage_points": 1.3168493150684917,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15829476698655712,
            "maximum_error_percentage_points": 0.7915243942702297,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3248482043687521,
            "maximum_error_percentage_points": 3.0649315068493053,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3267271380970015,
            "maximum_error_percentage_points": 3.064931506849316,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0026675305442428834,
            "maximum_error_percentage_points": 0.05589041095890224,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.405405405405405,
          "radiance_percent": 5.405405405405405,
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
      "maximum_error_percentage_points": 0.004957191780825099,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004957191780825099,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_triangle_grid",
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
      "study_preparation_seconds": 0.008346624905243516,
      "weather_seconds": 0.08522687503136694,
      "metric_reduction_seconds": 0.1550657080952078,
      "write_seconds": 0.022992625134065747,
      "total_seconds": 0.2634167498908937,
      "cold_end_to_end_seconds": 0.2717633747961372,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002710832981392741,
      "engine_upload_seconds": 0.0008775,
      "engine_acceleration_structure_seconds": 0.003068208,
      "engine_tracing_seconds": 0.08552691666409373,
      "engine_annual_reduction_seconds": 0.0033088333439081907,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.08552691666409373
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008346624905243516,
      "weather_seconds": 0.07833033404313028,
      "metric_reduction_seconds": 0.05321604199707508,
      "write_seconds": 0.01590637513436377,
      "total_seconds": 0.14758295891806483,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14758295891806483,
      "raw_export_seconds": 0.0024535830598324537,
      "engine_upload_seconds": 6.8958e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0032920001540333033,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.023253042018041015,
      "full": 0.08857766701839864
    }
  },
  "elapsed_seconds": 1.8123397920280695,
  "result_class": "passed"
}
```
