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
  "model_sha256": "119e23184f8d9bc6d7dc0b23424da8ae403e6effb3b4ba8e216c7371d17e9edb",
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
      "solver_version": "0.2.0",
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.1288739559557457,
        "rms_normalized_error_percent": 1.4119016067570942,
        "absolute_error": {
          "p95": 0.0,
          "p99": 2.5371631636517122e-05,
          "maximum": 0.0006167888641357422
        },
        "worst_index": [
          33,
          133,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.1090059392920461,
        "rms_normalized_error_percent": 1.295184435658015,
        "absolute_error": {
          "p95": 1.2175529263913631e-05,
          "p99": 8.954014629125595e-05,
          "maximum": 0.0004080869257450104
        },
        "worst_index": [
          21,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": -0.1471301433467679,
        "rms_normalized_error_percent": 1.0610895481238756,
        "absolute_error": {
          "p95": 1.1543743312358856e-05,
          "p99": 6.903987377882004e-05,
          "maximum": 0.00026282109320163727
        },
        "worst_index": [
          21,
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.19316529679918437,
                "cvrmse_percent": 34.54131399064717,
                "rms_normalized_rmse_percent": 3.914459736278427,
                "reference_energy": 2.4615372808111715,
                "candidate_energy": 2.45678244501687,
                "relative_energy_error_percent": 0.19316529679918432,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0002610449446365237,
                  "maximum": 0.0009035351686179638
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.006812316831201315,
                  "candidate": 0.007715851999819279
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2285392667584732,
                "cvrmse_percent": 185.01404584226236,
                "rms_normalized_rmse_percent": 4.53359442969232,
                "reference_energy": 0.5909413345476615,
                "candidate_energy": 0.5922918675406095,
                "relative_energy_error_percent": 0.22853926675847316,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1563910447875969e-05,
                  "p99": 0.00029999157413840294,
                  "maximum": 0.0009244921384379268
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 20,
                  "rgb_channel": 0,
                  "reference": 0.0005992839578539133,
                  "candidate": 0.00152377609629184
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 121.979666990228,
            "full": 279.8307080520317
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.5447500795126,
            "full": 270.3342910390347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 116.36283400002867,
            "full": 265.8372090663761
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 122.53091600723565,
            "full": 269.0594169544056
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.027832086133738592,
                "cvrmse_percent": 15.229212876876252,
                "rms_normalized_rmse_percent": 1.7245420471753432,
                "reference_energy": 2.462383797774237,
                "candidate_energy": 2.461698464994697,
                "relative_energy_error_percent": 0.02783208613373859,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.32102557271719e-05,
                  "maximum": 0.00038781994953751564
                },
                "worst": {
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.0075544798746705055,
                  "candidate": 0.00716665992513299
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.579016000384501,
                "cvrmse_percent": 56.72883955005401,
                "rms_normalized_rmse_percent": 2.407925611570678,
                "reference_energy": 1.1277564221746914,
                "candidate_energy": 1.1212265320449362,
                "relative_energy_error_percent": 0.5790160003845009,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.818066301481849e-08,
                  "p90": 8.587750926380977e-06,
                  "p95": 1.8546903447713703e-05,
                  "p99": 0.0001512009184807539,
                  "maximum": 0.0007025944069027901
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020779444836080074,
                  "candidate": 0.020076850429177284
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.73620897904038,
            "full": 3192.8210409823805
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.08204200584441,
            "full": 3268.258332973346
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.85570903122425,
            "full": 3191.5970420232043
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.56695899087936,
            "full": 3251.1800420470536
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.2368813017735308,
                "cvrmse_percent": 16.01465740977293,
                "rms_normalized_rmse_percent": 1.8165517077951245,
                "reference_energy": 2.466590726375216,
                "candidate_energy": 2.4607478341531532,
                "relative_energy_error_percent": 0.2368813017735308,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.411311475560069e-05,
                  "maximum": 0.00039690127596259117
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007504708599299192,
                  "candidate": 0.007901609875261784
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.8303786753325287,
                "cvrmse_percent": 54.992521750503116,
                "rms_normalized_rmse_percent": 2.320756340104566,
                "reference_energy": 1.1221139770455366,
                "candidate_energy": 1.1314317722238485,
                "relative_energy_error_percent": 0.8303786753325287,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.371541706404969e-08,
                  "p90": 8.296401119878283e-06,
                  "p95": 1.8677985281101428e-05,
                  "p99": 0.0001633784850127995,
                  "maximum": 0.0007911408320069313
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020156679674983025,
                  "candidate": 0.020947820506989956
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.64833297301084,
            "full": 3463.134292047471
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.9451250359416,
            "full": 3448.3387080254033
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 153.35416700690985,
            "full": 3476.4875419205055
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.47875000163913,
            "full": 3428.23595891241
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08246993629786957,
                "cvrmse_percent": 8.228728017750887,
                "rms_normalized_rmse_percent": 0.9328776833339436,
                "reference_energy": 2.464280768926983,
                "candidate_energy": 2.4622484781466483,
                "relative_energy_error_percent": 0.08246993629786957,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.675518721342087e-05,
                  "maximum": 0.00024351617321372032
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0077414915431290865,
                  "candidate": 0.007497975369915366
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.49452854033947063,
                "cvrmse_percent": 29.775868289591443,
                "rms_normalized_rmse_percent": 1.2555463087057528,
                "reference_energy": 1.1191277102581907,
                "candidate_energy": 1.124662116188265,
                "relative_energy_error_percent": 0.49452854033947063,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.9999993478877514e-08,
                  "p90": 6.007465344737284e-06,
                  "p95": 1.28799511003308e-05,
                  "p99": 8.179305586963892e-05,
                  "maximum": 0.0003448566421866417
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 7.226807065308094e-05,
                  "candidate": 0.00041712471283972263
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.24858292471617,
            "full": 6086.893209023401
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.90750001370907,
            "full": 6140.309292008169
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 224.84366700518876,
            "full": 6098.466750001535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.35179105680436,
            "full": 6097.055959049612
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1147.5051250308752,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_cross_arch/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 4146.318375016563,
      "worker_pool_size": 12,
      "invocation_count": 3
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
            "nmbe_percent": -0.8097034185631058,
            "cvrmse_percent": 69.21053328228864,
            "rms_normalized_rmse_percent": 2.923757546250739,
            "reference_energy": 1.1213810918148255,
            "candidate_energy": 1.1123012307792806,
            "relative_energy_error_percent": 0.8097034185631059,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.599043883033119e-08,
              "p90": 2.514761308702873e-05,
              "p95": 4.8346824769396335e-05,
              "p99": 0.00013565620247391053,
              "maximum": 0.0013692695647478104
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02411765046417713,
              "candidate": 0.025486920028924942,
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
            "nmbe_percent": -0.26470479484807785,
            "cvrmse_percent": 21.265467918616828,
            "rms_normalized_rmse_percent": 2.8720987058531025,
            "reference_energy": 3.5851595423282987,
            "candidate_energy": 3.5756694531168023,
            "relative_energy_error_percent": 0.26470479484807785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.66138015251272e-08,
              "p90": 2.517929533496499e-05,
              "p95": 4.864295988227241e-05,
              "p99": 0.00012465938925743103,
              "maximum": 0.0013692695647478104
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02411765046417713,
              "candidate": 0.025486920028924942,
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
            "nmbe_percent": 89.48977998072563,
            "cvrmse_percent": 785.4447607587895,
            "rms_normalized_rmse_percent": 19.133074752425618,
            "reference_energy": 0.5869980063792468,
            "candidate_energy": 1.1123012307792806,
            "relative_energy_error_percent": 89.48977998072563,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.745000114780851e-05,
              "p95": 0.00010558310896158218,
              "p99": 0.0003238373901695013,
              "maximum": 0.007962649688124657
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017524270340800285,
              "candidate": 0.025486920028924942,
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
            "nmbe_percent": 17.205226395338613,
            "cvrmse_percent": 151.01482266194373,
            "rms_normalized_rmse_percent": 19.118880475053583,
            "reference_energy": 3.05077645689272,
            "candidate_energy": 3.5756694531168023,
            "relative_energy_error_percent": 17.20522639533861,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.745000114780851e-05,
              "p95": 0.00010524137178435922,
              "p99": 0.00031459005549550056,
              "maximum": 0.007962649688124657
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017524270340800285,
              "candidate": 0.025486920028924942,
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
      "bias_percent": -0.2360638465083293,
      "rms_normalized_error_percent": 0.35178730254349333,
      "absolute_error": {
        "p95": 0.06858440222591802,
        "p99": 0.12095626257493138,
        "maximum": 0.12213560437000703
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.823703277025741,
      "rms_normalized_to_uniform_percent": 0.35178730254349333
    },
    "overcast": {
      "bias_percent": -0.2634978901430926,
      "rms_normalized_error_percent": 0.24389220209800286,
      "absolute_error": {
        "p95": 0.04857129454612732,
        "p99": 0.056251471042633054,
        "maximum": 0.05745720863342285
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.524775505065918,
      "rms_normalized_to_uniform_percent": 0.17349192228713625
    },
    "horizon": {
      "bias_percent": -0.3354737645965843,
      "rms_normalized_error_percent": 3.702733157616417,
      "absolute_error": {
        "p95": 0.033406356027219766,
        "p99": 0.040043822775667,
        "maximum": 0.04015308621324576
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.3280761103356904,
      "rms_normalized_to_uniform_percent": 0.164811158972161
    },
    "north": {
      "bias_percent": -100.0,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 9.819204751693178e-05,
        "p99": 0.00018598630515043624,
        "maximum": 0.00020568374020513147
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 2.2943793737795204e-05,
      "rms_normalized_to_uniform_percent": 0.000434005971561956
    },
    "east": {
      "bias_percent": -0.8110410349766688,
      "rms_normalized_error_percent": 0.6741473385183434,
      "absolute_error": {
        "p95": 0.027471912093460563,
        "p99": 0.06345545530319215,
        "maximum": 0.0730586051940918
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.6183812618255615,
      "rms_normalized_to_uniform_percent": 0.15457757199443511
    },
    "south": {
      "bias_percent": -0.11110555333134498,
      "rms_normalized_error_percent": 0.48232189224181354,
      "absolute_error": {
        "p95": 0.06187534779310227,
        "p99": 0.112407386302948,
        "maximum": 0.11580848693847656
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.740396499633789,
      "rms_normalized_to_uniform_percent": 0.3175658122565178
    },
    "west": {
      "bias_percent": -0.11729639548275281,
      "rms_normalized_error_percent": 0.5788482642964368,
      "absolute_error": {
        "p95": 0.03123821020126343,
        "p99": 0.04487496316432953,
        "maximum": 0.04844611883163452
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.6103531122207642,
      "rms_normalized_to_uniform_percent": 0.12686753897726963
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
          "nmbe_percent": -0.15894241917691182,
          "cvrmse_percent": 4.028206946859539,
          "absolute_error_percentiles_lux": {
            "p50": 1.465677261352539,
            "p90": 16.58227210044861,
            "p95": 27.58706588745113,
            "p99": 62.17013122558592
          },
          "maximum_absolute_error_lux": 236.9951171875,
          "worst": {
            "sensor_index": 33,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2603.5,
            "foton_lux": 12992.76953125,
            "radiance_lux": 12755.7744140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1485709838107099,
            "maximum_error_percentage_points": 1.1801369863013704,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4511942935034878,
            "maximum_error_percentage_points": 1.5166310055179846,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7028704856787045,
            "maximum_error_percentage_points": 4.626575342465742,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7026120797011205,
            "maximum_error_percentage_points": 4.626575342465754,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.011432129514321343,
            "maximum_error_percentage_points": 0.19506849315068564,
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
      "maximum_error_percentage_points": 0.004969499143832934,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004969499143832934,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
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
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.007624582969583571,
      "weather_seconds": 0.10596008296124637,
      "metric_reduction_seconds": 0.03628779202699661,
      "write_seconds": 0.03873704106081277,
      "total_seconds": 0.18117499991785735,
      "cold_end_to_end_seconds": 0.18879958288744092,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027583459042944014,
      "engine_upload_seconds": 0.000293042,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.017663458362221718,
      "engine_annual_reduction_seconds": 0.00041399989277124405,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.017663458362221718
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007624582969583571,
      "weather_seconds": 0.10170391702558845,
      "metric_reduction_seconds": 0.011482707923278213,
      "write_seconds": 0.025551291997544467,
      "total_seconds": 0.13918025000020862,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13918025000020862,
      "raw_export_seconds": 0.00993162498343736,
      "engine_upload_seconds": 5.7417e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006310833850875497,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013318208046257496,
      "full": 0.013610917027108371
    }
  },
  "elapsed_seconds": 62.12286704196595,
  "result_class": "passed"
}
```
