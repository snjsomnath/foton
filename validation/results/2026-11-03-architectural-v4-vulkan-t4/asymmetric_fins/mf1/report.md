# Foton report

Status: **passed**

```json
{
  "scene": "asymmetric_fins",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "asymmetric_fins",
    "category": "shading",
    "question": "Do unequal fins produce different east and west sky masks?",
    "interactions": [
      "fins",
      "asymmetric_shading"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 2,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0510a6805d048c7473529755c206b4a2ab87a7b21bc7bce93e3105c5b337c757",
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
      "scene_fingerprint": 12247094324704974908,
      "basis": "Tregenza",
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
      "scene_fingerprint": 12247094324704974908,
      "basis": "Tregenza",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "f804216acbb9232aa7fda96d823b626095bdd036a0e10dce3b34a7ee3a194380",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0005634976550936699,
          "p95": 2.082379069179292e-06,
          "p99": 0.00010405806824564934
        },
        "bias_percent": -0.11363643576137482,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4419839383822288,
        "worst_index": [
          10,
          70,
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
          "maximum": 0.0004999227821826935,
          "p95": 3.804781299550086e-05,
          "p99": 0.00013820035383105278
        },
        "bias_percent": 0.0013431143905797977,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1096397569322334,
        "worst_index": [
          27,
          0,
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
          "maximum": 0.00034437328577041626,
          "p95": 3.3096819970523897e-05,
          "p99": 0.00011184136383235455
        },
        "bias_percent": -0.0240310420568117,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9532605360471063,
        "worst_index": [
          28,
          0,
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006105049978941679,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.515294858720153e-05,
                  "p99": 0.000230276957154274
                },
                "candidate_energy": 4.723735160674551,
                "cvrmse_percent": 13.956124233043074,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1821588435473068,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.715146105058011,
                "relative_energy_error_percent": 0.18215884354730683,
                "rms_normalized_rmse_percent": 2.5320637120022402,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00216708704829216,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.002777592046186328,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011650994420051575,
                  "p50": 0.0,
                  "p90": 2.050593866442796e-05,
                  "p95": 7.811889117874668e-05,
                  "p99": 0.0004032765282317996
                },
                "candidate_energy": 1.7760374446523883,
                "cvrmse_percent": 65.42135228148388,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.36603015876496486,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7825621597558268,
                "relative_energy_error_percent": 0.3660301587649648,
                "rms_normalized_rmse_percent": 3.5767900805678967,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.019980925135314465,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.021146024577319622,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.48087500501424,
            "full": 226.2253339868039
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.67725005745888,
            "full": 226.99520806781948
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.83345794212073,
            "full": 236.84874991886318
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.84066600818187,
            "full": 218.17941695917398
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039036781527101994,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3433818932971906e-05,
                  "p99": 0.00016011809930205345
                },
                "candidate_energy": 4.72095417977107,
                "cvrmse_percent": 9.404000311343829,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02075745055013655,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.721934332955243,
                "relative_energy_error_percent": 0.02075745055013655,
                "rms_normalized_rmse_percent": 1.7085794701358399,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007438195636495948,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.007828563451766968,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006016511470079422,
                  "p50": 1.747763349158049e-06,
                  "p90": 2.842439425876364e-05,
                  "p95": 6.669681060884589e-05,
                  "p99": 0.00024764443514868617
                },
                "candidate_energy": 3.2545291578530566,
                "cvrmse_percent": 22.798139336515415,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06139563501431584,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.256528524219924,
                "relative_energy_error_percent": 0.06139563501431583,
                "rms_normalized_rmse_percent": 1.9478174861286213,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026306435465812683,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.02570478431880474,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.83958299085498,
            "full": 2363.8140000402927
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.95658299326897,
            "full": 2352.5839160429314
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.298415992409,
            "full": 2309.236083063297
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.83229200169444,
            "full": 2325.9897920070216
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004307685885578394,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3304772730625698e-05,
                  "p99": 0.00015845010057091713
                },
                "candidate_energy": 4.7222798981547385,
                "cvrmse_percent": 9.442138256814639,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.023095921159429465,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.721189495950966,
                "relative_energy_error_percent": 0.023095921159429468,
                "rms_normalized_rmse_percent": 1.7160557770136207,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007198445964604616,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.006767677376046777,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007480946369469166,
                  "p50": 1.959277142304927e-06,
                  "p90": 2.70757736871019e-05,
                  "p95": 6.895578117109825e-05,
                  "p99": 0.000258626532740891
                },
                "candidate_energy": 3.260624063328841,
                "cvrmse_percent": 24.67587612309163,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.32482417038545636,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2500670599643406,
                "relative_energy_error_percent": 0.32482417038545636,
                "rms_normalized_rmse_percent": 2.107066915739012,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004475545138120651,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": -0.00030054012313485146,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              }
            },
            "start_sensor_index": 0
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.00120807252824,
            "full": 2481.3885838957503
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.17475002259016,
            "full": 2528.187375050038
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.53508294839412,
            "full": 2477.6635830057785
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.54441709816456,
            "full": 2504.3953330023214
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002261454937979579,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1731402082659768e-05,
                  "p99": 8.115009404718876e-05
                },
                "candidate_energy": 4.71816120247604,
                "cvrmse_percent": 5.027101772154431,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06987379438416474,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.721460265914175,
                "relative_energy_error_percent": 0.06987379438416474,
                "rms_normalized_rmse_percent": 0.9135742384107343,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0023460430093109608,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002119897515513003,
                  "rgb_channel": 0,
                  "sky_patch_index": 20
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006826147437095642,
                  "p50": 1.4649098289964968e-06,
                  "p90": 1.952354796230793e-05,
                  "p95": 3.8655994285363605e-05,
                  "p99": 0.00014339014887809753
                },
                "candidate_energy": 3.2600710455379733,
                "cvrmse_percent": 14.523375228879118,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.29031361033400516,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.250634012577315,
                "relative_energy_error_percent": 0.29031361033400516,
                "rms_normalized_rmse_percent": 1.2412155929828457,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02050356473773718,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.019820949994027615,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.96112496219575,
            "full": 4389.551499974914
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.50254211388528,
            "full": 4475.973125081509
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.84637491870672,
            "full": 4415.218249894679
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.3580829706043,
            "full": 4392.58487499319
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/asymmetric_fins/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 801.8630830338225,
      "invocation_count": 3,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2749.698583036661,
      "invocation_count": 3,
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
      36,
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
        "identifier": "asymmetric_fins_grid",
        "full_identifier": "asymmetric_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06237419080983089,
            "cvrmse_percent": 5.2027968693058355,
            "rms_normalized_rmse_percent": 0.9454672505350414,
            "reference_energy": 4.721375241873375,
            "candidate_energy": 4.7184303222711605,
            "relative_energy_error_percent": 0.062374190809830886,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.7985119484364235e-06,
              "p99": 5.8523379266262054e-05,
              "maximum": 0.0003406982868909836
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.012816520407795906,
              "candidate": 0.012475822120904922,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9346992942977498,
            "cvrmse_percent": 24.116771559806185,
            "rms_normalized_rmse_percent": 2.0614179983412413,
            "reference_energy": 3.2537880249369735,
            "candidate_energy": 3.223374891229943,
            "relative_energy_error_percent": 0.9346992942977498,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.7566032372305926e-06,
              "p90": 3.363040741533041e-05,
              "p95": 5.2481883903965355e-05,
              "p99": 0.00013072974979877472,
              "maximum": 0.001115093007683754
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022836923599243164,
              "candidate": 0.02172183059155941,
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
            "nmbe_percent": -0.418274237068833,
            "cvrmse_percent": 9.68780667359626,
            "rms_normalized_rmse_percent": 2.0296571532080683,
            "reference_energy": 7.975163266810348,
            "candidate_energy": 7.9418052135011035,
            "relative_energy_error_percent": 0.41827423706883293,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.7326300369168166e-06,
              "p90": 3.3425501896999776e-05,
              "p95": 5.096140885143541e-05,
              "p99": 0.00011252262629568577,
              "maximum": 0.001115093007683754
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022836923599243164,
              "candidate": 0.02172183059155941,
              "position": [
                1.5,
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
      36,
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
        "identifier": "asymmetric_fins_grid",
        "full_identifier": "asymmetric_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06237419080983089,
            "cvrmse_percent": 5.2027968693058355,
            "rms_normalized_rmse_percent": 0.9454672505350414,
            "reference_energy": 4.721375241873375,
            "candidate_energy": 4.7184303222711605,
            "relative_energy_error_percent": 0.062374190809830886,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.7985119484364235e-06,
              "p99": 5.8523379266262054e-05,
              "maximum": 0.0003406982868909836
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.012816520407795906,
              "candidate": 0.012475822120904922,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.35692564343374,
            "cvrmse_percent": 436.44560262782625,
            "rms_normalized_rmse_percent": 23.786316539463957,
            "reference_energy": 1.7773652038893886,
            "candidate_energy": 3.223374891229943,
            "relative_energy_error_percent": 81.35692564343374,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.979822446988692e-06,
              "p90": 0.00018922366143669933,
              "p95": 0.00026465149567229664,
              "p99": 0.00048616714775562286,
              "maximum": 0.006543602794408798
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013444807380437851,
              "candidate": 0.01998841017484665,
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
            "nmbe_percent": 22.205299315796363,
            "cvrmse_percent": 119.34126406025185,
            "rms_normalized_rmse_percent": 23.781553656813315,
            "reference_energy": 6.498740445762763,
            "candidate_energy": 7.9418052135011035,
            "relative_energy_error_percent": 22.20529931579636,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.979999968985794e-06,
              "p90": 0.00019080112178926356,
              "p95": 0.0002637068610056303,
              "p99": 0.0004759363364428282,
              "maximum": 0.006543602794408798
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013444807380437851,
              "candidate": 0.01998841017484665,
              "position": [
                5.5,
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
      "bias_percent": 0.06215377849204299,
      "rms_normalized_error_percent": 0.28497382006041905,
      "absolute_error": {
        "p95": 0.08372259479191158,
        "p99": 0.11079005293437608,
        "maximum": 0.11966931570413752
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.637287648473592,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.28497382006041905
    },
    "overcast": {
      "bias_percent": -0.004405654245656198,
      "rms_normalized_error_percent": 0.25067029505712485,
      "absolute_error": {
        "p95": 0.060195207595825195,
        "p99": 0.06743159294128417,
        "maximum": 0.06903076171875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.2853312492370605,
      "reference_fraction_of_uniform": 0.652188777923584,
      "rms_normalized_to_uniform_percent": 0.18080876876090177
    },
    "horizon": {
      "bias_percent": 1.5260743974592659,
      "rms_normalized_error_percent": 2.902993789481261,
      "absolute_error": {
        "p95": 0.06798755039218077,
        "p99": 0.08124548424698878,
        "maximum": 0.08606904422260886
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8267870647991725,
      "reference_fraction_of_uniform": 0.08579043139073718,
      "rms_normalized_to_uniform_percent": 0.16522821831440193
    },
    "north": {
      "bias_percent": 0.44629119220880964,
      "rms_normalized_error_percent": 10.205027026680236,
      "absolute_error": {
        "p95": 0.002520327689126134,
        "p99": 0.003244803845882416,
        "maximum": 0.003259219229221344
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0066757965832948685,
      "reference_fraction_of_uniform": 0.000692704867105931,
      "rms_normalized_to_uniform_percent": 0.0064595871289759195
    },
    "east": {
      "bias_percent": -0.16805926364879273,
      "rms_normalized_error_percent": 0.49529285022477515,
      "absolute_error": {
        "p95": 0.02940306067466736,
        "p99": 0.04122005105018615,
        "maximum": 0.04382145404815674
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.416309118270874,
      "reference_fraction_of_uniform": 0.14696137607097626,
      "rms_normalized_to_uniform_percent": 0.08059307021193922
    },
    "south": {
      "bias_percent": 0.14660278311647332,
      "rms_normalized_error_percent": 0.3408033157883894,
      "absolute_error": {
        "p95": 0.06191051006317139,
        "p99": 0.09803386926650995,
        "maximum": 0.11445021629333496
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.771962642669678,
      "reference_fraction_of_uniform": 0.7026834487915039,
      "rms_normalized_to_uniform_percent": 0.2256227698291152
    },
    "west": {
      "bias_percent": -0.04125618145272077,
      "rms_normalized_error_percent": 0.40699715945904946,
      "absolute_error": {
        "p95": 0.02770073711872101,
        "p99": 0.04011528491973876,
        "maximum": 0.042656898498535156
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.02160906791687,
      "reference_fraction_of_uniform": 0.20976950228214264,
      "rms_normalized_to_uniform_percent": 0.09084944336569016
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
        "identifier": "asymmetric_fins_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0824998310413712,
          "cvrmse_percent": 1.9069747674523183,
          "absolute_error_percentiles_lux": {
            "p50": 2.307525634765625,
            "p90": 21.89122009277344,
            "p95": 32.91683349609373,
            "p99": 63.68238342285132
          },
          "maximum_absolute_error_lux": 407.27734375,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4993.2373046875,
            "radiance_lux": 5400.5146484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3949771689497731,
            "maximum_error_percentage_points": 1.6164383561643838,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17845158414240064,
            "maximum_error_percentage_points": 0.6373476680393111,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1225532724505331,
            "maximum_error_percentage_points": 0.5736986301369846,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1264649923896505,
            "maximum_error_percentage_points": 0.5776712328767246,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.031149162861491348,
            "maximum_error_percentage_points": 0.16041095890410872,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 38.888888888888886,
          "radiance_percent": 41.666666666666664,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004868899828764484,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "asymmetric_fins_grid",
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
      "study_preparation_seconds": 0.3774186739974539,
      "weather_seconds": 0.23477930300214211,
      "metric_reduction_seconds": 0.17351965099805966,
      "write_seconds": 0.027322660000208998,
      "total_seconds": 0.4360266240000783,
      "cold_end_to_end_seconds": 0.8134452979975322,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.014695179997943342,
      "engine_upload_seconds": 0.014668835,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010402226,
      "engine_annual_reduction_seconds": 0.007016675,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010402226
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3774186739974539,
      "weather_seconds": 0.25358566400245763,
      "metric_reduction_seconds": 0.1517310790004558,
      "write_seconds": 0.02141643600043608,
      "total_seconds": 0.4270578870018653,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4270578870018653,
      "raw_export_seconds": 0.008444205999694532,
      "engine_upload_seconds": 0.013547386,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.5e-08,
      "engine_annual_reduction_seconds": 0.006941292,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013864338001440046,
      "full": 0.02125210800295463
    }
  },
  "elapsed_seconds": 2.551195361000282,
  "result_class": "passed"
}
```
