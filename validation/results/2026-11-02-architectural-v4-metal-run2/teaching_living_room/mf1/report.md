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
  "model_sha256": "954acf389f91cd00faeca08daae5a52a1670d83456b5a3f574b94574bf2841df",
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
    "maximum_samples": 65536,
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
        "bias_percent": 0.03018089522801461,
        "rms_normalized_error_percent": 0.6879697824456971,
        "absolute_error": {
          "p95": 6.665394175797645e-05,
          "p99": 0.0001699044369161129,
          "maximum": 0.0005950257182121277
        },
        "worst_index": [
          3,
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
        "bias_percent": 0.029389478464678404,
        "rms_normalized_error_percent": 0.6066728516421571,
        "absolute_error": {
          "p95": 6.590906996279921e-05,
          "p99": 0.0001538093201816082,
          "maximum": 0.00047879666090011597
        },
        "worst_index": [
          14,
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
                "nmbe_percent": -0.08970071032720679,
                "cvrmse_percent": 7.085083503673046,
                "rms_normalized_rmse_percent": 1.9197792283023276,
                "reference_energy": 6.350541776169848,
                "candidate_energy": 6.344845295086998,
                "relative_energy_error_percent": 0.08970071032720679,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.116631414741285e-05,
                  "p95": 0.0001316875917837009,
                  "p99": 0.00023633893579244614,
                  "maximum": 0.0006438156124204397
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0032982840202748775,
                  "candidate": 0.002654468407854438
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.3756995709976026,
                "cvrmse_percent": 37.4666940569833,
                "rms_normalized_rmse_percent": 2.7531061552243514,
                "reference_energy": 2.8888441945214254,
                "candidate_energy": 2.8779908192758192,
                "relative_energy_error_percent": 0.37569957099760265,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.054594279907234e-05,
                  "p95": 0.00025398385478183597,
                  "p99": 0.0006367249879986048,
                  "maximum": 0.0015061013400554657
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.033626969903707504,
                  "candidate": 0.03212086856365204
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.88420900609344,
            "full": 237.40458290558308
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.65345798432827,
            "full": 199.27458406891674
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.58391695469618,
            "full": 185.3987080976367
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.72629094030708,
            "full": 179.36908302363008
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
                "nmbe_percent": -0.005711922836765087,
                "cvrmse_percent": 6.52117962198171,
                "rms_normalized_rmse_percent": 1.7679746438211754,
                "reference_energy": 6.344799949923981,
                "candidate_energy": 6.344437539846695,
                "relative_energy_error_percent": 0.005711922836765088,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.166089070669853e-05,
                  "p95": 9.383367723785073e-05,
                  "p99": 0.00023324904032051563,
                  "maximum": 0.0004234299995005131
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.007530167466029525,
                  "candidate": 0.007106737466529012
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.015612841306163345,
                "cvrmse_percent": 13.236236308403141,
                "rms_normalized_rmse_percent": 1.3578009588246172,
                "reference_energy": 5.049704494831143,
                "candidate_energy": 5.0504928971803515,
                "relative_energy_error_percent": 0.015612841306163344,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.588997969927732e-07,
                  "p90": 5.760275671491403e-05,
                  "p95": 0.0001475134806241824,
                  "p99": 0.00034415535628795624,
                  "maximum": 0.0010776109993457794
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0696728266775608,
                  "candidate": 0.07075043767690659
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.2316660778597,
            "full": 2122.4234589608386
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.88633298687637,
            "full": 1904.3748339172453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.26479108445346,
            "full": 1976.7847919138148
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.77054094802588,
            "full": 1977.1622919943184
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
                "nmbe_percent": -0.004963194245919553,
                "cvrmse_percent": 6.873918348407187,
                "rms_normalized_rmse_percent": 1.8606829728474887,
                "reference_energy": 6.346911846612784,
                "candidate_energy": 6.346596837049219,
                "relative_energy_error_percent": 0.004963194245919553,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.0125290757278237e-05,
                  "p95": 8.790673455223426e-05,
                  "p99": 0.00026847259141504765,
                  "maximum": 0.0005596480332314968
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0073192245326936245,
                  "candidate": 0.007878872565925121
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.08695353851675001,
                "cvrmse_percent": 13.037917434499503,
                "rms_normalized_rmse_percent": 1.3371776373504205,
                "reference_energy": 5.049206827751032,
                "candidate_energy": 5.053597291754791,
                "relative_energy_error_percent": 0.08695353851675001,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.8332238716520806e-07,
                  "p90": 6.070408198866064e-05,
                  "p95": 0.00016585665289312585,
                  "p99": 0.0003925962373614311,
                  "maximum": 0.0006552259437739849
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.0005394644103944302,
                  "candidate": 0.001194690354168415
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.83087493944913,
            "full": 2134.206041926518
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.6099590761587,
            "full": 1815.0530840503052
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.13045801967382,
            "full": 1527.6818330166861
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.19791695661843,
            "full": 1661.5024589700624
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
                "nmbe_percent": 0.044395562002061656,
                "cvrmse_percent": 3.710062519406572,
                "rms_normalized_rmse_percent": 1.0056545198472047,
                "reference_energy": 6.343619027793466,
                "candidate_energy": 6.346435313112124,
                "relative_energy_error_percent": 0.044395562002061656,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.06727820821107e-05,
                  "p95": 5.242603147053152e-05,
                  "p99": 0.00015072920359671116,
                  "maximum": 0.00023277639411389828
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007404237519949675,
                  "candidate": 0.007637013914063573
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.07274636647297979,
                "cvrmse_percent": 7.873357494876847,
                "rms_normalized_rmse_percent": 0.808955862687104,
                "reference_energy": 5.058319005570365,
                "candidate_energy": 5.0546392622892,
                "relative_energy_error_percent": 0.0727463664729798,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.3729915454850925e-07,
                  "p90": 3.611699212342514e-05,
                  "p95": 8.403561078011967e-05,
                  "p99": 0.00021297484636306763,
                  "maximum": 0.0005176793783903122
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05174837447702885,
                  "candidate": 0.05226605385541916
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.73966703098267,
            "full": 2703.1699999934062
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.00499994680285,
            "full": 2709.4592089997604
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.08845791779459,
            "full": 2653.835208970122
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 171.33004206698388,
            "full": 2816.7073749937117
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 459.1235410189256,
      "worker_pool_size": 12,
      "invocation_count": 2
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_living_room/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1683.605125057511,
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
            "nmbe_percent": -1.2149852589850427,
            "cvrmse_percent": 21.896099095215966,
            "rms_normalized_rmse_percent": 2.249120286176973,
            "reference_energy": 5.056711574447666,
            "candidate_energy": 4.995273274228737,
            "relative_energy_error_percent": 1.2149852589850425,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.170569781550057e-06,
              "p90": 5.3569517331197894e-05,
              "p95": 8.102710271487009e-05,
              "p99": 0.0002209783997386694,
              "maximum": 0.0027588307857513428
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06681206077337265,
              "candidate": 0.06405322998762131,
              "position": [
                1.5,
                0.5625,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5101581390871627,
            "cvrmse_percent": 9.685526683881395,
            "rms_normalized_rmse_percent": 2.2431753398779395,
            "reference_energy": 11.401506261854314,
            "candidate_energy": 11.343340549680931,
            "relative_energy_error_percent": 0.5101581390871627,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.170569781550057e-06,
              "p90": 5.225688801147044e-05,
              "p95": 7.873091381043165e-05,
              "p99": 0.00019641639664769173,
              "maximum": 0.0027588307857513428
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06681206077337265,
              "candidate": 0.06405322998762131,
              "position": [
                1.5,
                0.5625,
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
            "nmbe_percent": 73.06741996352098,
            "cvrmse_percent": 388.1102782650783,
            "rms_normalized_rmse_percent": 28.548207307053453,
            "reference_energy": 2.8863163703957895,
            "candidate_energy": 4.995273274228737,
            "relative_energy_error_percent": 73.06741996352098,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3000000365082087e-07,
              "p90": 0.0004918770398944617,
              "p95": 0.0006186533253639934,
              "p99": 0.0010438174940645695,
              "maximum": 0.017969118431210518
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023953350260853767,
              "candidate": 0.041922468692064285,
              "position": [
                0.5,
                3.9375,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.881638826056257,
            "cvrmse_percent": 121.3704854171537,
            "rms_normalized_rmse_percent": 28.55267682511747,
            "reference_energy": 9.231111057802437,
            "candidate_energy": 11.343340549680931,
            "relative_energy_error_percent": 22.881638826056253,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3000000365082087e-07,
              "p90": 0.0004922956693917514,
              "p95": 0.0006263269926421341,
              "p99": 0.001041210489347577,
              "maximum": 0.017969118431210518
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023953350260853767,
              "candidate": 0.041922468692064285,
              "position": [
                0.5,
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
      "bias_percent": 0.1785690460058602,
      "rms_normalized_error_percent": 0.27065000193788924,
      "absolute_error": {
        "p95": 0.18456258338955522,
        "p99": 0.23991541627893684,
        "maximum": 0.25375362450128236
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.717261242907522,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.27065000193788924
    },
    "overcast": {
      "bias_percent": 0.12124443478196315,
      "rms_normalized_error_percent": 0.20132166857423317,
      "absolute_error": {
        "p95": 0.07183225154876713,
        "p99": 0.11786490917205802,
        "maximum": 0.12937307357788086
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.341723442077637,
      "reference_fraction_of_uniform": 0.6468589901924133,
      "rms_normalized_to_uniform_percent": 0.1398803641655643
    },
    "horizon": {
      "bias_percent": 1.4741793001832344,
      "rms_normalized_error_percent": 2.386970522099911,
      "absolute_error": {
        "p95": 0.09674745391397284,
        "p99": 0.1463150024897428,
        "maximum": 0.1587068896336854
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.097075375290565,
      "reference_fraction_of_uniform": 0.08841979492542296,
      "rms_normalized_to_uniform_percent": 0.1583219120899938
    },
    "north": {
      "bias_percent": -59.064231187219136,
      "rms_normalized_error_percent": 109.92848912509854,
      "absolute_error": {
        "p95": 0.00011024591932482514,
        "p99": 0.00016780701538891653,
        "maximum": 0.0001821972894049395
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.7097597921965644e-05,
      "reference_fraction_of_uniform": 1.1425264574427274e-06,
      "rms_normalized_to_uniform_percent": 0.00015473907748940027
    },
    "east": {
      "bias_percent": 0.009633827499279803,
      "rms_normalized_error_percent": 0.22861845471088155,
      "absolute_error": {
        "p95": 0.03159515261650085,
        "p99": 0.03183859229087829,
        "maximum": 0.031899452209472656
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.648923873901367,
      "reference_fraction_of_uniform": 0.1960143744945526,
      "rms_normalized_to_uniform_percent": 0.05035833653327514
    },
    "south": {
      "bias_percent": 0.24140187091074983,
      "rms_normalized_error_percent": 0.35934872735103557,
      "absolute_error": {
        "p95": 0.1760834693908692,
        "p99": 0.21751115798950188,
        "maximum": 0.22786808013916016
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.3541316986084,
      "reference_fraction_of_uniform": 0.6895455718040466,
      "rms_normalized_to_uniform_percent": 0.23548734735262955
    },
    "west": {
      "bias_percent": 0.2510708875992161,
      "rms_normalized_error_percent": 0.3639652167998876,
      "absolute_error": {
        "p95": 0.051223516464233405,
        "p99": 0.06035227775573729,
        "maximum": 0.06263446807861328
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.515354633331299,
      "reference_fraction_of_uniform": 0.19038264453411102,
      "rms_normalized_to_uniform_percent": 0.07676933651219107
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
          "nmbe_percent": 0.049736694145653335,
          "cvrmse_percent": 1.1213119138933905,
          "absolute_error_percentiles_lux": {
            "p50": 4.0828857421875,
            "p90": 36.17757568359376,
            "p95": 52.30888671875,
            "p99": 95.51491577148424
          },
          "maximum_absolute_error_lux": 255.0546875,
          "worst": {
            "sensor_index": 9,
            "position": [
              2.5,
              2.8125,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 15381.8798828125,
            "radiance_lux": 15126.8251953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10255479452055027,
            "maximum_error_percentage_points": 0.4961643835616485,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04974784818085638,
            "maximum_error_percentage_points": 0.20377511536140958,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03930821917808212,
            "maximum_error_percentage_points": 0.16013698630137085,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07163013698630287,
            "maximum_error_percentage_points": 0.22342465753424534,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.06663698630137038,
            "maximum_error_percentage_points": 0.219041095890411,
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
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004805222602726644,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_living_room_grid",
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
      "study_preparation_seconds": 0.02079075004439801,
      "weather_seconds": 0.10038520907983184,
      "metric_reduction_seconds": 0.08421579108107835,
      "write_seconds": 0.03560549998655915,
      "total_seconds": 0.22044491698034108,
      "cold_end_to_end_seconds": 0.2412356670247391,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012970958021469414,
      "engine_upload_seconds": 0.000344375,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024420708301477134,
      "engine_annual_reduction_seconds": 0.00024162500631064177,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024420708301477134
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.02079075004439801,
      "weather_seconds": 0.09913624997716397,
      "metric_reduction_seconds": 0.015615209005773067,
      "write_seconds": 0.03225795808248222,
      "total_seconds": 0.14717408397700638,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14717408397700638,
      "raw_export_seconds": 0.010613291058689356,
      "engine_upload_seconds": 7.0458e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00023987493477761745,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.05141462502069771,
      "full": 0.02515283296816051
    }
  },
  "elapsed_seconds": 32.95317900006194,
  "result_class": "passed"
}
```
