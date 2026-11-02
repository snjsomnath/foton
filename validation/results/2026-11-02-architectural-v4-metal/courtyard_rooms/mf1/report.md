# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_rooms",
    "category": "connections",
    "question": "Do four inward-facing rooms shade one another beneath a pergola?",
    "interactions": [
      "multiroom_context",
      "courtyard",
      "combined_shading"
    ],
    "room_count": 4,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 4,
    "apertures": 4,
    "shades": 4,
    "sensors": 112,
    "floor_area": 112.0,
    "aperture_area": 17.999999999999996
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "737b82fa2d38d04afbb827f4135a443643b051683e395176dec1609c75cebfad",
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
      "scene_fingerprint": 16353448696249269853,
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
      "scene_fingerprint": 16353448696249269853,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.15601013692746718,
        "rms_normalized_error_percent": 2.6080787134746615,
        "absolute_error": {
          "p95": 5.2641611546278e-05,
          "p99": 0.00025876224972307723,
          "maximum": 0.0006226329132914543
        },
        "worst_index": [
          20,
          64,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.006317229002769663,
        "rms_normalized_error_percent": 2.750563290721376,
        "absolute_error": {
          "p95": 6.438465788960457e-05,
          "p99": 0.0002754469634965063,
          "maximum": 0.0006568883545696735
        },
        "worst_index": [
          4,
          56,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.052938446660532275,
        "rms_normalized_error_percent": 2.9311502537615928,
        "absolute_error": {
          "p95": 6.779102113796398e-05,
          "p99": 0.0003074812702834606,
          "maximum": 0.0009097978472709656
        },
        "worst_index": [
          11,
          119,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": -0.2635397678381154,
        "rms_normalized_error_percent": 2.7297397091358873,
        "absolute_error": {
          "p95": 8.244859054684639e-05,
          "p99": 0.0002848142758011818,
          "maximum": 0.000855528749525547
        },
        "worst_index": [
          8,
          64,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.10410892309417183,
        "rms_normalized_error_percent": 1.1231761550197505,
        "absolute_error": {
          "p95": 5.399249494075775e-05,
          "p99": 0.00016487007960677163,
          "maximum": 0.0008225180208683014
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": 0.10558756839031988,
        "rms_normalized_error_percent": 1.0230713544801582,
        "absolute_error": {
          "p95": 5.422579124569893e-05,
          "p99": 0.00015723980031907562,
          "maximum": 0.0005059652030467987
        },
        "worst_index": [
          12,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": 0.11057981861898947,
        "rms_normalized_error_percent": 1.008135139588933,
        "absolute_error": {
          "p95": 7.33816486899741e-05,
          "p99": 0.00018317019566893578,
          "maximum": 0.0004562661051750183
        },
        "worst_index": [
          13,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.06740841523270134,
        "rms_normalized_error_percent": 1.2160959071297093,
        "absolute_error": {
          "p95": 7.822643965482712e-05,
          "p99": 0.0002245921641588211,
          "maximum": 0.0007889196276664734
        },
        "worst_index": [
          6,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.02663230675950431,
        "rms_normalized_error_percent": 0.8820501317527252,
        "absolute_error": {
          "p95": 4.6726068831048906e-05,
          "p99": 0.0001488769426941872,
          "maximum": 0.0005609653890132904
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.019152647857112945,
        "rms_normalized_error_percent": 0.8982737446230836,
        "absolute_error": {
          "p95": 4.6304427087306976e-05,
          "p99": 0.00013619819073937842,
          "maximum": 0.0005390271544456482
        },
        "worst_index": [
          3,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.022981802509116685,
        "rms_normalized_error_percent": 0.9158799670014818,
        "absolute_error": {
          "p95": 6.47595152258873e-05,
          "p99": 0.00017173215746879578,
          "maximum": 0.0004292801022529602
        },
        "worst_index": [
          5,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.008353370664726344,
        "rms_normalized_error_percent": 0.9880120637992794,
        "absolute_error": {
          "p95": 6.210803985595703e-05,
          "p99": 0.00017660297453403473,
          "maximum": 0.000565897673368454
        },
        "worst_index": [
          6,
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
        "run_count": 12,
        "half_run_count": 6,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15938258802343122,
                "cvrmse_percent": 9.12428919666158,
                "rms_normalized_rmse_percent": 1.972692257677287,
                "reference_energy": 5.720001734793669,
                "candidate_energy": 5.729118421593569,
                "relative_energy_error_percent": 0.15938258802343097,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.582365964883743e-07,
                  "p95": 4.4251287666460457e-05,
                  "p99": 0.000218970396478351,
                  "maximum": 0.00043678275930384737
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 36,
                  "rgb_channel": 0,
                  "reference": 0.005417355025808017,
                  "candidate": 0.005854137785111864
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.4125379530890716,
                "cvrmse_percent": 34.16698758124221,
                "rms_normalized_rmse_percent": 2.1178651733355913,
                "reference_energy": 2.4047305162361994,
                "candidate_energy": 2.3948100901872102,
                "relative_energy_error_percent": 0.41253795308907354,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.169845048338175e-06,
                  "p90": 3.940011735418618e-05,
                  "p95": 9.729363773658407e-05,
                  "p99": 0.00032897458877414527,
                  "maximum": 0.0005633902425567309
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 65,
                  "rgb_channel": 0,
                  "reference": 0.0003352918041249116,
                  "candidate": -0.0002280984384318193
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03337603969732176,
                "cvrmse_percent": 8.87003136153041,
                "rms_normalized_rmse_percent": 1.9187185222769298,
                "reference_energy": 5.726195539448128,
                "candidate_energy": 5.724284362151735,
                "relative_energy_error_percent": 0.033376039697321364,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.235467738714456e-07,
                  "p95": 5.014582954269525e-05,
                  "p99": 0.0002015168157716593,
                  "maximum": 0.00048375393574436477
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 13,
                  "sky_patch_index": 57,
                  "rgb_channel": 0,
                  "reference": 0.004486912861466408,
                  "candidate": 0.0049706667972107725
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.058525757415645835,
                "cvrmse_percent": 33.77387088877068,
                "rms_normalized_rmse_percent": 2.092143875250163,
                "reference_energy": 2.401014334074361,
                "candidate_energy": 2.4024195458990363,
                "relative_energy_error_percent": 0.0585257574156454,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.120833174667496e-06,
                  "p90": 3.833136308154887e-05,
                  "p95": 8.458209534486019e-05,
                  "p99": 0.00030469750054180607,
                  "maximum": 0.0009811079750458376
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.039635419845581055,
                  "candidate": 0.04061652782062689
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.010194066609356624,
                "cvrmse_percent": 8.233793455066358,
                "rms_normalized_rmse_percent": 2.0088045366122214,
                "reference_energy": 5.35391174710044,
                "candidate_energy": 5.354457528430146,
                "relative_energy_error_percent": 0.010194066609357209,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.6466017617300785e-06,
                  "p95": 7.309190308054346e-05,
                  "p99": 0.00021684588864445686,
                  "maximum": 0.0004991989117115736
                },
                "worst": {
                  "global_sensor_index": 76,
                  "local_sensor_index": 12,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0061606642169257,
                  "candidate": 0.005661465305214127
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.27309313296569154,
                "cvrmse_percent": 32.346996977809425,
                "rms_normalized_rmse_percent": 2.2150360508798363,
                "reference_energy": 2.266482741339747,
                "candidate_energy": 2.2602931326132953,
                "relative_energy_error_percent": 0.27309313296569426,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.856883409355458e-06,
                  "p90": 4.799489988727146e-05,
                  "p95": 0.0001178047969006002,
                  "p99": 0.0003303891668717066,
                  "maximum": 0.0008182538052399907
                },
                "worst": {
                  "global_sensor_index": 79,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0470014667759339,
                  "candidate": 0.04618321297069391
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.050862931196798654,
                "cvrmse_percent": 9.546624951834811,
                "rms_normalized_rmse_percent": 2.2913342588397696,
                "reference_energy": 5.353573052526656,
                "candidate_energy": 5.356296036704933,
                "relative_energy_error_percent": 0.05086293119679869,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.258052962948568e-06,
                  "p95": 9.385841743399698e-05,
                  "p99": 0.000263992541780075,
                  "maximum": 0.00045383418910205364
                },
                "worst": {
                  "global_sensor_index": 99,
                  "local_sensor_index": 11,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.005817038317521413,
                  "candidate": 0.0062708725066234665
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.27282072921871925,
                "cvrmse_percent": 35.78868452157966,
                "rms_normalized_rmse_percent": 2.4098742445641568,
                "reference_energy": 2.1971974450308736,
                "candidate_energy": 2.1912030349389653,
                "relative_energy_error_percent": 0.27282072921871775,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.962435721727463e-06,
                  "p90": 5.14391128187223e-05,
                  "p95": 0.00013284990563988686,
                  "p99": 0.00038977044944961864,
                  "maximum": 0.0008397896308451891
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 61,
                  "rgb_channel": 0,
                  "reference": -0.0005008329171687365,
                  "candidate": 0.00033895671367645264
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.1450829692185,
            "full": 550.1520000398159
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 181.64508300833404,
            "full": 538.5972911026329
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.56950002815574,
            "full": 541.7585000395775
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 169.8191249743104,
            "full": 532.9067079583183
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.00820890907198,
            "full": 548.0456670047715
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 176.7525839386508,
            "full": 534.9722499959171
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 171.56912491191179,
            "full": 542.5851249601692
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.974916937761,
            "full": 527.879707980901
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 170.2123750001192,
            "full": 544.3172089289874
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 175.93799997121096,
            "full": 537.8802090417594
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 172.74800001177937,
            "full": 553.2951249042526
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 172.77754098176956,
            "full": 526.558291981928
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0895954514081426,
                "cvrmse_percent": 9.1103401590944,
                "rms_normalized_rmse_percent": 1.9706945088556367,
                "reference_energy": 5.716924676879593,
                "candidate_energy": 5.722046781350507,
                "relative_energy_error_percent": 0.0895954514081426,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.239876478910446e-07,
                  "p95": 4.635658115148544e-05,
                  "p99": 0.00020526689477264886,
                  "maximum": 0.0004719048738479614
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 65,
                  "rgb_channel": 0,
                  "reference": 0.008593159262090921,
                  "candidate": 0.009065064135938883
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.018373811935627257,
                "cvrmse_percent": 18.986292379929175,
                "rms_normalized_rmse_percent": 1.737331264528299,
                "reference_energy": 4.3851720141192345,
                "candidate_energy": 4.3843662908603065,
                "relative_energy_error_percent": 0.018373811935627257,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.089086754291202e-05,
                  "p90": 4.756805719807744e-05,
                  "p95": 9.448034688830376e-05,
                  "p99": 0.0003020673175342394,
                  "maximum": 0.0007403064519166946
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04137827083468437,
                  "candidate": 0.04063796438276768
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.14570258528966246,
                "cvrmse_percent": 8.811204069633408,
                "rms_normalized_rmse_percent": 1.9056455215319854,
                "reference_energy": 5.726927140647376,
                "candidate_energy": 5.735271421548955,
                "relative_energy_error_percent": 0.14570258528966246,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.575014879217633e-07,
                  "p95": 4.833005368709564e-05,
                  "p99": 0.00019282677676528726,
                  "maximum": 0.0005217588040977716
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 17,
                  "sky_patch_index": 51,
                  "rgb_channel": 0,
                  "reference": 0.0059109029825776815,
                  "candidate": 0.00538914417847991
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.22454811939259373,
                "cvrmse_percent": 19.143037726130352,
                "rms_normalized_rmse_percent": 1.7508378357537269,
                "reference_energy": 4.388355592737923,
                "candidate_energy": 4.378501622782171,
                "relative_energy_error_percent": 0.22454811939259375,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1357727089489345e-05,
                  "p90": 5.1545277983677806e-05,
                  "p95": 9.647756814956665e-05,
                  "p99": 0.0002703146979911263,
                  "maximum": 0.0008594393730163574
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04956399090588093,
                  "candidate": 0.050423430278897285
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.12114113170939174,
                "cvrmse_percent": 8.258039613699609,
                "rms_normalized_rmse_percent": 2.015601728655963,
                "reference_energy": 5.361743904870096,
                "candidate_energy": 5.355248627624377,
                "relative_energy_error_percent": 0.12114113170939174,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.133289505465655e-06,
                  "p95": 6.792042404413223e-05,
                  "p99": 0.00022586050909012556,
                  "maximum": 0.000649772584438324
                },
                "worst": {
                  "global_sensor_index": 81,
                  "local_sensor_index": 17,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.006151129025965929,
                  "candidate": 0.006800901610404253
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2867403211587775,
                "cvrmse_percent": 19.176012248196795,
                "rms_normalized_rmse_percent": 1.864572533232999,
                "reference_energy": 4.114831016278615,
                "candidate_energy": 4.126629895949833,
                "relative_energy_error_percent": 0.2867403211587775,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.41729424285586e-05,
                  "p90": 6.159767053759424e-05,
                  "p95": 0.00013108434359310195,
                  "p99": 0.0003578243777155876,
                  "maximum": 0.0007734359242022038
                },
                "worst": {
                  "global_sensor_index": 81,
                  "local_sensor_index": 17,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.0009327318985015154,
                  "candidate": 0.00015929597429931164
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.2136805696862825,
                "cvrmse_percent": 9.090015536326122,
                "rms_normalized_rmse_percent": 2.181806379317168,
                "reference_energy": 5.357422893040322,
                "candidate_energy": 5.34597512128197,
                "relative_energy_error_percent": 0.2136805696862825,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.626745744142681e-06,
                  "p95": 8.266023360192776e-05,
                  "p99": 0.00025000725872814655,
                  "maximum": 0.00046368478797376156
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 60,
                  "rgb_channel": 0,
                  "reference": 0.005802095634862781,
                  "candidate": 0.006265780422836542
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2372421879961589,
                "cvrmse_percent": 20.586026824462035,
                "rms_normalized_rmse_percent": 2.00178332653392,
                "reference_energy": 4.068694648551357,
                "candidate_energy": 4.078347308758463,
                "relative_energy_error_percent": 0.2372421879961589,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4187827673595166e-05,
                  "p90": 6.571176527359057e-05,
                  "p95": 0.00015077658463269472,
                  "p99": 0.00039723911322653294,
                  "maximum": 0.000849864911288023
                },
                "worst": {
                  "global_sensor_index": 104,
                  "local_sensor_index": 16,
                  "sky_patch_index": 108,
                  "rgb_channel": 0,
                  "reference": 7.580500096082687e-05,
                  "candidate": 0.0009256699122488499
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 280.70962498895824,
            "full": 7454.110624967143
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 274.3732500821352,
            "full": 7426.881375024095
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 272.7078750031069,
            "full": 7436.776375048794
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 274.5454580290243,
            "full": 7411.376165924594
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.08261076579091149,
                "cvrmse_percent": 8.303657218831855,
                "rms_normalized_rmse_percent": 1.7955289458563006,
                "reference_energy": 5.723794263879022,
                "candidate_energy": 5.728522734152708,
                "relative_energy_error_percent": 0.08261076579091148,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.810564521700144e-07,
                  "p95": 4.545506089925766e-05,
                  "p99": 0.00018373508937657003,
                  "maximum": 0.0005047516897320747
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 70,
                  "rgb_channel": 0,
                  "reference": 0.008587142452597618,
                  "candidate": 0.009091894142329693
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.14467548597429403,
                "cvrmse_percent": 20.88061116062342,
                "rms_normalized_rmse_percent": 1.9101006667398832,
                "reference_energy": 4.391792699739135,
                "candidate_energy": 4.385438852307804,
                "relative_energy_error_percent": 0.14467548597429403,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1530830306583084e-05,
                  "p90": 4.8762449296191335e-05,
                  "p95": 9.499024599790573e-05,
                  "p99": 0.00030837549129501124,
                  "maximum": 0.0013804510235786438
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.053317805752158165,
                  "candidate": 0.05193735472857952
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1938026988951845,
                "cvrmse_percent": 9.462069680774727,
                "rms_normalized_rmse_percent": 2.04550373616132,
                "reference_energy": 5.720070684733287,
                "candidate_energy": 5.731156336099012,
                "relative_energy_error_percent": 0.19380269889518448,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.094077902052959e-06,
                  "p95": 4.6762870624661446e-05,
                  "p99": 0.00020806735847145365,
                  "maximum": 0.0004542311653494835
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 17,
                  "sky_patch_index": 51,
                  "rgb_channel": 0,
                  "reference": 0.005841836566105485,
                  "candidate": 0.0053876054007560015
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.028505729673624622,
                "cvrmse_percent": 20.352140668725934,
                "rms_normalized_rmse_percent": 1.8627738021684985,
                "reference_energy": 4.398967131027181,
                "candidate_energy": 4.400221088705983,
                "relative_energy_error_percent": 0.028505729673624622,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0963597105728695e-05,
                  "p90": 4.788055957760662e-05,
                  "p95": 9.241560474038124e-05,
                  "p99": 0.0003142569097690305,
                  "maximum": 0.000899825245141983
                },
                "worst": {
                  "global_sensor_index": 51,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0431366041302681,
                  "candidate": 0.04403642937541008
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15549383543774215,
                "cvrmse_percent": 8.941701030648545,
                "rms_normalized_rmse_percent": 2.1817332343392706,
                "reference_energy": 5.34468280257191,
                "candidate_energy": 5.3529934548536104,
                "relative_energy_error_percent": 0.15549383543774215,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.8320698624593206e-06,
                  "p95": 6.812531501054764e-05,
                  "p99": 0.000247173011302948,
                  "maximum": 0.0006624250672757626
                },
                "worst": {
                  "global_sensor_index": 78,
                  "local_sensor_index": 14,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 0.010914145037531853,
                  "candidate": 0.011576570104807615
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.09601138876040749,
                "cvrmse_percent": 19.430287801831078,
                "rms_normalized_rmse_percent": 1.897752343389783,
                "reference_energy": 4.142859479763743,
                "candidate_energy": 4.13888186284283,
                "relative_energy_error_percent": 0.09601138876040749,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.401888130203588e-05,
                  "p90": 5.964959564153105e-05,
                  "p95": 0.00011855538468807936,
                  "p99": 0.0003697667270898819,
                  "maximum": 0.001124560832977295
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0589371994137764,
                  "candidate": 0.0578126385807991
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11394516981251497,
                "cvrmse_percent": 9.47323054934652,
                "rms_normalized_rmse_percent": 2.2751790048696323,
                "reference_energy": 5.365947335158523,
                "candidate_energy": 5.359833097355427,
                "relative_energy_error_percent": 0.11394516981251496,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.740555934607983e-06,
                  "p95": 8.4270432125777e-05,
                  "p99": 0.0002468298189342022,
                  "maximum": 0.0006445029284805059
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 33,
                  "rgb_channel": 0,
                  "reference": 0.006021212553605437,
                  "candidate": 0.005376709625124931
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.11643269590550197,
                "cvrmse_percent": 19.42478125772396,
                "rms_normalized_rmse_percent": 1.888853318509852,
                "reference_energy": 4.07105318906531,
                "candidate_energy": 4.0663131520855345,
                "relative_energy_error_percent": 0.11643269590550197,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3615046555059962e-05,
                  "p90": 5.8718491345644e-05,
                  "p95": 0.00012696650810539722,
                  "p99": 0.00039384025149047375,
                  "maximum": 0.0008682503830641508
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 60,
                  "rgb_channel": 0,
                  "reference": -5.634734407067299e-05,
                  "candidate": 0.0008119030389934778
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 272.29700004681945,
            "full": 7773.122833925299
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 273.5438330564648,
            "full": 7821.455333032645
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 270.4880420351401,
            "full": 7815.188667038456
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 279.99062498565763,
            "full": 7753.294916939922
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05846841517807581,
                "cvrmse_percent": 4.786728721246997,
                "rms_normalized_rmse_percent": 1.0356444188560208,
                "reference_energy": 5.72494906769553,
                "candidate_energy": 5.721601780705896,
                "relative_energy_error_percent": 0.0584684151780758,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.209578037261963e-07,
                  "p95": 2.8885697247460485e-05,
                  "p99": 9.997989982366584e-05,
                  "maximum": 0.00028834654949605465
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 40,
                  "rgb_channel": 0,
                  "reference": 0.005391007522121072,
                  "candidate": 0.005102660972625017
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1042992281131773,
                "cvrmse_percent": 12.212415448568672,
                "rms_normalized_rmse_percent": 1.1169231279015093,
                "reference_energy": 4.3964854210774895,
                "candidate_energy": 4.391899920719197,
                "relative_energy_error_percent": 0.1042992281131773,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.806145731592551e-06,
                  "p90": 3.445402762736194e-05,
                  "p95": 6.105424836277962e-05,
                  "p99": 0.0001756720477715135,
                  "maximum": 0.0007833987474441528
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.040814969688653946,
                  "candidate": 0.04003157094120979
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02911905747397841,
                "cvrmse_percent": 5.642880297111947,
                "rms_normalized_rmse_percent": 1.220907327576235,
                "reference_energy": 5.725878942477344,
                "candidate_energy": 5.724211620497194,
                "relative_energy_error_percent": 0.029119057473978405,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.959550435363781e-07,
                  "p95": 3.418803680688143e-05,
                  "p99": 0.00012742269318550845,
                  "maximum": 0.0002602504100650549
                },
                "worst": {
                  "global_sensor_index": 54,
                  "local_sensor_index": 22,
                  "sky_patch_index": 56,
                  "rgb_channel": 0,
                  "reference": 0.005557536613196135,
                  "candidate": 0.0058177870232611895
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.03655944039184356,
                "cvrmse_percent": 12.857071166689131,
                "rms_normalized_rmse_percent": 1.178088138997557,
                "reference_energy": 4.397419236656113,
                "candidate_energy": 4.399026908520717,
                "relative_energy_error_percent": 0.03655944039184356,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.269720183307072e-06,
                  "p90": 3.5129192838212475e-05,
                  "p95": 6.286869756877422e-05,
                  "p99": 0.0001886081416159871,
                  "maximum": 0.0007823389023542404
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05223981663584709,
                  "candidate": 0.05302215553820133
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03929470544319067,
                "cvrmse_percent": 5.31119178541392,
                "rms_normalized_rmse_percent": 1.29549093091245,
                "reference_energy": 5.357385123379995,
                "candidate_energy": 5.359490292083684,
                "relative_energy_error_percent": 0.03929470544319067,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.165109203313477e-06,
                  "p95": 4.6958914026618004e-05,
                  "p99": 0.00013524480164051056,
                  "maximum": 0.00041898153722286224
                },
                "worst": {
                  "global_sensor_index": 72,
                  "local_sensor_index": 8,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0056485875975340605,
                  "candidate": 0.006067569134756923
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0071135460555672575,
                "cvrmse_percent": 12.343776921531317,
                "rms_normalized_rmse_percent": 1.2019633459652224,
                "reference_energy": 4.128943280350516,
                "candidate_energy": 4.129236994632372,
                "relative_energy_error_percent": 0.007113546055567258,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0107231901201885e-05,
                  "p90": 4.1820508158707526e-05,
                  "p95": 8.398108184337616e-05,
                  "p99": 0.00022732838988304138,
                  "maximum": 0.0005906801670789719
                },
                "worst": {
                  "global_sensor_index": 77,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04593483544886112,
                  "candidate": 0.04534415528178215
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.049888452255563515,
                "cvrmse_percent": 5.612928796875613,
                "rms_normalized_rmse_percent": 1.346991396738271,
                "reference_energy": 5.355844187741397,
                "candidate_energy": 5.353172239970913,
                "relative_energy_error_percent": 0.049888452255563515,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.0112399801728316e-06,
                  "p95": 5.007954314351082e-05,
                  "p99": 0.000140494666993618,
                  "maximum": 0.00037164543755352497
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.005210692994296551,
                  "candidate": 0.005582338431850076
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1551289838823137,
                "cvrmse_percent": 12.663031405059881,
                "rms_normalized_rmse_percent": 1.233289464719929,
                "reference_energy": 4.074692527406356,
                "candidate_energy": 4.08101355652045,
                "relative_energy_error_percent": 0.1551289838823137,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0158920304093044e-05,
                  "p90": 4.3433850805740803e-05,
                  "p95": 8.967751637101173e-05,
                  "p99": 0.00021572550758719444,
                  "maximum": 0.00098380446434021
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.058572376146912575,
                  "candidate": 0.059556180611252785
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 452.41987495683134,
            "full": 13815.52716693841
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 461.0577920684591,
            "full": 13900.14370798599
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 461.6706660017371,
            "full": 13804.814958013594
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 466.687791980803,
            "full": 13763.474624953233
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 5177.2320420714095,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 19934.844124945812,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013835013175000495,
            "cvrmse_percent": 7.800969738846403,
            "rms_normalized_rmse_percent": 1.6874447406768363,
            "reference_energy": 5.720563109998523,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013835013175000495,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3539014613221285,
            "cvrmse_percent": 25.866120972072487,
            "rms_normalized_rmse_percent": 2.3675671960682925,
            "reference_energy": 4.3969049921278724,
            "candidate_energy": 4.381344281107786,
            "relative_energy_error_percent": 0.3539014613221285,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.603411030577263e-05,
              "p90": 9.233023774868343e-05,
              "p95": 0.00012334661732893437,
              "p99": 0.00024923004675656685,
              "maximum": 0.002253308892250061
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03722213953733444,
              "candidate": 0.03496883064508438,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.16162296253350114,
            "cvrmse_percent": 10.859193923091851,
            "rms_normalized_rmse_percent": 2.2871432194688053,
            "reference_energy": 10.117468102126395,
            "candidate_energy": 10.101115950446356,
            "relative_energy_error_percent": 0.16162296253350114,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.564934857218759e-05,
              "p90": 8.8881386545836e-05,
              "p95": 0.00011674914276227355,
              "p99": 0.00022532231650984673,
              "maximum": 0.002253308892250061
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03722213953733444,
              "candidate": 0.03496883064508438,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08641696995553096,
            "cvrmse_percent": 7.714185860707336,
            "rms_normalized_rmse_percent": 1.6690328357848911,
            "reference_energy": 5.717453573463455,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641696995553094,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0112595612929516,
            "cvrmse_percent": 27.279708466513547,
            "rms_normalized_rmse_percent": 2.502941768247938,
            "reference_energy": 4.405814793619232,
            "candidate_energy": 4.361260570265898,
            "relative_energy_error_percent": 1.0112595612929516,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4727230993448757e-05,
              "p90": 8.771892316872254e-05,
              "p95": 0.00012376746599329636,
              "p99": 0.0002534781408030545,
              "maximum": 0.0015589315444231033
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029286270961165428,
              "candidate": 0.027727339416742325,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4889238504342703,
            "cvrmse_percent": 11.544326221981269,
            "rms_normalized_rmse_percent": 2.433739690655419,
            "reference_energy": 10.123268367082687,
            "candidate_energy": 10.073773293592552,
            "relative_energy_error_percent": 0.4889238504342703,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4727230993448757e-05,
              "p90": 8.544232696294785e-05,
              "p95": 0.00011691493273247033,
              "p99": 0.00024238058649643802,
              "maximum": 0.0015589315444231033
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029286270961165428,
              "candidate": 0.027727339416742325,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3821225108837679,
            "cvrmse_percent": 6.386477548129004,
            "rms_normalized_rmse_percent": 1.5580886651593073,
            "reference_energy": 5.366319870222696,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821225108837679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9509498728191083,
            "cvrmse_percent": 28.05566596738011,
            "rms_normalized_rmse_percent": 2.727398544805489,
            "reference_energy": 4.1212080112291005,
            "candidate_energy": 4.0820173888877065,
            "relative_energy_error_percent": 0.9509498728191083,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.9673933113372186e-05,
              "p90": 0.00010055792517960072,
              "p95": 0.0001426523958798498,
              "p99": 0.0002964101731777191,
              "maximum": 0.0021642856299877167
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0584675557911396,
              "candidate": 0.056303270161151886,
              "position": [
                7.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6292106786663662,
            "cvrmse_percent": 12.05318628315781,
            "rms_normalized_rmse_percent": 2.697481163975558,
            "reference_energy": 9.487527881451797,
            "candidate_energy": 9.427831342880253,
            "relative_energy_error_percent": 0.629210678666366,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.931160452135373e-05,
              "p90": 9.868894994724542e-05,
              "p95": 0.0001421961933374405,
              "p99": 0.000258556567132473,
              "maximum": 0.0021642856299877167
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0584675557911396,
              "candidate": 0.056303270161151886,
              "position": [
                7.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22767839501203674,
            "cvrmse_percent": 5.926218592453318,
            "rms_normalized_rmse_percent": 1.4217865864313415,
            "reference_energy": 5.355987454013757,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839501203674,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.41957624742481264,
            "cvrmse_percent": 21.935329000637363,
            "rms_normalized_rmse_percent": 2.1350835675380533,
            "reference_energy": 4.076373789058152,
            "candidate_energy": 4.093477285233291,
            "relative_energy_error_percent": 0.41957624742481264,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.031612141057849e-05,
              "p90": 0.00010688742622733116,
              "p95": 0.00014626250413130037,
              "p99": 0.0002574566751718521,
              "maximum": 0.0013828165829181671
            },
            "worst": {
              "global_sensor_index": 104,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042320191860198975,
              "candidate": 0.04370300844311714,
              "position": [
                8.5,
                -0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.05204497343016834,
            "cvrmse_percent": 9.260248038578377,
            "rms_normalized_rmse_percent": 2.085642027589185,
            "reference_energy": 9.43236124307191,
            "candidate_energy": 9.437270312974704,
            "relative_energy_error_percent": 0.05204497343016835,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.995658724103123e-05,
              "p90": 0.00010591211321298033,
              "p95": 0.00014254114648792893,
              "p99": 0.00024986686185002327,
              "maximum": 0.0013828165829181671
            },
            "worst": {
              "global_sensor_index": 104,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042320191860198975,
              "candidate": 0.04370300844311714,
              "position": [
                8.5,
                -0.5,
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
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013835013175000495,
            "cvrmse_percent": 7.800969738846403,
            "rms_normalized_rmse_percent": 1.6874447406768363,
            "reference_energy": 5.720563109998523,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013835013175000495,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.26990630224516,
            "cvrmse_percent": 497.30018784989625,
            "rms_normalized_rmse_percent": 30.821634000265163,
            "reference_energy": 2.4037672317900443,
            "candidate_energy": 4.381344281107786,
            "relative_energy_error_percent": 82.26990630224518,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.800684112320596e-05,
              "p90": 0.00023158589283411857,
              "p95": 0.00032766303047537804,
              "p99": 0.0005585717024587257,
              "maximum": 0.013192074373364449
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021086866036057472,
              "candidate": 0.03427894040942192,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.3316744333983,
            "cvrmse_percent": 147.1233179455485,
            "rms_normalized_rmse_percent": 30.818657019840632,
            "reference_energy": 8.124330341788568,
            "candidate_energy": 10.101115950446356,
            "relative_energy_error_percent": 24.331674433398288,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.76484995285864e-05,
              "p90": 0.00022969116525928257,
              "p95": 0.00032538868981646374,
              "p99": 0.0005604664491329459,
              "maximum": 0.013192074373364449
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021086866036057472,
              "candidate": 0.03427894040942192,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08641696995553096,
            "cvrmse_percent": 7.714185860707336,
            "rms_normalized_rmse_percent": 1.6690328357848911,
            "reference_energy": 5.717453573463455,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641696995553094,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.00246976062905,
            "cvrmse_percent": 492.4885304997373,
            "rms_normalized_rmse_percent": 30.60126579242368,
            "reference_energy": 2.409503348784991,
            "candidate_energy": 4.361260570265898,
            "relative_energy_error_percent": 81.00246976062907,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.951398321078159e-05,
              "p90": 0.00022033019922673702,
              "p95": 0.0003167262801753168,
              "p99": 0.0005377448920626199,
              "maximum": 0.014290452003479004
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021379977464675903,
              "candidate": 0.03567042946815491,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.95504725778083,
            "cvrmse_percent": 146.00126642762504,
            "rms_normalized_rmse_percent": 30.598512661599063,
            "reference_energy": 8.126956922248446,
            "candidate_energy": 10.073773293592552,
            "relative_energy_error_percent": 23.95504725778083,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.914111584890634e-05,
              "p90": 0.00022356107365339994,
              "p95": 0.0003163699875585735,
              "p99": 0.0005519072066022116,
              "maximum": 0.014290452003479004
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021379977464675903,
              "candidate": 0.03567042946815491,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3821225108837679,
            "cvrmse_percent": 6.386477548129004,
            "rms_normalized_rmse_percent": 1.5580886651593073,
            "reference_energy": 5.366319870222696,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821225108837679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.32204003595513,
            "cvrmse_percent": 494.39418026344595,
            "rms_normalized_rmse_percent": 33.65462336336971,
            "reference_energy": 2.251252736886407,
            "candidate_energy": 4.0820173888877065,
            "relative_energy_error_percent": 81.32204003595513,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.89322828798322e-05,
              "p90": 0.0002824199909809977,
              "p95": 0.0003916560672223568,
              "p99": 0.0006503039039671421,
              "maximum": 0.015097077935934067
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022143863141536713,
              "candidate": 0.03724094107747078,
              "position": [
                7.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.76424655383954,
            "cvrmse_percent": 146.0502857375201,
            "rms_normalized_rmse_percent": 33.64078677889391,
            "reference_energy": 7.6175726071091034,
            "candidate_energy": 9.427831342880253,
            "relative_energy_error_percent": 23.76424655383954,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.794658661921858e-05,
              "p90": 0.00027714998577721417,
              "p95": 0.0003830331716017099,
              "p99": 0.0006124973297119141,
              "maximum": 0.015097077935934067
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022143863141536713,
              "candidate": 0.03724094107747078,
              "position": [
                7.5,
                11.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22767839501203674,
            "cvrmse_percent": 5.926218592453318,
            "rms_normalized_rmse_percent": 1.4217865864313415,
            "reference_energy": 5.355987454013757,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839501203674,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.64853390234323,
            "cvrmse_percent": 553.7159896224115,
            "rms_normalized_rmse_percent": 37.23954072822184,
            "reference_energy": 2.1931473018561443,
            "candidate_energy": 4.093477285233291,
            "relative_energy_error_percent": 86.64853390234323,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.637028087017825e-05,
              "p90": 0.0002886401489377022,
              "p95": 0.0003841065336018801,
              "p99": 0.0006427410989999771,
              "maximum": 0.01571960560977459
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021140264347195625,
              "candidate": 0.036859869956970215,
              "position": [
                6.5,
                -3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 25.011284314890062,
            "cvrmse_percent": 160.81997689508557,
            "rms_normalized_rmse_percent": 37.22945020978276,
            "reference_energy": 7.549134755869901,
            "candidate_energy": 9.437270312974704,
            "relative_energy_error_percent": 25.01128431489006,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.623816307969264e-05,
              "p90": 0.00028525758534669876,
              "p95": 0.00038242246955633163,
              "p99": 0.000615849974565208,
              "maximum": 0.01571960560977459
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021140264347195625,
              "candidate": 0.036859869956970215,
              "position": [
                6.5,
                -3.5,
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
      "bias_percent": -0.04847998926385129,
      "rms_normalized_error_percent": 0.461069057572531,
      "absolute_error": {
        "p95": 0.18124600945496316,
        "p99": 0.29367243080697986,
        "maximum": 0.3111115221418226
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 14.54532350780399,
      "rms_normalized_to_uniform_percent": 0.461069057572531
    },
    "overcast": {
      "bias_percent": -0.02126263467511317,
      "rms_normalized_error_percent": 0.41074526777530757,
      "absolute_error": {
        "p95": 0.1253843784332274,
        "p99": 0.15679654598236084,
        "maximum": 0.2002696990966797
      },
      "worst_index": [
        44
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 10.026911735534668,
      "rms_normalized_to_uniform_percent": 0.3006644362526479
    },
    "horizon": {
      "bias_percent": -3.4975315070897643,
      "rms_normalized_error_percent": 13.933186817993846,
      "absolute_error": {
        "p95": 0.07476184709945041,
        "p99": 0.09969541429137255,
        "maximum": 0.12532982187785208
      },
      "worst_index": [
        91
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.25244264717655246,
      "rms_normalized_to_uniform_percent": 0.1796412349614421
    },
    "north": {
      "bias_percent": -0.2122536332138973,
      "rms_normalized_error_percent": 0.621036442913485,
      "absolute_error": {
        "p95": 0.08962745666503905,
        "p99": 0.15957290649414066,
        "maximum": 0.17714309692382812
      },
      "worst_index": [
        101
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.834320545196533,
      "rms_normalized_to_uniform_percent": 0.21269770927933349
    },
    "east": {
      "bias_percent": 0.0889145072870369,
      "rms_normalized_error_percent": 0.5990980141304347,
      "absolute_error": {
        "p95": 0.0908252477645874,
        "p99": 0.10539766550064088,
        "maximum": 0.10779476165771484
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.7709925174713135,
      "rms_normalized_to_uniform_percent": 0.20246348609929316
    },
    "south": {
      "bias_percent": 0.09801694037969298,
      "rms_normalized_error_percent": 0.7026588249789095,
      "absolute_error": {
        "p95": 0.09766057729721069,
        "p99": 0.15235035181045534,
        "maximum": 0.23070669174194336
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.7374446392059326,
      "rms_normalized_to_uniform_percent": 0.2339978602458889
    },
    "west": {
      "bias_percent": -0.254908396898675,
      "rms_normalized_error_percent": 0.6182454581435083,
      "absolute_error": {
        "p95": 0.09852826595306396,
        "p99": 0.12579107284545898,
        "maximum": 0.1539764404296875
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.6972498893737793,
      "rms_normalized_to_uniform_percent": 0.20665047706818995
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
        "identifier": "courtyard_rooms_west_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.2226799075415607,
          "cvrmse_percent": 4.036950558509584,
          "absolute_error_percentiles_lux": {
            "p50": 6.249153137207031,
            "p90": 48.179129028320325,
            "p95": 70.97198181152342,
            "p99": 133.12012908935552
          },
          "maximum_absolute_error_lux": 415.4716796875,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              6.5,
              0.75
            ],
            "hour_of_year": 2961.5,
            "foton_lux": 6821.40625,
            "radiance_lux": 6405.9345703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7688955479452046,
            "maximum_error_percentage_points": 4.083698630136986,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3419713797042765,
            "maximum_error_percentage_points": 1.4452292885301503,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2872945205479454,
            "maximum_error_percentage_points": 0.9013698630136986,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.28307791095890433,
            "maximum_error_percentage_points": 0.9013698630136986,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.030342465753424724,
            "maximum_error_percentage_points": 0.19493150684931493,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 31.25,
          "radiance_percent": 34.375,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": -0.18389622874746434,
          "cvrmse_percent": 4.14096190838631,
          "absolute_error_percentiles_lux": {
            "p50": 6.583076477050781,
            "p90": 47.29833984375003,
            "p95": 70.31166992187497,
            "p99": 126.1169842529298
          },
          "maximum_absolute_error_lux": 324.8994140625,
          "worst": {
            "sensor_index": 25,
            "position": [
              13.5,
              6.5,
              0.75
            ],
            "hour_of_year": 2248.5,
            "foton_lux": 4653.34716796875,
            "radiance_lux": 4978.24658203125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.8802183219178082,
            "maximum_error_percentage_points": 4.0530136986301315,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4097519717185072,
            "maximum_error_percentage_points": 1.4845498504595227,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.26557363013698637,
            "maximum_error_percentage_points": 1.145753424657535,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2587671232876694,
            "maximum_error_percentage_points": 1.145753424657535,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04315496575342449,
            "maximum_error_percentage_points": 0.22164383561643852,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.75,
          "radiance_percent": 46.875,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.018380919059801413,
          "cvrmse_percent": 2.9938562412455636,
          "absolute_error_percentiles_lux": {
            "p50": 9.059127807617188,
            "p90": 68.4205200195313,
            "p95": 98.56929321289044,
            "p99": 172.62533935546867
          },
          "maximum_absolute_error_lux": 390.93212890625,
          "worst": {
            "sensor_index": 15,
            "position": [
              7.5,
              8.5,
              0.75
            ],
            "hour_of_year": 1358.5,
            "foton_lux": 6637.31201171875,
            "radiance_lux": 7028.244140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.36417808219178066,
            "maximum_error_percentage_points": 1.6212328767123338,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17946599266934862,
            "maximum_error_percentage_points": 0.7787295653612745,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.14716324200913258,
            "maximum_error_percentage_points": 0.6553424657534244,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.17756278538812786,
            "maximum_error_percentage_points": 0.6887671232876755,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.10429223744292275,
            "maximum_error_percentage_points": 0.3605479452054787,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.17202739976776416,
          "cvrmse_percent": 6.984654703824687,
          "absolute_error_percentiles_lux": {
            "p50": 5.616466522216797,
            "p90": 39.5861557006836,
            "p95": 56.480166625976565,
            "p99": 99.05960327148432
          },
          "maximum_absolute_error_lux": 322.906982421875,
          "worst": {
            "sensor_index": 8,
            "position": [
              6.5,
              -0.5,
              0.75
            ],
            "hour_of_year": 4447.5,
            "foton_lux": 1384.291259765625,
            "radiance_lux": 1707.1982421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6500799086757987,
            "maximum_error_percentage_points": 2.736438356164385,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.22827626333480122,
            "maximum_error_percentage_points": 0.5823402786145309,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.16743721461187136,
            "maximum_error_percentage_points": 0.4915068493150656,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16743721461187455,
            "maximum_error_percentage_points": 0.4915068493150727,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 41.666666666666664,
          "radiance_percent": 41.666666666666664,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
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
      "maximum_error_percentage_points": 0.004968161386983638,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004944884417795947,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.0047618792808208354,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004968161386983638,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004841074486293451,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004383561643836131,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0,
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
      "study_preparation_seconds": 0.014875374967232347,
      "weather_seconds": 0.10486870899330825,
      "metric_reduction_seconds": 0.04792404198087752,
      "write_seconds": 0.07132579199969769,
      "total_seconds": 0.2243330420460552,
      "cold_end_to_end_seconds": 0.23920841701328754,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03044245799537748,
      "engine_upload_seconds": 0.0002735,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.029297166620381176,
      "engine_annual_reduction_seconds": 0.0008690833346918225,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.029297166620381176
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.014875374967232347,
      "weather_seconds": 0.11996766598895192,
      "metric_reduction_seconds": 0.013852417003363371,
      "write_seconds": 0.04147929197642952,
      "total_seconds": 0.175893250037916,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.175893250037916,
      "raw_export_seconds": 0.025675583048723638,
      "engine_upload_seconds": 6.0916e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0008845416596159339,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01930937496945262,
      "full": 0.021692666923627257
    }
  },
  "elapsed_seconds": 156.79646808293182,
  "result_class": "passed"
}
```
