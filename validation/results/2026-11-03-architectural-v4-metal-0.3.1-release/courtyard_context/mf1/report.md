# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_context",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_context",
    "category": "context",
    "question": "How does enclosing context restrict a room's courtyard view?",
    "interactions": [
      "closed_context",
      "courtyard",
      "multiple_obstructions"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 18,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "cb3e924d1247babe58d39c649a3acb275b82974a3274b11ba3543287092e5c1c",
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
      "scene_fingerprint": 4828330442288497760,
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
      "scene_fingerprint": 4828330442288497760,
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
    "model_sha256": "51eefacff3d2ce7d39e1da3d32e708a07944c43faa4fa12312d8e0b7ee1504f4",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00046600401401519775,
          "p95": 0.0,
          "p99": 1.62342912517488e-05
        },
        "bias_percent": -0.16227101852864662,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.0425935331785077,
        "worst_index": [
          17,
          120,
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
          "maximum": 0.0004384508356451988,
          "p95": 2.204608626925616e-05,
          "p99": 6.318642408587039e-05
        },
        "bias_percent": 0.0752073194497973,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9933738280009414,
        "worst_index": [
          2,
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
          "maximum": 0.0005118995904922485,
          "p95": 1.9007203445653427e-05,
          "p99": 5.559297278523445e-05
        },
        "bias_percent": 0.052550541863444676,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8734249004762916,
        "worst_index": [
          14,
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00054964330047369,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.043215474463068e-05
                },
                "candidate_energy": 1.1061403275816701,
                "cvrmse_percent": 25.98958502975077,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04771459602194769,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.106668369923682,
                "relative_energy_error_percent": 0.0477145960219477,
                "rms_normalized_rmse_percent": 1.9387494660971558,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01740814233198762,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.01795778563246131,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010779178701341152,
                  "p50": 0.0,
                  "p90": 2.1849672066309722e-05,
                  "p95": 3.702507306115876e-05,
                  "p99": 0.000162394717335701
                },
                "candidate_energy": 1.7067544922105071,
                "cvrmse_percent": 39.90685330792668,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.15351256880973807,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7093786032149865,
                "relative_energy_error_percent": 0.1535125688097381,
                "rms_normalized_rmse_percent": 2.7447199178367483,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.019897097256034613,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.020975015126168728,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.17791608255357,
            "full": 246.61324999760836
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.78779100999236,
            "full": 236.26954201608896
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.06483290717006,
            "full": 229.10187509842217
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.66533301770687,
            "full": 241.6294579161331
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.06137500610203,
            "full": 240.06149999331683
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.06262497417629,
            "full": 234.2108329758048
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.16220794711262,
            "full": 240.02599995583296
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.46374998334795,
            "full": 230.61991692520678
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00025485106743872166,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.0979088731110096e-05
                },
                "candidate_energy": 1.105685142008042,
                "cvrmse_percent": 13.546417040873829,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03903823880663564,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.106116950584692,
                "relative_energy_error_percent": 0.03903823880663564,
                "rms_normalized_rmse_percent": 1.0129563633906271,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0033054654486477375,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.003560316516086459,
                  "rgb_channel": 0,
                  "sky_patch_index": 101
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000504164956510067,
                  "p50": 2.440944285808655e-06,
                  "p90": 1.98661073227413e-05,
                  "p95": 3.306113148937582e-05,
                  "p99": 0.00012025953037664294
                },
                "candidate_energy": 2.5738894030845785,
                "cvrmse_percent": 17.40263477985998,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04322966397550581,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.572777200146117,
                "relative_energy_error_percent": 0.0432296639755058,
                "rms_normalized_rmse_percent": 1.468331607648155,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017843805253505707,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.01733964029699564,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.554083019495,
            "full": 2430.675374926068
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.083625045605,
            "full": 2410.1223750039935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.44441701844335,
            "full": 2460.507250041701
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.41970802564174,
            "full": 2383.162165991962
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002496374072507024,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.7199665307998657e-05
                },
                "candidate_energy": 1.103110478281451,
                "cvrmse_percent": 15.31056149934439,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.27640391920499385,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1061679699032538,
                "relative_energy_error_percent": 0.27640391920499385,
                "rms_normalized_rmse_percent": 1.1456952169949692,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003636024077422917,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0038856614846736193,
                  "rgb_channel": 0,
                  "sky_patch_index": 120
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005558552220463753,
                  "p50": 2.5386964335183393e-06,
                  "p90": 1.9602131942519918e-05,
                  "p95": 3.139525424558087e-05,
                  "p99": 0.00010428291716380045
                },
                "candidate_energy": 2.577525530984868,
                "cvrmse_percent": 16.350936683437677,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.012675865417990673,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5771988487272495,
                "relative_energy_error_percent": 0.012675865417990675,
                "rms_normalized_rmse_percent": 1.37952364307139,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017673100344836712,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.017117245122790337,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.5977089367807,
            "full": 2572.3267500288785
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.14487505704165,
            "full": 2613.485625013709
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.15358408726752,
            "full": 2564.569750102237
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.81112495437264,
            "full": 2626.5520420856774
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001927390694618225,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.0574382031336427e-05
                },
                "candidate_energy": 1.106291444717499,
                "cvrmse_percent": 9.787930986188691,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.022563679393315623,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.106541121108421,
                "relative_energy_error_percent": 0.022563679393315623,
                "rms_normalized_rmse_percent": 0.7322018099161856,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020472859032452106,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.002240024972707033,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00036329496651887894,
                  "p50": 1.8004402591031976e-06,
                  "p90": 1.4595934771932662e-05,
                  "p95": 2.2125365376268733e-05,
                  "p99": 7.711630314588547e-05
                },
                "candidate_energy": 2.578529268270305,
                "cvrmse_percent": 11.857266667968371,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07833872822633202,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5765108624280657,
                "relative_energy_error_percent": 0.07833872822633202,
                "rms_normalized_rmse_percent": 1.0016618455612512,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02314622513949871,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.02278293017297983,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.64925007801503,
            "full": 4529.708291054703
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.57945797592402,
            "full": 4592.018750030547
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.73575006891042,
            "full": 4469.332332955673
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.25850000232458,
            "full": 4561.697750003077
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/courtyard_context/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 778.7374169565737,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2560.3289580903947,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.060396282560217666,
            "cvrmse_percent": 13.500669362420979,
            "rms_normalized_rmse_percent": 1.0083603335273357,
            "reference_energy": 1.1059725623790655,
            "candidate_energy": 1.1053045960652526,
            "relative_energy_error_percent": 0.06039628256021766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.585122663527727e-05,
              "maximum": 0.00025024404749274254
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.004304821603000164,
              "candidate": 0.0040545775555074215,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.9831587624475382,
            "cvrmse_percent": 29.93745415707719,
            "rms_normalized_rmse_percent": 2.5294307356017205,
            "reference_energy": 2.5779637538016544,
            "candidate_energy": 2.5268386397254154,
            "relative_energy_error_percent": 1.983158762447538,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.6572517981549026e-06,
              "p90": 1.836440060287714e-05,
              "p95": 2.7779394440585747e-05,
              "p99": 8.554616943001747e-05,
              "maximum": 0.0011134501546621323
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027144180610775948,
              "candidate": 0.026030730456113815,
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
            "nmbe_percent": -1.4059168222470204,
            "cvrmse_percent": 20.765992491579823,
            "rms_normalized_rmse_percent": 2.5072401019317976,
            "reference_energy": 3.68393631618072,
            "candidate_energy": 3.632143235790668,
            "relative_energy_error_percent": 1.4059168222470204,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.6579982659313828e-06,
              "p90": 1.8365622963756323e-05,
              "p95": 2.7763523030444033e-05,
              "p99": 7.368798833340406e-05,
              "maximum": 0.0011134501546621323
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027144180610775948,
              "candidate": 0.026030730456113815,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.060396282560217666,
            "cvrmse_percent": 13.500669362420979,
            "rms_normalized_rmse_percent": 1.0083603335273357,
            "reference_energy": 1.1059725623790655,
            "candidate_energy": 1.1053045960652526,
            "relative_energy_error_percent": 0.06039628256021766,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.585122663527727e-05,
              "maximum": 0.00025024404749274254
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.004304821603000164,
              "candidate": 0.0040545775555074215,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 47.89821791774247,
            "cvrmse_percent": 391.96425364487067,
            "rms_normalized_rmse_percent": 26.950371508133443,
            "reference_energy": 1.7084983682026404,
            "candidate_energy": 2.5268386397254154,
            "relative_energy_error_percent": 47.89821791774248,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.072858352330513e-06,
              "p90": 4.909758717985824e-05,
              "p95": 8.684304951884765e-05,
              "p99": 0.00021535999258048832,
              "maximum": 0.0062638092786073685
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009167010895907879,
              "candidate": 0.015430820174515247,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 29.052433845531397,
            "cvrmse_percent": 237.9051530867156,
            "rms_normalized_rmse_percent": 26.946622751264236,
            "reference_energy": 2.814470930581706,
            "candidate_energy": 3.632143235790668,
            "relative_energy_error_percent": 29.0524338455314,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.053869921946898e-06,
              "p90": 4.831000114791095e-05,
              "p95": 8.684304951884765e-05,
              "p99": 0.00021141567412996665,
              "maximum": 0.0062638092786073685
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009167010895907879,
              "candidate": 0.015430820174515247,
              "position": [
                5.5,
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
      "bias_percent": -0.2520175492631436,
      "rms_normalized_error_percent": 0.26744984304588254,
      "absolute_error": {
        "p95": 0.03743089483075018,
        "p99": 0.050771853686193386,
        "maximum": 0.05437188758103062
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.737468769699584,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.26744984304588254
    },
    "overcast": {
      "bias_percent": -0.21505948922504603,
      "rms_normalized_error_percent": 0.24415175265283975,
      "absolute_error": {
        "p95": 0.0301496759057045,
        "p99": 0.031459710001945494,
        "maximum": 0.03157401084899902
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2558441162109375,
      "reference_fraction_of_uniform": 0.8240620493888855,
      "rms_normalized_to_uniform_percent": 0.2077249861427781
    },
    "horizon": {
      "bias_percent": -0.8978174386648166,
      "rms_normalized_error_percent": 5.16836823821877,
      "absolute_error": {
        "p95": 0.007402044446805428,
        "p99": 0.014612273330632114,
        "maximum": 0.018342502899877988
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.04961355726651112,
      "reference_fraction_of_uniform": 0.01812388065050175,
      "rms_normalized_to_uniform_percent": 0.06090864000984755
    },
    "north": {
      "bias_percent": -0.14429575409620016,
      "rms_normalized_error_percent": 1.1346474641867073,
      "absolute_error": {
        "p95": 0.011858716607093811,
        "p99": 0.017409855127334596,
        "maximum": 0.017432093620300293
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.35217994451522827,
      "reference_fraction_of_uniform": 0.1286516785621643,
      "rms_normalized_to_uniform_percent": 0.08561202346261791
    },
    "east": {
      "bias_percent": -0.17850868057772884,
      "rms_normalized_error_percent": 0.46542969672591905,
      "absolute_error": {
        "p95": 0.009351742453873158,
        "p99": 0.012665777467191212,
        "maximum": 0.014412879943847656
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.45311757922172546,
      "reference_fraction_of_uniform": 0.16552428901195526,
      "rms_normalized_to_uniform_percent": 0.0726807578240903
    },
    "south": {
      "bias_percent": -0.3506033036341698,
      "rms_normalized_error_percent": 0.3290523495863848,
      "absolute_error": {
        "p95": 0.02226969599723816,
        "p99": 0.02725396156311035,
        "maximum": 0.027501463890075684
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0274385213851929,
      "reference_fraction_of_uniform": 0.3753243088722229,
      "rms_normalized_to_uniform_percent": 0.13979827923819507
    },
    "west": {
      "bias_percent": -0.566477429143164,
      "rms_normalized_error_percent": 0.7463926637129223,
      "absolute_error": {
        "p95": 0.01750868558883667,
        "p99": 0.02024642080068588,
        "maximum": 0.020504802465438843
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.38935133814811707,
      "reference_fraction_of_uniform": 0.14223042130470276,
      "rms_normalized_to_uniform_percent": 0.09638793165803018
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
        "identifier": "courtyard_context_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.673913282766722,
          "cvrmse_percent": 4.63946088574778,
          "absolute_error_percentiles_lux": {
            "p50": 0.6414632797241211,
            "p90": 9.426977539062504,
            "p95": 18.371228027343747,
            "p99": 45.08190032958978
          },
          "maximum_absolute_error_lux": 245.3592529296875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 1329.5233154296875,
            "radiance_lux": 1574.882568359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.26730213089802074,
            "maximum_error_percentage_points": 1.118630136986301,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.44608074698492683,
            "maximum_error_percentage_points": 1.2831545933904867,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7117275494672756,
            "maximum_error_percentage_points": 2.193972602739734,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7089878234398783,
            "maximum_error_percentage_points": 2.1939726027397253,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.011685692541857013,
            "maximum_error_percentage_points": 0.08602739726027409,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
      "maximum_error_percentage_points": 0.004995719178083391,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004995719178083391,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.0039726027397262165,
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
      "study_preparation_seconds": 0.007629833067767322,
      "weather_seconds": 0.09804737498052418,
      "metric_reduction_seconds": 0.04374154098331928,
      "write_seconds": 0.049800332984887064,
      "total_seconds": 0.19171533302869648,
      "cold_end_to_end_seconds": 0.1993451660964638,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027959082974120975,
      "engine_upload_seconds": 0.000305416,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0245986666996032,
      "engine_annual_reduction_seconds": 0.0003491666866466403,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0245986666996032
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007629833067767322,
      "weather_seconds": 0.09448212489951402,
      "metric_reduction_seconds": 0.012128832982853055,
      "write_seconds": 0.03390133299399167,
      "total_seconds": 0.1409216249594465,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1409216249594465,
      "raw_export_seconds": 0.010730208014138043,
      "engine_upload_seconds": 9.4917e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003458749270066619,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.010090416995808482,
      "full": 0.026791042066179216
    }
  },
  "elapsed_seconds": 0.6919032910373062,
  "result_class": "passed"
}
```
