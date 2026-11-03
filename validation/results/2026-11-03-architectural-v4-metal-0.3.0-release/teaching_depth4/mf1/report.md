# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth4",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth4",
    "category": "teaching",
    "question": "How does daylight fall off in a 4 m deep room?",
    "interactions": [
      "multiple_bounces",
      "room",
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
    "sensors": 24,
    "floor_area": 24.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "aafc0dbd2bffa87fbfc782ce0c4dbf077e33165f345a4aa2a9643495142c15b3",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1264132388842763511,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 1264132388842763511,
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
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "9dda0a8a6912aba59e1f74a9a0148be476b7acec392a211c80de6376d99e0399",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "2a3b410550d7942d297128a3106efcde5cf63c28104e15605e9a8b11f7687b28",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00029224716126918793,
          "p95": 1.6129284631460905e-05,
          "p99": 0.00015342188999056816
        },
        "bias_percent": -0.06804422780189273,
        "identifier": "teaching_depth4_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9156604833783333,
        "worst_index": [
          11,
          121,
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
          "maximum": 0.000815078616142273,
          "p95": 8.860975503921509e-05,
          "p99": 0.00019295141100883484
        },
        "bias_percent": 0.06376193165581083,
        "identifier": "teaching_depth4_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9737553951978584,
        "worst_index": [
          10,
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
          "maximum": 0.0005986467003822327,
          "p95": 7.218075916171074e-05,
          "p99": 0.00016179820522665977
        },
        "bias_percent": -0.005293708461179399,
        "identifier": "teaching_depth4_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7922896406250503,
        "worst_index": [
          10,
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
            "identifier": "teaching_depth4_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005576339899562299,
                  "p50": 0.0,
                  "p90": 4.439591430127621e-05,
                  "p95": 0.00013124250108376145,
                  "p99": 0.00024760980159044266
                },
                "candidate_energy": 8.480913408679044,
                "cvrmse_percent": 6.516618322005505,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0336490403894114,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.478060622635894,
                "relative_energy_error_percent": 0.0336490403894114,
                "rms_normalized_rmse_percent": 1.8794820509617336,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0027878149412572384,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0022301809513010085,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008955961093306541,
                  "p50": 0.0,
                  "p90": 9.050499647855759e-05,
                  "p95": 0.00023057602811604738,
                  "p99": 0.0005072739440947771
                },
                "candidate_energy": 2.7539225703777106,
                "cvrmse_percent": 38.84137171786736,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.40548153888925037,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.7651346810347306,
                "relative_energy_error_percent": 0.4054815388892504,
                "rms_normalized_rmse_percent": 2.6175086853958995,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02815374918282032,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.029049345292150974,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.0245829867199,
            "full": 181.5229159547016
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.93041709903628,
            "full": 179.4199589639902
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.48945800028741,
            "full": 181.0930829960853
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.0256669037044,
            "full": 187.6304999459535
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
            "identifier": "teaching_depth4_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005096679087728262,
                  "p50": 0.0,
                  "p90": 3.1348783522844315e-05,
                  "p95": 9.396695531904697e-05,
                  "p99": 0.00021462468430399895
                },
                "candidate_energy": 8.481022643357392,
                "cvrmse_percent": 5.9929497208976805,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.03803453128389031,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.484249587921113,
                "relative_energy_error_percent": 0.03803453128389031,
                "rms_normalized_rmse_percent": 1.726976248652689,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006954621057957411,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.007464288966730237,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007729507051408291,
                  "p50": 3.3622492878748744e-07,
                  "p90": 5.9632351621985435e-05,
                  "p95": 0.00015740003436803818,
                  "p99": 0.00039423489943146706
                },
                "candidate_energy": 4.924250061147379,
                "cvrmse_percent": 15.6123241824575,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2760961771199553,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.937883368358058,
                "relative_energy_error_percent": 0.2760961771199553,
                "rms_normalized_rmse_percent": 1.515752020784214,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0007841801270842552,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 1.1229421943426132e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.24245804082602,
            "full": 1537.0671669952571
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.92849997337908,
            "full": 1534.8145420430228
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.5186250032857,
            "full": 1550.1222499879077
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.32033301331103,
            "full": 1518.2257499545813
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
            "identifier": "teaching_depth4_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042092264629900455,
                  "p50": 0.0,
                  "p90": 2.5344081223011017e-05,
                  "p95": 9.241234511137009e-05,
                  "p99": 0.00024333992041647434
                },
                "candidate_energy": 8.484935109972866,
                "cvrmse_percent": 5.531522680971113,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.061870755163987934,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.479688662561784,
                "relative_energy_error_percent": 0.061870755163987934,
                "rms_normalized_rmse_percent": 1.5954558171923467,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005076423520222306,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.004655500873923302,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007104896940290928,
                  "p50": 3.898711611327599e-07,
                  "p90": 6.664381362497807e-05,
                  "p95": 0.0001697721309028566,
                  "p99": 0.0003400215646252036
                },
                "candidate_energy": 4.934838683204951,
                "cvrmse_percent": 15.295318165286584,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2064697701409244,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.945048713917934,
                "relative_energy_error_percent": 0.2064697701409244,
                "rms_normalized_rmse_percent": 1.4861075607436558,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00037711835466325283,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0010876080486923456,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.97991698607802,
            "full": 1613.7990419520065
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.5397909861058,
            "full": 1603.965291986242
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.79587498214096,
            "full": 1646.487999940291
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.35820806585252,
            "full": 1602.0046659978107
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
            "identifier": "teaching_depth4_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021744007244706154,
                  "p50": 0.0,
                  "p90": 1.8646474927663803e-05,
                  "p95": 5.674505518982187e-05,
                  "p99": 0.0001402534544467926
                },
                "candidate_energy": 8.481335028944613,
                "cvrmse_percent": 3.2288806149473306,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.03422093528398098,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.48423841468184,
                "relative_energy_error_percent": 0.034220935283980985,
                "rms_normalized_rmse_percent": 0.9312344083274907,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012690415140241385,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.012472975067794323,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005442742258310318,
                  "p50": 2.576984883262412e-07,
                  "p90": 4.099542275071144e-05,
                  "p95": 8.52739904075861e-05,
                  "p99": 0.0001965800765901804
                },
                "candidate_energy": 4.9358183580632975,
                "cvrmse_percent": 8.993811191674167,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1189873614395932,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.941698354545675,
                "relative_energy_error_percent": 0.1189873614395932,
                "rms_normalized_rmse_percent": 0.8739503382600148,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04276399500668049,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.04330826923251152,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.18875005934387,
            "full": 2807.1646250318736
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.82279195450246,
            "full": 2786.6540000541136
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.1205000113696,
            "full": 2836.9941669516265
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.8417910989374,
            "full": 2799.729833030142
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/teaching_depth4/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 485.49304192420095,
      "invocation_count": 2,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth4/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1602.974042063579,
      "invocation_count": 2,
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
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
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
            "nmbe_percent": 0.015862148997386513,
            "cvrmse_percent": 12.161016468199263,
            "rms_normalized_rmse_percent": 1.1806535507372211,
            "reference_energy": 4.935241362245048,
            "candidate_energy": 4.936024197583308,
            "relative_energy_error_percent": 0.015862148997386513,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1061616191909707e-06,
              "p90": 5.408903234638274e-05,
              "p95": 7.782038301229477e-05,
              "p99": 0.00018177239689975977,
              "maximum": 0.0012797266244888306
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05105552449822426,
              "candidate": 0.04977579787373543,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.04033914422171541,
            "cvrmse_percent": 4.493677984212536,
            "rms_normalized_rmse_percent": 1.1864478846468904,
            "reference_energy": 13.42154508796511,
            "candidate_energy": 13.416130951535294,
            "relative_energy_error_percent": 0.04033914422171542,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1061616191909707e-06,
              "p90": 5.222283652983606e-05,
              "p95": 7.728999480605125e-05,
              "p99": 0.00019288808107376099,
              "maximum": 0.0012797266244888306
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05105552449822426,
              "candidate": 0.04977579787373543,
              "position": [
                1.5,
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
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
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
            "nmbe_percent": 79.31495909794366,
            "cvrmse_percent": 451.1167354266926,
            "rms_normalized_rmse_percent": 30.28087959310353,
            "reference_energy": 2.752711888854293,
            "candidate_energy": 4.936024197583308,
            "relative_energy_error_percent": 79.31495909794366,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0003938744484912604,
              "p95": 0.0005240199971012771,
              "p99": 0.0008864188566803932,
              "maximum": 0.015985026955604553
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032740384340286255,
              "candidate": 0.04872541129589081,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.371050024503322,
            "cvrmse_percent": 110.48270688257423,
            "rms_normalized_rmse_percent": 30.278988966319957,
            "reference_energy": 11.239015614574356,
            "candidate_energy": 13.416130951535294,
            "relative_energy_error_percent": 19.371050024503322,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0003925299970433116,
              "p95": 0.0005172528326511383,
              "p99": 0.0008920649997889996,
              "maximum": 0.015985026955604553
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032740384340286255,
              "candidate": 0.04872541129589081,
              "position": [
                3.5,
                3.5,
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
      "bias_percent": 0.20195936869818976,
      "rms_normalized_error_percent": 0.3019700603255484,
      "absolute_error": {
        "p95": 0.21341803370110615,
        "p99": 0.26819867277556325,
        "maximum": 0.28074899902275874
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 25.177703733376607,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3019700603255484
    },
    "overcast": {
      "bias_percent": 0.15130077059979863,
      "rms_normalized_error_percent": 0.2377892470543673,
      "absolute_error": {
        "p95": 0.09042322635650633,
        "p99": 0.12432651042938231,
        "maximum": 0.1342482566833496
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.28083610534668,
      "reference_fraction_of_uniform": 0.6466370224952698,
      "rms_normalized_to_uniform_percent": 0.16535400597525984
    },
    "horizon": {
      "bias_percent": 1.3288545021013363,
      "rms_normalized_error_percent": 2.859834474613113,
      "absolute_error": {
        "p95": 0.1266469515726734,
        "p99": 0.19211840460976978,
        "maximum": 0.20999015731852522
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.135801268300524,
      "reference_fraction_of_uniform": 0.08482907301308885,
      "rms_normalized_to_uniform_percent": 0.18104958296931845
    },
    "north": {
      "bias_percent": -71.03180545687134,
      "rms_normalized_error_percent": 102.02023137704002,
      "absolute_error": {
        "p95": 0.00024797850346658357,
        "p99": 0.0002890463583753444,
        "maximum": 0.00029638971318490803
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.498446989804506e-05,
      "reference_fraction_of_uniform": 2.1838557131559355e-06,
      "rms_normalized_to_uniform_percent": 0.0002815843096407845
    },
    "east": {
      "bias_percent": 0.1475687234986581,
      "rms_normalized_error_percent": 0.22353448627030578,
      "absolute_error": {
        "p95": 0.03818105459213256,
        "p99": 0.046351644992828366,
        "maximum": 0.048603057861328125
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.15849494934082,
      "reference_fraction_of_uniform": 0.20488345623016357,
      "rms_normalized_to_uniform_percent": 0.05086863873407733
    },
    "south": {
      "bias_percent": 0.25319757959122224,
      "rms_normalized_error_percent": 0.3969315071391428,
      "absolute_error": {
        "p95": 0.2146674633026121,
        "p99": 0.24173783302307128,
        "maximum": 0.24567222595214844
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.151268005371094,
      "reference_fraction_of_uniform": 0.681208610534668,
      "rms_normalized_to_uniform_percent": 0.25535565741912797
    },
    "west": {
      "bias_percent": 0.09649145191749095,
      "rms_normalized_error_percent": 0.3688534704815536,
      "absolute_error": {
        "p95": 0.046684730052947994,
        "p99": 0.0593245768547058,
        "maximum": 0.06299877166748047
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.997059345245361,
      "reference_fraction_of_uniform": 0.19847160577774048,
      "rms_normalized_to_uniform_percent": 0.08044702015358295
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
        "identifier": "teaching_depth4_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.10177197613375823,
          "cvrmse_percent": 1.1997228186339781,
          "absolute_error_percentiles_lux": {
            "p50": 3.5103683471679688,
            "p90": 34.31899414062501,
            "p95": 52.43815307617184,
            "p99": 110.16739257812486
          },
          "maximum_absolute_error_lux": 502.6416015625,
          "worst": {
            "sensor_index": 8,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 14740.4375,
            "radiance_lux": 14237.7958984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1099486301369863,
            "maximum_error_percentage_points": 0.40958904109588445,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03963178006706869,
            "maximum_error_percentage_points": 0.17896544373752477,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.041906392694063856,
            "maximum_error_percentage_points": 0.19041095890410986,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09698630136986441,
            "maximum_error_percentage_points": 0.4641095890411009,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.09762557077625574,
            "maximum_error_percentage_points": 0.4667123287671231,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
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
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004902343750003979,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth4_grid",
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
      "study_preparation_seconds": 0.005958208930678666,
      "weather_seconds": 0.09156633401289582,
      "metric_reduction_seconds": 0.034835959086194634,
      "write_seconds": 0.04145108396187425,
      "total_seconds": 0.16802341700531542,
      "cold_end_to_end_seconds": 0.1739816259359941,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013070750050246716,
      "engine_upload_seconds": 0.000287959,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.016888541635125875,
      "engine_annual_reduction_seconds": 0.0002469166647642851,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.016888541635125875
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005958208930678666,
      "weather_seconds": 0.09064304095227271,
      "metric_reduction_seconds": 0.011090957908891141,
      "write_seconds": 0.02594191604293883,
      "total_seconds": 0.12783337500877678,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.12783337500877678,
      "raw_export_seconds": 0.00899141700938344,
      "engine_upload_seconds": 5.3709e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00026300002355128527,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011167458025738597,
      "full": 0.022251458023674786
    }
  },
  "elapsed_seconds": 0.6210790419718251,
  "result_class": "passed"
}
```
