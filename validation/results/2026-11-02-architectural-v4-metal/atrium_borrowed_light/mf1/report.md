# Foton report

Status: **failed**

```json
{
  "scene": "atrium_borrowed_light",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "atrium_borrowed_light",
    "category": "connections",
    "question": "Can a rooflit atrium feed rooms at two levels through internal glass?",
    "interactions": [
      "roof_glazing",
      "borrowed_light",
      "split_adjacency",
      "stacked_zones"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 108,
    "floor_area": 108.0,
    "aperture_area": 35.2
  },
  "sky_density": 1,
  "status": "failed",
  "passed": false,
  "model_sha256": "4dbea10fc2d26d15fe18ffbc5e7cee5fe74ee211ebf3cc5cfb55ef2c28d22e20",
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
      "scene_fingerprint": 13086254370129758359,
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
      "scene_fingerprint": 13086254370129758359,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": 0.0670691152015031,
        "rms_normalized_error_percent": 1.7294094851839876,
        "absolute_error": {
          "p95": 0.00018826813902705908,
          "p99": 0.0005134795792400837,
          "maximum": 0.0011473782360553741
        },
        "worst_index": [
          22,
          125,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": -0.5487684420738758,
        "rms_normalized_error_percent": 1.8489102110370925,
        "absolute_error": {
          "p95": 0.0,
          "p99": 3.227096749469638e-05,
          "maximum": 0.0002651200629770756
        },
        "worst_index": [
          9,
          102,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.34366405264341343,
        "rms_normalized_error_percent": 1.9304986962885404,
        "absolute_error": {
          "p95": 3.4552067518234253e-07,
          "p99": 7.683003786951303e-05,
          "maximum": 0.00029913708567619324
        },
        "worst_index": [
          6,
          76,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": -0.017583956782226372,
        "rms_normalized_error_percent": 0.7706840311540272,
        "absolute_error": {
          "p95": 9.620455093681805e-05,
          "p99": 0.0001950189471244812,
          "maximum": 0.0003806799650192261
        },
        "worst_index": [
          1,
          131,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.16010013401976741,
        "rms_normalized_error_percent": 1.5974739127693534,
        "absolute_error": {
          "p95": 2.2994742903392748e-05,
          "p99": 4.2970728827640414e-05,
          "maximum": 0.000122937373816967
        },
        "worst_index": [
          7,
          102,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.05190982882517953,
        "rms_normalized_error_percent": 1.4071343578226483,
        "absolute_error": {
          "p95": 1.8367800294072354e-05,
          "p99": 5.710450932383537e-05,
          "maximum": 0.00014694686979055405
        },
        "worst_index": [
          4,
          104,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": 0.030483006820153362,
        "rms_normalized_error_percent": 0.6738879507832533,
        "absolute_error": {
          "p95": 8.433992043137549e-05,
          "p99": 0.00016427040100097656,
          "maximum": 0.0003351159393787384
        },
        "worst_index": [
          17,
          128,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.021123368024802962,
        "rms_normalized_error_percent": 1.3647728628172633,
        "absolute_error": {
          "p95": 1.8759243903332387e-05,
          "p99": 3.5956225474365056e-05,
          "maximum": 0.0001196335069835186
        },
        "worst_index": [
          1,
          136,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.03731381330005468,
        "rms_normalized_error_percent": 1.231849906614036,
        "absolute_error": {
          "p95": 1.5792517297086305e-05,
          "p99": 4.899967461824417e-05,
          "maximum": 0.00014088675379753113
        },
        "worst_index": [
          2,
          80,
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
        "run_count": 12,
        "half_run_count": 6,
        "oracle_stable": false,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.01760992263846177,
                "cvrmse_percent": 3.484120697987086,
                "rms_normalized_rmse_percent": 0.9674450299201308,
                "reference_energy": 24.00306873948307,
                "candidate_energy": 23.99884181764719,
                "relative_energy_error_percent": 0.017609922638461454,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.9704305537355452e-05,
                  "p95": 0.00010772442134718055,
                  "p99": 0.00029049084211389166,
                  "maximum": 0.0004978716994325314
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 127,
                  "rgb_channel": 0,
                  "reference": 0.0132868648506701,
                  "candidate": 0.01378473655010263
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.09698089459871474,
                "cvrmse_percent": 23.749912436728604,
                "rms_normalized_rmse_percent": 1.3851119484840577,
                "reference_energy": 5.315767648528929,
                "candidate_energy": 5.320922927549262,
                "relative_energy_error_percent": 0.09698089459871469,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3888901359374973e-05,
                  "p90": 8.309120312333102e-05,
                  "p95": 0.00016064916271716322,
                  "p99": 0.0004101265221834183,
                  "maximum": 0.0006650301317373912
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 133,
                  "rgb_channel": 0,
                  "reference": 0.0016579382742444675,
                  "candidate": 0.0009929081425070763
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.11929454636782531,
                "cvrmse_percent": 10.846077759001206,
                "rms_normalized_rmse_percent": 1.0021814954932344,
                "reference_energy": 0.959585710972533,
                "candidate_energy": 0.9607304443934481,
                "relative_energy_error_percent": 0.11929454636782431,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.8832112244951246e-05,
                  "maximum": 0.00015897396951913834
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 121,
                  "rgb_channel": 0,
                  "reference": 0.008791610909005007,
                  "candidate": 0.008950584878524145
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.4180078480424827,
                "cvrmse_percent": 108.44795181901272,
                "rms_normalized_rmse_percent": 1.9589568062091935,
                "reference_energy": 0.18777463235063507,
                "candidate_energy": 0.18135648068025745,
                "relative_energy_error_percent": 3.4180078480424827,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.787955288070711e-08,
                  "p90": 1.4548255573269369e-05,
                  "p95": 2.3828105875622854e-05,
                  "p99": 5.730582900772181e-05,
                  "maximum": 0.0001839061345284184
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 102,
                  "rgb_channel": 0,
                  "reference": -5.6796474382281303e-05,
                  "candidate": 0.0001271096601461371
                },
                "passed": false,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15761095560512858,
                "cvrmse_percent": 9.783945288028972,
                "rms_normalized_rmse_percent": 1.581384676702857,
                "reference_energy": 2.0020539642437143,
                "candidate_energy": 2.005209420628489,
                "relative_energy_error_percent": 0.1576109556051287,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6947912778705745e-06,
                  "p99": 6.699901617442561e-05,
                  "maximum": 0.0002168638166040182
                },
                "worst": {
                  "global_sensor_index": 81,
                  "local_sensor_index": 9,
                  "sky_patch_index": 78,
                  "rgb_channel": 0,
                  "reference": 0.006112218756849567,
                  "candidate": 0.006329082573453586
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.9867566600024302,
                "cvrmse_percent": 340.0682938932891,
                "rms_normalized_rmse_percent": 2.4132678986041323,
                "reference_energy": 0.08821061734729341,
                "candidate_energy": 0.08469387468537093,
                "relative_energy_error_percent": 3.98675666000243,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.349168835285425e-07,
                  "p90": 1.0217167528026039e-05,
                  "p95": 1.982259402476903e-05,
                  "p99": 0.00010366862018903097,
                  "maximum": 0.0002661872034271558
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": -0.00016076692069570223,
                  "candidate": 0.00010542028273145358
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
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 302.32150002848357,
            "full": 980.3801249945536
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 285.1114999502897,
            "full": 1006.3664590707049
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 246.3780000107363,
            "full": 969.1796660190448
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 292.0186669798568,
            "full": 800.238374969922
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 226.00633290130645,
            "full": 698.077708017081
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 205.92591597232968,
            "full": 728.6446250509471
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 232.8697080956772,
            "full": 694.8884159792215
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 264.58995800931007,
            "full": 776.7037089215592
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 238.26599994208664,
            "full": 712.2275000438094
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.8481249306351,
            "full": 699.6857080375776
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 294.2330000223592,
            "full": 744.5407499326393
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 253.14579100813717,
            "full": 729.1568340733647
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.02207080530466405,
                "cvrmse_percent": 2.7868719868992664,
                "rms_normalized_rmse_percent": 0.7736087358411206,
                "reference_energy": 23.99648439740406,
                "candidate_energy": 24.001780614755376,
                "relative_energy_error_percent": 0.022070805304664046,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3101922124624252e-05,
                  "p95": 9.146279189735642e-05,
                  "p99": 0.00020951498299837112,
                  "maximum": 0.0003962395712733269
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 144,
                  "rgb_channel": 0,
                  "reference": 0.024106040596961975,
                  "candidate": 0.024502280168235302
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.2290162982904075,
                "cvrmse_percent": 13.18778172803066,
                "rms_normalized_rmse_percent": 1.3883811816336578,
                "reference_energy": 10.012934080198534,
                "candidate_energy": 9.990002829217804,
                "relative_energy_error_percent": 0.2290162982904075,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0734012650791556e-05,
                  "p90": 0.00010364881381974556,
                  "p95": 0.00017286153160966892,
                  "p99": 0.0003832443617284298,
                  "maximum": 0.000787719152867794
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 143,
                  "rgb_channel": 0,
                  "reference": 0.001108374446630478,
                  "candidate": 0.00032065529376268387
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.02359444229181958,
                "cvrmse_percent": 11.429592395504722,
                "rms_normalized_rmse_percent": 1.057090760869456,
                "reference_energy": 0.9597298663757101,
                "candidate_energy": 0.9599563092851895,
                "relative_energy_error_percent": 0.02359444229181958,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3212283849716187e-05,
                  "maximum": 0.00014387676492333412
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 135,
                  "rgb_channel": 0,
                  "reference": 0.008839723188430071,
                  "candidate": 0.008983599953353405
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0007752545533244257,
                "cvrmse_percent": 41.63026915606914,
                "rms_normalized_rmse_percent": 2.5164040732053974,
                "reference_energy": 0.6475783870961713,
                "candidate_energy": 0.6475834074771036,
                "relative_energy_error_percent": 0.0007752545533244258,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.6233793139217596e-06,
                  "p90": 2.2550735593540594e-05,
                  "p95": 3.3251428089897655e-05,
                  "p99": 6.801504787290469e-05,
                  "maximum": 0.0002672199625521898
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 10,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 4.1458988562226295e-06,
                  "candidate": 0.00027136586140841246
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04175307416684541,
                "cvrmse_percent": 11.789242450620346,
                "rms_normalized_rmse_percent": 1.905990316739923,
                "reference_energy": 2.0039124477939367,
                "candidate_energy": 2.004749142844503,
                "relative_energy_error_percent": 0.041753074166845414,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.454909794228996e-06,
                  "p99": 7.921724318293855e-05,
                  "maximum": 0.0002824591938406229
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 10,
                  "sky_patch_index": 80,
                  "rgb_channel": 0,
                  "reference": 0.006646749097853899,
                  "candidate": 0.006929208291694522
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.38494340386216036,
                "cvrmse_percent": 51.73118102327079,
                "rms_normalized_rmse_percent": 2.6468728539307045,
                "reference_energy": 0.6574893819742549,
                "candidate_energy": 0.6600203439812589,
                "relative_energy_error_percent": 0.3849434038621604,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.972401827923022e-06,
                  "p90": 1.7234629922313616e-05,
                  "p95": 2.7129937916470185e-05,
                  "p99": 0.00011397898924769834,
                  "maximum": 0.0002900124527513981
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 10,
                  "sky_patch_index": 80,
                  "rgb_channel": 0,
                  "reference": 0.0003670270089060068,
                  "candidate": 7.701455615460873e-05
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
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 356.46120796445757,
            "full": 9229.31491700001
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 358.6759160971269,
            "full": 9955.901874927804
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 357.9704170115292,
            "full": 11392.742458963767
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 469.43729103077203,
            "full": 13287.553500034846
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.004836506372971523,
                "cvrmse_percent": 2.925640132466642,
                "rms_normalized_rmse_percent": 0.812110572050735,
                "reference_energy": 24.00363519514019,
                "candidate_energy": 24.002474257794233,
                "relative_energy_error_percent": 0.004836506372971523,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3545464500784874e-05,
                  "p95": 9.493064135313034e-05,
                  "p99": 0.00021335110068321228,
                  "maximum": 0.00046213530004024506
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 135,
                  "rgb_channel": 0,
                  "reference": 0.020867375656962395,
                  "candidate": 0.02040524035692215
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.11419090155880027,
                "cvrmse_percent": 12.583467341674206,
                "rms_normalized_rmse_percent": 1.3224825450901443,
                "reference_energy": 9.997275601557078,
                "candidate_energy": 9.985859622416342,
                "relative_energy_error_percent": 0.11419090155880025,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0909501472488046e-05,
                  "p90": 0.0001013833680190146,
                  "p95": 0.00016356893174815915,
                  "p99": 0.000343074556440115,
                  "maximum": 0.0008324617519974709
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 135,
                  "rgb_channel": 0,
                  "reference": 0.0006353193894028664,
                  "candidate": 0.0014677811414003372
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.17588021780558571,
                "cvrmse_percent": 12.032938715225603,
                "rms_normalized_rmse_percent": 1.1124228198950068,
                "reference_energy": 0.9589663821661816,
                "candidate_energy": 0.9606530143278178,
                "relative_energy_error_percent": 0.17588021780558571,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.290625707246363e-05,
                  "maximum": 0.00015831738710403442
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 9,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 0.006113046547397971,
                  "candidate": 0.006271363934502006
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.25452216855066134,
                "cvrmse_percent": 42.839528952614856,
                "rms_normalized_rmse_percent": 2.60308152967754,
                "reference_energy": 0.6510162733278229,
                "candidate_energy": 0.6493592925913312,
                "relative_energy_error_percent": 0.25452216855066134,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.551098416210152e-06,
                  "p90": 2.195139677496627e-05,
                  "p95": 3.2741647828515825e-05,
                  "p99": 6.976992881391197e-05,
                  "maximum": 0.000279167084954679
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": -0.00011980999261140823,
                  "candidate": 0.00015935709234327078
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.011910611930611463,
                "cvrmse_percent": 10.632747384886034,
                "rms_normalized_rmse_percent": 1.7198452749525206,
                "reference_energy": 2.003611533725234,
                "candidate_energy": 2.003850176119613,
                "relative_energy_error_percent": 0.011910611930611463,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.7400041542713475e-06,
                  "p99": 8.079898543655872e-05,
                  "maximum": 0.00021212524734437466
                },
                "worst": {
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "sky_patch_index": 77,
                  "rgb_channel": 0,
                  "reference": 0.006146581145003438,
                  "candidate": 0.005934455897659063
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.16596102527325202,
                "cvrmse_percent": 47.024218347652294,
                "rms_normalized_rmse_percent": 2.4197107014152563,
                "reference_energy": 0.6612859405508615,
                "candidate_energy": 0.6601884636239355,
                "relative_energy_error_percent": 0.16596102527325202,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.9282348325286875e-06,
                  "p90": 1.708624404272996e-05,
                  "p95": 2.7474315629660844e-05,
                  "p99": 9.896628034766763e-05,
                  "maximum": 0.00025277247186750174
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 26,
                  "sky_patch_index": 54,
                  "rgb_channel": 0,
                  "reference": -3.384851152077317e-05,
                  "candidate": 0.00021892396034672856
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
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 541.7226669378579,
            "full": 14279.377250000834
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 485.45937496237457,
            "full": 10663.757000002079
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 346.6017920291051,
            "full": 9948.31504195463
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 348.71133300475776,
            "full": 9767.339166020975
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.002701208489274606,
                "cvrmse_percent": 2.0897736975863905,
                "rms_normalized_rmse_percent": 0.5800861283727188,
                "reference_energy": 24.001754343465848,
                "candidate_energy": 24.00240268089175,
                "relative_energy_error_percent": 0.0027012084892746057,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2055039405822754e-05,
                  "p95": 7.019671611487865e-05,
                  "p99": 0.00016433466225862503,
                  "maximum": 0.00033474061638116837
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 135,
                  "rgb_channel": 0,
                  "reference": 0.021979925222694874,
                  "candidate": 0.021645184606313705
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.027115713519716363,
                "cvrmse_percent": 8.617766803856487,
                "rms_normalized_rmse_percent": 0.9066182333022236,
                "reference_energy": 10.004262729021313,
                "candidate_energy": 10.001550001799952,
                "relative_energy_error_percent": 0.027115713519716363,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4522200217470527e-05,
                  "p90": 7.09142668711138e-05,
                  "p95": 0.00011399374343454815,
                  "p99": 0.00023696105927228928,
                  "maximum": 0.000490034930408001
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 144,
                  "rgb_channel": 0,
                  "reference": 0.0005344254896044731,
                  "candidate": 0.001024460420012474
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.026450295192612907,
                "cvrmse_percent": 9.312963224025843,
                "rms_normalized_rmse_percent": 0.8600742221199312,
                "reference_energy": 0.9592547629431465,
                "candidate_energy": 0.9590010372266988,
                "relative_energy_error_percent": 0.026450295192612907,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4994991943240166e-05,
                  "maximum": 0.00013448530808091164
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 123,
                  "rgb_channel": 0,
                  "reference": 0.010350170079618692,
                  "candidate": 0.01021568477153778
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.08352075660987486,
                "cvrmse_percent": 29.50236420062842,
                "rms_normalized_rmse_percent": 1.796215854715159,
                "reference_energy": 0.6514817205525212,
                "candidate_energy": 0.6509375980903407,
                "relative_energy_error_percent": 0.08352075660987486,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.6234965844196267e-06,
                  "p90": 1.5357552911154926e-05,
                  "p95": 2.2997260020929372e-05,
                  "p99": 4.550849371298682e-05,
                  "maximum": 0.0002522151917219162
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 123,
                  "rgb_channel": 0,
                  "reference": 0.00016840500757098198,
                  "candidate": 0.0004206201992928982
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08776412927889427,
                "cvrmse_percent": 5.973298689620022,
                "rms_normalized_rmse_percent": 0.9653095512088115,
                "reference_energy": 2.0044526473027418,
                "candidate_energy": 2.0026934568900288,
                "relative_energy_error_percent": 0.08776412927889425,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.9062939574940095e-06,
                  "p99": 4.12105000577867e-05,
                  "maximum": 0.00012203073129057884
                },
                "worst": {
                  "global_sensor_index": 87,
                  "local_sensor_index": 15,
                  "sky_patch_index": 80,
                  "rgb_channel": 0,
                  "reference": 0.004148803651332855,
                  "candidate": 0.004026772920042276
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3205300686683943,
                "cvrmse_percent": 29.845321845871194,
                "rms_normalized_rmse_percent": 1.5344680603063485,
                "reference_energy": 0.6608301387366922,
                "candidate_energy": 0.6629482980341663,
                "relative_energy_error_percent": 0.3205300686683943,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7845537715620594e-06,
                  "p90": 1.2207347026560456e-05,
                  "p95": 1.9080856873188137e-05,
                  "p99": 5.8908481150865555e-05,
                  "maximum": 0.0001570971217006445
                },
                "worst": {
                  "global_sensor_index": 86,
                  "local_sensor_index": 14,
                  "sky_patch_index": 78,
                  "rgb_channel": 0,
                  "reference": 0.0001400965265929699,
                  "candidate": 0.0002971936482936144
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
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 592.7783750230446,
            "full": 20686.270750011317
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 962.0513330446556,
            "full": 26241.87362496741
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 797.6985409623012,
            "full": 20326.412874972448
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 660.642542061396,
            "full": 17534.495041007176
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 3099.044375005178,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11691.900624893606,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.4786319576575537,
            "cvrmse_percent": 14.023858078198208,
            "rms_normalized_rmse_percent": 3.9272157184839114,
            "reference_energy": 23.99577915355235,
            "candidate_energy": 23.640969894498994,
            "relative_energy_error_percent": 1.4786319576575537,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.759407162666321e-05,
              "p95": 0.000200095693435287,
              "p99": 0.0006971295806579292,
              "maximum": 0.0040959627367556095
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.0040959627367556095,
              "candidate": 0.0,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5663066662632016,
            "cvrmse_percent": 49.575049626147496,
            "rms_normalized_rmse_percent": 5.218126686225385,
            "reference_energy": 10.009205702276057,
            "candidate_energy": 9.952522903144072,
            "relative_energy_error_percent": 0.5663066662632016,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.952838884899393e-05,
              "p90": 0.00027225096710026264,
              "p95": 0.00040512902342015845,
              "p99": 0.0009725129930302501,
              "maximum": 0.004342412576079369
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.00596175342798233,
              "candidate": 0.0016193408519029617,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.2100933434611156,
            "cvrmse_percent": 11.206394132244041,
            "rms_normalized_rmse_percent": 4.007378140815933,
            "reference_energy": 34.00498485582841,
            "candidate_energy": 33.593492797643066,
            "relative_energy_error_percent": 1.2100933434611314,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.707250577164814e-05,
              "p90": 0.0002401790115982294,
              "p95": 0.00032261504966299957,
              "p99": 0.0006706144195050001,
              "maximum": 0.004342449828982353
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.02979414165019989,
              "candidate": 0.025451691821217537,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.33255591361550063,
            "cvrmse_percent": 14.505490807793906,
            "rms_normalized_rmse_percent": 1.3378272180489916,
            "reference_energy": 0.9569211066882417,
            "candidate_energy": 0.9601034044171683,
            "relative_energy_error_percent": 0.33255591361550063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.4534063413739204e-05,
              "maximum": 0.00024422514252364635
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 9,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.0028928988613188267,
              "candidate": 0.003137124003842473,
              "position": [
                7.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9193266809293286,
            "cvrmse_percent": 65.81539235107668,
            "rms_normalized_rmse_percent": 4.017882540719302,
            "reference_energy": 0.6534164612089306,
            "candidate_energy": 0.6408752647313634,
            "relative_energy_error_percent": 1.9193266809293283,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.058358844209579e-06,
              "p90": 4.311242446419783e-05,
              "p95": 5.835155916429352e-05,
              "p99": 0.00010330552322557196,
              "maximum": 0.00022430461831390858
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 105,
              "rgb_channel": 0,
              "reference": 0.00035116460639983416,
              "candidate": 0.00012685998808592558,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5811762039968883,
            "cvrmse_percent": 25.913984438165667,
            "rms_normalized_rmse_percent": 3.8987986670573465,
            "reference_energy": 1.6103375678971723,
            "candidate_energy": 1.6009786691485317,
            "relative_energy_error_percent": 0.5811762039968882,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.051091555216772e-06,
              "p90": 4.301772059989162e-05,
              "p95": 5.8208842619933384e-05,
              "p99": 9.67512241913937e-05,
              "maximum": 0.0002206912758992985
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 85,
              "rgb_channel": 0,
              "reference": 0.0003059712762478739,
              "candidate": 8.528000034857541e-05,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "full_identifier": "atrium_borrowed_light_office_1_grid",
        "start_sensor_index": 72,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1325929355835285,
            "cvrmse_percent": 6.0722114313944475,
            "rms_normalized_rmse_percent": 0.982535812116992,
            "reference_energy": 2.0080703420130703,
            "candidate_energy": 2.005407782598013,
            "relative_energy_error_percent": 0.1325929355835285,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.179069608449736e-07,
              "p99": 3.751774784177542e-05,
              "maximum": 0.00014621688751503825
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.000927561370190233,
              "candidate": 0.0010737782577052712,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.7156620191880386,
            "cvrmse_percent": 63.887301385242544,
            "rms_normalized_rmse_percent": 3.266241400189036,
            "reference_energy": 0.6573919334108442,
            "candidate_energy": 0.6620966377954716,
            "relative_energy_error_percent": 0.7156620191880386,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1208705473109148e-05,
              "p90": 4.056590478285216e-05,
              "p95": 5.583321217272895e-05,
              "p99": 9.517930448055267e-05,
              "maximum": 0.00025151576846838
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 24,
              "sky_patch_index": 52,
              "rgb_channel": 0,
              "reference": 0.00016670417971909046,
              "candidate": 0.00041821994818747044,
              "position": [
                10.5,
                5.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.07661503928976901,
            "cvrmse_percent": 15.37055331460624,
            "rms_normalized_rmse_percent": 3.1861880663863955,
            "reference_energy": 2.6654622754239146,
            "candidate_energy": 2.6675044203934846,
            "relative_energy_error_percent": 0.07661503928976901,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1162445389345521e-05,
              "p90": 4.0308572351932526e-05,
              "p95": 5.5268670621444403e-05,
              "p99": 9.049680375028402e-05,
              "maximum": 0.00025192031171172857
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 24,
              "sky_patch_index": 52,
              "rgb_channel": 0,
              "reference": 0.0014185348991304636,
              "candidate": 0.0016704552108421922,
              "position": [
                10.5,
                5.5,
                3.75
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
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.4786319576575537,
            "cvrmse_percent": 14.023858078198208,
            "rms_normalized_rmse_percent": 3.9272157184839114,
            "reference_energy": 23.99577915355235,
            "candidate_energy": 23.640969894498994,
            "relative_energy_error_percent": 1.4786319576575537,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.759407162666321e-05,
              "p95": 0.000200095693435287,
              "p99": 0.0006971295806579292,
              "maximum": 0.0040959627367556095
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.0040959627367556095,
              "candidate": 0.0,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.95375462115469,
            "cvrmse_percent": 145.82830976787463,
            "rms_normalized_rmse_percent": 8.517832138716452,
            "reference_energy": 5.32352127578929,
            "candidate_energy": 9.952522903144072,
            "relative_energy_error_percent": 86.95375462115469,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.00023282162146642804,
              "p90": 0.0007242085412144661,
              "p95": 0.0009003353305160998,
              "p99": 0.0015393048524856567,
              "maximum": 0.0047795545106055215
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 129,
              "rgb_channel": 0,
              "reference": -0.003946074531995691,
              "candidate": 0.0008334799786098301,
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
            "nmbe_percent": 14.57808442122302,
            "cvrmse_percent": 23.01822454614527,
            "rms_normalized_rmse_percent": 7.404805695255428,
            "reference_energy": 29.319300429341638,
            "candidate_energy": 33.593492797643066,
            "relative_energy_error_percent": 14.578084421223021,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0002309877163497731,
              "p90": 0.0006754323840141296,
              "p95": 0.0008208323051803744,
              "p99": 0.00128084234893322,
              "maximum": 0.003703771159052849
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.029155462980270386,
              "candidate": 0.025451691821217537,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.33255591361550063,
            "cvrmse_percent": 14.505490807793906,
            "rms_normalized_rmse_percent": 1.3378272180489916,
            "reference_energy": 0.9569211066882417,
            "candidate_energy": 0.9601034044171683,
            "relative_energy_error_percent": 0.33255591361550063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.4534063413739204e-05,
              "maximum": 0.00024422514252364635
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 9,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.0028928988613188267,
              "candidate": 0.003137124003842473,
              "position": [
                7.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 241.2495329888182,
            "cvrmse_percent": 463.175635536028,
            "rms_normalized_rmse_percent": 8.366968615376033,
            "reference_energy": 0.18780253239272948,
            "candidate_energy": 0.6408752647313634,
            "relative_energy_error_percent": 241.24953298881817,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2195000181236537e-05,
              "p90": 9.097000292968005e-05,
              "p95": 0.00012527203734862268,
              "p99": 0.00020583439618349075,
              "maximum": 0.0003760559484362602
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 137,
              "rgb_channel": 0,
              "reference": -0.00011604605242609978,
              "candidate": 0.00026000989601016045,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 39.85722094756948,
            "cvrmse_percent": 76.16079368712113,
            "rms_normalized_rmse_percent": 8.385966096629568,
            "reference_energy": 1.1447236390809712,
            "candidate_energy": 1.6009786691485317,
            "relative_energy_error_percent": 39.85722094756948,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2217267794767395e-05,
              "p90": 9.170999692287296e-05,
              "p95": 0.00012646770915054615,
              "p99": 0.0002048053556791274,
              "maximum": 0.00034864526242017746
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0089201545342803,
              "candidate": 0.009268799796700478,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "full_identifier": "atrium_borrowed_light_office_1_grid",
        "start_sensor_index": 72,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1325929355835285,
            "cvrmse_percent": 6.0722114313944475,
            "rms_normalized_rmse_percent": 0.982535812116992,
            "reference_energy": 2.0080703420130703,
            "candidate_energy": 2.005407782598013,
            "relative_energy_error_percent": 0.1325929355835285,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.179069608449736e-07,
              "p99": 3.751774784177542e-05,
              "maximum": 0.00014621688751503825
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.000927561370190233,
              "candidate": 0.0010737782577052712,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 707.3010964722058,
            "cvrmse_percent": 1237.0905583363322,
            "rms_normalized_rmse_percent": 8.16252010663039,
            "reference_energy": 0.08201359327873359,
            "candidate_energy": 0.6620966377954716,
            "relative_energy_error_percent": 707.3010964722058,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9990000510006212e-05,
              "p90": 9.92700006463565e-05,
              "p95": 0.00014602388719282518,
              "p99": 0.000253013102337718,
              "maximum": 0.0004317518323659897
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 3,
              "sky_patch_index": 79,
              "rgb_channel": 0,
              "reference": -7.559172809123993e-05,
              "candidate": 0.00035616010427474976,
              "position": [
                6.5,
                2.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.626664908127957,
            "cvrmse_percent": 48.15579062551393,
            "rms_normalized_rmse_percent": 8.097466805749697,
            "reference_energy": 2.090083935291804,
            "candidate_energy": 2.6675044203934846,
            "relative_energy_error_percent": 27.626664908127957,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.000192921514099e-05,
              "p90": 9.904055866627459e-05,
              "p95": 0.00014459025114774702,
              "p99": 0.00024746000417508185,
              "maximum": 0.0004317415878176689
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 3,
              "sky_patch_index": 79,
              "rgb_channel": 0,
              "reference": 0.006755821406841278,
              "candidate": 0.007187562994658947,
              "position": [
                6.5,
                2.5,
                3.75
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
      "bias_percent": -1.0939335477614933,
      "rms_normalized_error_percent": 2.0980324570652438,
      "absolute_error": {
        "p95": 0.6284596488222491,
        "p99": 3.6402522871178444,
        "maximum": 3.9588988340846853
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 21.148928545406225,
      "rms_normalized_to_uniform_percent": 2.0980324570652438
    },
    "overcast": {
      "bias_percent": -1.0783718850519497,
      "rms_normalized_error_percent": 2.0934185631293074,
      "absolute_error": {
        "p95": 0.5210155487060545,
        "p99": 3.2810031127929635,
        "maximum": 3.6134109497070312
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 18.539491653442383,
      "rms_normalized_to_uniform_percent": 1.8678877078410185
    },
    "horizon": {
      "bias_percent": 4.160531448581594,
      "rms_normalized_error_percent": 21.28526793049438,
      "absolute_error": {
        "p95": 0.04504123313400902,
        "p99": 0.05770492845262993,
        "maximum": 0.07304803031605688
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.06357089411514265,
      "rms_normalized_to_uniform_percent": 0.0597708126576568
    },
    "north": {
      "bias_percent": -0.8567227491216479,
      "rms_normalized_error_percent": 1.6814721035257778,
      "absolute_error": {
        "p95": 0.1622752428054809,
        "p99": 0.3510617399215687,
        "maximum": 0.7591705322265625
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.1901118755340576,
      "rms_normalized_to_uniform_percent": 0.29727326030414203
    },
    "east": {
      "bias_percent": 0.004170750889773392,
      "rms_normalized_error_percent": 0.6927296203730194,
      "absolute_error": {
        "p95": 0.09653239250183084,
        "p99": 0.17357295036315887,
        "maximum": 0.18230342864990234
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.129446268081665,
      "rms_normalized_to_uniform_percent": 0.12682080235083165
    },
    "south": {
      "bias_percent": -1.0149632732653673,
      "rms_normalized_error_percent": 2.0920166384355614,
      "absolute_error": {
        "p95": 0.18435134887695284,
        "p99": 0.5646104812622047,
        "maximum": 0.9208478927612305
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.184786081314087,
      "rms_normalized_to_uniform_percent": 0.369947401203028
    },
    "west": {
      "bias_percent": -2.8131288120291735,
      "rms_normalized_error_percent": 5.085796889094838,
      "absolute_error": {
        "p95": 0.3156497001647948,
        "p99": 1.711021947860715,
        "maximum": 1.7645950317382812
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.030074596405029,
      "rms_normalized_to_uniform_percent": 0.9660542683352182
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "atrium_borrowed_light_atrium_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -1.4710663639279526,
          "cvrmse_percent": 7.180972451282075,
          "absolute_error_percentiles_lux": {
            "p50": 16.5592041015625,
            "p90": 141.52279052734377,
            "p95": 214.89359130859373,
            "p99": 447.21175781249997
          },
          "maximum_absolute_error_lux": 3336.3671875,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 32823.1484375,
            "radiance_lux": 36159.515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.23517503805175088,
            "maximum_error_percentage_points": 1.091095890410955,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.12033298797014938,
            "maximum_error_percentage_points": 0.5602448201289434,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12063546423135449,
            "maximum_error_percentage_points": 0.739315068493152,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.45941019786910275,
            "maximum_error_percentage_points": 1.5093150684931445,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.52089802130898,
            "maximum_error_percentage_points": 1.9216438356164378,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.361915607488731,
          "cvrmse_percent": 16.288496133643314,
          "absolute_error_percentiles_lux": {
            "p50": 1.5560717582702637,
            "p90": 20.42327728271485,
            "p95": 32.61067962646479,
            "p99": 66.36246810913066
          },
          "maximum_absolute_error_lux": 225.80709838867188,
          "worst": {
            "sensor_index": 4,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 660.5842895507812,
            "radiance_lux": 434.7771911621094
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3217275494672755,
            "maximum_error_percentage_points": 3.967671232876711,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5648869226368238,
            "maximum_error_percentage_points": 2.197119977702748,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.2809817351598167,
            "maximum_error_percentage_points": 4.325616438356164,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.281681887366819,
            "maximum_error_percentage_points": 4.325616438356165,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0054452054794520725,
            "maximum_error_percentage_points": 0.1134246575342468,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.07901629286353415,
          "cvrmse_percent": 5.993196972588345,
          "absolute_error_percentiles_lux": {
            "p50": 2.727649688720703,
            "p90": 22.741797637939456,
            "p95": 33.64163646697993,
            "p99": 62.694990234374885
          },
          "maximum_absolute_error_lux": 216.9525146484375,
          "worst": {
            "sensor_index": 24,
            "position": [
              10.5,
              5.5,
              3.75
            ],
            "hour_of_year": 5752.5,
            "foton_lux": 1777.4310302734375,
            "radiance_lux": 1560.478515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6056735159817355,
            "maximum_error_percentage_points": 3.2575342465753465,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.40553542938557663,
            "maximum_error_percentage_points": 1.1901130612705124,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.1356430745814319,
            "maximum_error_percentage_points": 3.9689041095890474,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.137465753424658,
            "maximum_error_percentage_points": 3.9689041095890403,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.013904109589041048,
            "maximum_error_percentage_points": 0.11000000000000032,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 8.333333333333334,
          "radiance_percent": 8.333333333333334,
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
    "numerical_correctness": "failed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004978328339042548,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.00486247859588218,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004954215271832041,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004978328339042548,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.003835616438356837,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
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
      "study_preparation_seconds": 0.01492083293851465,
      "weather_seconds": 0.10041554202325642,
      "metric_reduction_seconds": 0.09445237508043647,
      "write_seconds": 0.09579483303241432,
      "total_seconds": 0.29096179199405015,
      "cold_end_to_end_seconds": 0.3058826249325648,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0443330000853166,
      "engine_upload_seconds": 0.000450375,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.035122916800901294,
      "engine_annual_reduction_seconds": 0.0009984165662899613,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.035122916800901294
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.01492083293851465,
      "weather_seconds": 0.10566800006199628,
      "metric_reduction_seconds": 0.0243279580026865,
      "write_seconds": 0.0804052499588579,
      "total_seconds": 0.21087599999736995,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.21087599999736995,
      "raw_export_seconds": 0.04016529198270291,
      "engine_upload_seconds": 7.8167e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001042374991811812,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.039493000018410385,
      "full": 0.032078291988000274
    }
  },
  "elapsed_seconds": 209.748026083922,
  "result_class": "accuracy_failure"
}
```
