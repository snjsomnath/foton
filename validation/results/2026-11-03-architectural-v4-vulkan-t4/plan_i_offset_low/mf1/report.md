# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4399999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "a63ff0ba5deef98e2e5dffefd8409e8ef2f17d940084c574e1e8e1854c7c99a3",
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
      "scene_fingerprint": 8364362664664098958,
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
      "scene_fingerprint": 8364362664664098958,
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
    "model_sha256": "9778f08e7e3143835cb1853ce8405829109e98b622205ab00a1b5309f2b50973",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "274288e18ebb896ca8da417745929f291321088f610eaef564604626c7d101ce",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00036203162744641304,
          "p95": 0.0,
          "p99": 2.591405063867569e-07
        },
        "bias_percent": 0.02542228369314817,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.126473137797895,
        "worst_index": [
          4,
          119,
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
          "maximum": 0.0004828907549381256,
          "p95": 5.640153176500462e-06,
          "p99": 2.3149390472099185e-05
        },
        "bias_percent": 0.11452125880723993,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.291420805358816,
        "worst_index": [
          4,
          73,
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
          "maximum": 0.0002458179369568825,
          "p95": 4.766494384966791e-06,
          "p99": 2.0703082554973662e-05
        },
        "bias_percent": -0.02775071958722772,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8639339965448317,
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042831525206565857,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.6798807084560394e-07
                },
                "candidate_energy": 1.3514033217711585,
                "cvrmse_percent": 38.06466808158922,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.22641508297877366,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3544700462502988,
                "relative_energy_error_percent": 0.2264150829787737,
                "rms_normalized_rmse_percent": 2.6274152087239844,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014146399684250355,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.014574714936316013,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006130998954176903,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.18956478824839e-05
                },
                "candidate_energy": 0.4087194867219637,
                "cvrmse_percent": 209.14391248731928,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9029249988877168,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4050620799411604,
                "relative_energy_error_percent": 0.9029249988877168,
                "rms_normalized_rmse_percent": 3.600400263813284,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00017868541181087494,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.00043441448360681534,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.76916599739343,
            "full": 402.9854160035029
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.91049998812377,
            "full": 381.03941606823355
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.104083025828,
            "full": 394.1602080594748
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.9472910715267,
            "full": 399.6257079998031
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004303199239075184,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4775432646274567e-06
                },
                "candidate_energy": 1.3529869505927081,
                "cvrmse_percent": 31.48310359111049,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.16253670104708473,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3507914187825918,
                "relative_energy_error_percent": 0.16253670104708473,
                "rms_normalized_rmse_percent": 2.167371178473601,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013511550147086382,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.0139418700709939,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008359658531844616,
                  "p50": 0.0,
                  "p90": 3.5785271847998956e-06,
                  "p95": 7.745290304228547e-06,
                  "p99": 4.2716506868600845e-05
                },
                "candidate_energy": 0.9158862704910327,
                "cvrmse_percent": 73.71121649226232,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1603449638980422,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9173572065727278,
                "relative_energy_error_percent": 0.1603449638980422,
                "rms_normalized_rmse_percent": 2.461894196586231,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -6.786501035094261e-05,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.000768100842833519,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.1886250646785,
            "full": 5306.7661670502275
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.23087509535253,
            "full": 5358.185624936596
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.48216707073152,
            "full": 5312.871792004444
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.78816702961922,
            "full": 5380.831666057929
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024317344650626183,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.5465215028598323e-06
                },
                "candidate_energy": 1.3539542884993807,
                "cvrmse_percent": 21.584579430699982,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.09608866634182972,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3526545407909225,
                "relative_energy_error_percent": 0.09608866634182973,
                "rms_normalized_rmse_percent": 1.4849353233857174,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0070880509447306395,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.007331224391236901,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005337842740118504,
                  "p50": 0.0,
                  "p90": 3.394354848751391e-06,
                  "p95": 7.807479960320052e-06,
                  "p99": 4.021813947474584e-05
                },
                "candidate_energy": 0.9181007028210395,
                "cvrmse_percent": 57.35614032596831,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0645786232886451,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9175081886642396,
                "relative_energy_error_percent": 0.0645786232886451,
                "rms_normalized_rmse_percent": 1.9151915134943693,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00041678454726934433,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": -0.00011699972674250603,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.736874951981,
            "full": 5746.542958077043
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.84524991177022,
            "full": 5810.280916979536
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.58291697409004,
            "full": 5791.559834033251
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.4126250334084,
            "full": 5700.5074579501525
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00013641302939504385,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.2132464917158359e-06
                },
                "candidate_energy": 1.3528195441339221,
                "cvrmse_percent": 12.90556033422569,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.12116725823499955,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.351182353522404,
                "relative_energy_error_percent": 0.12116725823499953,
                "rms_normalized_rmse_percent": 0.8877027890142353,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003698691027238965,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.003562277997843921,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00035024434328079224,
                  "p50": 0.0,
                  "p90": 2.44514694713871e-06,
                  "p95": 5.4917541092436295e-06,
                  "p99": 2.4868277250789106e-05
                },
                "candidate_energy": 0.9172948726415804,
                "cvrmse_percent": 34.22455151717251,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2572221085736691,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9196604426238153,
                "relative_energy_error_percent": 0.2572221085736691,
                "rms_normalized_rmse_percent": 1.1445707236438036,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02892336528748274,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.02927360963076353,
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 307.2730000130832,
            "full": 10092.162124929018
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.1915420908481,
            "full": 10253.105834010057
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 300.9062920464203,
            "full": 10191.881040926091
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 312.5745420111343,
            "full": 10001.995790982619
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_i_offset_low/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3140.312875038944,
      "invocation_count": 5,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10200.534416013397,
      "invocation_count": 5,
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
      74,
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
        "identifier": "plan_i_offset_low_grid",
        "full_identifier": "plan_i_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016398942589203942,
            "cvrmse_percent": 6.968549745597011,
            "rms_normalized_rmse_percent": 0.4797186531642916,
            "reference_energy": 1.3534391101221956,
            "candidate_energy": 1.3536610598248444,
            "relative_energy_error_percent": 0.016398942589203942,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.7927959561347961e-07,
              "maximum": 0.0001364145427942276
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313623558729887,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.6989680553757003,
            "cvrmse_percent": 52.06244509484456,
            "rms_normalized_rmse_percent": 1.7368279297736229,
            "reference_energy": 0.9170394953855663,
            "candidate_energy": 0.901459287303787,
            "relative_energy_error_percent": 1.6989680553757003,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.123507773736492e-06,
              "p95": 1.2766427971655503e-05,
              "p99": 3.961488255299628e-05,
              "maximum": 0.0007491819560527802
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031778931617736816,
              "candidate": 0.031029749661684036,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6764326403197203,
            "cvrmse_percent": 20.912420994194463,
            "rms_normalized_rmse_percent": 1.727292631530345,
            "reference_energy": 2.270478605507762,
            "candidate_energy": 2.2551203471286314,
            "relative_energy_error_percent": 0.6764326403197202,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.974718078505248e-06,
              "p95": 1.2648964911932126e-05,
              "p99": 3.850640496239066e-05,
              "maximum": 0.0007491819560527802
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031778931617736816,
              "candidate": 0.031029749661684036,
              "position": [
                0.5,
                0.5,
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
      74,
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
        "identifier": "plan_i_offset_low_grid",
        "full_identifier": "plan_i_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016398942589203942,
            "cvrmse_percent": 6.968549745597011,
            "rms_normalized_rmse_percent": 0.4797186531642916,
            "reference_energy": 1.3534391101221956,
            "candidate_energy": 1.3536610598248444,
            "relative_energy_error_percent": 0.016398942589203942,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.7927959561347961e-07,
              "maximum": 0.0001364145427942276
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.007450038101524115,
              "candidate": 0.007313623558729887,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 121.82212691319535,
            "cvrmse_percent": 1526.418978684717,
            "rms_normalized_rmse_percent": 26.394465782154832,
            "reference_energy": 0.40638835261756867,
            "candidate_energy": 0.901459287303787,
            "relative_energy_error_percent": 121.82212691319535,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7419999494450167e-05,
              "p95": 4.872999852523208e-05,
              "p99": 0.00018802471458911896,
              "maximum": 0.007822388783097267
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010616740211844444,
              "candidate": 0.01843912899494171,
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
            "nmbe_percent": 28.144400225336685,
            "cvrmse_percent": 352.46534180174416,
            "rms_normalized_rmse_percent": 26.392733749254017,
            "reference_energy": 1.7598274627397643,
            "candidate_energy": 2.2551203471286314,
            "relative_energy_error_percent": 28.144400225336685,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.734999932523351e-05,
              "p95": 4.797731025973917e-05,
              "p99": 0.00018629999249242246,
              "maximum": 0.007822388783097267
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010616740211844444,
              "candidate": 0.01843912899494171,
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
      "bias_percent": -0.25137038966351294,
      "rms_normalized_error_percent": 0.23653817615445086,
      "absolute_error": {
        "p95": 0.03106311268254534,
        "p99": 0.05390880170169683,
        "maximum": 0.08099126123087874
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3223710580953278,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23653817615445086
    },
    "overcast": {
      "bias_percent": -0.21960245246791846,
      "rms_normalized_error_percent": 0.21664677637720453,
      "absolute_error": {
        "p95": 0.01705987975001335,
        "p99": 0.03008357957005492,
        "maximum": 0.04644119739532471
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8198243379592896,
      "reference_fraction_of_uniform": 0.6199654340744019,
      "rms_normalized_to_uniform_percent": 0.139967031907372
    },
    "horizon": {
      "bias_percent": -0.6131877548698427,
      "rms_normalized_error_percent": 0.8916694766653249,
      "absolute_error": {
        "p95": 0.008426416565798333,
        "p99": 0.011808543290783268,
        "maximum": 0.012882817467496338
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.12419415621204624,
      "reference_fraction_of_uniform": 0.09391778158766483,
      "rms_normalized_to_uniform_percent": 0.05552500937810214
    },
    "north": {
      "bias_percent": -51.236621505892494,
      "rms_normalized_error_percent": 77.99786355041303,
      "absolute_error": {
        "p95": 7.322963101614727e-05,
        "p99": 8.627814568171738e-05,
        "maximum": 9.40929603530094e-05
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.856793101585936e-06,
      "reference_fraction_of_uniform": 6.697661319776671e-06,
      "rms_normalized_to_uniform_percent": 0.0003690840151096328
    },
    "east": {
      "bias_percent": -0.5138435142179936,
      "rms_normalized_error_percent": 0.38529572413814583,
      "absolute_error": {
        "p95": 0.010045727714896176,
        "p99": 0.023763054013252224,
        "maximum": 0.02977663278579712
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.21710915863513947,
      "reference_fraction_of_uniform": 0.16418172419071198,
      "rms_normalized_to_uniform_percent": 0.08631130611186161
    },
    "south": {
      "bias_percent": -0.2502966857046678,
      "rms_normalized_error_percent": 0.26426995546880977,
      "absolute_error": {
        "p95": 0.02943673282861709,
        "p99": 0.04702274322509757,
        "maximum": 0.06272757053375244
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.959557294845581,
      "reference_fraction_of_uniform": 0.7256339192390442,
      "rms_normalized_to_uniform_percent": 0.19312535239393352
    },
    "west": {
      "bias_percent": -0.19729321673668834,
      "rms_normalized_error_percent": 0.3235295892804329,
      "absolute_error": {
        "p95": 0.009983992390334595,
        "p99": 0.014476341605186438,
        "maximum": 0.018978595733642578
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3160291016101837,
      "reference_fraction_of_uniform": 0.23898671567440033,
      "rms_normalized_to_uniform_percent": 0.07369248781839939
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
        "identifier": "plan_i_offset_low_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.2651733215747699,
          "cvrmse_percent": 4.514714005765659,
          "absolute_error_percentiles_lux": {
            "p50": 0.144296333193779,
            "p90": 4.4120816707611095,
            "p95": 8.509561729431129,
            "p99": 23.478507843017567
          },
          "maximum_absolute_error_lux": 176.119140625,
          "worst": {
            "sensor_index": 9,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 14768.76171875,
            "radiance_lux": 14944.880859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.05510366530914458,
            "maximum_error_percentage_points": 2.222602739726028,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.19401319763438113,
            "maximum_error_percentage_points": 1.2022267542554612,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.17301740096260626,
            "maximum_error_percentage_points": 3.36561643835617,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.17442798963346917,
            "maximum_error_percentage_points": 3.365616438356164,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.001388374676045951,
            "maximum_error_percentage_points": 0.04986301369863,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.405405405405405,
          "radiance_percent": 5.405405405405405,
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
      "maximum_error_percentage_points": 0.004964281892124944,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.004964281892124944,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_offset_low_grid",
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
      "study_preparation_seconds": 0.45878488200105494,
      "weather_seconds": 0.4275708900022437,
      "metric_reduction_seconds": 0.5173095089994604,
      "write_seconds": 0.04137834300126997,
      "total_seconds": 0.9867120170019916,
      "cold_end_to_end_seconds": 1.4454968990030466,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01396226600263617,
      "engine_upload_seconds": 0.017773721,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024774101,
      "engine_annual_reduction_seconds": 0.012139581,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024774101
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.45878488200105494,
      "weather_seconds": 0.4270768850001332,
      "metric_reduction_seconds": 0.2701681029975589,
      "write_seconds": 0.02415075600220007,
      "total_seconds": 0.7222318150015781,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.7222318150015781,
      "raw_export_seconds": 0.011186001000169199,
      "engine_upload_seconds": 0.01590579,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 6.6e-08,
      "engine_annual_reduction_seconds": 0.012193516,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.016984338999463944,
      "full": 0.035197514000174124
    }
  },
  "elapsed_seconds": 4.039031642001646,
  "result_class": "passed"
}
```
