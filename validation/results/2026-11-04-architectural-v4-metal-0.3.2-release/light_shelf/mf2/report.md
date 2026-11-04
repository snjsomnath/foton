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
  "model_sha256": "0dd2cc7d27739142110ddaf5502faec9a58a92f35e1885edf9be412cfbedf6cd",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 16584052180798691258,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 16584052180798691258,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/light_shelf/mf2/oracle/scene.rad"
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
            "nmbe_percent": 0.0013689131614196294,
            "cvrmse_percent": 6.163326972913974,
            "rms_normalized_rmse_percent": 0.8886191806232978,
            "reference_energy": 2.0172348706487355,
            "candidate_energy": 2.0172624848423766,
            "relative_energy_error_percent": 0.0013689131614196292,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.127869710326195e-06,
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
            "nmbe_percent": -1.5038983891627018,
            "cvrmse_percent": 72.1857242000038,
            "rms_normalized_rmse_percent": 2.2301184481008107,
            "reference_energy": 5.588499270798094,
            "candidate_energy": 5.504453920286192,
            "relative_energy_error_percent": 1.5038983891627018,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.648884449423349e-06,
              "p90": 1.1882399485330115e-05,
              "p95": 1.756049459800124e-05,
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
            "nmbe_percent": -1.1046630707272949,
            "cvrmse_percent": 53.0382685673237,
            "rms_normalized_rmse_percent": 2.2300360949033546,
            "reference_energy": 7.605734141446829,
            "candidate_energy": 7.5217164051285685,
            "relative_energy_error_percent": 1.104663070727295,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.645377665226988e-06,
              "p90": 1.1844126038340625e-05,
              "p95": 1.759847509674728e-05,
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
            "nmbe_percent": 0.0013689131614196294,
            "cvrmse_percent": 6.163326972913974,
            "rms_normalized_rmse_percent": 0.8886191806232978,
            "reference_energy": 2.0172348706487355,
            "candidate_energy": 2.0172624848423766,
            "relative_energy_error_percent": 0.0013689131614196292,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.127869710326195e-06,
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
            "nmbe_percent": 57.145558756968015,
            "cvrmse_percent": 593.6482982970881,
            "rms_normalized_rmse_percent": 12.73779918745458,
            "reference_energy": 3.502774092902653,
            "candidate_energy": 5.504453920286192,
            "relative_energy_error_percent": 57.14555875696801,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.904999852646142e-06,
              "p90": 5.8813998839468785e-05,
              "p95": 8.149747736752033e-05,
              "p99": 0.00014920090325176716,
              "maximum": 0.013440296053886414
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24112297594547272,
              "candidate": 0.25456327199935913,
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
            "nmbe_percent": 36.26275708598394,
            "cvrmse_percent": 376.7043709105763,
            "rms_normalized_rmse_percent": 12.7377723844028,
            "reference_energy": 5.520008963551389,
            "candidate_energy": 7.5217164051285685,
            "relative_energy_error_percent": 36.26275708598394,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.904999852646142e-06,
              "p90": 5.8813998839468785e-05,
              "p95": 8.145999890984967e-05,
              "p99": 0.00014869350707158446,
              "maximum": 0.013440296053886414
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24112297594547272,
              "candidate": 0.25456327199935913,
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
      "bias_percent": -0.15063722172897517,
      "rms_normalized_error_percent": 0.4834309044326917,
      "absolute_error": {
        "p95": 0.08027166282042963,
        "p99": 0.09320849125533272,
        "maximum": 0.09647509031837931
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.645497778813125,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.4834309044326917
    },
    "overcast": {
      "bias_percent": -0.3577422105296348,
      "rms_normalized_error_percent": 0.4870584850152874,
      "absolute_error": {
        "p95": 0.043712496757507324,
        "p99": 0.0506326675415039,
        "maximum": 0.0525813102722168
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1468346118927,
      "reference_fraction_of_uniform": 0.5574060678482056,
      "rms_normalized_to_uniform_percent": 0.281561593179496
    },
    "horizon": {
      "bias_percent": 0.9617581927154412,
      "rms_normalized_error_percent": 2.107659669505254,
      "absolute_error": {
        "p95": 0.05588324386483923,
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
      "rms_normalized_to_uniform_percent": 0.3401643351956957
    },
    "north": {
      "bias_percent": -5.325119852333219,
      "rms_normalized_error_percent": 11.364033929139584,
      "absolute_error": {
        "p95": 0.0020405577961355448,
        "p99": 0.003303579753264782,
        "maximum": 0.0039034541696310043
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.00927149597555399,
      "reference_fraction_of_uniform": 0.0016422814223915339,
      "rms_normalized_to_uniform_percent": 0.013073710782222296
    },
    "east": {
      "bias_percent": -0.47373106545010574,
      "rms_normalized_error_percent": 0.7131610533749612,
      "absolute_error": {
        "p95": 0.023672819137573242,
        "p99": 0.027500140666961662,
        "maximum": 0.029279470443725586
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1450376510620117,
      "reference_fraction_of_uniform": 0.20282314717769623,
      "rms_normalized_to_uniform_percent": 0.14958791574708608
    },
    "south": {
      "bias_percent": 0.09270276089025152,
      "rms_normalized_error_percent": 0.4838426055698335,
      "absolute_error": {
        "p95": 0.05196255445480347,
        "p99": 0.08821330070495599,
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
      "rms_normalized_to_uniform_percent": 0.3708205859163398
    },
    "west": {
      "bias_percent": -0.1958839908127827,
      "rms_normalized_error_percent": 0.5989276711861158,
      "absolute_error": {
        "p95": 0.02419281005859375,
        "p99": 0.031885015964508046,
        "maximum": 0.034282684326171875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.163352370262146,
      "reference_fraction_of_uniform": 0.2060672789812088,
      "rms_normalized_to_uniform_percent": 0.1281993185718601
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
          "nmbe_percent": -0.35515786208780553,
          "cvrmse_percent": 3.9074630922520797,
          "absolute_error_percentiles_lux": {
            "p50": 3.2564849853515625,
            "p90": 27.23254699707032,
            "p95": 40.182989501953124,
            "p99": 75.798397827148
          },
          "maximum_absolute_error_lux": 303.263671875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 1858.5,
            "foton_lux": 22163.26953125,
            "radiance_lux": 21860.005859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6688698630136978,
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
            "maximum_error_percentage_points": 0.004740207619860826,
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
      "study_preparation_seconds": 0.009804749977774918,
      "weather_seconds": 0.08486404200084507,
      "metric_reduction_seconds": 0.16564725001808256,
      "write_seconds": 0.018008749932050705,
      "total_seconds": 0.2686721249483526,
      "cold_end_to_end_seconds": 0.2784768749261275,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00168674997985363,
      "engine_upload_seconds": 0.000792708,
      "engine_acceleration_structure_seconds": 0.00330325,
      "engine_tracing_seconds": 0.05850354162976146,
      "engine_annual_reduction_seconds": 0.0015349583700299263,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05850354162976146
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009804749977774918,
      "weather_seconds": 0.08070537506137043,
      "metric_reduction_seconds": 0.0528670409694314,
      "write_seconds": 0.015330125112086535,
      "total_seconds": 0.14919233391992748,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14919233391992748,
      "raw_export_seconds": 0.004773000022396445,
      "engine_upload_seconds": 4.1125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015633333241567016,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.07102666702121496,
      "full": 0.06245166703592986
    }
  },
  "elapsed_seconds": 1.4470349170733243,
  "result_class": "passed"
}
```
