# Foton report

Status: **passed**

```json
{
  "scene": "light_shelf",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "light_shelf",
    "category": "shading",
    "question": "Does a shelf block direct light and reflect light toward the ceiling?",
    "interactions": [
      "interior_shades",
      "exterior_shades",
      "shelf_reflection"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 2,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "ebfdce9d53978756a0890c1b29c72fc51711d3188c999a4eca19e3281586e5f0",
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
      "scene_fingerprint": 16584052180798691258,
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
      "scene_fingerprint": 16584052180798691258,
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
    "model_sha256": "da4bd6ca1d5da08752852b4c5a39e6ffc366f224c734a4f7ca46d2eaa89a5d0f",
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
          "maximum": 0.000105998944491148,
          "p95": 0.0,
          "p99": 8.038943633437157e-06
        },
        "bias_percent": 0.08366425731824396,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3550180328346797,
        "worst_index": [
          17,
          310,
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
          "maximum": 0.0010909736156463623,
          "p95": 1.694834281806834e-05,
          "p99": 7.838848978281021e-05
        },
        "bias_percent": 0.09546061676745492,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6323276286525236,
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
          "maximum": 0.0005722641944885254,
          "p95": 1.4714078133692965e-05,
          "p99": 6.572715938091278e-05
        },
        "bias_percent": 0.03673912520769952,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.4871455067332735,
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004297233826946467,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.481220331508666e-05
                },
                "candidate_energy": 2.0234308917215458,
                "cvrmse_percent": 63.55555254028864,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.4268103960312209,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0321041233783035,
                "relative_energy_error_percent": 0.4268103960312209,
                "rms_normalized_rmse_percent": 9.119843363842904,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009469281940255314,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.0005172048113308847,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.002061501145362854,
                  "p50": 0.0,
                  "p90": 7.317746621993927e-07,
                  "p95": 1.6857618902577087e-05,
                  "p99": 0.00022500392515212297
                },
                "candidate_energy": 3.501396592785497,
                "cvrmse_percent": 83.30672348627095,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.525691252977459,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4830863127059466,
                "relative_energy_error_percent": 0.525691252977459,
                "rms_normalized_rmse_percent": 1.7792255296652444,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.24393875151872635,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.2418772503733635,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.42083306144923,
            "full": 233.77433302812278
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.75308399833739,
            "full": 230.1327920285985
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.48525000922382,
            "full": 219.29741697385907
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.44900004565716,
            "full": 224.405457964167
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003486861241981387,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.408488404005766e-05
                },
                "candidate_energy": 2.0201274742312307,
                "cvrmse_percent": 57.46349121253514,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1926868238195558,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0162424407117214,
                "relative_energy_error_percent": 0.19268682381955582,
                "rms_normalized_rmse_percent": 8.279387986948958,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001998212421312928,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002346898545511067,
                  "rgb_channel": 0,
                  "sky_patch_index": 204
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0015575587749481201,
                  "p50": 1.832511941302073e-06,
                  "p90": 1.5043613075249607e-05,
                  "p95": 2.579557622084394e-05,
                  "p99": 0.00015231808356475085
                },
                "candidate_energy": 5.5763040469345775,
                "cvrmse_percent": 39.217414703415244,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04305570791266564,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.5787059982945095,
                "relative_energy_error_percent": 0.04305570791266564,
                "rms_normalized_rmse_percent": 1.20906213374253,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.2600490003824234,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.2584914416074753,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.6194999963045,
            "full": 2397.972041973844
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.84304210357368,
            "full": 2390.709750005044
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.8422918971628,
            "full": 2426.512207952328
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.6229580231011,
            "full": 2378.3690000418574
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000299985142191872,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010350389493396506
                },
                "candidate_energy": 2.0144897023747035,
                "cvrmse_percent": 57.039300643774126,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.12342428405207248,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.016979144443212,
                "relative_energy_error_percent": 0.12342428405207248,
                "rms_normalized_rmse_percent": 8.214490043016534,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0006702241953462362,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0009702093375381082,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012645162642002106,
                  "p50": 1.802101891712482e-06,
                  "p90": 1.4938431456812408e-05,
                  "p95": 2.5218796508852392e-05,
                  "p99": 0.00016119875363074243
                },
                "candidate_energy": 5.591615341390579,
                "cvrmse_percent": 36.574122175722714,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15794180125131704,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.582797770032371,
                "relative_energy_error_percent": 0.15794180125131704,
                "rms_normalized_rmse_percent": 1.129638612867091,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08778109028935432,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.08651657402515411,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.45112498104572,
            "full": 2579.8862089868635
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.9953330187127,
            "full": 2573.6010420368984
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.86120803747326,
            "full": 2661.3177499966696
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.450124935247,
            "full": 2597.899833926931
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018703335081227124,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.77795144636184e-05
                },
                "candidate_energy": 2.017077797031561,
                "cvrmse_percent": 33.732176329389,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.19881697979081941,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.013075461198696,
                "relative_energy_error_percent": 0.19881697979081941,
                "rms_normalized_rmse_percent": 4.855268862917421,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0003625584504334256,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.00017552509962115437,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013921111822128296,
                  "p50": 1.2628863146346703e-06,
                  "p90": 1.0605148463582746e-05,
                  "p95": 1.7347549146506935e-05,
                  "p99": 9.027012856677175e-05
                },
                "candidate_energy": 5.59181384876128,
                "cvrmse_percent": 26.801192716892057,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04137628493741746,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.589501120850937,
                "relative_energy_error_percent": 0.04137628493741746,
                "rms_normalized_rmse_percent": 0.8269899052014494,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.2587527483701706,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.2601448595523834,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.42145903687924,
            "full": 4568.377540912479
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.8277499238029,
            "full": 4896.078290999867
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.4601249936968,
            "full": 4614.745000028051
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.3947920333594,
            "full": 4549.170166021213
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
    "/content/suite-vulkan-0.3.3/light_shelf/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2564.9635000154376,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10753.982583992183,
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
        "identifier": "light_shelf_grid",
        "full_identifier": "light_shelf_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0013659298296051436,
            "cvrmse_percent": 6.163324668640257,
            "rms_normalized_rmse_percent": 0.8886188483965912,
            "reference_energy": 2.0172348706487355,
            "candidate_energy": 2.017262424661567,
            "relative_energy_error_percent": 0.0013659298296051434,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.1278988141566515e-06,
              "maximum": 7.743132300674915e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 310,
              "rgb_channel": 0,
              "reference": 0.002186180790886283,
              "candidate": 0.0021087494678795338,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.503949049993403,
            "cvrmse_percent": 72.18837887380114,
            "rms_normalized_rmse_percent": 2.230200462059592,
            "reference_energy": 5.588499270798094,
            "candidate_energy": 5.504451089106038,
            "relative_energy_error_percent": 1.503949049993403,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.6494506667186215e-06,
              "p90": 1.1883781189681032e-05,
              "p95": 1.7536669474793598e-05,
              "p99": 4.294223617762327e-05,
              "maximum": 0.005930274724960327
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.25998610258102417,
              "candidate": 0.25405582785606384,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.1047010862680728,
            "cvrmse_percent": 53.04020742550364,
            "rms_normalized_rmse_percent": 2.2301176157342746,
            "reference_energy": 7.605734141446829,
            "candidate_energy": 7.5217135137676046,
            "relative_energy_error_percent": 1.1047010862680728,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.646618329687044e-06,
              "p90": 1.1847309633594723e-05,
              "p95": 1.7592905351193622e-05,
              "p99": 4.262221045792103e-05,
              "maximum": 0.005930274724960327
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.25998610258102417,
              "candidate": 0.25405582785606384,
              "position": [
                2.5,
                0.5,
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
        "identifier": "light_shelf_grid",
        "full_identifier": "light_shelf_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0013659298296051436,
            "cvrmse_percent": 6.163324668640257,
            "rms_normalized_rmse_percent": 0.8886188483965912,
            "reference_energy": 2.0172348706487355,
            "candidate_energy": 2.017262424661567,
            "relative_energy_error_percent": 0.0013659298296051434,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.1278988141566515e-06,
              "maximum": 7.743132300674915e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 310,
              "rgb_channel": 0,
              "reference": 0.002186180790886283,
              "candidate": 0.0021087494678795338,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 57.14547793016961,
            "cvrmse_percent": 593.6451548943684,
            "rms_normalized_rmse_percent": 12.73773174005732,
            "reference_energy": 3.502774092902653,
            "candidate_energy": 5.504451089106038,
            "relative_energy_error_percent": 57.14547793016961,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.904999852646142e-06,
              "p90": 5.8813998839468785e-05,
              "p95": 8.149747736752033e-05,
              "p99": 0.00014920090325176716,
              "maximum": 0.013439729809761047
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24112297594547272,
              "candidate": 0.25456270575523376,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 36.26270470634139,
            "cvrmse_percent": 376.7023728137608,
            "rms_normalized_rmse_percent": 12.737704821336369,
            "reference_energy": 5.520008963551389,
            "candidate_energy": 7.5217135137676046,
            "relative_energy_error_percent": 36.26270470634139,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.904999852646142e-06,
              "p90": 5.8813998839468785e-05,
              "p95": 8.145999890984967e-05,
              "p99": 0.00014869350707158446,
              "maximum": 0.013439729809761047
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24112297594547272,
              "candidate": 0.25456270575523376,
              "position": [
                3.5,
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
      "bias_percent": -0.1506249063021594,
      "rms_normalized_error_percent": 0.48343827388424687,
      "absolute_error": {
        "p95": 0.08027770952144331,
        "p99": 0.09321686905059251,
        "maximum": 0.09647501868657571
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.645497778813125,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.48343827388424687
    },
    "overcast": {
      "bias_percent": -0.35772138129508635,
      "rms_normalized_error_percent": 0.4870545667394158,
      "absolute_error": {
        "p95": 0.043719351291656494,
        "p99": 0.05063024759292602,
        "maximum": 0.0525813102722168
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.146834373474121,
      "reference_fraction_of_uniform": 0.5574060082435608,
      "rms_normalized_to_uniform_percent": 0.2815593243818867
    },
    "horizon": {
      "bias_percent": 0.961367531407901,
      "rms_normalized_error_percent": 2.107161300194789,
      "absolute_error": {
        "p95": 0.05588322823608194,
        "p99": 0.08066329916922774,
        "maximum": 0.0889422066734391
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3285547223024725,
      "reference_fraction_of_uniform": 0.23532995217682642,
      "rms_normalized_to_uniform_percent": 0.3400839012112015
    },
    "north": {
      "bias_percent": -5.326040219776842,
      "rms_normalized_error_percent": 11.36254130302516,
      "absolute_error": {
        "p95": 0.0020382534712553024,
        "p99": 0.0033035785425454354,
        "maximum": 0.003903452306985855
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.009271495044231415,
      "reference_fraction_of_uniform": 0.0016422811895608902,
      "rms_normalized_to_uniform_percent": 0.013071993131202062
    },
    "east": {
      "bias_percent": -0.4741959054048501,
      "rms_normalized_error_percent": 0.7132614823594025,
      "absolute_error": {
        "p95": 0.023725688457489014,
        "p99": 0.02749990224838256,
        "maximum": 0.029279232025146484
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1450376510620117,
      "reference_fraction_of_uniform": 0.20282314717769623,
      "rms_normalized_to_uniform_percent": 0.14960898773997605
    },
    "south": {
      "bias_percent": 0.09270607306691217,
      "rms_normalized_error_percent": 0.48386544628823597,
      "absolute_error": {
        "p95": 0.05196559429168701,
        "p99": 0.0882173061370849,
        "maximum": 0.10368061065673828
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.198605537414551,
      "reference_fraction_of_uniform": 0.7437086701393127,
      "rms_normalized_to_uniform_percent": 0.37083809418468316
    },
    "west": {
      "bias_percent": -0.19543909521805386,
      "rms_normalized_error_percent": 0.5988772715521291,
      "absolute_error": {
        "p95": 0.024192988872528076,
        "p99": 0.03185588121414184,
        "maximum": 0.03423786163330078
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1633524894714355,
      "reference_fraction_of_uniform": 0.20606729388237,
      "rms_normalized_to_uniform_percent": 0.128188541783216
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
        "identifier": "light_shelf_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.35519237752731475,
          "cvrmse_percent": 3.907292360925734,
          "absolute_error_percentiles_lux": {
            "p50": 3.256092071533203,
            "p90": 27.22915649414063,
            "p95": 40.18301849365234,
            "p99": 75.79844909667924
          },
          "maximum_absolute_error_lux": 303.25390625,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 1858.5,
            "foton_lux": 22163.259765625,
            "radiance_lux": 21860.005859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6680365296803644,
            "maximum_error_percentage_points": 2.905205479452057,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17974655238115606,
            "maximum_error_percentage_points": 0.6152941923598192,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.23227549467275496,
            "maximum_error_percentage_points": 0.8204109589041089,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.24781963470319665,
            "maximum_error_percentage_points": 0.7947945205479385,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04398401826484014,
            "maximum_error_percentage_points": 0.5519178082191729,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 36.111111111111114,
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
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004746896404114409,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "light_shelf_grid",
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
      "study_preparation_seconds": 0.38517550999995365,
      "weather_seconds": 0.25714013299989347,
      "metric_reduction_seconds": 1.0354532210001253,
      "write_seconds": 0.012656833999926675,
      "total_seconds": 1.3055846370000381,
      "cold_end_to_end_seconds": 1.6907601469999918,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015578150000692403,
      "engine_upload_seconds": 0.045284057,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03226778,
      "engine_annual_reduction_seconds": 0.036256623,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03226778
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38517550999995365,
      "weather_seconds": 0.23769797499994638,
      "metric_reduction_seconds": 1.0160505950000243,
      "write_seconds": 0.011720500999899741,
      "total_seconds": 1.2657714449999276,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2657714449999276,
      "raw_export_seconds": 0.0016566100000545703,
      "engine_upload_seconds": 0.045081024,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.17e-07,
      "engine_annual_reduction_seconds": 0.042278953,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019201031999955376,
      "full": 0.05344303700007913
    }
  },
  "elapsed_seconds": 5.715258201000097,
  "result_class": "passed"
}
```
