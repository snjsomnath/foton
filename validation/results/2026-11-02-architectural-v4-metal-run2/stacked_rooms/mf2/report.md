# Foton report

Status: **passed**

```json
{
  "scene": "stacked_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "stacked_rooms",
    "category": "connections",
    "question": "Does an opaque shared slab isolate two storeys?",
    "interactions": [
      "stacked_zones",
      "opaque_adjacency",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 2,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 5.999999999999997
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2ee09b87e02506de28a9ff4e6541af9f1849efc815ac6e1bf38b76eca615c3b6",
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
      "scene_fingerprint": 6348620744982744529,
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
      "scene_fingerprint": 6348620744982744529,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.02574736435175291,
        "rms_normalized_error_percent": 0.7597631247218805,
        "absolute_error": {
          "p95": 3.259629011154175e-08,
          "p99": 7.011898560449481e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          17,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.02575210823513647,
        "rms_normalized_error_percent": 0.7597635803020724,
        "absolute_error": {
          "p95": 3.259629011154175e-08,
          "p99": 7.011898560449481e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          17,
          543,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.015568251632682962,
        "rms_normalized_error_percent": 1.7151553026948594,
        "absolute_error": {
          "p95": 2.2240157704800367e-05,
          "p99": 0.0001024911180138588,
          "maximum": 0.00047638267278671265
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": 0.21021092536730743,
        "rms_normalized_error_percent": 1.7444512430333685,
        "absolute_error": {
          "p95": 2.1411455236375332e-05,
          "p99": 0.00010423571802675724,
          "maximum": 0.0005303062498569489
        },
        "worst_index": [
          20,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": 0.05540411932982456,
        "rms_normalized_error_percent": 1.4131854803969284,
        "absolute_error": {
          "p95": 1.7875805497169495e-05,
          "p99": 8.217041613534093e-05,
          "maximum": 0.0006373263895511627
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.040383854723410884,
        "rms_normalized_error_percent": 1.4492190456984353,
        "absolute_error": {
          "p95": 1.839541073422879e-05,
          "p99": 8.441112004220486e-05,
          "maximum": 0.00040245428681373596
        },
        "worst_index": [
          16,
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09772640058814845,
                "cvrmse_percent": 30.86840445236691,
                "rms_normalized_rmse_percent": 5.938723071523123,
                "reference_energy": 6.003220565329684,
                "candidate_energy": 6.009087296707548,
                "relative_energy_error_percent": 0.09772640058814847,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.490511052310467e-06,
                  "p99": 0.00017770251724869013,
                  "maximum": 0.0004470349522307515
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 414,
                  "rgb_channel": 0,
                  "reference": 0.0032928584842011333,
                  "candidate": 0.0037398934364318848
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.7144048515074896,
                "cvrmse_percent": 166.14193071151732,
                "rms_normalized_rmse_percent": 6.284628498017532,
                "reference_energy": 2.0914313930163893,
                "candidate_energy": 2.0764901056787295,
                "relative_energy_error_percent": 0.7144048515074897,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.705131752620219e-06,
                  "p95": 4.826563599635847e-05,
                  "p99": 0.0003091110847890377,
                  "maximum": 0.0009189797565340996
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.025229250080883503,
                  "candidate": 0.024310270324349403
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04261331180972052,
                "cvrmse_percent": 36.120719676450385,
                "rms_normalized_rmse_percent": 6.956288820528645,
                "reference_energy": 6.018720193604167,
                "candidate_energy": 6.021284969607223,
                "relative_energy_error_percent": 0.042613311809720514,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.7207501009106636e-05,
                  "p99": 0.00018800696125254035,
                  "maximum": 0.0005422405665740371
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 315,
                  "rgb_channel": 0,
                  "reference": 0.003443926456384361,
                  "candidate": 0.003986167022958398
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2409237941620652,
                "cvrmse_percent": 171.83135446270705,
                "rms_normalized_rmse_percent": 6.431138218135546,
                "reference_energy": 2.0710288077699985,
                "candidate_energy": 2.0760184089518674,
                "relative_energy_error_percent": 0.24092379416206516,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.550026480705129e-06,
                  "p95": 5.192345997784287e-05,
                  "p99": 0.00031967152608558536,
                  "maximum": 0.000783134251832962
                },
                "worst": {
                  "global_sensor_index": 65,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.017894575372338295,
                  "candidate": 0.018677709624171257
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.5006249845028,
            "full": 400.64129198435694
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.2807920286432,
            "full": 399.47670802939683
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.2770000109449,
            "full": 414.76608300581574
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.53104194439948,
            "full": 406.6432500258088
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06526125278430116,
                "cvrmse_percent": 25.120342304733985,
                "rms_normalized_rmse_percent": 4.8394733038724365,
                "reference_energy": 6.0142236411602426,
                "candidate_energy": 6.018148598853713,
                "relative_energy_error_percent": 0.06526125278430116,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2529944544658065e-05,
                  "p99": 0.0001386693911626935,
                  "maximum": 0.00035288906656205654
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 307,
                  "rgb_channel": 0,
                  "reference": 0.003767037997022271,
                  "candidate": 0.0034141489304602146
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.6090623866151749,
                "cvrmse_percent": 60.82471808807241,
                "rms_normalized_rmse_percent": 3.2685976784498894,
                "reference_energy": 3.829702082415949,
                "candidate_energy": 3.8063768075125353,
                "relative_energy_error_percent": 0.6090623866151749,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.897509432386869e-08,
                  "p90": 1.3238964129413944e-05,
                  "p95": 3.6369812733028084e-05,
                  "p99": 0.0001997533836401999,
                  "maximum": 0.0008789403364062309
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02509330492466688,
                  "candidate": 0.02421436458826065
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03099315702333378,
                "cvrmse_percent": 25.03464570759333,
                "rms_normalized_rmse_percent": 4.829390935185187,
                "reference_energy": 6.020367951220578,
                "candidate_energy": 6.018502049128074,
                "relative_energy_error_percent": 0.030993157023333783,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2768459530198015e-05,
                  "p99": 0.0001365129282930866,
                  "maximum": 0.0003824236337095499
                },
                "worst": {
                  "global_sensor_index": 53,
                  "local_sensor_index": 17,
                  "sky_patch_index": 311,
                  "rgb_channel": 0,
                  "reference": 0.003827725537121296,
                  "candidate": 0.003445301903411746
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.18224226559138984,
                "cvrmse_percent": 60.31580107647103,
                "rms_normalized_rmse_percent": 3.225217168981261,
                "reference_energy": 3.8033186480925743,
                "candidate_energy": 3.810249902164518,
                "relative_energy_error_percent": 0.18224226559138984,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.12956283718313e-08,
                  "p90": 1.340738199360209e-05,
                  "p95": 3.944152922485955e-05,
                  "p99": 0.00019624189008027315,
                  "maximum": 0.0005834009498357773
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.025723694823682308,
                  "candidate": 0.026307095773518085
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 211.32958307862282,
            "full": 4947.250582976267
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.46745803486556,
            "full": 4905.826584086753
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.15741699840873,
            "full": 5052.460165927187
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.34308402240276,
            "full": 4800.309374928474
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.018910703900155285,
                "cvrmse_percent": 24.358763370654046,
                "rms_normalized_rmse_percent": 4.6958428121322475,
                "reference_energy": 6.015608922834872,
                "candidate_energy": 6.0167465168260605,
                "relative_energy_error_percent": 0.018910703900155285,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1465151803568006e-05,
                  "p99": 0.00013145845150575042,
                  "maximum": 0.0003958973102271557
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 451,
                  "rgb_channel": 0,
                  "reference": 0.004540647147223353,
                  "candidate": 0.004936544457450509
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.07513179356588236,
                "cvrmse_percent": 60.19808850149055,
                "rms_normalized_rmse_percent": 3.2265007576932607,
                "reference_energy": 3.815083635192888,
                "candidate_energy": 3.817949975954047,
                "relative_energy_error_percent": 0.07513179356588236,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9046375143716432e-08,
                  "p90": 1.3547802154789687e-05,
                  "p95": 3.863705205731094e-05,
                  "p99": 0.00019218685338273644,
                  "maximum": 0.0008108057081699371
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02925167977809906,
                  "candidate": 0.030062485486268997
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0069018826862334865,
                "cvrmse_percent": 24.470404757031456,
                "rms_normalized_rmse_percent": 4.718971510012296,
                "reference_energy": 6.01407289046665,
                "candidate_energy": 6.013657806211086,
                "relative_energy_error_percent": 0.0069018826862334865,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2116180844022892e-05,
                  "p99": 0.00013607449363917112,
                  "maximum": 0.0003918342699762434
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 0.0012925670016556978,
                  "candidate": 0.0009007327316794544
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.059819876429330524,
                "cvrmse_percent": 59.732450174828394,
                "rms_normalized_rmse_percent": 3.211714956450648,
                "reference_energy": 3.8318636542668365,
                "candidate_energy": 3.8341558703697594,
                "relative_energy_error_percent": 0.059819876429330524,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.93354221522668e-08,
                  "p90": 1.3596063672594144e-05,
                  "p95": 3.736980215762742e-05,
                  "p99": 0.0001973514154087752,
                  "maximum": 0.0006351899355649948
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029166920110583305,
                  "candidate": 0.02853173017501831
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.56391597166657,
            "full": 5164.461957989261
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.75275001022965,
            "full": 5185.528417001478
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 212.57500001229346,
            "full": 5217.9976250045
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.52887500729412,
            "full": 5236.072083003819
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0696430378505547,
                "cvrmse_percent": 13.567333168201458,
                "rms_normalized_rmse_percent": 2.61699385435493,
                "reference_energy": 6.013515178381795,
                "candidate_energy": 6.017703173033624,
                "relative_energy_error_percent": 0.0696430378505547,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1596610420383513e-05,
                  "p99": 7.027122774161398e-05,
                  "maximum": 0.00017585197929292917
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 158,
                  "rgb_channel": 0,
                  "reference": 0.0017089549801312387,
                  "candidate": 0.0015331030008383095
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.26061474617618247,
                "cvrmse_percent": 35.378932973523725,
                "rms_normalized_rmse_percent": 1.8991793574260336,
                "reference_energy": 3.8275206429519386,
                "candidate_energy": 3.8175455597434684,
                "relative_energy_error_percent": 0.26061474617618247,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.09540962967003e-08,
                  "p90": 9.02052088349593e-06,
                  "p95": 2.2041069314582273e-05,
                  "p99": 0.00011420244118198752,
                  "maximum": 0.00039732048753648996
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 158,
                  "rgb_channel": 0,
                  "reference": -0.00012036750558763742,
                  "candidate": 0.00027695298194885254
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.010721660900484509,
                "cvrmse_percent": 14.064886697744464,
                "rms_normalized_rmse_percent": 2.712276668175915,
                "reference_energy": 6.014968008274536,
                "candidate_energy": 6.015612912747656,
                "relative_energy_error_percent": 0.010721660900484509,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1441006790846586e-05,
                  "p99": 7.345853373408318e-05,
                  "maximum": 0.00023897795472294092
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 263,
                  "rgb_channel": 0,
                  "reference": 0.0032618314726278186,
                  "candidate": 0.0035008094273507595
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.20010065452118686,
                "cvrmse_percent": 35.111454808826856,
                "rms_normalized_rmse_percent": 1.8849838779327472,
                "reference_energy": 3.831441424000726,
                "candidate_energy": 3.8237746846337046,
                "relative_energy_error_percent": 0.2001006545211869,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.108266355411615e-08,
                  "p90": 9.238319398718898e-06,
                  "p95": 2.2080217604525387e-05,
                  "p99": 0.00011194497346878052,
                  "maximum": 0.0004037246108055115
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02485524956136942,
                  "candidate": 0.024451524950563908
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 339.90491600707173,
            "full": 9316.542125074193
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 342.05125004518777,
            "full": 9334.163208957762
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 344.03845900669694,
            "full": 9179.519500001334
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 343.0270840181038,
            "full": 9236.64604104124
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 9685.585541999899,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 38479.485791991465,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      72,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0192585935522882,
            "cvrmse_percent": 43.337291354767274,
            "rms_normalized_rmse_percent": 2.324383338063202,
            "reference_energy": 3.821981989678928,
            "candidate_energy": 3.783026109805105,
            "relative_energy_error_percent": 1.0192585935522882,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.899181168293593e-06,
              "p95": 1.65949750225991e-05,
              "p99": 4.439591430127621e-05,
              "maximum": 0.0012603290379047394
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02898580953478813,
              "candidate": 0.027725480496883392,
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
            "nmbe_percent": -0.4115364862966312,
            "cvrmse_percent": 16.803955405538915,
            "rms_normalized_rmse_percent": 2.3199678800953816,
            "reference_energy": 9.838142259527498,
            "candidate_energy": 9.797654714555774,
            "relative_energy_error_percent": 0.4115364862966312,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.845733438851327e-06,
              "p95": 1.639546826481819e-05,
              "p99": 4.355842247605324e-05,
              "maximum": 0.0012603290379047394
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02898580953478813,
              "candidate": 0.027725480496883392,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02543982524173226,
            "cvrmse_percent": 2.186229866982566,
            "rms_normalized_rmse_percent": 0.421728360326502,
            "reference_energy": 6.016159105113275,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02543982524173226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0065556864160514,
            "cvrmse_percent": 41.01434626914202,
            "rms_normalized_rmse_percent": 2.201549069125505,
            "reference_energy": 3.8267394206687815,
            "candidate_energy": 3.788221157425715,
            "relative_energy_error_percent": 1.0065556864160514,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0165947242057893e-05,
              "p95": 1.701021392364055e-05,
              "p99": 4.627474118024111e-05,
              "maximum": 0.0011002309620380402
            },
            "worst": {
              "global_sensor_index": 52,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0344960018992424,
              "candidate": 0.03339577093720436,
              "position": [
                2.5,
                1.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4068797773417018,
            "cvrmse_percent": 15.924911963789537,
            "rms_normalized_rmse_percent": 2.19868864586563,
            "reference_energy": 9.842898525782056,
            "candidate_energy": 9.802849762176384,
            "relative_energy_error_percent": 0.40687977734170166,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0149304580409085e-05,
              "p95": 1.6810765373520553e-05,
              "p99": 4.616368096321821e-05,
              "maximum": 0.0011002309620380402
            },
            "worst": {
              "global_sensor_index": 52,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0344960018992424,
              "candidate": 0.03339577093720436,
              "position": [
                2.5,
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
      72,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.40642873218555,
            "cvrmse_percent": 861.9856017948885,
            "rms_normalized_rmse_percent": 32.36762724898505,
            "reference_energy": 2.0739543754565,
            "candidate_energy": 3.783026109805105,
            "relative_energy_error_percent": 82.40642873218556,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.650000093737617e-05,
              "p95": 7.84146441219491e-05,
              "p99": 0.00016508856788277626,
              "maximum": 0.007899546064436436
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010575254447758198,
              "candidate": 0.018474800512194633,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.106500267479397,
            "cvrmse_percent": 220.9608316584804,
            "rms_normalized_rmse_percent": 32.365448243052555,
            "reference_energy": 8.09011464530507,
            "candidate_energy": 9.797654714555774,
            "relative_energy_error_percent": 21.106500267479397,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.6194020339717125e-05,
              "p95": 7.792701944708824e-05,
              "p99": 0.00016413815319538116,
              "maximum": 0.007899546064436436
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010575254447758198,
              "candidate": 0.018474800512194633,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02543982524173226,
            "cvrmse_percent": 2.186229866982566,
            "rms_normalized_rmse_percent": 0.421728360326502,
            "reference_energy": 6.016159105113275,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02543982524173226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.35685094430168,
            "cvrmse_percent": 864.3064053457724,
            "rms_normalized_rmse_percent": 32.472217229849505,
            "reference_energy": 2.0773670623336074,
            "candidate_energy": 3.788221157425715,
            "relative_energy_error_percent": 82.3568509443017,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.592347877154689e-05,
              "p95": 7.899000047473237e-05,
              "p99": 0.00016690336633473635,
              "maximum": 0.007953967899084091
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01118292286992073,
              "candidate": 0.019136890769004822,
              "position": [
                5.5,
                0.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.119640060034694,
            "cvrmse_percent": 221.8375484162005,
            "rms_normalized_rmse_percent": 32.47160855808947,
            "reference_energy": 8.093526167446882,
            "candidate_energy": 9.802849762176384,
            "relative_energy_error_percent": 21.119640060034698,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.601699849648871e-05,
              "p95": 7.899000047473237e-05,
              "p99": 0.00016573630273342133,
              "maximum": 0.007953967899084091
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01118292286992073,
              "candidate": 0.019136890769004822,
              "position": [
                5.5,
                0.5,
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
      "bias_percent": 0.1455680870528431,
      "rms_normalized_error_percent": 0.15873626050364317,
      "absolute_error": {
        "p95": 0.06671528800051083,
        "p99": 0.10585790683248023,
        "maximum": 0.12335284402999447
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.029304533623142,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.15873626050364317
    },
    "overcast": {
      "bias_percent": 0.0904020764465931,
      "rms_normalized_error_percent": 0.10677455922769441,
      "absolute_error": {
        "p95": 0.029107165336608894,
        "p99": 0.04804147243499758,
        "maximum": 0.050356507301330566
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.699631690979004,
      "reference_fraction_of_uniform": 0.6400728821754456,
      "rms_normalized_to_uniform_percent": 0.0759272069666602
    },
    "horizon": {
      "bias_percent": 0.8981083807956313,
      "rms_normalized_error_percent": 1.8585105080168351,
      "absolute_error": {
        "p95": 0.06670985493572161,
        "p99": 0.08742661178803471,
        "maximum": 0.09539463016073513
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4449818492504805,
      "reference_fraction_of_uniform": 0.12012181129936546,
      "rms_normalized_to_uniform_percent": 0.13091557222119088
    },
    "north": {
      "bias_percent": -79.53431536164575,
      "rms_normalized_error_percent": 100.15024003988667,
      "absolute_error": {
        "p95": 3.511620916469845e-05,
        "p99": 0.0001309708126791527,
        "maximum": 0.00021039888088125736
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.821049050311558e-06,
      "reference_fraction_of_uniform": 7.332967015827307e-07,
      "rms_normalized_to_uniform_percent": 0.000140237639608692
    },
    "east": {
      "bias_percent": 0.06212871310025174,
      "rms_normalized_error_percent": 0.17344629960269106,
      "absolute_error": {
        "p95": 0.013385772705078127,
        "p99": 0.020288822650909477,
        "maximum": 0.02619338035583496
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.275853157043457,
      "reference_fraction_of_uniform": 0.18919241428375244,
      "rms_normalized_to_uniform_percent": 0.03487101331045689
    },
    "south": {
      "bias_percent": 0.20137234743048277,
      "rms_normalized_error_percent": 0.22762356512351362,
      "absolute_error": {
        "p95": 0.0752124309539795,
        "p99": 0.10182176828384415,
        "maximum": 0.11895346641540527
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.367470741271973,
      "reference_fraction_of_uniform": 0.6955905556678772,
      "rms_normalized_to_uniform_percent": 0.14870851476724903
    },
    "west": {
      "bias_percent": 0.07531966214255427,
      "rms_normalized_error_percent": 0.18584944592228436,
      "absolute_error": {
        "p95": 0.014418384432792666,
        "p99": 0.02231110811233525,
        "maximum": 0.027039527893066406
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3027193546295166,
      "reference_fraction_of_uniform": 0.19142581522464752,
      "rms_normalized_to_uniform_percent": 0.037653688747351165
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
        "identifier": "stacked_rooms_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.056401643515646006,
          "cvrmse_percent": 1.758320000173245,
          "absolute_error_percentiles_lux": {
            "p50": 1.8601417541503906,
            "p90": 22.74541931152344,
            "p95": 35.57631225585937,
            "p99": 80.7117700195312
          },
          "maximum_absolute_error_lux": 378.96875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2724.5,
            "foton_lux": 40966.11328125,
            "radiance_lux": 40587.14453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3036415525114155,
            "maximum_error_percentage_points": 1.4269863013698654,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11265131647547319,
            "maximum_error_percentage_points": 0.6576560671362301,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08851978691019813,
            "maximum_error_percentage_points": 0.4365753424657548,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0946955859969556,
            "maximum_error_percentage_points": 0.43890410958904624,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0249162861491627,
            "maximum_error_percentage_points": 0.11273972602739679,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 55.55555555555556,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.03046642475540953,
          "cvrmse_percent": 1.7025793410060674,
          "absolute_error_percentiles_lux": {
            "p50": 1.8628158569335938,
            "p90": 22.710943603515624,
            "p95": 35.57065887451164,
            "p99": 74.96415771484368
          },
          "maximum_absolute_error_lux": 360.9423828125,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              3.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 15140.396484375,
            "radiance_lux": 15501.3388671875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2699162861491613,
            "maximum_error_percentage_points": 0.8509589041095893,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09427622380306389,
            "maximum_error_percentage_points": 0.36484526325583033,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07153729071537279,
            "maximum_error_percentage_points": 0.27876712328767184,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08738584474885809,
            "maximum_error_percentage_points": 0.2976712328767235,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.025292998477929898,
            "maximum_error_percentage_points": 0.10465753424657542,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 55.55555555555556,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004924282962321058,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004739137414375705,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
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
      "study_preparation_seconds": 0.010614707949571311,
      "weather_seconds": 0.11232291697524488,
      "metric_reduction_seconds": 0.2172189170960337,
      "write_seconds": 0.05186558293644339,
      "total_seconds": 0.3816063749836758,
      "cold_end_to_end_seconds": 0.3922210829332471,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.020880750031210482,
      "engine_upload_seconds": 0.00082675,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.16512958309613168,
      "engine_annual_reduction_seconds": 0.0031841250602155924,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.16512958309613168
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.010614707949571311,
      "weather_seconds": 0.11284770793281496,
      "metric_reduction_seconds": 0.045365541940554976,
      "write_seconds": 0.045182500034570694,
      "total_seconds": 0.20356049994006753,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.20356049994006753,
      "raw_export_seconds": 0.021228166995570064,
      "engine_upload_seconds": 7.8542e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031616666819900274,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01138137502130121,
      "full": 0.1560966249089688
    }
  },
  "elapsed_seconds": 134.2418595419731,
  "result_class": "passed"
}
```
