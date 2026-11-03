# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_circle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_circle",
    "category": "form",
    "question": "How does a circle opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "circle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.44
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "dca026f8505eeeb4cbf2fe2651043458124527213a7feba10ded39869ad033b5",
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
      "scene_fingerprint": 13085702229645769746,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 13085702229645769746,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "751adb8163a7ab389189b98273868852e7ba164f6ca91d082902a610f5c58977",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0005502613494172692,
          "p95": 0.0,
          "p99": 3.292235342087402e-05
        },
        "bias_percent": 0.33646983330868746,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.53516788898557,
        "worst_index": [
          37,
          99,
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
          "maximum": 0.00028902478516101837,
          "p95": 9.668423444963992e-06,
          "p99": 6.278452929109468e-05
        },
        "bias_percent": 0.08606759985183797,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.088335777770357,
        "worst_index": [
          25,
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
          "maximum": 0.0002693347632884979,
          "p95": 8.886931027518585e-06,
          "p99": 5.217075027758299e-05
        },
        "bias_percent": -0.014370061722267671,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9165690775500066,
        "worst_index": [
          26,
          12,
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008484201971441507,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018541161669418526
                },
                "candidate_energy": 2.37211510243651,
                "cvrmse_percent": 38.72611899556275,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.2607482365219749,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3659459401205822,
                "relative_energy_error_percent": 0.26074823652197493,
                "rms_normalized_rmse_percent": 3.816250927008884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001977762905880809,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0028261831030249596,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00089637516066432,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1130109669466037e-05,
                  "p99": 0.00023527653560450034
                },
                "candidate_energy": 0.565242572487449,
                "cvrmse_percent": 207.69937046571346,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.9400668725118841,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5706066566388586,
                "relative_energy_error_percent": 0.9400668725118841,
                "rms_normalized_rmse_percent": 4.447556723494521,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006884853355586529,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": -0.00020788982510566711,
                  "rgb_channel": 0,
                  "sky_patch_index": 133
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.95316698309034,
            "full": 300.3989999415353
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.23612501192838,
            "full": 297.51179192680866
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.40649999957532,
            "full": 310.89733401313424
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.1259579854086,
            "full": 301.7775419866666
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003194189630448818,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.712502567097619e-05
                },
                "candidate_energy": 2.372288336053316,
                "cvrmse_percent": 14.049124913548084,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1102295617714396,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3696762523049983,
                "relative_energy_error_percent": 0.1102295617714396,
                "rms_normalized_rmse_percent": 1.3867500720832637,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016728700138628483,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.00199228897690773,
                  "rgb_channel": 0,
                  "sky_patch_index": 12
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005401112139225006,
                  "p50": 0.0,
                  "p90": 5.502829310444213e-06,
                  "p95": 1.3863347703590989e-05,
                  "p99": 0.000107376509113239
                },
                "candidate_energy": 1.0916129454218755,
                "cvrmse_percent": 54.63154679112512,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.40497335459886796,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.096051662608076,
                "relative_energy_error_percent": 0.4049733545988679,
                "rms_normalized_rmse_percent": 2.0276716595573037,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024283744394779205,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.024823855608701706,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.26424992177635,
            "full": 3830.2894169464707
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 171.9316670205444,
            "full": 3747.694249963388
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.68124992772937,
            "full": 3683.784708031453
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.75295898132026,
            "full": 3782.2348750196397
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00035735382698476315,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.148049189709417e-05
                },
                "candidate_energy": 2.368125481872994,
                "cvrmse_percent": 16.166135108696697,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.19316458688265978,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.372708714859982,
                "relative_energy_error_percent": 0.19316458688265978,
                "rms_normalized_rmse_percent": 1.5961970878881884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005462631117552519,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.005819984944537282,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005197781138122082,
                  "p50": 0.0,
                  "p90": 5.63060530112125e-06,
                  "p95": 1.421194065187592e-05,
                  "p99": 0.00012705462286248916
                },
                "candidate_energy": 1.0972347054919673,
                "cvrmse_percent": 58.35017715466188,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.026401144719245935,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0975244645141728,
                "relative_energy_error_percent": 0.02640114471924593,
                "rms_normalized_rmse_percent": 2.1641066691987314,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00021439348347485065,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0007341715972870588,
                  "rgb_channel": 0,
                  "sky_patch_index": 42
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.27287506405264,
            "full": 4112.197958049364
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.96504194382578,
            "full": 4187.88266601041
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.91970795486122,
            "full": 4005.9792910469696
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 176.3185829622671,
            "full": 4015.2771660359576
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00017444067634642124,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6941628097556547e-05
                },
                "candidate_energy": 2.3698428455663816,
                "cvrmse_percent": 9.52694162962847,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.08315374824610025,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3718150987224362,
                "relative_energy_error_percent": 0.08315374824610024,
                "rms_normalized_rmse_percent": 0.940798961374914,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006020421627908945,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.005845980951562524,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003104209899902344,
                  "p50": 7.105427357601002e-15,
                  "p90": 3.854035185213434e-06,
                  "p95": 9.788645002117846e-06,
                  "p99": 6.859414628707264e-05
                },
                "candidate_energy": 1.099404074243452,
                "cvrmse_percent": 32.498545239409985,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5367354888715441,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0935346855032364,
                "relative_energy_error_percent": 0.536735488871544,
                "rms_normalized_rmse_percent": 1.203614235281146,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02107782568782568,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.020767404697835445,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.77799998689443,
            "full": 7177.272750064731
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 247.25966702681035,
            "full": 7214.312499971129
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 260.2510409196839,
            "full": 7231.917583965696
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.63099998421967,
            "full": 7119.671417050995
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_t_circle/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1855.0670420518145,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6431.066417018883,
      "invocation_count": 4,
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
      54,
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
        "identifier": "plan_t_circle_grid",
        "full_identifier": "plan_t_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06300992249201073,
            "cvrmse_percent": 8.084346418173368,
            "rms_normalized_rmse_percent": 0.7984285431221384,
            "reference_energy": 2.3723644207275356,
            "candidate_energy": 2.370869595744807,
            "relative_energy_error_percent": 0.06300992249201075,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.927262521348927e-05,
              "maximum": 0.00030892249196767807
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.011060246266424656,
              "candidate": 0.011369168758392334,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1994942413551304,
            "cvrmse_percent": 52.83078802917825,
            "rms_normalized_rmse_percent": 1.9577972491903683,
            "reference_energy": 1.0949339349841374,
            "candidate_energy": 1.0818002654873595,
            "relative_energy_error_percent": 1.1994942413551304,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 9.672014130046591e-06,
              "p95": 2.0779756596311927e-05,
              "p99": 7.115961052477557e-05,
              "maximum": 0.0011265557259321213
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02451176568865776,
              "candidate": 0.02338520996272564,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4218989247178233,
            "cvrmse_percent": 16.529264780717,
            "rms_normalized_rmse_percent": 1.939712924665355,
            "reference_energy": 3.467298355711673,
            "candidate_energy": 3.4526698612321667,
            "relative_energy_error_percent": 0.42189892471782325,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 9.74110298557207e-06,
              "p95": 2.111322828568518e-05,
              "p99": 6.659714104898782e-05,
              "maximum": 0.0011265557259321213
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02451176568865776,
              "candidate": 0.02338520996272564,
              "position": [
                5.5,
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
      54,
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
        "identifier": "plan_t_circle_grid",
        "full_identifier": "plan_t_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06300992249201073,
            "cvrmse_percent": 8.084346418173368,
            "rms_normalized_rmse_percent": 0.7984285431221384,
            "reference_energy": 2.3723644207275356,
            "candidate_energy": 2.370869595744807,
            "relative_energy_error_percent": 0.06300992249201075,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.927262521348927e-05,
              "maximum": 0.00030892249196767807
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.011060246266424656,
              "candidate": 0.011369168758392334,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 91.6078739002684,
            "cvrmse_percent": 897.9479231595299,
            "rms_normalized_rmse_percent": 19.0419837559536,
            "reference_energy": 0.5645907151239697,
            "candidate_energy": 1.0818002654873595,
            "relative_energy_error_percent": 91.6078739002684,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.3346485906804446e-05,
              "p95": 9.554286225466058e-05,
              "p99": 0.0002504156855866398,
              "maximum": 0.006816212087869644
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013832267373800278,
              "candidate": 0.020648479461669922,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.559503006542908,
            "cvrmse_percent": 172.57861375747098,
            "rms_normalized_rmse_percent": 19.037573666061814,
            "reference_energy": 2.9369551358515054,
            "candidate_energy": 3.4526698612321667,
            "relative_energy_error_percent": 17.559503006542904,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.3346485906804446e-05,
              "p95": 9.464496542932466e-05,
              "p99": 0.00023945686298248265,
              "maximum": 0.006816212087869644
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013832267373800278,
              "candidate": 0.020648479461669922,
              "position": [
                6.5,
                0.5,
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
      "bias_percent": 0.12754084634980395,
      "rms_normalized_error_percent": 0.25886061532046484,
      "absolute_error": {
        "p95": 0.06749483469474556,
        "p99": 0.08729295609937696,
        "maximum": 0.10466736513992814
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0175917647855566,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.25886061532046484
    },
    "overcast": {
      "bias_percent": 0.08708932296664579,
      "rms_normalized_error_percent": 0.20774174041250543,
      "absolute_error": {
        "p95": 0.036185669898986784,
        "p99": 0.05225730240344999,
        "maximum": 0.06381988525390625
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.031444787979126,
      "reference_fraction_of_uniform": 0.6732006669044495,
      "rms_normalized_to_uniform_percent": 0.15192611113179535
    },
    "horizon": {
      "bias_percent": 0.5812801564020943,
      "rms_normalized_error_percent": 2.251568684995521,
      "absolute_error": {
        "p95": 0.01779544263784307,
        "p99": 0.01998100051379268,
        "maximum": 0.020177987410418347
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2432427207783949,
      "reference_fraction_of_uniform": 0.08060822660539067,
      "rms_normalized_to_uniform_percent": 0.09026343907250892
    },
    "north": {
      "bias_percent": -99.99999999999999,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 4.879294938291395e-05,
        "p99": 0.00014060094668820954,
        "maximum": 0.00019202896510250866
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.0181563993683085e-05,
      "reference_fraction_of_uniform": 3.3740693652362097e-06,
      "rms_normalized_to_uniform_percent": 0.0003305857447641371
    },
    "east": {
      "bias_percent": 0.14896879327317342,
      "rms_normalized_error_percent": 0.23322058390826556,
      "absolute_error": {
        "p95": 0.01109645590186115,
        "p99": 0.020485348701477044,
        "maximum": 0.024295032024383545
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4980337917804718,
      "reference_fraction_of_uniform": 0.16504345834255219,
      "rms_normalized_to_uniform_percent": 0.05552739674352539
    },
    "south": {
      "bias_percent": 0.1793235064842646,
      "rms_normalized_error_percent": 0.3142670650877294,
      "absolute_error": {
        "p95": 0.05091468095779417,
        "p99": 0.06280385017395017,
        "maximum": 0.07314682006835938
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.113774299621582,
      "reference_fraction_of_uniform": 0.7004838585853577,
      "rms_normalized_to_uniform_percent": 0.19913412809373923
    },
    "west": {
      "bias_percent": -0.1267110670431894,
      "rms_normalized_error_percent": 0.43801935492807875,
      "absolute_error": {
        "p95": 0.01808280944824211,
        "p99": 0.04098991870880126,
        "maximum": 0.04467892646789551
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.482852041721344,
      "reference_fraction_of_uniform": 0.1600123792886734,
      "rms_normalized_to_uniform_percent": 0.09825968049470156
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
        "identifier": "plan_t_circle_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": 0.011270158601541616,
          "cvrmse_percent": 2.9962856834906746,
          "absolute_error_percentiles_lux": {
            "p50": 0.4300476312637329,
            "p90": 6.391070556640626,
            "p95": 12.688528060913075,
            "p99": 35.975608520507805
          },
          "maximum_absolute_error_lux": 282.591796875,
          "worst": {
            "sensor_index": 38,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 19663.349609375,
            "radiance_lux": 19945.94140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15064687975646876,
            "maximum_error_percentage_points": 2.217671232876711,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2586697990528616,
            "maximum_error_percentage_points": 1.8742193944868575,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2842998477929984,
            "maximum_error_percentage_points": 2.932602739726022,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.28746575342465736,
            "maximum_error_percentage_points": 2.932602739726029,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0037189244038559714,
            "maximum_error_percentage_points": 0.10753424657534794,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
      "maximum_error_percentage_points": 0.004931506849314982,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.004913848458897974,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.006810124963521957,
      "weather_seconds": 0.09237937501166016,
      "metric_reduction_seconds": 0.04345937503967434,
      "write_seconds": 0.03416074998676777,
      "total_seconds": 0.1701692920178175,
      "cold_end_to_end_seconds": 0.17697941698133945,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02271633397322148,
      "engine_upload_seconds": 0.000287917,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.022717291838489473,
      "engine_annual_reduction_seconds": 0.0006047083297744393,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.022717291838489473
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006810124963521957,
      "weather_seconds": 0.09181104204617441,
      "metric_reduction_seconds": 0.012962250038981438,
      "write_seconds": 0.0328153750160709,
      "total_seconds": 0.13803349994122982,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13803349994122982,
      "raw_export_seconds": 0.010044457972981036,
      "engine_upload_seconds": 6.1667e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0005015000933781266,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.009218957973644137,
      "full": 0.025065833004191518
    }
  },
  "elapsed_seconds": 0.7259768340736628,
  "result_class": "passed"
}
```
