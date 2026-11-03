# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "4a852021bd332590bbf7381858e9c2edd7635676a7e5dc2683ff7ec4cbe83d5f",
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
      "scene_fingerprint": 8144785219234473868,
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
      "scene_fingerprint": 8144785219234473868,
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
        "identifier": "plan_j_offset_low_grid",
        "bias_percent": 0.0209556389201628,
        "rms_normalized_error_percent": 1.1559886179307046,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.1751195415854454e-05,
          "maximum": 0.00036203162744641304
        },
        "worst_index": [
          4,
          119,
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
        "identifier": "plan_j_offset_low_grid",
        "bias_percent": 0.20107751402351817,
        "rms_normalized_error_percent": 1.316927887758756,
        "absolute_error": {
          "p95": 1.1482861737022176e-05,
          "p99": 4.8481597332283854e-05,
          "maximum": 0.00041568465530872345
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
        "identifier": "plan_j_offset_low_grid",
        "bias_percent": 0.08263373897435211,
        "rms_normalized_error_percent": 1.1736523721034429,
        "absolute_error": {
          "p95": 9.692506864666939e-06,
          "p99": 4.088599234819412e-05,
          "maximum": 0.00029454566538333893
        },
        "worst_index": [
          8,
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
            "identifier": "plan_j_offset_low_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.15815422974786736,
                "cvrmse_percent": 28.21637402940743,
                "rms_normalized_rmse_percent": 2.5975612140579933,
                "reference_energy": 1.4517551389208165,
                "candidate_energy": 1.4494591267630312,
                "relative_energy_error_percent": 0.15815422974786733,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.375298395752907e-05,
                  "maximum": 0.00035267649218440056
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 69,
                  "rgb_channel": 0,
                  "reference": 0.005795401055365801,
                  "candidate": 0.006148077547550201
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.2029640633373003,
                "cvrmse_percent": 92.8822701882697,
                "rms_normalized_rmse_percent": 2.81792180558925,
                "reference_energy": 0.5880372369807674,
                "candidate_energy": 0.5868437327106548,
                "relative_energy_error_percent": 0.2029640633373003,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.879553671344183e-06,
                  "p99": 0.00012764520943164825,
                  "maximum": 0.0005737936589866877
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 69,
                  "rgb_channel": 0,
                  "reference": 0.00039895554073154926,
                  "candidate": -0.0001748381182551384
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 120.9083329886198,
            "full": 267.58904103189707
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 116.05754203628749,
            "full": 260.0413329200819
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.74895798508078,
            "full": 264.0601670136675
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 110.44662492349744,
            "full": 270.4366249963641
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
            "identifier": "plan_j_offset_low_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0750254163931108,
                "cvrmse_percent": 17.04751255225521,
                "rms_normalized_rmse_percent": 1.5668747457132788,
                "reference_energy": 1.4509422280170838,
                "candidate_energy": 1.4498536525688905,
                "relative_energy_error_percent": 0.0750254163931108,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.057005910202861e-05,
                  "maximum": 0.00023339741164818406
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.0022012119879946113,
                  "candidate": 0.001967814576346427
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3962240988042937,
                "cvrmse_percent": 36.58320177453281,
                "rms_normalized_rmse_percent": 1.9618608336878716,
                "reference_energy": 1.2083138802785633,
                "candidate_energy": 1.2131015110614243,
                "relative_energy_error_percent": 0.3962240988042937,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.454330605416999e-08,
                  "p90": 8.189643267542124e-06,
                  "p95": 1.6560858057346195e-05,
                  "p99": 0.00010346947237849236,
                  "maximum": 0.00038557127118110657
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": -6.77141360938549e-05,
                  "candidate": 0.00031785713508725166
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.6812080470845,
            "full": 3190.8676250604913
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.15691601205617,
            "full": 3189.300165977329
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.44783302396536,
            "full": 3156.3592919846997
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.7084579821676,
            "full": 3148.9385419990867
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
            "identifier": "plan_j_offset_low_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.029714958341652834,
                "cvrmse_percent": 15.694981420542806,
                "rms_normalized_rmse_percent": 1.4421425610305778,
                "reference_energy": 1.450125363299776,
                "candidate_energy": 1.4496944591521697,
                "relative_energy_error_percent": 0.029714958341652838,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.5448497985489666e-05,
                  "maximum": 0.00027485541068017483
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0075784914661198854,
                  "candidate": 0.007303636055439711
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.0032011071982928595,
                "cvrmse_percent": 35.47294476147786,
                "rms_normalized_rmse_percent": 1.9075005493358856,
                "reference_energy": 1.2165660653010484,
                "candidate_energy": 1.21652712171716,
                "relative_energy_error_percent": 0.00320110719829286,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.114267516617474e-08,
                  "p90": 8.225970304920338e-06,
                  "p95": 1.5242821973515674e-05,
                  "p99": 8.788181003183126e-05,
                  "maximum": 0.0004533901810646057
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.013801299966871738,
                  "candidate": 0.013347909785807133
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.78658305760473,
            "full": 3550.402416032739
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.4735420504585,
            "full": 3455.0695409998298
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.3858750006184,
            "full": 3448.958875029348
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.93149995803833,
            "full": 3383.621291955933
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
            "identifier": "plan_j_offset_low_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07428327250864411,
                "cvrmse_percent": 10.14254845239223,
                "rms_normalized_rmse_percent": 0.9315058188834147,
                "reference_energy": 1.4496950316256516,
                "candidate_energy": 1.4507719125365384,
                "relative_energy_error_percent": 0.07428327250864411,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.5936518795788288e-05,
                  "maximum": 0.0001739058643579483
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007034938083961606,
                  "candidate": 0.007208843948319554
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.13245487652011345,
                "cvrmse_percent": 26.139327786941998,
                "rms_normalized_rmse_percent": 1.4074584605713427,
                "reference_energy": 1.2176200371723525,
                "candidate_energy": 1.2192328342890733,
                "relative_energy_error_percent": 0.13245487652011345,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0114026000328522e-08,
                  "p90": 5.845800842507742e-06,
                  "p95": 1.0970448784064502e-05,
                  "p99": 5.9011392295360565e-05,
                  "maximum": 0.00036587100476026535
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02403936069458723,
                  "candidate": 0.023673489689826965
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.6317920582369,
            "full": 6069.66266699601
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 207.32425001915544,
            "full": 6034.961500088684
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.0358750000596,
            "full": 6071.068749995902
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.0957079352811,
            "full": 6210.129417013377
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1380.1774999592453,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_offset_low/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 5202.895084046759,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      47,
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
        "identifier": "plan_j_offset_low_grid",
        "full_identifier": "plan_j_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.006657619246722185,
            "cvrmse_percent": 5.332090428255265,
            "rms_normalized_rmse_percent": 0.49025220498768407,
            "reference_energy": 1.4508272600794498,
            "candidate_energy": 1.4509238506343536,
            "relative_energy_error_percent": 0.006657619246722184,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.083879947662354e-06,
              "maximum": 0.00013641361147165298
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313624490052462,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4369141736718771,
            "cvrmse_percent": 75.36923545543137,
            "rms_normalized_rmse_percent": 4.0556240193926625,
            "reference_energy": 1.2178326442990883,
            "candidate_energy": 1.2003334344215517,
            "relative_energy_error_percent": 1.4369141736718771,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.999999880794803e-08,
              "p90": 2.7626927476376295e-05,
              "p95": 4.6636305341962725e-05,
              "p99": 0.00010549074795562774,
              "maximum": 0.0015961145982146263
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016619674861431122,
              "candidate": 0.015023560263216496,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6521107951627689,
            "cvrmse_percent": 34.432270941565804,
            "rms_normalized_rmse_percent": 4.060082543136112,
            "reference_energy": 2.668659904378538,
            "candidate_energy": 2.6512572850559053,
            "relative_energy_error_percent": 0.6521107951627689,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.999999703159119e-08,
              "p90": 2.7406727895140648e-05,
              "p95": 4.6636305341962725e-05,
              "p99": 0.00011100282426923513,
              "maximum": 0.0015961145982146263
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016619674861431122,
              "candidate": 0.015023560263216496,
              "position": [
                1.5,
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
      47,
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
        "identifier": "plan_j_offset_low_grid",
        "full_identifier": "plan_j_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.006657619246722185,
            "cvrmse_percent": 5.332090428255265,
            "rms_normalized_rmse_percent": 0.49025220498768407,
            "reference_energy": 1.4508272600794498,
            "candidate_energy": 1.4509238506343536,
            "relative_energy_error_percent": 0.006657619246722184,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.083879947662354e-06,
              "maximum": 0.00013641361147165298
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313624490052462,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 104.4093728985498,
            "cvrmse_percent": 840.8175410271983,
            "rms_normalized_rmse_percent": 25.49491303793169,
            "reference_energy": 0.5872203497328314,
            "candidate_energy": 1.2003334344215517,
            "relative_energy_error_percent": 104.4093728985498,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.184999801917002e-05,
              "p95": 0.00011494933823996689,
              "p99": 0.0002566399925854057,
              "maximum": 0.006271674297749996
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009328166022896767,
              "candidate": 0.015599840320646763,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 30.08809373693213,
            "cvrmse_percent": 242.26847672108045,
            "rms_normalized_rmse_percent": 25.49540458005552,
            "reference_energy": 2.0380476098122813,
            "candidate_energy": 2.6512572850559053,
            "relative_energy_error_percent": 30.088093736932134,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.183038567542098e-05,
              "p95": 0.00011424999684095383,
              "p99": 0.0002613416872918606,
              "maximum": 0.006271674297749996
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009328166022896767,
              "candidate": 0.015599840320646763,
              "position": [
                1.5,
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
      "bias_percent": 0.21518616323920345,
      "rms_normalized_error_percent": 0.47917457227577664,
      "absolute_error": {
        "p95": 0.07772007998692855,
        "p99": 0.11089957522009039,
        "maximum": 0.13385267025298053
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.306299476070004,
      "rms_normalized_to_uniform_percent": 0.47917457227577664
    },
    "overcast": {
      "bias_percent": 0.32902186035598363,
      "rms_normalized_error_percent": 0.41396323806411145,
      "absolute_error": {
        "p95": 0.042181384563446014,
        "p99": 0.06202602863311765,
        "maximum": 0.07255053520202637
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.4052648544311523,
      "rms_normalized_to_uniform_percent": 0.2673226227226255
    },
    "horizon": {
      "bias_percent": -0.00025187578792732726,
      "rms_normalized_error_percent": 3.95841028374296,
      "absolute_error": {
        "p95": 0.03947622387480934,
        "p99": 0.06801384852806293,
        "maximum": 0.08448245650746777
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.27108863511078624,
      "rms_normalized_to_uniform_percent": 0.2636426227858925
    },
    "north": {
      "bias_percent": -92.83482261532814,
      "rms_normalized_error_percent": 100.9366397067152,
      "absolute_error": {
        "p95": 5.651954757013297e-05,
        "p99": 0.00022605094200116557,
        "maximum": 0.00036001051194034517
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.6801785022835247e-05,
      "rms_normalized_to_uniform_percent": 0.0007152398291415958
    },
    "east": {
      "bias_percent": -0.6208804952377222,
      "rms_normalized_error_percent": 0.6771246886364813,
      "absolute_error": {
        "p95": 0.030273248255252804,
        "p99": 0.03379116237163544,
        "maximum": 0.03435143828392029
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.3696215748786926,
      "rms_normalized_to_uniform_percent": 0.15187244698657434
    },
    "south": {
      "bias_percent": 0.12411406737705487,
      "rms_normalized_error_percent": 0.5475726765722551,
      "absolute_error": {
        "p95": 0.06653583049774169,
        "p99": 0.08686140894889831,
        "maximum": 0.0879061222076416
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.7015191316604614,
      "rms_normalized_to_uniform_percent": 0.40043921844490704
    },
    "west": {
      "bias_percent": 0.5356543651642615,
      "rms_normalized_error_percent": 0.7877374319138839,
      "absolute_error": {
        "p95": 0.03095374107360838,
        "p99": 0.03582571625709533,
        "maximum": 0.037778764963150024
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.537695050239563,
      "rms_normalized_to_uniform_percent": 0.17938869558866985
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
        "identifier": "plan_j_offset_low_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.11124756908373307,
          "cvrmse_percent": 7.487259307589191,
          "absolute_error_percentiles_lux": {
            "p50": 0.9307727813720703,
            "p90": 18.575173950195314,
            "p95": 31.78390350341796,
            "p99": 70.73407524108889
          },
          "maximum_absolute_error_lux": 260.0869140625,
          "worst": {
            "sensor_index": 9,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 16310.8447265625,
            "radiance_lux": 16570.931640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5163305158845819,
            "maximum_error_percentage_points": 4.029452054794522,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.560084371541767,
            "maximum_error_percentage_points": 3.626876663554718,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5065170504226175,
            "maximum_error_percentage_points": 3.588904109589045,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5113582046050715,
            "maximum_error_percentage_points": 3.588904109589045,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006030311862430912,
            "maximum_error_percentage_points": 0.2494520547945207,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 8.51063829787234,
          "radiance_percent": 8.51063829787234,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
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
            "identifier": "plan_j_offset_low_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_offset_low_grid",
            "maximum_error_percentage_points": 0.0047668833275363864,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_offset_low_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_offset_low_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_offset_low_grid",
            "maximum_error_percentage_points": 0.0028767123287671836,
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
      "study_preparation_seconds": 0.01094133302103728,
      "weather_seconds": 0.11360645806416869,
      "metric_reduction_seconds": 0.10403129202313721,
      "write_seconds": 0.06211087491828948,
      "total_seconds": 0.28039229195564985,
      "cold_end_to_end_seconds": 0.29133362497668713,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.028796291910111904,
      "engine_upload_seconds": 0.000338208,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01889170822687447,
      "engine_annual_reduction_seconds": 0.0006036249687895179,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01889170822687447
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.01094133302103728,
      "weather_seconds": 0.1088949590921402,
      "metric_reduction_seconds": 0.015754458960145712,
      "write_seconds": 0.08776491601020098,
      "total_seconds": 0.21258654189296067,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.21258654189296067,
      "raw_export_seconds": 0.018175165983848274,
      "engine_upload_seconds": 7.5958e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006580000044777989,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01798933290410787,
      "full": 0.02271308400668204
    }
  },
  "elapsed_seconds": 62.655585667002015,
  "result_class": "passed"
}
```
