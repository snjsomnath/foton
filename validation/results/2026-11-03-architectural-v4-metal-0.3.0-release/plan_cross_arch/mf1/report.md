# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_arch",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_arch",
    "category": "form",
    "question": "How does a arch opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "arch"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "1e9b7b8035795953ab5f80869edab351387d81fbc529f4c3ef891e1949871b3c",
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
      "scene_fingerprint": 3167779511141355274,
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
      "scene_fingerprint": 3167779511141355274,
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
    "model_sha256": "e726265b02d6c86805289479cffc7f97bbcb22a16d44e30f04630866d50ff191",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9a3231f9777058abb1b3cf65cd66b5db7df4d557b41586683d412e16e4487cf8",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006167888641357422,
          "p95": 0.0,
          "p99": 2.5371631636517122e-05
        },
        "bias_percent": 0.1288739559557457,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4119016067570942,
        "worst_index": [
          33,
          133,
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
          "maximum": 0.0003777695819735527,
          "p95": 1.2385287845972925e-05,
          "p99": 7.27679580450058e-05
        },
        "bias_percent": 0.11549445458349115,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1284113115019243,
        "worst_index": [
          18,
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
          "maximum": 0.00028271786868572235,
          "p95": 1.04400678537786e-05,
          "p99": 6.589945405721664e-05
        },
        "bias_percent": -0.020612177313332886,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9611831902329516,
        "worst_index": [
          18,
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00046137755271047354,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010640453547239304
                },
                "candidate_energy": 2.4639961519424105,
                "cvrmse_percent": 16.666171218971947,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.003575514963476653,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4640842556436837,
                "relative_energy_error_percent": 0.0035755149634766527,
                "rms_normalized_rmse_percent": 1.885736080424462,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034635650226846337,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.003924942575395107,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000917539931833744,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1823005024780286e-05,
                  "p99": 0.0002722579229157418
                },
                "candidate_energy": 0.5866071876486956,
                "cvrmse_percent": 160.94181852292687,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.26387504018022473,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5881591929554304,
                "relative_energy_error_percent": 0.2638750401802247,
                "rms_normalized_rmse_percent": 3.932303145261358,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004572048783302307,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": -0.00046033505350351334,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.37833300605416,
            "full": 280.76591703575104
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.10812500678003,
            "full": 266.2629160331562
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.3134169857949,
            "full": 282.7660000184551
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.76466707792133,
            "full": 278.65920902695507
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000398817501263693,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.349948959425092e-05
                },
                "candidate_energy": 2.4624034211628896,
                "cvrmse_percent": 14.44576067719073,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05296988279972563,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4637084446385416,
                "relative_energy_error_percent": 0.05296988279972562,
                "rms_normalized_rmse_percent": 1.6379572336247197,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001079724112059921,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.000680906610796228,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006637926562689245,
                  "p50": 4.251852914194387e-08,
                  "p90": 8.264553798653651e-06,
                  "p95": 1.8029815691988915e-05,
                  "p99": 0.00016189459711313248
                },
                "candidate_energy": 1.1184208693126294,
                "cvrmse_percent": 51.62388806476244,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17307441786869243,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1203599257321244,
                "relative_energy_error_percent": 0.1730744178686924,
                "rms_normalized_rmse_percent": 2.1781730418494076,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00010172274778597057,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0005620699084829539,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.54049990978092,
            "full": 3237.4137500301003
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.63874996080995,
            "full": 3241.5516669861972
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.31950001139194,
            "full": 3272.6200410397723
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.4796659713611,
            "full": 3266.48608292453
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000375522009562701,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.231502190232277e-05
                },
                "candidate_energy": 2.4657339944424166,
                "cvrmse_percent": 13.753344792345734,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.007379771751894411,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.465915973412848,
                "relative_energy_error_percent": 0.0073797717518944116,
                "rms_normalized_rmse_percent": 1.5604352108810917,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0011972320498898625,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0008217100403271616,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004683844745159149,
                  "p50": 4.9999993478877514e-08,
                  "p90": 8.438264103460824e-06,
                  "p95": 1.7377431504428387e-05,
                  "p99": 0.0001597474329173565
                },
                "candidate_energy": 1.11951985184146,
                "cvrmse_percent": 49.05111551266811,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.22086030198179615,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1219978997911682,
                "relative_energy_error_percent": 0.22086030198179613,
                "rms_normalized_rmse_percent": 2.070936414355709,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00047294003888964653,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 4.555564373731613e-06,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.40033396426588,
            "full": 3537.7717500086874
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.4257920468226,
            "full": 3504.464332945645
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.72358401771635,
            "full": 3491.666999994777
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.1100410502404,
            "full": 3487.5040829647332
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00017470400780439377,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.351519212126732e-05
                },
                "candidate_energy": 2.4616085003526678,
                "cvrmse_percent": 7.844444395767229,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06215402088984435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4631394405550964,
                "relative_energy_error_percent": 0.062154020889844355,
                "rms_normalized_rmse_percent": 0.888497937668217,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006054240511730313,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.006228944519534707,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00028113555163145065,
                  "p50": 4.6196905856277226e-08,
                  "p90": 5.796395271318033e-06,
                  "p95": 1.3145661796443164e-05,
                  "p99": 9.063200559467077e-05
                },
                "candidate_energy": 1.1234911872523305,
                "cvrmse_percent": 27.189538341300825,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.003663200397450873,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1234500330262556,
                "relative_energy_error_percent": 0.003663200397450873,
                "rms_normalized_rmse_percent": 1.1498485349768377,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02398878987878561,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.02426992543041706,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.82362504303455,
            "full": 6150.915917009115
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 219.79899995494634,
            "full": 6159.036125056446
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 235.53387506399304,
            "full": 6147.444500005804
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.0640839599073,
            "full": 6161.925041000359
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/plan_cross_arch/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1201.0290829930454,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4118.350500008091,
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
      44,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.016650367887826638,
            "cvrmse_percent": 6.7123516240032055,
            "rms_normalized_rmse_percent": 0.7606781016696392,
            "reference_energy": 2.463778450513473,
            "candidate_energy": 2.4633682223375217,
            "relative_energy_error_percent": 0.016650367887826638,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.773843541741371e-05,
              "maximum": 0.00047633983194828033
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.009515693411231041,
              "candidate": 0.00903935357928276,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9175162140210584,
            "cvrmse_percent": 48.07813003594483,
            "rms_normalized_rmse_percent": 2.03197404806464,
            "reference_energy": 1.1220661449254852,
            "candidate_energy": 1.100550344664498,
            "relative_energy_error_percent": 1.9175162140210584,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.489257131647719e-08,
              "p90": 1.3453116480377503e-05,
              "p95": 2.5441055186092854e-05,
              "p99": 6.845453754067421e-05,
              "maximum": 0.001166822388768196
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020695451647043228,
              "candidate": 0.019528629258275032,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6114606434653546,
            "cvrmse_percent": 14.53910824421205,
            "rms_normalized_rmse_percent": 1.9637281425099022,
            "reference_energy": 3.5858445954389584,
            "candidate_energy": 3.5639185670020197,
            "relative_energy_error_percent": 0.6114606434653546,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.489257131647719e-08,
              "p90": 1.3403376215137541e-05,
              "p95": 2.5373008611495607e-05,
              "p99": 6.605125963687897e-05,
              "maximum": 0.001166822388768196
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020695451647043228,
              "candidate": 0.019528629258275032,
              "position": [
                6.5,
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
      44,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.016650367887826638,
            "cvrmse_percent": 6.7123516240032055,
            "rms_normalized_rmse_percent": 0.7606781016696392,
            "reference_energy": 2.463778450513473,
            "candidate_energy": 2.4633682223375217,
            "relative_energy_error_percent": 0.016650367887826638,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.773843541741371e-05,
              "maximum": 0.00047633983194828033
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.009515693411231041,
              "candidate": 0.00903935357928276,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.28151428049006,
            "cvrmse_percent": 713.7430852770296,
            "rms_normalized_rmse_percent": 17.419864628677466,
            "reference_energy": 0.5876449413027558,
            "candidate_energy": 1.100550344664498,
            "relative_energy_error_percent": 87.28151428049004,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.796999928657897e-05,
              "p95": 9.870257781585678e-05,
              "p99": 0.00026031211018562317,
              "maximum": 0.00651942566037178
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01718568429350853,
              "candidate": 0.02370510995388031,
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
            "nmbe_percent": 16.79528237740715,
            "cvrmse_percent": 137.39558042256752,
            "rms_normalized_rmse_percent": 17.412578776037318,
            "reference_energy": 3.051423391816229,
            "candidate_energy": 3.5639185670020197,
            "relative_energy_error_percent": 16.79528237740715,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.7670000640209764e-05,
              "p95": 9.864156163530424e-05,
              "p99": 0.0002572504454292357,
              "maximum": 0.00651942566037178
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01718568429350853,
              "candidate": 0.02370510995388031,
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
      "bias_percent": -0.1182280720773492,
      "rms_normalized_error_percent": 0.1824502865706934,
      "absolute_error": {
        "p95": 0.036105195100318135,
        "p99": 0.06610796269203871,
        "maximum": 0.08001254195773555
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8247577474789565,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1824502865706934
    },
    "overcast": {
      "bias_percent": -0.1165260678853208,
      "rms_normalized_error_percent": 0.16324484444867046,
      "absolute_error": {
        "p95": 0.023002600669860842,
        "p99": 0.04889555931091309,
        "maximum": 0.056934356689453125
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5248353481292725,
      "reference_fraction_of_uniform": 0.6601294875144958,
      "rms_normalized_to_uniform_percent": 0.11610811822702141
    },
    "horizon": {
      "bias_percent": -0.5469342383645621,
      "rms_normalized_error_percent": 2.1775480747878646,
      "absolute_error": {
        "p95": 0.019936777469891278,
        "p99": 0.033613858006887265,
        "maximum": 0.04237572911113108
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3279634600194685,
      "reference_fraction_of_uniform": 0.08574751178310358,
      "rms_normalized_to_uniform_percent": 0.09677682020491682
    },
    "north": {
      "bias_percent": -96.2370707342535,
      "rms_normalized_error_percent": 100.17519359474286,
      "absolute_error": {
        "p95": 0.00013640850665979094,
        "p99": 0.00027916486753383653,
        "maximum": 0.0003093618724960834
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.6212925149593502e-05,
      "reference_fraction_of_uniform": 6.8534864112734795e-06,
      "rms_normalized_to_uniform_percent": 0.0005918647355852249
    },
    "east": {
      "bias_percent": -0.45259963695852434,
      "rms_normalized_error_percent": 0.3149185885672802,
      "absolute_error": {
        "p95": 0.017110383510589605,
        "p99": 0.02926183640956879,
        "maximum": 0.035861432552337646
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6187556982040405,
      "reference_fraction_of_uniform": 0.16177643835544586,
      "rms_normalized_to_uniform_percent": 0.07218800452226823
    },
    "south": {
      "bias_percent": -0.05456885011365163,
      "rms_normalized_error_percent": 0.21180065357928554,
      "absolute_error": {
        "p95": 0.031018400192260744,
        "p99": 0.04012262344360352,
        "maximum": 0.0449066162109375
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.741787910461426,
      "reference_fraction_of_uniform": 0.7168526649475098,
      "rms_normalized_to_uniform_percent": 0.13948529690158634
    },
    "west": {
      "bias_percent": -0.07176799664979766,
      "rms_normalized_error_percent": 0.23467631501807845,
      "absolute_error": {
        "p95": 0.012102428823709488,
        "p99": 0.018157896995544435,
        "maximum": 0.021846771240234375
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6107609868049622,
      "reference_fraction_of_uniform": 0.15968619287014008,
      "rms_normalized_to_uniform_percent": 0.05144110550932717
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
        "identifier": "plan_cross_arch_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.15105369611320302,
          "cvrmse_percent": 2.4864304571405733,
          "absolute_error_percentiles_lux": {
            "p50": 0.7875795364379883,
            "p90": 8.688812255859379,
            "p95": 14.847418212890624,
            "p99": 37.45047058105469
          },
          "maximum_absolute_error_lux": 168.40869140625,
          "worst": {
            "sensor_index": 19,
            "position": [
              5.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1859.5,
            "foton_lux": 7383.38916015625,
            "radiance_lux": 7214.98046875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10209838107098398,
            "maximum_error_percentage_points": 2.000410958904112,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.29265600369602185,
            "maximum_error_percentage_points": 1.2062095060604605,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.48617061021170593,
            "maximum_error_percentage_points": 3.092465753424662,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4928019925280205,
            "maximum_error_percentage_points": 3.0924657534246567,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006861768368617748,
            "maximum_error_percentage_points": 0.13767123287671268,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.636363636363637,
          "radiance_percent": 13.636363636363637,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.272727272727273,
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
      "maximum_error_percentage_points": 0.00492241010273986,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004520547945190856,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.00492241010273986,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_arch_grid",
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
      "study_preparation_seconds": 0.006995041971094906,
      "weather_seconds": 0.09118387498892844,
      "metric_reduction_seconds": 0.04219487507361919,
      "write_seconds": 0.04072804201859981,
      "total_seconds": 0.17424704099539667,
      "cold_end_to_end_seconds": 0.18124208296649158,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011925833998247981,
      "engine_upload_seconds": 0.000293542,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02231579157523811,
      "engine_annual_reduction_seconds": 0.00042845832649618387,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02231579157523811
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006995041971094906,
      "weather_seconds": 0.09493033308535814,
      "metric_reduction_seconds": 0.012224625097587705,
      "write_seconds": 0.03007758397143334,
      "total_seconds": 0.13760712498333305,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13760712498333305,
      "raw_export_seconds": 0.010351667064242065,
      "engine_upload_seconds": 6.0583e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004730833461508155,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014253500034101307,
      "full": 0.0232050420017913
    }
  },
  "elapsed_seconds": 0.7145403330214322,
  "result_class": "passed"
}
```
