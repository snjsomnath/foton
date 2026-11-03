# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 1.44
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "4fd30312bc1803fb47a1bd2ccea398fa2db197586568e99a37c140a615f02091",
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
      "scene_fingerprint": 17665444809337020543,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17665444809337020543,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "60803980e0f8e458f78b83f4f3232332613481acd700f9d549da1598c8351ed0",
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
          "maximum": 0.00043346919119358063,
          "p95": 0.0,
          "p99": 4.046782851219177e-05
        },
        "bias_percent": -0.010166153108011812,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2433599888093296,
        "worst_index": [
          39,
          132,
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
          "maximum": 0.0003810077905654907,
          "p95": 1.404155045747757e-05,
          "p99": 7.405132055282593e-05
        },
        "bias_percent": -0.04701226156500272,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1956371595498776,
        "worst_index": [
          35,
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
          "maximum": 0.00040930788964033127,
          "p95": 1.1524203728185967e-05,
          "p99": 5.771545693278313e-05
        },
        "bias_percent": 0.11672416009453726,
        "identifier": "plan_l_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.988652321439593,
        "worst_index": [
          35,
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000723179429769516,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012351013720035553
                },
                "candidate_energy": 2.5876628879559576,
                "cvrmse_percent": 22.54740532722233,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04803834835429675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.588906555905851,
                "relative_energy_error_percent": 0.04803834835429675,
                "rms_normalized_rmse_percent": 2.5459925015470057,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.011925219558179379,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.011202040128409863,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010093768942169845,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1572579751373269e-05,
                  "p99": 0.00022412766702473164
                },
                "candidate_energy": 0.6254719084896578,
                "cvrmse_percent": 151.38829327900646,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.6518671512965476,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6214210686717507,
                "relative_energy_error_percent": 0.6518671512965475,
                "rms_normalized_rmse_percent": 3.7540225140718575,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0006733724731020629,
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "reference": 0.00033600442111492157,
                  "rgb_channel": 0,
                  "sky_patch_index": 20
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.95383298583329,
            "full": 273.9154170267284
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.64554204232991,
            "full": 259.46833298075944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.90704204235226,
            "full": 276.675375062041
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.7088749781251,
            "full": 283.90925005078316
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000485594617202878,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.119066089624539e-05
                },
                "candidate_energy": 2.586599080957967,
                "cvrmse_percent": 14.975474877630697,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.17532720924946435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5911420580159756,
                "relative_energy_error_percent": 0.17532720924946432,
                "rms_normalized_rmse_percent": 1.6940525972791918,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002008748473599553,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.002494343090802431,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008714701980352402,
                  "p50": 4.735846026449053e-08,
                  "p90": 9.403402918906082e-06,
                  "p95": 2.0661951566580683e-05,
                  "p99": 0.00015160837210714817
                },
                "candidate_energy": 1.2699237731618958,
                "cvrmse_percent": 49.53785878533232,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5905419141853943,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2624683682937885,
                "relative_energy_error_percent": 0.5905419141853943,
                "rms_normalized_rmse_percent": 2.2904221716241455,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.019236464984714985,
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "reference": 0.018364994786679745,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.28708406258374,
            "full": 3040.081541053951
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.6414589760825,
            "full": 3096.0297499550506
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.7907500108704,
            "full": 3050.17045896966
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.01133301202208,
            "full": 3147.2170420456678
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004168921150267124,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.933370554586872e-05
                },
                "candidate_energy": 2.590525053839883,
                "cvrmse_percent": 14.608927436263839,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07187595255686935,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.588664426624746,
                "relative_energy_error_percent": 0.07187595255686934,
                "rms_normalized_rmse_percent": 1.6512479008946022,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00562939653173089,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.005212504416704178,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006503753829747438,
                  "p50": 4.36766356415319e-08,
                  "p90": 9.441283134492563e-06,
                  "p95": 1.975451596081257e-05,
                  "p99": 0.00013168947771191597
                },
                "candidate_energy": 1.261293331501399,
                "cvrmse_percent": 44.25572869668288,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.37380228686147465,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.266025764762336,
                "relative_energy_error_percent": 0.37380228686147465,
                "rms_normalized_rmse_percent": 2.0499968973386675,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0002296334132552147,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.00042074196971952915,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.6419579796493,
            "full": 3316.0144579596817
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.36795789841563,
            "full": 3238.4121250361204
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.33525003492832,
            "full": 3253.049209015444
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.67433298565447,
            "full": 3274.220082908869
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
            "identifier": "plan_l_small_center_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001913602463901043,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.2401807149872184e-05
                },
                "candidate_energy": 2.588927204612446,
                "cvrmse_percent": 7.514270500248501,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0653921406358476,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5872353560298507,
                "relative_energy_error_percent": 0.0653921406358476,
                "rms_normalized_rmse_percent": 0.8486887742869917,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014776010066270828,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.014584649819880724,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000329495407640934,
                  "p50": 4.8746247927056174e-08,
                  "p90": 6.743167250533591e-06,
                  "p95": 1.3024819054407999e-05,
                  "p99": 8.008250733837485e-05
                },
                "candidate_energy": 1.2690555555508425,
                "cvrmse_percent": 27.747088786543696,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.09684967631422445,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2702858232589342,
                "relative_energy_error_percent": 0.09684967631422445,
                "rms_normalized_rmse_percent": 1.2892428272041818,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01777043007314205,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.018099925480782986,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.47229200974107,
            "full": 5795.12424999848
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.04650002904236,
            "full": 5798.637000028975
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.4026670064777,
            "full": 5808.119958033785
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 239.4836669554934,
            "full": 5837.244792026468
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_l_small_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1311.0947080422193,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_small_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4883.553290972486,
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
        "identifier": "plan_l_small_center_grid",
        "full_identifier": "plan_l_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01614905774978766,
            "cvrmse_percent": 6.276302062834888,
            "rms_normalized_rmse_percent": 0.7087849847351071,
            "reference_energy": 2.587996424330413,
            "candidate_energy": 2.5884143613675406,
            "relative_energy_error_percent": 0.01614905774978766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.9098999220877886e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 41,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0513113531415974,
            "cvrmse_percent": 32.606110639451295,
            "rms_normalized_rmse_percent": 1.5144345784740447,
            "reference_energy": 1.2697555477951923,
            "candidate_energy": 1.2564064635640761,
            "relative_energy_error_percent": 1.0513113531415974,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.191997752897805e-08,
              "p90": 1.4514456961478573e-05,
              "p95": 2.609291550470516e-05,
              "p99": 6.722302350681275e-05,
              "maximum": 0.00047537311911582947
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005023983307182789,
              "candidate": 0.004548610188066959,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.33519903009377694,
            "cvrmse_percent": 10.19871507957739,
            "rms_normalized_rmse_percent": 1.4391668979651877,
            "reference_energy": 3.8577519721256053,
            "candidate_energy": 3.8448208249316167,
            "relative_energy_error_percent": 0.3351990300937769,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.191997752897805e-08,
              "p90": 1.4363913214765507e-05,
              "p95": 2.5686342269182205e-05,
              "p99": 6.140116602182388e-05,
              "maximum": 0.00047537311911582947
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005023983307182789,
              "candidate": 0.004548610188066959,
              "position": [
                0.5,
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
      48,
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
        "identifier": "plan_l_small_center_grid",
        "full_identifier": "plan_l_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01614905774978766,
            "cvrmse_percent": 6.276302062834888,
            "rms_normalized_rmse_percent": 0.7087849847351071,
            "reference_energy": 2.587996424330413,
            "candidate_energy": 2.5884143613675406,
            "relative_energy_error_percent": 0.01614905774978766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.9098999220877886e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 41,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 101.43280734693369,
            "cvrmse_percent": 725.2786977233798,
            "rms_normalized_rmse_percent": 18.077122743524296,
            "reference_energy": 0.623734772955892,
            "candidate_energy": 1.2564064635640761,
            "relative_energy_error_percent": 101.4328073469337,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.559546779953976e-05,
              "p95": 0.00011149000056320801,
              "p99": 0.0002439499949105084,
              "maximum": 0.004972847178578377
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015703972429037094,
              "candidate": 0.02067681960761547,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.71178746777531,
            "cvrmse_percent": 140.7919931908969,
            "rms_normalized_rmse_percent": 18.06931030291467,
            "reference_energy": 3.211731197286305,
            "candidate_energy": 3.8448208249316167,
            "relative_energy_error_percent": 19.71178746777531,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.615807865273385e-05,
              "p95": 0.00011239999730605632,
              "p99": 0.0002475989604135975,
              "maximum": 0.004972847178578377
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015703972429037094,
              "candidate": 0.02067681960761547,
              "position": [
                4.5,
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
      "bias_percent": 0.12536716547252438,
      "rms_normalized_error_percent": 0.2234110899690178,
      "absolute_error": {
        "p95": 0.03991686965059528,
        "p99": 0.08011111054006662,
        "maximum": 0.09849208727423253
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7219076744494077,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2234110899690178
    },
    "overcast": {
      "bias_percent": 0.10104972761902564,
      "rms_normalized_error_percent": 0.18752625763825798,
      "absolute_error": {
        "p95": 0.027995061874389646,
        "p99": 0.04705988407135014,
        "maximum": 0.06298112869262695
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.477062225341797,
      "reference_fraction_of_uniform": 0.6655356287956238,
      "rms_normalized_to_uniform_percent": 0.13664617987713334
    },
    "horizon": {
      "bias_percent": 0.6430694886694297,
      "rms_normalized_error_percent": 3.464473542900001,
      "absolute_error": {
        "p95": 0.01654770485930392,
        "p99": 0.04239308470458393,
        "maximum": 0.05262836838809548
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.23581298042602883,
      "reference_fraction_of_uniform": 0.0633580951093617,
      "rms_normalized_to_uniform_percent": 0.10701073608517071
    },
    "north": {
      "bias_percent": -93.37189000083923,
      "rms_normalized_error_percent": 99.71515981260653,
      "absolute_error": {
        "p95": 9.870482790574896e-05,
        "p99": 0.00028384960926814546,
        "maximum": 0.00036527967040456133
      },
      "worst_index": [
        44
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.9074699594057165e-05,
      "reference_fraction_of_uniform": 5.124979452375555e-06,
      "rms_normalized_to_uniform_percent": 0.0005939890901150307
    },
    "east": {
      "bias_percent": 0.05090811312503566,
      "rms_normalized_error_percent": 0.45740605507650484,
      "absolute_error": {
        "p95": 0.023035217821598043,
        "p99": 0.027776905298233037,
        "maximum": 0.028990983963012695
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9130687713623047,
      "reference_fraction_of_uniform": 0.2453227937221527,
      "rms_normalized_to_uniform_percent": 0.10051446131679143
    },
    "south": {
      "bias_percent": 0.14063738160170414,
      "rms_normalized_error_percent": 0.2849981952265579,
      "absolute_error": {
        "p95": 0.0374340385198593,
        "p99": 0.07012265205383304,
        "maximum": 0.08607101440429688
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3816537857055664,
      "reference_fraction_of_uniform": 0.6399013996124268,
      "rms_normalized_to_uniform_percent": 0.18498560062875957
    },
    "west": {
      "bias_percent": 0.15982114534174924,
      "rms_normalized_error_percent": 0.2838432178187295,
      "absolute_error": {
        "p95": 0.014722935855388633,
        "p99": 0.021884995102882387,
        "maximum": 0.02347320318222046
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7290275692939758,
      "reference_fraction_of_uniform": 0.19587470591068268,
      "rms_normalized_to_uniform_percent": 0.058881122826275896
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
        "identifier": "plan_l_small_center_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.06655554331131988,
          "cvrmse_percent": 2.555726906111657,
          "absolute_error_percentiles_lux": {
            "p50": 0.7368078231811523,
            "p90": 9.916697311401371,
            "p95": 16.947633361816408,
            "p99": 37.87910156249973
          },
          "maximum_absolute_error_lux": 170.6640625,
          "worst": {
            "sensor_index": 39,
            "position": [
              4.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4453.5,
            "foton_lux": 37376.2734375,
            "radiance_lux": 37546.9375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.21537385844748838,
            "maximum_error_percentage_points": 1.2378082191780821,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3325562645839019,
            "maximum_error_percentage_points": 1.2834459291663087,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.31292522831050135,
            "maximum_error_percentage_points": 3.179726027397251,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3135388127853874,
            "maximum_error_percentage_points": 3.179726027397262,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006204337899543467,
            "maximum_error_percentage_points": 0.1686301369863017,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 12.5,
          "radiance_percent": 12.5,
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
      "maximum_error_percentage_points": 0.004964549443492672,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004964549443492672,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_small_center_grid",
            "maximum_error_percentage_points": 0.004246575342467196,
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
      "study_preparation_seconds": 0.3728418159989815,
      "weather_seconds": 0.27143928599980427,
      "metric_reduction_seconds": 0.19282483300048625,
      "write_seconds": 0.039666356999077834,
      "total_seconds": 0.5044016930005455,
      "cold_end_to_end_seconds": 0.877243508999527,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.026803912998730084,
      "engine_upload_seconds": 0.013782055,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.013503689,
      "engine_annual_reduction_seconds": 0.007929163,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.013503689
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3728418159989815,
      "weather_seconds": 0.2217985339993902,
      "metric_reduction_seconds": 0.1755139680026332,
      "write_seconds": 0.022031240001524566,
      "total_seconds": 0.4196555349990376,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4196555349990376,
      "raw_export_seconds": 0.009244282999134157,
      "engine_upload_seconds": 0.013267012,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.007872514,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013938764997874387,
      "full": 0.023387899000226753
    }
  },
  "elapsed_seconds": 2.6469699689987465,
  "result_class": "passed"
}
```
