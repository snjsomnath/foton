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
  "model_sha256": "0cd01573c9c1b174028ec7b06d2071ffc5f0ec3d8c18ace10be2958f109d5480",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 13086254370129758359,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": -0.07672382825287284,
        "rms_normalized_error_percent": 1.0908881235476013,
        "absolute_error": {
          "p95": 6.735310307703912e-06,
          "p99": 8.77203419804573e-05,
          "maximum": 0.00024381768889725208
        },
        "worst_index": [
          33,
          528,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.2312468068990563,
        "rms_normalized_error_percent": 1.278655093290519,
        "absolute_error": {
          "p95": 0.0,
          "p99": 3.562308847904205e-08,
          "maximum": 7.613853085786104e-05
        },
        "worst_index": [
          4,
          502,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.23460445669819746,
        "rms_normalized_error_percent": 1.3484971770294452,
        "absolute_error": {
          "p95": 0.0,
          "p99": 9.63243655860424e-06,
          "maximum": 8.24473099783063e-05
        },
        "worst_index": [
          4,
          333,
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
        "bias_percent": 0.023586178416721792,
        "rms_normalized_error_percent": 1.8624308708391502,
        "absolute_error": {
          "p95": 5.561196303460747e-05,
          "p99": 0.00012588943354785442,
          "maximum": 0.00030881352722644806
        },
        "worst_index": [
          14,
          562,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": -0.0918503157705478,
        "rms_normalized_error_percent": 3.12789936962029,
        "absolute_error": {
          "p95": 1.1269470633124001e-05,
          "p99": 2.1982552425470203e-05,
          "maximum": 8.404464460909367e-05
        },
        "worst_index": [
          1,
          420,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.05754685243061315,
        "rms_normalized_error_percent": 3.19971945536962,
        "absolute_error": {
          "p95": 8.869004886946641e-06,
          "p99": 3.43486899510026e-05,
          "maximum": 0.00016575888730585575
        },
        "worst_index": [
          4,
          375,
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
        "bias_percent": -0.010800368496049087,
        "rms_normalized_error_percent": 1.5929374079560554,
        "absolute_error": {
          "p95": 4.739157157018781e-05,
          "p99": 0.00010914914309978485,
          "maximum": 0.0003014621324837208
        },
        "worst_index": [
          20,
          553,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.12320772062389788,
        "rms_normalized_error_percent": 2.8155481381822396,
        "absolute_error": {
          "p95": 9.748619049787521e-06,
          "p99": 1.892564796435181e-05,
          "maximum": 9.290128946304321e-05
        },
        "worst_index": [
          2,
          420,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.011384140314908536,
        "rms_normalized_error_percent": 2.4691314001839513,
        "absolute_error": {
          "p95": 7.637206181243528e-06,
          "p99": 2.6695779524743557e-05,
          "maximum": 0.00010642874985933304
        },
        "worst_index": [
          4,
          375,
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.008547005111096465,
                "cvrmse_percent": 15.619657196486004,
                "rms_normalized_rmse_percent": 4.325983545755472,
                "reference_energy": 24.000522841506154,
                "candidate_energy": 23.9984715155922,
                "relative_energy_error_percent": 0.008547005111096465,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.740469310287494e-06,
                  "p95": 0.0001347479410469532,
                  "p99": 0.00031988765113055706,
                  "maximum": 0.0006589035037904978
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 520,
                  "rgb_channel": 0,
                  "reference": 0.007200470892712474,
                  "candidate": 0.007859374396502972
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.04590753399481915,
                "cvrmse_percent": 104.25939724727817,
                "rms_normalized_rmse_percent": 6.069571093652531,
                "reference_energy": 5.3094969550364794,
                "candidate_energy": 5.307059495916892,
                "relative_energy_error_percent": 0.04590753399481916,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1651773093035445e-05,
                  "p90": 7.202065173714817e-05,
                  "p95": 0.00017571619537193328,
                  "p99": 0.0004433852154761553,
                  "maximum": 0.0009768621530383825
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 505,
                  "rgb_channel": 0,
                  "reference": 0.0010230974294245243,
                  "candidate": 4.623527638614178e-05
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
                "nmbe_percent": -0.003309244188176544,
                "cvrmse_percent": 64.00115977277584,
                "rms_normalized_rmse_percent": 5.596538858119768,
                "reference_energy": 0.9591491216579016,
                "candidate_energy": 0.9591173810713371,
                "relative_energy_error_percent": 0.003309244188176544,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.423534169793129e-06,
                  "maximum": 0.00024349353043362498
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 372,
                  "rgb_channel": 0,
                  "reference": 0.001802613027393818,
                  "candidate": 0.001559119496960193
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.2548278837895626,
                "cvrmse_percent": 518.8844981327568,
                "rms_normalized_rmse_percent": 8.80050196638742,
                "reference_energy": 0.1862621494104708,
                "candidate_energy": 0.18859941879821918,
                "relative_energy_error_percent": 1.2548278837895626,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2873515061073705e-05,
                  "p95": 2.1662885046680458e-05,
                  "p99": 4.860252374783158e-05,
                  "maximum": 0.0003903075121343136
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 372,
                  "rgb_channel": 0,
                  "reference": -0.0002186954952776432,
                  "candidate": 0.00017161201685667038
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
                "nmbe_percent": 0.08316325881404958,
                "cvrmse_percent": 45.81882188272973,
                "rms_normalized_rmse_percent": 6.692673570999817,
                "reference_energy": 2.002464017915372,
                "candidate_energy": 2.0041293322492493,
                "relative_energy_error_percent": 0.08316325881404958,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.724334500380792e-05,
                  "maximum": 0.0002853046462405473
                },
                "worst": {
                  "global_sensor_index": 89,
                  "local_sensor_index": 17,
                  "sky_patch_index": 280,
                  "rgb_channel": 0,
                  "reference": 0.0006353787030093372,
                  "candidate": 0.0009206833492498845
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.749537770719227,
                "cvrmse_percent": 1569.521675908054,
                "rms_normalized_rmse_percent": 9.713304312627685,
                "reference_energy": 0.08485926243736941,
                "candidate_energy": 0.08252602496470018,
                "relative_energy_error_percent": 2.749537770719227,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.893121389519367e-06,
                  "p95": 1.5126799780773581e-05,
                  "p99": 0.00011387759877834469,
                  "maximum": 0.00041103234980255365
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 371,
                  "rgb_channel": 0,
                  "reference": -0.0003134564030915499,
                  "candidate": 9.757594671100378e-05
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 226.68112500105053,
            "full": 694.7880419902503
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.93770890124142,
            "full": 715.1167499832809
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 236.51729198172688,
            "full": 717.8521250607446
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.0564159201458,
            "full": 712.3299170052633
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.005802636402371932,
                "cvrmse_percent": 8.119167813322909,
                "rms_normalized_rmse_percent": 2.248719492327906,
                "reference_energy": 24.0012773287624,
                "candidate_energy": 23.999884621907086,
                "relative_energy_error_percent": 0.005802636402371932,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7268859664909702e-06,
                  "p95": 6.680960359517485e-05,
                  "p99": 0.00016141333617269993,
                  "maximum": 0.0003592169377952814
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 437,
                  "rgb_channel": 0,
                  "reference": 0.005398930050432682,
                  "candidate": 0.005039713112637401
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.05258801495690834,
                "cvrmse_percent": 32.169640863761,
                "rms_normalized_rmse_percent": 3.3818036958405857,
                "reference_energy": 9.988914897823232,
                "candidate_energy": 9.994167869883732,
                "relative_energy_error_percent": 0.05258801495690835,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0450772606418468e-05,
                  "p90": 5.234359996393328e-05,
                  "p95": 0.00010042148642241955,
                  "p99": 0.00024848151952028275,
                  "maximum": 0.0005431189201772213
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 468,
                  "rgb_channel": 0,
                  "reference": 0.0011467437725514174,
                  "candidate": 0.000603624852374196
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
                "nmbe_percent": -0.020513346557273583,
                "cvrmse_percent": 33.29850538845168,
                "rms_normalized_rmse_percent": 2.91049124064733,
                "reference_energy": 0.9598964674514718,
                "candidate_energy": 0.9596995605625125,
                "relative_energy_error_percent": 0.020513346557273587,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.495415724813938e-06,
                  "maximum": 0.00013161147944629192
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 418,
                  "rgb_channel": 0,
                  "reference": 0.0020715384744107723,
                  "candidate": 0.0022031499538570642
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.41946969659016026,
                "cvrmse_percent": 94.08045656223774,
                "rms_normalized_rmse_percent": 5.4256190302256915,
                "reference_energy": 0.6510134001277237,
                "candidate_energy": 0.6482825961934466,
                "relative_energy_error_percent": 0.41946969659016026,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.618645455891965e-06,
                  "p90": 1.0898436266870723e-05,
                  "p95": 1.6213464732572902e-05,
                  "p99": 3.369020032550907e-05,
                  "maximum": 0.00020870956359431148
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 420,
                  "rgb_channel": 0,
                  "reference": 0.0001371570397168398,
                  "candidate": -7.155252387747169e-05
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
                "nmbe_percent": -0.008316436308611359,
                "cvrmse_percent": 27.317576202540348,
                "rms_normalized_rmse_percent": 3.9948783219568766,
                "reference_energy": 2.0019196542739337,
                "candidate_energy": 2.0017531659009364,
                "relative_energy_error_percent": 0.008316436308611357,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.729302600026131e-05,
                  "maximum": 0.00016767502529546618
                },
                "worst": {
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "sky_patch_index": 320,
                  "rgb_channel": 0,
                  "reference": 0.0012667175033129752,
                  "candidate": 0.0014343925286084414
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.051133408277695865,
                "cvrmse_percent": 133.08923442961134,
                "rms_normalized_rmse_percent": 6.23389373210786,
                "reference_energy": 0.6621754375095854,
                "candidate_energy": 0.6625140303795618,
                "relative_energy_error_percent": 0.051133408277695865,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.7940564021046157e-06,
                  "p90": 8.417613321398677e-06,
                  "p95": 1.3041010106462636e-05,
                  "p99": 7.165926945162937e-05,
                  "maximum": 0.0002822850365191698
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 462,
                  "rgb_channel": 0,
                  "reference": 0.00015582749620079994,
                  "candidate": -0.00012645754031836987
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 359.69724995084107,
            "full": 9158.725249930285
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 352.4305409519002,
            "full": 9217.473166063428
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 350.5826670443639,
            "full": 9360.374041949399
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 342.7889159647748,
            "full": 9471.681958064437
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05254409386265656,
                "cvrmse_percent": 8.874821134387764,
                "rms_normalized_rmse_percent": 2.4569876685394547,
                "reference_energy": 24.003116507775303,
                "candidate_energy": 23.990504287707495,
                "relative_energy_error_percent": 0.05254409386265656,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.9703001018788594e-06,
                  "p95": 6.943685002624989e-05,
                  "p99": 0.00018383609130978584,
                  "maximum": 0.000417372677475214
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 391,
                  "rgb_channel": 0,
                  "reference": 0.00418317667208612,
                  "candidate": 0.0037658039946109056
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.0752065943113248,
                "cvrmse_percent": 34.605263737246375,
                "rms_normalized_rmse_percent": 3.640897530830296,
                "reference_energy": 9.999569251014993,
                "candidate_energy": 10.007089586494484,
                "relative_energy_error_percent": 0.0752065943113248,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.041966061166022e-05,
                  "p90": 5.3022638894617585e-05,
                  "p95": 0.0001051807776093483,
                  "p99": 0.0002675925243238453,
                  "maximum": 0.0006397718098014593
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 522,
                  "rgb_channel": 0,
                  "reference": 0.00020505650900304317,
                  "candidate": 0.0008448283188045025
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
                "nmbe_percent": -0.0210190658269295,
                "cvrmse_percent": 32.646760370974675,
                "rms_normalized_rmse_percent": 2.859091045158556,
                "reference_energy": 0.9612703228513055,
                "candidate_energy": 0.9610682728093707,
                "relative_energy_error_percent": 0.0210190658269295,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.3489777706563473e-06,
                  "maximum": 0.00014435802586376667
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "sky_patch_index": 423,
                  "rgb_channel": 0,
                  "reference": 0.0022425029892474413,
                  "candidate": 0.0020981449633836746
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.9699146943744895,
                "cvrmse_percent": 97.94567711075277,
                "rms_normalized_rmse_percent": 5.651363212328669,
                "reference_energy": 0.6499504085520442,
                "candidate_energy": 0.6436464440333509,
                "relative_energy_error_percent": 0.9699146943744895,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.5848896737225004e-06,
                  "p90": 1.0619024124025615e-05,
                  "p95": 1.5848479506530566e-05,
                  "p99": 3.3854577850434e-05,
                  "maximum": 0.0002709140535444021
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 458,
                  "rgb_channel": 0,
                  "reference": 0.00016185862477868795,
                  "candidate": -0.00010905542876571417
                },
                "passed": true,
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
                "nmbe_percent": 0.20876431898543793,
                "cvrmse_percent": 27.042215859897134,
                "rms_normalized_rmse_percent": 3.9609163412177235,
                "reference_energy": 2.0012289245923967,
                "candidate_energy": 2.0054067765281616,
                "relative_energy_error_percent": 0.20876431898543793,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6297500375658274e-05,
                  "maximum": 0.0001846480299718678
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 321,
                  "rgb_channel": 0,
                  "reference": 0.0018143464694730937,
                  "candidate": 0.0019989944994449615
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.38235772568398446,
                "cvrmse_percent": 129.11230315873803,
                "rms_normalized_rmse_percent": 6.068758211012238,
                "reference_energy": 0.6636652311444742,
                "candidate_energy": 0.6611276558605148,
                "relative_energy_error_percent": 0.38235772568398446,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.8190667105955072e-06,
                  "p90": 8.150861185640693e-06,
                  "p95": 1.2582739145727828e-05,
                  "p99": 6.660650251433253e-05,
                  "maximum": 0.00028278952231630683
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 321,
                  "rgb_channel": 0,
                  "reference": 0.000192640523891896,
                  "candidate": -9.014899842441082e-05
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 347.87625004537404,
            "full": 9607.467833091505
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 346.7637080466375,
            "full": 9687.64525000006
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 344.8923750547692,
            "full": 9707.94674998615
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 350.2853329991922,
            "full": 9589.806457981467
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.007937461665711147,
                "cvrmse_percent": 5.509531678460599,
                "rms_normalized_rmse_percent": 1.5262099073608952,
                "reference_energy": 23.999770008113046,
                "candidate_energy": 24.0016749806573,
                "relative_energy_error_percent": 0.007937461665711147,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.928759022324897e-06,
                  "p95": 4.082685336470604e-05,
                  "p99": 0.00011592172086238861,
                  "maximum": 0.00023307651281356812
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 536,
                  "rgb_channel": 0,
                  "reference": 0.004949744092300534,
                  "candidate": 0.005182820605114102
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.03387041956384385,
                "cvrmse_percent": 21.691613990937636,
                "rms_normalized_rmse_percent": 2.2825650080912103,
                "reference_energy": 9.994052661055377,
                "candidate_energy": 9.997437688623108,
                "relative_energy_error_percent": 0.03387041956384386,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.648083737876732e-06,
                  "p90": 3.669978032121437e-05,
                  "p95": 6.674560427200049e-05,
                  "p99": 0.00016470649279654026,
                  "maximum": 0.0003816550597548485
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 528,
                  "rgb_channel": 0,
                  "reference": 0.0006746610160917044,
                  "candidate": 0.0002930059563368559
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
                "nmbe_percent": 0.05012488692035632,
                "cvrmse_percent": 15.936888308127754,
                "rms_normalized_rmse_percent": 1.3937061847871444,
                "reference_energy": 0.9583730537499378,
                "candidate_energy": 0.9588534371594051,
                "relative_energy_error_percent": 0.050124886920356326,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.865776307065971e-06,
                  "maximum": 8.489214815199375e-05
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 496,
                  "rgb_channel": 0,
                  "reference": 0.0024000979028642178,
                  "candidate": 0.0024849900510162115
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.35539175360859454,
                "cvrmse_percent": 56.31474728937116,
                "rms_normalized_rmse_percent": 3.2604788557144575,
                "reference_energy": 0.6524950820473236,
                "candidate_energy": 0.6501761683330258,
                "relative_energy_error_percent": 0.35539175360859454,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.2467524683756892e-06,
                  "p90": 7.507811051254995e-06,
                  "p95": 1.1219396128581138e-05,
                  "p99": 2.2847956188343232e-05,
                  "maximum": 9.186449460685253e-05
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 455,
                  "rgb_channel": 0,
                  "reference": 2.330448478460312e-05,
                  "candidate": 0.00011516897939145565
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
                "nmbe_percent": 0.048405773273852766,
                "cvrmse_percent": 15.829253822308031,
                "rms_normalized_rmse_percent": 2.320343381203914,
                "reference_energy": 2.0039257262660612,
                "candidate_energy": 2.004895742009694,
                "relative_energy_error_percent": 0.04840577327385277,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.8311507776379585e-05,
                  "maximum": 8.474104106426239e-05
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 420,
                  "rgb_channel": 0,
                  "reference": 0.0022501570638269186,
                  "candidate": 0.002165416022762656
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5266984122242544,
                "cvrmse_percent": 75.80652231466244,
                "rms_normalized_rmse_percent": 3.5609160465649587,
                "reference_energy": 0.6633539679420082,
                "candidate_energy": 0.659860093125431,
                "relative_energy_error_percent": 0.5266984122242545,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.333364480160526e-06,
                  "p90": 5.859847908595852e-06,
                  "p95": 9.061667583409871e-06,
                  "p99": 3.965426003560424e-05,
                  "maximum": 0.00013567355927079916
                },
                "worst": {
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "sky_patch_index": 324,
                  "rgb_channel": 0,
                  "reference": 0.00016523501835763454,
                  "candidate": 2.9561459086835384e-05
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 620.3580000437796,
            "full": 16717.105332994834
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 616.0649160156026,
            "full": 16759.292916976847
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 600.5141669884324,
            "full": 16650.518542039208
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 604.652333073318,
            "full": 16938.82195802871
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/atrium_borrowed_light/mf2/oracle/scene.rad"
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 19922.123749973252,
      "worker_pool_size": 12,
      "invocation_count": 7
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 75432.99433297943,
      "worker_pool_size": 12,
      "invocation_count": 7
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
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
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
            "nmbe_percent": -0.426087620015138,
            "cvrmse_percent": 50.39904159685523,
            "rms_normalized_rmse_percent": 5.303382121711429,
            "reference_energy": 9.995122800852522,
            "candidate_energy": 9.952534819992778,
            "relative_energy_error_percent": 0.42608762001515577,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.128927558776923e-06,
              "p90": 3.7931939004920437e-05,
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
            "nmbe_percent": -1.2147695344605984,
            "cvrmse_percent": 10.803691024529437,
            "rms_normalized_rmse_percent": 3.8667710502026877,
            "reference_energy": 33.9964676783916,
            "candidate_energy": 33.58348894624176,
            "relative_energy_error_percent": 1.2147695344605984,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.839349902700633e-06,
              "p90": 3.315475769340994e-05,
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
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
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
            "nmbe_percent": -0.44546697808755176,
            "cvrmse_percent": 40.464143277578216,
            "rms_normalized_rmse_percent": 2.337894217506171,
            "reference_energy": 0.6511219889988507,
            "candidate_energy": 0.6482214555507939,
            "relative_energy_error_percent": 0.44546697808755176,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2192717946390985e-06,
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
            "nmbe_percent": -0.16685991755019228,
            "cvrmse_percent": 16.03162721558281,
            "rms_normalized_rmse_percent": 2.2902444197733,
            "reference_energy": 1.6099488683074679,
            "candidate_energy": 1.6072625089532098,
            "relative_energy_error_percent": 0.16685991755019228,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2176283235021401e-06,
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
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
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
            "nmbe_percent": -0.00446777363631359,
            "cvrmse_percent": 41.27187106768655,
            "rms_normalized_rmse_percent": 1.9349923082518417,
            "reference_energy": 0.6618619960734566,
            "candidate_energy": 0.6618324255776873,
            "relative_energy_error_percent": 0.00446777363631359,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5317996826524904e-06,
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
            "nmbe_percent": -0.02894439243658075,
            "cvrmse_percent": 10.057389863547787,
            "rms_normalized_rmse_percent": 1.899354214346819,
            "reference_energy": 2.6660177662590048,
            "candidate_energy": 2.66524610361431,
            "relative_energy_error_percent": 0.028944392436580747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5341115613409784e-06,
              "p90": 5.835883530380672e-06,
              "p95": 8.142264505295316e-06,
              "p99": 1.7141224816441536e-05,
              "maximum": 5.405815318226814e-05
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 1,
              "sky_patch_index": 419,
              "rgb_channel": 0,
              "reference": 0.002164057921618223,
              "candidate": 0.0022181160748004913,
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
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
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
            "nmbe_percent": 87.55611241970253,
            "cvrmse_percent": 150.3800384857049,
            "rms_normalized_rmse_percent": 8.751010590344219,
            "reference_energy": 5.306430535157157,
            "candidate_energy": 9.952534819992778,
            "relative_energy_error_percent": 87.5561124197025,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.437429328798316e-05,
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
            "nmbe_percent": 14.589007433478779,
            "cvrmse_percent": 23.38117361976718,
            "rms_normalized_rmse_percent": 7.5147527507332805,
            "reference_energy": 29.30777541269624,
            "candidate_energy": 33.58348894624176,
            "relative_energy_error_percent": 14.589007433478766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.390022463165224e-05,
              "p90": 0.00015437536585523052,
              "p95": 0.00019804132170975208,
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
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
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
            "nmbe_percent": 245.28138583536705,
            "cvrmse_percent": 466.7770256539872,
            "rms_normalized_rmse_percent": 7.973586215397598,
            "reference_energy": 0.1877371564593613,
            "candidate_energy": 0.6482214555507939,
            "relative_energy_error_percent": 245.28138583536705,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.8503928863065084e-06,
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
            "nmbe_percent": 40.18078875783431,
            "cvrmse_percent": 76.3573631688807,
            "rms_normalized_rmse_percent": 7.966053600730615,
            "reference_energy": 1.1465640357679785,
            "candidate_energy": 1.6072625089532098,
            "relative_energy_error_percent": 40.180788757834314,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.849999757221667e-06,
              "p90": 2.105999919876922e-05,
              "p95": 2.9769998945994303e-05,
              "p99": 5.0549999286886305e-05,
              "maximum": 0.0002251691184937954
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 496,
              "rgb_channel": 0,
              "reference": 0.002272009151056409,
              "candidate": 0.0024971782695502043,
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
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
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
            "nmbe_percent": 698.9907613006467,
            "cvrmse_percent": 1289.7860993634674,
            "rms_normalized_rmse_percent": 7.79323333015604,
            "reference_energy": 0.08283355172972406,
            "candidate_energy": 0.6618324255776873,
            "relative_energy_error_percent": 698.9907613006467,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.650183425132127e-06,
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
            "nmbe_percent": 27.707701981357513,
            "cvrmse_percent": 50.94008005193707,
            "rms_normalized_rmse_percent": 7.754852716959323,
            "reference_energy": 2.086989321915272,
            "candidate_energy": 2.66524610361431,
            "relative_energy_error_percent": 27.707701981357513,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.654342146499403e-06,
              "p90": 2.2876999719301282e-05,
              "p95": 3.591441782191396e-05,
              "p99": 7.108354475349188e-05,
              "maximum": 0.00017331773415207863
            },
            "worst": {
              "global_sensor_index": 81,
              "local_sensor_index": 9,
              "sky_patch_index": 375,
              "rgb_channel": 0,
              "reference": 0.00115746830124408,
              "candidate": 0.0013307860353961587,
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
      "bias_percent": -1.0880718114339434,
      "rms_normalized_error_percent": 2.0450665523533775,
      "absolute_error": {
        "p95": 0.5684389982630312,
        "p99": 3.6106051759842117,
        "maximum": 3.752901764109737
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 21.144326002186634,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.0450665523533775
    },
    "overcast": {
      "bias_percent": -1.0679855970778933,
      "rms_normalized_error_percent": 2.050089523607847,
      "absolute_error": {
        "p95": 0.47605228424072243,
        "p99": 3.291004524230952,
        "maximum": 3.4175453186035156
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.614978790283203,
      "reference_fraction_of_uniform": 0.8803770542144775,
      "rms_normalized_to_uniform_percent": 1.8366246873179208
    },
    "horizon": {
      "bias_percent": -0.388948199214778,
      "rms_normalized_error_percent": 5.155737038366957,
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
      "rms_normalized_to_uniform_percent": 0.01121025866123574
    },
    "north": {
      "bias_percent": -0.6386536278204953,
      "rms_normalized_error_percent": 1.4881372763952094,
      "absolute_error": {
        "p95": 0.09635009765624993,
        "p99": 0.3817802906036362,
        "maximum": 0.7343587875366211
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1402947902679443,
      "reference_fraction_of_uniform": 0.14851714670658112,
      "rms_normalized_to_uniform_percent": 0.26073101809545335
    },
    "east": {
      "bias_percent": -0.30089377994624045,
      "rms_normalized_error_percent": 0.4045233955088756,
      "absolute_error": {
        "p95": 0.06027903556823726,
        "p99": 0.09095632553100579,
        "maximum": 0.102020263671875
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.016392946243286,
      "reference_fraction_of_uniform": 0.1426573246717453,
      "rms_normalized_to_uniform_percent": 0.07223821377851244
    },
    "south": {
      "bias_percent": -0.966434803521657,
      "rms_normalized_error_percent": 1.668575810254635,
      "absolute_error": {
        "p95": 0.1459402084350585,
        "p99": 0.4221881151199325,
        "maximum": 0.7529373168945312
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.155980110168457,
      "reference_fraction_of_uniform": 0.14925897121429443,
      "rms_normalized_to_uniform_percent": 0.2935028594410529
    },
    "west": {
      "bias_percent": -2.730995261703989,
      "rms_normalized_error_percent": 4.861343008252723,
      "absolute_error": {
        "p95": 0.30513815879821743,
        "p99": 1.603559770584104,
        "maximum": 1.6567554473876953
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.025930881500244,
      "reference_fraction_of_uniform": 0.19040243327617645,
      "rms_normalized_to_uniform_percent": 0.9200702901659007
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
          "nmbe_percent": -1.4795072549275954,
          "cvrmse_percent": 6.738593168818083,
          "absolute_error_percentiles_lux": {
            "p50": 9.42486572265625,
            "p90": 73.84174804687503,
            "p95": 115.76014404296787,
            "p99": 377.87140747070015
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
          "nmbe_percent": -0.16850362599505145,
          "cvrmse_percent": 8.912926778952277,
          "absolute_error_percentiles_lux": {
            "p50": 0.6442294120788574,
            "p90": 9.579616546630861,
            "p95": 15.902062988281244,
            "p99": 34.65174148559564
          },
          "maximum_absolute_error_lux": 155.267578125,
          "worst": {
            "sensor_index": 1,
            "position": [
              6.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3830.5,
            "foton_lux": 16568.103515625,
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
            "mean_absolute_error_percentage_points": 0.2731978380315493,
            "maximum_error_percentage_points": 1.355904397392969,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5787823439878235,
            "maximum_error_percentage_points": 2.548767123287675,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5764573820395734,
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
          "nmbe_percent": 0.0702476751688259,
          "cvrmse_percent": 2.962990544526183,
          "absolute_error_percentiles_lux": {
            "p50": 1.1652202606201172,
            "p90": 10.876615142822267,
            "p95": 16.16766967773436,
            "p99": 31.67456909179681
          },
          "maximum_absolute_error_lux": 146.56689453125,
          "worst": {
            "sensor_index": 9,
            "position": [
              7.5,
              2.5,
              3.75
            ],
            "hour_of_year": 4455.5,
            "foton_lux": 6130.185546875,
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
            "maximum_error_percentage_points": 0.004520547945205067,
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
            "maximum_error_percentage_points": 0.004520547945205067,
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
      "study_preparation_seconds": 0.012238167109899223,
      "weather_seconds": 0.12450174998957664,
      "metric_reduction_seconds": 0.38560812501236796,
      "write_seconds": 0.05891779193188995,
      "total_seconds": 0.5692859999835491,
      "cold_end_to_end_seconds": 0.5815241670934483,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.028677958995103836,
      "engine_upload_seconds": 0.000912084,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.32463100040331483,
      "engine_annual_reduction_seconds": 0.004242750001139939,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.32463100040331483
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.012238167109899223,
      "weather_seconds": 0.1499536669580266,
      "metric_reduction_seconds": 0.05365295894443989,
      "write_seconds": 0.058342208969406784,
      "total_seconds": 0.2621643749298528,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2621643749298528,
      "raw_export_seconds": 0.028326082974672318,
      "engine_upload_seconds": 8.8708e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.004420624929480255,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.028231916949152946,
      "full": 0.32113775005564094
    }
  },
  "elapsed_seconds": 251.33727254194673,
  "result_class": "passed"
}
```
