# Foton report

Status: **passed**

```json
{
  "scene": "teaching_classroom",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_classroom",
    "category": "teaching",
    "question": "How is a 9 x 7 m classroom with three windows lit?",
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
    "apertures": 3,
    "shades": 0,
    "sensors": 63,
    "floor_area": 63.0,
    "aperture_area": 11.520000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "e9c6f089399060035c5b3f1508c1e1ff0012327d68ccebe8fb3bc4eaf110954c",
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
      "scene_fingerprint": 117564074192331588,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 117564074192331588,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_classroom_grid",
        "bias_percent": 0.024707531623630725,
        "rms_normalized_error_percent": 0.7650893574334957,
        "absolute_error": {
          "p95": 2.44686380028723e-06,
          "p99": 2.4068605853244662e-05,
          "maximum": 0.00013817357830703259
        },
        "worst_index": [
          5,
          356,
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
        "identifier": "teaching_classroom_grid",
        "bias_percent": 0.02642022177920198,
        "rms_normalized_error_percent": 1.157144127648471,
        "absolute_error": {
          "p95": 5.9719453565776255e-05,
          "p99": 0.00013091880828142166,
          "maximum": 0.0006935000419616699
        },
        "worst_index": [
          5,
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
        "identifier": "teaching_classroom_grid",
        "bias_percent": -0.002701354745985402,
        "rms_normalized_error_percent": 0.9593017065172118,
        "absolute_error": {
          "p95": 4.7881435602903274e-05,
          "p99": 0.00010468187974765897,
          "maximum": 0.0006790310144424438
        },
        "worst_index": [
          1,
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0843821667802542,
                "cvrmse_percent": 24.64945708798117,
                "rms_normalized_rmse_percent": 6.980683473408593,
                "reference_energy": 23.054879772724234,
                "candidate_energy": 23.07433397982504,
                "relative_energy_error_percent": 0.08438216678025419,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.461151547729969e-05,
                  "p95": 0.0001236184849403789,
                  "p99": 0.0002700840122997761,
                  "maximum": 0.0005509735783562064
                },
                "worst": {
                  "global_sensor_index": 54,
                  "local_sensor_index": 54,
                  "sky_patch_index": 267,
                  "rgb_channel": 0,
                  "reference": 0.0030318754725158215,
                  "candidate": 0.003582849050872028
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.0974193913484812,
                "cvrmse_percent": 104.3337248639975,
                "rms_normalized_rmse_percent": 4.4582692932271755,
                "reference_energy": 8.67657477668358,
                "candidate_energy": 8.66812211034624,
                "relative_energy_error_percent": 0.09741939134848121,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.38386991340667e-05,
                  "p95": 0.000182051181764109,
                  "p99": 0.0004081289480382111,
                  "maximum": 0.0015087099745869637
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.019626825116574764,
                  "candidate": 0.021135535091161728
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.47833302337676,
            "full": 364.90875005256385
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.3121250225231,
            "full": 353.63024997059256
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.0629999851808,
            "full": 352.8715840075165
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.13799995277077,
            "full": 359.0895829256624
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03309491369696175,
                "cvrmse_percent": 16.450452252972063,
                "rms_normalized_rmse_percent": 4.665487328177571,
                "reference_energy": 23.061903402262942,
                "candidate_energy": 23.069535719290798,
                "relative_energy_error_percent": 0.03309491369696175,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3472850443795323e-05,
                  "p95": 8.075754158198833e-05,
                  "p99": 0.00017507351003587246,
                  "maximum": 0.00047882157377898693
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 60,
                  "sky_patch_index": 215,
                  "rgb_channel": 0,
                  "reference": 0.0019840284949168563,
                  "candidate": 0.0024628500686958432
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.03273253976488846,
                "cvrmse_percent": 38.066735857825854,
                "rms_normalized_rmse_percent": 2.1945743442442613,
                "reference_energy": 15.383472096601384,
                "candidate_energy": 15.388507497722625,
                "relative_energy_error_percent": 0.032732539764888456,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.4239252019906417e-05,
                  "p95": 0.00011759657354559729,
                  "p99": 0.0002525264862924814,
                  "maximum": 0.00156327523291111
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06143472157418728,
                  "candidate": 0.06299799680709839
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.76979199703783,
            "full": 4216.045249952003
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.65587506443262,
            "full": 4238.471708027646
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.62658302113414,
            "full": 4256.505458964966
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.47066601831466,
            "full": 4211.842958000489
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0076486820918354875,
                "cvrmse_percent": 16.703983915070527,
                "rms_normalized_rmse_percent": 4.738549773323858,
                "reference_energy": 23.06404779088234,
                "candidate_energy": 23.062283695189308,
                "relative_energy_error_percent": 0.0076486820918354875,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.348588895983994e-05,
                  "p95": 8.364070381503515e-05,
                  "p99": 0.0001754795084707439,
                  "maximum": 0.00044526148121804
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "sky_patch_index": 261,
                  "rgb_channel": 0,
                  "reference": 0.0026911834720522165,
                  "candidate": 0.0022459219908341765
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0760959291208067,
                "cvrmse_percent": 38.87294308226272,
                "rms_normalized_rmse_percent": 2.240267845041183,
                "reference_energy": 15.392846131899873,
                "candidate_energy": 15.404559461182078,
                "relative_energy_error_percent": 0.0760959291208067,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.5446649892255664e-05,
                  "p95": 0.00011992386071142361,
                  "p99": 0.0002583501045592129,
                  "maximum": 0.0015487372875213623
                },
                "worst": {
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07121093943715096,
                  "candidate": 0.06966220214962959
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 222.51091606449336,
            "full": 4485.193083994091
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.38420906290412,
            "full": 4429.161582957022
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 223.01983402576298,
            "full": 4397.855709074065
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.19149998109788,
            "full": 4536.450749961659
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": 0.017149209530101888,
                "cvrmse_percent": 9.466641992751246,
                "rms_normalized_rmse_percent": 2.6855796930785734,
                "reference_energy": 23.053204130144195,
                "candidate_energy": 23.057157572423876,
                "relative_energy_error_percent": 0.017149209530101888,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6571328160353005e-05,
                  "p95": 4.600763058988374e-05,
                  "p99": 0.0001009684638120234,
                  "maximum": 0.00022026582155376673
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 359,
                  "rgb_channel": 0,
                  "reference": 0.004015839891508222,
                  "candidate": 0.003795574069954455
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.03352649906305678,
                "cvrmse_percent": 22.110125311129263,
                "rms_normalized_rmse_percent": 1.2754801435889138,
                "reference_energy": 15.408231617018032,
                "candidate_energy": 15.403065776389319,
                "relative_energy_error_percent": 0.03352649906305678,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 2.651102840900421e-05,
                  "p95": 6.876024126540856e-05,
                  "p99": 0.00014603754971176386,
                  "maximum": 0.0006183590739965439
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0585643146187067,
                  "candidate": 0.05794595554471016
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 360.48537492752075,
            "full": 7941.087750019506
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 362.9465000703931,
            "full": 7933.918624999933
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 359.1499589383602,
            "full": 7800.055042025633
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 355.29483400750905,
            "full": 7916.589875007048
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 8601.140249986202,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_classroom/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 33752.365624997765,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0012228542050090397,
            "cvrmse_percent": 1.5293000894727466,
            "rms_normalized_rmse_percent": 0.4340807814641064,
            "reference_energy": 23.06225351042906,
            "candidate_energy": 23.06253552816588,
            "relative_energy_error_percent": 0.0012228542050090397,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.564652383327484e-08,
              "p95": 1.7872787395844986e-06,
              "p99": 1.48756371345371e-05,
              "maximum": 7.128785364329815e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888944372535,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3671321882765852,
            "cvrmse_percent": 46.110003105168055,
            "rms_normalized_rmse_percent": 2.658290367344857,
            "reference_energy": 15.398576006683893,
            "candidate_energy": 15.188057117560282,
            "relative_energy_error_percent": 1.3671321882765852,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.464355545825583e-08,
              "p90": 1.805419560696464e-05,
              "p95": 3.078406662098121e-05,
              "p99": 6.736465729773045e-05,
              "maximum": 0.0026625096797943115
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0718199610710144,
              "candidate": 0.06915745139122009,
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
            "nmbe_percent": -0.5466259413184128,
            "cvrmse_percent": 18.452539039157394,
            "rms_normalized_rmse_percent": 2.6570607537583,
            "reference_energy": 38.46082951711295,
            "candidate_energy": 38.25059264572616,
            "relative_energy_error_percent": 0.5466259413184174,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.40845146446145e-08,
              "p90": 1.777132274582982e-05,
              "p95": 3.0525358670274704e-05,
              "p99": 6.573507562279701e-05,
              "maximum": 0.0026625096797943115
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0718199610710144,
              "candidate": 0.06915745139122009,
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
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0012228542050090397,
            "cvrmse_percent": 1.5293000894727466,
            "rms_normalized_rmse_percent": 0.4340807814641064,
            "reference_energy": 23.06225351042906,
            "candidate_energy": 23.06253552816588,
            "relative_energy_error_percent": 0.0012228542050090397,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.564652383327484e-08,
              "p95": 1.7872787395844986e-06,
              "p99": 1.48756371345371e-05,
              "maximum": 7.128785364329815e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 413,
              "rgb_channel": 0,
              "reference": 0.0007990767480805516,
              "candidate": 0.0007277888944372535,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 75.08448633484375,
            "cvrmse_percent": 746.2938704695966,
            "rms_normalized_rmse_percent": 31.86645114783777,
            "reference_energy": 8.674701817106506,
            "candidate_energy": 15.188057117560282,
            "relative_energy_error_percent": 75.08448633484375,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012664368841797113,
              "p95": 0.00017737314983605753,
              "p99": 0.0002915918594226241,
              "maximum": 0.017011139541864395
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.039833150804042816,
              "candidate": 0.05684429034590721,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.52382546141484,
            "cvrmse_percent": 203.98702775997168,
            "rms_normalized_rmse_percent": 31.86669919875444,
            "reference_energy": 31.73695532753557,
            "candidate_energy": 38.25059264572616,
            "relative_energy_error_percent": 20.523825461414813,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001265900064026937,
              "p95": 0.00017737314983605753,
              "p99": 0.000291491043753922,
              "maximum": 0.017011139541864395
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.039833150804042816,
              "candidate": 0.05684429034590721,
              "position": [
                0.5,
                2.5,
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
      "bias_percent": 0.13935710785850228,
      "rms_normalized_error_percent": 0.20824331024738035,
      "absolute_error": {
        "p95": 0.1584172747911621,
        "p99": 0.21260208765281338,
        "maximum": 0.2528608170824942
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.718590231419174,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.20824331024738035
    },
    "overcast": {
      "bias_percent": 0.09082251771279785,
      "rms_normalized_error_percent": 0.1389056548229214,
      "absolute_error": {
        "p95": 0.074713134765625,
        "p99": 0.10277843475341798,
        "maximum": 0.10600090026855469
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.261022567749023,
      "reference_fraction_of_uniform": 0.6460304260253906,
      "rms_normalized_to_uniform_percent": 0.09780647863974377
    },
    "horizon": {
      "bias_percent": 1.0252026507156,
      "rms_normalized_error_percent": 1.8777834925355943,
      "absolute_error": {
        "p95": 0.13216963083007788,
        "p99": 0.16119024909042795,
        "maximum": 0.19656213037965875
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.997571639033147,
      "reference_fraction_of_uniform": 0.11219048658892992,
      "rms_normalized_to_uniform_percent": 0.1616771671419206
    },
    "north": {
      "bias_percent": -62.37107965435069,
      "rms_normalized_error_percent": 96.52447315417984,
      "absolute_error": {
        "p95": 2.5612626814108808e-05,
        "p99": 0.000283771439171688,
        "maximum": 0.00047444596793866367
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.8338221707381308e-05,
      "reference_fraction_of_uniform": 6.863469366180652e-07,
      "rms_normalized_to_uniform_percent": 0.0001792546978084039
    },
    "east": {
      "bias_percent": 0.013172044247116205,
      "rms_normalized_error_percent": 0.2181731787111877,
      "absolute_error": {
        "p95": 0.03241429328918457,
        "p99": 0.04264221191406253,
        "maximum": 0.0503997802734375
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.905510902404785,
      "reference_fraction_of_uniform": 0.18359917402267456,
      "rms_normalized_to_uniform_percent": 0.04374199511683592
    },
    "south": {
      "bias_percent": 0.18352903016899816,
      "rms_normalized_error_percent": 0.30640668239563695,
      "absolute_error": {
        "p95": 0.16632199287414548,
        "p99": 0.19941534996032728,
        "maximum": 0.2333354949951172
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.514705657958984,
      "reference_fraction_of_uniform": 0.6929522156715393,
      "rms_normalized_to_uniform_percent": 0.19541289346215246
    },
    "west": {
      "bias_percent": 0.14494616661538767,
      "rms_normalized_error_percent": 0.20258708300371903,
      "absolute_error": {
        "p95": 0.0271930456161499,
        "p99": 0.03539388656616211,
        "maximum": 0.03554821014404297
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.961853504180908,
      "reference_fraction_of_uniform": 0.1857079118490219,
      "rms_normalized_to_uniform_percent": 0.04089467309961982
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
        "identifier": "teaching_classroom_grid",
        "sensor_count": 63,
        "illuminance": {
          "nmbe_percent": -0.06500704777916876,
          "cvrmse_percent": 1.2610860829831396,
          "absolute_error_percentiles_lux": {
            "p50": 8.23858642578125,
            "p90": 58.87329101562497,
            "p95": 89.01424560546879,
            "p99": 175.2081738281247
          },
          "maximum_absolute_error_lux": 473.783203125,
          "worst": {
            "sensor_index": 6,
            "position": [
              0.5,
              0.5,
              0.75
            ],
            "hour_of_year": 7857.5,
            "foton_lux": 23745.978515625,
            "radiance_lux": 24219.76171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.090782778864971,
            "maximum_error_percentage_points": 0.7443835616438292,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02666295116584469,
            "maximum_error_percentage_points": 0.16732377514988173,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.02389432485322898,
            "maximum_error_percentage_points": 0.08643835616438356,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09741682974559689,
            "maximum_error_percentage_points": 0.4916438356164434,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.08529462926723214,
            "maximum_error_percentage_points": 0.5216438356164375,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004983946917803905,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004983946917803905,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_classroom_grid",
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
      "study_preparation_seconds": 0.007843084051273763,
      "weather_seconds": 0.11109183297958225,
      "metric_reduction_seconds": 0.1956815420417115,
      "write_seconds": 0.029034625040367246,
      "total_seconds": 0.3359873340232298,
      "cold_end_to_end_seconds": 0.34383041807450354,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.014241791912354529,
      "engine_upload_seconds": 0.0007855,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.1430832917103544,
      "engine_annual_reduction_seconds": 0.0031061250483617187,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.1430832917103544
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007843084051273763,
      "weather_seconds": 0.1044196670409292,
      "metric_reduction_seconds": 0.04580637498293072,
      "write_seconds": 0.035679582972079515,
      "total_seconds": 0.18608204100746661,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18608204100746661,
      "raw_export_seconds": 0.014751625014469028,
      "engine_upload_seconds": 7.8458e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0026819166960194707,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011078582960180938,
      "full": 0.13234004203695804
    }
  },
  "elapsed_seconds": 116.66884716704953,
  "result_class": "passed"
}
```
