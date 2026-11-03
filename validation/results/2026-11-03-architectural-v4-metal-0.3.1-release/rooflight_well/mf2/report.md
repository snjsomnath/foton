# Foton report

Status: **passed**

```json
{
  "scene": "rooflight_well",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "rooflight_well",
    "category": "shading",
    "question": "How does a one-metre-deep opaque shaft below a rooflight restrict the sky?",
    "interactions": [
      "roof_glazing",
      "interior_shades",
      "lightwell"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 4,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.0
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "09d65417df40b64bd7c8e9bae8f031832139b0883761f81f92d6890c050ce1b2",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 12728338384374136256,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 12728338384374136256,
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
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "a3f21afd5501559cae7ea2f8f1ef32a6d4cec9ddc8cf3109d00ddbfcdd0b3097",
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
          "maximum": 0.0002751448191702366,
          "p95": 0.0,
          "p99": 4.4640153646469116e-05
        },
        "bias_percent": -0.045677425133728494,
        "identifier": "rooflight_well_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3803726726499452,
        "worst_index": [
          14,
          561,
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
          "maximum": 0.0003224094398319721,
          "p95": 1.6023404896259308e-05,
          "p99": 8.773361332714558e-05
        },
        "bias_percent": -0.061469266918299244,
        "identifier": "rooflight_well_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.0890147011926197,
        "worst_index": [
          20,
          559,
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
          "maximum": 0.00026617804542183876,
          "p95": 1.3391701941145584e-05,
          "p99": 7.036438910290599e-05
        },
        "bias_percent": 0.04458102451184824,
        "identifier": "rooflight_well_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6746192287036892,
        "worst_index": [
          21,
          554,
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
            "identifier": "rooflight_well_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008499082177877426,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0002752869622781873
                },
                "candidate_energy": 8.704472075514786,
                "cvrmse_percent": 35.10996000586441,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.039131208879833984,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.707879574059916,
                "relative_energy_error_percent": 0.039131208879833984,
                "rms_normalized_rmse_percent": 6.2312712570525175,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007550251204520464,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.006700342986732721,
                  "rgb_channel": 0,
                  "sky_patch_index": 553
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012298249639570713,
                  "p50": 1.7726142687024549e-06,
                  "p90": 1.028109031722125e-05,
                  "p95": 2.008436968026217e-05,
                  "p99": 0.00033820420503616333
                },
                "candidate_energy": 0.5080482228559937,
                "cvrmse_percent": 760.4479486519713,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4230816235681391,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5059078198380647,
                "relative_energy_error_percent": 0.4230816235681391,
                "rms_normalized_rmse_percent": 7.819071772642425,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00045388774015009403,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0007759372238069773,
                  "rgb_channel": 0,
                  "sky_patch_index": 553
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.07833291217685,
            "full": 251.2329580495134
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.86145903170109,
            "full": 254.08316706307232
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.8934588925913,
            "full": 245.59437506832182
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.19945806544274,
            "full": 258.94904194865376
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
            "identifier": "rooflight_well_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003966322401538491,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.000130921951495111
                },
                "candidate_energy": 8.70419107889029,
                "cvrmse_percent": 16.82390166190699,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08645730320358296,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.696672170663078,
                "relative_energy_error_percent": 0.08645730320358294,
                "rms_normalized_rmse_percent": 2.983637289209602,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0038738263538107276,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.004270458593964577,
                  "rgb_channel": 0,
                  "sky_patch_index": 430
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005442679394036531,
                  "p50": 2.648046347530908e-06,
                  "p90": 1.431669898011026e-05,
                  "p95": 2.3047263312037103e-05,
                  "p99": 0.00018103444017469883
                },
                "candidate_energy": 1.6729989616316203,
                "cvrmse_percent": 123.38060524806913,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.01510580880277121,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6727462797768418,
                "relative_energy_error_percent": 0.015105808802771209,
                "rms_normalized_rmse_percent": 4.141052721617002,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00034136418253183365,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0002029037568718195,
                  "rgb_channel": 0,
                  "sky_patch_index": 562
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.7107500480488,
            "full": 2360.872165998444
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.66354200523347,
            "full": 2365.212957956828
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.42358395457268,
            "full": 2378.274583024904
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.87891603354365,
            "full": 2369.833374978043
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
            "identifier": "rooflight_well_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032367510721087456,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013521546497941017
                },
                "candidate_energy": 8.708925411299788,
                "cvrmse_percent": 16.264515624542206,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07309040853948648,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.702564671228174,
                "relative_energy_error_percent": 0.07309040853948648,
                "rms_normalized_rmse_percent": 2.8846925543228523,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005430974997580051,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.005754650104790926,
                  "rgb_channel": 0,
                  "sky_patch_index": 516
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004757570568472147,
                  "p50": 2.663987061168882e-06,
                  "p90": 1.4448825459112432e-05,
                  "p95": 2.291162127221469e-05,
                  "p99": 0.00018248509149998426
                },
                "candidate_energy": 1.6620799272300886,
                "cvrmse_percent": 121.88808229369333,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10806630733172062,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6602857177637453,
                "relative_energy_error_percent": 0.10806630733172064,
                "rms_normalized_rmse_percent": 4.064145367886141,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002616883721202612,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": -0.0002140686847269535,
                  "rgb_channel": 0,
                  "sky_patch_index": 516
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.55495908483863,
            "full": 2458.2253330154344
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.68008294515312,
            "full": 2511.955374968238
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.61870802007616,
            "full": 2553.7931660655886
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.62145797815174,
            "full": 2527.600208995864
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
            "identifier": "rooflight_well_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022263056598603725,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.977259181439877e-05
                },
                "candidate_energy": 8.7050830289636,
                "cvrmse_percent": 9.068141967202495,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04204992661219966,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.701424086521001,
                "relative_energy_error_percent": 0.04204992661219965,
                "rms_normalized_rmse_percent": 1.609225761854506,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0072505229618400335,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.007027892395853996,
                  "rgb_channel": 0,
                  "sky_patch_index": 561
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003427555784583092,
                  "p50": 1.8788932720781304e-06,
                  "p90": 1.0122744424734269e-05,
                  "p95": 1.5552226614090614e-05,
                  "p99": 9.813570068217814e-05
                },
                "candidate_energy": 1.6682293612778771,
                "cvrmse_percent": 69.07270135059815,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.007989147187364968,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6683626492255428,
                "relative_energy_error_percent": 0.007989147187364968,
                "rms_normalized_rmse_percent": 2.3140216086562853,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00012494996190071106,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.00021780561655759811,
                  "rgb_channel": 0,
                  "sky_patch_index": 561
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.40974996425211,
            "full": 4327.054791036062
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.04554202128202,
            "full": 4324.176624999382
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.05566705856472,
            "full": 4344.939291011542
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.15191706549376,
            "full": 4341.472666012123
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/rooflight_well/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2567.3639579908922,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflight_well/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10551.59454094246,
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
        "identifier": "rooflight_well_grid",
        "full_identifier": "rooflight_well_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.045097302347393786,
            "cvrmse_percent": 4.43844603288067,
            "rms_normalized_rmse_percent": 0.7877185382426393,
            "reference_energy": 8.699198014817966,
            "candidate_energy": 8.703121118448507,
            "relative_energy_error_percent": 0.045097302347393786,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.832937752828002e-05,
              "maximum": 0.00013783667236566544
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.0055317687802016735,
              "candidate": 0.005669605452567339,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4077483949230181,
            "cvrmse_percent": 36.126615936371394,
            "rms_normalized_rmse_percent": 1.2131556828129502,
            "reference_energy": 1.6723515427596993,
            "candidate_energy": 1.6655325561866263,
            "relative_energy_error_percent": 0.4077483949230181,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3029674025565328e-06,
              "p90": 1.0944400310108913e-05,
              "p95": 1.606349178473465e-05,
              "p99": 4.4673215597867966e-05,
              "maximum": 0.00016019307076931
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 564,
              "rgb_channel": 0,
              "reference": 0.0002372032031416893,
              "candidate": 7.70101323723793e-05,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.027921410647999825,
            "cvrmse_percent": 5.633460667646609,
            "rms_normalized_rmse_percent": 1.1732230665117642,
            "reference_energy": 10.371549557577666,
            "candidate_energy": 10.368653674635134,
            "relative_energy_error_percent": 0.02792141064799982,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.3026236135592626e-06,
              "p90": 1.085190342564602e-05,
              "p95": 1.5798374079167843e-05,
              "p99": 4.213117063045502e-05,
              "maximum": 0.00016666436567902565
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.005589071195572615,
              "candidate": 0.00575573556125164,
              "position": [
                2.5,
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
        "identifier": "rooflight_well_grid",
        "full_identifier": "rooflight_well_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.045097302347393786,
            "cvrmse_percent": 4.43844603288067,
            "rms_normalized_rmse_percent": 0.7877185382426393,
            "reference_energy": 8.699198014817966,
            "candidate_energy": 8.703121118448507,
            "relative_energy_error_percent": 0.045097302347393786,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.832937752828002e-05,
              "maximum": 0.00013783667236566544
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.0055317687802016735,
              "candidate": 0.005669605452567339,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 224.0614242634084,
            "cvrmse_percent": 443.4769202897698,
            "rms_normalized_rmse_percent": 4.63291474888492,
            "reference_energy": 0.5139558217928535,
            "candidate_energy": 1.6655325561866263,
            "relative_energy_error_percent": 224.0614242634084,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.345673904841533e-06,
              "p90": 5.918233582633549e-05,
              "p95": 7.817168989276979e-05,
              "p99": 0.00013159308582544327,
              "maximum": 0.00046697864308953285
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": -0.00037180865183472633,
              "candidate": 9.516999125480652e-05,
              "position": [
                1.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 12.541848953315421,
            "cvrmse_percent": 24.671926147721226,
            "rms_normalized_rmse_percent": 4.6202861655634395,
            "reference_energy": 9.21315383661082,
            "candidate_energy": 10.368653674635134,
            "relative_energy_error_percent": 12.541848953315421,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.337881922670931e-06,
              "p90": 5.893400011700587e-05,
              "p95": 7.75500011513941e-05,
              "p99": 0.00012901285663247108,
              "maximum": 0.0005165650509297848
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": 0.0028355559334158897,
              "candidate": 0.0033521209843456745,
              "position": [
                1.5,
                3.5,
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
      "bias_percent": -0.027786582440549972,
      "rms_normalized_error_percent": 0.08103947131955472,
      "absolute_error": {
        "p95": 0.04576779969870759,
        "p99": 0.05372426010713318,
        "maximum": 0.053817561264366987
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.18986006293712,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.08103947131955472
    },
    "overcast": {
      "bias_percent": -0.043996942489392954,
      "rms_normalized_error_percent": 0.0795569427587733,
      "absolute_error": {
        "p95": 0.04006516933441162,
        "p99": 0.0476724863052368,
        "maximum": 0.050922393798828125
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.072391510009766,
      "reference_fraction_of_uniform": 0.8768187761306763,
      "rms_normalized_to_uniform_percent": 0.07250664674570124
    },
    "horizon": {
      "bias_percent": -1.2166100507123063,
      "rms_normalized_error_percent": 8.507557617035246,
      "absolute_error": {
        "p95": 0.002731208336833693,
        "p99": 0.0033994439002048094,
        "maximum": 0.003602511276141085
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.013117196318058043,
      "reference_fraction_of_uniform": 0.000763077550953419,
      "rms_normalized_to_uniform_percent": 0.005570967279651008
    },
    "north": {
      "bias_percent": 0.014738507481996075,
      "rms_normalized_error_percent": 0.1400902620555417,
      "absolute_error": {
        "p95": 0.01153707504272461,
        "p99": 0.014663237333297727,
        "maximum": 0.015362143516540527
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8131625652313232,
      "reference_fraction_of_uniform": 0.1636524498462677,
      "rms_normalized_to_uniform_percent": 0.026065388001450987
    },
    "east": {
      "bias_percent": -0.0171877429712967,
      "rms_normalized_error_percent": 0.1637722125867116,
      "absolute_error": {
        "p95": 0.017088890075683594,
        "p99": 0.020971184968948363,
        "maximum": 0.021667838096618652
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8655343055725098,
      "reference_fraction_of_uniform": 0.1666991114616394,
      "rms_normalized_to_uniform_percent": 0.03114862007811129
    },
    "south": {
      "bias_percent": -0.0016765355901281046,
      "rms_normalized_error_percent": 0.16952087777547292,
      "absolute_error": {
        "p95": 0.01585325598716736,
        "p99": 0.018348550796508784,
        "maximum": 0.01947307586669922
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8267014026641846,
      "reference_fraction_of_uniform": 0.16444005072116852,
      "rms_normalized_to_uniform_percent": 0.03172568930255611
    },
    "west": {
      "bias_percent": 0.0501953788044487,
      "rms_normalized_error_percent": 0.15122284618278092,
      "absolute_error": {
        "p95": 0.011269047856330872,
        "p99": 0.020102751255035384,
        "maximum": 0.024087905883789062
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.85558819770813,
      "reference_fraction_of_uniform": 0.1661205142736435,
      "rms_normalized_to_uniform_percent": 0.02863668732069834
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
        "identifier": "rooflight_well_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.00805647303908317,
          "cvrmse_percent": 2.594698436603627,
          "absolute_error_percentiles_lux": {
            "p50": 1.11639404296875,
            "p90": 15.877359008789064,
            "p95": 25.785519409179674,
            "p99": 65.07652221679683
          },
          "maximum_absolute_error_lux": 403.134765625,
          "worst": {
            "sensor_index": 25,
            "position": [
              4.5,
              4.5,
              0.75
            ],
            "hour_of_year": 4453.5,
            "foton_lux": 14210.318359375,
            "radiance_lux": 13807.18359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.27303272450532734,
            "maximum_error_percentage_points": 1.3653424657534252,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11257226318891206,
            "maximum_error_percentage_points": 0.4427390915128697,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.176978691019787,
            "maximum_error_percentage_points": 1.0361643835616405,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.18871385083713832,
            "maximum_error_percentage_points": 1.0361643835616405,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02119101978691023,
            "maximum_error_percentage_points": 0.13808219178082304,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 36.111111111111114,
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
            "identifier": "rooflight_well_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "rooflight_well_grid",
            "maximum_error_percentage_points": 0.004286172945199951,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "rooflight_well_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "rooflight_well_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "rooflight_well_grid",
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
      "study_preparation_seconds": 0.008818667032755911,
      "weather_seconds": 0.1337195000378415,
      "metric_reduction_seconds": 0.13639616698492318,
      "write_seconds": 0.10837162495590746,
      "total_seconds": 0.3786923330044374,
      "cold_end_to_end_seconds": 0.3875110000371933,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.028577374992892146,
      "engine_upload_seconds": 0.00093275,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.06966591661330312,
      "engine_annual_reduction_seconds": 0.0016333333915099502,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.06966591661330312
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008818667032755911,
      "weather_seconds": 0.1158347079763189,
      "metric_reduction_seconds": 0.05290120805148035,
      "write_seconds": 0.129637666977942,
      "total_seconds": 0.2985885420348495,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2985885420348495,
      "raw_export_seconds": 0.02415537496563047,
      "engine_upload_seconds": 9.6125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0016204999992623925,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012109249946661294,
      "full": 0.07855258404742926
    }
  },
  "elapsed_seconds": 1.8065753328846768,
  "result_class": "passed"
}
```
