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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "a6c529173dce23712275fa5cb81037c2986d8f829121827c1b65517fc24a79aa",
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
      "scene_fingerprint": 13086254370129758359,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 13086254370129758359,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "0cd01573c9c1b174028ec7b06d2071ffc5f0ec3d8c18ace10be2958f109d5480",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9c8ff7b285e183ba0928dcb0951c8cbb1b1f540858e87be7f2de7d3272b7001e",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00024381768889725208,
          "p95": 6.735310307703912e-06,
          "p99": 8.77203419804573e-05
        },
        "bias_percent": -0.07672382825287284,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0908881235476013,
        "worst_index": [
          33,
          528,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 7.613853085786104e-05,
          "p95": 0.0,
          "p99": 3.562308847904205e-08
        },
        "bias_percent": 0.2312468068990563,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.278655093290519,
        "worst_index": [
          4,
          502,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.24473099783063e-05,
          "p95": 0.0,
          "p99": 9.63243655860424e-06
        },
        "bias_percent": 0.23460445669819746,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3484971770294452,
        "worst_index": [
          4,
          333,
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
          "maximum": 0.00030881352722644806,
          "p95": 5.561196303460747e-05,
          "p99": 0.00012588943354785442
        },
        "bias_percent": 0.023586178416721792,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8624308708391502,
        "worst_index": [
          14,
          562,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.404464460909367e-05,
          "p95": 1.1269470633124001e-05,
          "p99": 2.1982552425470203e-05
        },
        "bias_percent": -0.0918503157705478,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.12789936962029,
        "worst_index": [
          1,
          420,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00016575888730585575,
          "p95": 8.869004886946641e-06,
          "p99": 3.43486899510026e-05
        },
        "bias_percent": 0.05754685243061315,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.19971945536962,
        "worst_index": [
          4,
          375,
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
          "maximum": 0.0003014621324837208,
          "p95": 4.739157157018781e-05,
          "p99": 0.00010914914309978485
        },
        "bias_percent": -0.010800368496049087,
        "identifier": "atrium_borrowed_light_atrium_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5929374079560554,
        "worst_index": [
          20,
          553,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 9.290128946304321e-05,
          "p95": 9.748619049787521e-06,
          "p99": 1.892564796435181e-05
        },
        "bias_percent": 0.12320772062389788,
        "identifier": "atrium_borrowed_light_office_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.8155481381822396,
        "worst_index": [
          2,
          420,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00010642874985933304,
          "p95": 7.637206181243528e-06,
          "p99": 2.6695779524743557e-05
        },
        "bias_percent": 0.011384140314908536,
        "identifier": "atrium_borrowed_light_office_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.4691314001839513,
        "worst_index": [
          4,
          375,
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006589035037904978,
                  "p50": 0.0,
                  "p90": 3.740469310287494e-06,
                  "p95": 0.0001347479410469532,
                  "p99": 0.00031988765113055706
                },
                "candidate_energy": 23.9984715155922,
                "cvrmse_percent": 15.619657196486004,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.008547005111096465,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.000522841506154,
                "relative_energy_error_percent": 0.008547005111096465,
                "rms_normalized_rmse_percent": 4.325983545755472,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007859374396502972,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.007200470892712474,
                  "rgb_channel": 0,
                  "sky_patch_index": 520
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009768621530383825,
                  "p50": 1.1651773093035445e-05,
                  "p90": 7.202065173714817e-05,
                  "p95": 0.00017571619537193328,
                  "p99": 0.0004433852154761553
                },
                "candidate_energy": 5.307059495916892,
                "cvrmse_percent": 104.25939724727817,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04590753399481915,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.3094969550364794,
                "relative_energy_error_percent": 0.04590753399481916,
                "rms_normalized_rmse_percent": 6.069571093652531,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 4.623527638614178e-05,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0010230974294245243,
                  "rgb_channel": 0,
                  "sky_patch_index": 505
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
                  "maximum": 0.00024349353043362498,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.423534169793129e-06
                },
                "candidate_energy": 0.9591173810713371,
                "cvrmse_percent": 64.00115977277584,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.003309244188176544,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9591491216579016,
                "relative_energy_error_percent": 0.003309244188176544,
                "rms_normalized_rmse_percent": 5.596538858119768,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001559119496960193,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": 0.001802613027393818,
                  "rgb_channel": 0,
                  "sky_patch_index": 372
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003903075121343136,
                  "p50": 0.0,
                  "p90": 1.2873515061073705e-05,
                  "p95": 2.1662885046680458e-05,
                  "p99": 4.860252374783158e-05
                },
                "candidate_energy": 0.18859941879821918,
                "cvrmse_percent": 518.8844981327568,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.2548278837895626,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.1862621494104708,
                "relative_energy_error_percent": 1.2548278837895626,
                "rms_normalized_rmse_percent": 8.80050196638742,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00017161201685667038,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": -0.0002186954952776432,
                  "rgb_channel": 0,
                  "sky_patch_index": 372
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
                  "maximum": 0.0002853046462405473,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.724334500380792e-05
                },
                "candidate_energy": 2.0041293322492493,
                "cvrmse_percent": 45.81882188272973,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.08316325881404958,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.002464017915372,
                "relative_energy_error_percent": 0.08316325881404958,
                "rms_normalized_rmse_percent": 6.692673570999817,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009206833492498845,
                  "global_sensor_index": 89,
                  "local_sensor_index": 17,
                  "reference": 0.0006353787030093372,
                  "rgb_channel": 0,
                  "sky_patch_index": 280
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00041103234980255365,
                  "p50": 0.0,
                  "p90": 8.893121389519367e-06,
                  "p95": 1.5126799780773581e-05,
                  "p99": 0.00011387759877834469
                },
                "candidate_energy": 0.08252602496470018,
                "cvrmse_percent": 1569.521675908054,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -2.749537770719227,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.08485926243736941,
                "relative_energy_error_percent": 2.749537770719227,
                "rms_normalized_rmse_percent": 9.713304312627685,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 9.757594671100378e-05,
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "reference": -0.0003134564030915499,
                  "rgb_channel": 0,
                  "sky_patch_index": 371
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.68112500105053,
            "full": 694.7880419902503
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.93770890124142,
            "full": 715.1167499832809
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.51729198172688,
            "full": 717.8521250607446
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.0564159201458,
            "full": 712.3299170052633
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003592169377952814,
                  "p50": 0.0,
                  "p90": 1.7268859664909702e-06,
                  "p95": 6.680960359517485e-05,
                  "p99": 0.00016141333617269993
                },
                "candidate_energy": 23.999884621907086,
                "cvrmse_percent": 8.119167813322909,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.005802636402371932,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.0012773287624,
                "relative_energy_error_percent": 0.005802636402371932,
                "rms_normalized_rmse_percent": 2.248719492327906,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005039713112637401,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.005398930050432682,
                  "rgb_channel": 0,
                  "sky_patch_index": 437
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005431189201772213,
                  "p50": 1.0450772606418468e-05,
                  "p90": 5.234359996393328e-05,
                  "p95": 0.00010042148642241955,
                  "p99": 0.00024848151952028275
                },
                "candidate_energy": 9.994167869883732,
                "cvrmse_percent": 32.169640863761,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05258801495690834,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.988914897823232,
                "relative_energy_error_percent": 0.05258801495690835,
                "rms_normalized_rmse_percent": 3.3818036958405857,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.000603624852374196,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0011467437725514174,
                  "rgb_channel": 0,
                  "sky_patch_index": 468
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
                  "maximum": 0.00013161147944629192,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.495415724813938e-06
                },
                "candidate_energy": 0.9596995605625125,
                "cvrmse_percent": 33.29850538845168,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.020513346557273583,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9598964674514718,
                "relative_energy_error_percent": 0.020513346557273587,
                "rms_normalized_rmse_percent": 2.91049124064733,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022031499538570642,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.0020715384744107723,
                  "rgb_channel": 0,
                  "sky_patch_index": 418
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00020870956359431148,
                  "p50": 1.618645455891965e-06,
                  "p90": 1.0898436266870723e-05,
                  "p95": 1.6213464732572902e-05,
                  "p99": 3.369020032550907e-05
                },
                "candidate_energy": 0.6482825961934466,
                "cvrmse_percent": 94.08045656223774,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.41946969659016026,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6510134001277237,
                "relative_energy_error_percent": 0.41946969659016026,
                "rms_normalized_rmse_percent": 5.4256190302256915,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -7.155252387747169e-05,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": 0.0001371570397168398,
                  "rgb_channel": 0,
                  "sky_patch_index": 420
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
                  "maximum": 0.00016767502529546618,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.729302600026131e-05
                },
                "candidate_energy": 2.0017531659009364,
                "cvrmse_percent": 27.317576202540348,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.008316436308611359,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0019196542739337,
                "relative_energy_error_percent": 0.008316436308611357,
                "rms_normalized_rmse_percent": 3.9948783219568766,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014343925286084414,
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "reference": 0.0012667175033129752,
                  "rgb_channel": 0,
                  "sky_patch_index": 320
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002822850365191698,
                  "p50": 1.7940564021046157e-06,
                  "p90": 8.417613321398677e-06,
                  "p95": 1.3041010106462636e-05,
                  "p99": 7.165926945162937e-05
                },
                "candidate_energy": 0.6625140303795618,
                "cvrmse_percent": 133.08923442961134,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.051133408277695865,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6621754375095854,
                "relative_energy_error_percent": 0.051133408277695865,
                "rms_normalized_rmse_percent": 6.23389373210786,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00012645754031836987,
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "reference": 0.00015582749620079994,
                  "rgb_channel": 0,
                  "sky_patch_index": 462
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 359.69724995084107,
            "full": 9158.725249930285
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 352.4305409519002,
            "full": 9217.473166063428
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 350.5826670443639,
            "full": 9360.374041949399
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 342.7889159647748,
            "full": 9471.681958064437
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000417372677475214,
                  "p50": 0.0,
                  "p90": 2.9703001018788594e-06,
                  "p95": 6.943685002624989e-05,
                  "p99": 0.00018383609130978584
                },
                "candidate_energy": 23.990504287707495,
                "cvrmse_percent": 8.874821134387764,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.05254409386265656,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 24.003116507775303,
                "relative_energy_error_percent": 0.05254409386265656,
                "rms_normalized_rmse_percent": 2.4569876685394547,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037658039946109056,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.00418317667208612,
                  "rgb_channel": 0,
                  "sky_patch_index": 391
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006397718098014593,
                  "p50": 1.041966061166022e-05,
                  "p90": 5.3022638894617585e-05,
                  "p95": 0.0001051807776093483,
                  "p99": 0.0002675925243238453
                },
                "candidate_energy": 10.007089586494484,
                "cvrmse_percent": 34.605263737246375,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0752065943113248,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.999569251014993,
                "relative_energy_error_percent": 0.0752065943113248,
                "rms_normalized_rmse_percent": 3.640897530830296,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008448283188045025,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.00020505650900304317,
                  "rgb_channel": 0,
                  "sky_patch_index": 522
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
                  "maximum": 0.00014435802586376667,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.3489777706563473e-06
                },
                "candidate_energy": 0.9610682728093707,
                "cvrmse_percent": 32.646760370974675,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0210190658269295,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9612703228513055,
                "relative_energy_error_percent": 0.0210190658269295,
                "rms_normalized_rmse_percent": 2.859091045158556,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020981449633836746,
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "reference": 0.0022425029892474413,
                  "rgb_channel": 0,
                  "sky_patch_index": 423
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002709140535444021,
                  "p50": 1.5848896737225004e-06,
                  "p90": 1.0619024124025615e-05,
                  "p95": 1.5848479506530566e-05,
                  "p99": 3.3854577850434e-05
                },
                "candidate_energy": 0.6436464440333509,
                "cvrmse_percent": 97.94567711075277,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.9699146943744895,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6499504085520442,
                "relative_energy_error_percent": 0.9699146943744895,
                "rms_normalized_rmse_percent": 5.651363212328669,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00010905542876571417,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.00016185862477868795,
                  "rgb_channel": 0,
                  "sky_patch_index": 458
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
                  "maximum": 0.0001846480299718678,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6297500375658274e-05
                },
                "candidate_energy": 2.0054067765281616,
                "cvrmse_percent": 27.042215859897134,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.20876431898543793,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0012289245923967,
                "relative_energy_error_percent": 0.20876431898543793,
                "rms_normalized_rmse_percent": 3.9609163412177235,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019989944994449615,
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "reference": 0.0018143464694730937,
                  "rgb_channel": 0,
                  "sky_patch_index": 321
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00028278952231630683,
                  "p50": 1.8190667105955072e-06,
                  "p90": 8.150861185640693e-06,
                  "p95": 1.2582739145727828e-05,
                  "p99": 6.660650251433253e-05
                },
                "candidate_energy": 0.6611276558605148,
                "cvrmse_percent": 129.11230315873803,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.38235772568398446,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6636652311444742,
                "relative_energy_error_percent": 0.38235772568398446,
                "rms_normalized_rmse_percent": 6.068758211012238,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -9.014899842441082e-05,
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "reference": 0.000192640523891896,
                  "rgb_channel": 0,
                  "sky_patch_index": 321
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 347.87625004537404,
            "full": 9607.467833091505
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 346.7637080466375,
            "full": 9687.64525000006
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 344.8923750547692,
            "full": 9707.94674998615
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 350.2853329991922,
            "full": 9589.806457981467
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023307651281356812,
                  "p50": 0.0,
                  "p90": 2.928759022324897e-06,
                  "p95": 4.082685336470604e-05,
                  "p99": 0.00011592172086238861
                },
                "candidate_energy": 24.0016749806573,
                "cvrmse_percent": 5.509531678460599,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.007937461665711147,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.999770008113046,
                "relative_energy_error_percent": 0.007937461665711147,
                "rms_normalized_rmse_percent": 1.5262099073608952,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005182820605114102,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.004949744092300534,
                  "rgb_channel": 0,
                  "sky_patch_index": 536
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003816550597548485,
                  "p50": 7.648083737876732e-06,
                  "p90": 3.669978032121437e-05,
                  "p95": 6.674560427200049e-05,
                  "p99": 0.00016470649279654026
                },
                "candidate_energy": 9.997437688623108,
                "cvrmse_percent": 21.691613990937636,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.03387041956384385,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.994052661055377,
                "relative_energy_error_percent": 0.03387041956384386,
                "rms_normalized_rmse_percent": 2.2825650080912103,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002930059563368559,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0006746610160917044,
                  "rgb_channel": 0,
                  "sky_patch_index": 528
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
                  "maximum": 8.489214815199375e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.865776307065971e-06
                },
                "candidate_energy": 0.9588534371594051,
                "cvrmse_percent": 15.936888308127754,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.05012488692035632,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9583730537499378,
                "relative_energy_error_percent": 0.050124886920356326,
                "rms_normalized_rmse_percent": 1.3937061847871444,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0024849900510162115,
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "reference": 0.0024000979028642178,
                  "rgb_channel": 0,
                  "sky_patch_index": 496
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 9.186449460685253e-05,
                  "p50": 1.2467524683756892e-06,
                  "p90": 7.507811051254995e-06,
                  "p95": 1.1219396128581138e-05,
                  "p99": 2.2847956188343232e-05
                },
                "candidate_energy": 0.6501761683330258,
                "cvrmse_percent": 56.31474728937116,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.35539175360859454,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6524950820473236,
                "relative_energy_error_percent": 0.35539175360859454,
                "rms_normalized_rmse_percent": 3.2604788557144575,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00011516897939145565,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 2.330448478460312e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 455
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
                  "maximum": 8.474104106426239e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.8311507776379585e-05
                },
                "candidate_energy": 2.004895742009694,
                "cvrmse_percent": 15.829253822308031,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.048405773273852766,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0039257262660612,
                "relative_energy_error_percent": 0.04840577327385277,
                "rms_normalized_rmse_percent": 2.320343381203914,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002165416022762656,
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "reference": 0.0022501570638269186,
                  "rgb_channel": 0,
                  "sky_patch_index": 420
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00013567355927079916,
                  "p50": 1.333364480160526e-06,
                  "p90": 5.859847908595852e-06,
                  "p95": 9.061667583409871e-06,
                  "p99": 3.965426003560424e-05
                },
                "candidate_energy": 0.659860093125431,
                "cvrmse_percent": 75.80652231466244,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5266984122242544,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6633539679420082,
                "relative_energy_error_percent": 0.5266984122242545,
                "rms_normalized_rmse_percent": 3.5609160465649587,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 2.9561459086835384e-05,
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "reference": 0.00016523501835763454,
                  "rgb_channel": 0,
                  "sky_patch_index": 324
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 620.3580000437796,
            "full": 16717.105332994834
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 616.0649160156026,
            "full": 16759.292916976847
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 600.5141669884324,
            "full": 16650.518542039208
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 604.652333073318,
            "full": 16938.82195802871
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/atrium_borrowed_light/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 19922.123749973252,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 75432.99433297943,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432113396211864,
            "cvrmse_percent": 14.465039897215688,
            "rms_normalized_rmse_percent": 4.045788043894173,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095340172731,
            "relative_energy_error_percent": 1.5432113396211864,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.190951585769653e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4260345487303969,
            "cvrmse_percent": 50.39955836011209,
            "rms_normalized_rmse_percent": 5.303436499591062,
            "reference_energy": 9.995122800852522,
            "candidate_energy": 9.95254012453286,
            "relative_energy_error_percent": 0.4260345487304148,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.128927558776923e-06,
              "p90": 3.793557989411058e-05,
              "p95": 7.139763329178095e-05,
              "p99": 0.0003670858422992751,
              "maximum": 0.0012632953003048897
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 525,
              "rgb_channel": 0,
              "reference": 0.0015035350807011127,
              "candidate": 0.00024023978039622307,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.2147560624185738,
            "cvrmse_percent": 10.803872243006223,
            "rms_normalized_rmse_percent": 3.866835910476664,
            "reference_energy": 33.9964676783916,
            "candidate_energy": 33.58349352626017,
            "relative_energy_error_percent": 1.2147560624185738,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.839349902700633e-06,
              "p90": 3.316752554383136e-05,
              "p95": 5.016103386878967e-05,
              "p99": 0.00019922027422580868,
              "maximum": 0.0012632994912564754
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 525,
              "rgb_channel": 0,
              "reference": 0.007855508476495743,
              "candidate": 0.006592208985239267,
              "position": [
                5.5,
                2.5,
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
            "nmbe_percent": 0.02233557112297189,
            "cvrmse_percent": 8.364121714247426,
            "rms_normalized_rmse_percent": 0.7313982468164603,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410387681914,
            "relative_energy_error_percent": 0.02233557112297189,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.44783047391948777,
            "cvrmse_percent": 40.4617980815713,
            "rms_normalized_rmse_percent": 2.3377587192665104,
            "reference_energy": 0.6511219889988507,
            "candidate_energy": 0.6482060663097231,
            "relative_energy_error_percent": 0.44783047391948777,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2189741624979433e-06,
              "p90": 6.296409719652732e-06,
              "p95": 8.836025699565653e-06,
              "p99": 1.532084570499137e-05,
              "maximum": 5.240144673734903e-05
            },
            "worst": {
              "global_sensor_index": 44,
              "local_sensor_index": 8,
              "sky_patch_index": 372,
              "rgb_channel": 0,
              "reference": -2.3861415684223175e-05,
              "candidate": 2.854003105312586e-05,
              "position": [
                7.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.1678167103775011,
            "cvrmse_percent": 16.030661614597285,
            "rms_normalized_rmse_percent": 2.290106476054981,
            "reference_energy": 1.6099488683074679,
            "candidate_energy": 1.6072471050779145,
            "relative_energy_error_percent": 0.1678167103775011,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2175280517112697e-06,
              "p90": 6.289653174462728e-06,
              "p95": 8.794281711743679e-06,
              "p99": 1.4869618098600768e-05,
              "maximum": 5.006091669201851e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 462,
              "rgb_channel": 0,
              "reference": 0.0019606510177254677,
              "candidate": 0.002010711934417486,
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
            "nmbe_percent": -0.037030330449992516,
            "cvrmse_percent": 4.693534946357391,
            "rms_normalized_rmse_percent": 0.688252500306755,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.003413624681116,
            "relative_energy_error_percent": 0.037030330449992516,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.0045628928313961245,
            "cvrmse_percent": 41.27303332052324,
            "rms_normalized_rmse_percent": 1.935046799367487,
            "reference_energy": 0.6618619960734566,
            "candidate_energy": 0.6618317960198841,
            "relative_energy_error_percent": 0.0045628928313961245,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5324274045269703e-06,
              "p90": 5.8398476539878195e-06,
              "p95": 8.184072612493765e-06,
              "p99": 1.7716836737236008e-05,
              "maximum": 5.4049771279096603e-05
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 1,
              "sky_patch_index": 419,
              "rgb_channel": 0,
              "reference": -5.5998098105192184e-06,
              "candidate": 4.8449961468577385e-05,
              "position": [
                6.5,
                4.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.028970007918913417,
            "cvrmse_percent": 10.057684112717169,
            "rms_normalized_rmse_percent": 1.8994097837746244,
            "reference_energy": 2.6660177662590048,
            "candidate_energy": 2.665245420701,
            "relative_energy_error_percent": 0.028970007918913413,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5345922292908654e-06,
              "p90": 5.835883530380672e-06,
              "p95": 8.142264505295316e-06,
              "p99": 1.714145764708519e-05,
              "maximum": 5.405792035162449e-05
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 1,
              "sky_patch_index": 419,
              "rgb_channel": 0,
              "reference": 0.002164057921618223,
              "candidate": 0.0022181158419698477,
              "position": [
                6.5,
                4.5,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432113396211864,
            "cvrmse_percent": 14.465039897215688,
            "rms_normalized_rmse_percent": 4.045788043894173,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095340172731,
            "relative_energy_error_percent": 1.5432113396211864,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.190951585769653e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.55621238407682,
            "cvrmse_percent": 150.3809831868478,
            "rms_normalized_rmse_percent": 8.75106556499238,
            "reference_energy": 5.306430535157157,
            "candidate_energy": 9.95254012453286,
            "relative_energy_error_percent": 87.55621238407679,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.438493437599391e-05,
              "p90": 0.00016575575245951802,
              "p95": 0.00022738341067451984,
              "p99": 0.00044415146112442017,
              "maximum": 0.001364411917165853
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": -0.0011848119174828753,
              "candidate": 0.0001795999996829778,
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
            "nmbe_percent": 14.589023060793876,
            "cvrmse_percent": 23.38135239347973,
            "rms_normalized_rmse_percent": 7.514810208937475,
            "reference_energy": 29.30777541269624,
            "candidate_energy": 33.58349352626017,
            "relative_energy_error_percent": 14.589023060793865,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.390521593857557e-05,
              "p90": 0.00015437536585523052,
              "p95": 0.000198041379917413,
              "p99": 0.00036778347566723824,
              "maximum": 0.0011332486756145954
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 521,
              "rgb_channel": 0,
              "reference": 0.007746007759124041,
              "candidate": 0.006612759083509445,
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
            "nmbe_percent": 0.02233557112297189,
            "cvrmse_percent": 8.364121714247426,
            "rms_normalized_rmse_percent": 0.7313982468164603,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410387681914,
            "relative_energy_error_percent": 0.02233557112297189,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 245.27318860826452,
            "cvrmse_percent": 466.7790361778598,
            "rms_normalized_rmse_percent": 7.973620559601693,
            "reference_energy": 0.1877371564593613,
            "candidate_energy": 0.6482060663097231,
            "relative_energy_error_percent": 245.27318860826452,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.849999757221667e-06,
              "p90": 2.1067330590085516e-05,
              "p95": 2.9779440410493407e-05,
              "p99": 5.0725182518363e-05,
              "maximum": 0.0002251656260341406
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 496,
              "rgb_channel": 0,
              "reference": -0.00017389561980962753,
              "candidate": 5.1270006224513054e-05,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 40.179445276370146,
            "cvrmse_percent": 76.35769024852702,
            "rms_normalized_rmse_percent": 7.966087723621797,
            "reference_energy": 1.1465640357679785,
            "candidate_energy": 1.6072471050779145,
            "relative_energy_error_percent": 40.17944527637015,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.849999757221667e-06,
              "p90": 2.105999919876922e-05,
              "p95": 2.9769998945994303e-05,
              "p99": 5.0549999286886305e-05,
              "maximum": 0.00022516888566315174
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 496,
              "rgb_channel": 0,
              "reference": 0.002272009151056409,
              "candidate": 0.0024971780367195606,
              "position": [
                6.5,
                2.5,
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
            "nmbe_percent": -0.037030330449992516,
            "cvrmse_percent": 4.693534946357391,
            "rms_normalized_rmse_percent": 0.688252500306755,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.003413624681116,
            "relative_energy_error_percent": 0.037030330449992516,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 698.9900012731094,
            "cvrmse_percent": 1289.786932566637,
            "rms_normalized_rmse_percent": 7.793238364592926,
            "reference_energy": 0.08283355172972406,
            "candidate_energy": 0.6618317960198841,
            "relative_energy_error_percent": 698.9900012731094,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.650771015552891e-06,
              "p90": 2.2856999930809295e-05,
              "p95": 3.591000131564215e-05,
              "p99": 7.190000178525224e-05,
              "maximum": 0.00018819852266460657
            },
            "worst": {
              "global_sensor_index": 81,
              "local_sensor_index": 9,
              "sky_patch_index": 375,
              "rgb_channel": 0,
              "reference": -0.00013227853924036026,
              "candidate": 5.591998342424631e-05,
              "position": [
                7.5,
                2.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.70766925894237,
            "cvrmse_percent": 50.94010630032886,
            "rms_normalized_rmse_percent": 7.754856712877903,
            "reference_energy": 2.086989321915272,
            "candidate_energy": 2.665245420701,
            "relative_energy_error_percent": 27.70766925894237,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.657763438193797e-06,
              "p90": 2.2876999719301282e-05,
              "p95": 3.591441782191396e-05,
              "p99": 7.108342833817005e-05,
              "maximum": 0.00017331750132143497
            },
            "worst": {
              "global_sensor_index": 81,
              "local_sensor_index": 9,
              "sky_patch_index": 375,
              "rgb_channel": 0,
              "reference": 0.00115746830124408,
              "candidate": 0.001330785802565515,
              "position": [
                7.5,
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
      "bias_percent": -1.08805492399663,
      "rms_normalized_error_percent": 2.045058392585892,
      "absolute_error": {
        "p95": 0.5684094481253785,
        "p99": 3.6105996096029114,
        "maximum": 3.7529064644584196
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 21.144326002186634,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.045058392585892
    },
    "overcast": {
      "bias_percent": -1.0679698906017683,
      "rms_normalized_error_percent": 2.0500837467349355,
      "absolute_error": {
        "p95": 0.47602653503417947,
        "p99": 3.291003189086909,
        "maximum": 3.4175491333007812
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.614978790283203,
      "reference_fraction_of_uniform": 0.8803770542144775,
      "rms_normalized_to_uniform_percent": 1.8366194703256264
    },
    "horizon": {
      "bias_percent": -0.3888115612273396,
      "rms_normalized_error_percent": 5.155775143250021,
      "absolute_error": {
        "p95": 0.00827854535663638,
        "p99": 0.011862024491607497,
        "maximum": 0.015007926487461493
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.04851970585714961,
      "reference_fraction_of_uniform": 0.002294691533422818,
      "rms_normalized_to_uniform_percent": 0.011210341513714877
    },
    "north": {
      "bias_percent": -0.6387012666344366,
      "rms_normalized_error_percent": 1.4881466487392134,
      "absolute_error": {
        "p95": 0.09634819030761711,
        "p99": 0.3817811441421494,
        "maximum": 0.7343606948852539
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1402947902679443,
      "reference_fraction_of_uniform": 0.14851714670658112,
      "rms_normalized_to_uniform_percent": 0.2607326596490632
    },
    "east": {
      "bias_percent": -0.3009179914559901,
      "rms_normalized_error_percent": 0.40453981564921015,
      "absolute_error": {
        "p95": 0.060279011726379346,
        "p99": 0.09097024917602531,
        "maximum": 0.1020212173461914
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.016392946243286,
      "reference_fraction_of_uniform": 0.1426573246717453,
      "rms_normalized_to_uniform_percent": 0.07224114271491913
    },
    "south": {
      "bias_percent": -0.9663555828945516,
      "rms_normalized_error_percent": 1.668545281728552,
      "absolute_error": {
        "p95": 0.14594149589538566,
        "p99": 0.4221891117095931,
        "maximum": 0.752924919128418
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.155980110168457,
      "reference_fraction_of_uniform": 0.14925897121429443,
      "rms_normalized_to_uniform_percent": 0.29349748503950823
    },
    "west": {
      "bias_percent": -2.7309572558517536,
      "rms_normalized_error_percent": 4.861339076875757,
      "absolute_error": {
        "p95": 0.30513753890991174,
        "p99": 1.6035560894012428,
        "maximum": 1.6567554473876953
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.025930404663086,
      "reference_fraction_of_uniform": 0.19040240347385406,
      "rms_normalized_to_uniform_percent": 0.9200694806326136
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
          "nmbe_percent": -1.4795641806228894,
          "cvrmse_percent": 6.739322516129395,
          "absolute_error_percentiles_lux": {
            "p50": 9.425827026367188,
            "p90": 73.83997802734376,
            "p95": 115.83328857421846,
            "p99": 377.87192138671577
          },
          "maximum_absolute_error_lux": 4749.865234375,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 32200.673828125,
            "radiance_lux": 36950.5390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.19729832572298475,
            "maximum_error_percentage_points": 1.091095890410955,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10200365168377938,
            "maximum_error_percentage_points": 0.523418027799508,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0909855403348555,
            "maximum_error_percentage_points": 0.657123287671233,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4290677321156764,
            "maximum_error_percentage_points": 2.1373972602739713,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.49536529680365315,
            "maximum_error_percentage_points": 2.6035616438356164,
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
          "nmbe_percent": -0.1673399891414521,
          "cvrmse_percent": 8.910494489894452,
          "absolute_error_percentiles_lux": {
            "p50": 0.6442298889160156,
            "p90": 9.57311172485352,
            "p95": 15.879172515869115,
            "p99": 34.65174148559564
          },
          "maximum_absolute_error_lux": 155.26953125,
          "worst": {
            "sensor_index": 1,
            "position": [
              6.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3830.5,
            "foton_lux": 16568.10546875,
            "radiance_lux": 16412.8359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.12166286149162867,
            "maximum_error_percentage_points": 1.6999999999999993,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.27292006025377147,
            "maximum_error_percentage_points": 1.355904397392969,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.578226788432268,
            "maximum_error_percentage_points": 2.548767123287675,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5759018264840179,
            "maximum_error_percentage_points": 2.5487671232876714,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0024543378995434007,
            "maximum_error_percentage_points": 0.08150684931506902,
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
          "nmbe_percent": 0.07025989588249905,
          "cvrmse_percent": 2.9629903177567347,
          "absolute_error_percentiles_lux": {
            "p50": 1.1652603149414062,
            "p90": 10.87661476135254,
            "p95": 16.167645263671865,
            "p99": 31.67469726562493
          },
          "maximum_absolute_error_lux": 146.5654296875,
          "worst": {
            "sensor_index": 9,
            "position": [
              7.5,
              2.5,
              3.75
            ],
            "hour_of_year": 4455.5,
            "foton_lux": 6130.18408203125,
            "radiance_lux": 5983.61865234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20619482496194808,
            "maximum_error_percentage_points": 0.8190410958904053,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2101882573912189,
            "maximum_error_percentage_points": 0.5901937166183053,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6032686453576868,
            "maximum_error_percentage_points": 3.0445205479452113,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6080707762557077,
            "maximum_error_percentage_points": 3.044520547945204,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007777777777777788,
            "maximum_error_percentage_points": 0.052054794520548064,
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
      "maximum_error_percentage_points": 0.004989833047943648,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004794520547945158,
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
            "maximum_error_percentage_points": 0.004893514554794365,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004989833047943648,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.0049855522260315865,
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
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004383561643835243,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
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
      "study_preparation_seconds": 0.33903447299962863,
      "weather_seconds": 0.2295989029989869,
      "metric_reduction_seconds": 2.8967495110009622,
      "write_seconds": 0.039390142999764066,
      "total_seconds": 3.166127876000246,
      "cold_end_to_end_seconds": 3.5051623489998747,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.023164498001278844,
      "engine_upload_seconds": 0.04507919,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.120295987,
      "engine_annual_reduction_seconds": 0.056443603,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.120295987
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.33903447299962863,
      "weather_seconds": 0.2338796160001948,
      "metric_reduction_seconds": 2.810142417001771,
      "write_seconds": 0.040518052999686915,
      "total_seconds": 3.0849196369999845,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 3.0849196369999845,
      "raw_export_seconds": 0.023054326000419678,
      "engine_upload_seconds": 0.045423005,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5e-08,
      "engine_annual_reduction_seconds": 0.056997165,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.024892355999327265,
      "full": 0.15927995099991676
    }
  },
  "elapsed_seconds": 11.20147273999828,
  "result_class": "passed"
}
```
