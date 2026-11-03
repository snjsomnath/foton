# Foton report

Status: **passed**

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
  "status": "passed",
  "passed": true,
  "model_sha256": "280bc792d4912f4969942a59e44f5e075eab373cc760604a30c0a07ca224b587",
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
      "solver_version": "0.3.0",
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
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "0cd01573c9c1b174028ec7b06d2071ffc5f0ec3d8c18ace10be2958f109d5480",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9c8ff7b285e183ba0928dcb0951c8cbb1b1f540858e87be7f2de7d3272b7001e",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0011473782360553741,
          "p95": 0.00018826813902705908,
          "p99": 0.0005134795792400837
        },
        "bias_percent": 0.0670691152015031,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7294094851839876,
        "worst_index": [
          22,
          125,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0002651200629770756,
          "p95": 0.0,
          "p99": 3.227096749469638e-05
        },
        "bias_percent": -0.5487684420738758,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8489102110370925,
        "worst_index": [
          9,
          102,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00029913708567619324,
          "p95": 3.4552067518234253e-07,
          "p99": 7.683003786951303e-05
        },
        "bias_percent": 0.34366405264341343,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9304986962885404,
        "worst_index": [
          6,
          76,
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
          "maximum": 0.0004309341311454773,
          "p95": 9.821622224990267e-05,
          "p99": 0.00019021518528461456
        },
        "bias_percent": 0.0046256362540679314,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7726282622001353,
        "worst_index": [
          15,
          144,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00012778211385011673,
          "p95": 2.2297451869235372e-05,
          "p99": 4.5062159188091755e-05
        },
        "bias_percent": 0.14219074109351393,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.587353703238353,
        "worst_index": [
          1,
          121,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0001237732358276844,
          "p95": 1.8609914513945102e-05,
          "p99": 5.6894030421972275e-05
        },
        "bias_percent": 0.116218405672488,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.392749694269023,
        "worst_index": [
          3,
          123,
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
          "maximum": 0.00031019560992717743,
          "p95": 8.676210418343539e-05,
          "p99": 0.00016427785158157349
        },
        "bias_percent": -0.0034101528292270243,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.666392960647879,
        "worst_index": [
          12,
          118,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 9.101373143494129e-05,
          "p95": 1.9266818799223974e-05,
          "p99": 3.485797060420737e-05
        },
        "bias_percent": -0.07554164779731949,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3479464956751837,
        "worst_index": [
          2,
          103,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00011740927584469318,
          "p95": 1.5132433873077389e-05,
          "p99": 4.186108708381653e-05
        },
        "bias_percent": -0.048435522949022806,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1020951206429936,
        "worst_index": [
          1,
          121,
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007962975651025772,
                  "p50": 0.0,
                  "p90": 4.3266627471894026e-05,
                  "p95": 0.0001408507552696391,
                  "p99": 0.0003399001434445381
                },
                "candidate_energy": 24.01490030823163,
                "cvrmse_percent": 4.555302471336338,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.022987034471911427,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.0093812634841,
                "relative_energy_error_percent": 0.022987034471911427,
                "rms_normalized_rmse_percent": 1.2640616788825014,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012448747642338276,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.013245045207440853,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008974685333669186,
                  "p50": 1.6436262740171514e-05,
                  "p90": 0.0001015994930639863,
                  "p95": 0.00018553039408288893,
                  "p99": 0.0004892349243164062
                },
                "candidate_energy": 5.297133087865436,
                "cvrmse_percent": 28.937311272118002,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2755649583608201,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.311770465938121,
                "relative_energy_error_percent": 0.2755649583608201,
                "rms_normalized_rmse_percent": 1.6859129546810874,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008607630152255297,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0017582315485924482,
                  "rgb_channel": 0,
                  "sky_patch_index": 110
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019821478053927422,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.1321600545197725e-05
                },
                "candidate_energy": 0.961093220181283,
                "cvrmse_percent": 14.662205031207755,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.13079282045429114,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9598378212231182,
                "relative_energy_error_percent": 0.13079282045429114,
                "rms_normalized_rmse_percent": 1.3541428482985132,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005313058733008802,
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "reference": 0.005114843952469528,
                  "rgb_channel": 0,
                  "sky_patch_index": 105
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000536174513399601,
                  "p50": 0.0,
                  "p90": 2.0144949758105213e-05,
                  "p95": 3.194281998730728e-05,
                  "p99": 7.091532461345196e-05
                },
                "candidate_energy": 0.1853694248790152,
                "cvrmse_percent": 160.20918812797703,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10703177252969405,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.1855680416432346,
                "relative_energy_error_percent": 0.10703177252969405,
                "rms_normalized_rmse_percent": 2.8575997634368906,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00027711945585906506,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.0002590550575405359,
                  "rgb_channel": 0,
                  "sky_patch_index": 122
                }
              }
            },
            "start_sensor_index": 36
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002996382536366582,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.135154838673507e-06,
                  "p99": 0.00010415317956358194
                },
                "candidate_energy": 2.008657651010708,
                "cvrmse_percent": 15.098492751219936,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.21095362142147014,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0044292349507487,
                "relative_energy_error_percent": 0.21095362142147014,
                "rms_normalized_rmse_percent": 2.438539394010604,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0072151361964643,
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "reference": 0.006915497942827642,
                  "rgb_channel": 0,
                  "sky_patch_index": 123
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005500680999830365,
                  "p50": 5.454495806134219e-07,
                  "p90": 1.2426202829374233e-05,
                  "p95": 2.4865975211696373e-05,
                  "p99": 0.0001211259514093399
                },
                "candidate_energy": 0.08231354851959516,
                "cvrmse_percent": 483.4629463988898,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5121058060809126,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0827372507846551,
                "relative_energy_error_percent": 0.5121058060809126,
                "rms_normalized_rmse_percent": 3.217454813712815,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0003608895931392908,
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "reference": 0.0001891785068437457,
                  "rgb_channel": 0,
                  "sky_patch_index": 101
                }
              }
            },
            "start_sensor_index": 72
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.42870794795454,
            "full": 666.1978749325499
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.07374993618578,
            "full": 665.5378750292584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.68183398246765,
            "full": 642.3897910863161
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.06254202034324,
            "full": 660.9038750175387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.93120805826038,
            "full": 652.126666973345
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.45616701990366,
            "full": 665.0200829608366
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.7162499865517,
            "full": 655.9312499593943
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.35395802836865,
            "full": 655.5246249772608
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00034636445343494415,
                  "p50": 0.0,
                  "p90": 2.2880500182509422e-05,
                  "p95": 8.740829653106586e-05,
                  "p99": 0.00018746498972177505
                },
                "candidate_energy": 23.997788749059396,
                "cvrmse_percent": 2.4202353095126536,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.006486615831492675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.99623220566218,
                "relative_energy_error_percent": 0.006486615831492676,
                "rms_normalized_rmse_percent": 0.6717247990585326,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.020382375456392765,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.02072873990982771,
                  "rgb_channel": 0,
                  "sky_patch_index": 132
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006756847724318504,
                  "p50": 2.0704494090750813e-05,
                  "p90": 9.525154018774629e-05,
                  "p95": 0.00014818785712122885,
                  "p99": 0.0003221607767045498
                },
                "candidate_energy": 10.00842440122036,
                "cvrmse_percent": 11.6044484702822,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08451574289889344,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.999972849876599,
                "relative_energy_error_percent": 0.08451574289889345,
                "rms_normalized_rmse_percent": 1.2202492015321633,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006066299974918365,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.001282314769923687,
                  "rgb_channel": 0,
                  "sky_patch_index": 139
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00012088660150766373,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3738481104373932e-05
                },
                "candidate_energy": 0.9608239688841422,
                "cvrmse_percent": 10.490930936310429,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.21722869060326447,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9587413076951634,
                "relative_energy_error_percent": 0.21722869060326447,
                "rms_normalized_rmse_percent": 0.9686946882051315,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037491684779524803,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.003870055079460144,
                  "rgb_channel": 0,
                  "sky_patch_index": 102
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00025504420045763254,
                  "p50": 3.551901045284467e-06,
                  "p90": 2.1598607418127358e-05,
                  "p95": 3.1075065817276444e-05,
                  "p99": 6.244153883017134e-05
                },
                "candidate_energy": 0.6465977439184165,
                "cvrmse_percent": 38.665617770869986,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5606960351369266,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6502436341940729,
                "relative_energy_error_percent": 0.5606960351369266,
                "rms_normalized_rmse_percent": 2.348665240765064,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 8.33242665976286e-06,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": 0.0002633766271173954,
                  "rgb_channel": 0,
                  "sky_patch_index": 104
                }
              }
            },
            "start_sensor_index": 36
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019610743038356304,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1230778656898974e-06,
                  "p99": 6.908038631081581e-05
                },
                "candidate_energy": 2.0032822618254613,
                "cvrmse_percent": 9.637781285527508,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.05132868261689627,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0022545309520865,
                "relative_energy_error_percent": 0.051328682616896264,
                "rms_normalized_rmse_percent": 1.557715871181876,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0067584095522761345,
                  "global_sensor_index": 76,
                  "local_sensor_index": 4,
                  "reference": 0.0069545169826596975,
                  "rgb_channel": 0,
                  "sky_patch_index": 80
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00031638145446777344,
                  "p50": 3.852404233839479e-06,
                  "p90": 1.7465794371673837e-05,
                  "p95": 2.8187477164465234e-05,
                  "p99": 0.00010676047531887889
                },
                "candidate_energy": 0.6600875202007259,
                "cvrmse_percent": 50.260457308219664,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2927667649667736,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6620257114594139,
                "relative_energy_error_percent": 0.2927667649667737,
                "rms_normalized_rmse_percent": 2.586661255245746,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 4.2634084820747375e-05,
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "reference": 0.0003590155392885208,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
                }
              }
            },
            "start_sensor_index": 72
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 317.81287502963096,
            "full": 8517.187500023283
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 320.8707500016317,
            "full": 8488.545708940364
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 320.29516610782593,
            "full": 8520.812125061639
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 331.7838340299204,
            "full": 8473.161624977365
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004155207425355911,
                  "p50": 0.0,
                  "p90": 2.36674677580595e-05,
                  "p95": 0.00011321881320327501,
                  "p99": 0.0002484256401658058
                },
                "candidate_energy": 23.99825522519029,
                "cvrmse_percent": 3.173210302186796,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.02989576644792675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.00543183302591,
                "relative_energy_error_percent": 0.029895766447926752,
                "rms_normalized_rmse_percent": 0.8809577539504305,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.020751910284161568,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.020336389541625977,
                  "rgb_channel": 0,
                  "sky_patch_index": 131
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007651550695300102,
                  "p50": 2.0451312593650073e-05,
                  "p90": 0.00010293093509972095,
                  "p95": 0.0001682655900367533,
                  "p99": 0.0003567454405128956
                },
                "candidate_energy": 9.992064107538624,
                "cvrmse_percent": 12.480568350643997,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17731059894403975,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 10.009812566152846,
                "relative_energy_error_percent": 0.17731059894403972,
                "rms_normalized_rmse_percent": 1.313317154588879,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.004988979548215866,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.004223824478685856,
                  "rgb_channel": 0,
                  "sky_patch_index": 112
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00016598147340118885,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.5501398593187332e-05
                },
                "candidate_energy": 0.9585690234516733,
                "cvrmse_percent": 12.790343103850104,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07412344520790064,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9592800748923764,
                "relative_energy_error_percent": 0.07412344520790062,
                "rms_normalized_rmse_percent": 1.1827204490629957,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00124731648247689,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.0010813350090757012,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00028103648219257593,
                  "p50": 3.617242782638641e-06,
                  "p90": 2.2355168766807765e-05,
                  "p95": 3.258937886130285e-05,
                  "p99": 6.748984742444009e-05
                },
                "candidate_energy": 0.6532122550105157,
                "cvrmse_percent": 42.82392155985169,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5067570265125603,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6499187460980416,
                "relative_energy_error_percent": 0.5067570265125604,
                "rms_normalized_rmse_percent": 2.600117689275204,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -5.174550460651517e-05,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.00022929097758606076,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              }
            },
            "start_sensor_index": 36
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000193099956959486,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.5107179428449414e-06,
                  "p99": 7.362343603745103e-05
                },
                "candidate_energy": 2.005838152094384,
                "cvrmse_percent": 10.601044988407926,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1429869116013546,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0029741612011094,
                "relative_energy_error_percent": 0.1429869116013546,
                "rms_normalized_rmse_percent": 1.7129305071660519,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006862187059596181,
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "reference": 0.007055287016555667,
                  "rgb_channel": 0,
                  "sky_patch_index": 123
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003503951011225581,
                  "p50": 3.943870069633704e-06,
                  "p90": 1.7178494090330787e-05,
                  "p95": 2.936684140877327e-05,
                  "p99": 0.0001123835681937635
                },
                "candidate_energy": 0.6622974655311609,
                "cvrmse_percent": 52.607900600054855,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06555497817432485,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6627319192962098,
                "relative_energy_error_percent": 0.06555497817432483,
                "rms_normalized_rmse_percent": 2.7111306186272195,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -5.3581083193421364e-05,
                  "global_sensor_index": 82,
                  "local_sensor_index": 10,
                  "reference": 0.00029681401792913675,
                  "rgb_channel": 0,
                  "sky_patch_index": 104
                }
              }
            },
            "start_sensor_index": 72
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 335.41616692673415,
            "full": 9278.54870900046
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 328.74016696587205,
            "full": 9073.558083036914
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 321.22899999376386,
            "full": 9026.468332973309
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 330.95750003121793,
            "full": 8894.529332988895
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002575758844614029,
                  "p50": 0.0,
                  "p90": 1.6073405276983976e-05,
                  "p95": 6.786358135286718e-05,
                  "p99": 0.0001582549884915352
                },
                "candidate_energy": 23.999726398160533,
                "cvrmse_percent": 1.9417733284575203,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.01741452298276265,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.00390656398588,
                "relative_energy_error_percent": 0.01741452298276265,
                "rms_normalized_rmse_percent": 0.5389817151801878,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.026541675440967083,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.02628409955650568,
                  "rgb_channel": 0,
                  "sky_patch_index": 144
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00048410985618829727,
                  "p50": 1.4856923371553421e-05,
                  "p90": 6.904901238158345e-05,
                  "p95": 0.0001103232250898145,
                  "p99": 0.00023950997274369001
                },
                "candidate_energy": 10.002239398218293,
                "cvrmse_percent": 8.632570522223999,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.048683480540962575,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.9973723294057,
                "relative_energy_error_percent": 0.04868348054096257,
                "rms_normalized_rmse_percent": 0.9075980117422592,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.002277170307934284,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.0027612801641225815,
                  "rgb_channel": 0,
                  "sky_patch_index": 131
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 9.671843145042658e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.2160977348685265e-05
                },
                "candidate_energy": 0.9596419176154996,
                "cvrmse_percent": 7.8758969162881165,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.027906372948409836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9593741910757672,
                "relative_energy_error_percent": 0.027906372948409836,
                "rms_normalized_rmse_percent": 0.7271830444067953,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002236819011159241,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.0021401005797088146,
                  "rgb_channel": 0,
                  "sky_patch_index": 104
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00015282537788152695,
                  "p50": 2.5594567318876216e-06,
                  "p90": 1.5181796698016115e-05,
                  "p95": 2.3016103295958556e-05,
                  "p99": 4.4354397687129676e-05
                },
                "candidate_energy": 0.6485846917813092,
                "cvrmse_percent": 27.345760952538374,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3627702845001963,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.650946130912363,
                "relative_energy_error_percent": 0.3627702845001963,
                "rms_normalized_rmse_percent": 1.66218900209382,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002758312039077282,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.00012300582602620125,
                  "rgb_channel": 0,
                  "sky_patch_index": 121
                }
              }
            },
            "start_sensor_index": 36
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 9.862615843303502e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.602559647537336e-06,
                  "p99": 4.3377047404646873e-05
                },
                "candidate_energy": 2.0027786338425813,
                "cvrmse_percent": 5.928766097858843,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.022477458484550218,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.002328561271497,
                "relative_energy_error_percent": 0.022477458484550218,
                "rms_normalized_rmse_percent": 0.9579617657135246,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008702701015863568,
                  "global_sensor_index": 76,
                  "local_sensor_index": 4,
                  "reference": 0.0009688962600193918,
                  "rgb_channel": 0,
                  "sky_patch_index": 55
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0001183649874292314,
                  "p50": 2.8303193175815977e-06,
                  "p90": 1.1803331290138885e-05,
                  "p95": 1.815531686588656e-05,
                  "p99": 5.597504787147045e-05
                },
                "candidate_energy": 0.6631566134434834,
                "cvrmse_percent": 26.880972443559898,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.02446164253578765,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.662994434114978,
                "relative_energy_error_percent": 0.02446164253578765,
                "rms_normalized_rmse_percent": 1.3862044532699687,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 1.1706491932272911e-05,
                  "global_sensor_index": 79,
                  "local_sensor_index": 7,
                  "reference": 0.00013007147936150432,
                  "rgb_channel": 0,
                  "sky_patch_index": 53
                }
              }
            },
            "start_sensor_index": 72
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 541.6402079863474,
            "full": 15687.460041954182
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 550.5563749466091,
            "full": 15606.065374915488
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 543.3579579694197,
            "full": 15481.209042016417
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 582.4558750027791,
            "full": 15705.944458954036
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/atrium_borrowed_light/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 5526.1258750688285,
      "invocation_count": 7,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 19738.05858299602,
      "invocation_count": 7,
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
            "nmbe_percent": -0.5014828455718021,
            "cvrmse_percent": 46.79885001143938,
            "rms_normalized_rmse_percent": 4.9248010472362225,
            "reference_energy": 10.005843159853598,
            "candidate_energy": 9.955665572852112,
            "relative_energy_error_percent": 0.501482845571802,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.411307989154011e-05,
              "p90": 0.00016193697229027748,
              "p95": 0.0003075706044910474,
              "p99": 0.0009002778097055852,
              "maximum": 0.004217460751533508
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.006040031090378761,
              "candidate": 0.001822570338845253,
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
            "nmbe_percent": -1.1910809499673898,
            "cvrmse_percent": 9.945469000658235,
            "rms_normalized_rmse_percent": 3.5565156585261106,
            "reference_energy": 34.001622313405946,
            "candidate_energy": 33.596635467351106,
            "relative_energy_error_percent": 1.19108094996739,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.262918835389428e-05,
              "p90": 0.00012299686204642057,
              "p95": 0.00019352453527972063,
              "p99": 0.0006675765616819263,
              "maximum": 0.004217498004436493
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.02987241931259632,
              "candidate": 0.025654921308159828,
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
            "nmbe_percent": -1.2494162401177893,
            "cvrmse_percent": 37.20800007700976,
            "rms_normalized_rmse_percent": 2.267849670606277,
            "reference_energy": 0.6523523491557324,
            "candidate_energy": 0.6442017529625907,
            "relative_energy_error_percent": 1.2494162401177893,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.440114025783259e-06,
              "p90": 2.1804597054142505e-05,
              "p95": 2.9830084622517446e-05,
              "p99": 5.582875746767968e-05,
              "maximum": 0.0002239398891106248
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 4,
              "sky_patch_index": 103,
              "rgb_channel": 0,
              "reference": 0.0003177298931404948,
              "candidate": 9.379000402987003e-05,
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
            "nmbe_percent": -0.3087292868824078,
            "cvrmse_percent": 13.453290540249062,
            "rms_normalized_rmse_percent": 2.0228052598986404,
            "reference_energy": 1.609273455843974,
            "candidate_energy": 1.604305157379759,
            "relative_energy_error_percent": 0.30872928688240786,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.426946816238342e-06,
              "p90": 2.1435291273519397e-05,
              "p95": 2.9448497662087897e-05,
              "p99": 5.235912976786494e-05,
              "maximum": 0.0001151704927906394
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.0016022835625335574,
              "candidate": 0.0017174540553241968,
              "position": [
                6.5,
                3.5,
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
            "nmbe_percent": 0.29414644476937746,
            "cvrmse_percent": 36.693945721209,
            "rms_normalized_rmse_percent": 1.8765458274659819,
            "reference_energy": 0.6575587803084861,
            "candidate_energy": 0.6594929660830324,
            "relative_energy_error_percent": 0.29414644476937746,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.0958764152019285e-06,
              "p90": 2.075678639812395e-05,
              "p95": 2.9740237550868177e-05,
              "p99": 5.6874952861107886e-05,
              "maximum": 0.00015658466145396233
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 4,
              "sky_patch_index": 124,
              "rgb_channel": 0,
              "reference": -3.036484122276306e-05,
              "candidate": 0.00012621982023119926,
              "position": [
                6.5,
                1.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.027324642967461295,
            "cvrmse_percent": 8.194196537302371,
            "rms_normalized_rmse_percent": 1.6987766393298005,
            "reference_energy": 2.6656291223215565,
            "candidate_energy": 2.6649007486810454,
            "relative_energy_error_percent": 0.027324642967461298,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.068577022233512e-06,
              "p90": 2.0236535419826396e-05,
              "p95": 2.861465663954731e-05,
              "p99": 5.225231871008873e-05,
              "maximum": 0.00010662246495485306
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 4,
              "sky_patch_index": 124,
              "rgb_channel": 0,
              "reference": 0.003833521157503128,
              "candidate": 0.003940143622457981,
              "position": [
                6.5,
                1.5,
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
            "nmbe_percent": 87.10796228547301,
            "cvrmse_percent": 142.72167727987855,
            "rms_normalized_rmse_percent": 8.330947750592792,
            "reference_energy": 5.320813423034679,
            "candidate_energy": 9.955665572852112,
            "relative_energy_error_percent": 87.10796228547301,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0002499474212527275,
              "p90": 0.0006783403296140023,
              "p95": 0.0008601100082159971,
              "p99": 0.001422390341758728,
              "maximum": 0.004634765180526301
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 129,
              "rgb_channel": 0,
              "reference": -0.003944725176552311,
              "candidate": 0.0006900400039739907,
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
            "nmbe_percent": 14.599387290944001,
            "cvrmse_percent": 22.263044568765963,
            "rms_normalized_rmse_percent": 7.160189008111575,
            "reference_energy": 29.316592576587027,
            "candidate_energy": 33.596635467351106,
            "relative_energy_error_percent": 14.599387290944003,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0002497911482350901,
              "p90": 0.0006264375988394022,
              "p95": 0.0007781021937262263,
              "p99": 0.0012499447911977768,
              "maximum": 0.0037523750215768814
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.028459735214710236,
              "candidate": 0.024707360193133354,
              "position": [
                5.5,
                3.5,
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
            "nmbe_percent": 240.82378566081263,
            "cvrmse_percent": 425.30232147984947,
            "rms_normalized_rmse_percent": 7.728527621597641,
            "reference_energy": 0.18901314405435876,
            "candidate_energy": 0.6442017529625907,
            "relative_energy_error_percent": 240.82378566081263,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2996496408845815e-05,
              "p90": 8.032248388190055e-05,
              "p95": 0.00011664144476526399,
              "p99": 0.00018930970691144466,
              "maximum": 0.0004822826012969017
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 136,
              "rgb_channel": 0,
              "reference": -0.0001675821840763092,
              "candidate": 0.0003147004172205925,
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
            "nmbe_percent": 39.99975621115437,
            "cvrmse_percent": 70.1595115527314,
            "rms_normalized_rmse_percent": 7.729533093771796,
            "reference_energy": 1.1459342507426005,
            "candidate_energy": 1.604305157379759,
            "relative_energy_error_percent": 39.99975621115437,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.293346076636226e-05,
              "p90": 8.151822839863598e-05,
              "p95": 0.00011760599772969718,
              "p99": 0.00018951162110170117,
              "maximum": 0.0004825480282306671
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 136,
              "rgb_channel": 0,
              "reference": 0.010578273795545101,
              "candidate": 0.011060821823775768,
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
            "nmbe_percent": 714.2039415796768,
            "cvrmse_percent": 1176.8653274081582,
            "rms_normalized_rmse_percent": 7.66822371033612,
            "reference_energy": 0.08099849833734751,
            "candidate_energy": 0.6594929660830324,
            "relative_energy_error_percent": 714.2039415796768,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.180657384087681e-05,
              "p90": 9.18200021260418e-05,
              "p95": 0.00013712249347008757,
              "p99": 0.00024587754160165787,
              "maximum": 0.0004308554343879223
            },
            "worst": {
              "global_sensor_index": 88,
              "local_sensor_index": 16,
              "sky_patch_index": 80,
              "rgb_channel": 0,
              "reference": -0.00013867532834410667,
              "candidate": 0.0002921801060438156,
              "position": [
                8.5,
                1.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.564046584220666,
            "cvrmse_percent": 45.153708171227834,
            "rms_normalized_rmse_percent": 7.58817280001169,
            "reference_energy": 2.089068840350418,
            "candidate_energy": 2.6649007486810454,
            "relative_energy_error_percent": 27.564046584220662,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.1782429826089356e-05,
              "p90": 9.110209066420794e-05,
              "p95": 0.00013712249347008757,
              "p99": 0.00023517064983025193,
              "maximum": 0.00036650849506258965
            },
            "worst": {
              "global_sensor_index": 88,
              "local_sensor_index": 16,
              "sky_patch_index": 80,
              "rgb_channel": 0,
              "reference": 0.004040071740746498,
              "candidate": 0.004406580235809088,
              "position": [
                8.5,
                1.5,
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
      "bias_percent": -1.0728289246274196,
      "rms_normalized_error_percent": 2.0489856153399213,
      "absolute_error": {
        "p95": 0.554862224409032,
        "p99": 3.4795227229358208,
        "maximum": 3.87665748724816
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 21.14657546102794,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.0489856153399213
    },
    "overcast": {
      "bias_percent": -1.055434955189405,
      "rms_normalized_error_percent": 2.0580386648624684,
      "absolute_error": {
        "p95": 0.49255123138427676,
        "p99": 3.194809532165524,
        "maximum": 3.5210227966308594
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.537504196166992,
      "reference_fraction_of_uniform": 0.8766196370124817,
      "rms_normalized_to_uniform_percent": 1.836322595124746
    },
    "horizon": {
      "bias_percent": 3.3459603308353283,
      "rms_normalized_error_percent": 12.219467075874988,
      "absolute_error": {
        "p95": 0.02440351172932412,
        "p99": 0.04853829123226319,
        "maximum": 0.056344659726283025
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.06354849592949678,
      "reference_fraction_of_uniform": 0.0030051436009869976,
      "rms_normalized_to_uniform_percent": 0.03430269630024448
    },
    "north": {
      "bias_percent": -0.5741915354469552,
      "rms_normalized_error_percent": 1.4310197953404034,
      "absolute_error": {
        "p95": 0.09181481599807738,
        "p99": 0.29569646358489854,
        "maximum": 0.7504892349243164
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1883907318115234,
      "reference_fraction_of_uniform": 0.150775745511055,
      "rms_normalized_to_uniform_percent": 0.25293421309146263
    },
    "east": {
      "bias_percent": -0.28957070528271533,
      "rms_normalized_error_percent": 0.4564997773152399,
      "absolute_error": {
        "p95": 0.057621574401855453,
        "p99": 0.10460374832153307,
        "maximum": 0.12501144409179688
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1300718784332275,
      "reference_fraction_of_uniform": 0.14801789820194244,
      "rms_normalized_to_uniform_percent": 0.08360618439040085
    },
    "south": {
      "bias_percent": -1.035249920159033,
      "rms_normalized_error_percent": 1.9087394213489863,
      "absolute_error": {
        "p95": 0.15350756645202637,
        "p99": 0.5258926010131811,
        "maximum": 0.8626089096069336
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1850051879882812,
      "reference_fraction_of_uniform": 0.1506156474351883,
      "rms_normalized_to_uniform_percent": 0.3376338158551901
    },
    "west": {
      "bias_percent": -2.705287018247485,
      "rms_normalized_error_percent": 4.876132055381141,
      "absolute_error": {
        "p95": 0.29764752388000476,
        "p99": 1.5735355377197247,
        "maximum": 1.707204818725586
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.029035568237305,
      "reference_fraction_of_uniform": 0.1905289739370346,
      "rms_normalized_to_uniform_percent": 0.9259973023769823
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -1.5263497741953955,
          "cvrmse_percent": 6.092578778081561,
          "absolute_error_percentiles_lux": {
            "p50": 9.96856689453125,
            "p90": 85.98890380859376,
            "p95": 143.32258300781243,
            "p99": 387.17365722655785
          },
          "maximum_absolute_error_lux": 3558.783203125,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 32595.607421875,
            "radiance_lux": 36154.390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1983866057838664,
            "maximum_error_percentage_points": 1.0384931506849284,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10404629115826698,
            "maximum_error_percentage_points": 0.5565365728613045,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08315068493150671,
            "maximum_error_percentage_points": 0.7093150684931508,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.45457001522069995,
            "maximum_error_percentage_points": 1.645753424657535,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.49314687975646876,
            "maximum_error_percentage_points": 1.836164383561644,
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
          "nmbe_percent": -0.36202078992197906,
          "cvrmse_percent": 8.366031967534951,
          "absolute_error_percentiles_lux": {
            "p50": 0.8194808959960938,
            "p90": 10.257006835937503,
            "p95": 16.503919982910148,
            "p99": 34.09681945800774
          },
          "maximum_absolute_error_lux": 114.74078369140625,
          "worst": {
            "sensor_index": 4,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2603.5,
            "foton_lux": 395.2767028808594,
            "radiance_lux": 510.0174865722656
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.16168569254185688,
            "maximum_error_percentage_points": 2.328630136986301,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.31205065914340835,
            "maximum_error_percentage_points": 1.1644704597018674,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5832876712328776,
            "maximum_error_percentage_points": 3.3673972602739752,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5806925418569251,
            "maximum_error_percentage_points": 3.3673972602739726,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.005220700152207009,
            "maximum_error_percentage_points": 0.05726027397260269,
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
          "nmbe_percent": -0.019539654726387343,
          "cvrmse_percent": 3.306307006807593,
          "absolute_error_percentiles_lux": {
            "p50": 1.5205154418945312,
            "p90": 12.35450744628907,
            "p95": 18.42337646484374,
            "p99": 34.84953643798825
          },
          "maximum_absolute_error_lux": 106.14111328125,
          "worst": {
            "sensor_index": 2,
            "position": [
              6.5,
              3.5,
              3.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 631.4563598632812,
            "radiance_lux": 525.3152465820312
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3121727549467279,
            "maximum_error_percentage_points": 1.947123287671232,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.33116913718281354,
            "maximum_error_percentage_points": 1.076699277048185,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6763089802130902,
            "maximum_error_percentage_points": 2.878356164383561,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6748744292237436,
            "maximum_error_percentage_points": 2.878356164383561,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004901065449010598,
            "maximum_error_percentage_points": 0.03219178082191654,
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
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004999197345888717,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004989297945215299,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004915186215740164,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004999197345888717,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.00410958904109604,
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
      "study_preparation_seconds": 0.00845233304426074,
      "weather_seconds": 0.09274875000119209,
      "metric_reduction_seconds": 0.10079679207410663,
      "write_seconds": 0.06560212501790375,
      "total_seconds": 0.2592887500068173,
      "cold_end_to_end_seconds": 0.267741083051078,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02790116600226611,
      "engine_upload_seconds": 0.000312167,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07908341661095619,
      "engine_annual_reduction_seconds": 0.0009517499711364508,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07908341661095619
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00845233304426074,
      "weather_seconds": 0.09140012494754046,
      "metric_reduction_seconds": 0.015032833092845976,
      "write_seconds": 0.05036204098723829,
      "total_seconds": 0.15697683300822973,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15697683300822973,
      "raw_export_seconds": 0.027091083000414073,
      "engine_upload_seconds": 6.5375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0009219166822731495,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.016189167043194175,
      "full": 0.09383362508378923
    }
  },
  "elapsed_seconds": 1.1026049999054521,
  "result_class": "passed"
}
```
