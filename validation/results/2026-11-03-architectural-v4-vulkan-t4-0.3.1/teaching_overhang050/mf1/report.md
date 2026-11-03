# Foton report

Status: **passed**

```json
{
  "scene": "teaching_overhang050",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_overhang050",
    "category": "teaching",
    "question": "What does a 0.5 m overhang remove from the base room?",
    "interactions": [
      "multiple_bounces",
      "overhang",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "544e519e9091079ac3c9813bb4389796978d8b4f3f8909903ff3c35f8db7ba2d",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 14403547847970506616,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 14403547847970506616,
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
    "model_sha256": "cb5086441c7e0fc253688640734dc38c6624544ccc07c8794637a12c71c58cea",
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
          "maximum": 0.0005182148888707161,
          "p95": 1.1456708307377977e-05,
          "p99": 9.922072058543563e-05
        },
        "bias_percent": -0.009715214964916043,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5389652743041011,
        "worst_index": [
          4,
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
          "maximum": 0.0004800371825695038,
          "p95": 5.8078047004528195e-05,
          "p99": 0.00016426946967840195
        },
        "bias_percent": -0.0374678759861102,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8623357688099065,
        "worst_index": [
          3,
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
          "maximum": 0.0005072802305221558,
          "p95": 4.4671329669654354e-05,
          "p99": 0.00013474468141794205
        },
        "bias_percent": 0.07892491144576613,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7203547096369257,
        "worst_index": [
          3,
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.001299123978242278,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.00018822994898073367,
                  "p99": 0.0005587639752775431
                },
                "candidate_energy": 6.680838394911916,
                "cvrmse_percent": 24.85097480639329,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.00906308613365904,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.680232959644854,
                "relative_energy_error_percent": 0.009063086133659038,
                "rms_normalized_rmse_percent": 5.6893746693652405,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014857519418001175,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0027848759200423956,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011637164279818535,
                  "p50": 0.0,
                  "p90": 3.5410746932029724e-05,
                  "p95": 0.00023646572954021366,
                  "p99": 0.0006451750523410738
                },
                "candidate_energy": 3.352646855416083,
                "cvrmse_percent": 57.46428827838517,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.26915461911376776,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.343647274330351,
                "relative_energy_error_percent": 0.26915461911376776,
                "rms_normalized_rmse_percent": 3.960161179853644,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0007676649838685989,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.00039605144411325455,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.11608304642141,
            "full": 246.07379199005663
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.77816702891141,
            "full": 231.5824159886688
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.4152080155909,
            "full": 235.5778330238536
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.50383293069899,
            "full": 258.4099159575999
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005406289710663259,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.993813440203667e-05,
                  "p99": 0.000219075009226799
                },
                "candidate_energy": 6.6700335925670515,
                "cvrmse_percent": 9.866831987522184,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.029280216868609897,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.671987164878374,
                "relative_energy_error_percent": 0.029280216868609897,
                "rms_normalized_rmse_percent": 2.2582478270638235,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001832363021094352,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002372991992160678,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007825605571269989,
                  "p50": 1.1499323093744351e-07,
                  "p90": 3.745980211533606e-05,
                  "p95": 0.00011791425058618152,
                  "p99": 0.00032439641654491425
                },
                "candidate_energy": 5.610601930047036,
                "cvrmse_percent": 17.858270090163245,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.005004420090417538,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.610882722189235,
                "relative_energy_error_percent": 0.005004420090417538,
                "rms_normalized_rmse_percent": 1.6642885861070729,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033432114869356155,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.032649554312229156,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.66241702716798,
            "full": 2280.0635839812458
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.05895909760147,
            "full": 2305.6945420103148
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.0516659701243,
            "full": 2238.711916957982
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.45554099883884,
            "full": 2250.578250037506
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043522100895643234,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.962602492421865e-05,
                  "p99": 0.00020971044432371855
                },
                "candidate_energy": 6.666235288817916,
                "cvrmse_percent": 8.867275592723121,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03673184781105161,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.668684819976988,
                "relative_energy_error_percent": 0.03673184781105161,
                "rms_normalized_rmse_percent": 2.0293460592059054,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007165554445236921,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007600775454193354,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008675884455442429,
                  "p50": 1.21218270976442e-07,
                  "p90": 3.7297955714166164e-05,
                  "p95": 0.00011146559845656137,
                  "p99": 0.0003016907721757889
                },
                "candidate_energy": 5.611898951590653,
                "cvrmse_percent": 17.23159323984473,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07875330824484092,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.607482873318652,
                "relative_energy_error_percent": 0.07875330824484092,
                "rms_normalized_rmse_percent": 1.6046799119785604,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0399051234126091,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.03903753496706486,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.79920799285173,
            "full": 2351.7753750784323
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.83270801976323,
            "full": 2434.7699590725824
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.81933306343853,
            "full": 2401.1180410161614
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.62112504709512,
            "full": 2383.880125009455
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002664311323314905,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.48115456290543e-05,
                  "p99": 0.00010544015094637871
                },
                "candidate_energy": 6.668607861751298,
                "cvrmse_percent": 5.0376895352316176,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.054679088640679586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.672256190628104,
                "relative_energy_error_percent": 0.054679088640679586,
                "rms_normalized_rmse_percent": 1.152938837813057,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0076737620402127504,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.00740733090788126,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006277933716773987,
                  "p50": 8.489340785899913e-08,
                  "p90": 2.416121424175799e-05,
                  "p95": 6.339477913570579e-05,
                  "p99": 0.00017061480320990086
                },
                "candidate_energy": 5.619463124504989,
                "cvrmse_percent": 10.289705881934022,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.108828247726085,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.613354209480153,
                "relative_energy_error_percent": 0.108828247726085,
                "rms_normalized_rmse_percent": 0.9590323250751188,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.049881404265761375,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.04925361089408398,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.2613749401644,
            "full": 4133.245749981143
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.86645900644362,
            "full": 4238.9690830605105
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.63541703671217,
            "full": 4149.911292013712
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.8317499253899,
            "full": 4228.973333025351
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
    "/content/suite-vulkan-0.3.1/teaching_overhang050/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 837.4199999962002,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2829.725709045306,
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
        "identifier": "teaching_overhang050_grid",
        "full_identifier": "teaching_overhang050_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.14278889034743195,
            "cvrmse_percent": 4.033844768987682,
            "rms_normalized_rmse_percent": 0.9230852338184815,
            "reference_energy": 6.666114801017102,
            "candidate_energy": 6.67563327237076,
            "relative_energy_error_percent": 0.14278889034743197,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.3772662542758495e-06,
              "p99": 6.904127076268196e-05,
              "maximum": 0.0004526840057224035
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 116,
              "rgb_channel": 0,
              "reference": 0.0028026108630001545,
              "candidate": 0.003255294868722558,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0449543091280977,
            "cvrmse_percent": 21.841414463124114,
            "rms_normalized_rmse_percent": 2.0377681987479614,
            "reference_energy": 5.620725906463338,
            "candidate_energy": 5.56199188889947,
            "relative_energy_error_percent": 1.0449543091280977,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5964189376281865e-07,
              "p90": 4.0106926462613046e-05,
              "p95": 6.270112571655768e-05,
              "p99": 0.00017013703472912312,
              "maximum": 0.001885008066892624
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04888574779033661,
              "candidate": 0.047000739723443985,
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
            "nmbe_percent": -0.40055493012330234,
            "cvrmse_percent": 9.945740730903449,
            "rms_normalized_rmse_percent": 2.028425092668452,
            "reference_energy": 12.28684070748044,
            "candidate_energy": 12.23762516127023,
            "relative_energy_error_percent": 0.4005549301233023,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.6342193848449824e-07,
              "p90": 4.056209581904113e-05,
              "p95": 6.203880766406652e-05,
              "p99": 0.00015695812180638313,
              "maximum": 0.001885008066892624
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04888574779033661,
              "candidate": 0.047000739723443985,
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
        "identifier": "teaching_overhang050_grid",
        "full_identifier": "teaching_overhang050_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.14278889034743195,
            "cvrmse_percent": 4.033844768987682,
            "rms_normalized_rmse_percent": 0.9230852338184815,
            "reference_energy": 6.666114801017102,
            "candidate_energy": 6.67563327237076,
            "relative_energy_error_percent": 0.14278889034743197,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.3772662542758495e-06,
              "p99": 6.904127076268196e-05,
              "maximum": 0.0004526840057224035
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 116,
              "rgb_channel": 0,
              "reference": 0.0028026108630001545,
              "candidate": 0.003255294868722558,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 65.40905423456714,
            "cvrmse_percent": 404.30496535409253,
            "rms_normalized_rmse_percent": 27.981698947237245,
            "reference_energy": 3.3625679770902934,
            "candidate_energy": 5.56199188889947,
            "relative_energy_error_percent": 65.40905423456714,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00027092359960079193,
              "p95": 0.00036779000074602634,
              "p99": 0.0006344218272715807,
              "maximum": 0.011962749063968658
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02526818960905075,
              "candidate": 0.03723093867301941,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.026246437717166,
            "cvrmse_percent": 135.57902003681048,
            "rms_normalized_rmse_percent": 27.985322540371524,
            "reference_energy": 10.028682778107395,
            "candidate_energy": 12.23762516127023,
            "relative_energy_error_percent": 22.026246437717166,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002714351958275074,
              "p95": 0.00036667123495135454,
              "p99": 0.0006317533552646637,
              "maximum": 0.011962749063968658
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02526818960905075,
              "candidate": 0.03723093867301941,
              "position": [
                5.5,
                2.5,
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
      "bias_percent": 0.2334149297553239,
      "rms_normalized_error_percent": 0.2789877321913849,
      "absolute_error": {
        "p95": 0.10816352085436431,
        "p99": 0.1258631448059505,
        "maximum": 0.12866207497816617
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.48747114868296,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2789877321913849
    },
    "overcast": {
      "bias_percent": 0.1992329598853386,
      "rms_normalized_error_percent": 0.25429319181451365,
      "absolute_error": {
        "p95": 0.07319498062133789,
        "p99": 0.0858455181121826,
        "maximum": 0.08864498138427734
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.050250053405762,
      "reference_fraction_of_uniform": 0.5968687534332275,
      "rms_normalized_to_uniform_percent": 0.16551119969008823
    },
    "horizon": {
      "bias_percent": 0.8191872597463682,
      "rms_normalized_error_percent": 2.142728779508063,
      "absolute_error": {
        "p95": 0.08851839325440863,
        "p99": 0.1032916009459602,
        "maximum": 0.10500660030925202
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6324019107309133,
      "reference_fraction_of_uniform": 0.12103098443997902,
      "rms_normalized_to_uniform_percent": 0.1730453173546885
    },
    "north": {
      "bias_percent": -99.61749578342588,
      "rms_normalized_error_percent": 99.99727066123468,
      "absolute_error": {
        "p95": 0.00014722361447638832,
        "p99": 0.0002738035022048277,
        "maximum": 0.0003346964076627046
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.7092642994830385e-05,
      "reference_fraction_of_uniform": 2.0087265966139967e-06,
      "rms_normalized_to_uniform_percent": 0.00032418678526807573
    },
    "east": {
      "bias_percent": 0.12085228715010954,
      "rms_normalized_error_percent": 0.3925177596145731,
      "absolute_error": {
        "p95": 0.03193020820617676,
        "p99": 0.052970361709594696,
        "maximum": 0.06136608123779297
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8004491329193115,
      "reference_fraction_of_uniform": 0.2076333612203598,
      "rms_normalized_to_uniform_percent": 0.09107198438838651
    },
    "south": {
      "bias_percent": 0.2867081956257475,
      "rms_normalized_error_percent": 0.33764831577996285,
      "absolute_error": {
        "p95": 0.09798359870910645,
        "p99": 0.10118803977966308,
        "maximum": 0.1016082763671875
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.935405731201172,
      "reference_fraction_of_uniform": 0.7366396188735962,
      "rms_normalized_to_uniform_percent": 0.2349720770126674
    },
    "west": {
      "bias_percent": 0.13674843071549123,
      "rms_normalized_error_percent": 0.3316508299035317,
      "absolute_error": {
        "p95": 0.029062777757644653,
        "p99": 0.03189180195331573,
        "maximum": 0.03303629159927368
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7179903984069824,
      "reference_fraction_of_uniform": 0.20151963829994202,
      "rms_normalized_to_uniform_percent": 0.0746853430769918
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
        "identifier": "teaching_overhang050_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.12347508826166868,
          "cvrmse_percent": 1.6011562426330475,
          "absolute_error_percentiles_lux": {
            "p50": 2.776641845703125,
            "p90": 25.83167724609375,
            "p95": 39.08402709960934,
            "p99": 77.9525122070311
          },
          "maximum_absolute_error_lux": 358.756591796875,
          "worst": {
            "sensor_index": 15,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 6250.5,
            "foton_lux": 4147.490234375,
            "radiance_lux": 3788.733642578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24226027397260275,
            "maximum_error_percentage_points": 1.1272602739726025,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09692590887144527,
            "maximum_error_percentage_points": 0.5309900159051324,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06156773211567712,
            "maximum_error_percentage_points": 0.21999999999999886,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06818873668188709,
            "maximum_error_percentage_points": 0.21780821917808169,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03447869101978668,
            "maximum_error_percentage_points": 0.16164383561643836,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
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
      "maximum_error_percentage_points": 0.0049866224315024965,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.0049866224315024965,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.44664642099814955,
      "weather_seconds": 0.39397198100050446,
      "metric_reduction_seconds": 0.33034051099821227,
      "write_seconds": 0.0630543890001718,
      "total_seconds": 0.7892134150024503,
      "cold_end_to_end_seconds": 1.2358598360006,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.04295923199970275,
      "engine_upload_seconds": 0.015143363,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.012536822,
      "engine_annual_reduction_seconds": 0.006844178,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.012536822
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.44664642099814955,
      "weather_seconds": 0.30066062200057786,
      "metric_reduction_seconds": 0.1558523849962512,
      "write_seconds": 0.020594918001734186,
      "total_seconds": 0.4774646610021591,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4774646610021591,
      "raw_export_seconds": 0.00861734600039199,
      "engine_upload_seconds": 0.015953414,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.5e-08,
      "engine_annual_reduction_seconds": 0.006887598,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01420510999741964,
      "full": 0.02181675299652852
    }
  },
  "elapsed_seconds": 3.0634353599962196,
  "result_class": "passed"
}
```
