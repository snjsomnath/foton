# Foton report

Status: **passed**

```json
{
  "scene": "teaching_reflectance30",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_reflectance30",
    "category": "teaching",
    "question": "How much does 0.3 surface reflectance cost at the back of the room?",
    "interactions": [
      "multiple_bounces",
      "reflectance",
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
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "dafe41b134670508fe460690438ba75e062d0036e902fdf7bc68919b000069c4",
  "weather_sha256": "d6e21c48181f8f154e82514cc5fb46924d2844a9b5984ce6959d4ba6c95ddafe",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 8544998466427496008,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 8544998466427496008,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_reflectance30_grid",
        "bias_percent": -0.060910624560303654,
        "rms_normalized_error_percent": 0.9651389221795657,
        "absolute_error": {
          "p95": 1.1893303599208524e-05,
          "p99": 0.00012718886137008667,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          17,
          121,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_reflectance30_grid",
        "bias_percent": 0.0013469798750903215,
        "rms_normalized_error_percent": 1.1339225533855668,
        "absolute_error": {
          "p95": 6.17127705481833e-05,
          "p99": 0.0001617162488400936,
          "maximum": 0.00031404406763613224
        },
        "worst_index": [
          10,
          14,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_reflectance30_grid",
        "bias_percent": 0.0026335752748036577,
        "rms_normalized_error_percent": 0.8843461215542829,
        "absolute_error": {
          "p95": 5.070024053566157e-05,
          "p99": 0.00012181326746940613,
          "maximum": 0.00030777696520090103
        },
        "worst_index": [
          23,
          73,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_reflectance30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.001923233748183947,
                "cvrmse_percent": 8.006436269944835,
                "rms_normalized_rmse_percent": 1.9801296193904543,
                "reference_energy": 8.95430237162509,
                "candidate_energy": 8.954130159459964,
                "relative_energy_error_percent": 0.001923233748183947,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.759073585271835e-07,
                  "p95": 9.161668604065195e-05,
                  "p99": 0.00023534346837550402,
                  "maximum": 0.0005262200720608234
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.012748399749398232,
                  "candidate": 0.013274619821459055
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.015711239949777783,
                "cvrmse_percent": 64.9925989924586,
                "rms_normalized_rmse_percent": 2.8912904598701545,
                "reference_energy": 1.8596650038524984,
                "candidate_energy": 1.8599571802835158,
                "relative_energy_error_percent": 0.015711239949777783,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.3579301089048386e-05,
                  "p95": 0.00015979807940311722,
                  "p99": 0.0003753025084733963,
                  "maximum": 0.0007930994033813477
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.0005279998295009136,
                  "candidate": -0.00026509957388043404
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 112.14766697958112,
            "full": 220.5153750255704
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 104.49158295523375,
            "full": 226.57891595736146
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 117.4960839562118,
            "full": 225.3935420885682
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 107.60545800440013,
            "full": 234.26312510855496
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_reflectance30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.014480354982425142,
                "cvrmse_percent": 7.040333762240674,
                "rms_normalized_rmse_percent": 1.7381158730639383,
                "reference_energy": 8.955192788238492,
                "candidate_energy": 8.953896044533394,
                "relative_energy_error_percent": 0.014480354982425142,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.316680133342743e-07,
                  "p95": 7.039290794637054e-05,
                  "p99": 0.00020652031525969505,
                  "maximum": 0.0004205788718536496
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.004208698403090239,
                  "candidate": 0.003788119531236589
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.21603182215798714,
                "cvrmse_percent": 35.63035274981491,
                "rms_normalized_rmse_percent": 2.0586251005910334,
                "reference_energy": 2.5302312677832184,
                "candidate_energy": 2.524765163070615,
                "relative_energy_error_percent": 0.21603182215798714,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.663469668907965e-08,
                  "p90": 2.3474087356589735e-05,
                  "p95": 0.00011417530768085246,
                  "p99": 0.00029072281904518604,
                  "maximum": 0.0006541889160871506
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 42,
                  "rgb_channel": 0,
                  "reference": 0.0003815449308604002,
                  "candidate": 0.0010357338469475508
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.38279201183468,
            "full": 1456.6857080208138
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 129.35587496031076,
            "full": 1443.5617920244113
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.06558307260275,
            "full": 1437.5661660451442
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.5584170240909,
            "full": 1431.7858750000596
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_reflectance30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02473713211716699,
                "cvrmse_percent": 7.023698496649764,
                "rms_normalized_rmse_percent": 1.7339183102950997,
                "reference_energy": 8.95099578472491,
                "candidate_energy": 8.94878156507184,
                "relative_energy_error_percent": 0.02473713211716699,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.479967851191759e-07,
                  "p95": 8.28175107017159e-05,
                  "p99": 0.0002088181208819151,
                  "maximum": 0.00042125198524445295
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.001895635505206883,
                  "candidate": 0.002316887490451336
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.03681285013479788,
                "cvrmse_percent": 36.55574617672224,
                "rms_normalized_rmse_percent": 2.115234559355921,
                "reference_energy": 2.531842558124435,
                "candidate_energy": 2.532774601531006,
                "relative_energy_error_percent": 0.03681285013479788,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0919892545757648e-07,
                  "p90": 2.6611844077706337e-05,
                  "p95": 0.00012698843493126334,
                  "p99": 0.0003018598072230816,
                  "maximum": 0.0005931220948696136
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": -7.575168274343014e-05,
                  "candidate": 0.0005173704121261835
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.94033296592534,
            "full": 1445.9714160766453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.25333300884813,
            "full": 1440.1922500692308
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.08995806518942,
            "full": 1431.70304200612
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.89379198290408,
            "full": 1396.8059999169782
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_reflectance30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.009489252842916013,
                "cvrmse_percent": 3.6089688333361787,
                "rms_normalized_rmse_percent": 0.8911567025683281,
                "reference_energy": 8.95001625380155,
                "candidate_energy": 8.950865543473356,
                "relative_energy_error_percent": 0.009489252842916013,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.0511215552687645e-06,
                  "p95": 4.265708557795708e-05,
                  "p99": 0.00010782794561237097,
                  "maximum": 0.00023207534104585648
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.007134623592719436,
                  "candidate": 0.007366698933765292
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.12271887774307924,
                "cvrmse_percent": 19.848292884071963,
                "rms_normalized_rmse_percent": 1.1475137339791976,
                "reference_energy": 2.53050604955504,
                "candidate_energy": 2.5336114581802747,
                "relative_energy_error_percent": 0.12271887774307923,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.739544116702746e-08,
                  "p90": 1.5806173905730247e-05,
                  "p95": 6.509454688057298e-05,
                  "p99": 0.00016397936269640923,
                  "maximum": 0.00035353144630789757
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 73,
                  "rgb_channel": 0,
                  "reference": -4.367902874946594e-05,
                  "candidate": 0.0003098524175584316
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.07470802031457,
            "full": 2447.5551249925047
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 209.78824992198497,
            "full": 2452.2018749266863
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 205.56016697082669,
            "full": 2489.6276249783114
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 206.6938750213012,
            "full": 2479.448084020987
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 764.4704999402165,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance30/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2474.691708921455,
      "worker_pool_size": 12,
      "invocation_count": 3
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
        "identifier": "teaching_reflectance30_grid",
        "full_identifier": "teaching_reflectance30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05723220978688256,
            "cvrmse_percent": 2.4774779687458786,
            "rms_normalized_rmse_percent": 0.6117136004025637,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272297551739,
            "relative_energy_error_percent": 0.05723220978688257,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.248906720429523e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.026316598088036,
            "cvrmse_percent": 28.888275564402516,
            "rms_normalized_rmse_percent": 1.6690272599725104,
            "reference_energy": 2.529103131239655,
            "candidate_energy": 2.503146526020978,
            "relative_energy_error_percent": 1.026316598088036,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.296567771509217e-07,
              "p90": 2.0631348888855428e-05,
              "p95": 4.12501161918044e-05,
              "p99": 0.00011560576967895031,
              "maximum": 0.0011674724519252777
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02409423142671585,
              "candidate": 0.022926758974790573,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.27068001596379554,
            "cvrmse_percent": 6.34568940221239,
            "rms_normalized_rmse_percent": 1.6645257760428869,
            "reference_energy": 11.482499655473195,
            "candidate_energy": 11.451418823572716,
            "relative_energy_error_percent": 0.2706800159638033,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.2761145146432682e-07,
              "p90": 2.0098406821489334e-05,
              "p95": 3.939515445381394e-05,
              "p99": 0.0001153913326561451,
              "maximum": 0.0011674724519252777
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02409423142671585,
              "candidate": 0.022926758974790573,
              "position": [
                3.5,
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
        "identifier": "teaching_reflectance30_grid",
        "full_identifier": "teaching_reflectance30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05723220978688256,
            "cvrmse_percent": 2.4774779687458786,
            "rms_normalized_rmse_percent": 0.6117136004025637,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272297551739,
            "relative_energy_error_percent": 0.05723220978688257,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.248906720429523e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 34.53214237295649,
            "cvrmse_percent": 174.74546902425186,
            "rms_normalized_rmse_percent": 7.781145682421421,
            "reference_energy": 1.8606308365190785,
            "candidate_energy": 2.503146526020978,
            "relative_energy_error_percent": 34.53214237295649,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.445999603485689e-05,
              "p95": 0.00014710389514220842,
              "p99": 0.00039656367152929306,
              "maximum": 0.003232399933040142
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009465799666941166,
              "candidate": 0.012698199599981308,
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
            "nmbe_percent": 5.894117349225373,
            "cvrmse_percent": 30.078282844295178,
            "rms_normalized_rmse_percent": 7.784270362982261,
            "reference_energy": 10.814027360752618,
            "candidate_energy": 11.451418823572716,
            "relative_energy_error_percent": 5.894117349225365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.530286843073554e-05,
              "p95": 0.00015088830841705186,
              "p99": 0.00039588427171111107,
              "maximum": 0.003232399933040142
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009465799666941166,
              "candidate": 0.012698199599981308,
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
      "bias_percent": 0.07325999124487477,
      "rms_normalized_error_percent": 0.1520019150711872,
      "absolute_error": {
        "p95": 0.06942980670910992,
        "p99": 0.07305820278075419,
        "maximum": 0.07463325382101926
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.904688052489908,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1520019150711872
    },
    "overcast": {
      "bias_percent": 0.03658345883776166,
      "rms_normalized_error_percent": 0.12911350310595116,
      "absolute_error": {
        "p95": 0.04460543394088745,
        "p99": 0.05151011943817138,
        "maximum": 0.05376768112182617
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.265722274780273,
      "reference_fraction_of_uniform": 0.645452618598938,
      "rms_normalized_to_uniform_percent": 0.09079575328240007
    },
    "horizon": {
      "bias_percent": 1.1668381291528545,
      "rms_normalized_error_percent": 2.0068191534249586,
      "absolute_error": {
        "p95": 0.06757944872624777,
        "p99": 0.08206747923064392,
        "maximum": 0.08785091664879552
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2784280315321181,
      "reference_fraction_of_uniform": 0.08038057881506062,
      "rms_normalized_to_uniform_percent": 0.1022601403634855
    },
    "north": {
      "bias_percent": -60.6462184477459,
      "rms_normalized_error_percent": 86.1566265071017,
      "absolute_error": {
        "p95": 1.8375601314346568e-05,
        "p99": 0.0001555039606841999,
        "maximum": 0.00021607194503303617
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.0225999176327605e-05,
      "reference_fraction_of_uniform": 6.429550580833165e-07,
      "rms_normalized_to_uniform_percent": 0.00013735350633085352
    },
    "east": {
      "bias_percent": -0.010039678735949274,
      "rms_normalized_error_percent": 0.1610546577363629,
      "absolute_error": {
        "p95": 0.02127707004547119,
        "p99": 0.029349160194396963,
        "maximum": 0.03145551681518555
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.192307949066162,
      "reference_fraction_of_uniform": 0.20071490108966827,
      "rms_normalized_to_uniform_percent": 0.036527748606014876
    },
    "south": {
      "bias_percent": 0.10776055525590161,
      "rms_normalized_error_percent": 0.19077860781086853,
      "absolute_error": {
        "p95": 0.06187748908996582,
        "p99": 0.07295563220977781,
        "maximum": 0.07738947868347168
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.958292007446289,
      "reference_fraction_of_uniform": 0.6889976263046265,
      "rms_normalized_to_uniform_percent": 0.12157688045596314
    },
    "west": {
      "bias_percent": 0.0012247342635737105,
      "rms_normalized_error_percent": 0.21099960778792745,
      "absolute_error": {
        "p95": 0.026796936988830566,
        "p99": 0.03706674575805662,
        "maximum": 0.04106283187866211
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0949769020080566,
      "reference_fraction_of_uniform": 0.19459526240825653,
      "rms_normalized_to_uniform_percent": 0.04586108809392029
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
        "identifier": "teaching_reflectance30_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.060519803331117145,
          "cvrmse_percent": 1.0942872056767514,
          "absolute_error_percentiles_lux": {
            "p50": 3.0895233154296875,
            "p90": 20.331756591796886,
            "p95": 34.02089843750002,
            "p99": 97.62220703125001
          },
          "maximum_absolute_error_lux": 444.92236328125,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6542.5,
            "foton_lux": 5767.65673828125,
            "radiance_lux": 6212.5791015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.38067732115677316,
            "maximum_error_percentage_points": 1.346027397260272,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.21520340483165296,
            "maximum_error_percentage_points": 1.1252108589916077,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1065487062404872,
            "maximum_error_percentage_points": 0.6558904109589054,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1230175038051745,
            "maximum_error_percentage_points": 0.6558904109589037,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01977929984779267,
            "maximum_error_percentage_points": 0.16726027397260168,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 66.66666666666667,
          "radiance_percent": 66.66666666666667,
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
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004876391267131908,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_reflectance30_grid",
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
      "study_preparation_seconds": 0.007090458064340055,
      "weather_seconds": 0.0990315000526607,
      "metric_reduction_seconds": 0.04768816696014255,
      "write_seconds": 0.03687304200138897,
      "total_seconds": 0.18376191693823785,
      "cold_end_to_end_seconds": 0.1908523750025779,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00842750002630055,
      "engine_upload_seconds": 0.000329625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02973870828282088,
      "engine_annual_reduction_seconds": 0.00034374999813735485,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02973870828282088
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007090458064340055,
      "weather_seconds": 0.0967597080161795,
      "metric_reduction_seconds": 0.011778207961469889,
      "write_seconds": 0.030005999957211316,
      "total_seconds": 0.13870558398775756,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13870558398775756,
      "raw_export_seconds": 0.009335958980955184,
      "engine_upload_seconds": 5.2292e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003528749803081155,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.007481875014491379,
      "full": 0.02123354095965624
    }
  },
  "elapsed_seconds": 29.362381541985087,
  "result_class": "passed"
}
```
