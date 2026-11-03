# Foton report

Status: **incomplete**

```json
{
  "scene": "deep_reflective",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "deep_reflective",
    "category": "materials",
    "question": "Does reflected light reach the rear of a deep bright room?",
    "interactions": [
      "deep_plan",
      "multiple_bounces",
      "high_reflectance"
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
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "0cba50819b296cea2cf0f9d0dfab599041214948d3178df3038e8637c5d342d4",
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
      "scene_fingerprint": 17209437186486154619,
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
      "scene_fingerprint": 17209437186486154619,
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "f183c02c2d6f97c824fe68b25c00f3360cca9d3a391b83a30066435724d73d2a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "bc8dc63ed3373f853fc8759757ef0d2a72678922d616cafd9d7d27a1c69847a7",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 0.0,
          "p99": 3.773719072341919e-06
        },
        "bias_percent": -0.021064643331798805,
        "identifier": "deep_reflective_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7716788117364117,
        "worst_index": [
          35,
          543,
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
          "maximum": 0.00294388085603714,
          "p95": 3.886465419782323e-05,
          "p99": 8.87115893419832e-05
        },
        "bias_percent": 3.6101597539909998,
        "identifier": "deep_reflective_grid",
        "passed": false,
        "rms_normalized_error_percent": 4.014465652750799,
        "worst_index": [
          43,
          0,
          0
        ]
      }
    ],
    "passed": false
  },
  "sample_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0011653602123260498,
          "p95": 3.0817983861197516e-05,
          "p99": 7.032928988337517e-05
        },
        "bias_percent": -0.02284574598705074,
        "identifier": "deep_reflective_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8965953788172335,
        "worst_index": [
          70,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005172655219212174,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013998005306348205
                },
                "candidate_energy": 6.252826724798069,
                "cvrmse_percent": 52.38214015488951,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1432795468105873,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.2438805210840655,
                "relative_energy_error_percent": 0.1432795468105873,
                "rms_normalized_rmse_percent": 7.37432321934884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016927134711295366,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.002209978993050754,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001218404620885849,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0648680563460739e-05,
                  "p99": 0.00023100839462131262
                },
                "candidate_energy": 3.9190791447106506,
                "cvrmse_percent": 145.15990013140035,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5663380283388931,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.941400796269175,
                "relative_energy_error_percent": 0.5663380283388931,
                "rms_normalized_rmse_percent": 4.919604104029714,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030915754847228527,
                  "global_sensor_index": 59,
                  "local_sensor_index": 59,
                  "reference": 0.029697350226342678,
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.00204093847424,
            "full": 361.9339580181986
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.76337503176183,
            "full": 349.2792920442298
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.8634159490466,
            "full": 355.9803329408169
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.12870799098164,
            "full": 361.4137909607962
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003469179500825703,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010764249600470066
                },
                "candidate_energy": 6.245015083112776,
                "cvrmse_percent": 38.09794933515179,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0025409034791922403,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.245173766950302,
                "relative_energy_error_percent": 0.0025409034791922403,
                "rms_normalized_rmse_percent": 5.37222393913213,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022594049805775285,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.0019124870304949582,
                  "rgb_channel": 0,
                  "sky_patch_index": 204
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0018379278481006622,
                  "p50": 7.526022471893157e-08,
                  "p90": 3.1248178856913e-05,
                  "p95": 5.226216890150631e-05,
                  "p99": 0.00017140188720077276
                },
                "candidate_energy": 16.709618586438914,
                "cvrmse_percent": 29.739675118040797,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09903810024038183,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 16.693086071122583,
                "relative_energy_error_percent": 0.09903810024038182,
                "rms_normalized_rmse_percent": 1.9262449368207946,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07327321171760559,
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "reference": 0.07511113956570625,
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.75812498200685,
            "full": 4613.521958002821
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.5293329572305,
            "full": 4669.969332986511
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.33049991168082,
            "full": 4696.860500029288
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.3727500634268,
            "full": 4713.059584028088
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00033588544465601444,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011127276229672134
                },
                "candidate_energy": 6.248987639788538,
                "cvrmse_percent": 38.25960224534519,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0841418276029135,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.243734047850012,
                "relative_energy_error_percent": 0.0841418276029135,
                "rms_normalized_rmse_percent": 5.390894673488214,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018359179957769811,
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "reference": 0.0015000325511209667,
                  "rgb_channel": 0,
                  "sky_patch_index": 157
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0015720892697572708,
                  "p50": 7.908004917567268e-08,
                  "p90": 3.1850786399445496e-05,
                  "p95": 5.2815064555034016e-05,
                  "p99": 0.00015549920499324799
                },
                "candidate_energy": 17.51044524773193,
                "cvrmse_percent": 27.318121828882592,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20567149238435184,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.546533464971056,
                "relative_energy_error_percent": 0.20567149238435187,
                "rms_normalized_rmse_percent": 1.7948096670178681,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04623685963451862,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.04466477036476135,
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.36166699882597,
            "full": 5315.650083008222
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.29154192563146,
            "full": 5292.21954208333
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 182.44083295576274,
            "full": 5362.475667032413
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.22758297715336,
            "full": 5395.881042000838
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
            "identifier": "deep_reflective_grid",
            "sensor_count": 72,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018574448768049479,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.0969450967386365e-05
                },
                "candidate_energy": 6.247565967863011,
                "cvrmse_percent": 19.298653290300027,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.017156146622356885,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.246494310140406,
                "relative_energy_error_percent": 0.01715614662235689,
                "rms_normalized_rmse_percent": 2.7223317177693493,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016288745100609958,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.0018146189977414906,
                  "rgb_channel": 0,
                  "sky_patch_index": 153
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008962824940681458,
                  "p50": 5.849637751964565e-08,
                  "p90": 2.19704961637035e-05,
                  "p95": 3.55600081093141e-05,
                  "p99": 9.129848331212997e-05
                },
                "candidate_energy": 17.527309048485627,
                "cvrmse_percent": 17.118533900426847,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05617800040390934,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.517468085193972,
                "relative_energy_error_percent": 0.056178000403909335,
                "rms_normalized_rmse_percent": 1.1225661975742507,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07514002546668053,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.07603630796074867,
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 300.9385420009494,
            "full": 10599.704375024885
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 297.47345799114555,
            "full": 10428.18408308085
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 277.06591703463346,
            "full": 10547.39541595336
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 287.1349169872701,
            "full": 10612.100041937083
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/deep_reflective/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11989.527166937478,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_reflective/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 45521.57874999102,
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
    "passed": false,
    "matrix_shape": [
      72,
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
        "identifier": "deep_reflective_grid",
        "full_identifier": "deep_reflective_grid",
        "start_sensor_index": 0,
        "sensor_count": 72,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03007472284244326,
            "cvrmse_percent": 3.0372608208199185,
            "rms_normalized_rmse_percent": 0.4285512398289285,
            "reference_energy": 6.248309748263523,
            "candidate_energy": 6.246430586424395,
            "relative_energy_error_percent": 0.030074722842443263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.843007678166032e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -5.509465118859958,
            "cvrmse_percent": 79.11790315518154,
            "rms_normalized_rmse_percent": 5.189261744594585,
            "reference_energy": 17.52110886860662,
            "candidate_energy": 16.55578948705326,
            "relative_energy_error_percent": 5.509465118859959,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.83577762067489e-08,
              "p90": 2.827194384735776e-05,
              "p95": 4.177452756266553e-05,
              "p99": 7.658003596588969e-05,
              "maximum": 0.004113771021366119
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08001472800970078,
              "candidate": 0.07590095698833466,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -4.069087927569365,
            "cvrmse_percent": 58.31960223071371,
            "rms_normalized_rmse_percent": 5.18922297900066,
            "reference_energy": 23.769418616870144,
            "candidate_energy": 22.802220073477656,
            "relative_energy_error_percent": 4.069087927569365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.83094273262941e-08,
              "p90": 2.8258771635591984e-05,
              "p95": 4.185055258858479e-05,
              "p99": 7.660652045160532e-05,
              "maximum": 0.004113771021366119
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08001472800970078,
              "candidate": 0.07590095698833466,
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
      72,
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
        "identifier": "deep_reflective_grid",
        "full_identifier": "deep_reflective_grid",
        "start_sensor_index": 0,
        "sensor_count": 72,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03007472284244326,
            "cvrmse_percent": 3.0372608208199185,
            "rms_normalized_rmse_percent": 0.4285512398289285,
            "reference_energy": 6.248309748263523,
            "candidate_energy": 6.246430586424395,
            "relative_energy_error_percent": 0.030074722842443263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.843007678166032e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 321.2364836317634,
            "cvrmse_percent": 3787.070734324711,
            "rms_normalized_rmse_percent": 128.09445459312764,
            "reference_energy": 3.9302838501344066,
            "candidate_energy": 16.55578948705326,
            "relative_energy_error_percent": 321.2364836317634,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00020537000091280788,
              "p95": 0.00027637815655907606,
              "p99": 0.0004008302930742502,
              "maximum": 0.04270625859498978
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 71,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019015222787857056,
              "candidate": 0.06172148138284683,
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
            "nmbe_percent": 124.02132330999673,
            "cvrmse_percent": 1462.3047805834108,
            "rms_normalized_rmse_percent": 128.09396518628856,
            "reference_energy": 10.17859359839793,
            "candidate_energy": 22.802220073477656,
            "relative_energy_error_percent": 124.02132330999673,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002054782471532235,
              "p95": 0.0002762260002782566,
              "p99": 0.0004000358749181032,
              "maximum": 0.04270625859498978
            },
            "worst": {
              "global_sensor_index": 71,
              "local_sensor_index": 71,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019015222787857056,
              "candidate": 0.06172148138284683,
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
      "bias_percent": -3.0339836967055485,
      "rms_normalized_error_percent": 1.9465095586194692,
      "absolute_error": {
        "p95": 0.45802970969937773,
        "p99": 0.47470940875709144,
        "maximum": 0.4804114625525271
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.470365791691709,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 1.9465095586194692
    },
    "overcast": {
      "bias_percent": -2.9361862928019336,
      "rms_normalized_error_percent": 1.6952129644437999,
      "absolute_error": {
        "p95": 0.2821157217025757,
        "p99": 0.2938607501983643,
        "maximum": 0.2959442138671875
      },
      "worst_index": [
        55
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.057438373565674,
      "reference_fraction_of_uniform": 0.6152758002281189,
      "rms_normalized_to_uniform_percent": 1.1621654135028479
    },
    "horizon": {
      "bias_percent": -4.8911594715192095,
      "rms_normalized_error_percent": 5.070181185267292,
      "absolute_error": {
        "p95": 0.16301857852293816,
        "p99": 0.17710726586626344,
        "maximum": 0.17731868203981027
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.0547575761602177,
      "reference_fraction_of_uniform": 0.17913618566973105,
      "rms_normalized_to_uniform_percent": 0.5859643635373631
    },
    "north": {
      "bias_percent": -73.10313561101695,
      "rms_normalized_error_percent": 100.73661131466702,
      "absolute_error": {
        "p95": 0.00013119932773406618,
        "p99": 0.00026994000189006377,
        "maximum": 0.0003248496213927865
      },
      "worst_index": [
        58
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.8312373615335673e-05,
      "reference_fraction_of_uniform": 2.4683060928509803e-06,
      "rms_normalized_to_uniform_percent": 0.00035677448685758454
    },
    "east": {
      "bias_percent": -3.023645385834351,
      "rms_normalized_error_percent": 1.8781211132714533,
      "absolute_error": {
        "p95": 0.1106269955635071,
        "p99": 0.117478506565094,
        "maximum": 0.11797499656677246
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2042083740234375,
      "reference_fraction_of_uniform": 0.19216549396514893,
      "rms_normalized_to_uniform_percent": 0.3839332423010875
    },
    "south": {
      "bias_percent": -2.943150892753055,
      "rms_normalized_error_percent": 2.0244511846407653,
      "absolute_error": {
        "p95": 0.3215619206428528,
        "p99": 0.32924498558044435,
        "maximum": 0.32947587966918945
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.133899688720703,
      "reference_fraction_of_uniform": 0.7091229557991028,
      "rms_normalized_to_uniform_percent": 1.3454376359674776
    },
    "west": {
      "bias_percent": -3.013349463734147,
      "rms_normalized_error_percent": 1.8747241802951564,
      "absolute_error": {
        "p95": 0.1035886108875275,
        "p99": 0.11518813610076911,
        "maximum": 0.12367129325866699
      },
      "worst_index": [
        66
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2285473346710205,
      "reference_fraction_of_uniform": 0.19428738951683044,
      "rms_normalized_to_uniform_percent": 0.38645424899219405
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
        "identifier": "deep_reflective_grid",
        "sensor_count": 72,
        "illuminance": {
          "nmbe_percent": -2.840495445833782,
          "cvrmse_percent": 5.551239970781275,
          "absolute_error_percentiles_lux": {
            "p50": 15.196044921875,
            "p90": 90.5552978515625,
            "p95": 126.31586608886715,
            "p99": 213.04130371093564
          },
          "maximum_absolute_error_lux": 585.3251953125,
          "worst": {
            "sensor_index": 71,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 6252.5,
            "foton_lux": 3012.021484375,
            "radiance_lux": 3597.3466796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.228645357686453,
            "maximum_error_percentage_points": 4.763835616438357,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.7367977152084292,
            "maximum_error_percentage_points": 1.9122988167745092,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5703291476407915,
            "maximum_error_percentage_points": 1.3716438356164353,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6589231354642313,
            "maximum_error_percentage_points": 1.533698630136982,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.23100076103500772,
            "maximum_error_percentage_points": 1.5573972602739712,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 88.88888888888889,
          "radiance_percent": 100.0,
          "difference_percentage_points": 11.111111111111114,
          "tolerance_percentage_points": 2.0,
          "ambiguous_sensor_count": 8,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049700342465826,
      "metrics": {
        "da": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.0049700342465826,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "deep_reflective_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "deep_reflective_grid",
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
      "study_preparation_seconds": 0.0068377499701455235,
      "weather_seconds": 0.09594662499148399,
      "metric_reduction_seconds": 0.18427995790261775,
      "write_seconds": 0.03456687496509403,
      "total_seconds": 0.3149251249851659,
      "cold_end_to_end_seconds": 0.3217628749553114,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010438499972224236,
      "engine_upload_seconds": 0.000985333,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.12492029170971364,
      "engine_annual_reduction_seconds": 0.0035755833378061652,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.12492029170971364
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0068377499701455235,
      "weather_seconds": 0.09787170903291553,
      "metric_reduction_seconds": 0.04846575006376952,
      "write_seconds": 0.028116167057305574,
      "total_seconds": 0.17482220905367285,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.17482220905367285,
      "raw_export_seconds": 0.010084165958687663,
      "engine_upload_seconds": 9.0209e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.003054041648283601,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011994959088042378,
      "full": 0.12848620803561062
    }
  },
  "elapsed_seconds": 1.6757602919824421,
  "result_class": "unstable_reference"
}
```
