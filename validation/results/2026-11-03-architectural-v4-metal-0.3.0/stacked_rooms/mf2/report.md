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
  "model_sha256": "4bfac668c37ffc604342292b499e2b090d664248f9834ac469cdbb2450989615",
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
      "solver_version": "0.3.0",
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
        "bias_percent": 0.056851179140817346,
        "rms_normalized_error_percent": 1.7250598697334545,
        "absolute_error": {
          "p95": 2.0654406398534775e-05,
          "p99": 0.00010097899939864874,
          "maximum": 0.0005105752497911453
        },
        "worst_index": [
          14,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": 0.08826729836398464,
        "rms_normalized_error_percent": 1.7059307492124838,
        "absolute_error": {
          "p95": 2.1077808924019337e-05,
          "p99": 0.00010604807175695896,
          "maximum": 0.0003206904511898756
        },
        "worst_index": [
          16,
          212,
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
        "bias_percent": -0.03125615521826078,
        "rms_normalized_error_percent": 1.4111707443632402,
        "absolute_error": {
          "p95": 1.726584741845727e-05,
          "p99": 7.937522605061531e-05,
          "maximum": 0.0005003772675991058
        },
        "worst_index": [
          22,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.032344802902103086,
        "rms_normalized_error_percent": 1.417501824418293,
        "absolute_error": {
          "p95": 1.8320984963793308e-05,
          "p99": 8.138734847307205e-05,
          "maximum": 0.0003219805657863617
        },
        "worst_index": [
          9,
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
                "nmbe_percent": -0.10503137026927324,
                "cvrmse_percent": 50.24571413373553,
                "rms_normalized_rmse_percent": 9.6832826654551,
                "reference_energy": 6.022063674730816,
                "candidate_energy": 6.015738618734758,
                "relative_energy_error_percent": 0.10503137026927326,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.463200457394123e-05,
                  "p99": 0.00026280595920979977,
                  "maximum": 0.0007735990220680833
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 318,
                  "rgb_channel": 0,
                  "reference": 0.0035375439329072833,
                  "candidate": 0.004311142954975367
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.9691836956279491,
                "cvrmse_percent": 210.26533785934393,
                "rms_normalized_rmse_percent": 7.869687089057912,
                "reference_energy": 2.064693236421512,
                "candidate_energy": 2.084703906633642,
                "relative_energy_error_percent": 0.9691836956279494,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.6237908211187565e-06,
                  "p95": 5.568329288507812e-05,
                  "p99": 0.00037117768079042435,
                  "maximum": 0.0012180487683508545
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 88,
                  "rgb_channel": 0,
                  "reference": 0.0007032177236396819,
                  "candidate": -0.0005148310447111726
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
                "nmbe_percent": 0.10434306967952306,
                "cvrmse_percent": 44.06449132174838,
                "rms_normalized_rmse_percent": 8.484605827983584,
                "reference_energy": 6.011404168939407,
                "candidate_energy": 6.017676652580121,
                "relative_energy_error_percent": 0.10434306967952306,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.383050327305682e-05,
                  "p99": 0.00023420143406838179,
                  "maximum": 0.000595927587710321
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 267,
                  "rgb_channel": 0,
                  "reference": 0.003261824487708509,
                  "candidate": 0.00385775207541883
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.6486780235054177,
                "cvrmse_percent": 182.47500633843177,
                "rms_normalized_rmse_percent": 6.8724373614726915,
                "reference_energy": 2.094314751546534,
                "candidate_energy": 2.0807293920102197,
                "relative_energy_error_percent": 0.6486780235054177,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.618767045234566e-06,
                  "p95": 5.325862730387598e-05,
                  "p99": 0.0003380808739166241,
                  "maximum": 0.001136135309934616
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028275270015001297,
                  "candidate": 0.02713913470506668
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.2996249953285,
            "full": 436.30595807917416
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.11691703554243,
            "full": 416.95929097477347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.83016606979072,
            "full": 428.220291971229
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.93691606633365,
            "full": 426.63929203990847
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
                "nmbe_percent": -0.05096138622622892,
                "cvrmse_percent": 25.237741546575098,
                "rms_normalized_rmse_percent": 4.864269351478906,
                "reference_energy": 6.016110666262648,
                "candidate_energy": 6.0130447728702165,
                "relative_energy_error_percent": 0.05096138622622893,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2553896997123957e-05,
                  "p99": 0.00013767342898063362,
                  "maximum": 0.0003795101074501872
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 310,
                  "rgb_channel": 0,
                  "reference": 0.0035643085138872266,
                  "candidate": 0.003943818621337414
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.22031188814494287,
                "cvrmse_percent": 60.85528596332696,
                "rms_normalized_rmse_percent": 3.2650174084638106,
                "reference_energy": 3.81423114787761,
                "candidate_energy": 3.8226343525377118,
                "relative_energy_error_percent": 0.22031188814494293,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4564079720003065e-08,
                  "p90": 1.3364655387704345e-05,
                  "p95": 3.697240026667714e-05,
                  "p99": 0.00020164193119853735,
                  "maximum": 0.0006774095818400383
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.025958379730582237,
                  "candidate": 0.0252809701487422
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
                "nmbe_percent": -0.059189586716957066,
                "cvrmse_percent": 26.813206188368994,
                "rms_normalized_rmse_percent": 5.172848526559833,
                "reference_energy": 6.015639756717519,
                "candidate_energy": 6.012079124407137,
                "relative_energy_error_percent": 0.05918958671695707,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.255065192002803e-05,
                  "p99": 0.00013913004659116268,
                  "maximum": 0.0004682451253756881
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 13,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.0007952413870953023,
                  "candidate": 0.0012634865124709904
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.08761055085195822,
                "cvrmse_percent": 63.53356146789333,
                "rms_normalized_rmse_percent": 3.408492614860266,
                "reference_energy": 3.8200630720055493,
                "candidate_energy": 3.8234098503058256,
                "relative_energy_error_percent": 0.08761055085195821,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.366908802287071e-08,
                  "p90": 1.334927310381318e-05,
                  "p95": 3.674966865219176e-05,
                  "p99": 0.0002066462766379118,
                  "maximum": 0.0007088091224431992
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.021284104324877262,
                  "candidate": 0.020575295202434063
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 226.973665994592,
            "full": 5127.430583001114
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 225.60220793820918,
            "full": 4958.138665999286
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 222.4714590702206,
            "full": 4879.717999952845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.20520905405283,
            "full": 4913.423583959229
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
                "nmbe_percent": -0.028267823575158103,
                "cvrmse_percent": 23.38462310470287,
                "rms_normalized_rmse_percent": 4.510725600666004,
                "reference_energy": 6.014131486740553,
                "candidate_energy": 6.012431422662303,
                "relative_energy_error_percent": 0.0282678235751581,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.166602644138038e-05,
                  "p99": 0.0001343139447271824,
                  "maximum": 0.0003725888964254409
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 88,
                  "rgb_channel": 0,
                  "reference": 0.0012804559664800763,
                  "candidate": 0.0009078670700546354
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.22274547070333053,
                "cvrmse_percent": 57.21642333016022,
                "rms_normalized_rmse_percent": 3.0703806000919367,
                "reference_energy": 3.8210635923316048,
                "candidate_energy": 3.8295748384162174,
                "relative_energy_error_percent": 0.2227454707033305,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.1897038848806005e-08,
                  "p90": 1.3094685436954085e-05,
                  "p95": 3.4127209801226854e-05,
                  "p99": 0.00018855600501410663,
                  "maximum": 0.0005817357450723648
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028611394576728344,
                  "candidate": 0.02919313032180071
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
                "nmbe_percent": 0.06700424718501687,
                "cvrmse_percent": 23.993450635756627,
                "rms_normalized_rmse_percent": 4.623454987678183,
                "reference_energy": 6.014956814293328,
                "candidate_energy": 6.018987090825249,
                "relative_energy_error_percent": 0.06700424718501688,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2556450858246535e-05,
                  "p99": 0.00012913299724459648,
                  "maximum": 0.0003956813598051667
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "sky_patch_index": 88,
                  "rgb_channel": 0,
                  "reference": 0.0009310181485489011,
                  "candidate": 0.0013266995083540678
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.20173941488155117,
                "cvrmse_percent": 58.46948041538442,
                "rms_normalized_rmse_percent": 3.1422936886059794,
                "reference_energy": 3.831170034845396,
                "candidate_energy": 3.8234410548339817,
                "relative_energy_error_percent": 0.20173941488155114,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.3295797291211784e-08,
                  "p90": 1.3174070409149876e-05,
                  "p95": 3.3423901186324656e-05,
                  "p99": 0.00019591848831623793,
                  "maximum": 0.0007696999236941338
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.026127370074391365,
                  "candidate": 0.02535767015069723
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.6420000353828,
            "full": 5244.2854170221835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.02145897224545,
            "full": 5296.327791991644
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.3502079937607,
            "full": 5228.216041927226
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 212.76383404619992,
            "full": 5270.456874975935
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
                "nmbe_percent": 0.03115382030592102,
                "cvrmse_percent": 13.905725897804603,
                "rms_normalized_rmse_percent": 2.6822767434045502,
                "reference_energy": 6.014918099428542,
                "candidate_energy": 6.016791976204786,
                "relative_energy_error_percent": 0.03115382030592102,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1495430953800678e-05,
                  "p99": 7.030559936538339e-05,
                  "maximum": 0.00020145997405052185
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 145,
                  "rgb_channel": 0,
                  "reference": 0.0015651024878025055,
                  "candidate": 0.0017665624618530273
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.0887644166848391,
                "cvrmse_percent": 35.14374407416041,
                "rms_normalized_rmse_percent": 1.8863952550495895,
                "reference_energy": 3.8213664559735996,
                "candidate_energy": 3.8179744423295645,
                "relative_energy_error_percent": 0.0887644166848391,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.5776927259357763e-08,
                  "p90": 9.150956248049632e-06,
                  "p95": 2.3787682948750444e-05,
                  "p99": 0.00011280993930995464,
                  "maximum": 0.0004177801311016083
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0343485102057457,
                  "candidate": 0.03393073007464409
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
                "nmbe_percent": 0.031524227057295004,
                "cvrmse_percent": 13.730979617795589,
                "rms_normalized_rmse_percent": 2.647932763693954,
                "reference_energy": 6.014249695356739,
                "candidate_energy": 6.016145641086496,
                "relative_energy_error_percent": 0.031524227057295004,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1503463611006737e-05,
                  "p99": 7.104664109647274e-05,
                  "maximum": 0.00020741898333653808
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 208,
                  "rgb_channel": 0,
                  "reference": 0.0015879279817454517,
                  "candidate": 0.0013805089984089136
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.07068696347873761,
                "cvrmse_percent": 34.81169895941436,
                "rms_normalized_rmse_percent": 1.8695551895061706,
                "reference_energy": 3.8272484138789373,
                "candidate_energy": 3.824543048190378,
                "relative_energy_error_percent": 0.07068696347873762,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.4524069885956123e-08,
                  "p90": 9.43587347137516e-06,
                  "p95": 2.2953499865252525e-05,
                  "p99": 0.00011368724517524242,
                  "maximum": 0.000492519699037075
                },
                "worst": {
                  "global_sensor_index": 53,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02889471035450697,
                  "candidate": 0.029387230053544044
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 347.25895803421736,
            "full": 9422.60254197754
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 355.18600000068545,
            "full": 9632.536333054304
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 367.2434160253033,
            "full": 9496.275874902494
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 381.5317079424858,
            "full": 9894.39058303833
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 11896.264374954626,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 47293.08237496298,
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
            "nmbe_percent": -0.9514439847451766,
            "cvrmse_percent": 39.91062292929937,
            "rms_normalized_rmse_percent": 2.142588867127769,
            "reference_energy": 3.8193652305465893,
            "candidate_energy": 3.783026109805105,
            "relative_energy_error_percent": 0.9514439847451764,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0024784569395714e-05,
              "p95": 1.63012882694602e-05,
              "p99": 4.860933404415846e-05,
              "maximum": 0.0008931495249271393
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02861863002181053,
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
            "nmbe_percent": -0.3850407976458706,
            "cvrmse_percent": 15.477438222341117,
            "rms_normalized_rmse_percent": 2.139714330733016,
            "reference_energy": 9.835525500395159,
            "candidate_energy": 9.797654714555774,
            "relative_energy_error_percent": 0.38504079764587057,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.000580068648561e-05,
              "p95": 1.6163656255230308e-05,
              "p99": 4.7686509788036346e-05,
              "maximum": 0.0008931495249271393
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02861863002181053,
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
            "nmbe_percent": -0.9598372552103696,
            "cvrmse_percent": 39.82505151204278,
            "rms_normalized_rmse_percent": 2.13776922149091,
            "reference_energy": 3.8249343018421165,
            "candidate_energy": 3.788221157425715,
            "relative_energy_error_percent": 0.9598372552103694,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0045795352198184e-05,
              "p95": 1.643858922761865e-05,
              "p99": 4.5200344175100327e-05,
              "maximum": 0.0011569038033485413
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026592154055833817,
              "candidate": 0.025435250252485275,
              "position": [
                3.5,
                3.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3886117446256246,
            "cvrmse_percent": 15.46268079812366,
            "rms_normalized_rmse_percent": 2.135544563211247,
            "reference_energy": 9.841093406955391,
            "candidate_energy": 9.802849762176384,
            "relative_energy_error_percent": 0.38861174462562453,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0042371286544966e-05,
              "p95": 1.6522593796253204e-05,
              "p99": 4.481369978748262e-05,
              "maximum": 0.0011569038033485413
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026592154055833817,
              "candidate": 0.025435250252485275,
              "position": [
                3.5,
                3.5,
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
            "nmbe_percent": 82.10042590000172,
            "cvrmse_percent": 862.7214365730053,
            "rms_normalized_rmse_percent": 32.42459571116547,
            "reference_energy": 2.077439462927181,
            "candidate_energy": 3.783026109805105,
            "relative_energy_error_percent": 82.10042590000172,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.6262536008944225e-05,
              "p95": 7.750000077066943e-05,
              "p99": 0.00016860151663422585,
              "maximum": 0.007861490361392498
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010613310150802135,
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
            "nmbe_percent": 21.05435205646879,
            "cvrmse_percent": 221.43668554534105,
            "rms_normalized_rmse_percent": 32.42402295294025,
            "reference_energy": 8.09359973277575,
            "candidate_energy": 9.797654714555774,
            "relative_energy_error_percent": 21.05435205646879,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.6243200015160335e-05,
              "p95": 7.762000313960016e-05,
              "p99": 0.00016844389028847218,
              "maximum": 0.007861490361392498
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010613310150802135,
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
            "nmbe_percent": 81.6105755256622,
            "cvrmse_percent": 855.119807177086,
            "rms_normalized_rmse_percent": 32.18990140571365,
            "reference_energy": 2.0859033932693123,
            "candidate_energy": 3.788221157425715,
            "relative_energy_error_percent": 81.61057552566221,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.583099919022074e-05,
              "p95": 7.773999823257327e-05,
              "p99": 0.0001587884034961462,
              "maximum": 0.007748030126094818
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011388860642910004,
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
            "nmbe_percent": 20.99202843884906,
            "cvrmse_percent": 220.1481829243121,
            "rms_normalized_rmse_percent": 32.189125929040195,
            "reference_energy": 8.102062498382587,
            "candidate_energy": 9.802849762176384,
            "relative_energy_error_percent": 20.992028438849065,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.5774000793462706e-05,
              "p95": 7.757999992463738e-05,
              "p99": 0.00015863659791648388,
              "maximum": 0.007748030126094818
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011388860642910004,
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
      "bias_percent": 0.14268227358104912,
      "rms_normalized_error_percent": 0.1672090842251863,
      "absolute_error": {
        "p95": 0.07486519575170406,
        "p99": 0.1096959293219789,
        "maximum": 0.11899649770146015
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.029651182307711,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1672090842251863
    },
    "overcast": {
      "bias_percent": 0.0940683509330097,
      "rms_normalized_error_percent": 0.11762101807185847,
      "absolute_error": {
        "p95": 0.03747451305389405,
        "p99": 0.05118327498435974,
        "maximum": 0.051425933837890625
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.699350357055664,
      "reference_fraction_of_uniform": 0.6400310397148132,
      "rms_normalized_to_uniform_percent": 0.08364228018878171
    },
    "horizon": {
      "bias_percent": 1.106443255113515,
      "rms_normalized_error_percent": 1.8811011453507984,
      "absolute_error": {
        "p95": 0.06043552167090497,
        "p99": 0.09010686095567164,
        "maximum": 0.10253818456546826
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.442004392005786,
      "reference_fraction_of_uniform": 0.11987083998965617,
      "rms_normalized_to_uniform_percent": 0.13220441707165273
    },
    "north": {
      "bias_percent": -86.42344235685329,
      "rms_normalized_error_percent": 99.52705490306381,
      "absolute_error": {
        "p95": 4.709764780272965e-05,
        "p99": 0.0002391346902390981,
        "maximum": 0.0002675560256193421
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.329709903075127e-05,
      "reference_fraction_of_uniform": 1.1053602975152899e-06,
      "rms_normalized_to_uniform_percent": 0.0002068901214835672
    },
    "east": {
      "bias_percent": 0.07084802420994728,
      "rms_normalized_error_percent": 0.20388707722820357,
      "absolute_error": {
        "p95": 0.017706680297851562,
        "p99": 0.028767242431640687,
        "maximum": 0.03578615188598633
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2756550312042236,
      "reference_fraction_of_uniform": 0.1891704797744751,
      "rms_normalized_to_uniform_percent": 0.04099084813771096
    },
    "south": {
      "bias_percent": 0.18958487511283775,
      "rms_normalized_error_percent": 0.23042861672842624,
      "absolute_error": {
        "p95": 0.0702613711357117,
        "p99": 0.10560057878494268,
        "maximum": 0.11245918273925781
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.368454933166504,
      "reference_fraction_of_uniform": 0.6956523060798645,
      "rms_normalized_to_uniform_percent": 0.15055168508466318
    },
    "west": {
      "bias_percent": 0.07899418327846894,
      "rms_normalized_error_percent": 0.1987604896862719,
      "absolute_error": {
        "p95": 0.01661469042301179,
        "p99": 0.019568970203399667,
        "maximum": 0.020525217056274414
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3026347160339355,
      "reference_fraction_of_uniform": 0.1914132535457611,
      "rms_normalized_to_uniform_percent": 0.040268624046862767
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
          "nmbe_percent": 0.02237832420426149,
          "cvrmse_percent": 1.7755617269485964,
          "absolute_error_percentiles_lux": {
            "p50": 1.9015045166015625,
            "p90": 23.168945312500007,
            "p95": 36.65395355224607,
            "p99": 80.52507812499994
          },
          "maximum_absolute_error_lux": 542.15234375,
          "worst": {
            "sensor_index": 10,
            "position": [
              1.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2674.5,
            "foton_lux": 18489.263671875,
            "radiance_lux": 19031.416015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.26862633181126305,
            "maximum_error_percentage_points": 1.2352054794520555,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09888358606974022,
            "maximum_error_percentage_points": 0.5887752002722095,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08866438356164391,
            "maximum_error_percentage_points": 0.4639726027397266,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09762557077625583,
            "maximum_error_percentage_points": 0.46630136986301807,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.022519025875190432,
            "maximum_error_percentage_points": 0.0871232876712329,
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
          "nmbe_percent": 0.045276705514071744,
          "cvrmse_percent": 1.7253730401884086,
          "absolute_error_percentiles_lux": {
            "p50": 1.940155029296875,
            "p90": 22.820489501953137,
            "p95": 35.60753936767577,
            "p99": 78.15702636718679
          },
          "maximum_absolute_error_lux": 384.890625,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              3.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 12596.5009765625,
            "radiance_lux": 12981.3916015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3027777777777779,
            "maximum_error_percentage_points": 1.0649315068493195,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11159185017958745,
            "maximum_error_percentage_points": 0.39886756026589865,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07882800608828013,
            "maximum_error_percentage_points": 0.3310958904109569,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08708143074581444,
            "maximum_error_percentage_points": 0.32684931506848613,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02514079147640795,
            "maximum_error_percentage_points": 0.08287671232876725,
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
      "study_preparation_seconds": 0.01178883295506239,
      "weather_seconds": 0.14420350000727922,
      "metric_reduction_seconds": 0.22307141695637256,
      "write_seconds": 0.032025333028286695,
      "total_seconds": 0.3995987920789048,
      "cold_end_to_end_seconds": 0.4113876250339672,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01968754199333489,
      "engine_upload_seconds": 0.000814125,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.16766920825466514,
      "engine_annual_reduction_seconds": 0.0033551249653100967,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.16766920825466514
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.01178883295506239,
      "weather_seconds": 0.11908654100261629,
      "metric_reduction_seconds": 0.048179166042245924,
      "write_seconds": 0.0582496669376269,
      "total_seconds": 0.22569791693240404,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.22569791693240404,
      "raw_export_seconds": 0.031653417041525245,
      "engine_upload_seconds": 7.9834e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031181250233203173,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.023228459060192108,
      "full": 0.16476295900065452
    }
  },
  "elapsed_seconds": 147.71089658304118,
  "result_class": "passed"
}
```
