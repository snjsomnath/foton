# Foton report

Status: **passed**

```json
{
  "scene": "teaching_living_room",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_living_room",
    "category": "teaching",
    "question": "How is a 5 x 4.5 m living room with a tall window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
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
    "sensors": 20,
    "floor_area": 22.5,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "807cc848f08ce1d066a7b4863577da8b97fe61cfdac5d466fa4a4a17048e9173",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 5011208731090707716,
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
      "scene_fingerprint": 5011208731090707716,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_living_room_grid",
        "bias_percent": -0.07151979699695074,
        "rms_normalized_error_percent": 1.3445794157223598,
        "absolute_error": {
          "p95": 9.847903857007378e-06,
          "p99": 0.00012934557162225246,
          "maximum": 0.0007540034130215645
        },
        "worst_index": [
          11,
          134,
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
        "identifier": "teaching_living_room_grid",
        "bias_percent": 0.03489168821906306,
        "rms_normalized_error_percent": 0.701233516362487,
        "absolute_error": {
          "p95": 7.864539511501782e-05,
          "p99": 0.0001706564798951149,
          "maximum": 0.0005657747387886047
        },
        "worst_index": [
          11,
          0,
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
        "identifier": "teaching_living_room_grid",
        "bias_percent": 0.018110020315317006,
        "rms_normalized_error_percent": 0.5751373258783041,
        "absolute_error": {
          "p95": 6.349444156512612e-05,
          "p99": 0.00014479528181254864,
          "maximum": 0.0004833489656448364
        },
        "worst_index": [
          11,
          0,
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
            "identifier": "teaching_living_room_grid",
            "start_sensor_index": 0,
            "sensor_count": 20,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07702931577296722,
                "cvrmse_percent": 7.131522391821661,
                "rms_normalized_rmse_percent": 1.9301848489995816,
                "reference_energy": 6.34363217511418,
                "candidate_energy": 6.348518631573825,
                "relative_energy_error_percent": 0.07702931577296722,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.730659373104593e-05,
                  "p95": 0.0001232214272022247,
                  "p99": 0.0002667950466275215,
                  "maximum": 0.000416286988183856
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.007045758189633489,
                  "candidate": 0.006629471201449633
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1587804700378762,
                "cvrmse_percent": 27.266700105412838,
                "rms_normalized_rmse_percent": 2.007885927961434,
                "reference_energy": 2.8870143593586306,
                "candidate_energy": 2.88243034438878,
                "relative_energy_error_percent": 0.1587804700378762,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.7449997984804454e-05,
                  "p95": 0.00018876906688092222,
                  "p99": 0.000466733006760478,
                  "maximum": 0.0009411759674549103
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05316632613539696,
                  "candidate": 0.05222515016794205
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 114.05766604002565,
            "full": 184.6800419734791
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 120.1049160445109,
            "full": 183.78366599790752
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 111.00325000006706,
            "full": 179.0675000520423
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 112.76299995370209,
            "full": 180.2348339697346
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
            "identifier": "teaching_living_room_grid",
            "start_sensor_index": 0,
            "sensor_count": 20,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05320986974279147,
                "cvrmse_percent": 5.536053234515558,
                "rms_normalized_rmse_percent": 1.4999736693815289,
                "reference_energy": 6.342582914254308,
                "candidate_energy": 6.345957794361311,
                "relative_energy_error_percent": 0.05320986974279147,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.161739394068718e-05,
                  "p95": 9.033444803208113e-05,
                  "p99": 0.00021008646581321955,
                  "maximum": 0.0003415551036596298
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.005960526876151562,
                  "candidate": 0.0063020819798111916
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.07501101280050644,
                "cvrmse_percent": 11.889333702693037,
                "rms_normalized_rmse_percent": 1.2193389108278372,
                "reference_energy": 5.048536599657911,
                "candidate_energy": 5.052323558092919,
                "relative_energy_error_percent": 0.07501101280050643,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.079685768625495e-07,
                  "p90": 5.6704488815739775e-05,
                  "p95": 0.00014319766778498716,
                  "p99": 0.0003596888855099678,
                  "maximum": 0.0005796328186988831
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06717822328209877,
                  "candidate": 0.06659859046339989
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.47475000005215,
            "full": 1435.5800839839503
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.44841701816767,
            "full": 1432.8201250173151
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.65624998509884,
            "full": 1422.2793340450153
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.0594999017194,
            "full": 1473.778416053392
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
            "identifier": "teaching_living_room_grid",
            "start_sensor_index": 0,
            "sensor_count": 20,
            "stages": {
              "direct": {
                "nmbe_percent": -0.12625225415683267,
                "cvrmse_percent": 5.535262152420793,
                "rms_normalized_rmse_percent": 1.500240636209969,
                "reference_energy": 6.352455407522939,
                "candidate_energy": 6.344435289376634,
                "relative_energy_error_percent": 0.12625225415683267,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.0457967184484107e-05,
                  "p95": 8.460035605821756e-05,
                  "p99": 0.0002029405441135168,
                  "maximum": 0.0003780997358262539
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 70,
                  "rgb_channel": 0,
                  "reference": 0.01270577497780323,
                  "candidate": 0.012327675241976976
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1652936581340468,
                "cvrmse_percent": 12.399942990391413,
                "rms_normalized_rmse_percent": 1.2715767911364653,
                "reference_energy": 5.046060436630768,
                "candidate_energy": 5.05440125451813,
                "relative_energy_error_percent": 0.1652936581340468,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.318532091929228e-07,
                  "p90": 5.959825357422239e-05,
                  "p95": 0.0001511968672275524,
                  "p99": 0.0003367899917066097,
                  "maximum": 0.000839725136756897
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06726256012916565,
                  "candidate": 0.06642283499240875
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 130.27787499595433,
            "full": 1514.5066659897566
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.28208297491074,
            "full": 1515.9455829998478
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 128.14974994398654,
            "full": 1481.6081669414416
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.98574998043478,
            "full": 1517.4633749993518
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
            "identifier": "teaching_living_room_grid",
            "start_sensor_index": 0,
            "sensor_count": 20,
            "stages": {
              "direct": {
                "nmbe_percent": -0.01036444406027963,
                "cvrmse_percent": 2.6230846979961897,
                "rms_normalized_rmse_percent": 0.710938773518754,
                "reference_energy": 6.347226894999949,
                "candidate_energy": 6.346569040219038,
                "relative_energy_error_percent": 0.010364444060279629,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.187217801809318e-06,
                  "p95": 4.514027386903756e-05,
                  "p99": 9.229150600731373e-05,
                  "maximum": 0.00021793972700834274
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 118,
                  "rgb_channel": 0,
                  "reference": 0.018044600263237953,
                  "candidate": 0.018262539990246296
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.19948365324614045,
                "cvrmse_percent": 6.35853425110736,
                "rms_normalized_rmse_percent": 0.652870757602492,
                "reference_energy": 5.058888447241024,
                "candidate_energy": 5.048796791752821,
                "relative_energy_error_percent": 0.19948365324614045,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.416931721427318e-07,
                  "p90": 3.566884261090311e-05,
                  "p95": 7.742397137917544e-05,
                  "p99": 0.0001696235267445445,
                  "maximum": 0.000420987606048584
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07010498270392418,
                  "candidate": 0.07052597030997276
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.4004170531407,
            "full": 2655.472957994789
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.30804192554206,
            "full": 2611.212208052166
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 181.36354093439877,
            "full": 2580.455124960281
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 173.0166660854593,
            "full": 2687.2819589916617
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 449.2725000018254,
      "worker_pool_size": 12,
      "invocation_count": 2
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_living_room/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1329.9879579572007,
      "worker_pool_size": 12,
      "invocation_count": 2
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      20,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05157910077126447,
            "cvrmse_percent": 1.9383485945756473,
            "rms_normalized_rmse_percent": 0.5252373475133134,
            "reference_energy": 6.344794687406647,
            "candidate_energy": 6.348067275452195,
            "relative_energy_error_percent": 0.051579100771264465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7960555851459622e-07,
              "p95": 8.088909089565258e-06,
              "p99": 7.439218461513519e-05,
              "maximum": 0.0001857280731201172
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.010556221939623356,
              "candidate": 0.010741950012743473,
              "position": [
                0.5,
                1.6875,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1022599274635656,
            "cvrmse_percent": 25.113319705173357,
            "rms_normalized_rmse_percent": 2.5786373302639554,
            "reference_energy": 5.055945845005972,
            "candidate_energy": 5.000216180002212,
            "relative_energy_error_percent": 1.1022599274635654,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5531072676822077e-06,
              "p90": 0.00010494322341401135,
              "p95": 0.00015733018226455825,
              "p99": 0.00033747858833521605,
              "maximum": 0.002781979739665985
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07031548023223877,
              "candidate": 0.06753350049257278,
              "position": [
                1.5,
                1.6875,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4601199089574554,
            "cvrmse_percent": 11.100934866901117,
            "rms_normalized_rmse_percent": 2.5702557702369653,
            "reference_energy": 11.40074053241262,
            "candidate_energy": 11.348283455454407,
            "relative_energy_error_percent": 0.46011990895745547,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5376460851257434e-06,
              "p90": 0.00010428592213429531,
              "p95": 0.00014922096524969542,
              "p99": 0.00035629933699965477,
              "maximum": 0.002781979739665985
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07031548023223877,
              "candidate": 0.06753350049257278,
              "position": [
                1.5,
                1.6875,
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
      20,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05157910077126447,
            "cvrmse_percent": 1.9383485945756473,
            "rms_normalized_rmse_percent": 0.5252373475133134,
            "reference_energy": 6.344794687406647,
            "candidate_energy": 6.348067275452195,
            "relative_energy_error_percent": 0.051579100771264465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7960555851459622e-07,
              "p95": 8.088909089565258e-06,
              "p99": 7.439218461513519e-05,
              "maximum": 0.0001857280731201172
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.010556221939623356,
              "candidate": 0.010741950012743473,
              "position": [
                0.5,
                1.6875,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 73.25747785819318,
            "cvrmse_percent": 391.1538415885387,
            "rms_normalized_rmse_percent": 28.800568413986355,
            "reference_energy": 2.8860030988646628,
            "candidate_energy": 5.000216180002212,
            "relative_energy_error_percent": 73.25747785819318,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0004919733744827684,
              "p95": 0.0006509076505608375,
              "p99": 0.0011700759641826153,
              "maximum": 0.01784662716090679
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030482230708003044,
              "candidate": 0.048328857868909836,
              "position": [
                3.5,
                3.9375,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.93935711962372,
            "cvrmse_percent": 122.30428597388187,
            "rms_normalized_rmse_percent": 28.802990419176627,
            "reference_energy": 9.23079778627131,
            "candidate_energy": 11.348283455454407,
            "relative_energy_error_percent": 22.939357119623722,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0004947902169078588,
              "p95": 0.0006543542625877306,
              "p99": 0.0011287899687886238,
              "maximum": 0.01784662716090679
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030482230708003044,
              "candidate": 0.048328857868909836,
              "position": [
                3.5,
                3.9375,
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
      "bias_percent": 0.1840579586136704,
      "rms_normalized_error_percent": 0.5022256126333353,
      "absolute_error": {
        "p95": 0.33230046264180313,
        "p99": 0.3395209248152467,
        "maximum": 0.3413260403586076
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 23.710990491744287,
      "rms_normalized_to_uniform_percent": 0.5022256126333353
    },
    "overcast": {
      "bias_percent": 0.104696143463928,
      "rms_normalized_error_percent": 0.3841778216428395,
      "absolute_error": {
        "p95": 0.161592435836792,
        "p99": 0.18172644615173336,
        "maximum": 0.18675994873046875
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 15.337438583374023,
      "rms_normalized_to_uniform_percent": 0.26690600510497736
    },
    "horizon": {
      "bias_percent": 2.1595404422758016,
      "rms_normalized_error_percent": 3.9025607980745494,
      "absolute_error": {
        "p95": 0.1653513076231028,
        "p99": 0.19760282969757859,
        "maximum": 0.20566571021619762
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.09539374485716,
      "rms_normalized_to_uniform_percent": 0.2586370280033278
    },
    "north": {
      "bias_percent": 18.161232997401243,
      "rms_normalized_error_percent": 467.70179407780705,
      "absolute_error": {
        "p95": 5.827762624903725e-05,
        "p99": 0.0003451602314635233,
        "maximum": 0.0004168808827671455
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.906479701574426e-05,
      "rms_normalized_to_uniform_percent": 0.0002928026808447875
    },
    "east": {
      "bias_percent": -0.18096492037031248,
      "rms_normalized_error_percent": 0.7099116036227722,
      "absolute_error": {
        "p95": 0.09192910194396973,
        "p99": 0.10163624763488768,
        "maximum": 0.10406303405761719
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.64907693862915,
      "rms_normalized_to_uniform_percent": 0.15638921328973987
    },
    "south": {
      "bias_percent": 0.289325631727768,
      "rms_normalized_error_percent": 0.6138593971907346,
      "absolute_error": {
        "p95": 0.3128583669662476,
        "p99": 0.31476130962371823,
        "maximum": 0.31523704528808594
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 16.349491119384766,
      "rms_normalized_to_uniform_percent": 0.40229943474053714
    },
    "west": {
      "bias_percent": 0.39477813678183116,
      "rms_normalized_error_percent": 0.7098263282577548,
      "absolute_error": {
        "p95": 0.089347517490387,
        "p99": 0.12387536287307734,
        "maximum": 0.13250732421875
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.5129547119140625,
      "rms_normalized_to_uniform_percent": 0.1497020047509752
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
        "identifier": "teaching_living_room_grid",
        "sensor_count": 20,
        "illuminance": {
          "nmbe_percent": 0.0221667390744666,
          "cvrmse_percent": 2.0819677082750667,
          "absolute_error_percentiles_lux": {
            "p50": 7.553741455078125,
            "p90": 66.15047607421877,
            "p95": 96.91506347656252,
            "p99": 171.62337890624983
          },
          "maximum_absolute_error_lux": 724.5869140625,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              3.9375,
              0.75
            ],
            "hour_of_year": 1093.5,
            "foton_lux": 11280.34375,
            "radiance_lux": 10555.7568359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.19277397260274043,
            "maximum_error_percentage_points": 0.764109589041098,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08861699722946384,
            "maximum_error_percentage_points": 0.31234242426205583,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09030136986301347,
            "maximum_error_percentage_points": 0.36013698630137014,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10785616438356342,
            "maximum_error_percentage_points": 0.2760273972602718,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.12973972602739714,
            "maximum_error_percentage_points": 0.38383561643835584,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 5.0,
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
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004585027825356747,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
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
      "study_preparation_seconds": 0.007027833955362439,
      "weather_seconds": 0.1087002499261871,
      "metric_reduction_seconds": 0.029536457965150476,
      "write_seconds": 0.03457825002260506,
      "total_seconds": 0.1729547498980537,
      "cold_end_to_end_seconds": 0.17998258385341614,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.015280374907888472,
      "engine_upload_seconds": 0.000277,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.012329458259046078,
      "engine_annual_reduction_seconds": 0.000282999943010509,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.012329458259046078
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007027833955362439,
      "weather_seconds": 0.10939758399035782,
      "metric_reduction_seconds": 0.011876291944645345,
      "write_seconds": 0.03592674992978573,
      "total_seconds": 0.15736333397217095,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15736333397217095,
      "raw_export_seconds": 0.009211499942466617,
      "engine_upload_seconds": 6.4583e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00037062494084239006,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012654833029955626,
      "full": 0.008585834060795605
    }
  },
  "elapsed_seconds": 29.13546645909082,
  "result_class": "passed"
}
```
