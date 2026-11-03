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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "73387be497de557f8b3b4bcc945a5564600b84454d3c25a5cfa9ef6006959a11",
  "weather_sha256": "67ef83472f8207a15e51875aa6e0f8ccf8b790e4fa9c78142c709d765ff48de1",
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
      "scene_fingerprint": 117564074192331588,
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
        "identifier": "teaching_classroom_grid",
        "bias_percent": -0.07611121373907904,
        "rms_normalized_error_percent": 1.045527656388712,
        "absolute_error": {
          "p95": 4.024847876280543e-05,
          "p99": 0.00014926279429346287,
          "maximum": 0.00047375215217471123
        },
        "worst_index": [
          26,
          99,
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
        "bias_percent": 0.08875130394130332,
        "rms_normalized_error_percent": 0.8149203737262675,
        "absolute_error": {
          "p95": 9.453808888792966e-05,
          "p99": 0.00019847367424517828,
          "maximum": 0.0006711333990097046
        },
        "worst_index": [
          40,
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
        "bias_percent": -0.020975530718954683,
        "rms_normalized_error_percent": 0.644145511182882,
        "absolute_error": {
          "p95": 8.14870465546846e-05,
          "p99": 0.00015260010957717884,
          "maximum": 0.0005038455128669739
        },
        "worst_index": [
          12,
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
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": -0.20020647229659583,
                "cvrmse_percent": 12.658306480525896,
                "rms_normalized_rmse_percent": 3.7210149160844477,
                "reference_energy": 23.08660588757266,
                "candidate_energy": 23.040385008352132,
                "relative_energy_error_percent": 0.20020647229659586,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.948015213012695e-05,
                  "p95": 0.00023650901857763445,
                  "p99": 0.0004871785640716544,
                  "maximum": 0.0015137596055865288
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 0.01645749993622303,
                  "candidate": 0.014943740330636501
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.20445996390395038,
                "cvrmse_percent": 48.07044164548161,
                "rms_normalized_rmse_percent": 3.388253715590653,
                "reference_energy": 8.67657300764806,
                "candidate_energy": 8.694313125687597,
                "relative_energy_error_percent": 0.20445996390395035,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00018053334206342698,
                  "p95": 0.00035709411604329896,
                  "p99": 0.0007089811819605522,
                  "maximum": 0.0022172294557094574
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": -0.0016926797106862068,
                  "candidate": 0.0005245497450232506
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.0943330740556,
            "full": 350.5574580049142
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.45520799420774,
            "full": 350.40095797739923
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.36641698051244,
            "full": 347.43416705168784
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.66641709581017,
            "full": 349.32229097466916
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
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": -0.00811059445578113,
                "cvrmse_percent": 6.232794319729525,
                "rms_normalized_rmse_percent": 1.832201094427954,
                "reference_energy": 23.06355807185946,
                "candidate_energy": 23.06168748019718,
                "relative_energy_error_percent": 0.008110594455781132,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.930448533035849e-05,
                  "p95": 0.0001246811181772494,
                  "p99": 0.0002560807543341069,
                  "maximum": 0.0004922100342810154
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.006975901313126087,
                  "candidate": 0.007468111347407103
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.06501041943688154,
                "cvrmse_percent": 15.066083745065551,
                "rms_normalized_rmse_percent": 1.5220597569535002,
                "reference_energy": 15.375808434135646,
                "candidate_energy": 15.385804311690489,
                "relative_energy_error_percent": 0.06501041943688154,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.7278780951055523e-07,
                  "p90": 9.709744481369855e-05,
                  "p95": 0.0001890453509986396,
                  "p99": 0.0003794224822195244,
                  "maximum": 0.000994330272078514
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06059708446264267,
                  "candidate": 0.061591414734721184
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.22437498159707,
            "full": 4107.910500024445
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 197.5264169741422,
            "full": 4153.802541899495
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 196.0163329495117,
            "full": 4140.695792040788
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.99954097066075,
            "full": 4123.126625083387
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
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08758575689352936,
                "cvrmse_percent": 5.666537339505498,
                "rms_normalized_rmse_percent": 1.6662141415770662,
                "reference_energy": 23.065131756803567,
                "candidate_energy": 23.04492998657588,
                "relative_energy_error_percent": 0.08758575689352936,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.860600456595445e-05,
                  "p95": 0.00011406236153561622,
                  "p99": 0.00023093074327334753,
                  "maximum": 0.00043593021109700203
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 0.011341480072587729,
                  "candidate": 0.010905549861490726
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.24392269105898798,
                "cvrmse_percent": 14.692119243868277,
                "rms_normalized_rmse_percent": 1.48498741011003,
                "reference_energy": 15.403730693021057,
                "candidate_energy": 15.441303887450953,
                "relative_energy_error_percent": 0.24392269105898798,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.687906371396821e-07,
                  "p90": 9.340879623778175e-05,
                  "p95": 0.0001884131284896277,
                  "p99": 0.00035884652752429195,
                  "maximum": 0.001130085438489914
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04199665039777756,
                  "candidate": 0.04086656495928764
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 193.6880419962108,
            "full": 4374.483166960999
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.46637500915676,
            "full": 4388.726375065744
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 196.95987505838275,
            "full": 4365.634916932322
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.946458959952,
            "full": 4400.394750060514
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
            "identifier": "teaching_classroom_grid",
            "start_sensor_index": 0,
            "sensor_count": 63,
            "stages": {
              "direct": {
                "nmbe_percent": -0.016848429323565253,
                "cvrmse_percent": 3.050147000854651,
                "rms_normalized_rmse_percent": 0.8967156396830417,
                "reference_energy": 23.067211770443464,
                "candidate_energy": 23.063325307571404,
                "relative_energy_error_percent": 0.016848429323565253,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.125866060145201e-05,
                  "p95": 6.236158660612967e-05,
                  "p99": 0.00012185066472738973,
                  "maximum": 0.0002451827749609947
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 71,
                  "rgb_channel": 0,
                  "reference": 0.007480335654690862,
                  "candidate": 0.007725518429651856
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.13174728898559265,
                "cvrmse_percent": 8.377564201107367,
                "rms_normalized_rmse_percent": 0.8472839392154756,
                "reference_energy": 15.414362737105733,
                "candidate_energy": 15.394054732085191,
                "relative_energy_error_percent": 0.13174728898559263,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.575080486622028e-07,
                  "p90": 4.911823198199275e-05,
                  "p95": 0.00010152081667911228,
                  "p99": 0.0002008318551816046,
                  "maximum": 0.0007697511464357376
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.059160759672522545,
                  "candidate": 0.05993051081895828
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 329.9623749917373,
            "full": 7746.5068330056965
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 327.00100005604327,
            "full": 7716.537082917057
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 321.44520804286003,
            "full": 7802.375040948391
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 327.8616250026971,
            "full": 7734.772124909796
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2183.2960420288146,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_classroom/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 8512.43975001853,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01266871125203931,
            "cvrmse_percent": 1.9996825692834805,
            "rms_normalized_rmse_percent": 0.5879454999976449,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066395475735135,
            "relative_energy_error_percent": 0.012668711252039312,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.249399691820145e-06,
              "p95": 2.6832130970433354e-05,
              "p99": 8.811010047793388e-05,
              "maximum": 0.00021480349823832512
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.0013871249975636601,
              "candidate": 0.001172321499325335,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3273378099568696,
            "cvrmse_percent": 23.91025850480108,
            "rms_normalized_rmse_percent": 2.417741375682621,
            "reference_energy": 15.406003685735403,
            "candidate_energy": 15.201513973811288,
            "relative_energy_error_percent": 1.3273378099568696,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1814545928245934e-06,
              "p90": 5.86712965741754e-05,
              "p95": 9.207502880599344e-05,
              "p99": 0.00021905256784521021,
              "maximum": 0.002955302596092224
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06981810182332993,
              "candidate": 0.0668627992272377,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5239683018989111,
            "cvrmse_percent": 9.56379919678122,
            "rms_normalized_rmse_percent": 2.4148063459986946,
            "reference_energy": 38.46947731659155,
            "candidate_energy": 38.26790944954642,
            "relative_energy_error_percent": 0.5239683018989019,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1625713227658707e-06,
              "p90": 5.936910456512125e-05,
              "p95": 9.267029818147412e-05,
              "p99": 0.00020826539024710645,
              "maximum": 0.002955302596092224
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06981810182332993,
              "candidate": 0.0668627992272377,
              "position": [
                3.5,
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
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01266871125203931,
            "cvrmse_percent": 1.9996825692834805,
            "rms_normalized_rmse_percent": 0.5879454999976449,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066395475735135,
            "relative_energy_error_percent": 0.012668711252039312,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.249399691820145e-06,
              "p95": 2.6832130970433354e-05,
              "p99": 8.811010047793388e-05,
              "maximum": 0.00021480349823832512
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.0013871249975636601,
              "candidate": 0.001172321499325335,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 75.02245746267378,
            "cvrmse_percent": 381.16217911736584,
            "rms_normalized_rmse_percent": 26.925242301858674,
            "reference_energy": 8.685464822166175,
            "candidate_energy": 15.201513973811288,
            "relative_energy_error_percent": 75.02245746267378,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.6144361697788554e-07,
              "p90": 0.0005120525628171893,
              "p95": 0.0006712074158713216,
              "p99": 0.001064935430185869,
              "maximum": 0.017219178378582
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045532114803791046,
              "candidate": 0.06275129318237305,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.532878622603288,
            "cvrmse_percent": 104.2708636679654,
            "rms_normalized_rmse_percent": 26.924579736047804,
            "reference_energy": 31.748938453022326,
            "candidate_energy": 38.26790944954642,
            "relative_energy_error_percent": 20.532878622603288,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.2255024845208027e-07,
              "p90": 0.0005142787034856159,
              "p95": 0.0006644964145380061,
              "p99": 0.001035097439307712,
              "maximum": 0.017219178378582
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045532114803791046,
              "candidate": 0.06275129318237305,
              "position": [
                0.5,
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
      "bias_percent": 0.14703747431203004,
      "rms_normalized_error_percent": 0.23478815945601736,
      "absolute_error": {
        "p95": 0.17772346395245373,
        "p99": 0.21303668003637874,
        "maximum": 0.2228523665756299
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.727396951699042,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23478815945601736
    },
    "overcast": {
      "bias_percent": 0.12476190159565516,
      "rms_normalized_error_percent": 0.17991448403843818,
      "absolute_error": {
        "p95": 0.08589587211608886,
        "p99": 0.14647605895996096,
        "maximum": 0.15070724487304688
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.217119216918945,
      "reference_fraction_of_uniform": 0.6441749334335327,
      "rms_normalized_to_uniform_percent": 0.12586475983177303
    },
    "horizon": {
      "bias_percent": 0.9900611169837303,
      "rms_normalized_error_percent": 2.294342637598638,
      "absolute_error": {
        "p95": 0.12896384400631294,
        "p99": 0.17263020576341154,
        "maximum": 0.17507799399682167
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4071978881569085,
      "reference_fraction_of_uniform": 0.09006480849994951,
      "rms_normalized_to_uniform_percent": 0.15818104752729673
    },
    "north": {
      "bias_percent": -35.73851388918219,
      "rms_normalized_error_percent": 126.50364582534077,
      "absolute_error": {
        "p95": 9.571746068104403e-05,
        "p99": 0.00034344869578490034,
        "maximum": 0.0003444944304646924
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.135582301183604e-05,
      "reference_fraction_of_uniform": 1.1731716540452908e-06,
      "rms_normalized_to_uniform_percent": 0.00019430478613646006
    },
    "east": {
      "bias_percent": 0.07346213244961557,
      "rms_normalized_error_percent": 0.35517221610312444,
      "absolute_error": {
        "p95": 0.05384700298309326,
        "p99": 0.06402744293212893,
        "maximum": 0.07048892974853516
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.270660400390625,
      "reference_fraction_of_uniform": 0.19720067083835602,
      "rms_normalized_to_uniform_percent": 0.07548319208656445
    },
    "south": {
      "bias_percent": 0.17237947739225273,
      "rms_normalized_error_percent": 0.31171900798227425,
      "absolute_error": {
        "p95": 0.15442547798156736,
        "p99": 0.17999887466430675,
        "maximum": 0.20543861389160156
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.421968460083008,
      "reference_fraction_of_uniform": 0.6892541646957397,
      "rms_normalized_to_uniform_percent": 0.19865664132617836
    },
    "west": {
      "bias_percent": 0.10110239984869024,
      "rms_normalized_error_percent": 0.3079672301335956,
      "absolute_error": {
        "p95": 0.04400535225868225,
        "p99": 0.05347589015960695,
        "maximum": 0.0584874153137207
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.12924337387085,
      "reference_fraction_of_uniform": 0.1919095814228058,
      "rms_normalized_to_uniform_percent": 0.06329683977988676
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
          "nmbe_percent": 0.008957139594931152,
          "cvrmse_percent": 1.0575067873232835,
          "absolute_error_percentiles_lux": {
            "p50": 3.05755615234375,
            "p90": 32.585205078125,
            "p95": 51.935156250000006,
            "p99": 103.47034179687532
          },
          "maximum_absolute_error_lux": 397.345947265625,
          "worst": {
            "sensor_index": 47,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5411.5,
            "foton_lux": 4244.40771484375,
            "radiance_lux": 3847.061767578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10423135464231242,
            "maximum_error_percentage_points": 0.5516438356164315,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.052904164322634804,
            "maximum_error_percentage_points": 0.32740091275944394,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03082626657969129,
            "maximum_error_percentage_points": 0.2417808219178088,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06576647097195014,
            "maximum_error_percentage_points": 0.24315068493150704,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05296803652968059,
            "maximum_error_percentage_points": 0.24452054794520528,
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
      "maximum_error_percentage_points": 0.004950770547949901,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004950770547949901,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.007312332978472114,
      "weather_seconds": 0.09283379092812538,
      "metric_reduction_seconds": 0.06275916693266481,
      "write_seconds": 0.04376008303370327,
      "total_seconds": 0.19950941705610603,
      "cold_end_to_end_seconds": 0.20682175003457814,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01751495897769928,
      "engine_upload_seconds": 0.00026925,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.044225333258509636,
      "engine_annual_reduction_seconds": 0.0005370000144466758,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.044225333258509636
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007312332978472114,
      "weather_seconds": 0.09286166599486023,
      "metric_reduction_seconds": 0.011925667058676481,
      "write_seconds": 0.02438458299729973,
      "total_seconds": 0.12940320803318173,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.12940320803318173,
      "raw_export_seconds": 0.012145415996201336,
      "engine_upload_seconds": 6.0041e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0005590833025053144,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.007838416029699147,
      "full": 0.03429662506096065
    }
  },
  "elapsed_seconds": 82.21304425003473,
  "result_class": "passed"
}
```
