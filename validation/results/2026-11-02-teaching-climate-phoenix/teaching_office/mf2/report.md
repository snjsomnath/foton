# Foton report

Status: **passed**

```json
{
  "scene": "teaching_office",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_office",
    "category": "teaching",
    "question": "How is a 12 x 8 m open-plan office with a ribbon window lit?",
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
    "sensors": 96,
    "floor_area": 96.0,
    "aperture_area": 17.6
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "334b793878cbbeae1672b17c0e08a6c2298fa16766988f0045bcd4eac5bfe4a4",
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
      "scene_fingerprint": 17113111844658936175,
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
      "scene_fingerprint": 17113111844658936175,
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
        "identifier": "teaching_office_grid",
        "bias_percent": 0.033900770041301743,
        "rms_normalized_error_percent": 0.7639001981790288,
        "absolute_error": {
          "p95": 1.038727532431949e-06,
          "p99": 2.4425185984000564e-05,
          "maximum": 0.00013817357830703259
        },
        "worst_index": [
          6,
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
        "identifier": "teaching_office_grid",
        "bias_percent": 0.06228858395374035,
        "rms_normalized_error_percent": 1.0329537070702624,
        "absolute_error": {
          "p95": 6.516324356198311e-05,
          "p99": 0.00013762422720901629,
          "maximum": 0.0008316114544868469
        },
        "worst_index": [
          45,
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
        "identifier": "teaching_office_grid",
        "bias_percent": -0.01739501735448693,
        "rms_normalized_error_percent": 0.8539874441461563,
        "absolute_error": {
          "p95": 5.258020246401429e-05,
          "p99": 0.00011093739070929533,
          "maximum": 0.0008459538221359253
        },
        "worst_index": [
          84,
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
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05991546149407761,
                "cvrmse_percent": 30.21915067820182,
                "rms_normalized_rmse_percent": 8.82021746771185,
                "reference_energy": 37.045256378531576,
                "candidate_energy": 37.06745221485244,
                "relative_energy_error_percent": 0.059915461494077615,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.7241191350622105e-05,
                  "p95": 0.00014177720731822774,
                  "p99": 0.00033006271049089116,
                  "maximum": 0.0008805078687146306
                },
                "worst": {
                  "global_sensor_index": 78,
                  "local_sensor_index": 78,
                  "sky_patch_index": 265,
                  "rgb_channel": 0,
                  "reference": 0.004072961863130331,
                  "candidate": 0.0031924539944157004
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.20119972197377342,
                "cvrmse_percent": 100.66920977934537,
                "rms_normalized_rmse_percent": 3.9197759199717033,
                "reference_energy": 15.519436235131181,
                "candidate_energy": 15.4882111725742,
                "relative_energy_error_percent": 0.20119972197377342,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.583455346524716e-05,
                  "p95": 0.0002154927933588624,
                  "p99": 0.0004590136837214216,
                  "maximum": 0.001883048564195633
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08701420575380325,
                  "candidate": 0.08889725431799889
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 182.9664169345051,
            "full": 466.1446249810979
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 175.0998339848593,
            "full": 484.3675420852378
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.13079203106463,
            "full": 486.1974169034511
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 170.86637497413903,
            "full": 478.1298330053687
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
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05825311778495481,
                "cvrmse_percent": 16.309738715958773,
                "rms_normalized_rmse_percent": 4.774636226480308,
                "reference_energy": 37.095137755377095,
                "candidate_energy": 37.073528681087964,
                "relative_energy_error_percent": 0.0582531177849548,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6508122391534452e-05,
                  "p95": 8.747342508286238e-05,
                  "p99": 0.00017652136739343405,
                  "maximum": 0.00042812805622816086
                },
                "worst": {
                  "global_sensor_index": 78,
                  "local_sensor_index": 78,
                  "sky_patch_index": 412,
                  "rgb_channel": 0,
                  "reference": 0.0025460240431129932,
                  "candidate": 0.0021178959868848324
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.14642737396205555,
                "cvrmse_percent": 34.58893517058335,
                "rms_normalized_rmse_percent": 1.888416255030623,
                "reference_energy": 26.76666996219545,
                "candidate_energy": 26.805863694118184,
                "relative_energy_error_percent": 0.14642737396205555,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 5.035843350924557e-05,
                  "p95": 0.00012579028407344595,
                  "p99": 0.0002656264611869112,
                  "maximum": 0.0010904744267463684
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0716012455523014,
                  "candidate": 0.07269171997904778
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 275.08545794989914,
            "full": 5773.560000001453
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 263.56699992902577,
            "full": 5724.048999953084
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 265.28833305928856,
            "full": 5731.030500028282
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 282.06158289685845,
            "full": 5641.713749966584
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
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05729342307708936,
                "cvrmse_percent": 16.890619652118144,
                "rms_normalized_rmse_percent": 4.9430243998073475,
                "reference_energy": 37.07890687330632,
                "candidate_energy": 37.10015064829361,
                "relative_energy_error_percent": 0.057293423077089366,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.727038274519245e-05,
                  "p95": 9.013083763420582e-05,
                  "p99": 0.00018313819426111837,
                  "maximum": 0.0004519944777712226
                },
                "worst": {
                  "global_sensor_index": 62,
                  "local_sensor_index": 62,
                  "sky_patch_index": 357,
                  "rgb_channel": 0,
                  "reference": 0.00410078652203083,
                  "candidate": 0.003648792044259608
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.05138236895934798,
                "cvrmse_percent": 36.06363972933404,
                "rms_normalized_rmse_percent": 1.972219092107166,
                "reference_energy": 26.82774783243472,
                "candidate_energy": 26.813963100059976,
                "relative_energy_error_percent": 0.05138236895934799,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 5.22290780281769e-05,
                  "p95": 0.00012824160512536764,
                  "p99": 0.00027313075494020964,
                  "maximum": 0.0013033784925937653
                },
                "worst": {
                  "global_sensor_index": 85,
                  "local_sensor_index": 85,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07918877899646759,
                  "candidate": 0.08049215748906136
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 270.4057089285925,
            "full": 6059.698541997932
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 276.3442920986563,
            "full": 5995.932082994841
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 282.6181249693036,
            "full": 6213.2339590461925
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 287.4516249867156,
            "full": 5890.835208003409
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
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": -0.031260380305501864,
                "cvrmse_percent": 9.664796650173106,
                "rms_normalized_rmse_percent": 2.8304918122308442,
                "reference_energy": 37.095819163221336,
                "candidate_energy": 37.08422286907347,
                "relative_energy_error_percent": 0.031260380305501864,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.131345063389747e-05,
                  "p95": 4.770606756210327e-05,
                  "p99": 0.00010529309278354044,
                  "maximum": 0.00023394616437144578
                },
                "worst": {
                  "global_sensor_index": 64,
                  "local_sensor_index": 64,
                  "sky_patch_index": 93,
                  "rgb_channel": 0,
                  "reference": 0.0009815603552851826,
                  "candidate": 0.0012155065196566284
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.05061574716667961,
                "cvrmse_percent": 20.832763208797125,
                "rms_normalized_rmse_percent": 1.1388192148455727,
                "reference_energy": 26.802462767593816,
                "candidate_energy": 26.816029034382705,
                "relative_energy_error_percent": 0.05061574716667962,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.9999993478877514e-08,
                  "p90": 3.00626546959393e-05,
                  "p95": 7.340003503486514e-05,
                  "p99": 0.00015683152625570044,
                  "maximum": 0.0009072348475456238
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 45,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0940002091228962,
                  "candidate": 0.09490744397044182
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 474.2126250639558,
            "full": 10714.797999942675
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 470.1945419656113,
            "full": 10658.998167025857
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 479.3980000540614,
            "full": 10819.239417091012
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 473.86799997184426,
            "full": 10742.615250055678
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 16547.984332893975,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_office/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 65863.16674994305,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9184875314363317,
            "cvrmse_percent": 63.00630987833824,
            "rms_normalized_rmse_percent": 3.4451938716588497,
            "reference_energy": 26.81619439115483,
            "candidate_energy": 26.301729045354797,
            "relative_energy_error_percent": 1.9184875314363283,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.823623183687232e-08,
              "p90": 1.859786498243925e-05,
              "p95": 3.272630419814959e-05,
              "p99": 6.67214073473587e-05,
              "maximum": 0.004817470908164978
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10802294313907623,
              "candidate": 0.10320547223091125,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7974598086499463,
            "cvrmse_percent": 26.434003656342238,
            "rms_normalized_rmse_percent": 3.4442232744543535,
            "reference_energy": 63.89926686689821,
            "candidate_energy": 63.389695895612746,
            "relative_energy_error_percent": 0.7974598086499116,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.852386308902169e-08,
              "p90": 1.8341396935284208e-05,
              "p95": 3.195821773260832e-05,
              "p99": 6.591191631741797e-05,
              "maximum": 0.004817470908164978
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10802294313907623,
              "candidate": 0.10320547223091125,
              "position": [
                4.5,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.93958639976047,
            "cvrmse_percent": 597.302598121198,
            "rms_normalized_rmse_percent": 23.185052310373372,
            "reference_energy": 15.477105483523683,
            "candidate_energy": 26.301729045354797,
            "relative_energy_error_percent": 69.93958639976047,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015667089028283956,
              "p95": 0.00022640787938144058,
              "p99": 0.0003561537095811212,
              "maximum": 0.01926371455192566
            },
            "worst": {
              "global_sensor_index": 94,
              "local_sensor_index": 94,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05723540484905243,
              "candidate": 0.07649911940097809,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.604035900978662,
            "cvrmse_percent": 175.88831475813487,
            "rms_normalized_rmse_percent": 23.185568472406665,
            "reference_energy": 52.56017795926708,
            "candidate_energy": 63.389695895612746,
            "relative_energy_error_percent": 20.60403590097867,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00015651791472919292,
              "p95": 0.00022682000417262316,
              "p99": 0.00035737047612201397,
              "maximum": 0.01926371455192566
            },
            "worst": {
              "global_sensor_index": 94,
              "local_sensor_index": 94,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05723540484905243,
              "candidate": 0.07649911940097809,
              "position": [
                11.5,
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
      "bias_percent": 0.13371728522391502,
      "rms_normalized_error_percent": 0.18380283089968094,
      "absolute_error": {
        "p95": 0.1716724876816631,
        "p99": 0.18603529938476687,
        "maximum": 0.1874303134645885
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.444966457628784,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.18380283089968094
    },
    "overcast": {
      "bias_percent": 0.0933920712858456,
      "rms_normalized_error_percent": 0.13651499086681193,
      "absolute_error": {
        "p95": 0.07120251655578613,
        "p99": 0.08349037170410155,
        "maximum": 0.08758544921875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.160131454467773,
      "reference_fraction_of_uniform": 0.6384303569793701,
      "rms_normalized_to_uniform_percent": 0.09562704068041702
    },
    "horizon": {
      "bias_percent": 0.815753549687253,
      "rms_normalized_error_percent": 1.7654022682703012,
      "absolute_error": {
        "p95": 0.16488947717167202,
        "p99": 0.20314294114754156,
        "maximum": 0.20354454219694507
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.481941524436262,
      "reference_fraction_of_uniform": 0.1224097602513581,
      "rms_normalized_to_uniform_percent": 0.16188317183136056
    },
    "north": {
      "bias_percent": -53.255173950700446,
      "rms_normalized_error_percent": 87.90653672840405,
      "absolute_error": {
        "p95": 4.1434811464569066e-05,
        "p99": 7.38751989274533e-05,
        "maximum": 7.623388228239492e-05
      },
      "worst_index": [
        76
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1101478776254226e-05,
      "reference_fraction_of_uniform": 3.9027918319334276e-07,
      "rms_normalized_to_uniform_percent": 4.369670744882732e-05
    },
    "east": {
      "bias_percent": 0.05747833940814588,
      "rms_normalized_error_percent": 0.20067743393067144,
      "absolute_error": {
        "p95": 0.03372478485107422,
        "p99": 0.04110393524169917,
        "maximum": 0.05677032470703125
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.448315143585205,
      "reference_fraction_of_uniform": 0.19153881072998047,
      "rms_normalized_to_uniform_percent": 0.04103150804015793
    },
    "south": {
      "bias_percent": 0.1735093941674632,
      "rms_normalized_error_percent": 0.2586143757657744,
      "absolute_error": {
        "p95": 0.16961383819580078,
        "p99": 0.18329269886016844,
        "maximum": 0.1921682357788086
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.692110061645508,
      "reference_fraction_of_uniform": 0.6922880411148071,
      "rms_normalized_to_uniform_percent": 0.16399335996651132
    },
    "west": {
      "bias_percent": 0.11600261162956925,
      "rms_normalized_error_percent": 0.16811729240720816,
      "absolute_error": {
        "p95": 0.025501251220703125,
        "p99": 0.03668311834335326,
        "maximum": 0.039234161376953125
      },
      "worst_index": [
        77
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.510802745819092,
      "reference_fraction_of_uniform": 0.19373559951782227,
      "rms_normalized_to_uniform_percent": 0.034630181376893276
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
        "identifier": "teaching_office_grid",
        "sensor_count": 96,
        "illuminance": {
          "nmbe_percent": -0.11321447071900714,
          "cvrmse_percent": 1.2141602919887542,
          "absolute_error_percentiles_lux": {
            "p50": 9.232269287109375,
            "p90": 60.554760742187526,
            "p95": 90.83460083007809,
            "p99": 178.25390625
          },
          "maximum_absolute_error_lux": 512.4140625,
          "worst": {
            "sensor_index": 22,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 7284.5,
            "foton_lux": 41320.9609375,
            "radiance_lux": 40808.546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09452910958904193,
            "maximum_error_percentage_points": 0.5499999999999972,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.024794683103621946,
            "maximum_error_percentage_points": 0.13783603047669146,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.01930650684931506,
            "maximum_error_percentage_points": 0.10945205479452058,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10792665525114108,
            "maximum_error_percentage_points": 0.60109589041096,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.09818921232876711,
            "maximum_error_percentage_points": 0.6328767123287662,
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
      "maximum_error_percentage_points": 0.004972977311652471,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004972977311652471,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_office_grid",
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
      "study_preparation_seconds": 0.008738792035728693,
      "weather_seconds": 0.14457562507595867,
      "metric_reduction_seconds": 0.25687925005331635,
      "write_seconds": 0.03744849993381649,
      "total_seconds": 0.43907941703218967,
      "cold_end_to_end_seconds": 0.44781820906791836,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02455512504093349,
      "engine_upload_seconds": 0.000873417,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.20128108316566795,
      "engine_annual_reduction_seconds": 0.003692750004120171,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.20128108316566795
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008738792035728693,
      "weather_seconds": 0.1072587090311572,
      "metric_reduction_seconds": 0.04885208292398602,
      "write_seconds": 0.028493457939475775,
      "total_seconds": 0.18477558402810246,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18477558402810246,
      "raw_export_seconds": 0.012529833009466529,
      "engine_upload_seconds": 9.0833e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0037457499420270324,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01278229197487235,
      "full": 0.2001558339688927
    }
  },
  "elapsed_seconds": 182.50673008302692,
  "result_class": "passed"
}
```
