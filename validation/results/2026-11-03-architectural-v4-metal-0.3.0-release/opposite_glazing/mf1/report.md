# Foton report

Status: **passed**

```json
{
  "scene": "opposite_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "opposite_glazing",
    "category": "openings",
    "question": "How does glazing on opposite facades balance daylight?",
    "interactions": [
      "two_aspects",
      "bilateral_lighting"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 2,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 5.999999999999998
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "fad1d2e4c3083bbb293165fcbd04b730d60ed8ac548240b36051cc2bafb72177",
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
      "scene_fingerprint": 6289786852115784515,
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
      "scene_fingerprint": 6289786852115784515,
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
    "model_sha256": "e681fd9367c36c6ee9ccaa90de7f187b6d12beb4e2725d221a5707965aa9b569",
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
          "maximum": 0.000381584744900465,
          "p95": 2.9412796720862382e-05,
          "p99": 0.00015549547970294952
        },
        "bias_percent": -0.03703973564134615,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1109920833059392,
        "worst_index": [
          8,
          63,
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
          "maximum": 0.0005768649280071259,
          "p95": 8.810621220618483e-05,
          "p99": 0.0001966138370335102
        },
        "bias_percent": 0.011548893362253284,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.929819379996391,
        "worst_index": [
          29,
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
          "maximum": 0.0005052946507930756,
          "p95": 6.627198308706284e-05,
          "p99": 0.00014582928270101547
        },
        "bias_percent": 0.04053987479346962,
        "identifier": "opposite_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7191774535940909,
        "worst_index": [
          19,
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007169046439230442,
                  "p50": 0.0,
                  "p90": 5.928543396294117e-05,
                  "p95": 0.00015487631317228034,
                  "p99": 0.0003367047756910324
                },
                "candidate_energy": 12.047904736489954,
                "cvrmse_percent": 9.017204662266447,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06081619903957927,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.040582112107131,
                "relative_energy_error_percent": 0.06081619903957927,
                "rms_normalized_rmse_percent": 2.6112481685124624,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.011793730314821005,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.012510634958744049,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012911614030599594,
                  "p50": 0.0,
                  "p90": 0.0001014983281493187,
                  "p95": 0.00026281559839844674,
                  "p99": 0.0005410308949649334
                },
                "candidate_energy": 3.935692735603965,
                "cvrmse_percent": 45.32506295051463,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4481581352056124,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.9534102653260774,
                "relative_energy_error_percent": 0.4481581352056124,
                "rms_normalized_rmse_percent": 2.9855640195987436,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04355390556156635,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.04226274415850639,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.8967500180006,
            "full": 248.30204097088426
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.21883301995695,
            "full": 227.7286669705063
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.9582499852404,
            "full": 244.24912489484996
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.96141699515283,
            "full": 238.1344580790028
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000501289963722229,
                  "p50": 0.0,
                  "p90": 4.5855529606342316e-05,
                  "p95": 0.00010480656637810155,
                  "p99": 0.00021892657969146967
                },
                "candidate_energy": 12.04236627209923,
                "cvrmse_percent": 5.846057190657195,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.047961978567958474,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.04814480072639,
                "relative_energy_error_percent": 0.047961978567958474,
                "rms_normalized_rmse_percent": 1.692093936988193,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013922784943133593,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.013421494979411364,
                  "rgb_channel": 0,
                  "sky_patch_index": 84
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008123554289340973,
                  "p50": 8.30698809295427e-06,
                  "p90": 7.019063923507929e-05,
                  "p95": 0.0001569586805999278,
                  "p99": 0.0003177525941282511
                },
                "candidate_energy": 7.187902619011481,
                "cvrmse_percent": 15.498880752635927,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2606815894941695,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.169213798527245,
                "relative_energy_error_percent": 0.2606815894941695,
                "rms_normalized_rmse_percent": 1.5065196626657567,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.051626820117235184,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.050814464688301086,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.34287509135902,
            "full": 2275.0394999748096
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.9087500590831,
            "full": 2253.4721670672297
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.98587495554239,
            "full": 2233.5130410501733
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.61858300678432,
            "full": 2304.5614999718964
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005558258853852749,
                  "p50": 0.0,
                  "p90": 4.595553036779165e-05,
                  "p95": 0.0001109706819988787,
                  "p99": 0.00022749463096261024
                },
                "candidate_energy": 12.050948185001403,
                "cvrmse_percent": 6.09741982475314,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1329587136918952,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.034946674709204,
                "relative_energy_error_percent": 0.13295871369189521,
                "rms_normalized_rmse_percent": 1.763915588280965,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007774054072797298,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0072182281874120235,
                  "rgb_channel": 0,
                  "sky_patch_index": 32
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012042000889778137,
                  "p50": 8.072599484876264e-06,
                  "p90": 7.930852007120848e-05,
                  "p95": 0.00016386747156502633,
                  "p99": 0.0003581830533221364
                },
                "candidate_energy": 7.176712698867835,
                "cvrmse_percent": 16.674767953717147,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17730657675352368,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.1894600844306,
                "relative_energy_error_percent": 0.17730657675352368,
                "rms_normalized_rmse_percent": 1.6259965459078483,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05629586987197399,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.05509166978299618,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.19112507998943,
            "full": 2386.117208050564
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.22245796676725,
            "full": 2402.708583045751
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.86758299265057,
            "full": 2434.978250064887
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.81012492999434,
            "full": 2366.491666994989
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
            "identifier": "opposite_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024254200980067253,
                  "p50": 0.0,
                  "p90": 2.3232772946357727e-05,
                  "p95": 5.7222729083150524e-05,
                  "p99": 0.00011622998863458633
                },
                "candidate_energy": 12.038409452208953,
                "cvrmse_percent": 3.121248279977247,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.058947750467436666,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.045510009391819,
                "relative_energy_error_percent": 0.058947750467436666,
                "rms_normalized_rmse_percent": 0.9033018342062897,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0052280614618211985,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.004985519452020526,
                  "rgb_channel": 0,
                  "sky_patch_index": 50
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006318110972642899,
                  "p50": 5.908874300075695e-06,
                  "p90": 4.2190542444586754e-05,
                  "p95": 8.653951808810144e-05,
                  "p99": 0.00019328633788973093
                },
                "candidate_energy": 7.1984532476575005,
                "cvrmse_percent": 9.455202043947745,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18329140569554025,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.185283241001862,
                "relative_energy_error_percent": 0.18329140569554028,
                "rms_normalized_rmse_percent": 0.9210855058699609,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05370364151895046,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.05307183042168617,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.95383299607784,
            "full": 4192.535458016209
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.26312494743615,
            "full": 4231.873500044458
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.9217920852825,
            "full": 4332.919167005457
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.64458403736353,
            "full": 4354.658208088949
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/opposite_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 816.2899171002209,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/opposite_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2601.0972920339555,
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
        "identifier": "opposite_glazing_grid",
        "full_identifier": "opposite_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16298689849533293,
            "cvrmse_percent": 2.3405604716308868,
            "rms_normalized_rmse_percent": 0.6773431818511352,
            "reference_energy": 12.047674440164883,
            "candidate_energy": 12.028038309254043,
            "relative_energy_error_percent": 0.16298689849533296,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.41819429397583e-06,
              "p95": 2.758574119070543e-05,
              "p99": 8.910195901989937e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.2606141831483088,
            "cvrmse_percent": 14.281435943926835,
            "rms_normalized_rmse_percent": 1.3909227534222361,
            "reference_energy": 7.186153539809709,
            "candidate_energy": 7.167425404462151,
            "relative_energy_error_percent": 0.2606141831483088,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4003991964273155e-05,
              "p90": 5.322307697497308e-05,
              "p95": 7.242155261337752e-05,
              "p99": 0.00015371432527899742,
              "maximum": 0.0016517266631126404
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05540909618139267,
              "candidate": 0.05375736951828003,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.19946245905048765,
            "cvrmse_percent": 5.29925580703202,
            "rms_normalized_rmse_percent": 1.3813866517454267,
            "reference_energy": 19.233827979974592,
            "candidate_energy": 19.195463713716194,
            "relative_energy_error_percent": 0.19946245905048768,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3816196769766975e-05,
              "p90": 5.263373168418184e-05,
              "p95": 7.219778635771943e-05,
              "p99": 0.00014669820666313171,
              "maximum": 0.0016517266631126404
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05540909618139267,
              "candidate": 0.05375736951828003,
              "position": [
                3.5,
                3.5,
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
        "identifier": "opposite_glazing_grid",
        "full_identifier": "opposite_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16298689849533293,
            "cvrmse_percent": 2.3405604716308868,
            "rms_normalized_rmse_percent": 0.6773431818511352,
            "reference_energy": 12.047674440164883,
            "candidate_energy": 12.028038309254043,
            "relative_energy_error_percent": 0.16298689849533296,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.41819429397583e-06,
              "p95": 2.758574119070543e-05,
              "p99": 8.910195901989937e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.86263050193503,
            "cvrmse_percent": 436.73466765181604,
            "rms_normalized_rmse_percent": 28.672951669591804,
            "reference_energy": 3.9411204955522123,
            "candidate_energy": 7.167425404462151,
            "relative_energy_error_percent": 81.86263050193503,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.490804404777009e-05,
              "p90": 0.000269028969341889,
              "p95": 0.00033529499778524037,
              "p99": 0.0005781175568699837,
              "maximum": 0.015097560361027718
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026063328608870506,
              "candidate": 0.041160888969898224,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.055725218138708,
            "cvrmse_percent": 107.62819585104849,
            "rms_normalized_rmse_percent": 28.6666414918024,
            "reference_energy": 15.988794935717095,
            "candidate_energy": 19.195463713716194,
            "relative_energy_error_percent": 20.05572521813871,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.467991935707687e-05,
              "p90": 0.00026609000633470714,
              "p95": 0.00033111172961071124,
              "p99": 0.0005636034766212106,
              "maximum": 0.015097560361027718
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026063328608870506,
              "candidate": 0.041160888969898224,
              "position": [
                5.5,
                4.5,
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
      "bias_percent": 0.023311587703939703,
      "rms_normalized_error_percent": 0.19125188733258944,
      "absolute_error": {
        "p95": 0.1275661534420145,
        "p99": 0.1487376819395161,
        "maximum": 0.14892985494824984
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.74581446106938,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19125188733258944
    },
    "overcast": {
      "bias_percent": 0.015727574368888598,
      "rms_normalized_error_percent": 0.1740680716005527,
      "absolute_error": {
        "p95": 0.074737548828125,
        "p99": 0.10089449882507322,
        "maximum": 0.10718536376953125
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.160956382751465,
      "reference_fraction_of_uniform": 0.6384685635566711,
      "rms_normalized_to_uniform_percent": 0.11995762619383443
    },
    "horizon": {
      "bias_percent": -0.10045135073361469,
      "rms_normalized_error_percent": 1.383461972028588,
      "absolute_error": {
        "p95": 0.07691484265733106,
        "p99": 0.08734796986071174,
        "maximum": 0.08951583094927784
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5207610484007983,
      "reference_fraction_of_uniform": 0.10615601551732487,
      "rms_normalized_to_uniform_percent": 0.11164219004881203
    },
    "north": {
      "bias_percent": 0.06592141870357121,
      "rms_normalized_error_percent": 0.24980331795087624,
      "absolute_error": {
        "p95": 0.0696256160736084,
        "p99": 0.07040330171585082,
        "maximum": 0.07057595252990723
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.263083457946777,
      "reference_fraction_of_uniform": 0.3479806184768677,
      "rms_normalized_to_uniform_percent": 0.1080398104095312
    },
    "east": {
      "bias_percent": 0.12772220597586117,
      "rms_normalized_error_percent": 0.3309830674607133,
      "absolute_error": {
        "p95": 0.0490032434463501,
        "p99": 0.05074433088302612,
        "maximum": 0.050942182540893555
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.817408561706543,
      "reference_fraction_of_uniform": 0.20287400484085083,
      "rms_normalized_to_uniform_percent": 0.07046687715628701
    },
    "south": {
      "bias_percent": -0.04675791014464209,
      "rms_normalized_error_percent": 0.24120700161987108,
      "absolute_error": {
        "p95": 0.06385242938995361,
        "p99": 0.09788805246353142,
        "maximum": 0.11468958854675293
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.171854972839355,
      "reference_fraction_of_uniform": 0.3441387414932251,
      "rms_normalized_to_uniform_percent": 0.10339667223347598
    },
    "west": {
      "bias_percent": 0.05146058073762353,
      "rms_normalized_error_percent": 0.2854387187439366,
      "absolute_error": {
        "p95": 0.0358770415186882,
        "p99": 0.05665123611688612,
        "maximum": 0.060715675354003906
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.589277744293213,
      "reference_fraction_of_uniform": 0.19326679408550262,
      "rms_normalized_to_uniform_percent": 0.05802214973682262
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
        "identifier": "opposite_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.06794351712660665,
          "cvrmse_percent": 1.3133450947785654,
          "absolute_error_percentiles_lux": {
            "p50": 3.46112060546875,
            "p90": 23.961114501953134,
            "p95": 35.669860839843736,
            "p99": 66.16936523437474
          },
          "maximum_absolute_error_lux": 386.7822265625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5311.3095703125,
            "radiance_lux": 5698.091796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.13566210045662133,
            "maximum_error_percentage_points": 0.7913698630136992,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04901844836626444,
            "maximum_error_percentage_points": 0.27246496206014115,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.02907914764079135,
            "maximum_error_percentage_points": 0.10931506849315298,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.04942161339421642,
            "maximum_error_percentage_points": 0.11246575342465803,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.035589802130897935,
            "maximum_error_percentage_points": 0.11301369863013733,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 97.22222222222223,
          "radiance_percent": 97.22222222222223,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.00486167594176834,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "opposite_glazing_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "opposite_glazing_grid",
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
      "study_preparation_seconds": 0.006213583052158356,
      "weather_seconds": 0.09073445806279778,
      "metric_reduction_seconds": 0.038491041981615126,
      "write_seconds": 0.04337133304215968,
      "total_seconds": 0.17276500002481043,
      "cold_end_to_end_seconds": 0.1789785830769688,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.017330833012238145,
      "engine_upload_seconds": 0.000284834,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01945479155983776,
      "engine_annual_reduction_seconds": 0.00037504162173718214,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01945479155983776
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006213583052158356,
      "weather_seconds": 0.08974516694433987,
      "metric_reduction_seconds": 0.012411458999849856,
      "write_seconds": 0.040478625101968646,
      "total_seconds": 0.14278354193083942,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14278354193083942,
      "raw_export_seconds": 0.012996500008739531,
      "engine_upload_seconds": 5.1083e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00038649991620332,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014282541000284255,
      "full": 0.024093707907013595
    }
  },
  "elapsed_seconds": 0.6841243749950081,
  "result_class": "passed"
}
```
