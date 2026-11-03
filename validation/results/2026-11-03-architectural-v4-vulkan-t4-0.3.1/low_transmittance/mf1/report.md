# Foton report

Status: **passed**

```json
{
  "scene": "low_transmittance",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "low_transmittance",
    "category": "materials",
    "question": "Does low-transmittance glass attenuate light without turning opaque?",
    "interactions": [
      "glazing_attenuation"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c13a18a8acb38fc2db3dbc451e19f06b94b06cdd7bc48fb4bda9655a6e361ec3",
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
      "scene_fingerprint": 13137537828487568414,
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
      "scene_fingerprint": 13137537828487568414,
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
    "model_sha256": "be5131aca161898e7aec5d894595ac294d20221c42adb5b2f90f827262a09658",
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
          "maximum": 0.00010101217776536942,
          "p95": 1.1401367373764342e-06,
          "p99": 2.6175461243838072e-05
        },
        "bias_percent": -0.06844817739779885,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0621844589539986,
        "worst_index": [
          9,
          72,
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
          "maximum": 0.00013550790026783943,
          "p95": 1.3259878141980126e-05,
          "p99": 4.397728480398655e-05
        },
        "bias_percent": 0.09521352752968205,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1240829105879064,
        "worst_index": [
          20,
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
          "maximum": 0.00011372752487659454,
          "p95": 1.1550987255759533e-05,
          "p99": 3.743689740076661e-05
        },
        "bias_percent": 0.011152891998804764,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9448734706117962,
        "worst_index": [
          33,
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019249925389885902,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.5558069571852666e-05,
                  "p99": 7.74547370383516e-05
                },
                "candidate_energy": 1.7393552790445028,
                "cvrmse_percent": 12.951643391595494,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.14703109114209773,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7419164377897687,
                "relative_energy_error_percent": 0.14703109114209773,
                "rms_normalized_rmse_percent": 2.682848408152348,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004180361516773701,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.00437286077067256,
                  "rgb_channel": 0,
                  "sky_patch_index": 120
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00032511295285075903,
                  "p50": 0.0,
                  "p90": 5.660584974975791e-06,
                  "p95": 3.9205975190270646e-05,
                  "p99": 0.0001455234014429152
                },
                "candidate_energy": 0.6033405414843998,
                "cvrmse_percent": 72.5453356020243,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5633091892652283,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5999609065657161,
                "relative_energy_error_percent": 0.5633091892652283,
                "rms_normalized_rmse_percent": 4.051318997089338,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00023773510474711657,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 8.737784810364246e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.17287498805672,
            "full": 228.2025000313297
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.75037505663931,
            "full": 225.08620808366686
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.11483303364366,
            "full": 224.07416603527963
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.22633300349116,
            "full": 240.9793749684468
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00014504848513752222,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.4237485083867735e-05,
                  "p99": 5.7938508689403534e-05
                },
                "candidate_energy": 1.7404942026178105,
                "cvrmse_percent": 9.315891505251175,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10061175775790161,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.738744820890588,
                "relative_energy_error_percent": 0.10061175775790161,
                "rms_normalized_rmse_percent": 1.9280878311059566,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0011933940113522112,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0013384424964897335,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00023406464606523514,
                  "p50": 6.286436438074361e-08,
                  "p90": 9.173540092888288e-06,
                  "p95": 2.5579624343663358e-05,
                  "p99": 9.084295015782118e-05
                },
                "candidate_energy": 1.1081778935573041,
                "cvrmse_percent": 24.27477575769036,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.30668313927348767,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1115869432907424,
                "relative_energy_error_percent": 0.30668313927348767,
                "rms_normalized_rmse_percent": 2.1228314819438676,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0067485731560736895,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.006514508510008454,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.93462499883026,
            "full": 2234.6399169182405
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.40283309482038,
            "full": 2218.298416933976
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.09679106250405,
            "full": 2200.3171669784933
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.31299997866154,
            "full": 2234.8450829740614
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001275109825655818,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.4995555829955255e-05,
                  "p99": 5.346030229702592e-05
                },
                "candidate_energy": 1.739907119387226,
                "cvrmse_percent": 9.31766357658123,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.028525747013347938,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7394109394231236,
                "relative_energy_error_percent": 0.028525747013347938,
                "rms_normalized_rmse_percent": 1.931435702533156,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002303591463714838,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0021760804811492562,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00021699321223422885,
                  "p50": 5.973097216838141e-08,
                  "p90": 8.397120836889371e-06,
                  "p95": 2.534015584387811e-05,
                  "p99": 8.711754344403744e-05
                },
                "candidate_energy": 1.1119844087473751,
                "cvrmse_percent": 23.183858783998286,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1027038534121561,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1131276337206018,
                "relative_energy_error_percent": 0.1027038534121561,
                "rms_normalized_rmse_percent": 2.0280615910527806,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -4.376715514808893e-05,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.00017322605708613992,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.8574579982087,
            "full": 2367.4617080250755
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.78008302953094,
            "full": 2393.3552500093356
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.75320900883526,
            "full": 2359.552707988769
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.94966698717326,
            "full": 2396.9996250234544
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 6.564299110323191e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.17311268090269e-06,
                  "p99": 2.6416440960019827e-05
                },
                "candidate_energy": 1.7391974630286313,
                "cvrmse_percent": 4.623841839484263,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.002752331349247602,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.739149595869094,
                "relative_energy_error_percent": 0.002752331349247602,
                "rms_normalized_rmse_percent": 0.9580335447360429,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034161414951086044,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0034817844862118363,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00014594732783734798,
                  "p50": 5.000000768973223e-08,
                  "p90": 5.707101081497967e-06,
                  "p95": 1.3876332013751369e-05,
                  "p99": 4.72519313916564e-05
                },
                "candidate_energy": 1.1118551560985566,
                "cvrmse_percent": 13.073992409920072,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.26989295753690146,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.114864095779172,
                "relative_energy_error_percent": 0.26989295753690146,
                "rms_normalized_rmse_percent": 1.1443888221563634,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.006211883155629039,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.006357830483466387,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.31241694372147,
            "full": 4210.841708001681
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.97366604488343,
            "full": 4224.044666974805
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.54899993818253,
            "full": 4193.743124953471
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.22779199946672,
            "full": 4131.345249945298
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
    "/content/suite-vulkan-0.3.1/low_transmittance/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 806.9478750694543,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2805.685375002213,
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
        "identifier": "low_transmittance_grid",
        "full_identifier": "low_transmittance_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03703990782219166,
            "cvrmse_percent": 3.3058963265175874,
            "rms_normalized_rmse_percent": 0.6847166498081896,
            "reference_energy": 1.7389886154214764,
            "candidate_energy": 1.738344495641286,
            "relative_energy_error_percent": 0.03703990782219166,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 9.246199624612858e-07,
              "p99": 1.5032477676868439e-05,
              "maximum": 8.990475907921791e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.0007211664342321455,
              "candidate": 0.0008110711933113635,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4333495294739622,
            "cvrmse_percent": 27.96840139540112,
            "rms_normalized_rmse_percent": 2.447465942445555,
            "reference_energy": 1.1135445408857176,
            "candidate_energy": 1.0975835554484492,
            "relative_energy_error_percent": 1.4333495294739622,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2499999968440534e-07,
              "p90": 1.174774115497712e-05,
              "p95": 1.7112588102463627e-05,
              "p99": 4.065211396664381e-05,
              "maximum": 0.00044754426926374435
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007854684256017208,
              "candidate": 0.007407139986753464,
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
            "nmbe_percent": -0.5821178688403198,
            "cvrmse_percent": 10.869160665777532,
            "rms_normalized_rmse_percent": 2.4365096157239887,
            "reference_energy": 2.852533156307194,
            "candidate_energy": 2.835928051089735,
            "relative_energy_error_percent": 0.5821178688403199,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.257962836120896e-07,
              "p90": 1.1812429875135422e-05,
              "p95": 1.7390908033121355e-05,
              "p99": 3.936036955565214e-05,
              "maximum": 0.00044754426926374435
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007854684256017208,
              "candidate": 0.007407139986753464,
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
        "identifier": "low_transmittance_grid",
        "full_identifier": "low_transmittance_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03703990782219166,
            "cvrmse_percent": 3.3058963265175874,
            "rms_normalized_rmse_percent": 0.6847166498081896,
            "reference_energy": 1.7389886154214764,
            "candidate_energy": 1.738344495641286,
            "relative_energy_error_percent": 0.03703990782219166,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 9.246199624612858e-07,
              "p99": 1.5032477676868439e-05,
              "maximum": 8.990475907921791e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.0007211664342321455,
              "candidate": 0.0008110711933113635,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.93058884946724,
            "cvrmse_percent": 439.1922665862095,
            "rms_normalized_rmse_percent": 24.660730262694933,
            "reference_energy": 0.6032979733587354,
            "candidate_energy": 1.0975835554484492,
            "relative_energy_error_percent": 81.93058884946723,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.63876417092979e-05,
              "p95": 9.069390071090307e-05,
              "p99": 0.00018253520829603076,
              "maximum": 0.0022952849976718426
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0031197750940918922,
              "candidate": 0.005415060091763735,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.07519484055092,
            "cvrmse_percent": 113.11803674341914,
            "rms_normalized_rmse_percent": 24.659897832316272,
            "reference_energy": 2.342286588780212,
            "candidate_energy": 2.835928051089735,
            "relative_energy_error_percent": 21.075194840550918,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.607999966945499e-05,
              "p95": 9.014769530040212e-05,
              "p99": 0.0001784486521501094,
              "maximum": 0.0022952849976718426
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0031197750940918922,
              "candidate": 0.005415060091763735,
              "position": [
                1.5,
                5.5,
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
      "bias_percent": 0.05454500676629835,
      "rms_normalized_error_percent": 0.25431056808496083,
      "absolute_error": {
        "p95": 0.03066126278320097,
        "p99": 0.037960763069295696,
        "maximum": 0.0388543124332521
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4831879289601444,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.25431056808496083
    },
    "overcast": {
      "bias_percent": -0.009173258673532275,
      "rms_normalized_error_percent": 0.21116254236318716,
      "absolute_error": {
        "p95": 0.01840224862098694,
        "p99": 0.019566091895103454,
        "maximum": 0.020101547241210938
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.194040536880493,
      "reference_fraction_of_uniform": 0.6298943758010864,
      "rms_normalized_to_uniform_percent": 0.14683953655739232
    },
    "horizon": {
      "bias_percent": 0.7201317802300552,
      "rms_normalized_error_percent": 2.1850069142761783,
      "absolute_error": {
        "p95": 0.020102371571186203,
        "p99": 0.023727808066342664,
        "maximum": 0.02424731924118534
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3421079624894572,
      "reference_fraction_of_uniform": 0.09821691205492566,
      "rms_normalized_to_uniform_percent": 0.13422669548205737
    },
    "north": {
      "bias_percent": -94.20175464399206,
      "rms_normalized_error_percent": 101.16323548178218,
      "absolute_error": {
        "p95": 0.00012793411406164523,
        "p99": 0.0001813068825867958,
        "maximum": 0.00019222630362492055
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.4187766030081548e-05,
      "reference_fraction_of_uniform": 6.944146207388258e-06,
      "rms_normalized_to_uniform_percent": 0.0008483895148832521
    },
    "east": {
      "bias_percent": -0.12535185848125208,
      "rms_normalized_error_percent": 0.43252416644144204,
      "absolute_error": {
        "p95": 0.010882541537284851,
        "p99": 0.014194777607917779,
        "maximum": 0.01588308811187744
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6898199915885925,
      "reference_fraction_of_uniform": 0.19804272055625916,
      "rms_normalized_to_uniform_percent": 0.08968120834620766
    },
    "south": {
      "bias_percent": 0.16417725221760177,
      "rms_normalized_error_percent": 0.3112079975126506,
      "absolute_error": {
        "p95": 0.03213164210319519,
        "p99": 0.03348555564880371,
        "maximum": 0.03366446495056152
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.469149589538574,
      "reference_fraction_of_uniform": 0.708876371383667,
      "rms_normalized_to_uniform_percent": 0.2087949362576217
    },
    "west": {
      "bias_percent": -0.0595259762405938,
      "rms_normalized_error_percent": 0.40984069770514014,
      "absolute_error": {
        "p95": 0.008505739271640778,
        "p99": 0.010805504024028774,
        "maximum": 0.011813610792160034
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6685951352119446,
      "reference_fraction_of_uniform": 0.19194920361042023,
      "rms_normalized_to_uniform_percent": 0.0816922207740482
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
        "identifier": "low_transmittance_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.07806169155696203,
          "cvrmse_percent": 1.781792824228533,
          "absolute_error_percentiles_lux": {
            "p50": 0.8471603393554688,
            "p90": 7.845349121093751,
            "p95": 11.490586853027326,
            "p99": 21.22145645141598
          },
          "maximum_absolute_error_lux": 108.674560546875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 1441.2816162109375,
            "radiance_lux": 1549.9561767578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15499619482496169,
            "maximum_error_percentage_points": 0.4695890410958903,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.25729781802812723,
            "maximum_error_percentage_points": 0.8320103959785747,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4182077625570776,
            "maximum_error_percentage_points": 1.6993150684931493,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4228424657534248,
            "maximum_error_percentage_points": 1.6993150684931528,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006807458143074673,
            "maximum_error_percentage_points": 0.05575342465753441,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
      "maximum_error_percentage_points": 0.004888966181511023,
      "metrics": {
        "da": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004888966181511023,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
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
      "study_preparation_seconds": 0.3662211920018308,
      "weather_seconds": 0.2378094619998592,
      "metric_reduction_seconds": 0.15626148599403678,
      "write_seconds": 0.03251499900216004,
      "total_seconds": 0.42694423800276127,
      "cold_end_to_end_seconds": 0.793165430004592,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.020501922997937072,
      "engine_upload_seconds": 0.014012,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010643814,
      "engine_annual_reduction_seconds": 0.007418329,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010643814
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3662211920018308,
      "weather_seconds": 0.25561068800016074,
      "metric_reduction_seconds": 0.14011576100165257,
      "write_seconds": 0.022228670000913553,
      "total_seconds": 0.41835603999788873,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.41835603999788873,
      "raw_export_seconds": 0.01017349000176182,
      "engine_upload_seconds": 0.01393613,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.8e-08,
      "engine_annual_reduction_seconds": 0.006973063,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013676825001311954,
      "full": 0.02258852399972966
    }
  },
  "elapsed_seconds": 2.467522879000171,
  "result_class": "passed"
}
```
